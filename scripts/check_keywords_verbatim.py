#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_keywords_verbatim.py —— AGENTS 第 9 条 b/d 项的机检（关键词与导航/总结层英文逐字核对）

## 为什么需要它（2026-10-01 The Death of Us 五步审查实证）

AGENTS 第 9 条 b 规定「块内『关键词』的英文词必须能在该块引语中找到（允许词形变化）；
语境延伸词必须在『为什么这样写』中有呼应，否则替换为引语逐字词」。
这条**六道门禁结构上查不了**：

* `verify_quotes` / `sweep_full` 只锚 `> **原句 N:**` 那一行 ⇒ 分析层完全在口径外；
* `sweep_analysis_inline` 拿的是**全章**参照集 ⇒ 关键词在第 3 块里引用第 1 块的句子也判命中；
* `check_anchor` 只查「词**全书**查无」⇒ `wouldn’t`（原文 `wouldn’t’ve`）这类**换词**
  每个词都在书里，照样过；
* `flat_alpha` 会把撇号抹成空串 ⇒ `wouldn’t have` 与 `wouldn’t’ve` **归一后完全相同**，
  任何走 flat 的实现都抓不到。

The Death of Us 实测 10 条 `check_analysis_indep` ⚠️ 里 **7 条**属此类，全部门禁看不见。

## 判据

对每个 `**关键词**` 行 / 导航层 / `## 一句话总结` 里的**英文片段**（≥2 个英文词）：

1. **引语层**（`关键词` 在某个引语块内）：片段必须是**该块引语**的连续子串 ⇒ 阻断型；
   不是子串但在同块 `为什么这样写` 里被呼应 ⇒ 提示型（AGENTS 9b 明许的「语境延伸词」）。
2. **导航/总结层**：片段必须是**本章 `text/chNN*.txt`** 的连续子串 ⇒ 阻断型。

## 为什么用「原文连续子串」而不是 flat 比对

本工具**故意不调 `flat_alpha`**：它剥掉标点后 `wouldn’t have` ≡ `wouldn’t’ve`，
换词类缺陷会整类漏网。改为**只归一空白 + 已知良性差异**（弯/直引号、`...`↔`. . .`），
其余逐字比对。正因如此本工具能抓 flat 口径抓不到的（第 9 条实测 7 条里至少 2 条是撇号类）。

## 退出码

0 = 阻断型 0；1 = 有阻断型；提示型与假红型只打印，不影响退出码。
"""

import glob
import io
import os
import re
import sys
import unicodedata

# 良性归一：只处理「排版造成的差异」，不处理「换词造成的差异」
BENIGN = [
    (re.compile(r"\s+"), " "),
]


def norm(s):
    """只归一空白与**双引号**；**撇号必须保留**。

    为什么剥双引号但不剥撇号——这是本工具能不能抓到换词类缺陷的分界：
    * 剥双引号：`“Abusive,” she added…` 与 `Abusive, she added…` 视为同一
      （AGENTS：弯/直引号差异属正常；关键词省略外层引号也不改变语义）；
    * 留撇号：`wouldn’t have` ≠ `wouldn’t’ve`、`don’t` ≠ `dont`
      ⇒ **换词与掉撇号仍被抓**，而任何走 flat_alpha 的实现都会把它们抹平后放过。
    """
    s = s.replace("'", "’")           # 直撇号 → 弯撇号（只统一方向，不删）
    s = s.replace("...", ". . . ")    # 三点 → 省略号排版
    s = re.sub(r"[“”\"]", "", s)      # 剥双引号：外层引号的有无不影响语义
    # ⚠️ 必须用 `\s+` 而不是 `[ \t　]+`：**引语块可能跨物理行**（源段落自带 \n），
    # 只归一空格不归一换行 ⇒ 跨行引语的后半截永远匹配不上（2026-10-01 三版判据
    # 连续踩同一个坑：假红从 100 → 98 → 96 一路不降的真因就在这里）。
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def hit_in(frag, scope):
    """片段是否命中参照集。**大小写不敏感** —— 关键词是「指路」不是引文复刻，
    把句中片段首字母改成小写（`Not like Link`→`not like Link`）不改变语义；
    真正要抓的是词本身变了（no→a、wouldn’t→won’t、people are→not），
    那些在大写归一之后依然不等 ⇒ 不受影响。"""
    f = frag.lower()
    return f in scope.lower()


# 纯专有名词（≤3 词、每词首字母大写）：`Key Kehoe`、`Jamie Ward`、`Ennis Larkin`
PROPER = re.compile(r"^(?:[A-Z][A-Za-z’'\-]*)(?:\s+(?:[A-Z][A-Za-z’'\-]*)){0,2}$")


def is_proper_noun(s):
    return bool(PROPER.match(s.strip()))


# 片段内部的连接号：导航里 `Robbie Hubbard——Link` 是「两个人」而不是一段英文；
# 省略号两侧各自独立判定（AGENTS 第 2 条：省略两侧都必须是原词）。
# ⚠️ 三点式必须同时覆盖 `...`（无空格）与 `. . .`（原书排版）：
# 只写 `\.\s\.\s\.` 时，md 里写成 `instinct ... is` 的关键词整段不被切开，
# 拿整串去比对自然不命中 ⇒ 假红（本工具第一版就踩了这条，ch13:76／ch16:28 假红）。
SPLIT_INNER = re.compile(r"(?:——|—|\.\s*\.\s*\.+|…|\.\s*\.\s*\.\s*\.\s*\.\s*\.\s*\.\s*\.\s*\.)")


# 英文片段：≥2 个英文词（词内可含撇号/连字符）
ENG = re.compile(r"[A-Za-z][A-Za-z0-9’'\-–—]*"
                 r"(?:[ ,]+[A-Za-z0-9’'\-–—:;.]+)*")


def english_fragments(text):
    """返回英文片段列表（≥2 词）。先按连接号/省略号切开，避免 `A——B`、
    `X … Y` 这类被当成一整段英文。"""
    out = []
    for chunk in SPLIT_INNER.split(text):
        for m in ENG.finditer(chunk):
            frag = m.group(0).strip(" ,;:.")
            if len(re.findall(r"[A-Za-z0-9’'\-]+", frag)) >= 2:
                out.append(frag)
    return out


def split_keyword_line(body):
    """关键词行的分隔符：`／`（全角）／`｜`（全角）／`/`（半角，且两侧不粘字母）。"""
    parts = re.split(r"[／｜]|\s/\s", body)
    return [p.strip() for p in parts if p.strip()]


QUOTE_RE = re.compile(r"^>\s*\*\*原句\s*\d+:\*\*\s*(.+?)\s*$")
KW_RE = re.compile(r"^\*\*关键词\*\*[：:]\s*(.+?)\s*$")
WHY_RE = re.compile(r"^\*\*为什么这样写\*\*[：:]\s*(.+?)\s*$")
NAV_RE = re.compile(r"^-\s*\*\*(一句话概括|情感弧线位置|线索结构|人物弧线|本章状态)\*\*[：:]\s*(.+?)\s*$")
SUM_RE = re.compile(r"^##\s+一句话总结\s*$")


def read_chapter_text(book_dir, n):
    # ⚠️ 2026-10-02 收口：原写只认 chNN_*.txt（下划线），而根 AGENTS.md 规定精读文件名
    # 唯一分隔符是空格 ⇒ 用空格命名的书参照集恒为空，该工具对任何文件都必然报「查无」
    # （假红型）。分隔符与章号位数统一走 chapter_text_path 唯一实现。
    import sys as _sys, os as _os
    _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
    from chapter_text_path import find_chapter_text
    p = find_chapter_text(book_dir, n)
    return io.open(p, encoding="utf-8", errors="replace").read() if p else ""


def main():
    if len(sys.argv) < 2:
        print("用法：python3 scripts/check_keywords_verbatim.py <书目录>")
        return 0
    book = sys.argv[1]
    blockers, notes = [], []
    files = sorted(glob.glob(os.path.join(book, "ch*.md")),
                   key=lambda p: int(re.match(r".*?ch(\d+)", p).group(1)))
    for path in files:
        n = int(re.match(r".*?ch(\d+)", path).group(1))
        chapter_text = norm(read_chapter_text(book, n))
        lines = io.open(path, encoding="utf-8").read().split("\n")
        in_sum = False
        # 逐块两遍解析：关键词**排在**为什么这样写之前（子项固定顺序
        # 中文理解→关键词→为什么这样写→读者视角提示），单向向后扫永远取不到
        # 「为什么这样写」，提示型分支会静默失效成死代码（2026-10-01 自回归实测）。
        blocks, cur = [], None
        navs = []
        for i, raw in enumerate(lines, 1):
            line = raw.rstrip()
            if SUM_RE.match(line):
                in_sum = True
                continue
            if in_sum and line.startswith("#"):
                in_sum = False
            if in_sum:
                navs.append((i, line, "总结层"))
                continue
            mq = QUOTE_RE.match(line)
            if mq:
                # 引语可能**跨物理行**：源 text/ 的段落自带换行（The Death of Us
                # 实测 47 条），注入时原样带进来，渲染上是 blockquote 的 lazy
                # continuation。**只取 `> ` 那一行 ⇒ 关键词命中续行内容会被误报**，
                # 而 verify_quotes / check_chapter_quotes / sweep_full 也都只读那一行
                # ⇒ 这是**全库共有的口径盲区**（见本文件顶部「为什么需要它」）。
                parts = [mq.group(1)]
                k = i          # i 是 1-based、lines 是 0-based ⇒ k=i 即下一行
                while k < len(lines) and lines[k].strip() \
                        and not lines[k].startswith(">") \
                        and not lines[k].lstrip().startswith("**") \
                        and not lines[k].startswith("#") \
                        and not lines[k].startswith("- ") \
                        and not lines[k].startswith("|"):
                    parts.append(lines[k].strip())
                    k += 1
                cur = {"quote": norm("\n".join(parts)), "kws": [], "why": ""}
                blocks.append(cur)
                continue
            if cur is not None:
                mk = KW_RE.match(line)
                if mk:
                    cur["kws"].append((i, mk.group(1)))
                    continue
                mw = WHY_RE.match(line)
                if mw:
                    cur["why"] = norm(mw.group(1))
                    continue
            mn = NAV_RE.match(line)
            if mn:
                navs.append((i, norm(mn.group(2)), "导航层"))

        for b in blocks:
            for i, kbody in b["kws"]:
                for part in split_keyword_line(kbody):
                    for frag in english_fragments(part):
                        f = norm(frag)
                        if hit_in(f, b["quote"]):
                            continue
                        if hit_in(f, b["why"]):
                            notes.append((path, i, frag,
                                          "提示型·语境延伸词（为什么这样写有呼应）"))
                        else:
                            blockers.append((path, i, frag,
                                             "阻断型·非本块引语的连续子串"))
        for i, body, layer in navs:
            for frag in english_fragments(body):
                f = norm(frag)
                if hit_in(f, chapter_text):
                    continue
                if is_proper_noun(f):
                    # 导航/总结层用**人物全名**指称（`视角人物 Key Kehoe`、
                    # `给 Jamie 挡一句`）：这不是引语，是叙述里的指代。
                    # 本书正文一律用名（Key / Jamie），所以「全名不在本章 text/」
                    # 是**正常**的 —— 判阻断型会让本工具永久变红而被忽略。
                    # 降为提示型：人判一次即可（The Death of Us 批 ch25/37/40/44/
                    # 50/54/58/70 的 `Key Kehoe` ×8 与 ch09 的 `Jamie Ward` ×1）。
                    notes.append((path, i, frag,
                                  "提示型·导航层人物全名指代（非引语，不要求逐字命中）"))
                    continue
                blockers.append((path, i, frag,
                                 "阻断型·非本章 text/ 的连续子串（%s）" % layer))

    base = os.path.basename(book.rstrip("/"))
    print("=== 关键词/导航/总结层英文逐字核对（%s）===" % base)
    print("扫 %d 个章节 md（判据=原文**连续子串**，只归一空白与弯/直引号，不调 flat_alpha）" % len(files))
    if blockers:
        print("--- 阻断型 %d 条 ---" % len(blockers))
        for path, i, frag, why in blockers:
            print("  %s:%d  %s\n      %s" % (os.path.basename(path), i, frag, why))
    else:
        print("✅ 阻断型 0 条")
    if notes:
        print("--- 提示型 %d 条（只记不改）---" % len(notes))
        for path, i, frag, why in notes:
            print("  %s:%d  %s\n      %s" % (os.path.basename(path), i, frag, why))
    else:
        print("提示型 0 条")
    return 1 if blockers else 0


if __name__ == "__main__":
    sys.exit(main())