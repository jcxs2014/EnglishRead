#!/usr/bin/env python3
"""对 --full 取证非零的引语做人工分类取证：把 md 引语的首 52 字符在 epub 展平全文里的
真实上下文打印出来，看 md 引语的「继续」是不是原文里真的接得上的下一句。
"""
import glob
import os
import re
import sys
import unicodedata
import zipfile


def flat_alpha(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    return re.sub(r"[^0-9a-z]+", "", s.lower())


def epub_flat(epub: str) -> str:
    parts = []
    with zipfile.ZipFile(epub) as z:
        for n in sorted(z.namelist()):
            if not n.lower().endswith((".xhtml", ".html", ".htm")):
                continue
            t = z.read(n).decode("utf-8", "ignore")
            t = re.sub(r"<[^>]+>", " ", t)
            parts.append(t)
    return flat_alpha(" ".join(parts))


def md_quotes(md: str):
    out = []
    for i, line in enumerate(open(md, encoding="utf-8"), 1):
        m = re.match(r"^>\s*\*{0,2}(?:原句\s*\d+|Quote\s*\d+)?\*{0,2}\s*[:：]?\s*(.+?)\s*$", line)
        if m and re.search(r"[A-Za-z]{3}", m.group(1)):
            out.append((i, m.group(1)))
    return out


def probe(book, targets):
    d = glob.glob(f"notes/books/*/{book}")[0]
    epub = glob.glob(os.path.join(d, "library", "*.epub"))[0]
    full = epub_flat(epub)
    print(f"\n{'='*78}\n### {book}   (epub flat len={len(full)})")
    for md in sorted(glob.glob(os.path.join(d, "ch*.md"))):
        for ln, q in md_quotes(md):
            fa = flat_alpha(q)
            if len(fa) < 60:
                continue
            probe52 = fa[:52]
            pos = full.find(probe52)
            if pos < 0:
                continue
            # 关键：md 紧接着 52 字符之后写了什么 vs 原文在 pos+52 处是什么
            nxt_md = fa[52:52 + 40]
            nxt_src = full[pos + 52:pos + 92]
            if nxt_src[:len(nxt_md)] == nxt_md:
                continue
            print(f"\n-- {os.path.basename(md)}:{ln}")
            print(f"   md 引语(展平后 52-92): {nxt_md!r}")
            print(f"   原文同位(52-92)       : {nxt_src!r}")
            print(f"   原文该处上下文        : ...{full[pos:pos+150]}...")


if __name__ == "__main__":
    for b in sys.argv[1:]:
        probe(b, None)