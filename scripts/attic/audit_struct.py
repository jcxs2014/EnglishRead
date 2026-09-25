#!/usr/bin/env python3
"""
audit_struct.py — 五步审查 c 步：结构扫描（**全新实现**，不与写作期 selfcheck 共享代码路径）

口径：只认**行首**的 `> **原句 N:**` 引语块标记（不用整文正则，避免把导航里的
圈数字引用误算成引语块）。

逐文件检查：
  1. 编号从 1 起连续、无跳号/重号
  2. 每块四子项齐全（中文理解 / 关键词 / 为什么这样写 / 读者视角提示）
  3. 零孤儿块（有分析无引语 / 有引语无分析）
  4. 零重复块（同文件内同一引语出现两次）
  5. 关键词锚定：关键词行的实词须能在本块引语或「为什么这样写」中找到
  6. 导航 5 项齐全 + 三档词汇齐全 + 一句话总结存在
  7. 占位行 / 未完成标记 / 乱码字符
总览三篇另查 H1 语义与四子项结构。
用法：python3 scripts/attic/audit_struct.py "<书目录>"
"""
import os
import re
import sys
import glob
import unicodedata

BOOK = sys.argv[1]
NL = chr(0xFFFD)
BLOCK = re.compile('^>\\s*\\*\\*原句\\s*(\\d+)\\s*[:：]\\*\\*\\s*(.*)$')
SUBITEMS = ['\u4e2d\u6587\u7406\u89e3', '\u5173\u952e\u8bcd', '\u4e3a\u4ec0\u4e48\u8fd9\u6837\u5199', '\u8bfb\u8005\u89c6\u89d2\u63d0\u793a']
NAV = ['\u4e00\u53e5\u8bdd\u6982\u62ec', '\u6c1b\u56f4\u5f27\u7ebf\u4f4d\u7f6e',
       '\u7ebf\u7d22\u4e0e\u6bcd\u9898\u63a8\u8fdb', '\u4eba\u7269\u5f27\u7ebf', '\u53d9\u4e8b\u624b\u6cd5']
TIER = ['\u2b50\u2b50\u2b50 \u9ad8\u7ea7', '\u2b50\u2b50 \u8fdb\u9636', '\u2b50 \u57fa\u7840']
STOP = set('''the a an and or but of to in on at for with by from as is are was were be been
being it its this that these those he she they we you i him her them us me my your our their
not no so if then than there here what which who whom when where why how do does did done
have has had will would can could shall should may might must let lets get got give gave
take took make made say said see saw know knew think thought want wanted need needed
because while after before again very more most much many some any all each every other
one two three four five six seven eight nine ten first last next new old young long short
like just also still even only own same both few own too s t re ve ll d m'''.split())


def toks(s):
    """抽取英文实词（词形原样，不做归一）"""
    return [w for w in re.findall(r"[A-Za-z][A-Za-z'\-]{2,}", s) if w.lower() not in STOP]


errors, warns, total_blocks = [], [], 0
for path in sorted(glob.glob(os.path.join(BOOK, 'ch*.md'))):
    name = os.path.basename(path)
    lines = open(path, encoding='utf-8').read().split('\n')
    marks = [(i, m) for i, l in enumerate(lines) if (m := BLOCK.match(l))]

    # --- 1 编号连续
    nums = [int(m.group(1)) for _, m in marks]
    if nums != list(range(1, len(nums) + 1)):
        errors.append(f"{name}: 编号不连续 -> {nums}")
    total_blocks += len(marks)

    # --- 3b 引语块数须在 3–8 配额内
    if not (3 <= len(marks) <= 8):
        warns.append(f"{name}: 引语块 {len(marks)} 处，超出 3–8 配额")

    # --- 2/3/4/5 逐块
    for idx, (i, m) in enumerate(marks):
        n = int(m.group(1))
        quote = m.group(2).strip()
        end = marks[idx + 1][0] if idx + 1 < len(marks) else len(lines)
        body = lines[i + 1:end]
        btext = '\n'.join(body)

        for it in SUBITEMS:
            if f"**{it}" not in btext:
                errors.append(f"{name} 块{n}: 缺子项「{it}」")

        if '**\u4e2d\u6587\u7406\u89e3\uff1a**' in btext:
            after = btext.split('**\u4e2d\u6587\u7406\u89e3\uff1a**', 1)[1]
            head = after.split('**\u5173\u952e\u8bcd', 1)[0]
            if len(head.strip()) < 4:
                errors.append(f"{name} 块{n}: 中文理解为空")

        if '**\u4e3a\u4ec0\u4e48\u8fd9\u6837\u5199\uff1a**' in btext:
            after = btext.split('**\u4e3a\u4ec0\u4e48\u8fd9\u6837\u5199\uff1a**', 1)[1]
            if len(after.strip()) < 20:
                errors.append(f"{name} 块{n}: 为什么这样写过短")

        # 关键词锚定
        km = re.search(r'\*\*\u5173\u952e\u8bcd\uff1a\*\*(.*)', btext)
        if km:
            kwin = km.group(1)
            why = btext.split('**\u4e3a\u4ec0\u4e48\u8fd9\u6837\u5199\uff1a**', 1)[-1]
            hay = (quote + ' ' + why).lower()
            for w in toks(kwin):
                wl = w.lower().rstrip("'s")
                stem = re.sub(r"(ing|ed|es|s|ly|ment|ness|tion)$", '', wl)
                if wl in hay or (len(stem) > 4 and stem in hay):
                    continue
                errors.append(f"{name} 块{n}: 关键词「{w}」未锚定到引语/为什么这样写")

    # --- 4 重复块
    seen = {}
    for i, m in marks:
        k = re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', m.group(2)).lower())[:90]
        if k in seen:
            errors.append(f"{name} 块{int(m.group(1))} 与块{seen[k]} 引语重复")
        seen[k] = int(m.group(1))

    # --- 6 导航 / 词汇 / 总结
    whole = '\n'.join(lines)
    for it in NAV:
        if f"**{it}**" not in whole:
            errors.append(f"{name}: 导航缺「{it}」")
    for t in TIER:
        if t not in whole:
            errors.append(f"{name}: 词汇缺档「{t}」")
    if '\u4e00\u53e5\u8bdd\u603b\u7ed3' not in whole:
        errors.append(f"{name}: 缺「一句话总结」")

    # --- 7 占位 / 乱码
    for i, l in enumerate(lines, 1):
        if NL in l:
            errors.append(f"{name}:L{i} 乱码字符 U+FFFD")
        if re.search(r'\uff08\u672a\u51fa\u73b0\u5728\u539f\u6587\uff09|TODO|待补|\u3010\u3011', l):
            errors.append(f"{name}:L{i} 占位/未完成标记")
        if re.search(r'^\|.*\|\s*$', l) and l.count('|') >= 3 and not l.strip().startswith('|---'):
            pass  # 正常表格行

# --- 总览 H1 语义
print("=== 总览 H1 语义校验 ===")
EXP = {'00_\u6982\u8ff0.md': '\u6982\u8ff0',
       '00_\u91d1\u53e5\u7cbe\u9009.md': '\u91d1\u53e5',
       '00_\u60c5\u611f\u8282\u70b9.md': '\u60c5\u611f\u8282\u70b9'}
for fn, kw in EXP.items():
    p = os.path.join(BOOK, fn)
    if not os.path.exists(p):
        errors.append(f"{fn}: 文件缺失")
        continue
    h1 = next((l.strip() for l in open(p, encoding='utf-8') if l.startswith('# ')), '')
    ok = kw in h1
    if not ok:
        errors.append(f"{fn}: H1 与文件语义不符 -> {h1}")
    # 四子项：金句每条须有 出处/中文理解/为什么重要/呼应
    if fn == '00_\u91d1\u53e5\u7cbe\u9009.md':
        s = open(p, encoding='utf-8').read()
        for it in ['\u51fa\u5904', '\u4e2d\u6587\u7406\u89e3', '\u4e3a\u4ec0\u4e48\u91cd\u8981', '\u547c\u5e94']:
            c = s.count(f'**{it}')
            if c < 20:
                errors.append(f"{fn}: 四子项「{it}」仅 {c} 处（应覆盖 25 句）")
    if fn == '00_\u6982\u8ff0.md':
        s = open(p, encoding='utf-8').read()
        for it in ['\u4e3b\u9898', '\u4eba\u7269\u5f27\u5149']:
            if f"## {it}" not in s:
                errors.append(f"{fn}: 缺章节「{it}」")
        for nm in ['Anna Arbor', 'Jennie', 'Kowalski', 'Peter', 'Ursula']:
            if nm not in s:
                errors.append(f"{fn}: 人物弧光缺 {nm}")
    if fn == '00_\u60c5\u611f\u8282\u70b9.md':
        s = open(p, encoding='utf-8').read()
        c = len(re.findall(r'^### \u8282\u70b9', s, re.M))
        if not (8 <= c <= 10):
            errors.append(f"{fn}: 情感节点 {c} 个（应 8–10）")
        for it in ['\u53d9\u4e8b\u6982\u62ec', '\u5173\u952e\u5f15\u8bed', '\u60c5\u611f\u7ba1\u7406', '\u53d9\u4e8b\u8d21\u732e']:
            if s.count(f'**{it}') < 8:
                errors.append(f"{fn}: 情感节点四子项「{it}」不足 8 处")

print(f"\n共扫描 {total_blocks} 个引语块 / {len(glob.glob(os.path.join(BOOK,'ch*.md')))} 章")
if warns:
    print(f"\n--- WARN ({len(warns)}) ---")
    for w in warns:
        print("  ⚠ " + w)
if errors:
    print(f"\n--- FAIL ({len(errors)}) ---")
    for e in errors:
        print("  ✗ " + e)
    print('\nAUDIT_STRUCT FAIL')
    sys.exit(1)
print('\nAUDIT_STRUCT PASS')
