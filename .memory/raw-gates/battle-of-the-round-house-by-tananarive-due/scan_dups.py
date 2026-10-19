#!/usr/bin/env python3
"""一次性勘查：battle-of-the-round-house 的重复子项字段分布（不入库脚本）。"""
import glob
import os
import re

B = 'notes/books/short-story-anthologies/battle-of-the-round-house-by-tananarive-due'
DUP = re.compile(r"^\*\*(中文理解|句子结构|关键词|为什么这样写|表达方式|读者视角提示)\*\*[：:]")
STD = re.compile(r"^-\s*\*\*(中文理解|句子结构|关键词|为什么这样写|表达方式|读者视角提示)\*\*[：:]")

files = sorted(glob.glob(os.path.join(B, 'ch*.md'))) + sorted(glob.glob(os.path.join(B, '00_*.md')))
for f in files:
    lines = open(f, encoding='utf-8').read().split('\n')
    hits = [(i, l) for i, l in enumerate(lines, 1) if DUP.match(l)]
    if not hits:
        continue
    print(f"\n{os.path.basename(f)}: 重复字段 {len(hits)} 行")
    cur = ''
    for i, l in enumerate(lines, 1):
        if l.startswith('## '):
            cur = l.strip()
        if DUP.match(l):
            lab = DUP.match(l).group(1)
            print(f"   行{i}  [{cur}]  {lab}")
