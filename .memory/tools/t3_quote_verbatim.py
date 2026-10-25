#!/usr/bin/env python3
"""t3_quote_verbatim.py — 总览三篇的**整块引文逐字核验**（成对扫描 + 句级切片）

为什么另写一个（2026-10-25 实测订正）：
    旧工具 `t3_overview_labels.py` 的 QUOTE_RE 是 `“([^”]{12,})”|"([^"]{12,})"`，
    **中文引号分支在前** ⇒ 扫描位置被内层 `“…”` 对先占，
    外层整块引文（`"…"`，内含 `“…”`）**从未被提取**；
    且旧工具在「块后找不到紧邻标签」时**回退**去取「块前最近的标签」，
    ⇒ 中文译述句里的短引用（如 `"Daniel Ivanov"`）被错配到上一段的章号 ⇒ **假红**。
    ⇒ 三篇合计 315 个英文引文块，旧工具只核到 175 处。

本工具口径：
1. **栈式奇偶配对**扫描英文 `"` → 外层块（含内层 `“…”`）。
2. **紧邻标签**：块的结束位置到**下一块开始**之间最近的 `（chNN）`；
   **没有就不配对**（不回头找上一个标签 ⇒ 消除回退假红）。
3. **切片**：外层块按 `…`/`. . .` 切；每片再按**句末标点**切句 ⇒ 每句必须是原文连续片段。
   内层 `“…”` 对话段同样按句切（**句级**，不整段核 ⇒ 避免嵌套引号跨句配错）。
4. **核验**：归一化（弯引号统一、`…`→空格、`—`→`-`、空白压平）后回 `text/<chNN>*.txt` 找。
   - 查无 ⇒ 报「最长命中前缀长度 / 片段长度」：**≥80% 视为切分差异（提示型）**，否则为阻断候选。
   - 含汉字的片段跳过（中文译述句不是原文引文）。
   - 归一化后长度 < 12 的跳过。

退出码：0 = 无阻断候选（提示型仍计数）；1 = 有阻断候选。
"""
import os
import re
import sys

CJK = re.compile(r"[　-〿一-鿿＀-￯]")
LABEL_RE = re.compile(r"[（(](ch\d\d)[）)]")
CN_DQ = re.compile(r"“([^”]{6,})”")
SENT_SPLIT = re.compile(r"(?<=[.?!…])\s+")


def norm(s):
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-")
    s = s.replace("…", " ").replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip()


def scan_blocks(text):
    """栈式奇偶配对：返回 [(start, end, body), ...]（end = 闭合引号后一位）"""
    out = []
    i = 0
    n = len(text)
    while i < n:
        if text[i] == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 1
            if j < n:
                out.append((i, j + 1, text[i + 1:j]))
                i = j + 1
                continue
        i += 1
    return out


def sentences(seg):
    """`…` 切片 + 句级切片"""
    out = []
    for part in re.split(r"…|\.\.\.", seg):
        part = part.strip()
        if not part:
            continue
        for s in SENT_SPLIT.split(part):
            s = s.strip()
            if s:
                out.append(s)
    return out


def check(seg, corpus, ch):
    """返回 (kind, info)；kind ∈ {ok, skip, warn, bad}"""
    nf = norm(seg)
    if len(nf) < 12:
        return "skip", None
    if CJK.search(nf):
        return "skip", None
    letters = sum(c.isascii() and c.isalpha() for c in nf)
    if letters < len(nf) * 0.5:
        return "skip", None
    if nf in corpus.get(ch, ""):
        return "ok", None
    other = [c for c in corpus if nf in corpus[c]]
    if other:
        return "bad", (nf[:90], other)
    # 最长命中前缀：区分「切分差异」与「真缺陷」
    lo, hi = 0, len(nf)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if nf[:mid] in corpus.get(ch, ""):
            lo = mid
        else:
            hi = mid - 1
    ratio = lo / len(nf)
    kind = "warn" if ratio >= 0.8 else "bad"
    return kind, (nf[:90], f"最长命中前缀 {lo}/{len(nf)} 字（{ratio:.0%}）", "全书查无")


def main():
    book_dir = sys.argv[1]
    tdir = os.path.join(book_dir, "text")
    corpus = {}
    for f in sorted(os.listdir(tdir)):
        if f.startswith("ch") and f.endswith(".txt"):
            corpus[f[:4]] = norm(open(os.path.join(tdir, f), encoding="utf-8").read())

    pairs = nolabel = nseg = 0
    bad, warn = [], []
    for name in ("00_概述.md", "00_金句精选.md", "00_情感节点.md"):
        p = os.path.join(book_dir, name)
        if not os.path.exists(p):
            continue
        txt = open(p, encoding="utf-8").read()
        blocks = scan_blocks(txt)
        labels = list(LABEL_RE.finditer(txt))
        for bi, (bs, be, body) in enumerate(blocks):
            nxt = blocks[bi + 1][0] if bi + 1 < len(blocks) else len(txt) + 1
            lab = None
            for m in labels:
                if be <= m.start() < nxt:
                    lab = m
                    break
            if lab is None:
                nolabel += 1
                continue
            ch = lab.group(1)
            line = txt.count("\n", 0, bs) + 1
            pairs += 1
            segs = sentences(body)
            # 内层对话**逐个**独立核（不可 join：join 会把多句对话拼成一片 ⇒ 假红）
            for dq in CN_DQ.findall(body):
                segs += sentences(dq)
            for s in segs:
                kind, info = check(s, corpus, ch)
                if kind == "skip":
                    continue
                nseg += 1
                if kind == "bad":
                    bad.append((name, line, ch, info))
                elif kind == "warn":
                    warn.append((name, line, ch, info))
    for tag, lst in (("🔶 提示（切分差异）", warn), ("❌ 阻断候选", bad)):
        for n, ln, ch, info in lst:
            print(f"{tag} {n}:{ln}  标签 {ch} ｜ 片段“{info[0]}” ｜ {info[1]}")
    print("=" * 56)
    print(f"总览引文块：配对 {pairs} 处 ｜ 无紧邻标签（跳过）{nolabel} 处")
    print(f"句级片段实核 {nseg} ｜ 提示 {len(warn)} ｜ 阻断候选 {len(bad)}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
