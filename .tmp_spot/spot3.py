#!/usr/bin/env python3
"""用 scripts/verify_quotes.py 自己的管道复核 --full 取证非零的引语。

与工具同口径（flat_alpha = NFKD + 先剥 \n \t；epub_flat_text = 剥标签 + html.unescape），
差别只有一处：把引语按 `…` / `...` / `. . .` 切段逐段查，查无的段打印原文上下文供人工判读。
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.join(os.getcwd(), "scripts"))
import verify_quotes as VQ

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


def probe(book, want=()):
    d = glob.glob(f"notes/books/*/{book}")[0]
    full = VQ.flat_alpha(VQ.epub_flat_text(glob.glob(os.path.join(d, "library", "*.epub"))[0]))
    print(f"\n{'='*76}\n### {book}   (epub flat {len(full)} 字符)")
    nbad = 0
    for md in sorted(glob.glob(os.path.join(d, "ch*.md"))):
        base = os.path.basename(md)
        for ln, q in md_quotes(md):
            if want and not any(w in base for w in want):
                continue
            segs = [s for s in ELL.split(q) if VQ.flat_alpha(s)]
            bad = [s for s in segs if VQ.flat_alpha(s) not in full]
            if not bad:
                continue
            nbad += 1
            print(f"\n-- {base}:{ln}   [{len(segs)} 段 / {len(bad)} 段查无]")
            for s in bad:
                f = VQ.flat_alpha(s)
                pos = full.find(f[:40])
                print(f"   ✗ 段({len(f)}字符): {s.strip()[:110]!r}")
                if pos >= 0:
                    print(f"     原文前 40 字符能命中，但整段对不上；原文该处：...{full[pos:pos+130]}...")
    print(f"\n→ {book}: 查无引语 {nbad} 条")


if __name__ == "__main__":
    a = sys.argv[1:]
    for b in [x for x in a if not x.startswith("@")]:
        probe(b, [x[1:] for x in a if x.startswith("@")])