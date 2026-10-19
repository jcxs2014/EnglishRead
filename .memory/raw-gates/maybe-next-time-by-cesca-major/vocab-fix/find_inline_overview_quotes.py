#!/usr/bin/env python3
"""总览三篇里的「行内英文原句」检测（AGENTS 第 9 条 d2 硬性规定）。

d2：三篇总览中任何英文原句**一律**写成独立成行的 `> "…"（chNN）` 引用块，
**禁止嵌在中文正文里**、也禁止塞进表格单元格。
本脚本列出所有**非引用块行**里的英文引号内容。
"""
import os
import re

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
B = os.path.join(_ROOT, "notes", "books", "novels", "maybe-next-time-by-cesca-major")

# 行内英文原句：中文行内出现 "..." 或 "…" 且里面含 ≥2 个英文单词
INLINE = re.compile(r'[""“”]([^""“”\n]{8,})[""“”]')
n = 0
for f in sorted(os.listdir(B)):
    if not f.startswith("00_"):
        continue
    p = os.path.join(B, f)
    for i, line in enumerate(open(p, encoding="utf-8").read().split("\n"), 1):
        s = line.strip()
        if s.startswith(">"):          # 独立引用块 ✓
            continue
        if s.startswith("|"):          # 表格单元格（d2 同样禁止）
            print(f"  ⚠️ 表格内 {f}:{i}  {s[:120]}")
            n += 1
            continue
        for m in INLINE.finditer(line):
            frag = m.group(1)
            words = re.findall(r"[A-Za-z]{2,}", frag)
            # 排除纯中文/纯术语的短引号（如「礼物」）
            if len(words) >= 3:
                print(f"  ❌ 行内引语 {f}:{i}  “{frag[:90]}”")
                n += 1
print(f"\n合计 {n} 处")
