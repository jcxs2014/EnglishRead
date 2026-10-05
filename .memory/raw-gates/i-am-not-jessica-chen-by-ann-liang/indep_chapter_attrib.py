#!/usr/bin/env python3
"""**第二实现**：逐章归属独立核对（b 步用）。

为什么要第二实现（AGENTS 第 10 条「审查过程自身四条纪律」第 1 条：
「换检查路径」必须换实现，不能换文件名）：写作期走的是
`check_chapter_quotes.py --book-dir` 全书模式；`audit_structure` /
`check_chapter_quotes` 又都拿同一套 `_norm()`。复用同一实现＝用同一把尺子
量两遍。

本实现与那套**无共享代码**，且口径故意不同——多查两件它们不查的事：
  ① **短引语全覆盖**：`check_chapter_quotes` 与 `verify_quotes` 都跳过
     `<20 flat 字符` 的引语（实测本书 10 条），那些行**从未被任何门禁核过**；
  ② **反向跨章**：不止查「在本章」，还查「是否**只**在本章」——
     一段话在两章都出现时，单向检查永远绿。

用法：python3 scripts/attic/indep_chapter_attrib.py "<书目录>"
"""
import re
import sys
from pathlib import Path

RX = re.compile(r"^>\s*\*\*原句\s*(\d+):?\*\*\s*(.*)$")


def flat(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.casefold())


def main():
    bd = Path(sys.argv[1])
    tdir = bd / "text"
    texts = {}
    for p in sorted(tdir.glob("ch*.txt")):
        n = int(re.search(r"ch(\d+)", p.name).group(1))
        texts[n] = flat(p.read_text(encoding="utf-8"))

    total = miss = shared = 0
    short_total = 0
    print("章  块数  本章命中  他章也命中  短引语(<20flat) 判定")
    for md in sorted(bd.glob("ch*.md")):
        mn = int(re.search(r"ch(\d+)", md.name).group(1))
        blocks = []
        for line in md.read_text(encoding="utf-8").split("\n"):
            m = RX.match(line)
            if m:
                blocks.append((int(m.group(1)), m.group(2).strip()))
        if not blocks or mn not in texts:
            continue
        own = texts[mn]
        others = {k: v for k, v in texts.items() if k != mn}
        miss_here = []
        shared_here = []
        short_here = 0
        for seq, q in blocks:
            fq = flat(q.strip("“”\""))
            if not fq:
                continue
            if len(fq) < 20:
                short_here += 1
            total += 1
            if fq not in own:
                miss_here.append(seq)
                miss += 1
                continue
            hit = [k for k, v in others.items() if fq in v]
            if hit:
                shared_here.append((seq, hit))
                shared += 1
        short_total += short_here
        flag = []
        if miss_here:
            flag.append(f"❌ 未命中本章 {miss_here}")
        if shared_here:
            flag.append(f"⚠️ 他章也命中 {shared_here}")
        print(f"ch{mn:02d} {len(blocks):>4} {len(blocks)-len(miss_here):>8} "
              f"{len(shared_here):>10} {short_here:>14}  "
              f"{'｜'.join(flag) if flag else '✅'}")
    print(f"\n合计：{total} 条引语｜本章未命中 {miss}｜他章也命中 {shared}"
          f"｜其中 <20 flat 字符的短引语 {short_total} 条（本实现逐条核，主门禁全部跳过）")
    return 1 if miss else 0


if __name__ == "__main__":
    sys.exit(main())