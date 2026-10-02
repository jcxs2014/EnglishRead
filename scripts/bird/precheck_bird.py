#!/usr/bin/env python3
"""
precheck_bird.py — Bird of a Thousand Stories 单章写作期预检（生成期强制）

为什么需要这个脚本（不是「再加一道检查」）
--------------------------------------------
本项目已反复验证：**引语层一旦程序化抽取就 0 缺陷，凭印象手打必出伪造**。
而本书 40 章里六道主门禁都**不覆盖**两层：
  ① `## 本章导航` / `## 一句话总结` —— verify_quotes / check_chapter_quotes /
     sweep_full 全部只解析 `## 精读` 的引语行（AGENTS：六道门禁一律不解析这三层）
  ② 分析层（中文理解/为什么这样写/读者视角提示）里的行内英文 —— 禁令 3 的事后抓手

⇒ 本脚本把「写完这一章，提交前」该过的判据一次性收齐，**凡 ❌ 一律不许 commit**。

判据（全部以 `text/chNN_*.txt` 为真值，text/ 是 AGENTS 第 1 条的真值层）
--------------------------------------------------------------------
 1. 引语逐字        每条 `> **原句 N:**` 整串 flat 命中本章 text
 2. 引语块结构      编号连续无撞车；每块四子项齐全；无孤儿分析
 3. 块数配额        3–8 处（体裁表：精简格式）
 4. 关键词锚定      每个关键词必须能在**本块引语**里找到（禁令 4）
 5. 词表逐字        每个词头加词边界命中本章；每条例句 flat 命中本章（禁令 1a）
 6. 行内英文归属    全文件任何拉丁词（含导航/总结/分析层）必须在本章 text/ 出现
 7. 禁写标注        （未出现 / 未见于原文 / 本章未 / 中文理解补充 / 草稿标记 A→B）
 8. 最高级断言      唯一/全书唯一/第一次/最高级（禁令 2 同族的第三类）
 9. U+FFFD          写作截断损坏（六道门禁全看不见）
10. 空段            导航 ≥4 项且有正文；一句话总结有正文；三档词表档位非空

用法
----
    python3 scripts/bird/precheck_bird.py <md 文件>
    # 退出码 0 = 可提交；1 = 有 ❌（禁止 commit）
"""
import re
import sys
import glob
import os

QUOTE_RE = re.compile(r'(?m)^>\s*\*\*原句\s*(\d+)[：:]\*\*\s*(.+?)\s*$')
SUBITEMS = ("中文理解", "关键词", "为什么这样写", "读者视角提示")
TIER_RE = re.compile(r"(?m)^###\s*(.*)$")
FORBIDDEN_ANNOT = re.compile(
    r"（[^）]*(?:未出现|未见于原文|本章未|原文无|见工具输出|待填|释义待填)[^）]*）"
    r"|中文理解补充|未出现在原文"
)
SUPERLATIVE = re.compile(r"唯一|全书唯一|第一次|最高级|最深的|最远|从未有|再也?没有比")
LATIN = re.compile(r"[A-Za-z][A-Za-z'-]{2,}")
GLOSS_CELLS = re.compile(r"(?m)^\|([^|]*)\|([^|]*)\|([^|]*)\|$")
# 技术/结构词：它们是**文件与版的元信息**，不是「从本章原文引的证据」，
# 不该按「必须逐字命中本章 text/」判（判据过严比没有检查器更坏——会逼人改正文）。
TECH = {
    "modified", "status", "epub", "xhtml", "ncx", "spine", "toc", "markdown",
    "chapter", "prologue", "epilogue", "text", "isbn", "lcgft", "llcgft",
    "opf", "h1", "h2", "aq", "mq", "px",
}
CODE_SPAN = re.compile(r"`[^`]*`")


def flat(s):
    """与 verify_quotes / check_chapter_quotes 同口径的归一化。"""
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def load_text(text_dir, nn):
    cands = glob.glob(os.path.join(text_dir, "ch%02d_*.txt" % nn)) or \
           glob.glob(os.path.join(text_dir, "ch%d_*.txt" % nn))
    if not cands:
        sys.exit("找不到 text/ch%02d_*.txt" % nn)
    return open(cands[0], encoding="utf-8").read(), cands[0]


def main():
    md = sys.argv[1]
    book = os.path.dirname(md)
    m = re.search(r"ch0*(\d+)", os.path.basename(md))
    nn = int(m.group(1))
    txt, tpath = load_text(os.path.join(book, "text"), nn)
    ftxt = flat(txt)
    src = open(md, encoding="utf-8").read()
    errs, warns = [], []

    # --- 1/2 引语逐字 + 块结构 -------------------------------------------
    qs = QUOTE_RE.findall(src)
    if not qs:
        errs.append("❌ 本文件没有抽到任何引语行（`> **原句 N:**`）")
    seen = set()
    for i, (n, q) in enumerate(qs, 1):
        if int(n) != i:
            errs.append(f"❌ 引语编号不连续：第 {i} 块写的是「原句 {n}」")
        if n in seen:
            errs.append(f"❌ 引语编号撞车：原句 {n} 出现两次")
        seen.add(n)
        inner = q.strip().strip('"').strip()
        # 省略号分段：每段都要是本章 text 的连续片段（禁令 5）
        parts = [p for p in re.split(r"\s*…\s*", inner) if p.strip()]
        for p in parts:
            if flat(p) not in ftxt:
                errs.append(f"❌ 原句 {n} 不是本章 text/ 的逐字连续片段：{p[:60]}…")
    blocks = re.split(r"(?m)^> ", src)[1:]
    for bi, blk in enumerate(blocks, 1):
        head = blk.split("\n", 1)[0]
        for sub in SUBITEMS:
            if f"**{sub}" not in blk:
                errs.append(f"❌ 第 {bi} 块缺子项「**{sub}**」（块首：{head[:40]}）")
    orphan = len(re.findall(r"(?m)^\*\*中文理解", src)) - len(qs)
    if orphan > 0:
        errs.append(f"❌ 孤儿分析：{orphan} 处「**中文理解**」上方没有引语行")

    # --- 3 块数配额 ------------------------------------------------------
    if not (3 <= len(qs) <= 8):
        errs.append(f"❌ 引语块数 {len(qs)} 不在体裁配额 3–8 处内")

    # --- 4 关键词锚定（禁令 4：只从本块引语里挑）------------------------
    # 逐块取出「本块引语行」与「本块关键词行」成对比较：块是按 `^> ` 切出来的，
    # 切完第一行才是引语本身（编号前缀已被 split 吃掉）。
    for bi, blk in enumerate(blocks, 1):
        qline = blk.split("\n", 1)[0]
        km = re.search(r"\*\*关键词\*\*[：:]\s*(.+)", blk)
        if not km:
            continue
        qflat = flat(qline)
        for w in re.split(r"[/／、,，]", km.group(1)):
            w = w.strip().strip("`*_ ")
            for tok in LATIN.findall(w):
                if len(tok) < 3 or tok.lower() in TECH:
                    continue
                if flat(tok) not in qflat:
                    errs.append(f"❌ 第 {bi} 块关键词「{tok}」不在本块引语里（禁令 4）")

    # --- 5 词表逐字 ------------------------------------------------------
    vsec = re.search(r"(?m)^## (?:本章词汇|词汇分级)[ \t]*$", src)
    if not vsec:
        errs.append("❌ 缺 `## 本章词汇` 节")
        vsrc = ""
    else:
        # ⚠️ 2026-10-02 修正（本脚本第一版的死代码）：写成
        #   `vsrc = re.split(r"(?m)^## ", src[vsec.start():])[0]`
        # 而 vsec.start() 正落在 "## 本章词汇" 这一行上 ⇒ 切出来的第 0 段是**空串**
        # ⇒ `tiers` 恒为 [] ⇒ **整个词表判据从未执行**，却因为「没有报错」被读成「词表干净」。
        # 这正是 AGENTS 8c「现写检查器先验该报的报了」与 8.4「0 报警可能来自工具在骗我」。
        # 正解：先吃掉标题行本身，再切到下一个 H2。
        _rest = src[vsec.end():]
        _nxt = re.search(r"(?m)^## ", _rest)
        vsrc = _rest[:_nxt.start()] if _nxt else _rest
        # ⚠️ 2026-10-02 第二次修正（负控暴露）：`re.split(r"(?m)^### ", vsrc)[1:]`
        # 每段是「档名 + \n + 表体」**连在一起**的一整块，原写法 `zip(tiers[::2], tiers[1::2])`
        # 于是把「档名」当成表体、「表体」当成下一个档名 ⇒ **整张表一次都没被检查**
        # （负控里伪造的词头 zorblatt 与伪造例句因此零报警）。
        # 正解：按块取，块内第一行是档名，其余是表体。
        blocks_t = re.split(r"(?m)^### ", vsrc)[1:]
        if not blocks_t:
            errs.append("❌ `## 本章词汇` 节内没有任何 `### ⭐ 档位` 小节")
        for tb in blocks_t:
            tname, _, tbody = tb.partition("\n")
            tname = tname.strip()
            rows = [r for r in tbody.split("\n")
                    if r.startswith("| ") and "词/短语" not in r and not r.startswith("|---")]
            if not rows and not any(re.fullmatch(r"\s*（本章[^）]*）\s*", x)
                                    for x in tbody.split("\n")):
                errs.append(f"❌ 词表档位「{tname.strip()}」只有表头没有词条")
            for row in rows:
                cells = [c.strip() for c in row.strip().strip("|").split("|")]
                if len(cells) < 3:
                    continue
                head, gloss, ex = cells[0], cells[1], cells[2]
                if head in ("（本章过短，无基础词条）", "—", ""):
                    continue
                if gloss in ("（释义待填）", "待填", "—", ""):
                    errs.append(f"❌ 词条「{head}」释义未填（禁写占位）")
                if not ex or ex in ("—", "（同上）"):
                    errs.append(f"❌ 词条「{head}」例句缺失（禁写占位行）")
                    continue
                # 词头加词边界命中本章（8a：词头须用本章原词形）
                if not re.search(r"(?<![A-Za-z])" + re.escape(head.split()[0]) + r"(?![A-Za-z])",
                                 txt, re.I) and flat(head.split()[0]) not in ftxt:
                    errs.append(f"❌ 词头「{head}」不在本章 text/（A 类虚构或派生词）")
                if flat(ex) not in ftxt:
                    errs.append(f"❌ 词条「{head}」例句不是本章逐字：{ex[:50]}…")

    # --- 6 行内英文归属（六道门禁的结构性盲区）-------------------------
    # 分析层/导航层的中文里混写的拉丁词，必须在本章 text/ 逐字存在。
    # 豁免：frontmatter、反引号代码片段（`ch01a.xhtml` 是文件名不是引证）、技术词表。
    for ln, line in enumerate(src.split("\n"), 1):
        if ln <= 6 or line.startswith("|") or line.startswith("|"):
            continue
        scan = CODE_SPAN.sub(" ", line)
        for tok in LATIN.findall(scan):
            t = tok.strip("'-")
            if len(t) < 3 or t.lower() in TECH:
                continue
            if flat(t) not in ftxt:
                ctx = line.strip()[:70]
                errs.append(f"❌ 行 {ln} 拉丁词「{t}」不在本章 text/：{ctx}")

    # --- 7 禁写标注 ------------------------------------------------------
    for i, line in enumerate(src.split("\n"), 1):
        if FORBIDDEN_ANNOT.search(line):
            errs.append(f"❌ 行 {i} 禁写标注：{line.strip()[:70]}")

    # --- 8 最高级断言 ----------------------------------------------------
    for i, line in enumerate(src.split("\n"), 1):
        if SUPERLATIVE.search(line):
            warns.append(f"⚠️ 行 {i} 疑似最高级断言（禁令 2 第三类，须改成可证写法）：{line.strip()[:60]}")

    # --- 9 U+FFFD --------------------------------------------------------
    nbad = src.count(chr(0xFFFD))
    if nbad:
        errs.append(f"❌ 含 U+FFFD 替换字符 {nbad} 处（写作截断损坏）")

    # --- 10 空段 ---------------------------------------------------------
    nav = re.search(r"(?m)^## (?:本章导航|概览)\s*\n(.*?)(?=\n## |\Z)", src, re.S)
    items = re.findall(r"(?m)^[-*]?\s*\*\*([^*]+)\*\*[：:]\s*(\S.*)$", nav.group(1)) if nav else []
    if len(items) < 4:
        errs.append(f"❌ 导航粗体项 {len(items)} 条 < 4（缺项或写法不匹配 `**X**：`）")
    for k, v in items:
        if not v.strip():
            errs.append(f"❌ 导航项「{k}」有标题无正文")
    one = re.search(r"(?m)^## 一句话总结\s*\n(.*?)(?=\n## |\Z)", src, re.S)
    if not one or not one.group(1).strip():
        errs.append("❌ `## 一句话总结` 有标题无正文")

    name = os.path.basename(md)
    print(f"=== precheck: {name}（真值 {os.path.basename(tpath)}，{len(txt)} 字符）===")
    nrows = len([r for r in vsrc.split("\n")
                 if r.startswith("| ") and "词/短语" not in r and not r.startswith("|---")])
    print(f"  引语 {len(qs)} 条 ｜ 导航 {len(items)} 项 ｜ 词条行 {nrows}")
    for w in warns:
        print("  " + w)
    if errs:
        print(f"--- FAIL ({len(errs)}) ---")
        for e in errs:
            print("  " + e)
        return 1
    print("--- FAIL (0) ---  ✅ 可提交")
    return 0


if __name__ == "__main__":
    sys.exit(main())
