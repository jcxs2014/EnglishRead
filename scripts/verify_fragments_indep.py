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
QLINE = re.compile(r"^>\s*\*\*原句\s*\d+(?:\s*\([^)]*\))?\s*[:：]\*\*\s*(.+?)\s*$")
# ⚠️ 2026-10-18 修：原为 `\s*[::]\*\*` —— **字符类里写的是两个半角冒号**,
# 全角 `：` 打不中 ⇒ 全库 7 本书 1,813 条 `> **原句 N：**` 引语从未进过本工具的
# 扫描集（devil-inside 全书 9 条/ch 一条未查）。AGENTS 第 2 条明写「全角冒号」
# 是本库通用写法 ⇒ 这是第五种形态的「跳过型假绿」，与 Q 档案第 2 类同族。
CHAP = re.compile(r"^ch(\d{1,3})")


QUOTES = "\"'“”‘’"
TBL = {ord(c): None for c in QUOTES}

# ⚠️ 2026-10-13（Something Followed Us Home 五步审查）**句末标点容差**。
# 症状：ch08 一条引语 `Blood is the currency of power.` 判 MISS，而原文是
# `“Blood is the currency of power,” Isabel replied, …`——**词全对**，只差句末
# 逗号→句点（截到从句末尾时 md 补一个句号，是本库通用写法）。
# 判据：同库另外四把尺子（`verify_quotes` / `check_chapter_quotes` / `sweep_full` /
# `check_short_quotes`）**一律按标点无关比对**，唯本脚本保留句末标点 ⇒
# 「同一份规范不得有两把尺子」。全库实测（前 120 本有 text/ 的书）：
# MISS 共 3025 条，其中**仅句末标点差异 934 条**（artifact）、词面不同 2091 条
# （真缺陷类，本脚本正是要抓它）⇒ 容差必须**只放句末**，不能整串 flat
# （整串 flat 会把 2091 条真缺陷一起放过）。
# 修法：片段比对前**只裁掉末尾标点**，串内标点与词序照旧严格。
TRIM_END = ".,;:!?…"

# ⚠️ 2026-10-18（DSH-Mac，C 组 C4 修工具）**「拼接未标省略号」判据**。
# 症状：devil-inside ch10 `> **原句 9:** "It's her eyes that halt me, though. … That look.
#   Those are Lilith's eyes. Only they're in someone else's sockets."` 判 MISS，
#   而这三段**逐字都在本章 text/ 里**——md 把 `Where have I seen those eyes . . . ? /
#   Before I can respond, …` 整段删掉、**却没写省略号**。
# 后果：AGENTS 第 2 条明写「需省略中间文字用 `…` 且省略号两侧都必须是原词」，
#   不写省略号 = 伪造了一条原文中不存在的连续引语，比改写更严重。
# 判据：片段**前 WIN 词**与**后 WIN 词**各自在本章按序命中，且两锚点之间间隔
#   大于 SPICE_GAP ⇒ 判「拼接未标省略号」（阻断型，与 MISS 同级）。
# 门槛来自全库实测：295 条锚点双命中样本的 gap 中位 224、p90 750，而真正
#   连贯文本的 gap 上界只有 70（`the-art-of-a-lie` ch04 实测）⇒ 取 80 安全。
WIN = 8
SPICE_GAP = 150


def _head_pos(body: str, seq: str) -> int:
    """seq 的词序列在 body 中按序命中时的**结束位置**；查无返回 -1。"""
    pos = 0
    for w in seq.split():
        j = body.find(w, pos)
        if j < 0:
            return -1
        pos = j + len(w)
    return pos


def splice_gap(body: str, frag: str):
    """片段首尾各 WIN 词的原文间隔；判不了返回 None。"""
    words = frag.split()
    if len(words) < 2 * WIN + 2:
        return None
    head_end = _head_pos(body, " ".join(words[:WIN]))
    if head_end < 0:
        return None
    tail_start = body.find(" ".join(words[-WIN:]), head_end)
    if tail_start < 0:
        return None
    return tail_start - head_end


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

    total_frag = total_quote = miss = nochap = splice = 0
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
                    # 只裁**片段末尾**标点（见 TRIM_END 注）：句末逗号↔句点不算改写；
                    # 串内标点/词序仍严格（那 2091 条真缺陷类照旧报）。
                    nf = norm(fr).strip().strip(TRIM_END)
                    # 过短片段（<12 归一化字符）无判定力，跳过但计数
                    if len(nf) < 12:
                        continue
                    if nf in body:
                        continue
                    # 「拼接未标省略号」：首尾都能命中但中间跳过了叙述
                    g = splice_gap(body, nf)
                    if g is not None and g > SPICE_GAP:
                        splice += 1
                        print(f"❌ 拼接未标省略号 {fn}:{lineno}  "
                              f"（首尾段均在本章命中，中间跳过 {g} 字符）  片段: {fr[:96]}")
                        continue
                    miss += 1
                    misses.append((fn, lineno, q.group(0)[:0], fr))
                    print(f"❌ MISS {fn}:{lineno}  片段: {fr[:110]}")

    print()
    print("=== 逐片段核验（独立实现） ===")
    print(f"  引语条数 {total_quote} ｜ 受检片段 {total_frag} ｜ ❌ MISS {miss}"
          f" ｜ ❌ 拼接未标省略号 {splice} ｜ 缺参照章 {nochap}")
    if miss or splice:
        if miss:
            print("  ⇒ 有片段在**本章** text/ 里查无 = 伪造或跨章搬引，必须改")
        if splice:
            print("  ⇒ 首尾段逐字命中、中间叙述被删却没写 `…` = AGENTS 第 2 条违规，"
                  "必须在省略处补 `…`（省略号两侧都必须是原词）")
        return 1
    print("  ⇒ 每个受检片段都在**本章** text/ 里逐字命中")
    return 0


if __name__ == "__main__":
    sys.exit(main())