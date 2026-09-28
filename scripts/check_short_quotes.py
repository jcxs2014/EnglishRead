#!/usr/bin/env python3
"""
check_short_quotes.py — 短引语兜底核对（方案 P1 第 5 个脚本）

为什么需要
----------
`verify_quotes` 对 **<20 个 flat 字符**的引语**静默跳过、只计数**——这是三本书
互证出来的盲区（Perfection / Forest of Scars / Rookie Season），AGENTS 盲区表
里明载「<20 flat 字符短引语不校验，单列计数提示人工 grep」。

也就是说：**一批书的引语门禁全绿，可能只是因为那些引语太短、被跳过了。**
本脚本把那批引语逐条捡回来核对。

口径必须复用 verify_quotes，不能自己写一套抽取器
------------------------------------------------
这是本脚本唯一的硬约束。attic 三份同族实现里，`short_quotes.py` 自己复刻了
抽取与剥离逻辑、`verify_short_quotes.py` 只认 `> **原句 N:**` 一种格式、
`check_short_quotes.py` 复用了 `extract_quotes`——**只有最后这一份口径是对的**。
两套抽取器必然出现「verify_quotes 说跳过了 N 条、本脚本却抽到 M ≠ N 条」的
矛盾，那时谁该信谁都说不清。故本脚本直接 `from verify_quotes import
extract_quotes, flat_alpha`，**口径随主门禁演进而自动同步**。

用法
----
    python3 scripts/check_short_quotes.py "<书目录>" [--quiet]

参照集：`<书目录>/text/chNN*.txt`（逐章，与 check_chapter_quotes 同口径）。
无 text/ → ❓ 无法判定，退出码 2。md 无 `source_text` / 名为 chNN 时按文件名推章。

退出码：有 MISS 则 1；无参照集则 2。
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_quotes import extract_quotes, flat_alpha  # noqa: E402

SHORT_LIMIT = 20


def chapter_texts(book):
    """{章号: flat 正文}。文件名形态不设限（ch01_ / ch25_byrds_of_a_feather 都收）。"""
    out = {}
    for p in sorted(glob.glob(os.path.join(book, 'text', '*.txt'))):
        m = re.match(r'ch(\d+)([a-z]?)', os.path.basename(p))
        if not m:
            continue
        # 2026-09-28：键带字母后缀（'18'/'18a'），与 check_vocab 对齐
        out[str(int(m.group(1))) + m.group(2)] = flat_alpha(
            open(p, encoding='utf-8', errors='ignore').read())
    return out


def md_chapter(body, name):
    """frontmatter `source_text: chNN` 优先（偏移书的唯一可靠口径），
    否则从文件名推 `chNN` / `NN.` / `NN-` 前缀。推不出返回 None。

    ⚠️ **总览文件必须返回 None，不能返回 0**——`00 金句精选.md` 会被
    `^(\\d{1,3})[.\\-\\s]` 匹配成「ch0」，而它根本没有单一章号。第一版把
    总览的短引语按「无章可对」整批跳过（实测 that-first-flight 4 条），
    覆盖率上的洞比判红更糟——总览引语本就该按**全书口径**核。
    """
    if re.match(r'^0\d[_. ]', name) or name.startswith('00'):
        return None
    m = re.search(r'^source_text:\s*ch(\d+)([a-z]?)', body, re.M)
    if m:
        return str(int(m.group(1))) + m.group(2)
    m = re.match(r'ch(\d+)([a-z]?)', name)
    if m:
        return str(int(m.group(1))) + m.group(2)
    m = re.match(r'^(\d{1,3})[.\-\s]', name)
    return str(int(m.group(1))) if m else None


def epub_flat(book):
    p = sorted(glob.glob(os.path.join(book, 'library', '*.epub')))
    if not p:
        return ''
    try:
        from verify_quotes import epub_flat_text
        return flat_alpha(epub_flat_text(p[0]))
    except Exception:
        return ''


def main():
    args = sys.argv[1:]
    quiet = '--quiet' in args
    pos = [a for a in args if not a.startswith('--')]
    if not pos:
        raise SystemExit('用法: check_short_quotes.py "<书目录>" [--quiet]')
    book = pos[0]
    texts = chapter_texts(book)
    if not texts:
        print('=== 短引语兜底核对（%s）===' % os.path.basename(book.rstrip('/')))
        print('  ❓ **无法判定**：text/ 无提取件 —— 短引语无从核对，不等于通过。')
        return 2
    allflat = ''.join(texts.values())
    epflat = epub_flat(book)          # B 类裁决：text/ 缺但 epub 有 = 语料缺失

    n_short = n_hit = n_miss = n_nochap = n_over = n_gap = n_splice = 0
    misses, otherchap, gaps, splices = [], [], [], []

    def halves(q):
        """按句末标点切成子句；返回每段的 flat（长度够的）。

        **跨标签拼接兜底不可省**（AGENTS 有 She Haunts 12 条实证：两半逐字都在
        原文、中间叙述标签被换成句号，flat 整串查无）。实测 that-first-flight
        2 处「MISS」全是这一类：
          原书 `"Jesus," she breathes out. "It's thick."`
          md   `Jesus. It's thick.`      ← 吞掉叙述标签、逗号改句号
          原书 `"I need more," I plead. "Please."`
          md   `I need more. Please.`
        不做这一步就把**真引语**报成凭空造词（退出码 1 变成假红）。
        """
        parts = re.split(r'(?<=[.!?…])\s+', q.strip())
        return [flat_alpha(p) for p in parts if len(flat_alpha(p)) >= 5]

    for md in sorted(glob.glob(os.path.join(book, '*.md'))):
        name = os.path.basename(md)
        body = open(md, encoding='utf-8', errors='ignore').read()
        quotes, _short = extract_quotes(body, include_short=True)
        chap = md_chapter(body, name)
        if chap is None:
            chap_flat = allflat        # 总览：按全书口径
            n_over += 1
        else:
            chap_flat = texts.get(chap, '')
        for q in quotes:
            fq = flat_alpha(q)
            if len(fq) >= SHORT_LIMIT:
                continue               # 主门禁已覆盖，不重复核
            n_short += 1
            if not chap_flat:
                n_nochap += 1          # 章号推出但 text/ 无该章文件
                continue
            if fq in chap_flat:
                n_hit += 1
            elif fq in allflat:
                otherchap.append((name, chap, q))
            elif epflat and fq in epflat:
                n_gap += 1             # B 类：epub 有、text/ 缺 = 语料缺失
                gaps.append((name, chap, q))
            else:
                seg = halves(q)
                if len(seg) > 1 and all(s in allflat for s in seg):
                    n_splice += 1       # 跨标签拼接：各段逐字都在，只是中间被换掉
                    splices.append((name, chap, q))
                else:
                    n_miss += 1
                    misses.append((name, chap, q))

    print('=== 短引语兜底核对（%s）===' % os.path.basename(book.rstrip('/')))
    print('  verify_quotes 跳过（<%d flat 字符）的引语：%d 条 —— 这些主门禁**根本没查**'
          % (SHORT_LIMIT, n_short))
    if n_short == 0:
        print('  ✅ 本书无短引语，主门禁已全覆盖。')
        return 0
    print('  ✅ 命中 %d ｜ ⚠️ 在别的章 %d ｜ 🔶 跨标签拼接 %d ｜ 🔧 B类语料缺 %d ｜ ❌ 全书查无 %d'
          % (n_hit, len(otherchap), n_splice, n_gap, n_miss))
    print('  口径：正文章节按本章核；总览文件（00_*）按全书核')
    if not quiet:
        for name, chap, q in otherchap:
            print('  ⚠️  %s（ch%02s 标注）实为别章：%s' % (name[:34], chap, q[:56]))
        for name, chap, q in splices:
            print('  🔶 %s（ch%02s）跨标签拼接，各段逐字都在：%s' % (name[:34], chap, q[:48]))
        for name, chap, q in gaps:
            print('  🔧 %s（ch%02s）text/ 缺、epub 有 → B 类语料缺失：%s' % (name[:34], chap, q[:44]))
        for name, chap, q in misses:
            print('  ❌ %s（ch%02s）text/ 与 epub 均查无：%s' % (name[:34], chap, q[:56]))
        if n_nochap:
            print('  ❓ %d 条短引语所在 md 的章号在 text/ 无对应提取件，未核' % n_nochap)
    return 1 if n_miss else 0


if __name__ == '__main__':
    sys.exit(main())
