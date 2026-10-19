#!/usr/bin/env python3
"""battle-of-the-round-house 引语逐片段独立取证（一次性复核工具）。

不采信 verify_quotes 的结论——逐条把每个引语的**每个片段**（`…` 分隔）拿到
本章 text/ 里 flat 比对，验证「多段引语的每一段都逐字来自本章原文」。
"""
import os
import re
import unicodedata

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
B = os.path.join(_ROOT, "notes", "books", "short-story-anthologies",
                 "battle-of-the-round-house-by-tananarive-due")
T = os.path.join(B, "text")


def flat(s):
    return re.sub(r"[^0-9a-z]", "", unicodedata.normalize("NFKD", s).lower())


texts = {}
for x in os.listdir(T):
    m = re.match(r"ch(\d+)_", x)
    if m:
        texts[int(m.group(1))] = flat(open(os.path.join(T, x), encoding="utf-8").read())

tot_lines = tot_frags = 0
bad = []
multi = []
for f in sorted(os.listdir(B)):
    m = re.match(r"ch(\d+)", f)
    if not m or not f.endswith(".md"):
        continue
    cn = int(m.group(1))
    t = open(os.path.join(B, f), encoding="utf-8").read()
    # 引语行：`> **原句 N:** <内容>` —— 口径**放宽**到整行（实测有三种形态：
    #   ① 整行被 "…" 全包裹  ② 引语跨多行（长引语）  ③ 引号只包引语本体、
    #   后接叙述（如 `"Leave us alone!" Lucy shouted.`）——门禁口径能处理，
    #   复核脚本若只认 ① 会漏 3 条（2026-10-19 实测）。
    for mm in re.finditer(r'^> \*\*原句 (\d+):\*\*\s*(.*)$', t, re.M):
        tot_lines += 1
        q = mm.group(2).strip()
        if q.startswith('"'):
            q = q[1:]
            # 去掉尾部收尾引号（若整行以 " 结尾）
            if q.endswith('"'):
                q = q[:-1]
        frags = [x for x in re.split(r"\s*…\s*", q) if x.strip()]
        tot_frags += len(frags)
        if len(frags) > 1:
            multi.append((f, mm.group(1), len(frags)))
        for fr in frags:
            if flat(fr) not in texts.get(cn, ""):
                bad.append((f, mm.group(1), fr[:70]))

print(f"引语行 {tot_lines} ｜ 片段 {tot_frags} ｜ 多段引语 {len(multi)}")
for x in multi:
    print(f"   多段: {x[0]} 原句{x[1]} = {x[2]} 段")
print(f"逐片段不命中本章 text/ 的: {len(bad)}")
for b in bad:
    print("  ❌", b)
