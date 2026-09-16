#!/usr/bin/env python3
"""
fix_strange_block_order.py — 行级修复「关键词」写在「为什么这样写」之后的结构缺陷

背景：Strange Is the Light 部分章节生成时把四子项顺序写成
    中文理解 → 为什么这样写 → 关键词 → 读者视角提示
规范顺序为
    中文理解 → 关键词 → 为什么这样写 → 读者视角提示

修复方式：纯行级作用域（**禁止 re.S 跨块**），仅当连续四行字段恰好是
[中文理解, 为什么这样写, 关键词, 读者视角提示] 时交换第 2、3 行。

用法：
  python3 scripts/attic/fix_strange_block_order.py <md 文件> [更多文件...]
"""
import sys, re

ORDER = ['中文理解', '关键词', '为什么这样写', '读者视角提示']
WRONG = ['中文理解', '为什么这样写', '关键词', '读者视角提示']
FIELD = re.compile(r'^\*\*(中文理解|关键词|为什么这样写|读者视角提示)[:：]\*\*')


def fix(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    idx = [i for i, l in enumerate(lines) if FIELD.match(l)]
    swaps = 0
    i = 0
    while i + 3 < len(idx):
        quad = idx[i:i + 4]
        names = [FIELD.match(lines[j]).group(1) for j in quad]
        if names == WRONG:
            a, b = quad[1], quad[2]
            lines[a], lines[b] = lines[b], lines[a]
            swaps += 1
            i += 4
        elif names == ORDER:
            i += 4
        else:
            i += 1
    if swaps:
        open(path, 'w', encoding='utf-8').write('\n'.join(lines))
    return swaps


if __name__ == '__main__':
    total = 0
    for p in sys.argv[1:]:
        n = fix(p)
        total += n
        print(f'{p}: 交换 {n} 处')
    print(f'合计 {total} 处')
