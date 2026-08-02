# the-grizzly-bear.github.io

Personal cybersecurity notes and CTF writeups, migrated from Notion and published
as a static GitHub Pages site. Minimal light documentation theme, no build step
required on GitHub's side.

## How it works

- Content lives as Markdown under `_src/content/` (one file per Notion page).
- `_src/structure.json` is the navigation tree, built from the content folder by
  `_src/build_structure.py` (ordering follows each page's `## Contents` list).
- `_src/generate.py` renders every Markdown file into a static `.html` page at the
  repo root, using `assets/style.css` and the shared client-side sidebar
  (`assets/nav.js` + `assets/nav.json`).
- `.nojekyll` tells GitHub Pages to serve the files as-is (no Jekyll processing).

## Regenerating the site

```bash
pip install markdown
python3 _src/build_structure.py   # rebuild nav from _src/content
python3 _src/generate.py          # render HTML pages + assets/nav.json
```

## Publishing

This repo is a GitHub user/organization page, so GitHub Pages serves the root of
the default branch automatically. Push to `main` and the site goes live at
https://the-grizzly-bear.github.io/

## Note on images

Screenshots from the original Notion pages are not embedded — the environment used
to migrate the content could not reach Notion's image host. Those spots are marked
"image unavailable". To add them, re-run the migration with access to the images,
or do a Notion **Markdown & CSV export** (which bundles the images) and drop the
image files into `assets/img/…` matching the referenced paths.
