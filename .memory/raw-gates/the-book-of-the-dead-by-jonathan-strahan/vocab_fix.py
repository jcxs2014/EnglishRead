#!/usr/bin/env python3
"""词汇表取证器：逐章解析「## 本章词汇」三档表，核对词头与例句。

对不合格的行，列出该章 text/ 里**含该词头的单行原文**（按 AGENTS：例句只能整行复制，
不得跨行拼接、不得追加省略号），供人工挑选替换。

用法：
    python3 vocab_fix.py "<书目录>"            # 列出所有不合格行 + 候选
    python3 vocab_fix.py "<书目录>" --apply    # 用候选里第一条自动替换（谨慎）
"""
import glob
import os
import re
import sys

BOOK = sys.argv[1]
APPLY = "--apply" in sys.argv

RE_ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$")
TIER = re.compile(r"^###\s*(⭐+)\s*(\S+)")
STOP = set("the a an and or but of in on at to for with is was were be been being that this those these "
           "it its as by from not no so if then than there their they them he she his her you your i me my".split())


def flat(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def chapter_text(book, fname):
    cnum = re.match(r"ch(\d+)", fname).group(1)
    buf = ""
    for tp in sorted(glob.glob(os.path.join(book, "text", "ch*.txt"))):
        if os.path.basename(tp).startswith("ch" + cnum + "_"):
            buf += open(tp, encoding="utf-8").read()
    return buf


def chapter_lines(book, fname):
    cnum = re.match(r"ch(\d+)", fname).group(1)
    out = []
    for tp in sorted(glob.glob(os.path.join(book, "text", "ch*.txt"))):
        if os.path.basename(tp).startswith("ch" + cnum + "_"):
            out += [l.strip() for l in open(tp, encoding="utf-8").read().split("\n") if l.strip()]
    return out


bad_rows = []
for md in sorted(glob.glob(os.path.join(BOOK, "ch*.md")),
                 key=lambda x: int(re.search(r"ch(\d+)", x).group(1))):
    fname = os.path.basename(md)
    text = chapter_text(BOOK, fname)
    lines = chapter_lines(BOOK, fname)
    tf = flat(text)
    body = open(md, encoding="utf-8").read().split("\n")
    in_vocab = False
    for i, ln in enumerate(body):
        if re.match(r"^##\s*本章词汇", ln):
            in_vocab = True
            continue
        if in_vocab and re.match(r"^##\s", ln):
            in_vocab = False
        if not in_vocab:
            continue
        m = RE_ROW.match(ln)
        if not m:
            continue
        head, gloss, ex = m.group(1), m.group(2), m.group(3)
        if head in ("词/短语", "词", "词汇") or set(head) <= set("- "):
            continue
        head_flat = flat(head)
        ex_flat = flat(ex)
        problems = []
        if not head_flat:
            problems.append("空词头")
        elif head_flat not in tf:
            problems.append("词头本章查无(A类虚构)")
        if ex.strip() in ("-", "—", "no", "N/A") or "not in text" in ex.lower() \
                or "未出现" in ex or "未在原文" in ex:
            problems.append("例句为占位")
        elif ex_flat and ex_flat not in tf:
            problems.append("例句不命中本章")
        if problems:
            bad_rows.append((fname, i + 1, head, gloss, ex, problems, lines))

print(f"=== 不合格词条行：{len(bad_rows)} ===")
for fname, ln, head, gloss, ex, problems, lines in bad_rows:
    print(f"\n{fname}:{ln}  [{'、'.join(problems)}]")
    print(f"  词头：{head}   释义：{gloss}")
    print(f"  现例句：{ex}")
    if "词头本章查无" not in problems:
        cands = [l for l in lines if flat(head) in flat(l)]
        for c in cands[:3]:
            print(f"  候选：{c[:160]}")
    else:
        print("  候选：词头本章不存在，需换词")
