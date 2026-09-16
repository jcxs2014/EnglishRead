#!/usr/bin/env python3
"""批6 (ch17-ch19) 结构复核：块数/四子项/导航/直撇/自标注释/空单元格/中文理解英文泄漏。"""
import re

BOOK = "notes/books/novels/kiss-slay-replay-by-rachel-harrison"
FILES = [
    "ch17 part 2 the unkindness descends.md",
    "ch18 part 2 mouth full of raven beaks.md",
    "ch19 part 2 my time is up.md",
]
NAMES = {"Willa", "Danny", "Ravi", "Steph", "Jace", "Luke", "Cassie", "Wyatt",
         "Evan", "Tanya", "Theo", "Tokyo", "Cass", "Wy"}

for fn in FILES:
    path = f"{BOOK}/{fn}"
    with open(path, encoding="utf-8") as f:
        s = f.read()
    lines = s.split("\n")
    blocks = sum(1 for l in lines if l.startswith("> **原句"))
    subs = {k: sum(1 for l in lines if l.startswith(f"**{k}：**"))
            for k in ("中文理解", "关键词", "为什么这样写", "读者视角提示")}
    nav = sum(1 for l in lines if re.match(r"^- \*\*", l))
    straight = len(re.findall(r"[A-Za-z]'[A-Za-z]", s))
    notes = sum(1 for l in lines if "未出现在原文" in l)
    rows = [l for l in lines if l.startswith("| ") and "词/短语" not in l and not set(l) <= set("|- ")]
    empty = [l[:40] for l in rows if len(l.split("|")) < 5 or not l.split("|")[3].strip()]
    # 中文理解英文泄漏
    leak = []
    for l in lines:
        if l.startswith("**中文理解："):
            body = l.split("：**", 1)[1]
            for w in re.findall(r"[A-Za-z']+", body):
                if w in NAMES:
                    continue
                if w.lower() in ("md", "part", "chapter", "chap", "snapping", "snap"):
                    continue
                leak.append(w)
    print(f"--- {fn} ---")
    print(f"  块={blocks} 四子项={subs} 导航={nav} 词条={len(rows)}")
    print(f"  直撇={straight} 自标注释={notes} 空单元格={len(empty)}")
    if leak:
        print(f"  中文理解英文泄漏={sorted(set(leak))}")
    else:
        print(f"  中文理解英文泄漏=0")
