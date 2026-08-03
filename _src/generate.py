#!/usr/bin/env python3
"""Build the static site from a Notion Markdown/CSV export.

    python3 _src/generate.py path/to/ExportBlock-*.zip
    python3 _src/generate.py path/to/unzipped-export-dir

Every exported page becomes one HTML file, every exported attachment is copied
next to the page that references it, and the sidebar/nav mirrors the Notion
hierarchy 1:1.  Output goes to the repo root so GitHub Pages serves it as-is.
"""
import html
import json
import os
import pathlib
import re
import shutil
import sys
import tempfile
import unicodedata
import urllib.parse
import zipfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import mdlite  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent

SITE_TITLE = "the-grizzly-bear"
SITE_SUB = "Cybersecurity Notes & CTF Writeups"
SITE_DESC = ("Cybersecurity notes, CTF writeups and reference material — hands-on work across "
             "capture-the-flag competitions, HackTheBox labs, reverse-engineering challenges "
             "and blue-team fundamentals.")

# Strings that must not reach the public site.  The Notion root page is titled with
# the account holder's real name, so that title is redacted automatically (it is
# never written into this file).  Extra patterns can go in _src/redactions.txt, one
# `pattern = replacement` per line — that file is gitignored for the same reason.
REDACTIONS = []
REDACTION_FILE = pathlib.Path(__file__).resolve().parent / "redactions.txt"


def load_redactions(root_title):
    REDACTIONS.clear()
    words = [re.escape(w) for w in root_title.split() if w]
    if words:
        REDACTIONS.append((re.compile(r"\b" + r"\s+".join(words) + r"\b", re.I), SITE_TITLE))
    if REDACTION_FILE.exists():
        for line in REDACTION_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            pat, repl = line.split("=", 1)
            REDACTIONS.append((re.compile(pat.strip(), re.I), repl.strip()))

# Keep the historical URLs for the five top-level sections.
SECTION_SLUGS = {
    "Huntress CTF": "huntress",
    "HackTheBox": "htb",
    "Flare-on Challenges": "flareon",
    "Other": "other",
    "Cyber Security Notes": "notes",
}

NOTION_ID_RE = re.compile(r"[ -]([0-9a-f]{32})$")
PAGE_EXT = ".md"


def redact(text):
    for pat, repl in REDACTIONS:
        text = pat.sub(repl, text)
    return text


def strip_id(name):
    """'Some Page 11a6c6e1...' -> 'Some Page'"""
    return NOTION_ID_RE.sub("", name).strip()


def slugify(name, fallback="page"):
    name = strip_id(name)
    name = unicodedata.normalize("NFKD", name)
    name = "".join(c for c in name if not unicodedata.combining(c))
    name = name.encode("ascii", "ignore").decode("ascii").lower()
    name = re.sub(r"[^a-z0-9]+", "-", name).strip("-")
    return name or fallback


def unique(slug, taken):
    if slug not in taken:
        taken.add(slug)
        return slug
    i = 2
    while f"{slug}-{i}" in taken:
        i += 1
    taken.add(f"{slug}-{i}")
    return f"{slug}-{i}"


# --------------------------------------------------------------------- model
class Page:
    def __init__(self, src, title, out, parent):
        self.src = src            # pathlib.Path of the .md
        self.title = title        # display title
        self.out = out            # output path relative to repo root, e.g. htb/index.html
        self.parent = parent
        self.children = []
        self.assets = {}          # source Path -> output path (relative to repo root)
        self.dir = None           # sibling folder holding children + attachments


def dir_candidates(md_path):
    """Folder names Notion pairs with a page, most specific first.

    Same-titled siblings get an abbreviated-id suffix ('2023-10-03 11b6-5e44');
    only one of them keeps the plain title as its folder name.
    """
    stem = md_path.stem
    names = [stem]
    m = NOTION_ID_RE.search(stem)
    if m:
        nid = m.group(1)
        names.append(f"{strip_id(stem)} {nid[:4]}-{nid[-4:]}")
    names.append(strip_id(stem))
    return [md_path.parent / n for n in names]


def assign_dirs(pages):
    """Pair each page with its folder, never handing one folder to two pages."""
    claimed = set()
    for rank in range(3):
        for page in pages:
            if page.dir:
                continue
            cands = dir_candidates(page.src)
            if rank < len(cands) and cands[rank].is_dir() and cands[rank] not in claimed:
                page.dir = cands[rank]
                claimed.add(cands[rank])


def build_tree(export_root):
    tops = sorted(p for p in export_root.iterdir() if p.suffix == PAGE_EXT)
    if not tops:
        sys.exit(f"no top-level .md page found in {export_root}")
    root_md = tops[0]
    load_redactions(strip_id(root_md.stem))
    root = Page(root_md, SITE_TITLE, "index.html", None)
    assign_dirs([root])
    if root.dir:
        add_children(root, root.dir, "")
    return root


def add_children(parent, folder, out_prefix):
    taken = set()
    mds = sorted((p for p in folder.iterdir() if p.suffix == PAGE_EXT), key=lambda p: p.name.lower())
    for md in mds:
        title = redact(strip_id(md.stem))
        slug = SECTION_SLUGS.get(strip_id(md.stem)) if parent.parent is None else None
        slug = unique(slug or slugify(md.stem), taken)
        parent.children.append(Page(md, title, f"{out_prefix}{slug}.html", parent))

    assign_dirs(parent.children)
    for child in parent.children:
        if child.dir:
            add_children(child, child.dir, child.out[:-len(".html")] + "/")

    # A page with children is nicer as <slug>/index.html so the folder is browsable.
    for child in parent.children:
        if child.children:
            child.out = child.out[:-len(".html")] + "/index.html"


def collect_assets(page, taken_by_dir):
    """Copy-plan every non-page file that lives in this page's folder."""
    if not page.dir:
        return
    asset_dir = (pathlib.PurePosixPath(page.out).parent if page.children
                 else pathlib.PurePosixPath(page.out[:-len(".html")]))
    taken = taken_by_dir.setdefault(str(asset_dir), set())
    for f in sorted(page.dir.iterdir()):
        if f.is_dir() or f.suffix == PAGE_EXT:
            continue
        stem, ext = os.path.splitext(f.name)
        name = unique(slugify(stem, "file") + ext.lower(), taken)
        page.assets[f.resolve()] = str(asset_dir / name)


def walk(page):
    yield page
    for c in page.children:
        yield from walk(c)


# ------------------------------------------------------------------ rendering
class LinkRenderer(mdlite.Renderer):
    def __init__(self, page, site):
        self.page = page
        self.site = site

    def _resolve(self, raw):
        if raw.startswith(("http://", "https://", "mailto:", "#", "data:")):
            return raw
        # '#' is a fragment separator, but Notion also leaves it unescaped inside
        # page names ('Scenario #1 <id>.md'), so try the whole string first.
        attempts = [(raw, "")]
        if "#" in raw:
            head, frag = raw.split("#", 1)
            attempts.append((head, frag))
        out = None
        for path, frag in attempts:
            target = urllib.parse.unquote(path.replace("&amp;", "&"))
            cand = (self.page.src.parent / target).resolve()
            if cand.suffix == PAGE_EXT:
                hit = self.site["pages_by_src"].get(cand)
                out = hit.out if hit else None
            else:
                out = self.page.assets.get(cand) or self.site["assets"].get(cand)
            if out:
                break
        if not out:
            self.site["missing"].append((str(self.page.src), raw))
            return raw
        rel = relpath(self.page.out, out)
        return rel + ("#" + frag if frag else "")

    def link(self, url):
        return self._resolve(url)

    def image(self, url):
        return self._resolve(url)


def relpath(from_out, to_out):
    frm = pathlib.PurePosixPath(from_out).parent
    return urllib.parse.quote(os.path.relpath(to_out, str(frm)).replace(os.sep, "/"))


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<title>{title} · {site_title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="{assets}/style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><text y='14' font-size='14'>&#127988;</text></svg>">
</head>
<body>
<button id="menu-toggle" aria-label="Toggle navigation">&#9776;</button>
<div class="layout">
<aside class="sidebar" id="sidebar">
  <a class="brand" href="{home}">
    <span class="brand-flag">&#127988;</span>
    <span class="brand-text"><strong>{site_title}</strong><small>{site_sub}</small></span>
  </a>
  <nav class="nav" id="nav-root" data-current="{current}" data-root="{root}"></nav>
</aside>
<main class="content">
  <article class="doc">
{breadcrumb}
{body}
  </article>
  <footer class="foot">Built from a Notion export · <a href="https://github.com/{site_title}">github.com/{site_title}</a></footer>
</main>
</div>
<script src="{assets}/nav.js" defer></script>
<script>
document.getElementById('menu-toggle').addEventListener('click',function(){{
  document.getElementById('sidebar').classList.toggle('open');
}});
</script>
</body>
</html>
"""


def breadcrumb(page):
    trail, n = [], page.parent
    while n:
        trail.append(n)
        n = n.parent
    if not trail:
        return ""
    parts = [f'<a href="{relpath(page.out, p.out)}">{html.escape(p.title)}</a>' for p in reversed(trail)]
    return '  <div class="breadcrumb">' + " &rsaquo; ".join(parts) + "</div>"


def child_index(page, body):
    """List sub-pages the page's own content doesn't already link to."""
    missing = [c for c in page.children if f'href="{relpath(page.out, c.out)}"' not in body]
    if not missing:
        return ""
    items = "".join(
        f'<li><a href="{relpath(page.out, c.out)}">{html.escape(c.title)}'
        f'{f"<span>{len(c.children)} pages</span>" if c.children else ""}</a></li>'
        for c in missing)
    heading = "Pages" if len(missing) == len(page.children) else "More pages"
    return f'<h2 id="pages">{heading}</h2><ul class="child-index">{items}</ul>'


HOME_SECTION_BLURB = {
    "huntress": "Huntress CTF writeups (2023–2025), by year, day and challenge.",
    "htb": "Completed HackTheBox machines and challenges, plus the Hack The Boo events.",
    "flareon": "Reverse-engineering writeups from the annual Flare-on contest.",
    "other": "Blue Team Field Manual, CSO CTFs, SANS Holiday Hack and lab exercises.",
    "notes": "Threat intel, threat hunting and incident-response reference notes.",
}


def render_home(root, site):
    """The Notion home page is a bare list of links; lay it out as cards."""
    raw = redact(root.src.read_text(encoding="utf-8", errors="replace"))
    rend = LinkRenderer(root, site)
    bookmarks, sections = [], []
    for m in mdlite.LINK_RE.finditer(raw):
        label, url = m.group(1), m.group(2)
        if url.startswith("http"):
            host = urllib.parse.urlparse(url).netloc.replace("www.", "")
            name = label if not label.startswith("http") else url.rstrip("/").split("/")[-1]
            bookmarks.append((name, url, host))
        else:
            resolved = rend.link(url)
            page = next((p for p in walk(root) if relpath(root.out, p.out) == resolved), None)
            if page:
                sections.append(page)

    for c in root.children:
        if c not in sections:
            sections.append(c)

    cards = "".join(
        f'<a class="card" href="{relpath(root.out, p.out)}">'
        f'<strong>{html.escape(p.title)}</strong>'
        f'<span>{html.escape(HOME_SECTION_BLURB.get(pathlib.PurePosixPath(p.out).parts[0], ""))}</span>'
        f'<em>{sum(1 for _ in walk(p)) - 1} pages</em></a>'
        for p in sections)

    links = "".join(
        f'<li><a href="{html.escape(url, quote=True)}" target="_blank" rel="noopener">'
        f'{html.escape(name)}<span>{html.escape(host)}</span></a></li>'
        for name, url, host in bookmarks)

    return (f'<h1 id="home">&#127988; {html.escape(SITE_TITLE)}</h1>\n'
            f'<p class="lede">{html.escape(SITE_DESC)}</p>\n'
            f'<h2 id="sections">Sections</h2>\n<div class="cards">{cards}</div>\n'
            + (f'<h2 id="links">Links &amp; bookmarks</h2>\n<ul class="bookmarks">{links}</ul>\n' if links else "")
            + '<blockquote><p>Writeups from before 2024 are often screenshots rather than '
              'detailed notes.</p></blockquote>')


def toc_html(toc):
    if len(toc) < 3:
        return ""
    items = "".join(f'<li class="lvl{lvl}"><a href="#{aid}">{html.escape(txt)}</a></li>'
                    for lvl, txt, aid in toc)
    return f'<nav class="toc"><strong>On this page</strong><ul>{items}</ul></nav>'


def nav_tree(page, root_out="index.html"):
    return [{"title": c.title, "out": c.out, "children": nav_tree(c, root_out)} for c in page.children]


# ---------------------------------------------------------------------- build
def build(export_root):
    root = build_tree(export_root)
    pages = list(walk(root))
    taken_by_dir = {}
    for p in pages:
        collect_assets(p, taken_by_dir)

    site = {
        "pages_by_src": {p.src.resolve(): p for p in pages},
        "assets": {src: out for p in pages for src, out in p.assets.items()},
        "missing": [],
    }

    # wipe previously generated output
    top_dirs = {pathlib.PurePosixPath(c.out).parts[0] for c in root.children}
    for d in top_dirs:
        shutil.rmtree(ROOT / d, ignore_errors=True)
    for f in ("index.html", "404.html", "assets/nav.json"):
        (ROOT / f).unlink(missing_ok=True)

    # copy attachments
    n_assets = 0
    for src, out in site["assets"].items():
        dest = ROOT / out
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        n_assets += 1

    for page in pages:
        depth = len(pathlib.PurePosixPath(page.out).parts) - 1
        up = "/".join([".."] * depth) or "."
        if page is root:
            body, toc = render_home(root, site), []
        else:
            raw = redact(page.src.read_text(encoding="utf-8", errors="replace"))
            # the first H1 duplicates the page title Notion already gives us
            raw = re.sub(r"\A\s*#\s+.*\n", "", raw, count=1)
            body, toc = mdlite.convert(raw, LinkRenderer(page, site))
            body = (f'<h1 id="title">{html.escape(page.title)}</h1>\n'
                    + toc_html(toc) + "\n" + body + child_index(page, body))
        html_ = TEMPLATE.format(
            title=html.escape(page.title),
            site_title=html.escape(SITE_TITLE),
            site_sub=html.escape(SITE_SUB),
            desc=html.escape(SITE_DESC if page is root else f"{page.title} — {SITE_SUB}", quote=True),
            current=page.out,
            root=up,
            home=relpath(page.out, root.out),
            assets=f"{up}/assets",
            breadcrumb=breadcrumb(page),
            body=body,
        )
        dest = ROOT / page.out
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html_, encoding="utf-8")

    (ROOT / "assets").mkdir(exist_ok=True)
    (ROOT / "assets/nav.json").write_text(json.dumps(nav_tree(root), ensure_ascii=False), encoding="utf-8")
    (ROOT / ".nojekyll").touch()

    # GitHub Pages serves this for any unknown path, so it needs absolute URLs.
    (ROOT / "404.html").write_text(TEMPLATE.format(
        title="Not found", site_title=html.escape(SITE_TITLE), site_sub=html.escape(SITE_SUB),
        desc="Page not found", current="404.html", root="", home="/", assets="/assets",
        breadcrumb="", body='<h1 id="not-found">404 — page not found</h1>'
                           '<p>That page does not exist. Try the sidebar, or '
                           '<a href="/">start from the home page</a>.</p>',
    ), encoding="utf-8")

    print(f"pages: {len(pages)}   attachments: {n_assets}")
    if site["missing"]:
        print(f"unresolved links: {len(site['missing'])}")
        for src, url in site["missing"][:10]:
            print("  ", os.path.basename(src), "->", url[:80])


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    target = pathlib.Path(sys.argv[1]).expanduser().resolve()
    tmp = None
    if target.is_file() and target.suffix == ".zip":
        tmp = pathlib.Path(tempfile.mkdtemp(prefix="notion-export-"))
        extract(target, tmp)
        # Notion splits big exports into an inner Part-N zip
        inner = sorted(tmp.glob("*.zip"))
        if inner and not any(p.suffix == PAGE_EXT for p in tmp.iterdir()):
            for z in inner:
                extract(z, tmp)
                z.unlink()
        target = tmp
    if not target.is_dir():
        sys.exit(f"not an export directory or zip: {target}")
    try:
        build(target)
    finally:
        if tmp:
            shutil.rmtree(tmp, ignore_errors=True)


def extract(zip_path, dest):
    """unzip, honouring the UTF-8 filename flag (plain `unzip` mangles these)."""
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            out = dest / info.filename
            if info.is_dir():
                out.mkdir(parents=True, exist_ok=True)
                continue
            out.parent.mkdir(parents=True, exist_ok=True)
            with z.open(info) as s, open(out, "wb") as d:
                shutil.copyfileobj(s, d)


if __name__ == "__main__":
    main()
