#!/usr/bin/env python3
"""一次性修复：把引语块内的 **关键词：** 行移到 **中文理解：** 之后。

背景：Daggerbound 批次在部分章节把 关键词 写到了 为什么这样写 之后，
违反 AGENTS.md 的子项顺序（中文理解 / 关键词 / 为什么这样写 / 读者视角提示）。
本脚本行级作用域（禁止 re.S 跨块替换，见 AGENTS.md 第 9g 条）。

用法：python3 scripts/attic/fix_block_order.py <书目录>
"""
import re, sys, glob, os

KW = re.compile(r'^\*\*关键词：\*\*')
CN = re.compile(r'^\*\*中文理解：\*\*')
WHY = re.compile(r'^\*\*为什么这样写：\*\*')
BLOCK = re.compile(r'^> \*\*原句')


def fix_file(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    starts = [i for i, l in enumerate(lines) if BLOCK.match(l)]
    ranges = []
    for idx, s in enumerate(starts):
        e = starts[idx + 1] if idx + 1 < len(starts) else len(lines)
        ranges.append((s, e))
    changed = False
    out = lines[:]
    for (s, e) in reversed(ranges):
        seg = out[s:e]
        ci = next((i for i, l in enumerate(seg) if CN.match(l)), None)
        wi = next((i for i, l in enumerate(seg) if WHY.match(l)), None)
        ki = next((i for i, l in enumerate(seg) if KW.match(l)), None)
        if None in (ci, wi, ki) or ci < ki < wi:
            continue
        kwline = seg[ki]
        del seg[ki]
        if ki < len(seg) and seg[ki].strip() == '':
            del seg[ki]
        ci2 = next(i for i, l in enumerate(seg) if CN.match(l))
        ins = ci2 + 1
        if ins < len(seg) and seg[ins].strip() == '':
            ins += 1
        seg[ins:ins] = [kwline, '']
        out[s:e] = seg
        changed = True
    if changed:
        open(path, 'w', encoding='utf-8').write('\n'.join(out))
    return changed


def main(book_dir):
    n = 0
    for f in sorted(glob.glob(os.path.join(book_dir, 'ch*.md'))):
        if fix_file(f):
            n += 1
            print('fixed:', os.path.basename(f))
    print('files fixed:', n)


if __name__ == '__main__':
    main(sys.argv[1])
