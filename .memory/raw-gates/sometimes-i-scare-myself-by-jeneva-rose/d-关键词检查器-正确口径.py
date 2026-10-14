import os, re, glob, sys

book_dir = sys.argv[1] if len(sys.argv) > 1 else "notes/books/novels/sometimes-i-scare-myself-by-jeneva-rose"
issues = []
checked = 0
blocks_found = 0

for md_path in sorted(glob.glob(f"{book_dir}/ch*.md")):
    with open(md_path, encoding='utf-8') as f:
        lines = f.read().split('\n')

    for i, line in enumerate(lines):
        m = re.match(r'^> \*\*原句 (\d+):\*\*(.*)$', line)
        if not m:
            continue
        blocks_found += 1
        block_no = m.group(1)

        # 完整引语：本行剩余 + 后续非空非 `**` 行
        quote_line = m.group(2)
        j = i + 1
        while j < len(lines) and lines[j].strip() and not lines[j].lstrip().startswith('**') and not lines[j].lstrip().startswith('>'):
            quote_line += ' ' + lines[j]
            j += 1

        # 向后找本块的关键词行（遇下一个原句即停）
        kw_text = None
        for k in range(i + 1, min(i + 25, len(lines))):
            if re.match(r'^> \*\*原句', lines[k]):
                break
            km = re.match(r'^\*\*关键词\*\*[:：](.+)$', lines[k])
            if km:
                kw_text = km.group(1).strip()
                break

        if not kw_text:
            continue
        checked += 1

        q_l = quote_line.lower()
        for kw in [x.strip() for x in kw_text.split(',') if x.strip()]:
            kw_l = kw.lower()
            if kw_l in q_l:
                continue
            # 词形变化：去后缀还原词根
            roots = [kw_l]
            for suf in ('ed', 'ing', 'es', 's', 'ly', 'd'):
                if kw_l.endswith(suf) and len(kw_l) > len(suf) + 2:
                    stem = kw_l[:-len(suf)]
                    roots += [stem, stem + 'e', stem + 'ed']
            if any(len(r) >= 3 and r in q_l for r in roots):
                continue
            # 多词短语：逐词都出现即算命中
            if ' ' in kw_l:
                words = [w.strip(".,'\"") for w in kw_l.split()]
                if all((w in q_l) or len(w) < 4 for w in words):
                    continue
            issues.append(f"{os.path.basename(md_path)} 块{block_no}: 「{kw}」  ← 引语: {quote_line[:90]}")

print(f"扫描 {blocks_found} 个引语块，检查 {checked} 个有词表的块")
if issues:
    print(f"\n真缺陷 {len(issues)} 个：")
    for x in issues:
        print(f"  {x}")
else:
    print("关键词层：0 缺陷")
