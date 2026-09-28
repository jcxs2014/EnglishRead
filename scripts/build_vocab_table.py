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

    判据：丢弃开头那些**与首行完全相同、且不含句末标点**的行。真正的正文首段
    带标点，不会被误删。
    """
    lines = text.split("\n")
    nonempty = [(i, l.strip()) for i, l in enumerate(lines) if l.strip()]
    if len(nonempty) < 2:
        return text
    title = nonempty[0][1]
    cut = nonempty[0][0] + 1
    for i, l in nonempty[1:]:
        if l == title and not re.search(r"[.?!:;,]", l):
            cut = i + 1
            continue
        break
    return "\n".join(lines[cut:])


def sentences(text: str) -> list[str]:
    flat = re.sub(r"\s+", " ", text.replace("\n", " "))
    return [s.strip() for s in re.split(r"(?<=[.?!”])\s+", flat) if s.strip()]


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
