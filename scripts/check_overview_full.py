#!/usr/bin/env python3
"""
check_overview_full.py — 总览三篇整串核查 + 章节标签对账（方案 P1 第 9 个脚本）

⚠️ **条件性工具**（2026-09-26 用户已定：epub 以后一定清理）
------------------------------------------------------------------------
与 `sweep_full` 同：**不进常规门禁清单**。无 epub / 无 text/ 时报「❓ 无法判定」
并返回 2，**不计入「门禁全绿」判定**；epub 清理后应从清单撤下而非任其报错。

为什么需要
----------
`verify_overview_quotes` 只验「引语在全书某处存在」，**不验它是否在所标注的那
一章**。AGENTS 有明确实证：「总览引语的章节标注（chNN）是独立工具盲区——verify
只验逐字、不验标注对错，『引语真实但章节标错』**5 处全绿漏网**（2026-09-19）」。

五项检查
--------
| 项 | 内容 | 依据 |
|----|------|------|
| A | 概述/金句/情感节点里所有引语**整串** flat 比对 | verify_overview_quotes 不覆盖行内引语 |
| B | **章节标签对账**：引语是否真在它标注的那一章 | 「引语真实但章节标错」盲区 |
| C | 跨章多重命中（同一句在多章出现 → 标注有歧义） | 标签不可靠的信号 |
| D | 短引语（<20 flat）逐条列出，须人工核 | verify_quotes 的跳过盲区 |
| E | **总览 H1 语义校验** | AGENTS 第 9 条 h：Impossible Garden 事故就是 H1 错位 |

E 项的由来值得记：AGENTS 第 9 条 h 记了一次整文件写错的事故——把修过的
`金句精选` **整文件写进了 `00_情感节点.md`**，H1 都变成「# 金句精选」、16 个节点
全丢，修复报告却称完成。**一行 `grep -m1 '^# '` 就能抓住**，故机械化为门禁项。

用法
----
    python3 scripts/check_overview_full.py "<书目录>" [--quiet]
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_quotes import flat_alpha, epub_flat_text  # noqa: E402

# 总览里引语的载体：反引号、直/弯双引号、圆圈编号后的引号
# 总览里引语的载体：反引号、直/弯双引号。用显式 unicode 转义写定，别直接内嵌
# 那三个字符——第一版内嵌时正则编译直接报 `missing ), unterminated subpattern`。
SPAN = re.compile('`([^`\\n]{4,})`|"([^"\\n]{4,})"|“([^”\\n]{4,})”')
# 章节标签：`chNN`、`**出处**：chNN`、`（chNN）`
RE_LABEL = re.compile(r'ch(\d{1,3})')
# 总览 H1 语义：文件名 → H1 应含的关键词
H1_EXPECT = {
    '概述': ['概述'],
    '金句': ['金句'],
    '情感节点': ['情感节点'],
    '一句话总结': ['一句话总结'],
}
NOT_QUOTEISH = re.compile(r'[*_/|]|ch\d|text/|\.md\b|\.txt\b|\.epub\b')


def is_quoteish(x):
    if re.search(r'[一-鿿]', x):
        return False
    if NOT_QUOTEISH.search(x):
        return False
    if '·' in x or '•' in x:
        return False
    words = re.findall(r"[A-Za-z][A-Za-z']*", x)
    if sum(c.isascii() and c.isalpha() for c in x) < 8:
        return False
    return len(words) >= 3


def load_chapters(book):
    out = {}
    for p in sorted(glob.glob(os.path.join(book, 'text', '*.txt'))):
        m = re.match(r'ch(\d+)([a-z]?)', os.path.basename(p))
        if m:
            # 2026-09-28：键带字母后缀（'18'/'18a'），与 check_vocab 对齐
            out[str(int(m.group(1))) + m.group(2)] = flat_alpha(
                open(p, encoding='utf-8', errors='ignore').read())
    return out


def suffix_match(seg, allflat):
    """seg 去掉前 k 个词后能否命中（k=1..词数-1）。

    抓的是**段内拼接**：叙述标签被删导致的前缀错位，如
      原书 `Not entirely,' Sam said, "still means you lied. To me.`
      md   `'Not entirely,' still means you lied. To me.`
    整段比对与按句切两段都救不了——切分点落在段**内部**。只能逐词丢前缀试。
    """
    toks = re.findall(r"[A-Za-z][A-Za-z']*", seg)
    for k in range(1, len(toks)):
        cand = ' '.join(toks[k:])
        if len(cand) >= 12 and flat_alpha(cand) in allflat:
            return k
    return 0


def halves(q):
    """按句末标点**与省略号**切分，返回**原文**片段（不是 flat 串）。

    ⚠️ 必须返回原文：`suffix_match` 要按词切分做「丢前缀」搜索，若这里已 flat
    成 `notentirelystillmeansyoulied`，词数恒为 1、k 循环体永不执行 →
    段内拼接永远抓不到（第一版即如此，what-grows 概述:50 漏网）。

    ⚠️ 只按 `.!?…` 切会漏掉两类：① 片段以 `…` 表示省略；② 片段以逗号/破折号
    **悬空结尾**（`It shouldn't have reduced me to atoms where I stood,`）——
    中间被换掉的部分不在片段里，须额外试「去掉末段」的变体。
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


def label_near(line, span_start, span_end):
    """取引语**紧邻**的章节标签。

    ⚠️ **不能取整行第一个 `chNN`**——总览里一行常出现多个章号，且第一个往往属于
    别的句子。实测两处假红：
      `- **呼应关系**：ch07 章题 "…" 的兑现；ch02 的 "What are the odds of that!"`
        → 整行第一个是 ch07，但引语属 ch02
      `| 两颗珍珠 | ch02 祖母的比喻 | … ch27 Ursula 复述"two pearls in a single oyster" |`
        → 整行第一个是 ch02，但引语属 ch27
    故只看引语**前 40 字**窗口内的 chNN（标签惯例是紧贴引语写），没有再看后 20 字；
    且窗口内取**最后一个**——两种写法（`出处：chNN —— "…"` 与
    `…ch27 Ursula 复述"…"`）标签都在引语紧前方，取第一个会拿到同一行里更早的
    那个章号（实测 forgotten-sisters 概述:106 报到 ch18、真值是 ch27）。
    """
    pre = line[max(0, span_start - 40):span_start]
    found = RE_LABEL.findall(pre)
    if found:
        return int(found[-1])
    post = line[span_end:span_end + 20]
    m = RE_LABEL.search(post)
    return int(m.group(1)) if m else None


def main():
    args = sys.argv[1:]
    quiet = '--quiet' in args
    pos = [a for a in args if not a.startswith('--')]
    if not pos:
        raise SystemExit('用法: check_overview_full.py "<书目录>" [--quiet]')
    book = pos[0]
    ovs = sorted(glob.glob(os.path.join(book, '0*.md')))
    if not ovs:
        print('=== 总览整串核查（%s）===' % os.path.basename(book.rstrip('/')))
        print('  该书无 0*.md 总览文件。')
        print('  ⚠️ 注意：**短篇合集豁免总览三篇**（§10.5 第 4 维），缺总览不算缺陷；')
        print('     但若本应有总览而缺失，请人工确认体裁。')
        return 2
    chapters = load_chapters(book)
    epaths = sorted(glob.glob(os.path.join(book, 'library', '*.epub')))
    if not chapters and not epaths:
        print('=== 总览整串核查（%s）===' % os.path.basename(book.rstrip('/')))
        print('  ❓ **无法判定**：无 text/ 且无 library/*.epub —— 无参照集。')
        print('     本脚本是**条件性工具**，epub 清理后应从门禁清单撤下。')
        return 2
    allflat = ''.join(chapters.values())
    if not allflat and epaths:
        allflat = flat_alpha(epub_flat_text(epaths[0]))

    n_ok = n_nolabel = n_short = n_splice = n_miss = n_ellipsis = 0
    n_label_ok = n_label_bad = n_label_undet = n_multi = 0
    problems = []
    for md in ovs:
        name = os.path.basename(md)
        lines = open(md, encoding='utf-8', errors='ignore').read().split('\n')
        # ── E. H1 语义校验
        h1 = next((l[2:].strip() for l in lines if l.startswith('# ')), '')
        for key, words in H1_EXPECT.items():
            if key in name and not any(w in h1 for w in words):
                problems.append(('E', name, 1,
                                 'H1「%s」与文件名「%s」语义不符 —— 疑似整文件写错'
                                 % (h1[:34], name)))
        in_fm = False
        for i, ln in enumerate(lines, 1):
            s = ln.strip()
            if i == 1 and s == '---':
                in_fm = True
                continue
            if in_fm:
                in_fm = s != '---'
                continue
            for m in SPAN.finditer(ln):
                frag = m.group(1) or m.group(2) or m.group(3) or ''
                if not is_quoteish(frag):
                    continue
                fq = flat_alpha(frag)
                # ── D. 短引语列出
                if len(fq) < 20:
                    n_short += 1
                    continue
                # ── A. 整串 flat
                if fq in allflat:
                    n_ok += 1
                else:
                    seg = halves(frag)
                    if len(seg) > 1 and all(flat_alpha(x) in allflat for x in seg if x):
                        n_splice += 1
                        problems.append(('A', name, i, '跨标签拼接：%s' % frag[:50]))
                        continue
                    if any(suffix_match(x, allflat) for x in seg if x):
                        n_splice += 1
                        problems.append(('A', name, i,
                                         '段内拼接（叙述标签被删）：%s' % frag[:50]))
                        continue
                    if re.search(r'…|\.\.\.', frag):
                        # **省略号片段不判红**——`didn't matter whether … or …` 是
                        # **图式引语**（用省略号表示可变槽位），本就不是逐字引用。
                        # AGENTS 的逐字要求针对引语行，不针对总览里的句式模板。
                        n_ellipsis += 1
                        problems.append(('A', name, i,
                                         '省略号图式引语，无法整串验证，待人核：%s'
                                         % frag[:46]))
                        continue
                    n_miss += 1
                    problems.append(('A', name, i, '全书查无：%s' % frag[:52]))
                    continue
                # ── B/C. 章节标签对账（标签须取**紧邻引语**的那个 chNN）
                lab = label_near(ln, m.start(), m.end())
                if lab is None:
                    n_nolabel += 1
                elif not chapters:
                    n_label_undet += 1          # 只有 epub，不能定章
                else:
                    where = [k for k, v in chapters.items() if fq in v]
                    # ⚠️ 2026-09-28 修正：`chapters` 的键是**字符串**（load_chapters
                    # 里 str(int(...))），而 `label_near` 返回 **int** ⇒ `lab in where`
                    # 恒为 False，**每一条章节标签都被误报成「标注与实章不符」**
                    # （本库实测 41/41 全红，且提示语自相矛盾：「标注 ch1 …（实为 ch1）」）。
                    # 属假红型：先修工具，不许据此改 md。
                    if str(lab) in where:
                        n_label_ok += 1
                    else:
                        n_label_bad += 1
                        _where_s = (','.join('ch%s' % k for k in where[:4])
                                    if where else '全书无')
                        problems.append(('B', name, i,
                                         '标注 ch%s 但引语不在该章（实为 %s）：%s'
                                         % (lab, _where_s, frag[:40])))
                    if len(where) > 1:
                        n_multi += 1
                        problems.append(('C', name, i,
                                         '同一句在 %d 章出现（%s），章节标注有歧义：%s'
                                         % (len(where),
                                            ','.join('ch%s' % k for k in where[:4]),
                                            frag[:36])))

    print('=== 总览整串核查（%s）===' % os.path.basename(book.rstrip('/')))
    print('  参照集：%s ｜ 总览文件 %d 个'
          % ('text/ 逐章（%d 章）' % len(chapters) if chapters else 'epub 整书（不能定章）',
             len(ovs)))
    print('  A 整串：命中 %d ｜ 🔶 拼接 %d ｜ ⚪ 省略号图式 %d ｜ ❌ 查无 %d ｜ 短引语列出 %d'
          % (n_ok, n_splice, n_ellipsis, n_miss, n_short))
    print('  B 章节标签：对 %d ｜ 标注与实章不符 %d（**只报不判红**：分不清真错标与'
          '有意的相关章引用）｜ 无标签未判 %d ｜ 无法判定(无逐章参照) %d'
          % (n_label_ok, n_label_bad, n_nolabel, n_label_undet))
    print('  C 跨章多重命中：%d ｜ E H1 语义错配：%d'
          % (n_multi, sum(1 for p in problems if p[0] == 'E')))
    if not quiet:
        for kind, name, ln, msg in problems:
            print('  %s %s:%d  %s' % ({'A': '⚠️', 'B': '⚠️', 'C': '⚠️', 'E': '❌'}[kind],
                                      name[:30], ln, msg))
    # ⚠️ **B（章节标签错）只报不判红**——机械上分不清两种情况：
    #   ① 真错标：引语在 ch29、标成 ch02
    #   ② **有意的相关章引用**：`「不够怕」是 ch25 里母亲那句判断的回声`——
    #      引的是「相关章」而非「字面出处」，这是分析行为、不是缺陷
    #      （the-morningside 金句精选:152 实证）。故只列出让 人判，退出码不因此为 1。
    n_err = sum(1 for p in problems if p[0] == 'E') + n_miss
    return 1 if n_err else 0


if __name__ == '__main__':
    sys.exit(main())
