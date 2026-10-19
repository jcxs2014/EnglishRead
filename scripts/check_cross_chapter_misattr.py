#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""跨章误标检查器：导航/总结/词表层引用的英文，其实属于别的章

为什么需要这个工具
------------------
子代理在本轮实测中反复报出同一类**真缺陷**（不是工具误报）：
ch48 的导航/一句话总结/词表里挂着 ch52 的句子、ch49 挂着 ch50 的、
ch50 挂着 ch53 的、ch47 挂着 ch42 的、ch54 挂着 ch47/ch51 的……
⇒ 特征：**英文确实在书里，但不在本章**。
   `check_nav_layer` 只能判「全书查无」，**判不出「在别章」**；
   `check_analysis_quotes` 只扫三个分析字段，**不扫导航/总结/词表**。
   ⇒ 这一整类缺陷目前**没有任何工具能抓**。

判据
----
1. 扫描每章 md 的四个「非引语块」层：
   `## 本章导航` / `## 一句话总结` / `## 读者视角提示`（文件级小节） / `## 词汇`
2. 从这些行里抽**引号内英文整段**（≥8 个英文字母）
3. 逐条 flat 比对：
   - 本章 `text/` 命中 → ✅ 正常
   - **别章 `text/` 命中** → ⚠️ **跨章误标**（本工具要抓的）
   - 全书查无 → ❌ 伪造（check_nav_layer 已覆盖）
4. 词表层的例句单独查（`例句（本章）` 列）

用法
----
    python3 scripts/check_cross_chapter_misattr.py "<书目录>" [--file X.md] [--max-list 20]
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

FLAT_STRIP = re.compile(r"[^0-9a-z]+")
QUOTED_RE = re.compile(r'[“"]([^“”"]{6,})[”"]')
# 词表行：| 词条 | 释义 | 例句 |
VOCAB_ROW = re.compile(r'^\|(.+)\|\s*$')


def flat(s: str) -> str:
    return FLAT_STRIP.sub("", s.lower())


def has_en(s: str) -> bool:
    return len(re.findall(r"[A-Za-z]", s)) >= 8


def build_refs(book_dir):
    per_chapter = {}
    for p in sorted(glob.glob(os.path.join(book_dir, "text", "ch*.txt"))):
        ch = os.path.basename(p).split("_")[0]
        per_chapter[ch] = flat(open(p, encoding="utf-8").read())
    return per_chapter


def section_of(line_no, sections):
    for name, (s, e) in sections.items():
        if s <= line_no <= e:
            return name
    return "（未知）"


def main():
    ap = argparse.ArgumentParser(description="跨章误标检查器")
    ap.add_argument("book_dir")
    ap.add_argument("--file")
    ap.add_argument("--max-list", type=int, default=20)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()
    book_dir = args.book_dir

    refs = build_refs(args.book_dir)
    if not refs:
        print("❓ 无参照集：text/ 下没有 ch*.txt ⇒ 无法判定（不是「干净」）")
        return 2
    all_refs = list(refs.values())

    findings = []
    for path in sorted(glob.glob(os.path.join(book_dir, "ch*.md"))):
        name = os.path.basename(path)
        if args.file and name != args.file:
            continue
        ch = name[:4]
        own = refs.get(ch, "")
        lines = open(path, encoding="utf-8").read().split("\n")
        # 章节切分
        sections = {}
        for i, l in enumerate(lines, 1):
            if l.startswith("## "):
                sections[l[3:].strip()] = (i, len(lines))
        in_quote = False
        for i, raw in enumerate(lines, 1):
            s = raw.strip()
            if s.startswith("> **原句"):
                in_quote = True
                continue
            if in_quote:
                if s.startswith(">") or s == "":
                    continue
                in_quote = False
            sec = section_of(i, sections)
            if sec in ("精读", "（未知）"):
                continue
            frags = []
            for qm in QUOTED_RE.finditer(s):
                q = qm.group(1)
                if has_en(q):
                    frags.append(q)
            # 词表例句列（第 3 列起）
            if sec == "词汇" and s.startswith("|"):
                cells = [c.strip() for c in s.strip("|").split("|")]
                if len(cells) >= 3 and has_en(cells[2]):
                    frags.append(cells[2])
            for q in frags:
                f = flat(q)
                if len(f) < 8:
                    continue
                if f in own:
                    continue
                # 找它在哪些章
                hit = [c for c, r in refs.items() if f in r]
                if hit:
                    findings.append((name, i, sec, q, hit))

    print(f"=== 跨章误标检查（{os.path.basename(args.book_dir.rstrip('/'))}）===")
    if not findings:
        print("✅ 未发现跨章误标")
        return 0
    print(f"⚠️ 跨章误标：{len(findings)} 条（英文在书里，但不在本章）")
    by_file = {}
    for name, line, sec, q, hit in findings:
        by_file.setdefault(name, []).append((line, sec, q, hit))
    for name in sorted(by_file):
        items = by_file[name]
        print(f"  {name}（{len(items)} 条）")
        for line, sec, q, hit in items[: args.max_list]:
            print(f"    L{line} [{sec}] 实为 {'/'.join(hit)}：{q[:70]}")
        if len(items) > args.max_list:
            print(f"    …… 另有 {len(items) - args.max_list} 条")
    return 1


if __name__ == "__main__":
    sys.exit(main())
