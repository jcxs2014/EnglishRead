#!/usr/bin/env python3
"""Affairs of State 关键词锚定自查（AGENTS.md 第8e条，≥20章推荐）。

对全书每章精读文件：
  1) 结构：每个 `> **原句 N:**` 块必须含四子项（中文理解/关键词/为什么这样写/读者视角提示），编号连续；
  2) 锚定：`**关键词：**` 里每个英文短语须能在本块引语行中找到（允许词形变化与引号/撇号差异）；
  3) 孤儿块 / 重复引语块检测。

用法: python3 scripts/attic/kw_anchor_afs.py "<书目录>"
"""
import re
import sys
from pathlib import Path

STOP = {"the", "a", "an", "of", "to", "in", "for", "and", "or", "is", "are", "was", "were",
        "it", "its", "i", "you", "we", "they", "he", "she", "my", "your", "our", "their",
        "that", "this", "with", "on", "at", "be", "not", "no"}


def norm(s: str) -> str:
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", s).strip().lower()


def tok(s: str):
    return [w for w in re.findall(r"[a-z']+", norm(s)) if w not in STOP and len(w) > 1]


def word_in(word: str, quote_norm: str) -> bool:
    if word in quote_norm:
        return True
    # 词形变化容忍：ing/ed/es/s/d
    for suf in ("ing", "ed", "es", "s", "d"):
        if word.endswith(suf) and word[: -len(suf)] in quote_norm:
            return True
        if (word + suf) in quote_norm:
            return True
    return False


def main(book_dir: str):
    problems = []
    files = sorted(Path(book_dir).glob("ch*.md"))
    total_kw = total_blocks = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        lines = text.split("\n")
        blocks = []  # (n, quote, body_lines)
        cur = None
        for ln in lines:
            m = re.match(r"^> \*\*原句 (\d+):\*\* (.+)$", ln)
            if m:
                if cur:
                    blocks.append(cur)
                cur = [int(m.group(1)), m.group(2), []]
            elif cur is not None:
                if ln.startswith("> ") or (ln.strip() == "" and False):
                    cur[2].append(ln)
                else:
                    if re.match(r"^\*\*", ln.strip()) or ln.strip() == "":
                        cur[2].append(ln)
                    if re.match(r"^## ", ln):
                        blocks.append(cur)
                        cur = None
        if cur:
            blocks.append(cur)

        nums = [b[0] for b in blocks]
        if nums != list(range(1, len(nums) + 1)):
            problems.append(f"{f.name}: 编号不连续 {nums}")
        seen_quotes = set()
        for n, quote, body in blocks:
            total_blocks += 1
            qnorm = norm(quote)
            blob = norm(" ".join(body))
            # 四子项齐全
            for item in ("中文理解", "关键词", "为什么这样写", "读者视角提示"):
                if f"**{item}：**" not in " ".join(body):
                    problems.append(f"{f.name} 原句{n}: 缺子项 {item}")
            # 重复块
            key = qnorm[:60]
            if key in seen_quotes:
                problems.append(f"{f.name} 原句{n}: 与前块引语重复")
            seen_quotes.add(key)
            # 关键词锚定
            m = re.search(r"\*\*关键词：\*\* (.+)", "\n".join(body))
            if not m:
                problems.append(f"{f.name} 原句{n}: 有关键词行")
                continue
            total_kw += 1
            for phrase in m.group(1).split(","):
                phrase = phrase.strip()
                if not phrase or not re.search(r"[a-zA-Z]", phrase):
                    continue
                words = tok(phrase)
                if not words:
                    continue
                missing = [w for w in words if not word_in(w, qnorm)]
                if missing:
                    problems.append(f"{f.name} 原句{n}: 关键词未锚定引语 -> '{phrase}' (缺 {missing})")
    print(f"扫描 {len(files)} 文件 / {total_blocks} 引语块 / {total_kw} 关键词行")
    if problems:
        print(f"发现 {len(problems)} 处问题：")
        for p in problems:
            print("  -", p)
        sys.exit(1)
    print("锚定自查全绿：关键词全部命中本块引语，无缺子项/编号断裂/重复块")


if __name__ == "__main__":
    main(sys.argv[1])
