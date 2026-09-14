#!/usr/bin/env python3
"""Daggerbound 独立审查标准件（五步法 c/d 两项）：
 1) 结构扫描：引语块编号连续 / 四子项齐全且顺序正确 / 零孤儿块 / 零重复块
 2) 关键词锚定：块内"关键词"行的英文词须命中该块引语（允许词形变化）
 3) 整行连续 sweep：引语整行须在某章 text/ 中连续命中（防跨段拼接）

用法：python3 scripts/attic/review_daggerbound.py <书目录>
"""
import re, sys, os, glob, unicodedata

STOP = set("""a an the and or but if in on at to of for with as is are was were be been being
that this these those it its he she they them his her their you your i me my we our not no
do does did done have has had will would can could shall should may might must from by than then
there here what which who whom when where how all any both each few more most other some such
only own same so too very just also into over under out up down off about after before again""".split())


def flat(s):
    s = unicodedata.normalize('NFKD', s)
    return re.sub(r'[^a-z0-9]', '', s.lower())


def stem_forms(w):
    out = {w}
    if w.endswith('s'):
        out.add(w[:-1])
    if w.endswith('ing'):
        out.add(w[:-3]); out.add(w[:-3] + 'e')
    if w.endswith('ed'):
        out.add(w[:-2]); out.add(w[:-1])
    if w.endswith('ly'):
        out.add(w[:-2])
    if w.endswith('ies'):
        out.add(w[:-3] + 'y')
    return out


def main(book_dir):
    text_dir = os.path.join(book_dir, 'text')
    corpora = {}
    for f in glob.glob(os.path.join(text_dir, 'ch*.txt')):
        m = re.match(r'ch(\d+)', os.path.basename(f))
        if m:
            corpora[int(m.group(1))] = flat(open(f, encoding='utf-8', errors='ignore').read())

    struct_bad, kw_bad, sweep_bad = [], [], []
    total_blocks = 0
    for path in sorted(glob.glob(os.path.join(book_dir, 'ch*.md'))):
        name = os.path.basename(path)
        nn = int(re.match(r'ch(\d+)', name).group(1))
        corpus = corpora.get(nn, '')
        txt = open(path, encoding='utf-8').read()
        blocks = re.split(r'(?=^> \*\*原句)', txt, flags=re.M)
        nums = []
        seen = set()
        for b in blocks:
            m = re.match(r'^> \*\*原句 (\d+):\*\* (.+)$', b.split('\n')[0])
            if not m:
                continue
            total_blocks += 1
            num, quote = int(m.group(1)), m.group(2).strip()
            nums.append(num)
            if quote in seen:
                struct_bad.append(f'{name} 原句{num} 重复块')
            seen.add(quote)
            items = [x.group(0).strip('*：') for x in
                     re.finditer(r'^\*\*(中文理解|关键词|为什么这样写|读者视角提示)：\*\*', b, re.M)]
            if items != ['中文理解', '关键词', '为什么这样写', '读者视角提示']:
                struct_bad.append(f'{name} 原句{num} 子项异常 {items}')
            # 关键词锚定
            km = re.search(r'^\*\*关键词：\*\* (.+)$', b, re.M)
            qf = flat(quote)
            if km:
                for phrase in [p.strip() for p in km.group(1).split(',')]:
                    if not phrase:
                        continue
                    for w in re.findall(r"[A-Za-z]+", phrase):
                        wl = w.lower()
                        if wl in STOP or len(wl) < 3:
                            continue
                        if not any(f in qf for f in stem_forms(wl)):
                            kw_bad.append(f'{name} 原句{num} 「{phrase}」')
                            break
            # 整行连续 sweep（省略号分段：每段都须连续命中本章）
            segs = [s for s in re.split(r'…|\.\.\.', quote) if len(flat(s)) >= 12] or [quote]
            for s in segs:
                if flat(s)[:60] not in corpus:
                    sweep_bad.append(f'{name} 原句{num} 「{s[:70]}」')
        if nums and nums != list(range(1, len(nums) + 1)):
            struct_bad.append(f'{name} 编号不连续 {nums}')

    print(f'引语块总数：{total_blocks}')
    print(f'\n--- 结构异常 ({len(struct_bad)}) ---')
    for x in struct_bad[:20]:
        print(' ', x)
    print(f'\n--- 关键词锚定违规 ({len(kw_bad)}) ---')
    for x in kw_bad[:30]:
        print(' ', x)
    print(f'\n--- 整行连续 sweep 未命中 ({len(sweep_bad)}) ---')
    for x in sweep_bad[:30]:
        print(' ', x)


if __name__ == '__main__':
    main(sys.argv[1])
