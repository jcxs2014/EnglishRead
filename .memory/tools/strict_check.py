#!/usr/bin/env python3
"""EnglishRead 逐章精读严格自检（比 gate.sh 更严的三项）
1) 引语与词条例句必须**逐字**出现在**本章** text/ 提取件里
2) 词条「词头」必须在本章原文出现（gate 的 check_vocab 对词形变化会漏）
3) 分析层（中���理解／为什么这样写／读者视角提示）英文字符占比 <= 30%
另查 U+FFFD 损坏字符。
用法: python3 strict_check.py <书目录>
"""
import re, sys, glob, os

book = sys.argv[1] if len(sys.argv) > 1 else "."
import os
problems = 0
for srcf in sorted(glob.glob(os.path.join(book, "text", "ch*.txt"))):
    ch = int(os.path.basename(srcf)[2:4])
    src = open(srcf, encoding="utf-8").read()
    mdfs = glob.glob(os.path.join(book, f"ch{ch:02d} *.md"))
    if not mdfs:
        continue  # 该章尚未开写
    md = open(mdfs[0], encoding="utf-8").read()
    quotes = re.findall(r'> \*\*原句 \d+:\*\* "(.*)"\n', md)
    rows = [r for r in re.findall(r'^\| ([^|]+?) \| ([^|]+?) \| (.+?) \|$', md, re.M)
            if r[0] not in ("词/短语", "---")]
    errs = []
    if len(quotes) != 10:
        errs.append(f"引语块数 {len(quotes)} ≠ 10")
    if len(rows) != 30:
        errs.append(f"词条数 {len(rows)} ≠ 30")
    for i, q in enumerate(quotes, 1):
        if q not in src:
            errs.append(f"引语{i} 非本章逐字")
    for w, g, ex in rows:
        ex = ex.strip()
        if ex not in src:
            errs.append(f"词条例句[{w}] 非本章逐字")
        if w.lower() not in src.lower():
            errs.append(f"词头[{w}] 本章原文查无")
        elif w.lower() not in ex.lower():
            errs.append(f"词头[{w}] 不在它自己的例句里")
    for i, l in enumerate(md.split("\n"), 1):
        if "�" in l:
            errs.append(f"行{i} U+FFFD 损坏字符")
        m = re.match(r'\*\*(中文理解|为什么这样写|读者视角提示)：\*\*(.*)', l)
        if m:
            t = m.group(2)
            han = len(re.findall(r'[一-鿿]', t)); eng = len(re.findall(r'[A-Za-z]', t))
            r = eng / (han + eng) if han + eng else 0
            if r > 0.30:
                errs.append(f"行{i} [{m.group(1)}] 英字占比 {r:.0%} > 30%")
    status = "✅" if not errs else "❌"
    print(f"{status} ch{ch:02d}  引语{len(quotes)} 词条{len(rows)}  问题{len(errs)}")
    for e in errs:
        print("      -", e)
    problems += len(errs)
print("=== 问题合计:", problems, "===")
sys.exit(1 if problems else 0)
