#!/usr/bin/env python3
"""t3_overview_labels.py — 总览三篇的**引语↔章号标签**核验（逐片段回 text/）

用法：
    python3 .memory/tools/t3_overview_labels.py "<书目录>"

核验对象：三个总览 md 里的**英文引文**（成对的 “…” 或 "…"）与其后/前最近的
`(chNN)` 标签是否一致——即「这句引语真的在 chNN 那章的 text/ 里」。

口径（重要）：
- 引文按 `…` 切成片段，**每段**各自回 text/ 找；任一片段查无 ⇒ 该标签存疑。
- 片段做归一化（弯直引号统一、空白压平）后比对。
- 只报**标签与内容不符**的；章号标签本身不在标签位（如「上下文：ch31」）的，
  按「最近的 (chNN)」取。

退出码：0 = 无不符；1 = 有不符。
"""
import os
import re
import sys

QUOTE_RE = re.compile(r"“([^”]{12,})”|\"([^\"]{12,})\"")
LABEL_RE = re.compile(r"（(ch\d\d)）|\(ch(\d\d)\)")


def norm(s):
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-").replace("…", " ")
    return re.sub(r"\s+", " ", s).strip()


def main():
    book_dir = sys.argv[1]
    tdir = os.path.join(book_dir, "text")
    corpus = {}
    for f in sorted(os.listdir(tdir)):
        if f.startswith("ch") and f.endswith(".txt"):
            corpus[f[:4]] = norm(open(os.path.join(tdir, f), encoding="utf-8").read())
    allc = "\n".join(corpus.values())

    total = 0
    bad = []
    for name in ("00_概述.md", "00_金句精选.md", "00_情感节点.md"):
        p = os.path.join(book_dir, name)
        if not os.path.exists(p):
            continue
        txt = open(p, encoding="utf-8").read()
        # 逐行处理：引文与标签在同一行或紧邻
        lines = txt.splitlines()
        for i, line in enumerate(lines):
            quotes = [m for m in QUOTE_RE.finditer(line)]
            if not quotes:
                continue
            labels = list(LABEL_RE.finditer(line))
            for qi, q in enumerate(quotes):
                seg = q.group(1) if q.group(1) is not None else q.group(2)
                if not seg or len(seg) < 12:
                    continue
                # 只验英文引文（中文译述句不参与逐字核）
                letters = sum(c.isascii() and c.isalpha() for c in seg)
                if letters < len(seg) * 0.5:
                    continue
                # 配对：引文与其**后**第一个标签，且该标签必须落在这条引文与下一条引文之间
                nxt = quotes[qi + 1].start() if qi + 1 < len(quotes) else len(line) + 1
                lab = None
                for m in labels:
                    if q.end() <= m.start() < nxt:
                        lab = m
                        break
                if lab is None:
                    # 回退：引文之前、且在该引文与上一条引文之间的标签
                    prev = quotes[qi - 1].end() if qi > 0 else -1
                    for m in reversed(labels):
                        if prev <= m.start() < q.start():
                            lab = m
                            break
                if not lab:
                    continue
                ch = lab.group(1) or "ch" + lab.group(2)
                total += 1
                frags = [x for x in re.split(r"…|\.\.\.", seg) if len(norm(x)) > 12]
                if not frags:
                    continue
                miss = [f for f in frags if norm(f) not in corpus.get(ch, "")]
                if miss:
                    other = []
                    for f in frags:
                        for c in corpus:
                            if norm(f) in corpus[c] and c not in other:
                                other.append(c)
                    bad.append((name, i + 1, ch, seg[:60],
                                f"该章查无 {len(miss)}/{len(frags)} 片段；实际所在：{other or '全书查无'}"))
    for n, ln, ch, seg, why in bad:
        print(f"❌ {n}:{ln}  标签 {ch} ｜ “{seg}…” ｜ {why}")
    print("=" * 50)
    print(f"核验引文-标签对 {total} 处 ｜ 不符 {len(bad)} 处")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
