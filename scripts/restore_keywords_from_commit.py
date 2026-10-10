#!/usr/bin/env python3
"""按块序号从指定 commit 恢复关键词行（引语块被批量改成占位符后的回滚）。

用法：python3 scripts/restore_keywords_from_commit.py <书目录> <commit> [--dry]
"""
import glob
import os
import re
import subprocess
import sys


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    book, commit = sys.argv[1], sys.argv[2]
    dry = '--dry' in sys.argv

    for md in sorted(glob.glob(os.path.join(book, 'ch*.md'))):
        rel = md
        old = subprocess.run(['git', 'show', f'{commit}:{rel}'],
                             capture_output=True, text=True,
                             cwd='/Users/jcxs2014/Documents/Works/EnglishRead')
        if old.returncode != 0:
            print(f'⚠ 无旧版 {os.path.basename(md)}')
            continue

        def kw_lines(text):
            return re.findall(r'\*\*关键词\*\*[：:][：:]?\s*(.+)', text)

        old_kw = kw_lines(old.stdout)
        cur = open(md, encoding='utf-8').read()
        new_kw = kw_lines(cur)

        if len(old_kw) != len(new_kw):
            print(f'⚠ {os.path.basename(md)}: 块数不一致 旧{len(old_kw)} vs 新{len(new_kw)}，跳过')
            continue

        # 只把占位符行按序换回旧内容
        idx = [0]
        placeholder = re.compile(r'\*\*关键词\*\*[：:][：:]?\s*（待补充）')

        def repl(m):
            i = idx[0]
            idx[0] += 1
            if i < len(old_kw) and old_kw[i].strip() != '（待补充）':
                return '**关键词**：' + old_kw[i].strip()
            return m.group(0)

        new = placeholder.sub(repl, cur)
        if new != cur:
            if not dry:
                open(md, 'w', encoding='utf-8').write(new)
            n = sum(1 for m in placeholder.finditer(cur))
            print(f'✓ {os.path.basename(md)}: 可恢复 {n} 行')


if __name__ == '__main__':
    main()
