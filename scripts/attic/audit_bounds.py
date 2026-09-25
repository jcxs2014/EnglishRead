#!/usr/bin/env python3
"""
audit_bounds.py v3 — 引语边界对齐检查（一次性脚本，attic 存档）

## 为什么需要它
`verify_quotes` / `check_chapter_quotes` / `selfcheck` 的全串 sweep 都用
「引语 flat 后是否是章节 flat 的**子串**」判定。本书 ch26 块4 因此漏网：
    md   : "Hate it here. Will you take me away …"   → flat = hateitherewill…
    原文 : "I hate it here. Will you take me away …"  → flat = ihateitherewill…
`hateitherewill…` 确实是原文子串，三个工具**同时放行**，
而真实缺陷是引语**首词被吞**（漏了原文的 "I"）。

## v3 口径
1. 弯撇号/弯引号归一为 ASCII（消除纯形态差异的假警报）
2. 引语编成正则：词与词之间允许任意非词字符；词内保留连字符（déjà-vu / twenty-five）
3. 在**原文层**匹配后，检查匹配串前后一字符是否仍是词字符 → 吞词
4. 引语首字母为小写而原文对应处为大写 → 句中截断未加 `…`（大小写敏感，不归一）
用法：python3 scripts/attic/audit_bounds.py "<书目录>"
"""
import glob
import os
import re
import sys

BOOK = sys.argv[1]

# 只归一撇号与引号；**不**把破折号归一成 '-'，否则 "killed—the" 会被当成一个词
NORM = {'\u2019': "'", '\u2018': "'", '\u201c': '"', '\u201d': '"'}
# 边界判定用的词字符集：不含 '-'（连字符在词内已由 TOKEN 处理，
# 而引语若真在连字符处被截断，flat sweep 已能发现，不必在此报）
WD = r"[A-Za-z0-9']"
TOKEN = re.compile(r"[A-Za-z0-9'\u00c0-\u024f]+(?:-[A-Za-z0-9'\u00c0-\u024f]+)*")
BLOCK = re.compile('^>\\s*\\*\\*原句\\s*(\\d+)\\s*[:：]\\*\\*\\s*(.*)$')

corp = {}
for f in glob.glob(os.path.join(BOOK, 'text', 'ch*.txt')):
    nn = int(re.match(r'ch(\d+)', os.path.basename(f)).group(1))
    t = open(f, encoding='utf-8').read()
    for a, b in NORM.items():
        t = t.replace(a, b)
    corp[nn] = t


def tokens(q):
    for a, b in NORM.items():
        q = q.replace(a, b)
    return TOKEN.findall(q)


LEFT = RIGHT = CASE = MISS = 0
for path in sorted(glob.glob(os.path.join(BOOK, 'ch*.md')),
                   key=lambda p: int(re.match(r'ch(\d+)', os.path.basename(p)).group(1))):
    name = os.path.basename(path)
    nn = int(re.match(r'ch(\d+)', name).group(1))
    for i, l in enumerate(open(path, encoding='utf-8'), 1):
        m = BLOCK.match(l)
        if not m:
            continue
        n, q = m.group(1), m.group(2).strip()
        for seg in re.split(r'\s*…\s*', q):          # 省略号分段各自对齐
            parts = tokens(seg)
            if len(parts) < 2:
                continue
            rx = r'\W+'.join(re.escape(p) for p in parts)
            hits = list(re.finditer(rx, corp[nn]))
            if not hits:
                MISS += 1
                print(f"  ✗ 未命中 {name} 块{n}：{seg[:76]}")
                continue
            h = hits[0]
            before = corp[nn][h.start() - 1] if h.start() > 0 else ''
            after = corp[nn][h.end()] if h.end() < len(corp[nn]) else ''
            if before and re.match(WD, before):
                LEFT += 1
                print(f"  ✗ 左边界吞词 {name} 块{n}")
                print(f"      原文: …{corp[nn][max(0, h.start() - 18):h.start() + 32]}…")
                print(f"      引语: {seg[:88]}")
            if after and re.match(WD, after):
                RIGHT += 1
                print(f"  ✗ 右边界吞词 {name} 块{n}")
                print(f"      原文: …{corp[nn][h.start():h.end() + 18]}…")
                print(f"      引语: {seg[:88]}")
            if parts[0][:1].islower() and h.start() > 0 and corp[nn][h.start()].isupper():
                CASE += 1
                print(f"  ⚠ 句中截断未标 … {name} 块{n}：原文此处是大写 "
                      f"{corp[nn][h.start()]!r}，引语写成小写")
                print(f"      引语: {seg[:88]}")

print(f"\n左边界吞词 {LEFT} / 右边界吞词 {RIGHT} / 句中截断未标 {CASE} / 未命中 {MISS}")
print('AUDIT_BOUNDS ' + ('PASS' if (LEFT + RIGHT + CASE + MISS) == 0 else 'FAIL'))
sys.exit(1 if (LEFT + RIGHT + CASE + MISS) else 0)
