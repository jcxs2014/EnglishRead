#!/usr/bin/env python3
"""对查无的引语逐字符定位第一个分歧点，打印 md / 原文 两侧各 60 字符。"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.join(os.getcwd(), "scripts"))
import verify_quotes as VQ


def first_diff(a, b):
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return i
    return min(len(a), len(b))


def show(book, mdfile, ln):
    ln = int(ln)
    d = glob.glob(f"notes/books/*/{book}")[0]
    full = VQ.flat_alpha(VQ.epub_flat_text(glob.glob(os.path.join(d, "library", "*.epub"))[0]))
    path = os.path.join(d, mdfile)
    line = open(path, encoding="utf-8").read().split("\n")[ln - 1]
    q = re.sub(r'^>\s*(?:\*{0,2}(?:原句|Quote|引用)\s*\d+\*{0,2}\s*[:：]\s*)?', "", line).strip()
    f = VQ.flat_alpha(q)
    pos = full.find(f[:40])
    seg = full[pos:pos + len(f)]
    i = first_diff(f, seg)
    print(f"\n### {book} :: {mdfile}:{ln}")
    print(f"  首个分歧在展平后第 {i} 字符（占引语 {i*100//len(f)}%）")
    print(f"  md  : ...{f[max(0,i-45):i]}【{f[i:i+45]}】...")
    print(f"  原文: ...{seg[max(0,i-45):i]}【{seg[i:i+45]}】...")


if __name__ == "__main__":
    show(*sys.argv[1:])