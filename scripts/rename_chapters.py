#!/usr/bin/env python3
"""把章节文件统一改名成 `chNN <place> <month year>.md`（抬头从 text/ 逐字读出，不手打）。

为什么需要：本书三条时间线（1932 柏林 / 1936 巴黎 / 1944 纽约）**抬头是唯一有用的标识**，
而 `new_chapter.py` 早期版本从 text 文件名派生 slug ⇒ 产出 `ch07 chapter 6.md`，
与手写的 ch01–06（`ch01 new york city november 1943.md`）不一致。

同时校验三方一致（防章节偏移）：
  ① 文件名里的 NN ② H1 里的 `NN.` ③ text/ 首行是 Prologue / Chapter N / Epilogue
  抬头 = text/ 里前几个非空行中，形如地点 / 月份 年的那两行。

用法:
  python3 scripts/rename_chapters.py <书目录> [--check]
"""
import re
import sys
from pathlib import Path

book = Path(sys.argv[1])
check_only = "--check" in sys.argv
texts = sorted((book / "text").glob("ch[0-9][0-9]_*.txt"),
                key=lambda x: int(x.stem[2:4]))
problems = []
plan = []

for t in texts:
    nn = int(t.stem[2:4])
    lines = [l.strip() for l in t.read_text(encoding="utf-8").split("\n") if l.strip()]
    head = lines[0]
    # 抬头：紧随标题之后的连续短行（地点 / 月份 年）
    place = next((l for l in lines[1:4] if not re.fullmatch(r"[A-Z][a-z]+ \d{4}", l)
                  and not l.startswith("Chapter") and l != "Prologue" and l != "Epilogue"), "")
    date = next((l for l in lines[1:4] if re.fullmatch(r"[A-Z][a-z]+ \d{4}", l)), "")
    if not place or not date:
        problems.append(f"ch{nn:02d}: 抬头读不出（place={place!r} date={date!r}）")
        continue
    slug = f"{place} {date}".lower()
    slug = re.sub(r"[^a-z0-9 ]", "", slug)
    slug = re.sub(r"\s+", " ", slug).strip()
    newname = f"ch{nn:02d} {slug}.md"
    cur = book / f"ch{nn:02d} {head.lower().replace(' ', '-')}.md"
    existing = sorted(book.glob(f"ch{nn:02d} *.md"))
    old = existing[0] if existing else None
    # 三方一致：H1 编号 vs text 首行
    if old:
        m = re.search(r"^# (\d+)\.", old.read_text(encoding="utf-8"), re.M)
        if not m or int(m.group(1)) != nn:
            problems.append(f"ch{nn:02d}: H1 编号 {m.group(1) if m else '缺'} ≠ 文件号 {nn}")
        m2 = re.fullmatch(r"(?:Chapter (\d+)|Prologue|Epilogue)", head)
        if m2 and m2.group(1) and int(m2.group(1)) != nn - 1:
            problems.append(f"ch{nn:02d}: text 首行 {head!r} 与文件号不符（期望 Chapter {nn - 1}）")
    if old and old.name == newname:
        continue
    plan.append((old, book / newname, nn))

for old, new, nn in plan:
    if old is None:
        problems.append(f"ch{nn:02d}: 缺 md 文件")
        continue
    if check_only:
        print(f"would rename: {old.name} -> {new.name}")
    else:
        old.rename(new)
        print(f"renamed: {old.name} -> {new.name}")

for p in problems:
    print("❌ " + p)
print(f"=== 待改名 {len(plan)} / 问题 {len(problems)} ===")
sys.exit(2 if problems else 0)
