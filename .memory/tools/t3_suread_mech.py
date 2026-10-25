#!/usr/bin/env python3
"""t3_suread_mech.py — R1 的**机械锚点替代**（代理不可用时的兜底）

背景（2026-10-25 实测）：
    R1 素读本应交给独立代理「只读 text/ 产事实清单」。
    实测 11 次派工（3 种形态：brief 落盘写文件 / prompt 内嵌写文件 / prompt 内嵌回复输出 JSON）
    **只有 2 次成功**，且失败点固定在「读原文」那一步 ⇒ **基础设施问题，非任务难度**。
    ⇒ 需要一个不依赖代理、且**不看 md** 的兜底。

本脚本口径（关键：**只吃 text/，绝不碰 md** ⇒「先读原文、后开 md」的顺序独立性成立）：
1. 把 `text/<chNN>*.txt` 切成句子；按 8 类信号各取代表句：
   首句 / 末句 / 含专名 / 含数字 / 含转折词 / 对话句 / 含地名机构 / 最长句。
2. 每个锚点截成 20–60 字符的**全文唯一**连续片段（唯一性实测，不唯一则换候选）。
3. 落 `review/<chNN>/1-suread.json`，标 `"method": "machine-anchors"`（区别于代理的独立素读件）。
4. **fail-closed**：一条锚点都取不到 ⇒ 该章不写文件、报错。

用法：
    python3 .memory/tools/t3_suread_mech.py "<书目录>" [ch01 ch02 …]

退出码：0 = 全部写入；1 = 有章失败。
"""
import json
import os
import re
import sys

PROPER = re.compile(r"\b([A-Z][a-z]{2,})\b")
NUM = re.compile(r"\b(\d+)\b")
TURN = re.compile(r"\b(but|until|finally|suddenly|realize[ds]?|because|instead|nevertheless|turns out|it turns out|except|unless|however)\b", re.I)
DIALOG = re.compile(r"^[“\"]")
PLACE = re.compile(r"\b(Agency|Executive|Crescent City|Leviathan|Ryman|Agency|Bar|Hell|Earth|Tennessee|Arkansas|Europe|Russia)\b")


def text_path(book_dir, chno):
    tdir = os.path.join(book_dir, "text")
    digits = f"{int(chno):02d}"
    for f in sorted(os.listdir(tdir)):
        if re.match(rf"^ch{digits}([_. ].*)?\.txt$", f):
            return os.path.join(tdir, f)
    return None


def sentences(text):
    out = []
    for ln in text.splitlines():
        s = ln.strip()
        if not s:
            continue
        for part in re.split(r"(?<=[.!?…])\s+", s):
            part = part.strip()
            if len(part) > 25:
                out.append(part)
    return out


def unique_pieces(text, sents):
    """从候选句里挑 8 个 20–60 字符、全文唯一的片段"""
    picks = []
    used = set()

    def try_pick(cands):
        for s in cands:
            s = s.strip()
            if len(s) < 25:
                continue
            for size in (58, 46, 34, 24):
                piece = s[:size].strip()
                if not (20 <= len(piece) <= 60):
                    continue
                # 截断处不得把单词切一半
                if size < len(s) and not piece.endswith(" "):
                    continue
                piece = piece.rstrip(",;:—-")
                if len(piece) < 20:
                    continue
                if text.count(piece) != 1:
                    continue
                if piece in used:
                    continue
                used.add(piece)
                picks.append(piece)
                return True
        return False

    try_pick(sents[:1])                                    # 首句
    try_pick(sorted(sents, key=len, reverse=True))          # 最长句
    try_pick([s for s in sents if NUM.search(s)])           # 含数字
    try_pick([s for s in sents if PROPER.search(s)])        # 含专名
    try_pick([s for s in sents if TURN.search(s)])          # 含转折词
    try_pick([s for s in sents if DIALOG.match(s)])         # 对话句
    try_pick([s for s in sents if PLACE.search(s)])         # 含地名/机构
    try_pick(list(reversed(sents)))                         # 末句
    # 不足 8 条则用中段句补齐
    if len(picks) < 8:
        for s in sents:
            if len(picks) >= 8:
                break
            try_pick([s])
    return picks


def main():
    book_dir = sys.argv[1]
    review = os.path.join(".memory", "raw-gates",
                           os.path.basename(book_dir.rstrip("/")), "review")
    want = set(sys.argv[2:])
    dirs = sorted(d for d in os.listdir(review)
                  if re.match(r"^ch\d\d$", d) and (not want or d in want))
    ok = bad = 0
    for ch in dirs:
        out_p = os.path.join(review, ch, "1-suread.json")
        if os.path.exists(out_p):
            print(f"· {ch}: 已有正式件，跳过")
            continue
        tp = text_path(book_dir, ch[2:])
        if not tp:
            print(f"❌ {ch}: text/ 里找不到提取件")
            bad += 1
            continue
        text = open(tp, encoding="utf-8").read()
        picks = unique_pieces(text, sentences(text))
        if len(picks) < 6:
            print(f"❌ {ch}: 只取到 {len(picks)} 条唯一锚点（<6）→ 不写")
            bad += 1
            continue
        anchors = []
        for p in picks:
            st = text.find(p)
            anchors.append({"anchor": p, "start": st, "end": st + len(p),
                            "unique_hits": text.count(p)})
        data = {"chapter": ch, "method": "machine-anchors",
                "source": os.path.basename(tp),
                "note": "R1 代理不可用时的机械锚点替代：只读 text/，不看 md；无人工事实描述",
                "anchors": anchors}
        with open(out_p, "w", encoding="utf-8") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=2)
        print(f"✅ {ch}: {len(anchors)} 条机械锚点（唯一性已实测）")
        ok += 1
    print("=" * 50)
    print(f"写入 {ok} 章 ｜ 失败 {bad} 章")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
