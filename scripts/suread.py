#!/usr/bin/env python3
"""suread.py —— 生产期素读清单（把「我读过原文」变成可核对的数据）

为什么要有它（2026-10-21）
--------------------------
「素读」原本只是审查方 R1 的动作：先读 `text/chNN.txt`，写出 5–8 条「谁做了什么」，
再开 md 对账。但执行方写的时候**本来就要读原文**，这一步没做，等于把最容易发现
「读错了章/漏了转折/把自我安慰当事实」的机会，推迟到审查期。

本工具让写的人在动笔前先交 5–8 条事实，每条必须挂一段**原文逐字锚点**：
锚点在原文找不到 = 这条事实是凭印象写的，直接打回。产出可入库的 JSON，
审查方第一眼就能看见「写的人到底读了哪几段」。

用法：
    python3 scripts/suread.py "<书目录>" <chNN> <facts.txt> [--check]

facts.txt 每行一条，格式：
    原文里能逐字找到的一段话 || 谁做了什么（一条事实）
空行与 # 开头的行忽略。锚点建议 15–60 字符。

产出：.memory/raw-gates/<slug>/production/<chNN>-suread.json
退出码：
    0 = 全部锚点命中
    1 = 有锚点在原文中找不到（或不足 5 条）
    2 = 无法判定（找不到本章 text）
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def find_anchor(text: str, anchor: str) -> tuple[int, int] | None:
    """逐字找；失败时退化为「空白/弯直引号不敏感」的匹配。"""
    i = text.find(anchor)
    if i >= 0:
        return i, i + len(anchor)
    pat = re.escape(anchor).replace(r"\ ", r"\s+")
    pat = pat.replace("\u2018", "['\u2018]").replace("\u2019", "['\u2019]")
    pat = pat.replace("\u201c", '["\u201c]').replace("\u201d", '["\u201d]')
    m = re.search(pat, text)
    return (m.start(), m.end()) if m else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("book")
    ap.add_argument("chapter", help="章号，如 ch03 或 03")
    ap.add_argument("facts")
    ap.add_argument("--min", type=int, default=5, help="至少几条事实（默认 5）")
    ap.add_argument("--check", action="store_true", help="只校验，不写 JSON")
    a = ap.parse_args()

    book = Path(a.book).resolve()
    num = re.sub(r"\D", "", a.chapter).zfill(2)
    texts = sorted((book / "text").glob(f"ch{num}_*.txt"))
    if not texts:
        print(f"❓ 无法判定：{book.name} 没有 text/ch{num}_*.txt")
        return 2
    text = texts[0].read_text(encoding="utf-8", errors="ignore")

    lines = []
    for ln in Path(a.facts).read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        parts = re.split(r"\s*\|\|\s*", ln, maxsplit=1)
        if len(parts) != 2:
            print(f"⚠️ 格式不对（需要「锚点 || 事实」）：{ln[:50]}")
            continue
        lines.append((parts[0].strip(), parts[1].strip()))

    rows, bad = [], []
    for anchor, fact in lines:
        hit = find_anchor(text, anchor)
        if not hit:
            bad.append((anchor, fact))
            continue
        rows.append({"fact": fact, "anchor": anchor, "start": hit[0], "end": hit[1]})

    print(f"=== 素读清单：{book.name} ch{num}（text {len(text)} 字符）===")
    for r in rows:
        print(f"  ✅ [{r['start']:>6}:{r['end']:>6}] {r['fact'][:52]}  ←「{r['anchor'][:28]}…」")
    for anchor, fact in bad:
        print(f"  ❌ 原文查无：{fact[:40]}  ←「{anchor[:40]}」")

    ok = not bad and len(rows) >= a.min
    if len(rows) < a.min:
        print(f"⚠️ 只给了 {len(rows)} 条，少于 {a.min} 条 —— 一章通常至少 5 条（谁做了什么）")
    if bad:
        print(f"❌ {len(bad)} 条锚点在原文中找不到 —— 这条事实是凭印象写的，先回原文重读")

    if ok and not a.check:
        slug = book.name
        out = REPO / ".memory" / "raw-gates" / slug / "production"
        out.mkdir(parents=True, exist_ok=True)
        dest = out / f"ch{num}-suread.json"
        dest.write_text(json.dumps({"book": slug, "chapter": f"ch{num}",
                                    "text": str(texts[0].relative_to(REPO)),
                                    "facts": rows}, ensure_ascii=False, indent=1),
                        encoding="utf-8")
        print(f"\n已写入 {dest.relative_to(REPO)}")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
