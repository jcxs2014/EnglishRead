#!/usr/bin/env python3
"""
check_crossref.py — 分析层交叉引用校验器

背景：verify_quotes/check_chapter_quotes/check_vocab 三道门禁都不管
"分析文字里 chNN '引语'" 是否指对章。Forest of Scars 审查 21 处缺陷中
16 处源于此（分析层 cross-ref 章号错/说话人错），Life and Death and
Giants 亦有 10 处同类——凭印象写 cross-ref = 凭记忆引语。

用法：
  python3 scripts/check_crossref.py "<书目录>" [--verbose]

原理：
  1. 扫描所有 ch*.md 的非引语行（分析/导航/总结层）；
  2. 正则抓 `chNN "quoted"` / `chNN "…quoted…"` 对（兼容中文引导的引用）；
  3. flat 比对引语片段是否存在于所指章的 text/chNN*.txt；
  4. 未命中 → 报警（附文件/行号/上下文，供人工读行复核——同行多引用
     会误配，报警不等于缺陷）。

局限（须人工复核的原因）：
  - 同一行多个 chNN 引用会与最近的引语错误配对；
  - 章内跨章叙事（如 "ch54 讲的手术" 无引语）不覆盖；
  - 中文理解/关键词子项内的合法引用同源，需人工判断。

Exit 0 = 零报警；Exit 1 = 有待人工复核的报警。
"""
import re, sys, os, glob, unicodedata

flat = lambda s: re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).lower())

# chNN + 引语（中英文引号均可，允许省略号）
XREF_RE = re.compile(
    r'ch(\d{1,3})\s*[「"“]([^」"”]{12,200})[」"”]'
)

def load_corpora(book_dir):
    corpora = {}
    for f in glob.glob(os.path.join(book_dir, 'text', 'ch*.txt')):
        m = re.match(r'ch(\d+)', os.path.basename(f))
        if m:
            corpora.setdefault(int(m.group(1)), []).append(flat(open(f, encoding='utf-8', errors='ignore').read()))
    return corpora

def main(book_dir, verbose=False):
    corpora = load_corpora(book_dir)
    if not corpora:
        raise SystemExit(f'no text/ch*.txt under {book_dir}/text')
    alerts = []
    checked = 0
    for f in sorted(glob.glob(os.path.join(book_dir, 'ch*.md'))):
        name = os.path.basename(f)
        if name.startswith('00_'):
            continue
        for lineno, line in enumerate(open(f, encoding='utf-8'), 1):
            s = line.strip()
            if s.startswith('> '):          # 引语行本身不在分析层口径
                continue
            for m in XREF_RE.finditer(s):
                nn = int(m.group(1))
                quoted = m.group(2)
                fp = flat(quoted)
                # 省略号分段：两侧都须命中所指章
                segs = [p for p in re.split(r'…|\.\.\.', quoted)
                        if len(flat(p)) >= 15]
                pieces = segs if segs else [quoted]
                checked += 1
                corp_list = corpora.get(nn, [])
                ok = any(all(fp[:40] in c or flat(p)[:40] in c for p in pieces) for c in corp_list)
                if not ok:
                    alerts.append((name, lineno, nn, quoted[:70], s[:110]))
    print(f'交叉引用核对：{checked} 对，报警 {len(alerts)}')
    for name, lineno, nn, quoted, ctx in alerts:
        print(f'  ⚠️ {name}:{lineno} → ch{nn:02d} 查无「{quoted}…」')
        if verbose:
            print(f'      行：{ctx}')
    if alerts:
        print(f'\n⚠️ 报警须人工读行复核（同行多引用会误配）；确认后再判缺陷')
    sys.exit(1 if alerts else 0)

if __name__ == '__main__':
    main(sys.argv[1], '--verbose' in sys.argv)
