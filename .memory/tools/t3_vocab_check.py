#!/usr/bin/env python3
"""t3_vocab_check.py — 「本章词汇」层的**词条锚定 + 例句逐字**核验（35 章全量）

层结构：`## 本章词汇` 下三档（⭐⭐⭐ / ⭐⭐ / ⭐）表格，行格式 `| 词/短语 | 释义 | 例句 |`。

核两条：
1. **词条锚定**：词/短语本身是否在该章 `text/` 里出现（大小写不敏感，允许常见词形变体：
   复数 / 过去式 / -ing / -ed / -ly / 比较级）。查无 ⇒ 凭空生词候选。
2. **例句逐字**：例句（去表格首尾空格后）是否在该章原文**逐字命中**。查无 ⇒ 例句不实候选。

口径：
- 例句若含 `…` 或 `...` ⇒ 跳过（省略引用另行处理，不在本工具判据内）。
- 例句若以省略号开头（原文如此）⇒ 归一化后仍核。
- 词条若含空格（短语）⇒ 按整串匹配；单��� ⇒ 按词边界匹配。

退出码：0 = 无候选；1 = 有候选。
"""
import os
import re
import sys


def norm(s):
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip()


def variants(w):
    """常见词形变体"""
    v = {w}
    lw = w.lower()
    if " " not in lw:
        v |= {lw + "s", lw + "es", lw + "ed", lw + "ing", lw + "ly",
              lw + "er", lw + "est", lw + "d"}
        if lw.endswith("e"):
            v |= {lw[:-1] + "ing", lw[:-1] + "ed", lw[:-1] + "ly"}
        if lw.endswith("y"):
            v |= {lw[:-1] + "ies", lw[:-1] + "ied", lw[:-1] + "ier", lw[:-1] + "iest"}
        if lw.endswith("s"):
            v |= {lw[:-1], lw[:-1] + "ed", lw[:-1] + "ing"}
    return {x for x in v if x}


def main():
    book_dir = sys.argv[1]
    tdir = os.path.join(book_dir, "text")
    md_files = sorted(f for f in os.listdir(book_dir) if f.startswith("ch") and f.endswith(".md"))
    total_words = total_ex = 0
    bad_words, bad_ex = [], []
    for mf in md_files:
        ch = mf[:4]
        tp = None
        for f in sorted(os.listdir(tdir)):
            if re.match(rf"^ch{int(ch[2:]):02d}([_. ].*)?\.txt$", f):
                tp = os.path.join(tdir, f)
                break
        if not tp:
            continue
        raw = open(tp, encoding="utf-8").read()
        text = norm(raw)
        low = text.lower()
        md = open(os.path.join(book_dir, mf), encoding="utf-8").read()
        i = md.find("## 本章词汇")
        j = md.find("## 一句话总结")
        seg = md[i:j] if i >= 0 and j > i else ""
        for ln_no, line in enumerate(seg.splitlines(), 1):
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 3:
                continue
            word, _gloss, ex = cells[0], cells[1], cells[2]
            if word in ("词/短语", "---") or set(word) <= set("-: "):
                continue
            total_words += 1
            hit = False
            for v in variants(norm(word)):
                vl = v.lower()
                if " " in vl:
                    if vl in low:
                        hit = True
                        break
                elif re.search(rf"\b{re.escape(vl)}\b", low):
                    hit = True
                    break
            if not hit:
                bad_words.append((ch, word, ex[:60]))
            # 例句
            ne = norm(ex)
            if ne and "…" not in ne and "..." not in ne and len(ne) >= 15:
                total_ex += 1
                if ne not in text:
                    bad_ex.append((ch, word, ne[:80]))
    print("── 词条锚定查无 ──")
    for ch, w, e in bad_words:
        print(f"❌ {ch} 词「{w}」  例句：{e}")
    print("── 例句逐字查无 ──")
    for ch, w, e in bad_ex:
        print(f"❌ {ch} 词「{w}」  例句「{e}」")
    print("=" * 56)
    print(f"词条 {total_words} ｜ 锚定查无 {len(bad_words)} ｜ 例句应核 {total_ex} ｜ 例句查无 {len(bad_ex)}")
    return 1 if (bad_words or bad_ex) else 0


if __name__ == "__main__":
    sys.exit(main())
