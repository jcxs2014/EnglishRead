#!/usr/bin/env python3
"""
audit_numbers.py — 计数断言核查（方案 P1 第 6 个脚本）

为什么需要
----------
**计数断言是本库最高频的语义缺陷**，而工具门禁完全不看它：`verify_quotes` /
`check_chapter_quotes` 只管引语是否逐字，`check_vocab` 只管词表，
`check_entities` 只管梗概实体——于是「整句十九个词」「只有七个词」「三个分句」
「`分隔线`切为四段」这类**生成时凭印象写出**的数字断言全部漏网。

attic 实证（`count_claim_audit.py` 文件头自记）：本批次最高频的语义缺陷就是
「计数断言」。

来源：`attic/count_claim_audit.py`（83 行，A/B 两类）+ `count_claims.py`（76 行，
「N 个 `every single`」这类词形计数）合并。

可核查与不可核查的分界（不假装全都做了）
----------------------------------------
| 断言形态 | 可否机械核查 | 本脚本 |
|----------|-------------|--------|
| 「N 个词」「N 词」「N-word」 | ✅ 数参照串的词 | ✅ 判 |
| 「N 个 `token`」「N 次 `token`」 | ✅ 数 token 在块内引语出现次数 | ✅ 判 |
| 「N 个分句」「N 句」 | ✅ 数引语句末标点 | ✅ 判 |
| 「N 个字符」 | ✅ 数 ASCII 字符 | ✅ 判 |
| 「分隔线切为 N 段」 | ✅ 数 `text/` 里 `^—$` 行数 | ✅ 判 |
| **「年龄 N 岁」「占比 N%」** | ❌ 需故事事实，非文本可推 | **只统计并列出，不判** |

年龄与百分比**不做判红**：它们要的是「人物实际年龄」这类故事事实，文本层
推不出来，硬做只能靠猜。脚本会统计这类断言的条数并原样列出，让人去核——
比给一个假的判定强。

严重度：差 1 处只提示、差 ≥2 处判 FAIL
--------------------------------------
词数天然有口径差（连字符 `well-known` 数 1 还是 2、缩写带不带点、破折号连词），
差 1 极可能是口径而非错误。差 ≥2 才是真的写错。故按**差值**分两级，不一律判红。

用法
----
    python3 scripts/audit_numbers.py "<书目录>" [--quiet]

退出码：有 FAIL 则 1；无参照集（无 text/）→ 2。
"""
import glob
import os
import re
import sys

CN = {'零': 0, '一': 1, '两': 2, '二': 2, '三': 3, '四': 4, '五': 5,
      '六': 6, '七': 7, '八': 8, '九': 9, '十': 10, '廿': 20, '卅': 30}
NUM = '零一二三四五六七八九十廿卅两0-9'
# 预置字符类。**不要用 `(%s)` 直接插值 NUM**——那样 `+` 会落进方括号里变成
# 字面量（`(零…两0-9+)`），量词失效、静默一条不报。必须插 NUMC。
NUMC = '[' + NUM + ']+'
SHORT_QUOTE_WORDS = 12   # 参照引语词数上限：超过则「N 个词」指向不明
SPAN = re.compile(r'`([^`\n]+)`|"([^"\n]{2,})"|“([^”\n]{2,})”')


def cn2int(s):
    if s.isdigit():
        return int(s)
    if s in CN:
        return CN[s]
    if len(s) == 2 and s[0] == '十' and s[1] in CN:
        return 10 + CN[s[1]]
    if len(s) == 2 and s[1] == '十' and s[0] in CN:
        return CN[s[0]] * 10
    if len(s) == 3 and s[1] == '十':
        return CN[s[0]] * 10 + CN[s[2]]
    return None


def nwords(s):
    """词数。口径：字母数字与撇号连写算 1 个词，故 `well-known` 算 2、
    `don't` 算 1——**这个口径必须在报告里写明**，否则读者无从判断差 1 是否合理。"""
    return len(re.findall(r"[A-Za-z0-9'’]+", s))


def nascii(s):
    return sum(1 for c in s if c.isascii() and c.isalnum())


def nclauses(s):
    """**分句**数（逗号级），不是句子数。

    ⚠️ 中文「三个分句」指分句/小句，按 `，,；;：:—–` 断；按 `.!?…` 断是**句子**，
    会把「三个分句」数成 1——纯属口径错，不是缺陷（实测 forgotten-sisters
    ch03:108、ch13:72 两处都是这个坑）。"""
    parts = re.split(r'(?<=[，,；;：:—–])\s*|(?<=[.!?…])\s+', s.strip())
    return len([x for x in parts if x.strip()])


def spans(line):
    for m in SPAN.finditer(line):
        for g in m.groups():
            if g:
                yield m.start(), g


def is_quote_line(line):
    s = line.strip()
    if s.startswith('>'):
        return not re.match(r'^>\s*\*\*[^*]+\*\*\s*[:：]', s)
    return bool(re.match(r'^\*{0,2}[①-⑳㉑-㉕]', s))


def pick_ref(pre, cur_quote):
    """断言前的参照串解析（准确率关键）。

    1) 同一行内、断言**之前**的最后一个含英文的反引号/引号片段
    2) 否则：若前置语境含「全句/整句/该句/本章/全章/全文」，取本块引语
    3) 否则返回 None → 该条不判（计为「未解析」），不猜
    """
    last = None
    for pos, g in spans(pre):
        if re.search(r'[A-Za-z]', g):
            last = g
    if last:
        return last, '同行前引'
    if re.search(r'全句|整句|该句|本章|全章|全文|整段|全段', pre) and cur_quote:
        return cur_quote, '本块引语'
    return None, ''


def main():
    args = sys.argv[1:]
    quiet = '--quiet' in args
    pos = [a for a in args if not a.startswith('--')]
    if not pos:
        raise SystemExit('用法: audit_numbers.py "<书目录>" [--quiet]')
    book = pos[0]
    mds = sorted(glob.glob(os.path.join(book, '*.md')))
    if not mds:
        print('该目录下无 md 文件：%s' % book)
        return 2
    have_text = bool(glob.glob(os.path.join(book, 'text', '*.txt')))

    fails, warns, unresolved, unverifiable = [], [], [], []
    n_claims = 0

    for md in mds:
        name = os.path.basename(md)
        body = open(md, encoding='utf-8', errors='ignore').read()
        lines = body.split('\n')
        # 分隔线段数：需本章 text/
        seps = None
        if have_text:
            m = re.search(r'ch(\d+)', name)
            cand = None
            ms = re.search(r'^source_text:\s*ch(\d+)', body, re.M)
            if ms:
                cand = sorted(glob.glob(os.path.join(book, 'text', 'ch%02d*.txt' % int(ms.group(1)))))
            elif m:
                cand = sorted(glob.glob(os.path.join(book, 'text', 'ch%02d*.txt' % int(m.group(1)))))
            if cand and os.path.exists(cand[0]):
                seps = len(re.findall(r'(?m)^—\s*$',
                                      open(cand[0], encoding='utf-8', errors='ignore').read()))
        cur_quote = None
        for i, l in enumerate(lines, 1):
            if is_quote_line(l):
                b = re.sub(r'^\s*>\s*(?:\*{0,2}原句\s*\d+\s*[:：]?\*{0,2}\s*)?', '', l).strip()
                b = b.strip('*').strip('"“”\' ')
                # 元数据引用块（作者/原书/精读目录）不是引语——实测 floating-hotel
                # 00 概述把整条书目当成本块引语，后续断言全拿它当参照
                if re.search(r'[A-Za-z]{3}', b) and not re.search(
                        r'作者[：:]|原书|精读目录|notes/books|出版|ISBN', b):
                    cur_quote = b
                continue
            # 年龄 / 百分比：只统计，不判
            for m in re.finditer(r'(%s)\s*(?:岁|周岁)|\s*(%s)\s*%%|\s*(%s)\s*%%' % (NUMC, NUMC, NUMC), l):
                n_claims += 1
                unverifiable.append((name, i, m.group(0)))
            # 分隔线切为 N 段
            m = re.search(r'分隔线[^。]{0,14}?切为\s*(%s)\s*段' % NUMC, l)
            if m:
                n_claims += 1
                claim = cn2int(m.group(1))
                if seps is None:
                    unresolved.append((name, i, '切为%s段' % m.group(1), '无本章 text/'))
                elif claim is not None and claim != seps + 1:
                    fails.append((name, i, '「切为%s段」→ 实测 %d 段（分隔线 %d 条）'
                                  % (m.group(1), seps + 1, seps), 'md'))
            # 字符数
            for m in re.finditer(r'(%s)\s*个?\s*字符' % NUMC, l):
                n_claims += 1
                claim = cn2int(m.group(1))
                tgt, how = pick_ref(l[:m.start()], cur_quote)
                if claim is None or not tgt:
                    unresolved.append((name, i, '%s个字符' % m.group(1), '参照串未解析'))
                    continue
                if how != '本块引语':
                    # 参照串是同行里的某个片段时，「N 个字符」到底数的是哪个片段
                    # 说不准——实测 `「十一个词」` 的参照解析成 `made me`（被解释
                    # 的短语，不是被计数的对象）。这类**不判**，只记未解析。
                    unresolved.append((name, i, '%s个字符' % m.group(1),
                                       '参照串为同行片段，指向不明'))
                    continue
                unresolved.append((name, i, '%s个字符' % m.group(1),
                                   '「N 个字符」指引语内某子串，无法机械定位，不判'
                                   '（整条引语 %d 字符）' % nascii(tgt)))
            # 词数 / 分句数 / 次数
            # 单位（词/字/word）用非捕获组 `(?!word)` 收尾——`\b` 在中文字符后
            # 不可靠（实测 `词\b` 在 `词。` 上不匹配，须用 `(?!\w)`），
            # 而非捕获就没有 group(2) 可取，故单位直接从原文切出来。
            for m in re.finditer(r'(%s)\s*个?\s*(?:词|字|words?)(?!\w)' % NUMC, l):
                n_claims += 1
                claim = cn2int(m.group(1))
                unit = re.sub(r'^[个次\s]+', '', m.group(0)[len(m.group(1)):].strip()) or '词'
                tgt, how = pick_ref(l[:m.start()], cur_quote)
                if claim is None or not tgt:
                    unresolved.append((name, i, '%s个%s' % (m.group(1), unit), '参照串未解析'))
                    continue
                if how != '本块引语':
                    unresolved.append((name, i, '%s个%s' % (m.group(1), unit),
                                       '参照串为同行片段，指向不明'))
                    continue
                if not re.search(r'[A-Za-z]{3}', tgt):
                    unresolved.append((name, i, '%s个%s' % (m.group(1), unit), '参照串无英文'))
                    continue
                # **一律未判**：本库「N 个词」绝大多数指**引语里的某个子短语**，
                # 不是整条引语，而那个子短语无法机械定位。实测三例：
                #   `「五个词」` / 整条引语 10 词 —— 但 `steady as a forest pond` 恰 5 词
                #   `「六个词」` / 整条 11 词 —— 但 `finish-homework-before-going-to-parties` 恰 6 词
                #   `「三个词」` / 整条 5 词 —— 但 `peeled apathetically away` 恰 3 词
                # 判它只会造假红。**教训：能定位到「数的是哪一个」才谈得上核查。**
                unresolved.append((name, i, '%s个%s' % (m.group(1), unit),
                                   '「N 个词」指引语内某子短语，无法机械定位，不判'
                                   '（整条引语 %d 词）' % nwords(tgt)))
            for m in re.finditer(r'(%s)\s*个\s*分句' % NUMC, l):
                n_claims += 1
                # **一律未判**：本库「分句」口径不统一——按 `，,；;` 切得 6、
                # 按 `.!?…` 切得 1，同一条断言两种算法差 5 倍（实测 all-our-yesterdays
                # ch03:65「三个分句」实测 6、forgotten-sisters 00_金句精选:109
                # 「两个分句」实测 4）。没有可裁决的客观真值，交人判。
                unresolved.append((name, i, '%s个分句' % m.group(1),
                                   '分句口径不统一（按逗号切与按句号切结果差数倍），不判'))
            # 「N 个 `token`」/「N 次 `token`」：数 token 在块内引语的出现次数
            for m in re.finditer(r'(%s)\s*(?:个|次)\s*(?:`([^`]+)`|"([^"]+)")' % NUMC, l):
                n_claims += 1
                claim = cn2int(m.group(1))
                token = m.group(2) or m.group(3) or ''
                if claim is None or not token or not cur_quote:
                    unresolved.append((name, i, '%s个%s' % (m.group(1), token), '无块内引语可比'))
                    continue
                # ⚠️ 2026-09-28 假红守卫（Paris Deception 9 条实证）：
                # 中文「N 个 + token」**经常不是在数这个 token**，三种形态：
                #   ① 指示代词：「**前一个** `His` 后面断掉」——`一个`=the first one
                #   ② 被修饰的名词：「**两个** `I` **打头的名词**」——数的是名词
                #   ③ 结构/短语：「**三个** `of` **结构并排**」——数的是 of-结构
                # 这三种里「数的是哪一个」都无法机械定位，与本脚本对「N 个词」
                # 既有的不判原则同源（一律未判，不报 ❌）。
                # 判据：token 紧邻前方有指示代词，或紧邻后有中文修饰名。
                prefix_ctx = l[max(0, m.start() - 4):m.start()]
                token_raw = m.group(2) or m.group(3) or ''
                token_end_in_line = m.end(2) if m.group(2) else (m.end(3) if m.group(3) else m.end())
                # ⚠️ m.end(2) 落在**收尾反引号之前**，suffix 必须先剥掉
                # 闭合标记（实测 ch15 suffix 实际是 "` 打头的名词（"，
                # 不剥则 `\s*` 跳不过反引号，守卫对全部 backtick token 静默失效）。
                suffix_ctx = l[token_end_in_line:token_end_in_line + 10].lstrip('`"\u201c')
                if re.search(r'[前上后这那每另]$', prefix_ctx) or \
                        re.match(r'\s*(?:类?词(?:组|语)?|名词|动词|副词|形容词|结构|短语|'
                                 r'从句|词组|开头|起头|打头|结尾|并排|字样|出现|重复|'
                                 r'连用|类词|次|遍|各配|搭配|说法|形式|用法)', suffix_ctx):
                    unresolved.append((name, i, '%s个%s' % (m.group(1), token_raw),
                                       '「N 个」是指示代词或数的不是 token 本身（修饰名/结构），不判'))
                    continue
                # `N 个 a / b / c` 是**多 token 列表**，须逐个计数再求和——
                # 把整串当一个 token 永远得 0（实测「三个Their voices rose /
                # came coiling / hollering」误报为 0 次）
                toks = [x.strip() for x in re.split(r'[/／,，、;；]', token) if x.strip()]
                # 必须**以英文为主**才算英文 token：`两个"本该不在乎"的人`、
                # `三个"她不想知道"` 这类是中文短语/小节标题，被当英文 token 数
                # 必然得 0 → 批量假红（实测 floating-hotel 00 概述、the-morningside
                # ch13 各有）。ASCII 字母占比 <60% 一律不判。
                toks = [t for t in toks
                        if sum(c.isascii() and c.isalpha() for c in t) / max(1, len(t)) >= 0.6]
                # 去掉省略号：`三个 She hated...` 里 `She hated...` 带字面 `...`，
                # 拿去精确匹配必然 0 次（实测 the-morningside ch03:43 误报）
                toks = [re.sub(r'\s*(?:\.{3,}|…)+$', '', t).strip() for t in toks]
                toks = [t for t in toks if t]
                if not toks:
                    unresolved.append((name, i, '%s个%s' % (m.group(1), token),
                                       '非英文（中文短语或小节标题），不判'))
                    continue
                # **只有 token 逐字在引语内才判计数**——不在引语内的多半是
                # 意译/近义替换而非重复次数问题（实测「三个afraid」而引语是
                # `What did I have to fear?`，实为 afraid↔fear 的替换）
                if not any(re.search(r'(?<![A-Za-z])' + re.escape(t) + r'(?![A-Za-z])',
                                     cur_quote, re.I) for t in toks):
                    unresolved.append((name, i, '%s个%s' % (m.group(1), token),
                                       'token 不逐字在本块引语内（疑意译），不判'))
                    continue
                act = sum(len(re.findall(r'(?<![A-Za-z])' + re.escape(t) + r'(?![A-Za-z])',
                                         cur_quote, re.I)) for t in toks)
                d = abs(act - (claim or 0))
                if d == 0:
                    continue
                (warns if d == 1 else fails).append(
                    (name, i, '「%s个%s」→ 本块引语出现 %d 次'
                     % (m.group(1), token, act), '本块引语：%s' % cur_quote[:50]))

    print('=== 计数断言核查（%s）===' % os.path.basename(book.rstrip('/')))
    print('  扫 %d 个 md；抓到断言 %d 条（含不可机械核查的年龄/百分比 %d 条）'
          % (len(mds), n_claims, len(unverifiable)))
    print('  词数口径：连写算 1 词（`well-known`=2、`don\'t`=1）—— 差 1 极可能是口径而非错误')
    print('  ❌ 不符（差 ≥2）%d ｜ ⚠️ 差 1 %d ｜ ❓ 参照串未解析未判 %d ｜ ⚪ 不可机械核查 %d'
          % (len(fails), len(warns), len(unresolved), len(unverifiable)))
    if not quiet:
        for name, ln, msg, ctx in fails:
            print('  ❌ %s:%d  %s' % (name[:36], ln, msg))
            if ctx != 'md':
                print('       参照：%s' % ctx)
        for name, ln, msg, ctx in warns:
            print('  ⚠️ %s:%d  %s' % (name[:36], ln, msg))
            if ctx != 'md':
                print('       参照：%s' % ctx)
        for name, ln, claim, why in unresolved:
            print('  ❓ %s:%d  「%s」%s —— 需人判' % (name[:36], ln, claim, why))
        for name, ln, frag in unverifiable:
            print('  ⚪ %s:%d  「%s」年龄/百分比类，文本层推不出真值，只列出待人核' % (name[:36], ln, frag))
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
