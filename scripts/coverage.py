#!/usr/bin/env python3
"""coverage.py —— 反向覆盖探针：原文中被精读覆盖到的段落比例（提示型）

为什么要有它（2026-10-21）
--------------------------
现有 19 lane 全部只问**正向**问题：「md 里写的引语，在原文里查得到吗？」
没有任何一项问**反向**问题：「原文里的这一段，md 写了吗？」

后果是实测过的：
- `finding-darla` 全书 20 lane 全绿，而分析层被批量删词、读不通；
- `ebenezer-scrooge` 一章 800 词，用 10 个块 + 模板句「重新定义 as」填满，
  块数达标、引语逐字正确，但原文大部分段落从没被引进分析。

本工具把「覆盖」变成可数的东西：把 `text/chNN_*.txt` 按段落切开，
看每个段落是否被本章任一引语触及，报出未被覆盖的段落数与样例。

**不判好坏**：一段叙述本来就可能不需要单独成块。它给的是比例与清单，
供人判断「这一章是不是只读了开头」。

用法：
    python3 scripts/coverage.py "<书目录>" [--show 8] [--min-ratio 0.35]
退出码：
    0 = 报告完成（含比例偏低，属提示型）
    2 = 无法判定（缺 text/ 或缺章）
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.text import norm  # noqa: E402

QUOTE_LINE = re.compile(r"^>\s*\*\*原句\s*(\d+)[:：]\*\*\s*(.*)$")
PARA_MIN = 80           # 少于这个字符数的段落不参与统计（短对话/标题/空行）


def quotes_of(md: Path) -> list[str]:
    """取本章全部引语（含跨行）。"""
    out, cur = [], None
    for line in md.read_text(encoding="utf-8").splitlines():
        m = QUOTE_LINE.match(line)
        if m:
            if cur:
                out.append(cur)
            cur = m.group(2)
            continue
        if cur is not None:
            if line.strip() == "" or line.startswith("#") or line.startswith("**"):
                out.append(cur)
                cur = None
            else:
                cur += " " + line.strip()
    if cur:
        out.append(cur)
    return [q for q in (norm(x) for x in out) if len(q) >= 20]


def paragraphs_of(txt: Path) -> list[str]:
    raw = txt.read_text(encoding="utf-8", errors="ignore")
    paras = [norm(p) for p in re.split(r"\n\s*\n", raw)]
    return [p for p in paras if len(p) >= PARA_MIN]


def covered(para: str, quotes: list[str], probe: int = 60) -> bool:
    head = para[:probe]
    for q in quotes:
        if head in q or q[:probe] in para:
            return True
        # 引语常从段中起头：看段内是否有 40 字窗口落在引语里
        for i in range(0, max(1, len(para) - 40), 40):
            if para[i:i + 40] in q:
                return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("book")
    ap.add_argument("--show", type=int, default=8, help="每章最多列几条未覆盖段落（默认 8）")
    ap.add_argument("--min-ratio", type=float, default=0.35,
                    help="低于该比例标 ⚠️（默认 0.35，仅提示）")
    a = ap.parse_args()

    book = Path(a.book).resolve()
    chapters = sorted(book.glob("ch[0-9][0-9]*.md"))
    if not chapters:
        print(f"✗ 没找到章节 md：{book}")
        return 2

    print(f"=== 反向覆盖：{book.name}（段落是否被本章引语触及）===")
    total_p = total_c = 0
    low, missing_text = [], []
    for md in chapters:
        num = md.name[2:4]
        texts = sorted((book / "text").glob(f"ch{num}_*.txt"))
        if not texts:
            missing_text.append(md.name)
            continue
        paras = paragraphs_of(texts[0])
        if not paras:
            missing_text.append(md.name)
            continue
        qs = quotes_of(md)
        hit = [covered(p, qs) for p in paras]
        unc = [p for p, h in zip(paras, hit) if not h]
        ratio = 1 - len(unc) / len(paras)
        total_p += len(paras)
        total_c += len(paras) - len(unc)
        # 四分位覆盖：看「是不是只读了开头」
        q = []
        for i in range(4):
            seg = hit[i * len(hit) // 4:(i + 1) * len(hit) // 4]
            q.append(sum(seg) / len(seg) if seg else 0.0)
        front, back = q[0], q[3]
        head_only = front > 0 and back == 0
        flag = "⚠️" if head_only else "  "
        print(f"{flag} {md.name[:40]:<42} 段 {len(paras):>3} ｜ 覆盖 {ratio*100:5.1f}% "
              f"｜ 四分位 {''.join(f'{x*100:3.0f}' for x in q)}% ｜ 块 {len(qs):>2}")
        if head_only or (ratio < a.min_ratio and unc):
            low.append((md.name, ratio, q, unc[:a.show], head_only))

    if missing_text:
        print(f"\n❓ 缺 text/ 无法判定 {len(missing_text)} 章：{', '.join(missing_text[:5])}")

    if low:
        print("\n⚠️ 值得看的章（后半完全没覆盖 = 只读了开头；或整体低于 "
              f"{a.min_ratio*100:.0f}%），附未覆盖段落开头：")
        for name, ratio, q, samples, head_only in low:
            tag = "只读了开头" if head_only else "覆盖偏低"
            print(f"\n  [{name}] {ratio*100:.0f}%（{tag}；四分位 "
                  + "/".join(f"{x*100:.0f}%" for x in q) + "）")
            for s in samples:
                print(f"    - {s[:70]}…")

    if total_p:
        print(f"\n全书：段 {total_p} ｜ 被覆盖 {total_c}（{total_c/total_p*100:.1f}%）｜ 章 {len(chapters)}")
        print("ℹ️ 本项为提示型：一段叙述不必都单独成块；比例偏低时请人工确认「是不是只读了开头」。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
