#!/usr/bin/env python3
"""ch03 块4 引语截短修复：扩引语到覆盖分析所引的整段（text/ 107 + 116 行）。

check_anchor 报「关键词不在本块引语内 → ordered collection」——
「ordered collection」在 text/ 第 107 行（房屋依山而建那段），而引语只截了第 116 行。
⇒ 分析覆盖的是两段，引语只覆盖一段 ⇒ 第 9 条 a2「引语截短」。

片段逐字从 text/ 抽取，不手抄。
"""
import os
import re
import tempfile
import unicodedata

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
B = os.path.join(_ROOT, "notes", "books", "short-story-anthologies",
                 "battle-of-the-round-house-by-tananarive-due")
_TEXTDIR = os.path.join(B, "text")
TEXT = os.path.join(_TEXTDIR, [x for x in os.listdir(_TEXTDIR) if x.startswith("ch03")][0])
MD = os.path.join(B, [x for x in os.listdir(B) if x.startswith("ch03")][0])

WANT = [
    "North of the round house, clustered against the hillside, the ordered collection of "
    "homesteads with stone chimneys promised a warm place to rest.",
    "The round house was as big as a town church, a gathering space and dining hall.",
]


def flat(s):
    return re.sub(r"[^0-9a-z]", "", unicodedata.normalize("NFKD", s).lower())


src = open(TEXT, encoding="utf-8").read()
ft = flat(src)
for w in WANT:
    hit = flat(w) in ft
    print(f"  {'✅' if hit else '❌'} {w[:70]}")
    if not hit:
        raise SystemExit("片段未命中原文，停止")

new_quote = " … ".join(WANT)
md = open(MD, encoding="utf-8").read()
old = '> **原句 4:** "The round house was as big as a town church, a gathering space and dining hall."'
new = f'> **原句 4:** "{new_quote}"'
assert md.count(old) == 1, f"旧引语行命中 {md.count(old)} 次"
md2 = md.replace(old, new)
assert md2.count("\n") == md.count("\n")
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(MD), suffix=".tmp")
with os.fdopen(fd, "w", encoding="utf-8") as f:
    f.write(md2)
os.replace(tmp, MD)
print(f"✅ 已落盘 ch03 块4 引语（{len(new_quote)} 字符 / 2 段）")
