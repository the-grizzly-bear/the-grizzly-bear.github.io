#!/usr/bin/env python3
"""Minimal light-docs static site generator.

Reads _src/structure.json (the nav tree) and _src/content/*.md, and writes
plain HTML pages to the repo root so GitHub Pages (org page) serves them as-is.
"""
import json, os, re, html, pathlib
import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent      # site/
SRC = ROOT / "_src"
CONTENT = SRC / "content"
STRUCT = json.loads((SRC / "structure.json").read_text())

SITE_TITLE = "Will Seligman"
SITE_SUB = "Cybersecurity Notes & CTF Writeups"

MD = markdown.Markdown(extensions=["extra", "fenced_code", "tables", "toc", "sane_lists", "nl2br"])

IMG_MISSING = re.compile(r"\*\[image unavailable\]\*")

def iter_nodes(nodes):
    for n in nodes:
        yield n
        if n.get("children"):
            yield from iter_nodes(n["children"])

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · {site_title}</title>
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<button id="menu-toggle" aria-label="Toggle navigation">&#9776; Menu</button>
<div class="layout">
<aside class="sidebar" id="sidebar">
  <a class="brand" href="/index.html">
    <span class="brand-flag">&#127988;</span>
    <span class="brand-text"><strong>{site_title}</strong><small>{site_sub}</small></span>
  </a>
  <nav class="nav" id="nav-root" data-current="{current}"></nav>
</aside>
<main class="content">
  <article class="doc">
  {breadcrumb}
  {body}
  </article>
  <footer class="foot">Notes by Will Seligman · built from Notion</footer>
</main>
</div>
<script src="/assets/nav.js" defer></script>
<script>
document.getElementById('menu-toggle').addEventListener('click',function(){{
  document.getElementById('sidebar').classList.toggle('open');
}});
</script>
</body>
</html>
"""

def breadcrumb(trail):
    if not trail:
        return ""
    parts = []
    for t in trail:
        if t.get("out"):
            parts.append(f'<a href="/{t["out"]}">{html.escape(t["title"])}</a>')
        else:
            parts.append(html.escape(t["title"]))
    return '<div class="breadcrumb">' + ' &rsaquo; '.join(parts) + '</div>'

def build():
    # map out-path -> trail for breadcrumbs
    trails = {}
    def walk(nodes, trail):
        for n in nodes:
            t2 = trail + [n]
            if n.get("out"):
                trails[n["out"]] = t2
            if n.get("children"):
                walk(n["children"], t2)
    walk(STRUCT["nav"], [])

    count = 0
    for n in iter_nodes(STRUCT["nav"]):
        out = n.get("out")
        if not out:
            continue
        src = n.get("src")
        if src and (CONTENT / src).exists():
            raw = (CONTENT / src).read_text()
            raw = IMG_MISSING.sub('<span class="img-missing">image unavailable</span>', raw)
            MD.reset()
            body_html = MD.convert(raw)
        else:
            # auto index page: title + child links
            body_html = f"<h1>{html.escape(n['title'])}</h1>"
            if n.get("children"):
                body_html += '<ul class="child-index">'
                for c in n["children"]:
                    if c.get("out"):
                        body_html += f'<li><a href="/{c["out"]}">{html.escape(c["title"])}</a></li>'
                    else:
                        body_html += f'<li>{html.escape(c["title"])}</li>'
                body_html += '</ul>'
        page = TEMPLATE.format(
            title=html.escape(n["title"]),
            site_title=SITE_TITLE,
            site_sub=SITE_SUB,
            current=out,
            body=body_html,
            breadcrumb=breadcrumb(trails.get(out, [])[:-1]),
        )
        dest = ROOT / out
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page)
        count += 1
    # emit nav data for the shared client-side sidebar
    (ROOT / "assets" / "nav.json").write_text(json.dumps(STRUCT["nav"]))
    print(f"Generated {count} pages")

if __name__ == "__main__":
    build()
