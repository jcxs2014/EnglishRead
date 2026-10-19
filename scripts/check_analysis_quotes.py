#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""分析层英文取证检查器：分析层里的英文是否真的在原文里

为什么需要这个工具
------------------
AGENTS 8.2 禁令 3 明说：「**禁令 3 是本库唯一『事后无低成本机检』的缺陷类**」——
引语层有六道门禁（verify_quotes / check_chapter_quotes / sweep_full …），
但**分析层**（中文理解 / 为什么这样写 / 读者视角提示）里出现的英文
**六道门禁一条都不查**（`sweep_analysis_inline` 只判逐字/跨章/拼接，
`check_nav_layer` 只查导航层）。

⇒ 大规模改写分析层时，**最容易制造伪造英文**：
   凭印象写一句「Emma 的 "I knew I had to allow it"」——原文里根本没这句。
   这类缺陷**全库机械层抓不到**，只能靠本工具把候选捞出来人工判。

两档输出
--------
❌ **疑似伪造**（退出码 1）：**引号内**的英文整段，在**全书的 text/** 里都查无。
   ⇒ 引号里的英文按 AGENTS 8.2 禁令 3 必须**整段逐字复制**，
   查无就是伪造（或把别的书/别的章的句子搬进来了）。
   ⚠️ 少数是**跨章引用**（本块在讲别章的事）——那必须**在本块里标出 chNN**，
   否则读者会误以为引的是本章。

⚠️ **待判**（不判红）：**裸英文词组**（不在引号里的分析术语、跨章短引、
   语法记法）。裸词组在分析层是常见且合法的（`verb`、`free indirect discourse`），
   本工具**不判红**，只列出供人工扫一眼。

用法
----
    python3 scripts/check_analysis_quotes.py "<书目录>" [--quiet] [--max-list 40]
    python3 scripts/check_analysis_quotes.py "<书目录>" --file "ch49 the gift day.md"
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

# 块内三个分析字段（`**中文理解**：` / `**中文理解**:` / 裸 `中文理解：` 都认）
FIELD_RE = re.compile(
    r'^(?:\*\*)?(中文理解|为什么这样写|读者视角提示)(?:\*\*)?\s*[：:]\s*(.*)$'
)
BLOCK_RE = re.compile(r'^> \*\*原句 (\d+):\*\*')
# 引号内英文整段（弯引号 / 直引号 / 书名号）
QUOTED_RE = re.compile(r'[“"「]([^”"」]{6,})[”"」]')
# 裸英文词组
BARE_RE = re.compile(r"\b[A-Za-z][A-Za-z'’-]*(?:\s+[A-Za-z][A-Za-z'’-]*){2,}\b")
# 汉字
CJK = re.compile(r'[一-鿿]')

# 本库惯用的语法术语/句式记法——不是引文，不该判伪造
TERMINOLOGY = {
    "neither nor", "how adj", "not but", "adj adv", "subject verb",
    "present perfect", "past perfect", "used to", "there is", "there are",
    "n n", "v ing", "v ed", "n s", "adj comp", "adj sup",
    "free indirect discourse", "present day", "present day crisis",
    "loop iteration", "first person", "third person", "close third",
    "first past", "past year anchor", "dateversary",
}

FLAT_STRIP = re.compile(r"[^0-9a-z]+")


def flat(s: str) -> str:
    return FLAT_STRIP.sub("", s.lower())


def build_reference(book_dir):
    """返回 {章号: flat文本} 与 [全部 flat 文本]。"""
    per_chapter = {}
    for p in sorted(glob.glob(os.path.join(book_dir, "text", "ch*.txt"))):
        ch = os.path.basename(p).split("_")[0]
        try:
            per_chapter[ch] = flat(open(p, encoding="utf-8").read())
        except OSError:
            pass
    return per_chapter, list(per_chapter.values())


def has_en(s: str) -> bool:
    """片段是否算「英文原句」——**必须不含汉字**。

    ⚠️ 2026-10-19 修正：原判据只看「≥8 个英文字母」，于是
    `**中文理解**：Dan 去水槽洗早餐碗碟："Poppy 回来了吗？她跟你谈过放弃 Dance 的事吗？"`
    这类**中文翻译被引号包住**的写法被当成英文原句 → 报「疑似伪造」假红。
    ⇒ 加一条：**含汉字 ⇒ 不是英文原句**（中文译文被引号包住是合法写法）。
    """
    if CJK.search(s):
        return False
    return len(re.findall(r"[A-Za-z]", s)) >= 8


def collect(book_dir, only_file=None):
    """返回 (quoted_hits, quoted_miss, bare) —— 每条为 (file, line, field, frag, kind)"""
    per_chapter, all_refs = build_reference(book_dir)
    q_own, q_other, q_none, bare = [], [], [], []
    for path in sorted(glob.glob(os.path.join(book_dir, "ch*.md"))):
        name = os.path.basename(path)
        if only_file and name != only_file:
            continue
        ch = name[:4]
        own = per_chapter.get(ch, "")
        for i, raw in enumerate(open(path, encoding="utf-8").read().split("\n"), 1):
            s = raw.strip()
            if s.startswith("- ") or s.startswith("* "):
                s = re.sub(r'^[-*]\s+', '', s)
            s = s.replace("**", "").strip()
            m = FIELD_RE.match(s)
            if not m:
                continue
            field, body = m.group(1), m.group(2)
            seen = set()
            for qm in QUOTED_RE.finditer(body):
                q = qm.group(1)
                if not has_en(q) or q in seen:
                    continue
                seen.add(q)
                f = flat(q)
                if len(f) < 6:
                    continue
                if f in own:
                    q_own.append((name, i, field, q))
                elif any(f in r for r in all_refs):
                    # ⚠️ 2026-10-19：跨章引用若**本块已标出 chNN**（＝已标注）
                    # 就不该再报「须在本块内标出 chNN」——那是已完成的动作。
                    other_chs = [c for c, r in per_chapter.items() if f in r]
                    labeled = any(re.search(rf"(?<![A-Za-z0-9]){c}(?![A-Za-z0-9])", body) for c in other_chs)
                    q_other.append((name, i, field, q, labeled, other_chs))
                else:
                    q_none.append((name, i, field, q))
            for bm in BARE_RE.finditer(body):
                t = bm.group(0).strip()
                if flat(t) in {flat(x) for x in TERMINOLOGY}:
                    continue
                bare.append((name, i, field, t))
    return q_own, q_other, q_none, bare


def main():
    ap = argparse.ArgumentParser(description="分析层英文取证检查器")
    ap.add_argument("book_dir")
    ap.add_argument("--file", help="只查某一个 md")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--max-list", type=int, default=40)
    ap.add_argument("--show-bare", action="store_true", help="同时列裸词组")
    args = ap.parse_args()

    if not os.path.isdir(args.book_dir):
        print(f"❓ 书目录不存在：{args.book_dir}")
        return 2
    q_own, q_other, q_none, bare = collect(args.book_dir, args.file)
    if not (q_own or q_other or q_none or bare):
        print("❓ 参照集为空：text/ 下没有 ch*.txt ⇒ 无法判定（不是「干净」）")
        return 2

    print(f"=== 分析层英文取证（{os.path.basename(args.book_dir.rstrip('/'))}）===")
    print(f"    引号内英文：{len(q_own) + len(q_other) + len(q_none)} 条"
          f"（本章命中 {len(q_own)} · 他章命中 {len(q_other)} · 全书查无 {len(q_none)}）")
    print(f"    裸英文词组：{len(bare)} 条（不判红，仅供人工扫一眼）")

    if q_none:
        print(f"❌ 疑似伪造（引号内英文全书查无）：{len(q_none)} 条 ⇒ 必须改")
        by = {}
        for name, line, field, frag in q_none:
            by.setdefault(name, []).append((line, field, frag))
        for name in sorted(by):
            items = by[name]
            print(f"  {name}（{len(items)} 条）")
            for line, field, frag in items[: args.max_list]:
                print(f"    L{line} [{field}] {frag[:100]}")
            if len(items) > args.max_list:
                print(f"    …… 另有 {len(items) - args.max_list} 条")
    else:
        print("✅ 引号内英文全部能在 text/ 里查到")

    if q_other:
        labeled = [t for t in q_other if t[4]]
        unlabeled = [t for t in q_other if not t[4]]
        if unlabeled:
            print(f"⚠️ 跨章引用**未标注**（英文在他章、本章查无、块内无 chNN）："
                  f"{len(unlabeled)} 条 ⇒ 须在本块内标出 chNN，否则读者会误读为引自本章")
            if not args.quiet:
                for name, line, field, frag, _lbl, chs in unlabeled[: args.max_list]:
                    print(f"    {name}:{line} [{field}] 实为 {'/'.join(chs)}：{frag[:80]}")
                if len(unlabeled) > args.max_list:
                    print(f"    …… 另有 {len(unlabeled) - args.max_list} 条")
        if labeled:
            print(f"ℹ️ 跨章引用**已标注**（块内已标 chNN）：{len(labeled)} 条 —— 合规，不判红")
            if not args.quiet:
                for name, line, field, frag, _lbl, chs in labeled[: args.max_list]:
                    print(f"    {name}:{line} [{field}] 实为 {'/'.join(chs)}：{frag[:80]}")
                if len(labeled) > args.max_list:
                    print(f"    …… 另有 {len(labeled) - args.max_list} 条")

    if args.show_bare and bare:
        print(f"⚠️ 裸英文词组 {len(bare)} 条（不判红）")
        for name, line, field, frag in bare[: args.max_list]:
            print(f"    {name}:{line} [{field}] {frag[:70]}")

    return 1 if q_none else 0


if __name__ == "__main__":
    sys.exit(main())
