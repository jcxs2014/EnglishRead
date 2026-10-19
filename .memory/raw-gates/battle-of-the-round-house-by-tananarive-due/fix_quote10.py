#!/usr/bin/env python3
"""ch03 块10 引语截短修复：按第 9 条 a2 把引语扩到覆盖分析所引的整段。

⚠️ 片段**逐字**从 text/ch03_zipporah.txt 抽取（不手抄），拼装后逐片段独立取证。
"""
import os
import re
import unicodedata

# ⚠️ 绝对路径 + listdir 取真实名：本机**偶发**「同一字面量相对路径 exists=False，
#    而 listdir 出的同名立即可用」（2026-10-19 连续 3 次实测，且失败点随机漂移）。
_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
B = os.path.join(_ROOT, "notes", "books", "short-story-anthologies",
                 "battle-of-the-round-house-by-tananarive-due")
_TEXTDIR = os.path.join(B, "text")
TEXT = os.path.join(_TEXTDIR, [x for x in os.listdir(_TEXTDIR) if x.startswith("ch03")][0])
MD = os.path.join(B, [x for x in os.listdir(B) if x.startswith("ch03")][0])

# 5 个片段：每段都是原文里的**连续**一段
WANT = [
    "By morning, only trampled grasses and a few pocks in the round house from gunshots remained",
    "she was amazed to see no bodies. No blood. No hoofprints in the newly swept path.",
    "“Where they won’t be found,” Papa said, rubbing her hair.",
    "“Did you . . . ‘talk’ to those bulls when they were running at you?”",
    "For the rest of her life, she wouldn’t be quite sure.",
    "But on that morning after the battle, Lucy could only smile.",
]


def flat(s):
    return re.sub(r"[^0-9a-z]", "", unicodedata.normalize("NFKD", s).lower())


src = open(TEXT, encoding="utf-8").read()
ft = flat(src)
print("=== 片段取证（逐条独立 flat 命中）===")
ok = True
for w in WANT:
    hit = flat(w) in ft
    ok &= hit
    print(f"  {'✅' if hit else '❌'} {w[:70]}")
if not ok:
    raise SystemExit("片段未全部命中原文，停止")

new_quote = " … ".join(WANT)
print(f"\n新引语长度 {len(new_quote)} 字符 / {len(WANT)} 段")

md = open(MD, encoding="utf-8").read()
old = '> **原句 10:** "But on that morning after the battle, Lucy could only smile."'
new = f'> **原句 10:** "{new_quote}"'
assert md.count(old) == 1, f"旧引语行命中 {md.count(old)} 次"
md2 = md.replace(old, new)
assert md2.count("\n") == md.count("\n"), "行数变化"
fd, tmp = __import__("tempfile").mkstemp(dir=os.path.dirname(MD), suffix=".tmp")
with __import__("os").fdopen(fd, "w", encoding="utf-8") as f:
    f.write(md2)
__import__("os").replace(tmp, MD)
print("✅ 已落盘 ch03 块10 引语")
