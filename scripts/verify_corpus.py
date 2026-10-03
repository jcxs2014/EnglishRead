#!/usr/bin/env python3
"""
verify_corpus.py — 语料层（text/）验收门禁 = 方案 P0-0

为什么需要（方案 §10.1 Open Secrets 实证）
--------------------------------------------
`check_chapter_quotes` / `verify_quotes` / `audit_book.py` A2 **全部以 text/ 为真值**。
若 extract 边界错误把两篇合并进一个文件，则：
  - `check_chapter_quotes` 79/79 全绿——引语确实在"那一章"的 text 里（两个故事都在）
  - `verify_quotes` 对 epub 全文匹配也绿——内容确实都在 epub 里
  - `audit_book.py` A2「text/ vs epub 一致性抽检」也拦不住——它防**内容保真**，不防**归属边界**
即：**这一层错了，下面所有门禁的绿都是假的。**

四项检查
--------
① 件数对账      —— 件数 vs 预期篇目数（--expect N，或 --expect-from 说明预期数来源）
② 人物锚点双向  —— 本篇人物应 >0；相邻篇人物应 =0。锚点须用**该篇独有实体**
                   （--anchors "ch01=Alice,Bob; ch02=Carol"），禁用泛名
③ 首末句抽印    —— 打印每件首句/末句供人工过目（抓"从句中间开始/句中间结束"）
④ 字面转义符体检 —— 检出 text/ 里的字面 \n \t 与 LaTeX 命令（方案 §11.3 注记一）

用法
----
    # 最小：件数 + 首末句 + 转义符体检
    python3 scripts/verify_corpus.py "<书目录>"

    # 声明预期篇目数（来源必须同时说明，见 §11.3 提醒 1）
    python3 scripts/verify_corpus.py "<书目录>" --expect 8 --expect-source "epub spine + 目录页"

    # 人物锚点双向 grep（短篇集/分部书/多 POV 必跑）
    python3 scripts/verify_corpus.py "<书目录>" --expect 8 \
        --anchors "ch01=Louisa,Jack Agnew; ch02=Dorrie,Millicent"

    # 首末句各打印 N 句
    python3 scripts/verify_corpus.py "<书目录>" --edges 2

退出码
------
    0  全部检查通过（或仅 WARN）
    1  有 FAIL
    2  参数/环境错误

设计约束（方案 §6.1 / §8.6 / §11.3 注记一）
------------------------------------------
- **词边界匹配**，不做子串判定（子串会让"首词被吞"这类缺陷静默通过）
- **锚点查无 = FAIL 而非 WARN**：宁可假红不可假绿（§8.6「校验规则本身也会造假绿」）
- 同一位置/标签须回源核对，本脚本对每个判定打印可复现依据
- 启用前须先在**已知良好的书**上跑对照（§六.1）
"""
import argparse
import os
import re
import sys

# ⚠️ 后缀字母不可丢：`ch02a` 归一成 int(2) 会与 `ch02` 撞键，
# 后者静默覆盖前者（corpus 少一件）且锚点指向错误的 text/。
TEXT_RE = re.compile(r'^ch(\d+)([a-z]?)')


def chapter_key(digits, suffix=''):
    """统一键：'02' / '02a'。字符串键保证 sorted() 顺序正确（'02' < '02a' < '03'）。"""
    return '%02d%s' % (int(digits), suffix or '')
# 字面转义符：反斜杠 + n/t（非行尾的真实换行不算）
LITERAL_ESC = re.compile(r'\\[nt]')
# LaTeX 命令：\alpha \beta \nabla \text \frac ...
LATEX_CMD = re.compile(r'\\[A-Za-z]{2,}')
# 页码 bleed：数字紧贴单词（Profile Books 式 2Association / to 7describe）
PAGE_BLEED = re.compile(r'[A-Za-z]{3,}\d{1,3}[A-Za-z]|\b\d{1,3}[A-Za-z]{3,}')


def norm(s):
    """归一化但**保留单词边界**：非字母数字一律换成空格并折叠。

    ⚠️ 不可用 flat（删空格）做存在性判定——flat 串里每个字符都是字母数字，
    词边界判定恒为假，词尾不在语料末尾就一律查无（第一版 has_token 的死法）。
    锚点判定必须走 norm + lookaround 边界。
    """
    return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()


def find_texts(book_dir):
    """返回 [(NN, path)]，按章号排序。"""
    tdir = os.path.join(book_dir, 'text')
    if not os.path.isdir(tdir):
        return None
    out = []
    for f in os.listdir(tdir):
        if not f.endswith('.txt'):
            continue
        m = TEXT_RE.match(f)
        if m:
            out.append((chapter_key(m.group(1), m.group(2)), os.path.join(tdir, f)))
    return sorted(out)


def sentences(text):
    """粗切句：句末标点或换行即断。用于首末句抽印（不追求语言学精确）。"""
    parts = [p.strip() for p in re.split(r'(?<=[.!?…])\s+|\n+', text) if p.strip()]
    return parts or [text.strip()]


def parse_anchors(spec):
    """'ch01=A,B; ch02=C' -> {1: ['A','B'], 2: ['C']}"""
    out = {}
    for chunk in spec.split(';'):
        chunk = chunk.strip()
        if not chunk or '=' not in chunk:
            continue
        key, names = chunk.split('=', 1)
        m = TEXT_RE.match(key.strip())
        if m:
            out[chapter_key(m.group(1), m.group(2))] = [
                n.strip() for n in names.split(',') if n.strip()]
    return out


def has_token(corpus_norm, token):
    """词边界存在性判定。两侧断言 (?<![a-z0-9]) / (?![a-z0-9]) 保证不靠子串蒙对。

    短 token（<4 字母）额外要求**逐词**命中，避免 'rod' 命中 'prod'、
    'Ann' 命中 'Anne'——连续连载主角的名字往往只有 3 个字母。
    """
    t = re.sub(r'[^a-z0-9]+', ' ', token.lower()).strip()
    if not t:
        return False
    if not re.search(r'(?<![a-z0-9])' + re.escape(t) + r'(?![a-z0-9])', corpus_norm):
        return False
    if len(t.replace(' ', '')) < 4:
        return re.search(r'(?<![a-z0-9])' + re.escape(t) + r'(?![a-z0-9])', corpus_norm) is not None
    return True


def main():
    ap = argparse.ArgumentParser(description='语料层（text/）验收门禁 = 方案 P0-0')
    ap.add_argument('book_dir')
    ap.add_argument('--expect', type=int, default=None, help='预期篇目数')
    ap.add_argument('--expect-source', default='', help='预期篇目数的来源（必须写）')
    ap.add_argument('--anchors', default='', help='人物锚点："ch01=Alice,Bob; ch02=Carol"')
    ap.add_argument('--shared', default='',
                    help='合法跨篇共有人物（连载主角等），逗号分隔，豁免泄漏告警')
    ap.add_argument('--edges', type=int, default=1, help='每件首/末各打印几句')
    ap.add_argument('--quiet-edges', action='store_true', help='不打印首末句（批量模式）')
    args = ap.parse_args()

    texts = find_texts(args.book_dir)
    if texts is None:
        print('ERROR: 找不到 %s/text/' % args.book_dir, file=sys.stderr)
        return 2

    book = os.path.basename(args.book_dir.rstrip('/'))
    fails, warns = [], []
    print('=== 语料层验收（P0-0）: %s ===' % book)
    print('text/ 件数: %d' % len(texts))

    # ---- ① 件数对账 ----
    if args.expect is not None:
        if len(texts) == args.expect:
            print('  [1] 件数 %d == 预期 %d  OK' % (len(texts), args.expect))
        else:
            fails.append('件数 %d != 预期 %d（来源：%s）'
                          % (len(texts), args.expect, args.expect_source or '未说明'))
            print('  [1] 件数 %d != 预期 %d  FAIL' % (len(texts), args.expect))
    else:
        warns.append('未给 --expect：件数未对账。**"件数=自己数出来的"等于没验**'
                    '（Open Secrets 即 6 件=6 篇的自洽假象）')
        print('  [1] 未给 --expect，跳过件数对账  WARN')

    if args.expect is not None and not args.expect_source:
        warns.append('给了 --expect 但未给 --expect-source：预期数来源必须写明')

    # ---- 读取 + ②③ 预载 ----
    corpus = {}
    for nn, p in texts:
        corpus[nn] = open(p, encoding='utf-8', errors='ignore').read()

    # ---- ④ 字面转义符 / LaTeX / 页码 bleed 体检 ----
    lit_hit, tex_hit, bleed_hit = [], [], []
    for nn, p in texts:
        c = corpus[nn]
        if LITERAL_ESC.search(c):
            lit_hit.append(nn)
        if LATEX_CMD.search(c):
            tex_hit.append(nn)
        if PAGE_BLEED.search(c):
            bleed_hit.append(nn)
    if lit_hit or tex_hit:
        msg = []
        if lit_hit:
            msg.append('字面 \\n/\\t 于 ch%s' % ','.join(str(n) for n in lit_hit))
        if tex_hit:
            msg.append('LaTeX 命令于 ch%s' % ','.join(str(n) for n in tex_hit))
        warns.append('提取件含 %s → 该书须走人工比对，勿依赖纯脚本 flat '
                     '（方案 §11.3 注记一）' % '；'.join(msg))
        print('  [4] %s  WARN' % '；'.join(msg))
    else:
        print('  [4] 无字面转义符 / LaTeX 命令  OK')
    if bleed_hit:
        warns.append('疑似页码 bleed 于 %d 件（ch%s）——选句与例句须避开粘连点'
                     % (len(bleed_hit), ','.join(str(n) for n in bleed_hit[:8])))
        print('  [4b] 疑似页码 bleed %d 件  WARN' % len(bleed_hit))

    # ---- ② 人物锚点双向 ----
    if args.anchors:
        anchors = parse_anchors(args.anchors)
        shared = {n.strip().lower() for n in args.shared.split(',') if n.strip()}
        if not anchors:
            fails.append('--anchors 解析不出任何章（格式应为 "ch01=Alice,Bob; ch02=Carol"）')
        norm_all = {nn: norm(c) for nn, c in corpus.items()}
        miss_own, leak_other = [], []
        pairs = 0
        for nn, names in sorted(anchors.items()):
            if nn not in norm_all:
                fails.append('锚点指定 ch%s，但 text/ 无此件' % nn)
                continue
            for other_nn, other_names in sorted(anchors.items()):
                if other_nn == nn:
                    continue
                pairs += 1
                for nm in other_names:
                    if nm in names or nm.lower() in shared:
                        continue
                    if has_token(norm_all[nn], nm):
                        leak_other.append('ch%s 本篇含他篇 ch%s 的人物「%s」'
                                          '（长篇里角色跨章出现属正常；续章人物请用 --shared 豁免）'
                                          % (nn, other_nn, nm))
            for nm in names:
                if not has_token(norm_all[nn], nm):
                    miss_own.append('ch%s 未命中本篇人物「%s」' % (nn, nm))
        for x in leak_other:
            fails.append(x)
        for x in miss_own:
            fails.append(x)
        print('  [2] 人物锚点双向：本篇 %d 组 / 互查 %d 组%s  %s'
              % (len(anchors), pairs,
                 '（共享人物 %d 个已豁免）' % len(shared) if shared else '',
                 'FAIL' if (leak_other or miss_own) else 'OK'))
    else:
        warns.append('未给 --anchors：**本篇人物应 >0 / 相邻篇人物应 =0** 未验——'
                     '合并事故只能靠这一项抓（短篇集/分部书/多 POV/日历书必跑）')
        print('  [2] 未给 --anchors，跳过人物锚点双向  WARN')

    # ---- ③ 首末句抽印 ----
    if not args.quiet_edges:
        print('  [3] 首末句抽印（人工过目：抓"从句中间开始/句中间结束"的边界错位）')
        for nn, p in texts:
            sents = sentences(corpus[nn])
            head = sents[:args.edges]
            tail = sents[-args.edges:] if len(sents) > args.edges else sents
            print('    ch%s (%d 句)' % (nn, len(sents)))
            for s in head:
                print('      首| %s' % s[:96])
            for s in tail:
                print('      末| %s' % s[:96])
    else:
        print('  [3] 首末句抽印已跳过（--quiet-edges）')

    # ---- 汇总 ----
    print()
    for w in warns:
        print('WARN  %s' % w)
    for f in fails:
        print('FAIL  %s' % f)
    print('\n=== P0-0 语料验收: %s（FAIL %d / WARN %d）===' % ('PASS' if not fails else 'FAIL', len(fails), len(warns)))
    if fails:
        print('**这一层不过，下面所有门禁的绿都是假的**（方案 §10.1）')
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
