#!/usr/bin/env python3
"""Build _src/structure.json (the nav tree) from the _src/content filesystem.

Convention produced by the crawlers:
  <dir>/index.md         -> the section/self page
  <dir>/<stem>.md        -> a child page
  <dir>/<stem>/          -> that child's own children live here
Ordering of children is taken from the parent page's "## Contents" links
(basename before .html), with any unreferenced files appended alphabetically.
"""
import json, re, pathlib

SRC = pathlib.Path(__file__).resolve().parent
CONTENT = SRC / "content"

def title_of(md_path):
    try:
        for line in md_path.read_text().splitlines():
            m = re.match(r"#\s+(.*)", line)
            if m:
                return m.group(1).strip() or md_path.stem
    except FileNotFoundError:
        pass
    return md_path.stem

def contents_order(md_path):
    """Return list of html basenames (slugs) linked in the page, in order."""
    order = []
    try:
        text = md_path.read_text()
    except FileNotFoundError:
        return order
    for m in re.finditer(r"\[[^\]]*\]\(([^)]+?\.html)\)", text):
        base = m.group(1).split("/")[-1][:-5]  # strip .html
        if base and base not in order:
            order.append(base)
    return order

def rel(p):
    return str(p.relative_to(CONTENT))

def build_node(page_md, child_dir, title=None):
    node = {
        "title": title or title_of(page_md),
        "src": rel(page_md) if page_md.exists() else None,
        "out": rel(page_md).replace(".md", ".html") if page_md.exists()
               else rel(child_dir) + "/index.html",
        "children": [],
    }
    if child_dir and child_dir.is_dir():
        files = {p.stem: p for p in child_dir.glob("*.md") if p.stem != "index"}
        order = contents_order(page_md) if page_md.exists() else []
        ordered = [s for s in order if s in files] + \
                  [s for s in sorted(files) if s not in order]
        for stem in ordered:
            node["children"].append(
                build_node(files[stem], child_dir / stem)
            )
    return node

def section_node(dirname, title=None):
    d = CONTENT / dirname
    idx = d / "index.md"
    n = build_node(idx, d, title=title or title_of(idx))
    # section index out path
    n["out"] = f"{dirname}/index.html"
    n["src"] = f"{dirname}/index.md" if idx.exists() else None
    return n

def group(title, out, subdirs):
    return {
        "title": title, "src": None, "out": out,
        "children": [section_node(sd) for sd in subdirs],
    }

def hacktheboo_group():
    kids = []
    for year in ["2022", "2023", "2024", "2025"]:
        kids.append(section_node(f"htb/hacktheboo/{year}", title=title_of(CONTENT/f"htb/hacktheboo/{year}/index.md")))
    return {"title": "Hack The Boo", "src": None,
            "out": "htb/hacktheboo/index.html", "children": kids}

nav = [
    {"title": "Home", "src": "home.md", "out": "index.html", "children": []},
    group("Huntress CTF", "huntress/index.html",
          ["huntress/2023", "huntress/2024", "huntress/2025"]),
    {"title": "HackTheBox", "src": None, "out": "htb/index.html", "children": [
        section_node("htb/machines"),
        section_node("htb/challenges"),
        hacktheboo_group(),
    ]},
    section_node("flareon"),
    section_node("other"),
    section_node("notes"),
]

# nicer top-level titles
nav[1]["children"][0]["title"] = "2023"
nav[1]["children"][1]["title"] = "2024"
nav[1]["children"][2]["title"] = "2025"

def count(nodes):
    c = 0
    for n in nodes:
        c += 1
        c += count(n["children"])
    return c

out = {"nav": nav}
(SRC / "structure.json").write_text(json.dumps(out, indent=2))
print(f"structure.json written: {count(nav)} nodes")
