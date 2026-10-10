#!/usr/bin/env python3
"""check_quote_order.py — 章内引语块顺序 vs 原文顺序（第 10 条 c/d 步**抽查级**，不进门禁）

**为什么需要它**：18 道 lane 全部只验「引语逐字在不在本章 text」与「编号连不连续」，
**没有一道验块序**——把原句 3 与原句 5 的位置对调，①⑤⑥⑦⑰⑲ 照样全绿。
而「章内时序写反」是本项目缺陷簇第一名（实证见 `docs/实测档案/J_第8-10条_案例移出.md`）。
本书第一轮整改后仍有 **4/22 章**块序与原文相反（ch05/ch06/ch09/ch17），
六道门禁 + gate.sh 全部 0 阻断，只有换这把尺子才看得见。

判据（全部走 `chapter_contiguity.flat`，与门禁同一归一口径，不自造第二套字形规则）：
  A. 每条引语在**本章 text/** 里展平后**唯一命中**（0 处或多处 ⇒ 该章标「不可判定」，不判红）
  B. 命中位置必须**严格递增**
  C. `> **原句 N:**` 的 N 必须是 1..len(blocks) 连续

退出码：0 = 无缺陷；1 = 有 B/C 缺陷；2 = 有用章无法判定（A 不过）。
用法：python3 scripts/check_quote_order.py "<书目录>"
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chapter_contiguity import flat  # noqa: E402  与门禁共用归一，避免第二套尺子

Q = re.compile(r'^> \*\*原句 (\d+):\*\*\s*(.+)$')


def check(md: Path, txt: Path):
    lines = md.read_text(encoding="utf-8").split("\n")
    idx = [i for i, l in enumerate(lines) if l.startswith("> **原句 ")]
    if not idx:
        return None
    end = next((i for i in range(idx[-1] + 1, len(lines)) if lines[i].startswith("## ")),
               len(lines))
    quotes = []
    for k, i in enumerate(idx):
        stop = idx[k + 1] if k + 1 < len(idx) else end
        m = Q.match(lines[i])
        if not m:
            return None
        quotes.append((int(m.group(1)), m.group(2), i + 1, "\n".join(lines[i:stop])))
    T = flat(txt.read_text(encoding="utf-8"))
    offs = []
    for n, q, ln, _blk in quotes:
        f = flat(q).strip().rstrip('.,;')
        p = T.find(f)
        if p < 0 or T.count(f) != 1:
            return "undecidable", f, p
        offs.append((n, p, ln))
    bad = []
    seq = [o[1] for o in offs]
    for a, b in zip(offs, offs[1:]):
        if b[1] <= a[1]:
            bad.append(f"原句 {b[0]}（md:{b[2]}）在原文里位于原句 {a[0]} 之前")
    if [o[0] for o in offs] != list(range(1, len(offs) + 1)):
        bad.append(f"编号不连续：{[o[0] for o in offs]}")
    return ("defect" if bad else "ok"), bad, len(offs)


def main(book_dir):
    B = Path(book_dir)
    files = sorted(B.glob("ch*.md"))
    if not files:
        print(f"=== {B.name}：无 ch*.md，未做判定 ===")
        return 2
    n_def = n_und = n_blk = 0
    for md in files:
        stem = re.match(r'^(ch\d+)', md.name).group(1)
        cands = list(B.glob(f"text/{stem}_*.txt"))
        if not cands:
            print(f"  ❓ {md.name}：无 text/ 提取件，不可判定")
            n_und += 1
            continue
        r = check(md, cands[0])
        if r is None:
            continue
        kind, info, extra = r
        if kind == "undecidable":
            print(f"  ❓ {md.name}：引语展平后非唯一命中（pos={extra}），该章不判")
            n_und += 1
            continue
        if kind == "defect":
            n_def += 1
            for d in info:
                print(f"  ❌ {md.name}: {d}")
        n_blk += extra
    print(f"=== 章内块序：{len(files)} 个 md / {n_blk} 块，"
          f"顺序或编号缺陷 {n_def} 章 ／ 不可判定 {n_und} 章 ===")
    return 1 if n_def else (2 if n_und else 0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
