#!/usr/bin/env python3
"""逐段复核 --full 取证非零的引语：按 `…` / `...` / `. . .` 切段，每段单独 flat 查 epub 展平全文。
分段全中 = 合规省略号拼接（不报）；任一段查无 = 真缺陷候选。
与 scripts/verify_quotes.py::_p06_probe 同口径，但额外打印上下文供人工判读。
"""
import glob
import os
import re
import sys
import unicodedata
import zipfile


def flat_alpha(s):
    s = unicodedata.normalize("NFKC", s)
    return re.sub(r"[^0-9a-z]+", "", s.lower())


def epub_flat(epub):
    parts = []
    with zipfile.ZipFile(epub) as z:
        for n in sorted(z.namelist()):
            if n.lower().endswith((".xhtml", ".html", ".htm")):
                t = z.read(n).decode("utf-8", "ignore")
                parts.append(re.sub(r"<[^>]+>", " ", t))
    return flat_alpha(" ".join(parts))


ELL = re.compile(r"\s*(?:\.\s*\.\s*\.|\.\.\.|…)\s*")


def md_quotes(md):
    out = []
    for i, line in enumerate(open(md, encoding="utf-8"), 1):
        if not line.startswith(">"):
            continue
        m = re.match(r'^>\s*(?:\*{0,2}(?:原句|Quote|引用)\s*\d+\*{0,2}\s*[:：]\s*)?(.+?)\s*$', line)
        if m and re.search(r"[A-Za-z]{3}", m.group(1)):
            out.append((i, m.group(1)))
    return out


def probe(book, want):
    d = glob.glob(f"notes/books/*/{book}")[0]
    full = epub_flat(glob.glob(os.path.join(d, "library", "*.epub"))[0])
    print(f"\n{'='*76}\n### {book}")
    for md in sorted(glob.glob(os.path.join(d, "ch*.md"))):
        base = os.path.basename(md)
        for ln, q in md_quotes(md):
            segs = [s for s in ELL.split(q) if flat_alpha(s)]
            bad = [s for s in segs if flat_alpha(s) not in full]
            if not bad:
                continue
            if want and not any(w in base for w in want):
                continue
            nseg = len(segs)
            print(f"\n-- {base}:{ln}   [{nseg} 段, {len(bad)} 段查无]")
            for s in bad:
                f = flat_alpha(s)
                print(f"   ✗ 段({len(f)}字符): {s.strip()[:120]!r}")
                print(f"     flat 开头: {f[:60]!r}")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("@")]
    want = [a[1:] for a in sys.argv[1:] if a.startswith("@")]
    for b in args:
        probe(b, want)