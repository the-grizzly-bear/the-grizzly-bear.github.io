#!/usr/bin/env python3
"""A small, dependency-free Markdown -> HTML converter.

Only covers what Notion's Markdown export actually emits: ATX headings, fenced
code, pipe tables, blockquotes, nested ordered/unordered lists, images, links,
dividers and the usual inline spans.  Raw HTML in the source is escaped (Notion
puts HTML snippets inside writeups as literal text), except for a `<br>`.
"""
import html
import re

FENCE_RE = re.compile(r"^\s*```(.*)$")
HEAD_RE = re.compile(r"^(#{1,6})\s+(.*)$")
HR_RE = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$")
LIST_RE = re.compile(r"^(\s*)(-|\*|\+|\d+\.)\s+(.*)$")
QUOTE_RE = re.compile(r"^\s*>\s?(.*)$")
TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")

CODE_SPAN_RE = re.compile(r"`([^`]+)`")
# The URL part allows one level of balanced parens (Notion page titles contain
# them) plus a trailing unclosed '(' — Notion truncates long folder names mid-name,
# e.g. ![x](Baby Buffer Overflow - 32bit (Binary Ex/image.png).
_URL = r"((?:[^()\s]|\((?:[^()\s]|\([^()\s]*\))*\))*(?:\([^()\s]*)?)"
IMG_RE = re.compile(r"!\[([^\]]*)\]\(" + _URL + r"(?:\s+\"[^\"]*\")?\)")
LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(" + _URL + r"(?:\s+\"[^\"]*\")?\)")
NESTED_LINK_RE = re.compile(
    r"(?:<a [^>]*>)?\[+([^\]]*(?:<a [^>]*>|</a>)[^\]]*)\]\(" + _URL + r"\)")
TAG_RE = re.compile(r"<[^>]+>")
BOLD_RE = re.compile(r"\*\*(?=\S)(.+?)(?<=\S)\*\*", re.S)
ITAL_RE = re.compile(r"(?<![\*\w])\*(?=[^\s\*])(.+?)(?<=[^\s\*])\*(?!\*)", re.S)
STRIKE_RE = re.compile(r"~~(?=\S)(.+?)(?<=\S)~~", re.S)
# '**text.*' — an unbalanced marker the source pages use; rendered as emphasis.
LOPSIDED_RE = re.compile(r"\*\*(?=\S)([^*\n]+)(?<=\S)\*(?!\*)")
BARE_URL_RE = re.compile(r"(?<![\"'=(>])\bhttps?://[^\s<>\"')\]]+")
SLUG_STRIP_RE = re.compile(r"[^a-z0-9\s-]")


def slug_anchor(text, seen):
    s = SLUG_STRIP_RE.sub("", text.lower()).strip()
    s = re.sub(r"[\s-]+", "-", s) or "section"
    n = seen.get(s, 0)
    seen[s] = n + 1
    return s if not n else f"{s}-{n}"


class Renderer:
    """Hooks a caller can override to rewrite URLs (see generate.py)."""

    def link(self, url):
        return url

    def image(self, url):
        return url


class Markdown:
    def __init__(self, renderer=None):
        self.r = renderer or Renderer()

    # ---------------------------------------------------------------- inline
    def inline(self, text):
        codes = []

        def stash(m):
            codes.append(html.escape(m.group(1), quote=False))
            return f"\x00{len(codes) - 1}\x00"

        text = CODE_SPAN_RE.sub(stash, text)
        text = html.escape(text, quote=False)
        text = text.replace("&lt;br&gt;", "<br>").replace("&lt;br/&gt;", "<br>")

        def img(m):
            alt, url = m.group(1), self.image_url(m.group(2))
            return (f'<a class="img-link" href="{url}">'
                    f'<img src="{url}" alt="{html.escape(alt, quote=True)}" loading="lazy"></a>')

        text = IMG_RE.sub(img, text)

        def link(m):
            label, url = m.group(1), self.link_url(m.group(2))
            ext = ' target="_blank" rel="noopener"' if url.startswith(("http://", "https://")) else ""
            return f'<a href="{url}"{ext}>{label or html.escape(url)}</a>'

        text = LINK_RE.sub(link, text)
        # Notion sometimes nests a link inside a link label, which leaves an
        # already-rendered <a> stranded in the outer label.  Flatten it: keep the
        # outer target, using the label's plain text.
        def flatten(m):
            label = TAG_RE.sub("", m.group(1)).replace("[", "").replace("*", "").strip()
            url = self.link_url(m.group(2))
            ext = ' target="_blank" rel="noopener"' if url.startswith(("http://", "https://")) else ""
            return f'<a href="{url}"{ext}>{label}</a>'

        text = NESTED_LINK_RE.sub(flatten, text)
        text = BOLD_RE.sub(r"<strong>\1</strong>", text)
        text = LOPSIDED_RE.sub(r"<em>\1</em>", text)
        text = ITAL_RE.sub(r"<em>\1</em>", text)
        text = STRIKE_RE.sub(r"<del>\1</del>", text)
        text = BARE_URL_RE.sub(
            lambda m: f'<a href="{m.group(0)}" target="_blank" rel="noopener">{m.group(0)}</a>', text)

        return re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{codes[int(m.group(1))]}</code>", text)

    def link_url(self, raw):
        return html.escape(self.r.link(raw.strip()), quote=True)

    def image_url(self, raw):
        return html.escape(self.r.image(raw.strip()), quote=True)

    # ----------------------------------------------------------------- block
    def convert(self, text):
        self.anchors = {}
        self.toc = []
        lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
        out = []
        i = 0
        n = len(lines)
        while i < n:
            line = lines[i]

            if not line.strip():
                i += 1
                continue

            m = FENCE_RE.match(line)
            if m:
                lang = m.group(1).strip().split()[0] if m.group(1).strip() else ""
                body, i = [], i + 1
                while i < n and not FENCE_RE.match(lines[i]):
                    body.append(lines[i])
                    i += 1
                i += 1  # closing fence
                cls = f' class="language-{html.escape(lang, quote=True)}"' if lang else ""
                out.append(f'<pre><code{cls}>{html.escape("\n".join(body), quote=False)}</code></pre>')
                continue

            m = HEAD_RE.match(line)
            if m:
                lvl, txt = len(m.group(1)), m.group(2).strip()
                aid = slug_anchor(re.sub(r"[`*_\[\]()]", "", txt), self.anchors)
                rendered = self.inline(txt)
                if lvl <= 3:
                    self.toc.append((lvl, html.unescape(TAG_RE.sub("", rendered)).lstrip("# "), aid))
                out.append(f'<h{lvl} id="{aid}">{rendered}</h{lvl}>')
                i += 1
                continue

            if HR_RE.match(line):
                out.append("<hr>")
                i += 1
                continue

            if line.lstrip().startswith("|") and i + 1 < n and TABLE_SEP_RE.match(lines[i + 1]):
                block, i = [line], i + 1
                sep = lines[i]
                i += 1
                while i < n and lines[i].lstrip().startswith("|"):
                    block.append(lines[i])
                    i += 1
                out.append(self.table(block[0], sep, block[1:]))
                continue

            if QUOTE_RE.match(line):
                block = []
                while i < n and (QUOTE_RE.match(lines[i]) or (lines[i].strip() and block)):
                    m2 = QUOTE_RE.match(lines[i])
                    block.append(m2.group(1) if m2 else lines[i])
                    i += 1
                out.append(f"<blockquote>{self.convert_nested(block)}</blockquote>")
                continue

            if LIST_RE.match(line):
                block = []
                while i < n and (LIST_RE.match(lines[i]) or (lines[i].strip() and block) or
                                 (not lines[i].strip() and i + 1 < n and LIST_RE.match(lines[i + 1]))):
                    block.append(lines[i])
                    i += 1
                html_, _ = self.list_block(block, 0)
                out.append(html_)
                continue

            para = []
            while i < n and lines[i].strip() and not FENCE_RE.match(lines[i]) \
                    and not HEAD_RE.match(lines[i]) and not LIST_RE.match(lines[i]) \
                    and not QUOTE_RE.match(lines[i]) and not HR_RE.match(lines[i]):
                para.append(lines[i].strip())
                i += 1
            if para:
                body = self.inline("\n".join(para)).replace("\n", "<br>\n")
                cls = ' class="figure"' if body.startswith('<a class="img-link"') else ""
                out.append(f"<p{cls}>{body}</p>")
            else:
                i += 1
        return "\n".join(out)

    def convert_nested(self, lines):
        sub = Markdown(self.r)
        out = sub.convert("\n".join(lines))
        self.anchors.update(sub.anchors)
        return out

    def list_block(self, lines, idx):
        """Render one list starting at lines[idx]; returns (html, next_index)."""
        m = LIST_RE.match(lines[idx])
        base = len(m.group(1))
        ordered = m.group(2)[0].isdigit()
        items = []
        while idx < len(lines):
            line = lines[idx]
            if not line.strip():
                idx += 1
                continue
            m = LIST_RE.match(line)
            if not m:  # lazy continuation of the previous item
                if items:
                    items[-1].append(line.strip())
                    idx += 1
                    continue
                break
            ind = len(m.group(1))
            if ind < base:
                break
            if ind > base:
                nested, idx = self.list_block(lines, idx)
                if items:
                    items[-1].append(nested)
                continue
            items.append([m.group(3)])
            idx += 1

        tag = "ol" if ordered else "ul"
        html_items = []
        for parts in items:
            body = self.inline(parts[0])
            rest = "".join(p if p.startswith("<ul") or p.startswith("<ol")
                           else "<br>" + self.inline(p) for p in parts[1:])
            html_items.append(f"<li>{body}{rest}</li>")
        return f"<{tag}>" + "".join(html_items) + f"</{tag}>", idx

    def table(self, header, sep, rows):
        def cells(row):
            row = row.strip()
            if row.startswith("|"):
                row = row[1:]
            if row.endswith("|"):
                row = row[:-1]
            return [c.strip() for c in row.split("|")]

        aligns = []
        for c in cells(sep):
            left, right = c.startswith(":"), c.endswith(":")
            aligns.append(' style="text-align:center"' if left and right else
                          ' style="text-align:right"' if right else "")

        def align(k):
            return aligns[k] if k < len(aligns) else ""

        head = "".join(f"<th{align(k)}>{self.inline(c)}</th>" for k, c in enumerate(cells(header)))
        body = "".join(
            "<tr>" + "".join(f"<td{align(k)}>{self.inline(c)}</td>" for k, c in enumerate(cells(r))) + "</tr>"
            for r in rows)
        return (f'<div class="table-wrap"><table><thead><tr>{head}</tr></thead>'
                f"<tbody>{body}</tbody></table></div>")


def convert(text, renderer=None):
    md = Markdown(renderer)
    return md.convert(text), md.toc
