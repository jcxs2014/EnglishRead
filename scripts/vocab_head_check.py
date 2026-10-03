#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""词头逐字核验：md 词表**词头**是否真在本章 text/ 里。

为什么需要（2026-10-03 Evie 批次实测）：
  check_vocab.py 查词头词频、evie_vocab_cells_check.py 查例句连续子串，
  两者都**抓不到**「词头不在本章、但例句抄自本章真实句子」这一类 A 类虚构——
  实证 ch06 的 `exemplifies`：例句逐字正确，词头全书 0 次。
  本脚本补上这一半：按词头逐个做带词界的 norm+lookaround 命中。

用法：
  python3 scripts/vocab_head_check.py "<书目录>" [chNN ...]
  python3 scripts/vocab_head_check.py "<单个 md 文件>" "<本章 text 文件>"

退出码：0 = 全部命中；1 = 有词头查无（阻断型）。
"""
import argparse, glob, os, re, sys

ROW = re.compile(r'^\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*$')
SEP = re.compile(r'^\s*\|[\s:|-]+\|\s*$')


def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()


def has_token(corpus_n, token):
    """词界命中：只接受独立词或带连字符的整串，禁 'exemplifies' 命中 'exemplify'。"""
    t = norm(token)
    if not t or not re.search(r'[a-z]', t):
        return True, '非拉丁词头，跳过'
    pat = r'(?<![a-z0-9])' + re.escape(t).replace(r'\ ', r'[ \t]+') + r'(?![a-z0-9])'
    m = re.search(pat, corpus_n)
    return (bool(m), m.group(0) if m else '')


def rows_of(md_text):
    """只取三列表格数据行；表头与分隔线跳过。"""
    out = []
    for line in md_text.split('\n'):
        if SEP.match(line):
            continue
        m = ROW.match(line)
        if not m:
            continue
        head, gloss, ex = m.group(1), m.group(2), m.group(3)
        if head in ('词/短语', '词', 'word') or set(head) <= set('-: '):
            continue
        if '释义' in gloss and '例句' in ex:
            continue
        out.append((head, gloss, ex))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('target')
    ap.add_argument('rest', nargs='*')
    args = ap.parse_args()

    jobs = []
    if args.rest:                      # 单文件模式
        jobs.append((args.target, args.rest[0]))
    else:                              # 书目录模式
        for f in sorted(glob.glob(os.path.join(args.target, 'ch*.md'))):
            m = re.search(r'ch(\d+)([a-z]?)', os.path.basename(f))
            if not m:
                continue
            cand = glob.glob(os.path.join(args.target, 'text', 'ch%s%s_*.txt'
                                          % (m.group(1), m.group(2))))
            if cand:
                jobs.append((f, cand[0]))

    total = miss = skip = 0
    for md, txt in jobs:
        heads = rows_of(open(md, encoding='utf-8').read())
        if not heads:
            continue
        corpus_n = ' ' + norm(open(txt, encoding='utf-8').read()) + ' '
        bad = []
        for head, _g, _e in heads:
            ok, why = has_token(corpus_n, head)
            total += 1
            if why.startswith('非拉丁'):
                skip += 1
                continue
            if not ok:
                miss += 1
                bad.append(head)
        if bad:
            print('❌ %s（词头查无 %d）：%s' % (os.path.basename(md), len(bad),
                                              ' · '.join(bad[:12])))
        else:
            print('✅ %s：词头 %d 条全部命中本章' % (os.path.basename(md), len(heads)))
    print('--- 词头合计 %d 条｜查无 %d ｜跳过非拉丁 %d ---' % (total, miss, skip))
    return 1 if miss else 0


if __name__ == '__main__':
    sys.exit(main())
