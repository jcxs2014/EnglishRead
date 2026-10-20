#!/usr/bin/env python3
"""章内引语块重排：按**原文出现顺序**排列 `> **原句 N:**` 块并重编号。

**为什么需要它**（模板坑字典 7f）：19 道 lane 全部只验「引语逐字在不在本章 text」与
「编号连不连续」，**没有一道验块序**——把相邻两块的位置对调，①⑤⑥⑦⑰⑲ 照样全绿。
而「章内时序写反」是本项目缺陷簇第一名。

**判据（与 `scripts/check_quote_order.py` 同一把尺子）**：
  A. 每条引语在本章 `text/` 里展平后**唯一命中**（0 处或多处 ⇒ 不动该章，不猜）
  B. 命中位置**严格递增**
  C. `> **原句 N:**` 的 N 必须是 1..N 连续

**安全约束**：
  · 只搬动**整块**（引语行 + 其后的 中文理解/关键词/为什么这样写/读者视角提示 四行）；
  · 块外的所有行（frontmatter / 导航 / 词汇表 / 一句话总结）**一个字节都不动**；
  · 搬动前后**引语文本的多重集合必须相同**（只换顺序与编号，不改内容）；
  · 默认 dry-run，加 `--apply` 才落盘。

**⚠️ 2026-10-20 修 bug（首版实跑引入过缺陷）**
  首版把「末块之后、标题之前的空行」单独算作 `tail_blank`，而**每个块的尾空行归属**
  却是「谁在原位上谁带着」——结果**原末块搬到中间时会少一个空行、原中间块搬到末位时
  会多一个空行**，实测在 ch17/ch42 各造出 1 处「块间无空行」+ 1 处「标题前双空行」。
  ⇒ 现改为**核心块 + 统一分隔空行**的装配法：解析时把每个块拆成
  `core`（去掉尾部空行）与 `sep`（块间空行数），装配时 core 按新序拼接、sep 用**原文件的
  统一值**（不统一就整章跳过，不猜）；并加落盘后自检（块数/引语多重集/编号连续/无连续空行）。

用法：python3 .memory/tools/reorder_quote_blocks.py "<书目录>" [--apply]
"""
import os
import re
import sys
import glob
import collections

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "scripts"))
from chapter_contiguity import flat  # noqa: E402  与门禁共用归一

Q = re.compile(r"^> \*\*原句 (\d+):\*\*\s*(.+)$")


def parse_blocks(lines):
    """返回 (cores, seps, tail_blank, end, first_idx)。

    cores[i] = 第 i 块的正文行（引语行 + 分析行，**不含**尾部空行）
    seps[i]  = 第 i 块与第 i+1 块之间的空行数（len = n-1）
    tail_blank = 末块之后、`## ` 标题之前的空行数
    """
    idx = [i for i, l in enumerate(lines) if l.startswith("> **原句 ")]
    if not idx:
        return None
    end = next((i for i in range(idx[-1] + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    cores, seps = [], []
    for k, i in enumerate(idx):
        stop = idx[k + 1] if k + 1 < len(idx) else end
        seg = list(lines[i:stop])
        while seg and seg[-1].strip() == "":
            seg.pop()
        cores.append(seg)
        if k + 1 < len(idx):
            # 本块尾部到下一块引语行之间的空行数
            n = 0
            for x in reversed(lines[i:stop]):
                if x.strip() == "":
                    n += 1
                else:
                    break
            seps.append(n)
    tail_blank = 0
    for x in reversed(lines[idx[-1]:end]):
        if x.strip() == "":
            tail_blank += 1
        else:
            break
    return cores, seps, tail_blank, end, idx[0]


def assemble(lines, cores, order, sep, tail_blank, end):
    out = list(lines[:])
    first_idx = None
    for i, l in enumerate(lines):
        if l.startswith("> **原句 "):
            first_idx = i
            break
    body = []
    for k, ci in enumerate(order):
        core = list(cores[ci])
        core[0] = re.sub(r"^> \*\*原句 \d+:\*\*", "> **原句 %d:**" % (k + 1), core[0])
        body += core
        if k < len(order) - 1:
            body += [""] * sep
    body += [""] * tail_blank
    return lines[:first_idx] + body + lines[end:]


def selfcheck(old_lines, new_lines, old_cores, new_cores):
    """落盘前自检：内容与结构都变了 ⇒ 拒绝落盘。"""
    if len(old_cores) != len(new_cores):
        return "块数变了"
    norm = lambda c: tuple(re.sub(r"^> \*\*原句 \d+:\*\*", "> **原句 N:**", x) for x in c)
    o = collections.Counter(norm(c) for c in old_cores)
    n = collections.Counter(norm(c) for c in new_cores)
    if o != n:
        return "块内容（去编号后）多重集合不一致"
    dbl = [i + 1 for i in range(len(new_lines) - 1)
           if new_lines[i].strip() == "" and new_lines[i + 1].strip() == ""]
    if dbl:
        return "产物含连续空行 %s" % dbl
    return None


def main():
    book = sys.argv[1]
    apply_ = "--apply" in sys.argv
    changed = []
    skipped = []
    for md in sorted(glob.glob(os.path.join(book, "ch*.md"))):
        name = os.path.basename(md)
        txts = sorted(glob.glob(os.path.join(book, "text", name[:4] + "*.txt")))
        if not txts:
            continue
        T = flat(open(txts[0], encoding="utf-8").read())
        lines = open(md, encoding="utf-8").read().split("\n")
        got = parse_blocks(lines)
        if not got:
            continue
        cores, seps, tail_blank, end, first_idx = got
        # 分隔空行必须统一，否则不猜
        if len(set(seps)) > 1:
            skipped.append((name, "块间空行数不统一 %s ⇒ 跳过" % sorted(set(seps))))
            continue
        sep = seps[0] if seps else 1
        offs = []
        for core in cores:
            m = Q.match(core[0])
            if not m:
                offs = None
                break
            f = flat(m.group(2)).strip().rstrip(".,;")
            pos = [x.start() for x in re.finditer(re.escape(f), T)]
            if len(pos) != 1:          # 判据 A：非唯一命中 ⇒ 不动这一章
                offs = None
                break
            offs.append(pos[0])
        if not offs:
            skipped.append((name, "引语展平后非唯一命中 ⇒ 跳过"))
            continue
        order = sorted(range(len(offs)), key=lambda k: offs[k])
        if order == list(range(len(order))):
            continue
        new_lines = assemble(lines, cores, order, sep, tail_blank, end)
        new_cores, _, _, _, _ = parse_blocks(new_lines)
        bad = selfcheck(lines, new_lines, cores, new_cores)
        if bad:
            skipped.append((name, "自检不通过：%s ⇒ 不落盘" % bad))
            continue
        old_nums = [int(Q.match(c[0]).group(1)) for c in cores]
        new_nums = [int(Q.match(c[0]).group(1)) for c in new_cores]
        changed.append((name, old_nums, new_nums))
        if apply_:
            open(md, "w", encoding="utf-8").write("\n".join(new_lines))
    print("=== 引语块重排（%s）===" % ("已落盘" if apply_ else "dry-run，加 --apply 落盘"))
    for name, old, new in changed:
        moved = [(a, b) for a, b in zip(old, new) if a != b]
        print("  %-40s %s" % (name[:38], "；".join("位次%d 的原句由 %d 变 %d" % (k, a, b)
                                                 for k, (a, b) in enumerate(moved, 1)) or "（仅位置变化）"))
    for name, why in skipped:
        print("  ⏭ %-40s %s" % (name[:38], why))
    print("  受影响章数：%d ／ 跳过 %d" % (len(changed), len(skipped)))


if __name__ == "__main__":
    main()
