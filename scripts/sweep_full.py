#!/usr/bin/env python3
"""
sweep_full.py — 引语**整串** flat 比对（方案 P1 第 8 个脚本，AGENTS 第 10 条 d 终验件）

⚠️ **条件性工具**（2026-09-26 用户已定：epub 以后一定清理）
------------------------------------------------------------------------
**依赖 `library/*.epub` 才具备完整能力**，故**不进常规门禁清单**——epub 清理
当天它就成了跑不了的死条目，正是方案 §11.3 第 10 条「落点表自己也要验」要防的
缺陷。无 epub 时退化为「无参照集 → ❓ 无法判定」，**不计入「门禁全绿」判定**。

为什么需要
----------
`verify_quotes` 只取引语**前 52 字符**做指纹比对，其后内容**从未比对**——这是
AGENTS 盲区表明载的盲区。`--full` 只是关掉这个优化、走同一套比对逻辑，仍不
等于「整串逐字验证」。

本脚本是 AGENTS 第 10 条 d 指定的**终验标准件**：
「把引语**全串**（而非前 52 字符指纹）flat 比对当章 `text/`，是 52 字符指纹盲区
的**唯一克星**」。

四档判定
--------
| 档 | 判据 | 判定 |
|----|------|------|
| ✅ 本章命中 | 整串 flat 在**本章** text/ | 通过 |
| ⚠️ 跨章命中 | 整串在别的章 | 提示 |
| 🔶 拼接命中 | 整串查无但分段皆在 | 提示——**跨标签拼接** |
| ❌ 全书查无 | 分段也不在 | **FAIL** |

「拼接命中」这档不可省：flat 整串查无 ≠ 凭空造词。AGENTS 有 12 处实证——两半
逐字都在原文、中间叙述标签被换成句号，flat 口径天然对拼接假阴为「查无」，直接
判 A 类会误杀真引语（2026-09-22 She Haunts 实证）。实测本脚本在
that-first-flight 上就抓到 2 处这种拼接（`Jesus. It's thick.`）。

用法
----
    python3 scripts/sweep_full.py "<书目录>" [--quiet] [--ch NN]

参照集优先级：逐章 `text/`（能定章）→ epub（整书，不能定章）。
只有 epub 时，跨章/本章两档并为「全书命中」，且**章节归属不可判**。
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_quotes import extract_quotes, flat_alpha, epub_flat_text  # noqa: E402

CIRCLED = '①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕'


def load_chapters(book):
    out = {}
    for p in sorted(glob.glob(os.path.join(book, 'text', '*.txt'))):
        m = re.search(r'ch(\d+)', os.path.basename(p))
        if m:
            out[int(m.group(1))] = flat_alpha(
                open(p, encoding='utf-8', errors='ignore').read())
    return out


def halves(q):
    """按句末标点与省略号切分，返回**原文**片段（不是 flat 串——suffix_match 要按词切）。

    ⚠️ 只按 `.!?…` 切会漏掉「片段以逗号/破折号悬空结尾」的情形，须额外试
    「去掉末段」的变体（末段本身不在片段里，中间被换掉的部分缺位）。
    """
    parts = [p for p in re.split(r'(?<=[.!?…])\s+|\s*…\s*|\.\.\.', q.strip()) if p.strip()]
    seg = [p for p in parts if len(flat_alpha(p)) >= 5]
    if len(seg) > 1:
        return seg
    if len(parts) > 1 and any(p.rstrip().endswith((',', '，', '—', '–')) for p in parts):
        trimmed = [p for p in parts[:-1] if len(flat_alpha(p)) >= 5]
        if trimmed:
            return trimmed + ['']
    return seg


def suffix_match(seg, allflat):
    """seg 去掉前 k 个词后能否命中——抓**段内拼接**。

    叙述标签被删导致的前缀错位，整段比对与按句切两段都救不了（切分点落在段内部）：
      原书 `raised her eyebrows in surprise—"Tamsin from CRM Services for"—she
             squinted at the paper and l…`
      md   `We've got Tamsin from CRM Services for developing a template to…`
    与 `check_overview_full` 同一实现——两处口径必须一致，否则同一段文字在
    正文章节判 🔶、在总览判 ❌，排查的人会怀疑工具而不是怀疑书。
    """
    toks = re.findall(r"[A-Za-z][A-Za-z']*", seg)
    for k in range(1, len(toks)):
        cand = ' '.join(toks[k:])
        if len(cand) >= 12 and flat_alpha(cand) in allflat:
            return k
    return 0


def md_chapter(body, name):
    m = re.search(r'^source_text:\s*ch(\d+)', body, re.M)
    if m:
        return int(m.group(1))
    m = re.search(r'ch(\d+)', name) or re.match(r'^(\d{1,3})[.\-\s]', name)
    return int(m.group(1)) if m else None


def main():
    args = sys.argv[1:]
    quiet = '--quiet' in args
    only = None
    for a in args:
        if a.startswith('--ch'):
            only = int(a[4:])
    pos = [a for a in args if not a.startswith('--')]
    if not pos:
        raise SystemExit('用法: sweep_full.py "<书目录>" [--quiet] [--ch NN]')
    book = pos[0]
    mds = sorted(glob.glob(os.path.join(book, '*.md')))
    if not mds:
        print('该目录下无 md 文件：%s' % book)
        return 2
    chapters = load_chapters(book)
    epaths = sorted(glob.glob(os.path.join(book, 'library', '*.epub')))
    if not chapters and not epaths:
        print('=== 引语整串 flat 比对（%s）===' % os.path.basename(book.rstrip('/')))
        print('  ❓ **无法判定**：无 text/ 且无 library/*.epub —— 无参照集。')
        print('     本脚本是**条件性工具**：epub 清理后不再具备完整能力，')
        print('     届时应从门禁清单撤下而非任其报错。')
        return 2
    allflat = ''.join(chapters.values())
    if not allflat and epaths:
        allflat = flat_alpha(epub_flat_text(epaths[0]))

    n_ok = n_cross = n_splice = n_miss = n_short = n_nochap = 0
    misses, crosses, splices = [], [], []
    for md in mds:
        name = os.path.basename(md)
        if re.match(r'^0\d[_. ]', name) or name.startswith('00'):
            continue                      # 总览归 check_overview_full
        body = open(md, encoding='utf-8', errors='ignore').read()
        chap = md_chapter(body, name)
        if only is not None and chap != only:
            continue
        quotes, _ = extract_quotes(body, include_short=True)
        for q in quotes:
            fq = flat_alpha(q)
            if not fq:
                continue
            if len(fq) < 20:
                n_short += 1
                continue                  # 短引语归 check_short_quotes
            if chapters:
                cf = chapters.get(chap, '')
                if chap is None:
                    n_nochap += 1
                    cf = allflat
                if cf and fq in cf:
                    n_ok += 1
                    continue
                other = [str(k) for k, v in chapters.items()
                         if k != chap and fq in v]
                if other:
                    n_cross += 1
                    crosses.append((name, chap, q, other[:4]))
                    continue
            elif fq in allflat:
                n_ok += 1
                continue
            seg = halves(q)
            if len(seg) > 1 and all(flat_alpha(s) in allflat for s in seg if s):
                n_splice += 1
                splices.append((name, chap, q))
                continue
            if any(suffix_match(s, allflat) for s in seg if s):
                n_splice += 1
                splices.append((name, chap, q))
                continue
            n_miss += 1
            misses.append((name, chap, q))

    print('=== 引语整串 flat 比对（%s）===' % os.path.basename(book.rstrip('/')))
    print('  参照集：%s%s' % ('text/ 逐章（%d 章，可定章）' % len(chapters) if chapters
                             else 'epub 整书（**不能定章**，跨章/本章两档并为全书命中）',
                             ' + epub 交叉验证' if (chapters and epaths) else ''))
    print('  ✅ 本章命中 %d ｜ ⚠️ 跨章 %d ｜ 🔶 跨标签拼接 %d ｜ ❌ 全书查无 %d'
          % (n_ok, n_cross, n_splice, n_miss))
    print('  （短引语 %d 条归 check_short_quotes；无章可对 %d 条未判）' % (n_short, n_nochap))
    if not quiet:
        for name, chap, q, where in crosses:
            print('  ⚠️  %s（ch%02d）实为 ch%s：%s' % (name[:32], chap or 0, ','.join(where), q[:48]))
        for name, chap, q in splices:
            print('  🔶 %s（ch%02d）跨标签拼接，各段逐字都在：%s' % (name[:32], chap or 0, q[:44]))
        for name, chap, q in misses:
            print('  ❌ %s（ch%02d）整串与分段均全书查无：%s' % (name[:32], chap or 0, q[:52]))
    return 1 if n_miss else 0


if __name__ == '__main__':
    sys.exit(main())
