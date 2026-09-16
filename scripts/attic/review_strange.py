#!/usr/bin/env python3
"""
review_strange.py — Strange Is the Light 自建审查标准件（逐章结构 + 引语全文连续 sweep + 关键词锚定）

三合一，针对精简格式（`> **原句 N:** "..."` + 四子项：中文理解/关键词/为什么这样写/读者视角提示）：

  a. 结构扫描：编号是否从 1 连续、每块四子项是否齐全且顺序正确、零孤儿块、零重复块
  b. 引语全文 sweep：**整条引语**（非 verify_quotes 的前 52 字符指纹）flat 比对本章 text，
     省略号分段时逐段比对 —— 抓跨标签拼接 / 后半句虚构 / 末尾 gilding
  c. 关键词锚定：块内「关键词」的英文词必须命中该块引语（允许词形变化），
     否则必须在「为什么这样写」正文里出现（语境延伸词须有呼应）

用法：
  python3 scripts/attic/review_strange.py "<书目录>" [chNN ...]
"""
import re, sys, os, glob, unicodedata

flat = lambda s: re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).lower())
QUOTE_RE = re.compile(r'^>\s*\*\*原句\s*(\d+)[:：]\*\*\s*(.*)$')
FIELD_RE = re.compile(r'^\*\*(中文理解|关键词|为什么这样写|读者视角提示)[:：]\*\*')
ORDER = ['中文理解', '关键词', '为什么这样写', '读者视角提示']
STOP = set("""the a an of in on to and or but for with is are was were be been being it its this that these those
as at by from into over under then than so not no all any very s t d ll ve re m""".split())


def load_chapter_text(book_dir, nn, cache={}):
    if nn not in cache:
        cands = glob.glob(os.path.join(book_dir, 'text', f'ch{nn:02d}_*.txt')) + \
                glob.glob(os.path.join(book_dir, 'text', f'ch{nn:02d}.txt'))
        cache[nn] = flat(open(cands[0], encoding='utf-8').read()) if cands else ''
    return cache[nn]


def word_in(word, *haystacks):
    """关键词须命中引语，或（语境延伸词）命中「为什么这样写」正文。允许词形变化。"""
    w = flat(word)
    if len(w) < 3:
        return True          # 过短（如 it / be）不参与锚定
    if w.endswith('ing'):
        stems = {w, w[:-3], w[:-3] + 'e'}
    elif w.endswith('ed'):
        stems = {w, w[:-2], w[:-1]}
    else:
        stems = {w, w.rstrip('s'), w + 's', w + 'ed', w + 'ing'}
    return any(len(s) >= 3 and any(s in h for h in haystacks) for s in stems)


def check_file(path, book_dir):
    nn = int(re.match(r'ch(\d+)', os.path.basename(path)).group(1))
    corpus = load_chapter_text(book_dir, nn)
    lines = open(path, encoding='utf-8').read().splitlines()

    blocks, cur = [], None
    for i, raw in enumerate(lines, 1):
        s = raw.rstrip()
        m = QUOTE_RE.match(s)
        if m:
            cur = {'no': int(m.group(1)), 'line': i, 'quote': m.group(2).strip().strip('*').strip(),
                   'fields': {}, 'last': None}
            blocks.append(cur)
            continue
        fm = FIELD_RE.match(s)
        if fm and cur is not None:
            cur['last'] = (fm.group(1), i)
            cur['fields'].setdefault(fm.group(1), s)

    problems = []
    # a. structure
    nums = [b['no'] for b in blocks]
    if nums != list(range(1, len(blocks) + 1)):
        problems.append(f'编号不连续: {nums}')
    seen = {}
    for b in blocks:
        if b['quote'] in seen:
            problems.append(f"重复块 原句{b['no']} 与 原句{seen[b['quote']]} 引语相同")
        seen[b['quote']] = b['no']
        # field order & presence
        seq = []
        for j, raw in enumerate(lines[b['line']:], b['line'] + 1):
            fm = FIELD_RE.match(raw.rstrip())
            if fm:
                seq.append(fm.group(1))
            if QUOTE_RE.match(raw.rstrip()):
                break
        if seq != ORDER:
            problems.append(f"原句{b['no']} 四子项顺序/缺失: {seq}")

    # b. full-quote sweep + c. keyword anchoring
    for b in blocks:
        q = b['quote'].strip('"“”\'‘’ ')
        fq = flat(q)
        if not fq:
            continue
        segs = [p for p in re.split(r'…|\.\.\.', q) if len(flat(p)) >= 12]
        if segs:
            bad = [p[:50] for p in segs if flat(p) not in corpus]
        else:
            bad = [] if fq in corpus else [q[:70]]
        if bad:
            problems.append(f"原句{b['no']} 引语未连续命中本章 text: {bad}")

        kw_line = b['fields'].get('关键词', '')
        why = b['fields'].get('为什么这样写', '')
        why_flat = flat(why)
        kws = [w for w in re.findall(r"[A-Za-z]+(?:['’][A-Za-z]+)?", kw_line)]
        kws = [w for w in kws if flat(w) not in STOP]
        miss = [w for w in kws if not word_in(w, fq, why_flat)]
        if miss:
            problems.append(f"原句{b['no']} 关键词未锚定: {miss}")
    return nn, blocks, problems


def main():
    book_dir = sys.argv[1]
    only = [int(x) for x in sys.argv[2:]] or None
    files = sorted(glob.glob(os.path.join(book_dir, 'ch*.md')),
                   key=lambda p: int(re.match(r'ch(\d+)', os.path.basename(p)).group(1)))
    tb = tp = 0
    bad_files = 0
    for f in files:
        nn = int(re.match(r'ch(\d+)', os.path.basename(f)).group(1))
        if only and nn not in only:
            continue
        nn, blocks, problems = check_file(f, book_dir)
        tb += len(blocks)
        tp += len(problems)
        if problems:
            bad_files += 1
            print(f'{os.path.basename(f)}: {len(blocks)} 块, {len(problems)} 问题')
            for p in problems:
                print(f'    ✗ {p}')
        else:
            print(f'{os.path.basename(f)}: {len(blocks)} 块 ✅')
    print(f'\n=== 合计 {tb} 块 / {tp} 问题 / 异常文件 {bad_files} ===')
    sys.exit(1 if tp else 0)


if __name__ == '__main__':
    main()
