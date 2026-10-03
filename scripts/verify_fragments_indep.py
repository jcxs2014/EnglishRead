#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""逐片段核验引语（独立实现，与 verify_quotes.py / check_chapter_quotes.py 不同路径）

**为什么需要它**（2026-10-03 Darling Girls 五步审查 b 步实证）：
`verify_quotes.py` 对含省略号 / em-dash 拼接的引语只校验**第一片段**，后续片段
**整段丢弃不验**——实证：ch71 原句 7 被接上一段纯属虚构的对白
（`'I feel so lucky now.' 'For what?' 'Because I have you.'`，三句在 epub 里
grep 全为 False），而 `verify_quotes` 仍报 `7/7 ✅`；同一条
`check_chapter_quotes.py` 报 `6/7` 抓到了。⇒ **553/553 这个数字对拼接引语无效**。

本脚本的口径：
  1. 取每条 `> **原句 N:** …` 整行正文；
  2. 按分隔符切成片段：`(?:…|\.\.\.|—|–|-{2,})`（半角/全角省略号、em/en dash、连字符）；
  3. **每个片段各自**在该章 `text/chNN*.txt` 里做「规范化空白 + 统一引号」的子串判定；
  4. 任一片段查无 ⇒ 报 MISS，并列出该片段。

与既有脚本的差异（=「换实现」的依据）：
  - verify_quotes：peel 剥壳后只验主串，尾片段不查；参照集 = epub 展平全文
  - check_chapter_quotes：整串一次判定，不拆片段 ⇒ 拼接引语整串必 MISS（但它因此报不出
    「哪一段」是假的，只能报整串）
  - 本脚本：**按章 + 逐片段**独立判定，参照集 = text/ 逐章（比 epub 更严，跨章搬句也抓得到）

退出码：0 = 全片段命中；1 = 有 MISS；2 = 缺参照集/无法判定。
"""
import os
import re
import sys

SPLIT = re.compile(r"(?:…|\.\.\.|—|–|―|-{2,})")
QLINE = re.compile(r"^>\s*\*\*原句\s*\d+(?:\s*\([^)]*\))?\s*[::]\*\*\s*(.+?)\s*$")
CHAP = re.compile(r"^ch(\d{1,3})")


QUOTES = "\"'“”‘’"
TBL = {ord(c): None for c in QUOTES}


def norm(s: str) -> str:
    """规范化：剔除全部引号字符、统一破折号、压缩空白、小写。

    ⚠️ **为什么剔除全部引号**（2026-10-03 假红型实证）：原文**同一章内就混用**
    `'…'` 与 `“…”`，且同一段对话里内外层引号形态还不一致（ch64 实测
    `‘“Give me the tin, you bitch!” he said, pushing me again.`）。md 把它写成
    全单引号 ⇒ 词全对、字符级不等。只剥**外围**引号仍会因**内部**引号报假红。
    引号是作者的排版，不属于引语本体 ⇒ 两侧一并剔除。
    AGENTS.md 亦规定「弯/直引号差异视为正常」。
    """
    s = s.translate(TBL)
    s = s.replace("—", "-").replace("–", "-").replace("―", "-")
    s = s.replace("…", "...")
    return re.sub(r"\s+", " ", s).strip().lower()


def load_chapter(text_dir: str, nn: str):
    """读该章 text/ 提取件（允许文件名零填充与后缀差异），返回规范化正文或 None。

    ⚠️ 零填充坑（2026-10-03 实测）：提取件是 `ch09_*.txt`，而 md 文件名解析出的
    章号是 `9`；用 `startswith("ch9_")` 会**匹配不到** ⇒ 该章被静默跳过、
    只报一句「缺参照章」。第一版就踩了，8 章未查。⇒ 必须同时试补零/不补零两种前缀。
    """
    names = os.listdir(text_dir)
    prefixes = {f"ch{int(nn)}_", f"ch{int(nn):02d}_"}
    cands = [f for f in names if any(f.startswith(p) for p in prefixes)
             and f.endswith(".txt")]
    if not cands:
        cands = [f for f in names if re.fullmatch(rf"ch{int(nn)}\.txt", f)]
    if not cands:
        return None
    with open(os.path.join(text_dir, sorted(cands)[0]), encoding="utf-8") as f:
        return norm(f.read())


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    book = sys.argv[1]
    text_dir = os.path.join(book, "text")
    if not os.path.isdir(text_dir):
        print(f"❓ 无法判定：缺参照集 {text_dir}")
        return 2

    total_frag = total_quote = miss = nochap = 0
    misses = []
    for fn in sorted(os.listdir(book)):
        m = CHAP.match(fn)
        if not m:
            continue
        nn = str(int(m.group(1)))
        body = load_chapter(text_dir, nn)
        if body is None:
            nochap += 1
            print(f"❓ {fn}: 缺 ch{nn} 参照件")
            continue
        with open(os.path.join(book, fn), encoding="utf-8") as f:
            for lineno, line in enumerate(f, 1):
                q = QLINE.match(line.strip())
                if not q:
                    continue
                total_quote += 1
                raw = q.group(1)
                frags = [x for x in (p.strip() for p in SPLIT.split(raw)) if x]
                for fr in frags:
                    total_frag += 1
                    nf = norm(fr)
                    # 过短片段（<12 归一化字符）无判定力，跳过但计数
                    if len(nf) < 12:
                        continue
                    if nf not in body:
                        miss += 1
                        misses.append((fn, lineno, q.group(0)[:0], fr))
                        print(f"❌ MISS {fn}:{lineno}  片段: {fr[:110]}")

    print()
    print("=== 逐片段核验（独立实现） ===")
    print(f"  引语条数 {total_quote} ｜ 受检片段 {total_frag} ｜ ❌ MISS {miss}"
          f" ｜ 缺参照章 {nochap}")
    if miss:
        print("  ⇒ 有片段在**本章** text/ 里查无 = 伪造或跨章搬引，必须改")
        return 1
    print("  ⇒ 每个受检片段都在**本章** text/ 里逐字命中")
    return 0


if __name__ == "__main__":
    sys.exit(main())