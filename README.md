# the-grizzly-bear.github.io

Personal cybersecurity notes and CTF writeups, generated straight from a Notion
**Markdown & CSV** export and published as a static GitHub Pages site. Dark theme,
no build step on GitHub's side.

## How it works

- `_src/generate.py` reads a Notion export (a `.zip` or an unzipped folder) and
  writes the whole site to the repo root: one `.html` per exported page, with every
  attachment copied next to the page that references it.
- `_src/mdlite.py` is a small dependency-free Markdown converter (headings, fenced
  code, tables, nested lists, images, links) — no `pip install` needed.
- The page hierarchy mirrors Notion 1:1. A page with sub-pages becomes
  `<slug>/index.html`; its sub-pages and images live in `<slug>/`.
- `assets/style.css` plus a shared client-side sidebar (`assets/nav.js` reading
  `assets/nav.json`) provide navigation, breadcrumbs and a filter box.
- `.nojekyll` tells GitHub Pages to serve the files as-is.

## Regenerating the site

```bash
python3 _src/generate.py ~/Downloads/ExportBlock-<id>.zip   # or an unzipped export dir
```

The generator wipes and rewrites the top-level section folders, `index.html` and
`404.html`, then reports page/attachment counts and any link it could not resolve.

Standalone external links on the home page are rendered as Notion-style bookmark
cards. The title/description/preview image are scraped once and cached in
`_src/bookmarks.json`, with the images saved to `assets/bookmarks/` so the site
stays self-contained. Re-scrape with:

```bash
python3 _src/generate.py <export> --refresh-bookmarks
``` Notion export zips are `.gitignore`d — they are the source,
not part of the published site.

Export from Notion with **Export → Markdown & CSV**, "Include subpages" and
"Create folders for subpages" enabled, so attachments come with it.

## Publishing

This repo is a GitHub user page, so Pages serves the root of the default branch.
Push to `main` and the site is live at https://the-grizzly-bear.github.io/

## Notes

- Section URLs (`huntress/`, `htb/`, `flareon/`, `other/`, `notes/`) are pinned in
  `SECTION_SLUGS` so old links keep working; everything else is slugified.
- `REDACTIONS` in `_src/generate.py` strips names/strings that should not be
  published — it is applied to page titles and page bodies on every build.
