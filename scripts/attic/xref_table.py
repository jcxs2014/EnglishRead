#!/usr/bin/env python3
"""
xref_table.py — 跨章引用错位对账表（一次性脚本，attic 存档）

## 本书的两套编号（必须先说清）
`第 N 章` = **书内章号**（Prologue 不计，Chapter 1..31）
`chNN`    = **md 文件号 / text 文件号**（ch01=Prologue，ch02=Chapter 1 … ch32=Chapter 31）
换算：`第 N 章` = md ch(N+1)；`chNN` = 书内第 NN−1 章。

## 为什么必须建表
三个批次的子代理合计报出约 60 处「引用落到错章」，而它们的成因是同一个：
写作时把**书内章号**与 **md 文件号**混着用。本脚本把全书每一处
「第 N 章」/「chNN」引用抽出，附上**该处被引句的真实落点**（由 flat 探针在
text/ 全书定位），排成一张可直接改的表。

## 口径（统一，避免多路标准）
- 引用后 200 字符内的英文词序列 → 逐词递增探针 → 找**能 flat 命中最长**的那一段
- 探针在全书**唯一**命中一章 → 落点确定
- 探针多章命中或零命中 → 记为「不可机械判定」，不猜
用法：python3 scripts/attic/xref_table.py "<书目录>" > 报告
"""
import glob
import os
import re
import sys
import unicodedata

BOOK = sys.argv[1]
flat = lambda s: re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).lower())
corp = {}
for f in glob.glob(os.path.join(BOOK, 'text', 'ch*.txt')):
    nn = int(re.match(r'ch(\d+)', os.path.basename(f)).group(1))
    corp[nn] = flat(open(f, encoding='utf-8').read())

REF = re.compile(r'第\s*(\d+)\s*章|ch(\d\d)')
WORD = re.compile(r"[A-Za-z][A-Za-z'\-]{2,}")

rows = []
for path in sorted(glob.glob(os.path.join(BOOK, 'ch*.md')),
                   key=lambda p: int(re.match(r'ch(\d+)', os.path.basename(p)).group(1))):
    name = os.path.basename(path)
    for i, l in enumerate(open(path, encoding='utf-8'), 1):
        for m in REF.finditer(l):
            isbook = bool(m.group(1))
            claim = int(m.group(1)) + 1 if isbook else int(m.group(2))
            ws = WORD.findall(l[m.end():m.end() + 200])
            real, probe = None, ''
            for k in range(len(ws), 2, -1):
                pr = flat(' '.join(ws[:k]))
                if len(pr) < 16:
                    continue
                hits = sorted(h for h, c in corp.items() if pr in c)
                if len(hits) == 1:
                    real, probe = hits[0], ' '.join(ws[:k])
                    break
            rows.append((name, i, m.group(0), '书内' if isbook else '文件',
                         claim, real, probe))

ok = [r for r in rows if r[5] == r[4]]
bad = [r for r in rows if r[5] and r[5] != r[4]]
unk = [r for r in rows if not r[5]]

print("# 跨章引用对账总表\n")
print(f"总计 {len(rows)} 处 ｜ 落点一致 {len(ok)} ｜ **错位 {len(bad)}** ｜ 不可机械判定 {len(unk)}\n")
print("## 错位明细（可直接改）\n")
print("| 文件 | 行 | 声称 | 口径 | 标称 md | 实落 md | 实落书内 | 被引片段 |")
print("|---|---|---|---|---|---|---|---|")
for r in bad:
    print(f"| {r[0]} | L{r[1]} | {r[2]} | {r[3]} | ch{r[4]:02d} | **ch{r[5]:02d}** | "
          f"第 {r[5]-1} 章 | `{r[6][:52]}` |")
print("\n## 不可机械判定（需人工）\n")
print("| 文件 | 行 | 声称 | 被引片段 |")
print("|---|---|---|---|")
for r in unk:
    seg = r[6] or '（其后 200 字符无足够英文）'
    print(f"| {r[0]} | L{r[1]} | {r[2]} | `{seg[:56]}` |")
