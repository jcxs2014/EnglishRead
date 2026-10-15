#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""五步审查 b/c 步：第二套实现（不复用 check_chapter_quotes / audit_structure）。
b: 引语归属——每条引语必须在「本章」text 里逐字命中；并报出它在别章的出现情况。
c: 结构——每块必须「引语行 + 4 个分析子项」齐全；编号连续；无重复块。
"""
import re, glob, os, sys, unicodedata

B = "notes/books/mystery-thriller/this-is-the-night-they-come-for-you-by-robert-goddard"

def flat(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-")
    return re.sub(r"[^a-z0-9]", "", s.lower())

texts = {}
for p in glob.glob(os.path.join(B, "text", "ch*.txt")):
    n = int(re.match(r"ch(\d+)", os.path.basename(p)).group(1))
    texts[n] = flat(open(p, encoding="utf-8").read())

SUB = ["**中文理解**：", "**关键词**：", "**为什么这样写**：", "**读者视角提示**："]
issues = []
nq = 0
for p in sorted(glob.glob(os.path.join(B, "ch*.md"))):
    base = os.path.basename(p)
    n = int(re.match(r"ch(\d+)", base).group(1))
    lines = open(p, encoding="utf-8").read().splitlines()
    idx = []
    for i, l in enumerate(lines):
        m = re.match(r"^> \*\*原句 (\d+):\*\* (.+)$", l)
        if m:
            idx.append((i, int(m.group(1)), m.group(2).strip()))
    # 编号连续性
    nums = [x[1] for x in idx]
    if nums != list(range(1, len(nums) + 1)):
        issues.append("c|%s|编号不连续: %s" % (base, nums))
    seen = {}
    for k, (i, num, quote) in enumerate(idx):
        nq += 1
        end = idx[k + 1][0] if k + 1 < len(idx) else len(lines)
        blk = "\n".join(lines[i:end])
        # c: 子项齐全
        for s in SUB:
            if s not in blk:
                issues.append("c|%s|原句%d|缺子项 %s" % (base, num, s))
        # c: 重复块
        f = flat(quote)
        if f in seen:
            issues.append("c|%s|原句%d|与 原句%d 重复" % (base, num, seen[f]))
        seen[f] = num
        # b: 逐片段归属（省略号切段，每段≥12 字符须在本章 text 命中）
        frags = [x for x in re.split(r"…|\.\.\.", quote) if len(flat(x)) >= 12]
        if not frags:
            frags = [quote]
        for fr in frags:
            if flat(fr) not in texts.get(n, ""):
                others = [m for m, t in texts.items() if flat(fr) in t]
                issues.append("b|%s|原句%d|片段不在本章 text: %s | 出现在别章: %s"
                              % (base, num, fr[:70], others))

print("扫 %d 条引语（31 章）" % nq)
print("缺陷 %d 条" % len(issues))
for x in issues:
    print("  " + x)
