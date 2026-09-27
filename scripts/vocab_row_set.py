#!/usr/bin/env python3
"""按行号改写 md 的词表行，避免长例句 patch 匹配失败。

用法: python3 scripts/vocab_row_set.py <md> <行号> '<新行全文>'
行号从 1 起，与 grep -n 一致。
"""
import sys
from pathlib import Path

p = Path(sys.argv[1])
n = int(sys.argv[2])
new = sys.argv[3]
lines = p.read_text(encoding="utf-8").split("\n")
old = lines[n - 1]
if not old.startswith("|"):
    sys.exit(f"第 {n} 行不是表格行: {old[:60]}")
lines[n - 1] = new
p.write_text("\n".join(lines), encoding="utf-8")
print(f"行 {n} 已改写\n  旧: {old[:70]}\n  新: {new[:70]}")
