#!/usr/bin/env python3
"""全库扫描「同一引语块内同名子项标签重复」（2026-10-19 新增判据的批量取证）。

背景：battle-of-the-round-house 批次的「修复」不是翻译，而是**追加**了第二套无连字符字段，
解析器静默取最后一组 ⇒ 结构性假绿。本脚本按**同块内标签重复**判据扫全库，
输出每个书目录的重复处数——用于判断该缺陷类的全库影响面。

用法：python3 scripts/scan_dup_fields.py [根目录 ...] [--quiet]
"""
import glob
import os
import re
import sys
from collections import defaultdict

BLK = re.compile(r"^> \*\*原句 (\d+):\*\*")
LAB = re.compile(r"^(?:- )?\*\*(中文理解|理解|句子结构|关键词|为什么这样写|表达方式|读者视角提示)\*\*\s*[：:]")
BOOKDIR = re.compile(r"(notes1?/books/[^/]+/[^/]+)/")


def scan_file(path):
    """返回 [(块号, 标签, 出现次数)]"""
    try:
        lines = open(path, encoding="utf-8").read().split("\n")
    except Exception:
        return []
    cur, cnt = None, defaultdict(int)
    out = []
    for l in lines:
        m = BLK.match(l)
        if m:
            cur = int(m.group(1))
            cnt = defaultdict(int)
            continue
        if l.startswith("## "):
            cur = None
            continue
        mm = LAB.match(l.strip())
        if mm and cur is not None:
            cnt[mm.group(1)] += 1
            if cnt[mm.group(1)] == 2:
                out.append((cur, mm.group(1)))
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    roots = args or ["notes/books", "notes1/books"]
    per_book = defaultdict(int)
    per_file = defaultdict(int)
    for root in roots:
        for pat in ("**/ch*.md", "**/00_*.md"):
            for p in glob.glob(os.path.join(root, pat), recursive=True):
                hits = scan_file(p)
                if not hits:
                    continue
                per_file[p] = len(hits)
                rel = p.replace(os.sep, "/")
                m = BOOKDIR.search(rel)
                key = m.group(1) if m else rel
                per_book[key] += len(hits)
    total = sum(per_book.values())
    print(f"=== 同块内重复子项标签：{len(per_book)} 个书目录 / {total} 处 ===")
    for b, n in sorted(per_book.items(), key=lambda x: -x[1]):
        print(f"  {n:5d}  {b}")
    if "--quiet" in sys.argv:
        return
    print("\n--- 明细（每书前 5 处）---")
    for p, n in sorted(per_file.items(), key=lambda x: -x[1])[:40]:
        print(f"  {p}: {n}")


if __name__ == "__main__":
    main()
