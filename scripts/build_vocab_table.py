#!/usr/bin/env python3
"""Build a three-tier vocab table for a chapter.

The headword list is the only thing supplied by hand, and every headword is
verified verbatim (with word boundaries) against text/chNN*.txt. The example
sentence is extracted from that same file, so an example can never come from
another chapter and can never be invented.

  python3 scripts/build_vocab_table.py <book_dir> --ch 10 \
      --tiers tiers.json

where tiers.json is {"⭐⭐⭐": {"headword": "释义", ...}, "⭐⭐": {...}, "⭐": {...}}

Exits 2 on any headword not found in the chapter — the tool refuses to emit a
table containing an invented word.
"""
import json
import re
import sys
from pathlib import Path


def load_chapter(book_dir: str, ch: str) -> str:
    # ⚠️ 位数不能写死：`--ch 1` 配 `f"ch{ch}_*.txt"` 会找 `ch1_*.txt`，
    # 而磁盘上是 `ch01_*.txt` ⇒ 命中 0 件、静默 SystemExit（本库同型第 4 次：
    # check_chapter_quotes / gen_overview / 自写脚本都栽过）。
    # 做法：依次试 1/2/3/4 位，取第一个命中的；一个都没命中才报错。
    tdir = Path(book_dir, "text")
    for width in (1, 2, 3, 4):
        tag = str(int(ch)).zfill(width)
        hits = sorted(tdir.glob(f"ch{tag}_*.txt"))
        if len(hits) == 1:
            return strip_running_head(hits[0].read_text(encoding="utf-8"))
    sys.exit(f"expected exactly one text/ch<NN>_*.txt for ch{ch} (tried 1-4 digit tags), "
             f"got 0 in {tdir}")


def strip_running_head(text: str) -> str:
    """剥掉 text/ 开头的「章标题 + 书眉」重复行，只留正文。

    提取器把 xhtml 的 <h2>（章标题）写一次，又把同一段跑眉写一次，
    中间是空行——于是在 text/ 里变成「第 1 行=标题 / 第 10 行=标题 / 第 14 行=正文首段」
    （此形态 115 章一致）。不剥的话，正文里第一个出现的词头抽出的例句会以
    「Beatrix Beatrix The stairs wrap...」开头，把书眉当成例句的一部分。

    判据：丢弃开头那些与首行**同一条标题**的重复行，且不含句末标点。真正的正文
    首段带标点，不会被误删。

    ⚠️ 两种跑眉形态都要处理（2026-09-28 The Garnett Girls 实测：原实现对
    本书 28 章**一件都没剥掉**，例句全部以 `PROLOGUE` / `1 Sinking` 开头）：

      A 形态（Beyond That, The Sea 等 115 章）——整行重复：
        第 1 行 = "1 Sinking" / 第 13 行 = "1 Sinking"     → 原判据可剥
      B 形态（本书）——**拆成两行且大小写不同**：
        第 1 行 = "1 Sinking" / 第 13 行 = "13" / 第 16 行 = "Still Waters"
        第 1 行 = "Prologue" / 第 13 行 = "PROLOGUE"        （仅一行、全大写）

    B 形态用「与首行完全相同」永远判不出来（"13" ≠ "13 Still Waters"）⇒ 死代码。
    修法：把开头连续若干行**按顺序拼接**后与首行做**归一化**（去标点 + 忽略大小写）
    的相等判定；命中即整段丢弃。归一化必须去标点，否则
    「EPILOGUE」+「Never Enough Words」拼不出「Epilogue: Never Enough Words」
    （标题里的冒号是副题分隔符，⚠️ 早期版本把它当「首行是正文」的信号，整段放弃剥离
    ——又一处自己造的失败判据）。

    场景地点行（"Venice" / "Isle of Wight" / "London"）：`sentences()` 会把换行
    折成空格，于是它会被粘到正文首句前面（"Venice Imogen watched the door…"）。
    这类行同样没有句末标点、且每词首字母大写、长度极短 ⇒ 一并剥掉（只剥一行）。
    判据不靠「像不像地名」，靠三个可机械核的条件：无句末标点（含逗号分号）+ ≤4 词 +
    每个词首字母大写，**但小写的功能词除外**（of / the / de / la …）——否则
    「Isle of Wight」这类带介词的地名剥不掉。
    """
    FUNC = {"of", "the", "a", "an", "and", "on", "in", "at", "de", "du", "la",
            "le", "van", "von", "der", "das", "di", "el", "y", "e"}
    lines = text.split("\n")
    nonempty = [(i, l.strip()) for i, l in enumerate(lines) if l.strip()]
    if len(nonempty) < 2:
        return text

    def key(s: str) -> str:
        return re.sub(r"[^a-z0-9]+", " ", s.casefold()).strip()

    title = nonempty[0][1]
    cut = nonempty[0][0] + 1
    acc = ""
    for i, l in nonempty[1:4]:             # 最多再吃 3 行（B 形态需 2 行）
        acc = (acc + " " + l).strip()
        if key(acc) == key(title):
            cut = i + 1
            break
    else:
        cut = nonempty[0][0] + 1           # 没匹配上：只丢标题行（与旧行为一致）

    # 剥场景地点行：最多剥两行，且必须还有正文在后面
    # ⚠️ 2026-09-28 The Paris Deception 实测：原实现只剥一行，且判据要求
    # **每个词首字母大写** ⇒ 「June 1936」这种日期行判否（`1936` 首字符不是
    # 大写字母）⇒ 剥不掉，`sentences()` 又因为它没有句末标点而切不开，
    # 于是例句变成 `June 1936 The long, vaulted galleries of the Louvre ...`。
    # 形态：`June 1936` / `September 1940` / `One week earlier` / `5`（纯章号）
    # / `Venice`（地名）。
    # 判据（二选一，且都要求无句末标点 + ≤4 词 + 后面还有正文）：
    #   (a) 地名形态：每个词首字母大写（小写功能词除外）——原判据
    #   (b) 日期形态：首词是月份名，或全行是 1–4 位纯数字（章号）
    # 剥两行是因为「场景地点行 + 日期行」可以相邻。
    MONTHS = {"january", "february", "march", "april", "may", "june", "july",
              "august", "september", "october", "november", "december",
              "jan", "feb", "mar", "apr", "jun", "jul", "aug", "sep", "sept",
              "oct", "nov", "dec"}
    rest = [(i, l) for i, l in nonempty if i >= cut]
    for _ in range(2):
        if len(rest) < 2:
            break
        j, cand = rest[0]
        words = cand.split()
        # 归属行（"From the LiveJournal of …: March 26th, 2022" /
        # "Extract from Class of '92, by Kate Hemsworth …"）：**必须先于标点守卫判**——
        # 这类行含 `:` 与 `,`，会被下面的 `re.search(r"[.?!:;,]")` 否掉，于是
        # `sentences()` 折行时把它粘到正文首句前面（2026-09-30 Broken Light 实测：
        # 全库 10951 件里 28 件、13 本书命中，例句变成
        # "From the LiveJournal of … : March 26th, 2022 The first seven years…"）。
        #
        # ⚠️ **必须同时要求整行无句末标点**（2026-09-30 同日实测的过度修正）：
        # 头一版只判 `^From` 就把**以 From 开头的真散文**也剥了，回归扫到 11 处
        # （"From infancy to death, we're surrounded…" / "From the longhouse they
        # ride out…" / "From what we can see through the windows…"…）——而这些句子
        # 本来就以 `.` 收尾，`sentences()` 切得开，**根本不产生污染**。
        # 判据应当是「这行会不会被粘走」，不是「它像不像归属行」：
        # 粘连只发生在**没有句末标点**的行上。
        is_attr = bool(re.match(r"^(From|Extract from|Reprinted from|Adapted from|"
                                r"Translated from)\b", cand)) \
            and not re.search(r"[.!?]", cand)
        if is_attr:
            cut = j + 1
            rest = [(i, l) for i, l in rest if i > j]
            continue
        if re.search(r"[.?!:;,]", cand) or not (1 <= len(words) <= 4):
            break
        cap = [w for w in words if w.casefold() not in FUNC]
        is_place = bool(cap) and all(w[:1].isupper() for w in cap)
        head = words[0].strip(",.").casefold()
        is_date = head in MONTHS or (len(words) == 1 and cand.isdigit())
        if is_place or is_date:
            cut = j + 1
            rest = [(i, l) for i, l in rest if i > j]
        else:
            break
    return "\n".join(lines[cut:])


def sentences(text: str) -> list[str]:
    """按句末标点切句。

    ⚠️ 断句点必须区分**引号收尾**与**所有格撇号**（2026-09-28 The Garnett Girls
    两次实测，两次都是自己刚修完就造出新的错）：

      ① 本书正文对白用 `‘…’`，上一句以 `.’` / `?’` 收尾时，只看 `[.?!”]` 不断句，
         下一句的例句会带上**上一句的残片**（"She’s already at the walkway.’ Margo
         felt Rachel lurking…"）⇒ 右单引号要进断句点。
      ② 但把 `’` 直接放进 lookbehind 就会误切**所有格**：
         "the Garnetts’ passionately held opinions" 在 `Garnetts’` 后被切开，
         例句变成半句（"The rest of the time she quaked in the face of the Garnetts’"）。

    ⇒ 正确判据：右引号只有在**紧跟在句末标点之后**时才算收尾，即两类断句点
    「`.?!` / `.”`」与「`.?!` + `’`」；单独的 `’` 一律不切。

    ⚠️ 第一处 lookbehind 里**不能放裸右引号**（2026-09-29 Save What's Left 实测）：
    原为 `(?<=[.?!”])`，于是对白 `“You’re hyperventilating,” she said.` 在 `,”` 之后
    被切开，例句只剩 `“You’re hyperventilating,”`——**与上面这条判据直接矛盾**，
    属实现与判据脱节（不是抄写错误，是当初只顾修 ② 漏了 ①）。
    A/B 三本书 45 章：片段例句 6→5 / 1→0 / 0→0，零回归。
    """
    flat = re.sub(r"\s+", " ", text.replace("\n", " "))
    parts = re.split(r"(?<=[.?!])\s+|(?<=[.?!][”’])\s+", flat)
    return [s.strip() for s in parts if s.strip()]


def is_complete_sentence(s: str) -> bool:
    """例句是否是一句**完整**的话（不是被切下来的片段）。

    ⚠️ 2026-09-28 The Paris Deception ch09 实测：原实现取「第一句含该词的
    句子」，而 `sentences()` 的切分点是对话标签与句末标点——于是常取到
    跨标签的半句，例如 `he went on, "but the Depression changed our industry
    entirely.`（开头小写、结尾无收尾引号）。这类例句逐字为真但语义残缺，
    读者看不出它是谁说的话。

    判据（三条都要）：
      ① 以大写字母或开引号开头（不是 `he went on,` 这种接续状语）
      ② 以句末标点 + 可选收尾引号收尾
      ③ 长度在 30–320 字符之间（滤掉整段与过短的口号）
    """
    t = s.strip()
    if not (30 <= len(t) <= 320):
        return False
    if not re.match(r"^[A-Z“‘\"(]", t):
        return False
    return bool(re.search(r"[.!?][”’\"']?$", t))


def main() -> None:
    argv = sys.argv[1:]
    book_dir = argv[0]
    ch = argv[argv.index("--ch") + 1]
    tiers = json.loads(Path(argv[argv.index("--tiers") + 1]).read_text(encoding="utf-8"))

    text = load_chapter(book_dir, ch)
    sents = sentences(text)

    out, missing, fragmented = [], [], []
    for tier, label in (("⭐⭐⭐", "高级"), ("⭐⭐", "进阶"), ("⭐", "基础")):
        rows = []
        for head, gloss in tiers.get(tier, {}).items():
            pat = re.compile(rf"(?<!\w){re.escape(head)}(?!\w)", re.IGNORECASE)
            if not pat.search(text):
                missing.append(f"{tier} {head}")
                continue
            hits = [s for s in sents if pat.search(s)]
            # 完整句优先；一条都取不到才退回任意含该词的句子，并**显式报告**
            example = next((s for s in hits if is_complete_sentence(s)), "")
            if not example:
                if not hits:
                    missing.append(f"{tier} {head} (no example sentence)")
                    continue
                example = hits[0]
                fragmented.append(f"{tier} {head}")
            rows.append(f"| {head} | {gloss} | {example} |")
        if not rows:
            continue
        out += [f"### {tier} {label}", "", "| 词/短语 | 释义 | 例句 |", "|------|------|------|", *rows, ""]

    if missing:
        print("headwords not verbatim in ch%s: %s" % (ch, ", ".join(missing)), file=sys.stderr)
        sys.exit(2)
    if fragmented:
        print("⚠️ 以下词头只取到**片段**例句（本章内无完整句含该词），"
              "落地前请人工换一条完整句：%s" % ", ".join(fragmented), file=sys.stderr)
    print("\n".join(out))


if __name__ == "__main__":
    main()
