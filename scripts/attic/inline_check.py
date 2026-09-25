#!/usr/bin/env python3
"""总览短引语 + 行内英文片段兜底（verify_overview_quotes 与 overview_check 的补盲区）"""
import re, os, sys, glob, unicodedata

flat = lambda s: re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).lower())
book = sys.argv[1]
corp = {}
for f in glob.glob(os.path.join(book, 'text', 'ch*.txt')):
    nn = int(re.match(r'ch(\d+)', os.path.basename(f)).group(1))
    corp[nn] = flat(open(f, encoding='utf-8').read())
allflat = ''.join(corp.values())

SPAN = re.compile(r'[""“]([^""”\n]{4,})[""”]')
miss = 0
short = 0
zh = 0
print("=== 行内引号内容逐条核对（≥4 字符，英文为主）===")
for fn in ('00_概述.md', '00_金句精选.md', '00_情感节点.md'):
    p = os.path.join(book, fn)
    if not os.path.exists(p):
        continue
    for i, line in enumerate(open(p, encoding='utf-8'), 1):
        for q in SPAN.findall(line):
            a = sum(1 for c in q if 'a' <= c.lower() <= 'z')
            # 英文引语 = ASCII 字母占比 ≥60%（中文译文里嵌专名会被误捕，见 ch 概述 L36/L72）
            if a < 8 or a / max(1, len(q)) < 0.60:
                # 中文内容（中文引号里的译文/书名）——非英文引语，跳过但单独计数
                if sum(1 for c in q if '一' <= c <= '鿿') >= 8:
                    zh += 1
                continue
            fq = flat(q)
            if fq in allflat:
                tag = 'OK  '
            else:
                tag = 'MISS'
                miss += 1
            if len(fq) < 20:
                tag += ' [短]'
                short += 1
            print(f"  {tag} {os.path.basename(fn)}:L{i}  {q[:70]}")
print(f"\n英文短引语 {short} 条（均已 flat 命中全书，报告留档），中文引号内容 {zh} 处（译文/书名，非英文引语）")
print(f"MISS {miss} 条")
print('INLINE_CHECK ' + ('PASS' if miss == 0 else 'FAIL'))
sys.exit(1 if miss else 0)
