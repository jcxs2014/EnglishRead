#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""说话人归属核对（2026-09-29 新增，**抽查级·不进提交门禁**）

## 为什么做它

`docs/实测档案/M_第10条_五步审查实例与检查器死代码.md` 的 33 处阻断型里，
**8 处是说话人 / 人称 / 主语错配**——引语逐字全对，错的是「谁在说」。
六道门禁结构上看不见：它们只验「引语是否逐字」，而说话人错配时引语 100% 正确。

## ⚠️ 定级：抽查级，不阻塞 commit（2026-09-29 实测）

**全库 315 本跑下来只有 1 条真缺陷，命中里约 1/3 是假阳。** 达不到门禁精度。
调试中修掉的 6 类假阳，每一类都改变了结果——这个缺陷类**不可靠机械化**：

1. **连接粒度**：英文引语在「关键词」行、说话人归因在「读者视角提示」行，
   行级连接结构上不可能命中（三条判据必然全 0 = 死代码）⇒ 必须块级。
2. **动词歧义**：`Alison 承认 "He'd…"` 里 Alison 是**被叙述对象**不是说话人；
   `承认/否认/解释/指出` 叙述义与言语义同形 ⇒ 动词表收窄到无歧义集。
3. **真值不能取全书级**：同一句台词常被不同人物在不同场景说
   （the-color-of-death ch05「与儿子的问题一字不差——同一句问话从两个人嘴里说出」）
   ⇒ 真值**按章**索引；章内同句多人说过 ⇒ 判为不可判。
4. **指纹只取主引语**：抽块内所有引号片段会把「关键词」行的
   `going to run into trouble` 这类短片段也算进去，必然在同章别处碰撞。
5. **块内变量泄漏**：`analysis` 在构建循环里定义却在判据循环里用 ⇒
   守卫行为随机（20 → 3 条的降幅全部来自这个 bug 修复，不是口径改进）。
6. **多说话人块**：`"Sure," Julia said… "Very exciting…" Sylvie said…`
   说话人本就多人，判据不适用。

## 判据（唯一一条）

**原文邻接归属 vs md 分析层归因**。原文 `…"…," X said` 的说话人是硬事实。
仅当三条同时成立才报警：
  ① 该引语在**本章**只对应一个说话人
  ② md **分析层**归给了别人
  ③ **分析层完全不提**原文说话人

## 明确的盲区

1. 中短句、间接引语、无对话标签的段落全部不在口径内——本库大量叙述层引语
   （`"A small black hole had opened in her chest…"`）原文不带 `X said`。
2. **不做实体归一**（Jess/Jessica/the old man），只做 token 包含关系 + 称谓剥离。
3. 引语内的说话人 ≠ 说话人（`"I heard Mary say so"` 这类转述）⇒ **命中一律人判**。
4. 代词（`"Fine," she said`）一律跳过，只认专名 `X said`。

## 用法

```bash
python3 scripts/check_speaker_consistency.py "<书目录>" [--quiet]
```

退出码：0 = 未发现矛盾 ｜ 1 = 有命中（**需人判，可能假阳**）｜ 2 = 无法判定
"""

import glob
import os
import re
import sys
import unicodedata

CIRCLED = '①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕'
PRONOUNS = {'she', 'he', 'they', 'it', 'we', 'i', 'you', 'him', 'her', 'them'}

# 姓名抽取停用词：句首大写连词/副词 + 称谓冠词。
# 实测误报源：`…" said. And Ford looked…` → 姓名被抽成 `And Ford`；
# `Agent Hart` / `King Seran` / `Prince Aureli` → 称谓进了姓名。
NAME_STOP = {
    'and', 'but', 'so', 'then', 'now', 'yet', 'for', 'with', 'when', 'while',
    'his', 'her', 'their', 'its', 'my', 'our', 'your', 'this', 'that', 'there',
    'the', 'a', 'an', 'if', 'as', 'at', 'by', 'in', 'on', 'of', 'to', 'up',
    'out', 'no', 'not', 'yes', 'oh', 'well', 'just', 'only', 'even', 'after',
    'agent', 'king', 'queen', 'prince', 'princess', 'duke', 'duchess', 'lord',
    'lady', 'sir', 'dame', 'mr', 'mrs', 'ms', 'miss', 'dr', 'prof',
    'sgt', 'capt', 'col', 'gen', 'rev', 'father', 'mother', 'brother', 'sister',
    'uncle', 'aunt', 'coach', 'professor', 'detective', 'inspector', 'officer',
}

# 原文侧：`"…", X said`（X 必须是专名，代词跳过）
RE_SRC_ATTR = re.compile(
    r'[“"]([^“”"]{8,400}?)[”"][,，]?\s+'
    r'([A-Z][a-z]{1,15}(?:\s+[A-Z][a-z]{1,15})?)\s+'
    r'(?:said|asked|replied|added|answered|continued|observed|retained|murmured)\b'
)
# 原文侧：`X said: "…"`
RE_SRC_ATTR2 = re.compile(
    r'([A-Z][a-z]{1,15}(?:\s+[A-Z][a-z]{1,15})?)\s+'
    r'(?:said|asked|replied|added|answered)\s*:\s*'
    r'[“"]([^“”"]{8,400}?)[”"]'
)
# 原文侧：块内对话标签计数（多说话人判据）
RE_TAG = re.compile(
    r'[A-Z][a-z]{1,15}\s+(?:said|asked|replied|added|answered)\b')

# md 侧：归因。动词表**刻意收窄到无歧义的言语行为动词**——
# 承认/否认/解释/指出/提到/补充/提出 在中文里叙述义与言语义同形，无法靠形态区分。
RE_MD_ATTR = re.compile(
    r'([A-Z][a-z]{1,15})\s*'
    r'(?:追问|反问|问道|说|回答|答道|回应|开口|写道|回话|接话)'
)
RE_MD_ATTR_EN = re.compile(
    r'\b([A-Z][a-z]{1,15})\s+'
    r'(?:asks|asked|says|said|replies|replied|answers|answered|adds|added)\b'
)
RE_MD_ASK = re.compile(r'([A-Z][a-z]{1,15})\s*的\s*(?:回应|反问|追问|提问|说法|问题|提议)')
RE_MD_IS = re.compile(r'说话人(?:是|为)\s*([A-Z][a-z]{1,15})')

RE_QUOTE_LINE = re.compile(
    r'(?m)^>\s*\*\*(?:原句\s*\d+[:：]?|'
    + CIRCLED + r')\*\*\s*[“"]?(.{12,400}?)[”"]?\s*$')
RE_CH = re.compile(r'^ch0*(\d+)')


def flat(s):
    s = unicodedata.normalize('NFKD', s)
    return re.sub(r'[^a-z0-9]', '', s.lower())


def norm_person(name):
    """去称谓/停用词后的词元集合。空集合 = 抽不出人名。"""
    toks = [t for t in re.split(r'\s+', name.strip()) if t]
    return {t.lower() for t in toks if t.lower() not in NAME_STOP}


def same_person(a, b):
    ta, tb = norm_person(a), norm_person(b)
    if not ta or not tb:
        return True          # 抽不出人名 ⇒ 不当作错（宁可漏报）
    return bool(ta & tb) or ta <= tb or tb <= ta


def attributions(text):
    who = set()
    for rx in (RE_MD_ATTR, RE_MD_ATTR_EN, RE_MD_ASK, RE_MD_IS):
        for m in rx.finditer(text):
            w = m.group(1)
            if w.lower() not in PRONOUNS and norm_person(w):
                who.add(w)
    return who


def load_sources(book):
    """{章号: {引语指纹: {说话人, …}}}，按章索引（见模块 docstring 第 3 条）。"""
    out = {}
    for f in sorted(glob.glob(os.path.join(book, 'text', '*.txt'))):
        m0 = RE_CH.match(os.path.basename(f))
        if not m0:
            continue
        d = out.setdefault(str(int(m0.group(1))), {})
        t = open(f, encoding='utf-8', errors='replace').read()
        for m in RE_SRC_ATTR.finditer(t):
            who, q = m.group(2), m.group(1)
            if who.lower() not in PRONOUNS and norm_person(who):
                d.setdefault(flat(q)[:40], set()).add(who)
        for m in RE_SRC_ATTR2.finditer(t):
            who, q = m.group(1), m.group(2)
            if who.lower() not in PRONOUNS and norm_person(who):
                d.setdefault(flat(q)[:40], set()).add(who)
    return out


def load_md(book):
    """[(文件名, 起始行, 块全文, 章号或 None)]——**块级**（见 docstring 第 1 条）。"""
    out = []
    for f in sorted(glob.glob(os.path.join(book, '*.md'))):
        name = os.path.basename(f)
        if name.startswith('00_'):
            continue
        mch = RE_CH.match(name)
        ch = str(int(mch.group(1))) if mch else None
        lines = open(f, encoding='utf-8', errors='replace').read().split('\n')
        cur, start = [], None
        for i, ln in enumerate(lines, 1):
            if RE_QUOTE_LINE.match(ln):
                if cur:
                    out.append((name, start, '\n'.join(cur), ch))
                cur, start = [ln], i
            elif start is not None:
                if ln.startswith('#') or ln.strip() == '---':
                    out.append((name, start, '\n'.join(cur), ch))
                    cur, start = [], None
                else:
                    cur.append(ln)
        if cur:
            out.append((name, start, '\n'.join(cur), ch))
    return out


def main():
    argv = [a for a in sys.argv[1:] if not a.startswith('-')]
    quiet = '--quiet' in sys.argv
    if not argv:
        print('用法: check_speaker_consistency.py "<书目录>" [--quiet]')
        return 2
    book = argv[0]
    mds = load_md(book)
    if not mds:
        print(f'❌ {book} 下没有正文 md')
        return 2
    src = load_sources(book)
    if not src:
        print('❓ 无 text/ 或原文无邻接对话标签 ⇒ 本书无法判定')

    by_fp = {}
    for name, ln, text, ch in mds:
        mq = RE_QUOTE_LINE.search(text)
        if not mq:
            continue
        quote = mq.group(1)
        # 多说话人块：引语内对话标签 ≥2 ⇒ 判据不适用（docstring 第 6 条）
        if len(RE_TAG.findall(quote)) > 1:
            continue
        analysis = '\n'.join(x for x in text.split('\n') if not x.startswith('>'))
        who = attributions(analysis)
        # 候选指纹 = 主引语 + 内层第一段引语（后者才是带 X said 的那句）
        cands = [flat(quote)[:40]]
        inner = re.search(r'[“"]([^”"]{12,300})[”"]', quote)
        if inner:
            cands.append(flat(inner.group(1))[:40])
        for fp in dict.fromkeys(cands):
            if len(fp) >= 20:
                by_fp.setdefault(fp, []).append((name, ln, who, ch, analysis))

    mismatch = []
    for fp, occ in by_fp.items():
        for name, ln, who, ch, analysis in occ:
            cand = src.get(ch or '', {}).get(fp)
            if not cand or len(cand) != 1:
                continue                    # 无真值 / 同章多人说过 ⇒ 不可判
            truth = next(iter(cand))
            wrong = {w for w in who if not same_person(w, truth)}
            if not wrong:
                continue
            if any(re.search(r'\b' + re.escape(t) + r'\b', analysis, re.I)
                   for t in norm_person(truth)):
                continue                    # 分析层提到了原文说话人 ⇒ 常态
            mismatch.append((name, ln, truth, sorted(wrong)))

    print('=== 说话人归属核对（抽查级·命中需人判）===')
    print(f'分析块 {len(mds)} 个 / 正文 {len({n for n, _, _, _ in mds})} 篇')
    print(f'原文邻接归属 {sum(len(v) for v in src.values())} 条 / {len(src)} 章')
    print(f'可判指纹 {len(by_fp)} 个')
    print(f'⚠️ 归因与原文不一致 {len(mismatch)}')

    if not quiet:
        for name, ln, truth, wrong in mismatch:
            print(f'  {name}:{ln}  原文是 {truth}，分析层归给 {"/".join(wrong)}')

    print('\n⚠️ 抽查级：**报 0 不等于「说话人都对」**，只等于「没找到可判的归属矛盾」。')
    print('   实测 315 本 1 条真缺陷 / 命中约 1/3 假阳 ⇒ 不进提交门禁。')
    print('   无对话标签的叙述层引语、间接引语、转述，全部不在口径内。')
    return 1 if mismatch else 0


if __name__ == '__main__':
    sys.exit(main())
