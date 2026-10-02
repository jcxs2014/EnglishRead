#!/usr/bin/env python3
"""
gen_bird_overview.py — Bird of a Thousand Stories 总览三篇的**引语池**生成器

为什么要有这个（AGENTS 8.5「换生产方式」）
-----------------------------------------
总览三篇（概述/金句精选/情感节点）**不在 `verify_quotes` 主口径内**，是独立盲区；
而本项目已反复实测：「凭会话记忆重打总览」⇒ 引语大面积伪造（概述 5 条 0 命中）。
本脚本把「从已过门禁的章节 md 里抽引语」这一步**程序化**，
让总览的英文只能来自**已核实引语池**，不可能凭空产生。

用法
----
    python3 scripts/bird/gen_bird_overview.py <书目录> [--pool-out <json>]
    # 打印池子统计 + 每章可引条数 + 抽出的候选引语（供挑选）

口径
----
  - 引语一律从 `chNN *.md` 的 `> **原句 N:**` 行抽取（与 verify_quotes 同格式）
  - 每条抽出后**再对 `text/chNN_*.txt` 做一次 flat 比对**，不在本章即丢弃（错章即死）
  - 金句候选按长度排序（长的适合金句），并给出每章的可用条数
"""
import glob
import json
import os
import re
import sys

QUOTE_RE = re.compile(r'(?m)^>\s*\*\*原句\s*\d+[：:]\*\*\s*(.+?)\s*$')
BLOCK_SPLIT = re.compile(r"(?m)^>\s\*\*原句\s*\d+[：:]")


def flat(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def clean(q):
    q = q.strip()
    # ⚠️ 源格式是 `> **原句 N:** "…"`；若引文本身带粗体包裹（`** "…" **`），
    # 切块后第一行会残留 `**`。不剥掉的话整串 pool 都带 `**`，
    # 写进总览后 check_overview_labels 之类按 `**① "…"**` 判就全部对不上。
    q = q.strip("*").strip()
    if q.startswith('"') and q.endswith('"'):
        q = q[1:-1]
    return q.strip()


def main():
    book = sys.argv[1]
    textdir = os.path.join(book, "text")
    pool = {}
    stats = []
    for md in sorted(glob.glob(os.path.join(book, "ch*.md")),
                     key=lambda x: int(re.search(r"ch(\d+)", os.path.basename(x)).group(1))):
        nn = int(re.search(r"ch(\d+)", os.path.basename(md)).group(1))
        tf = glob.glob(os.path.join(textdir, "ch%02d_*.txt" % nn)) or \
             glob.glob(os.path.join(textdir, "ch%d_*.txt" % nn))
        if not tf:
            continue
        ftxt = flat(open(tf[0], encoding="utf-8").read())
        src = open(md, encoding="utf-8").read()
        # 按块切，取每块第一段（禁令 5：引语只取一个说话轮次）
        items = []
        for blk in BLOCK_SPLIT.split(src)[1:]:
            head = blk.split("\n", 1)[0]
            q = clean(head)
            if len(flat(q)) < 20:      # <20 flat 字符属短引语，单独口径
                continue
            for part in [p for p in re.split(r"\s*…\s*", q) if p.strip()]:
                if flat(part) in ftxt:
                    items.append(part)
                    break
        if items:
            pool[nn] = items
            stats.append((nn, os.path.basename(md), len(items), len(src)))

    total = sum(len(v) for v in pool.values())
    print(f"=== 引语池：{len(pool)} 章 / 共 {total} 条（均已对 text/ 二次 flat 核验）===")
    print(f"{'NN':>3} {'可用':>4}  {'md字节':>7}  文件")
    for nn, name, n, size in stats:
        print(f"{nn:3d} {n:4d}  {size:7d}  {name}")

    if "--pool-out" in sys.argv:
        out = sys.argv[sys.argv.index("--pool-out") + 1]
        with open(out, "w", encoding="utf-8") as f:
            json.dump(pool, f, ensure_ascii=False, indent=1)
        print(f"\n池已写：{out}")

    print("\n=== 最长候选（适合金句精选；按 flat 长度降序，前 40）===")
    flat_items = [(nn, q, len(flat(q))) for nn, qs in pool.items() for q in qs]
    for nn, q, n in sorted(flat_items, key=lambda x: -x[2])[:40]:
        print(f"[ch{nn:02d} {n:3d}] {q[:150]}")


if __name__ == "__main__":
    sys.exit(main())
