#!/usr/bin/env python3
"""
lk_verify_batch.py — 批内逐条引语/例句的**原始串**（不规范化）逐字核验器

为什么需要它（三个已知盲区，本脚本逐个封）
------------------------------------------------
1. **子串式门禁普遍做空白/引号规范化** ⇒ U+200A ↔ U+0020、弯引号 ↔ 直引号这类替换
   在 verify_quotes / sweep_full / check_chapter_quotes 全部绿灯下通过
   （Jenny 批次 ch06 实测 6 道门禁全绿仍漏 U+200A）。
   ⇒ 本脚本 `q in text`，**不做任何规范化**；命中失败时再按 `flat` 试一次并
   **分类命名**（[空白类] / [真查无]），诊断信息必须能区分这两者。

2. **词表例句不在 verify_quotes 口径内** ⇒ 词表层必须单独核。

3. **中文分析层（中文理解/导航/读者提示）是全库系统性盲区** ⇒ sweep_analysis_inline
   的「内容词全命中」判据放过代词/冠词/介词替换（she→he 全绿）。
   ⇒ 中文理解行里的**引号英文**同样逐字核。

用法
----
    python3 scripts/lk_verify_batch.py <ch01> [ch02 ...]   # 章号或 md 文件名均可
    python3 scripts/lk_verify_batch.py --self-test          # 投毒自证（正门在提交前必跑）

退出码：0 = 全通过；1 = 有真查无；2 = 参数/环境错误。
"""
import os
import re
import sys
import glob

BOOK = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'notes', 'books', 'short-story-anthologies',
                    'the-language-of-knives-by-haralambi-markov')

# 引语块：> **原句 N:** "..."
RE_QUOTE = re.compile(r'^>\s*\*\*原句\s+(\d+):\*\*\s*(.+?)\s*$', re.M)
# 词表行：| 词头 | 释义 | 例句 |
RE_VOCAB = re.compile(r'^\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*$', re.M)
RE_TIER = re.compile(r'^###\s*(⭐⭐⭐|⭐⭐|⭐)\s*(\S+)?')
# 中文层里带引号的英文片段（直引号 / 弯引号都收）
RE_ZH_INLINE = re.compile(r'[\"“]([^\"”]{8,})[\"”]')
# 不可核的计数断言（禁令 D5）
# ⚠️ **「一」不进数词表**（自写尺子的第一版假红）：中文「一个分句/一个词」绝大多数是
#   **不定冠词**不是计数（实测 ch01:84「where 与 what 各辖一个分句」被当计数断言报警）。
#   代价：「一个词」作为真计数时查不到——按 AGENTS 三档归**提示型（漏报可接受）**，
#   而把冠词当计数会让「照单全改」改坏正当内容（the-glass-girl ch07 教训）。
RE_NUM = r'([二三四五六七八九十两半]|\d+)'
RE_COUNT = re.compile(RE_NUM + r'\s*个(?:词|分句|字符|句读|英文字母)')
# ⚠️ **序数指代不是计数断言**：「第二个分句」「第三次出现」是在指位置，
#   而 D5 禁的是「N 个词」这类可数规模的断言 ⇒ 用否定后视排除「第+数词+量词」。
RE_COUNT_ORD = re.compile(r'第\s*' + RE_NUM + r'\s*个')
# 最高级断言（禁令 D6）
RE_SUPER = re.compile(r'全书唯一|唯一一次|第一次|全书中?最(?:大|多|早|高|深|好|美|强)|'
                      r'史上唯一|前所未有')
# 禁写标注（禁令 D4）
RE_FORBID = re.compile(r'未出现在原文|本章未出现|见工具输出|未见于原文|（本章无|待补|占位')


def norm_flat(s):
    return re.sub(r'[^a-z0-9]+', '', s.lower())


def chapter_path(nn):
    """nn 形如 'ch01' 或 '01'。返回 (md_path, txt_path) 或 None。"""
    m = re.match(r'^(?:ch)?(\d+)$', nn)
    if not m:
        return None
    key = int(m.group(1))
    # ⚠️ text/ 文件名是 `ch01_<slug>.txt`（**下划线**分隔），不是 `ch01.txt`
    # ——第一版正则写成 `^ch0*NN\.txt$`，glob 恒空 ⇒ self-test 报「找不到 text 文件」。
    # 「报告为 0/异常先怀疑量具」的第一个实例。
    txts = [f for f in glob.glob(os.path.join(BOOK, 'text', 'ch*.txt'))
            if re.match(r'^ch0*%d[a-z]?[_.]' % key, os.path.basename(f))]
    mds = [f for f in glob.glob(os.path.join(BOOK, 'ch*.md'))
           if re.match(r'^ch0*%d[a-z]? ' % key, os.path.basename(f))]
    if not txts or not mds:
        return None
    return mds[0], txts[0]


def unwrap(q):
    """剥掉引语块外层包裹的引号（不做内部规范化）。"""
    q = q.strip()
    while len(q) >= 2 and q[0] in '"“”' and q[-1] in '"“”':
        q = q[1:-1]
    return q


RE_CJK = re.compile(r'[\u3400-\u9fff\u3040-\u30ff]')
# 中英混排片段里要单独核的 ASCII 连续段（弯引号/弯撇号也算 ASCII 词的一部分，
# 否则 can't / “Don't 会被从中间切开）
RE_ASCII_RUN = re.compile("[A-Za-z0-9][A-Za-z0-9 ,.;:!?\\u2019\\u201c\\u201d\\-]*")

_LAST_CATS = {}   # self-test 读它做逐类断言


def check(label, seg, corpus):
    """原始串优先；失败再试 flat。返回 (kind, detail)。"""
    if seg in corpus:
        return None, ''
    fs = norm_flat(seg)
    # ⚠️⚠️ **flat 比对对中文完全不可见**（self-test 抓到的第三个盲区）：
    # `norm_flat` 把 CJK 全删掉 ⇒「原句 + 追加一句中文」的 flat 串与原句的 flat 串
    # **完全相同**，空串更是恒真于任何串 ⇒ 追加/改写中文会被误判成「空白类」。
    # ⇒ 只要片段含 CJK，flat 通道一律不作为通过依据。
    if RE_CJK.search(seg):
        return '真查无', f'（片段含中文 ⇒ flat 通道不可用，不做空白类豁免）'
    # ⚠️ **合法省略**：`…` 两侧各自都是原文的连续片段（禁令 D5 允许，且常用）。
    #   缺这一条时，中文层里每处合法省略都会报「空白/变音类」⇒ 假红淹没真缺陷
    #   （ch01 实测 2 处：`… that opposes…` / `… what will be left…?` 全是合法省略）。
    if '…' in seg or '...' in seg:
        parts = [p for p in re.split(r'…|\.\.\.', seg) if p.strip()]
        fc = norm_flat(corpus)
        if all(p.strip() and norm_flat(p.strip()) in fc for p in parts):
            return None, ''      # 合法省略，放行
        return '真查无', f'省略号某一侧不是原文连续片段（{parts}）'
    if fs and fs in norm_flat(corpus):
        # ⚠️ **不要把 flat 偏移量当原文偏移量去切片**——两者坐标系不同，
        #   切出来的「原文=」是另一处的文本，会把人引向完全错误的行（第一版就这么写）。
        i = norm_flat(corpus).find(fs)
        ctx = norm_flat(corpus)[max(0, i - 30):i + len(fs) + 30]
        return '空白/变音类', f'flat 命中但原始串不命中｜flat 上下文={ctx!r}'
    return '真查无', ''


def verify_one(nn, verbose=True, verbose_zh=None):
    # nn 可以是章号，也可以是 md 的**完整路径**（self-test 必须走路径：
    # 同章号存在两个 md 时，glob 顺序不定 → 会验到真文件而不是投毒文件，
    # 于是「self-test 全绿」其实验的是上一章）。
    if os.path.sep in nn or nn.endswith('.md'):
        md_p = nn
        m = re.match(r'^ch0*(\d+)', os.path.basename(md_p))
        if not m:
            print(f'❌ {nn}: 文件名不以 chNN 开头')
            return 1
        txts = [f for f in glob.glob(os.path.join(BOOK, 'text', 'ch*.txt'))
                if re.match(r'^ch0*%d[a-z]?[_.]' % int(m.group(1)), os.path.basename(f))]
        if not txts:
            print(f'❌ {nn}: 找不到对应 text/')
            return 1
        hit = (md_p, txts[0])
    else:
        hit = chapter_path(nn)
    if not hit:
        print(f'❌ {nn}: 找不到 md 或 text 文件')
        return 1
    md_p, txt_p = hit
    md = open(md_p, encoding='utf-8').read()
    corpus = open(txt_p, encoding='utf-8').read()
    problems = []

    # ① 引语块（逐字 + 编号连续）
    quotes = RE_QUOTE.findall(md)
    if not quotes:
        problems.append(('结构', '未提取到任何 `> **原句 N:**` 引语块'))
    nums = [int(n) for n, _ in quotes]
    if nums and nums != list(range(1, len(nums) + 1)):
        problems.append(('结构', f'引语编号不连续: {nums}'))
    for n, raw in quotes:
        seg = unwrap(raw)
        kind, detail = check('quote', seg, corpus)
        if kind:
            problems.append(('引语', f'原句 {n}: [{kind}] {seg[:110]!r} {detail}'))

    # ② 引语是否跨自然段（禁令 D2）
    for n, raw in quotes:
        seg = unwrap(raw)
        if '…' in seg or '...' in seg:
            halves = [s for s in re.split(r'…|\.\.\.', seg) if s.strip()]
            ok = all(h.strip() in corpus for h in halves)
            if not ok:
                problems.append(('引语', f'原句 {n}: 省略号两侧有非原词片段'))

    # ③ 词表例句（逐字；分三档，跨档例句不得重复）
    tier, rows, seen = None, [], {}
    for line in md.split('\n'):
        mt = RE_TIER.match(line)
        if mt:
            tier = mt.group(1)
            continue
        mv = RE_VOCAB.match(line)
        if not mv or set(line.replace('|', '').strip()) <= {'-', ':'}:
            continue
        head, gloss, sent = mv.group(1), mv.group(2), mv.group(3)
        if head in ('词/短语', '词汇', '词', '---') or set(head) <= {'-'}:
            continue
        rows.append((tier, head.strip(), gloss.strip(), sent.strip(), line))
    if not rows:
        problems.append(('词表', '未提取到任何词表行'))
    for tier, head, gloss, sent, line in rows:
        if tier is None:
            problems.append(('词表', f'词条 {head!r} 不在任何档位下（档标题须写 `### ⭐⭐⭐ 高级` 等带中文档名）'))
        if not gloss:
            problems.append(('词表', f'词条 {head!r} 释义列为空'))
        if not sent:
            problems.append(('词表', f'词条 {head!r} 例句为空/占位'))
        else:
            key = norm_flat(sent)
            if key in seen:
                problems.append(('词表', f'词条 {head!r} 例句与 {seen[key]} 重复'))
            seen[key] = head
            kind, detail = check('example', sent, corpus)
            if kind:
                problems.append(('词表', f'词条 {head!r} 例句: [{kind}] {sent[:90]!r} {detail}'))
        # 词头须在本章出现（词边界）
        if not re.search(r'(?<![A-Za-z])' + re.escape(head.split()[0].rstrip('.,;:')) +
                         r'(?![A-Za-z])', corpus, re.I):
            problems.append(('词表', f'词条 {head!r} 词头在本章 text/ 查无'))

    # ④ 中文层引号内英文（she→he 这类代词替换的克星）
    # ⚠️⚠️ **第一版这里是死代码**：只把片段 append 进 zh_en、**从不调用 check()** ⇒
    #    中文层的伪造/非逐字英文一项都不报，而输出里的「中文层英文片段 N」看着像已覆盖。
    #    实证：ch01 整改时我用直撇号写 `I'm sorry...`（原文是弯撇号），
    #    本脚本报 0 报警；是 `grep -F` 人工核才抓到。
    #    ⇒ 自写检查器每加一段，都必须问「这一段的 check() 在哪一行」。
    zh_en = []
    in_fm = False          # frontmatter 必跳过：`modified: "2026-10-06"` 会被当成中文层英文片段
    for line in md.split('\n'):
        if line.strip() == '---':
            in_fm = not in_fm
            continue
        if in_fm:
            continue
        if line.startswith('>') or RE_VOCAB.match(line) or line.startswith('|'):
            continue
        for seg in RE_ZH_INLINE.findall(line):
            # ⚠️ **中英混排片段要按 ASCII 段拆**（实测假红两类）：
            #   ① 引号正则跨引号边界，把「中文句子＋中间的英文引语」整段当一个片段，
            #      而整段含中文 ⇒ 第一版一律判真查无 ⇒ 把**合法**的英文引语误报成缺陷；
            #   ② 修正后只取片段里的 ASCII 连续段（≥20 flat 字符）逐段核。
            pieces = [seg] if not RE_CJK.search(seg) else \
                     [p for p in RE_ASCII_RUN.findall(seg) if len(norm_flat(p)) >= 20]
            for piece in pieces:
                piece = piece.strip()      # 首尾空白不是原文差异，否则报假红
                zh_en.append((line[:40], piece))
                kind, detail = check('zh', piece, corpus)
                if kind:
                    problems.append(('中文层', f'{kind} {piece[:90]!r} {detail}'))
    if verbose_zh is not None and not zh_en:
        problems.append(('中文层', f'未抽到任何引号内英文片段（传入 --require-zh-en）'))

    # ⑤ 禁令扫描
    for i, line in enumerate(md.split('\n'), 1):
        for rx, tag, msg in ((RE_COUNT, '禁令D5', '不可核的计数断言'),
                             (RE_SUPER, '禁令D6', '最高级/唯一断言'),
                             (RE_FORBID, '禁令D4', '禁写标注')):
            m = rx.search(line)
            if not m:
                continue
            if tag == '禁令D5' and RE_COUNT_ORD.search(line):
                continue          # 「第二个分句」＝序数指代，提示型不改
            problems.append((tag, f'{msg}: {line.strip()[:100]}'))

    _LAST_CATS.clear()
    for c, _ in problems:
        _LAST_CATS[c] = _LAST_CATS.get(c, 0) + 1
    if verbose:
        print(f'\n── {os.path.basename(md_p)} ──')
        print(f'   引语块 {len(quotes)} ｜ 词表行 {len(rows)} ｜ 中文层英文片段 {len(zh_en)} ｜ '
              f'text/ {len(corpus)} 字符')
        if not problems:
            print('   ✅ 本脚本 0 报警')
        for cat, msg in problems:
            print(f'   [{cat}] {msg}')
    return len(problems)


def self_test():
    """投毒自证：证明本脚本会报，而不是恒绿。"""
    print('=== self-test（投毒验证：下列 5 类各应被报出）===')
    import tempfile
    good_txt = open(glob.glob(os.path.join(BOOK, 'text', 'ch01*.txt'))[0],
                    encoding='utf-8').read()
    line1 = next(l for l in good_txt.split('\n') if len(l) > 60)
    md = f'''---
状态: 未读
chapter: 1
---

# Poison

## 本篇导航

**一句话主旨**：这是全书唯一一次写最高级断言，另外有三个分句。

## 精读

> **原句 1:** "{line1}"

**中文理解**：见 {line1[:40]}
**句子结构**：见 "this is a fabricated english fragment that does not exist at all"
**关键词**：*line1*
**表达方式**：见 “another fabricated quote used only for poison testing purposes”
**为什么这样写**：见 `the original text has three clauses`

---

> **原句 3:** "{line1} 但多了一句不存在的话"

**中文理解**：x
**句子结构**：x
**关键词**：x
**表达方式**：x
**为什么这样写**：x

## 词汇分级

### ⭐⭐⭐ 高级
| 词/短语 | 释义 | 例句 |
|---|---|---|
| nonexistentword | 虚构词 | this example sentence is definitely fabricated |
| line1 | 测试 | （本章未出现该词） |

## 一句话总结
x
'''
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md)
        tmp = f.name
    # 让 chapter_path 找到它：临时放进书目录
    target = os.path.join(BOOK, 'ch01 poison selftest.md')
    os.replace(tmp, target)
    try:
        n = verify_one(target)   # 按**路径**验投毒文件，不按章号
        # ⚠️ 逐类断言：只数总数会漏「某一段是死代码」——第一版正是如此，
        # 中文层那一段从未调用 check()，总数却已 ≥6，看起来完全正常。
        import importlib
        mod = importlib.import_module('lk_verify_batch') if False else None
        cats = globals().get('_LAST_CATS', {})
        need = {'结构': 1, '引语': 1, '词表': 2, '禁令D4': 1, '禁令D5': 1, '禁令D6': 1, '中文层': 1}
        print('\n逐类自证（每类都必须 ≥1，证明没有死代码段）：')
        ok = True
        for c, k in need.items():
            got = cats.get(c, 0)
            flag = 'OK ' if got >= k else '❌ '
            if got < k:
                ok = False
            print(f'  {flag}{c}: 报出 {got}（要求 ≥{k}）')
        print(f'\nself-test 报出问题数 = {n}')
        print('self-test 结论：', '✅ 每类都报得出，本脚本各段均非死代码' if ok else '❌ 存在死代码段，禁止用于验收')
    finally:
        os.remove(target)
    print('self-test 结论：', '✅ 本脚本会报，可用作门禁尺子' if ok else '❌ self-test 失败，脚本疑似死代码，禁止用于验收')
    return 0 if ok else 1


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == '--self-test':
        return self_test()
    total = 0
    for nn in argv:
        total += verify_one(nn)
    print(f'\n=== lk_verify_batch：合计报警 {total} 项 ===')
    return 1 if total else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))