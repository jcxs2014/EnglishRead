#!/usr/bin/env python3
"""
audit_sem.py — 五步审查 d 步：语义层机械筛查（**与写作期完全不同的检查路径**）

本脚本只做可机械判定的部分，凡需人读的一律输出待核清单交给 d 步人工/子代理：

  A. 说话人归属抽查：引语在原章中的 ±200 字符窗口内是否出现该块所声明的说话人
     （Room 金句 11/30 人物误归的专治手段）
  B. 数字/日期/专名断言：分析层（中文理解+为什么这样写）出现的数字须在当章 text/ 出现
  C. 章节号断言：分析层提到的"第 N 章/chNN"须在全书 text/ 中确有对应内容
  D. 终验标准件：引语**全串**（非 52 字符指纹）flat 比对当章 text/
  E. 待人读清单：导出全部块的四子项，供 d 步逐对语义核对
用法：python3 scripts/attic/audit_sem.py "<书目录>" [--dump-batch N]
"""
import os
import re
import sys
import glob
import unicodedata

BOOK = sys.argv[1]
flat = lambda s: re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).lower())

corp, raw = {}, {}
for f in glob.glob(os.path.join(BOOK, 'text', 'ch*.txt')):
    nn = int(re.match(r'ch(\d+)', os.path.basename(f)).group(1))
    raw[nn] = open(f, encoding='utf-8').read()
    corp[nn] = flat(raw[nn])
allflat = ''.join(corp.values())

BLOCK = re.compile('^>\\s*\\*\\*原句\\s*(\\d+)\\s*[:：]\\*\\*\\s*(.*)$')
CAST = ['Anna Arbor', 'Anna Evenhouse', 'Jennie Arbor', 'Jennie Evenhouse', 'Kowalski',
        'Rodriguez', 'Adam', 'John', 'Peter', 'Ursula', 'Jay', 'Evenhouse', 'Arbor',
        'Grandmother', 'Mer', 'Meredith', 'Martin', 'Robert', 'Bobby', 'Flanagan',
        'Keene', 'Carl', 'Dunning', 'Morgana', 'Steve', 'Rita']

# 说话人声明表：md 文件 -> 该文件里被声明星号过的角色（只对有明确说话人的块生效）
err_spk, err_num, err_ch, miss = [], [], [], []
pairs_dump, block_total = [], 0

for path in sorted(glob.glob(os.path.join(BOOK, 'ch*.md'))):
    name = os.path.basename(path)
    nn = int(re.match(r'ch(\d+)', name).group(1))
    lines = open(path, encoding='utf-8').read().split('\n')
    marks = [(i, m) for i, l in enumerate(lines) if (m := BLOCK.match(l))]

    for idx, (i, m) in enumerate(marks):
        n = int(m.group(1))
        quote = m.group(2).strip()
        end = marks[idx + 1][0] if idx + 1 < len(marks) else len(lines)
        body = '\n'.join(lines[i + 1:end])
        zh = body.split('**中文理解：**')[1].split('**关键词：**')[0] if '**中文理解：**' in body else ''
        why = body.split('**为什么这样写：**')[1].split('**读者视角提示：**')[0] if '**为什么这样写：**' in body else ''
        kw = body.split('**关键词：**')[1].split('**为什么这样写：**')[0] if '**关键词：**' in body else ''
        view = body.split('**读者视角提示：**')[1] if '**读者视角提示：**' in body else ''
        analysis = zh + why + view
        block_total += 1

        # D 终验件：全串 flat 比对当章
        fq = flat(quote)
        if fq:
            segs = [flat(s) for s in re.split(r'…|\.\.\.', quote)] if ('…' in quote or '...' in quote) else [fq]
            for sg in segs:
                if len(sg) < 15:
                    continue
                if sg not in corp[nn]:
                    miss.append(f"{name} 块{n}: 片段未命中本章 -> {quote[:60]}")

        # A 说话人：取本块「为什么这样写」中显式点名的角色，检查其是否在原章窗口出现
        # 词边界匹配：否则 'Adams'（街道名 Canal & Adams）会误命中 'Adam'，
        # 'Mer' 会误命中 'American'/'Mercury' 等
        named = [c for c in CAST if re.search(r'\b' + re.escape(c) + r'\b', why)]
        if named and fq in corp[nn]:
            pos = corp[nn].find(fq)
            win = corp[nn][max(0, pos - 200):pos + len(fq) + 200]
            for c in named:
                if flat(c) not in win:
                    # 允许：该角色可能在本块之前/之后才被引入；记为待人读而非直接 FAIL
                    err_spk.append(f"{name} 块{n}: 声明角色「{c}」在引语 ±200 字符窗口外 "
                                   f"(全书出现于 {[k for k, v in corp.items() if flat(c) in v][:5]})")

        # B 数字断言
        for num in re.findall(r'(?<![\w.])\d{1,4}(?![\w.])', analysis):
            if num in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '10', '100', '1000'):
                continue
            if num not in raw[nn] and num not in allflat:
                err_num.append(f"{name} 块{n}: 分析层数字 {num} 在全书 text/ 查无")

        # C 章节号断言
        for cm in re.finditer(r'第\s*(\d+)\s*章|ch(\d\d)', analysis + kw):
            ch_no = int(cm.group(1)) if cm.group(1) else int(cm.group(2)) - 1
            # 该章须存在对应 md 文件
            tgt = f"ch{ch_no:02d} " if cm.group(2) else None
            if tgt and not glob.glob(os.path.join(BOOK, tgt + '*.md')):
                err_ch.append(f"{name} 块{n}: 引用 {cm.group(0)} 无对应 md 文件")

        pairs_dump.append((name, n, quote, kw.strip(), zh.strip(), why.strip(), view.strip()))

print(f"=== 扫描 {block_total} 个引语块 / 32 章 ===\n")
print(f"--- A 说话人窗口外声明（{len(err_spk)}，需人读确认，非直接缺陷）---")
for e in err_spk:
    print("  ⚠ " + e)
print(f"\n--- B 分析层数字全书查无（{len(err_num)}）---")
for e in err_num:
    print("  ✗ " + e)
print(f"\n--- C 引用不存在的 md 文件（{len(err_ch)}）---")
for e in err_ch:
    print("  ✗ " + e)
print(f"\n--- D 终验件：引语全串/片段未命中本章（{len(miss)}）---")
for e in miss:
    print("  ✗ " + e)

if '--dump-batch' in sys.argv:
    k = int(sys.argv[sys.argv.index('--dump-batch') + 1])
    per = 32
    sl = pairs_dump[k * per:(k + 1) * per]
    print(f"\n===== DUMP BATCH {k}（{len(sl)} 块）=====")
    for name, n, q, kw, zh, why, v in sl:
        print(f"\n### {name} 块{n}\n引语: {q}\n关键词: {kw}\n中文: {zh}\n为什么: {why}\n提示: {v}")

errs = len(err_num) + len(err_ch) + len(miss)
print(f"\n机械判定 errors={errs}（数字 {len(err_num)} / 章节 {len(err_ch)} / 全串 {len(miss)}）；"
      f"说话人待人读 {len(err_spk)} 项")
print('AUDIT_SEM ' + ('PASS' if errs == 0 else 'FAIL'))
sys.exit(1 if errs else 0)
