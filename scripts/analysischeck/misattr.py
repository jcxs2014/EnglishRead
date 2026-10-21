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
CJK_RE = re.compile(r"[一-鿿]")

# ⚠️ 2026-10-21：中文写法的章号标注（第二十二章 / 第14章 / 第二章）。
#    本库大量精读在行内用「第N章」而非「chNN」标注跨章回指，
#    只认 chNN ⇒ 把合规回指误报成「未标 chNN 的跨章误标」。
CN_NUM = {"零": 0, "一": 1, "二": 2, "两": 2, "三": 3, "四": 4, "五": 5,
          "六": 6, "七": 7, "八": 8, "九": 9}
CN_CHAP_RE = re.compile(r"第\s*([0-9]{1,3}|[零一二两三四五六七八九十]{1,4})\s*章")


def flat(s: str) -> str:
    return FLAT_STRIP.sub("", s.lower())


def has_en(s: str) -> bool:
    """片段是否算「英文原句」——**必须不含汉字**。

    ⚠️ 2026-10-21 修正：本工具原先只看「≥8 个英文字母」，
    于是 `**中文理解**：Diana 问演出；Alba "bad"…` 这类
    **中文译文被引号包住**的写法被当成英文原句去别章比对 → 报「跨章误标」假红。
    ⇒ 与 `analysis_quotes.py`（2026-10-19 已修）**对齐**：含汉字 ⇒ 不是英文原句。
    """
    if CJK_RE.search(s):
        return False
    return len(re.findall(r"[A-Za-z]", s)) >= 8


def cn_to_int(s: str) -> int | None:
    """中文数字 → int（支持 1–99 常见的「十」「十四」「二十二」写法）。"""
    if s.isdigit():
        return int(s)
    if not s or any(c not in CN_NUM and c != "十" for c in s):
        return None
    if "十" not in s:
        n = 0
        for c in s:
            n = n * 10 + CN_NUM[c]
        return n
    head, _, tail = s.partition("十")
    tens = CN_NUM[head] if head else 1
    ones = CN_NUM[tail] if tail else 0
    return tens * 10 + ones


def has_chapter_label(line: str, ch: str) -> bool:
    """行内是否已标出该章号——**ASCII `chNN` 与中文「第N章」都算**。

    ⚠️ 2026-10-21：原先只认 `chNN`。本库行内大量用「第二十二章」标注，
    只认 chNN ⇒ 合规回指被误报成「未标注的跨章误标」。
    """
    m = re.search(rf"(?<![A-Za-z0-9]){re.escape(ch)}(?![A-Za-z0-9])", line)
    if m:
        return True
    want = ch[2:] if ch.startswith("ch") else ch
    want_int = int(want) if want.isdigit() else None
    for cm in CN_CHAP_RE.finditer(line):
        n = cn_to_int(cm.group(1))
        if n is not None and want_int is not None and n == want_int:
            return True
    return False


def looks_like_quotation(q: str) -> bool:
    """引号里的内容**像不像一句引语**（而不是一个概括词/术语/书名）。

    ⚠️ 2026-10-21 修正：原先只按「≥8 个英文字母」判定，于是导航层
    `- **人物弧线**：Alba 从"需要母亲代看"到"拒绝 compromise"` 里的
    **概括词**（compromise / practical / fainting / confused / terrific /
    traumatized）被当成引语去别章比对 → 报「跨章误标」假红。
    实测抽样 60 本：修复后告警 261 条里 120 条（46%）是这类概括词。

    判据（收窄，只排除明显不是引语的）：
      ① **≤2 个词且不含句内标点** ⇒ 概括词/术语/标签（如 "incident"、
         "Inexistence"、"Muriel Pendrake"、"identity shifts"）；
      ② **首字母大写但其余小写、且不含任何引号内的大写实词** ⇒ 专名/标签。
    ⇒ 「Don't trust them」这种 3 词但带撇号与动词的仍算引语（保留）。
    ⇒ **3 词不动**：实测 3 词片段里既有标签也有真引语
      （"Perception is reality" / "everything is fine" / "such was life"），
      按词数一刀切会把真引语一起放过 ⇒ 只收窄到 ≤2。
    """
    if not q:
        return False
    words = q.split()
    has_inner_punct = any(c in q for c in ".?!;:,—–")
    if len(words) <= 2 and not has_inner_punct:
        return False
    return True


def build_refs(book_dir):
    per_chapter = {}
    for p in sorted(glob.glob(os.path.join(book_dir, "text", "ch*.txt"))):
        # ⚠️ 2026-10-21 修正：原先用 `os.path.basename(p).split("_")[0]` 取章号。
        #   本库 `text/` 文件名有两种形态：
        #     `ch04_chapter_4.txt`（下划线）→ split("_")[0] = "ch04" ✅
        #     `ch01 series editors foreword.txt`（**空格**）→ split("_")[0] = **整个文件名** ❌
        #   ⇒ 键与 md 侧的 `name[:4]`（"ch01"）对不上 ⇒ `refs.get(ch)` 恒为空 ⇒
        #   **本章的每一句都被判成「他章命中」** ⇒ 假红成片。
        #   改为统一用正则取 `chNN` 前缀。
        m = re.match(r"(ch\d{1,3})", os.path.basename(p))
        if not m:
            continue
        ch = m.group(1)
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
        # ⚠️ 2026-10-21 修正：原先写成 `sections[l[3:].strip()] = (i, len(lines))`
        #   ⇒ **每个 H2 的 end 都被设成文件末尾** ⇒ `section_of()` 永远返回
        #   **第一个 H2**（`## 本章导航`）⇒ 所有精读层的行都被误报成「本章导航」。
        #   正确做法：记下一个 H2 的行号作为上一个 H2 的 end。
        h2s = [(i, l[3:].strip()) for i, l in enumerate(lines, 1) if l.startswith("## ")]
        sections = {}
        for idx, (i, name) in enumerate(h2s):
            end = h2s[idx + 1][0] - 1 if idx + 1 < len(h2s) else len(lines)
            sections[name] = (i, end)
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
            is_vocab_row = s.startswith("|")
            # ⚠️ 2026-10-21：词表节名不止「词汇」一种（本书用「词汇分级」，
            #   全库 novels 分布 本章词汇/词汇/词汇分级/词汇表）⇒ 按前缀认。
            is_vocab_sec = sec.startswith("词汇")
            if not (is_vocab_sec and is_vocab_row):
                # 词表行由下面的「例句列」分支单独处理：
                # 词条列与**释义列**里的引号内容（如 `文中指"Wicker Men"派对`）
                # 是释义不是引语 ⇒ 走通用扫描会把它们当引语报「跨章误标」。
                for qm in QUOTED_RE.finditer(s):
                    q = qm.group(1)
                    if has_en(q) and looks_like_quotation(q):
                        frags.append(q)
            # 词表例句列（第 3 列起）
            if is_vocab_sec and is_vocab_row:
                cells = [c.strip() for c in s.strip("|").split("|")]
                if len(cells) >= 3 and has_en(cells[2]) and looks_like_quotation(cells[2]):
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
                    # ⚠️ 2026-10-19：块内**已标出 chNN**的跨章回指是**合规**的
                    #（读者知道引自别章）⇒ 与「真误标」分开列。
                    # ⚠️ 2026-10-21：中文「第N章」标注同样算合规（见 has_chapter_label）。
                    labeled = any(has_chapter_label(s, c) for c in hit)
                    findings.append((name, i, sec, q, hit, labeled))

    print(f"=== 跨章误标检查（{os.path.basename(args.book_dir.rstrip('/'))}）===")
    unlabeled = [f for f in findings if not f[5]]
    labeled = [f for f in findings if f[5]]
    if unlabeled:
        print(f"❌ 跨章误标（块内**未标 chNN**，读者会误读为本章引文）：{len(unlabeled)} 条")
        by_file = {}
        for name, line, sec, q, hit, _l in unlabeled:
            by_file.setdefault(name, []).append((line, sec, q, hit))
        for name in sorted(by_file):
            items = by_file[name]
            print(f"  {name}（{len(items)} 条）")
            for line, sec, q, hit in items[: args.max_list]:
                print(f"    L{line} [{sec}] 实为 {'/'.join(hit)}：{q[:70]}")
            if len(items) > args.max_list:
                print(f"    …… 另有 {len(items) - args.max_list} 条")
    if labeled:
        print(f"ℹ️ 跨章回指**已标注**（块内已标 chNN）：{len(labeled)} 条 —— 合规，不判红")
        if args.quiet:
            pass
        else:
            by_file = {}
            for name, line, sec, q, hit, _l in labeled:
                by_file.setdefault(name, []).append((line, sec, q, hit))
            for name in sorted(by_file):
                items = by_file[name]
                print(f"  {name}（{len(items)} 条）")
                for line, sec, q, hit in items[: args.max_list]:
                    print(f"    L{line} [{sec}] 实为 {'/'.join(hit)}：{q[:70]}")
                if len(items) > args.max_list:
                    print(f"    …… 另有 {len(items) - args.max_list} 条")
    if not findings:
        return 0
    return 1 if unlabeled else 0


if __name__ == "__main__":
    sys.exit(main())
