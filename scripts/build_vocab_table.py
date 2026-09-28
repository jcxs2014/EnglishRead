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
    hits = sorted(Path(book_dir, "text").glob(f"ch{ch}_*.txt"))
    if len(hits) != 1:
        sys.exit(f"expected exactly one text/ch{ch}_*.txt, got {len(hits)}")
    return strip_running_head(hits[0].read_text(encoding="utf-8"))


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

    # 剥场景地点行：只剥一行，且必须还有正文在后面
    rest = [(i, l) for i, l in nonempty if i >= cut]
    if len(rest) >= 2:
        j, cand = rest[0]
        words = cand.split()
        cap = [w for w in words if w.casefold() not in FUNC]
        if (not re.search(r"[.?!:;,]", cand) and 1 <= len(words) <= 4
                and cap and all(w[:1].isupper() for w in cap)):
            cut = j + 1
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
    """
    flat = re.sub(r"\s+", " ", text.replace("\n", " "))
    parts = re.split(r"(?<=[.?!”])\s+|(?<=[.?!][”’])\s+", flat)
    return [s.strip() for s in parts if s.strip()]


def main() -> None:
    argv = sys.argv[1:]
    book_dir = argv[0]
    ch = argv[argv.index("--ch") + 1]
    tiers = json.loads(Path(argv[argv.index("--tiers") + 1]).read_text(encoding="utf-8"))

    text = load_chapter(book_dir, ch)
    sents = sentences(text)

    out, missing = [], []
    for tier, label in (("⭐⭐⭐", "高级"), ("⭐⭐", "进阶"), ("⭐", "基础")):
        rows = []
        for head, gloss in tiers.get(tier, {}).items():
            pat = re.compile(rf"(?<!\w){re.escape(head)}(?!\w)", re.IGNORECASE)
            if not pat.search(text):
                missing.append(f"{tier} {head}")
                continue
            example = next((s for s in sents if pat.search(s)), "")
            if not example:
                missing.append(f"{tier} {head} (no example sentence)")
                continue
            rows.append(f"| {head} | {gloss} | {example} |")
        if not rows:
            continue
        out += [f"### {tier} {label}", "", "| 词/短语 | 释义 | 例句 |", "|------|------|------|", *rows, ""]

    if missing:
        print("headwords not verbatim in ch%s: %s" % (ch, ", ".join(missing)), file=sys.stderr)
        sys.exit(2)
    print("\n".join(out))


if __name__ == "__main__":
    main()
