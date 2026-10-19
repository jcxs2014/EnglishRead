#!/usr/bin/env python3
"""验证 ch08 恢复块 5 的引语：逐字 + 落在同一自然段内。"""
import os
import re
import unicodedata

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
B = os.path.join(_ROOT, "notes", "books", "novels", "maybe-next-time-by-cesca-major")
T = os.path.join(B, "text")
txt = [x for x in os.listdir(T) if x.startswith("ch08")][0]
src = open(os.path.join(T, txt), encoding="utf-8").read()

Q = ("“I've been shit. And today, I'm so sorry. I feel bad. I know last year . . .” "
     "I didn't finish the sentence, wishing I could erase his hurt expression.")


def flat(s):
    return re.sub(r"[^0-9a-z]", "", unicodedata.normalize("NFKD", s).lower())


paras = [p for p in re.split(r"\n\s*\n", src) if p.strip()]
hits = [i for i, p in enumerate(paras) if flat(Q) in flat(p)]
print(f"自然段总数 {len(paras)} ｜ 引语命中的段序号: {hits}")
if len(hits) != 1:
    print("❌ 必须恰好命中 1 个自然段（跨段拼接红线）")
    raise SystemExit(1)
print("✅ 逐字命中且落在同一自然段内")
print("   该段原文：", paras[hits[0]][:200])
