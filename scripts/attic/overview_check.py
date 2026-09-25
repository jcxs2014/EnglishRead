#!/usr/bin/env python3
"""
overview_check.py — 总览三篇（00_*.md）自检
  A) 引语全串 flat 比对 text/（verify_overview_quotes 不覆盖的行内引语也查）
  B) 章节标签对账：引语 flat 命中**它所标注的那一章**
  C) 跨章多重命中检测
  D) 短引语（<20 flat）列出，须人工 grep
  E) 总览 H1 语义校验
用法：python3 scripts/attic/overview_check.py "<书目录>"
"""
import re, os, sys, glob, unicodedata

flat = lambda s: re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).lower())
book = sys.argv[1]

corp = {}
for f in glob.glob(os.path.join(book, 'text', 'ch*.txt')):
    nn = int(re.match(r'ch(\d+)', os.path.basename(f)).group(1))
    corp[nn] = flat(open(f, encoding='utf-8').read())

QUOTE = re.compile(r'[""“]([^""”\n]{12,})[""”]')
SRC = re.compile(r'-\s*\*\*出处\*\*[：:]\s*ch(\d\d)')


def looks_english(s):
    """只把以英文为主的引号内容当引语，避免中文顿号/引号误判。"""
    a = sum(1 for c in s if 'a' <= c.lower() <= 'z')
    return a >= 25 and a / max(1, len(s)) > 0.55


files = {
    '金句': os.path.join(book, '00_金句精选.md'),
    '节点': os.path.join(book, '00_情感节点.md'),
    '概述': os.path.join(book, '00_概述.md'),
}

miss_total = label_bad = 0
cross = {}
print("=== A/B/C 引语全串核对 + 章节标签对账 ===")
for tag, path in files.items():
    if not os.path.exists(path):
        print(f"  ✗ 缺文件 {path}")
        miss_total += 1
        continue
    lines = open(path, encoding='utf-8').read().split('\n')
    n_ok = 0
    for i, line in enumerate(lines, 1):
        # 归属标签优先级：① 同行内、出现在引语之前的 chNN / 第 N 章 回指
        #                 ② 否则取其后 9 行内本块的「出处」
        #                 （否则会把「呼应」行的回指错配到下一块的出处）
        nn = None
        inline = list(re.finditer(r'(?:ch(\d\d)|第\s*(\d+)\s*章)', line))
        before = [m for m in inline if m.start() < min(
            (qm.start() for qm in QUOTE.finditer(line) if looks_english(qm.group(1))),
            default=len(line))]
        if before:
            m = before[-1]
            nn = int(m.group(1)) if m.group(1) else int(m.group(2)) + 1
        else:
            for j in range(i, min(len(lines), i + 9)):
                m = SRC.search(lines[j])
                if m:
                    nn = int(m.group(1))
                    break
        for q in QUOTE.findall(line):
            if not looks_english(q):
                continue
            fq = flat(q)
            if len(fq) < 20:
                continue
            hits = [n for n, c in corp.items() if fq in c]
            if not hits:
                print(f"  ✗ MISS {os.path.basename(path)}:L{i}  {q[:70]}")
                miss_total += 1
                continue
            n_ok += 1
            if nn is not None and nn not in hits:
                print(f"  ✗ LABEL {os.path.basename(path)}:L{i} 标注 ch{nn:02d}，实际命中 ch{hits}")
                label_bad += 1
            if len(hits) > 1:
                cross.setdefault(fq, hits)
    print(f"  {tag}：长引语全串命中 {n_ok}")
print(f"  汇总：全串 MISS {miss_total}，章节标签错位 {label_bad}")

print("=== D 短引语（<20 flat，须人工 grep）===")
sh = 0
for tag, path in files.items():
    if not os.path.exists(path):
        continue
    for i, line in enumerate(open(path, encoding='utf-8'), 1):
        for q in QUOTE.findall(line):
            if looks_english(q) and 5 <= len(flat(q)) < 20:
                sh += 1
                print(f"  ⚠ {os.path.basename(path)}:L{i}  {q}")
print(f"  短引语合计 {sh}")

print("=== E 总览 H1 语义校验 ===")
expect = {'00_概述.md': '概述', '00_金句精选.md': '金句', '00_情感节点.md': '情感节点'}
h1_bad = 0
for fn, kw in expect.items():
    p = os.path.join(book, fn)
    if not os.path.exists(p):
        continue
    h1 = ''
    for line in open(p, encoding='utf-8'):
        if line.startswith('# '):
            h1 = line.strip()
            break
    ok = kw in h1
    if not ok:
        h1_bad += 1
    print(f"  {fn}  H1 = {h1}  {'PASS' if ok else 'FAIL'}")
print(f"  H1 问题 {h1_bad}")

if cross:
    print("=== C 跨章多重命中（需人工确认归属）===")
    for fq, hits in cross.items():
        print(f"  ⚠ 命中 {hits}  {fq[:60]}")

errs = miss_total + label_bad + h1_bad
print(f"\n总览 errors={errs}（MISS {miss_total} / 标签 {label_bad} / H1 {h1_bad}）")
print('OVERVIEW_CHECK ' + ('PASS' if errs == 0 else 'FAIL'))
sys.exit(1 if errs else 0)
