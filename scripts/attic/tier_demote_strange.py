#!/usr/bin/env python3
"""
tier_demote_strange.py — 把「分档注水」的词条从 ⭐⭐⭐ 高级档降到 ⭐⭐ 进阶档

背景：AGENTS.md 规则「分档不许注水：常见词混入 ⭐⭐⭐ 高级档视为不合格」。
check_vocab 只用 ~200 高频词表判 WARN，覆盖不到 B1/B2 级常见词，故需人工降档。
本脚本纯行级作用域（不跨块），把指定词条行从高级表移到进阶表末尾。

用法：
  python3 scripts/attic/tier_demote_strange.py <md> <word1,word2,...>
"""
import sys, re

def demote(path, words):
    lines = open(path, encoding='utf-8').read().split('\n')
    try:
        i_adv = next(i for i, l in enumerate(lines) if re.match(r'^### ⭐⭐⭐', l))
        i_int = next(i for i, l in enumerate(lines) if re.match(r'^### ⭐⭐ 进阶', l))
        i_bas = next(i for i, l in enumerate(lines) if re.match(r'^### ⭐ 基础', l))
    except StopIteration:
        return 0
    moved = []
    for w in words:
        pat = re.compile(r'^\| ' + re.escape(w) + r' \|')
        idx = next((i for i in range(i_adv, i_int) if pat.match(lines[i])), None)
        if idx is None:
            print(f'  ! 未在高级档找到: {w}'); continue
        moved.append(lines.pop(idx))
        # 索引因 pop 变化，重新计算进阶表末尾
        i_bas = next(i for i, l in enumerate(lines) if re.match(r'^### ⭐ 基础', l))
        insert_at = i_bas - 1
        while insert_at > 0 and lines[insert_at - 1].strip() == '':
            insert_at -= 1
        lines.insert(insert_at, moved[-1])
    if moved:
        open(path, 'w', encoding='utf-8').write('\n'.join(lines))
    return len(moved)

if __name__ == '__main__':
    n = demote(sys.argv[1], sys.argv[2].split(','))
    print(f'{sys.argv[1]}: 降档 {n} 条')
