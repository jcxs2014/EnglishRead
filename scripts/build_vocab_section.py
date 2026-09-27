#!/usr/bin/env python3
"""生成 md 的「本章词汇」三档小节（词头+例句由脚本从 text/ 逐字取出，释义由调用方提供）。

用法:
  python3 scripts/build_vocab_section.py <md> <NN> '<head>释义' '<head>释义' ...
  或 python3 scripts/build_vocab_section.py <md> <NN> --glosses <json 文件>

未提供释义的词头不会被写入（宁缺毋造），脚本会打印缺哪些释义。
"""
import json
import re
import subprocess
import sys
from pathlib import Path

md = Path(sys.argv[1])
ch = sys.argv[2]
gloss_arg = sys.argv[3:]

if gloss_arg and gloss_arg[0] == "--glosses":
    glosses = json.load(open(gloss_arg[1], encoding="utf-8"))
else:
    glosses = json.loads(" ".join(gloss_arg)) if glosses_arg else {}

out = subprocess.run(
    ["python3", "scripts/vocab_candidates.py", str(md.parent), "--ch", ch, "--tiers", "--limit", "12"],
    capture_output=True, text=True, check=True).stdout

rows, cur = [], None
for line in out.split("\n"):
    if line.startswith("###"):
        cur = "高级" if "⭐⭐⭐" in line else ("进阶" if "进阶" in line else "基础")
    elif line.startswith("| "):
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) >= 3 and c[0] != "词/短语" and not set(c[0]) <= set("-: "):
            rows.append((cur, c[0], c[2].replace("（释义待填）", "").strip()))

missing = [h for _, h, _ in rows if h not in glosses]
if missing:
    print("⚠️ 缺释义（这些词不会写入）: " + ", ".join(missing))

tables = {k: [] for k in ("高级", "进阶", "基础")}
for tier, head, ex in rows:
    if head in glosses:
        tables[tier].append(f"| {head} | {glosses[head]} | {ex} |")

sec = ["## 本章词汇", ""]
for tier, star in (("高级", "⭐⭐⭐"), ("进阶", "⭐⭐ 进阶"), ("基础", "⭐ 基础")):
    sec += [f"### {star}", "", "| 词/短语 | 释义 | 例句 |", "|---|---|---|"]
    sec += tables[tier] or [f"| （本章无{ '高级' if tier=='高级' else tier}词） | | |"]
    sec += [""]

text = md.read_text(encoding="utf-8")
i = text.index("## 本章词汇")
j = text.index("## 一句话总结")
md.write_text(text[:i] + "\n".join(sec) + "\n" + text[j:], encoding="utf-8")
print(f"已写入 {md.name}: 高级 {len(tables['高级'])} / 进阶 {len(tables['进阶'])} / 基础 {len(tables['基础'])}")
