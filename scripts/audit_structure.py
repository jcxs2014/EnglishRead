#!/usr/bin/env python3
"""
audit_structure.py — 精读文件结构扫描（方案 P1 第 7 个脚本）

为什么需要
----------
`audit_book.py` 的 C 节「五子项齐全」对言情/精简格式（四子项）**系统性误报**，
AGENTS 盲区表明载，多本书完工通报写「C 节缺概览节是短篇合集格式已知误报，未据
此改动」。这是 WARN 疲劳的既成来源。若本脚本不做体裁分派，会把同样的事再犯一遍
（方案 §10.5）。

做法：画像匹配，而非硬性体裁判定
--------------------------------
不给每本书贴一个「体裁」标签再按标签查——那会在标签判错时整本误报（Lonely
Mouth 目录归 non-fiction、实为小说，260912 实证）。改为**每个文件只要满足
任一已知格式画像就算合规**，报「都不满足」时才指出最接近的那个缺什么。

这样 §10.5 要求的「**同书内格式漂移要容忍**」是天然成立的：8 个文件里
`**原句N:**`（无空格）与 `**原句 N:**` 并存，两种都认。**格式漂移不是缺陷，
硬套单一模板才是。**

四维分派（§10.5）
------------------
① 子项数：期刊/短篇=五子项；言情/精简=四子项；诗歌回忆录=五子项+诗歌技法专项
② 每章引语配额：期刊/短篇=10；言情/精简=3–8
③ 必备节名：各画像一套（`## 故事梗概` / `## 逐句精读` / `## 词汇分级` …）
④ 总览豁免：短篇合集无总览三篇（`00_概述.md` 等缺失不算缺陷）

另含（§10.4 / §10.6.1）
-----------------------
· **占位/垃圾行扫描**：`未见于原文`、`本章无此搭配`、`（未出现在原文）`、
  空例句列、整行重复（§10.4：Morningside 词表节**存在**但内容是数百行占位，
  「只查缺节」是它的漏网变体）
· **四方映射检查**：文件名 ↔ H1 ↔ `source_text` ↔ `text/` 件存在性
  （§10.6.1；Room 实证 19 个文件章节号偏高 1，集中在三段——这类偏移肉眼难辨）

用法
----
    python3 scripts/audit_structure.py "<书目录>" [--quiet]

退出码：有 ❌ 则 1；无 md 则 2。
"""
import glob
import os
import re
import sys

CIRCLED = '①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕'

# ── §10.4 占位/垃圾行（这些词本身就是「此处本该有真内容」的记号）
PLACEHOLDER_PAT = re.compile(
    r'未见于原文|本章无此搭配|未出现在原文|本章未出现|暂缺|待补|TODO|TBD')
# 词表行例句列为空 / 纯破折号
PLACEHOLDER_ROW = re.compile(r'^\s*\|[^|]*\|[^|]*\|\s*(?:—|-|—\s*)?\s*\|\s*$')

# ── 引语块起始行：容忍 `**原句N:**` 与 `**原句 N:**` 两种（§10.5 格式漂移）
RE_QUOTE_CIRCLED = re.compile(r'^\s*(?:>\s*)?\*{0,2}[' + CIRCLED + r']\*{0,2}\s*["“]?(.+?)["”]?\s*$')
RE_QUOTE_YUANJU = re.compile(r'^\s*>\s*\*{0,2}原句\s*\d+\s*[:：]?\*{0,2}\s*["“]?(.+?)["”]?\s*$')
RE_QUOTE_BARE = re.compile(r'^\s*>\s*(?!\*\*)(?![一-鿿])(.+?)\s*$')
RE_QUOTE_HEAD = re.compile(r'^#{2,4}\s*第\s*[0-9一二三四五六七八九十百廿卅]+\s*处[^「\n]*「([^」]+)」')
RE_KWLINE = re.compile(r'\*\*(?:关键词|Key\s?words?)\*{0,2}\s*[:：]')

# 子项名 → 归一（容忍 `**X：**` 与 `**X**：` 两种，§10.5）
SUBITEMS = {
    '中文理解': ('中文理解', '中文'),
    '句子结构': ('句子结构',),
    '关键词': ('关键词',),
    '表达方式': ('表达方式', '表达'),
    '为什么这样写': ('为什么这样写',),
    '读者视角提示': ('读者视角提示', '读者视角'),
}
# 注：**不再保留闭合画像表**。曾用「期刊五子项 / 言情四子项」两张固定表判合规，
# 结果 the-morningside（用 `**中文**`/`**情绪**` 自造标签）36 个文件报 35 个 ❌、
# 总览三件套被套正文章节画像凭空多报 16 个 ❌——**用外部模板套书正是 §10.5 警告的
# 失败模式**。改为按每本书自己的主流子项集判「书内不一致」。配额同理（用本书众数）。
# 必备节名：按「该书 ≥50% 文件都有」判定（check_vocab v4 的同款口径，
# 免得格式没统一的书写成「缺章节」）
SECTIONS_CORE = ['## 故事梗概', '## 逐句精读', '## 词汇分级']


def norm(s):
    return re.sub(r'\s+', ' ', s.replace('’', "'").replace('“', '"')
                  .replace('”', '"')).strip()


def quote_text(m):
    if not m:
        return None
    for v in m.groupdict().values() if m.groupdict() else m.groups():
        if v and v.strip():
            return v.strip()
    return None


def scan_quotes(lines):
    """扫引语块。返回 [(行号, 引语)]，用**命名 group 取非空值**——
    三分支拼接后 group(1) 只归属第一分支（check_anchor 已踩过，见其注释）。"""
    out = []
    for i, ln in enumerate(lines, 1):
        m = RE_QUOTE_CIRCLED.match(ln)
        t = quote_text(m)
        if t is None:
            t = quote_text(RE_QUOTE_YUANJU.match(ln))
        if t is None:
            t = quote_text(RE_QUOTE_BARE.match(ln))
        if t is None:
            mh = RE_QUOTE_HEAD.match(ln.strip())
            t = mh.group(1).strip() if mh else None
        if t and re.search(r'[A-Za-z]{3,}', t):
            out.append((i, t))
    return out


def blocks_of(lines, quotes):
    """按引语行切块：块 = 引语行 + 其后到下一引语行/标题之间的内容。"""
    qidx = {i for i, _ in quotes}
    blocks = []
    for i, ln in enumerate(lines, 1):
        if i not in qidx:
            continue
        seg = []
        j = i
        while j < len(lines):
            if j + 1 > i and ((j + 1) in qidx or re.match(r'^#{1,6}\s', lines[j])):
                break
            seg.append(lines[j])
            j += 1
        blocks.append((i, seg))
    return blocks


def has_subitem(blob, sub):
    """子项是否在块内出现。**容忍两种写法**（§10.5 格式漂移）：
       `**中文理解：**`（冒号在星号内）与 `**中文理解**：`（冒号在星号外）。"""
    for n in SUBITEMS[sub]:
        if re.search(r'\*\*\s*%s\s*\*{0,2}\s*[:：]' % re.escape(n), blob):
            return True
    return False


def profile_misses(blocks, subs):
    """返回该画像下缺哪些子项（并集）。"""
    miss = set()
    for _, seg in blocks:
        blob = '\n'.join(seg)
        for s in subs:
            if not has_subitem(blob, s):
                miss.add(s)
    return miss


# ── 通用子项标签发现：不预设书名/作者/格式，只认「标签 + 冒号」这个形状。
# **两种载体都要认**：`中文理解**：`（粗体）与 `中文理解：`（裸标签，行首）。
# 只认粗体会让 the-morningside 整本书推断不出子项 → **该书子项检查整个空跑、
# 报「0 缺陷」是真空通过**（实测其精读体全是裸标签）。
RE_ANY_LABEL = re.compile(
    r'\*\*\s*([^*\n]{2,10}?)\s*\*{0,2}\s*[:：]'
    r'|^\s*([^*\n]{2,10}?)\s*[:：]', re.M)   # ⚠️ 必须 re.M：裸标签靠 ^ 行首锚定，
                                           # 不加 M 时多行拼成的 blob 只有第一行能匹配
                                           # （实测 the-morningside 整本书只推出「中文理解」）
# 已知的非子项标签（书级/导航/元信息），不参与画像推断
NOT_SUBITEM = re.compile(
    r'^(状态|modified|created|title|作者|原书|出版|ISBN|来源|出处|导航|说明|注|备注|'
    r'摘要|背景|引用|参考|延伸|标签|类型|章节|文件|格式|未读|已读)')


def labels_in(blob):
    """块内出现的「标签 + 冒号」标签集（粗体与裸标签都认，已排除非子项标签）。

    **必须剥掉列表符号**——同书内 `- 中文理解：…`（bullet 体）与
    `中文理解：…`（行首体）是同一个子项，不剥就变成两个标签，
    bullet 体文件会误报「缺全部子项」（实测 until-august ch01 Preface）。
    """
    out = set()
    for m in RE_ANY_LABEL.finditer(blob):
        lab = (m.group(1) or m.group(2) or '').strip()
        lab = re.sub(r'^[-*+•]\s*', '', lab)          # 列表符号
        lab = re.sub(r'^\d{1,2}[.、)]\s*', '', lab)     # 有序列表编号
        lab = lab.strip(' 　')
        if not lab or NOT_SUBITEM.match(lab):
            continue
        out.add(lab)
    return out


def book_profile(mds):
    """推断**这本书自己的**主流子项集与引语配额——不用外部模板硬套。

    为什么要自己推断（§10.5 的失败模式换了个马甲）：
      · 闭合画像表会把**格式自成一派的书**判成「缺子项」——实测 the-morningside
        用 `**中文**` / `**情绪**` 等自造标签，在闭合表里一个都不匹配，36 个文件
        报 35 个 ❌；overview 三件套被拿去套正文章节画像，凭空多出 16 个 ❌
      · 而**真正的缺陷是「某个文件的块比同书兄弟块少了子项」**——那是**书内
        不一致**，用书自己的主流集合才抓得到，也才不冤枉格式自成一派的书
    """
    lab_count = {}
    per_file_blocks = []
    for md in mds:
        name = os.path.basename(md)
        body = open(md, encoding='utf-8', errors='ignore').read()
        lines = body.split('\n')
        qs = scan_quotes(lines)
        bl = blocks_of(lines, qs)
        per_file_blocks.append((name, qs, bl))
        # ⚠️ **总览文件不参与主流子项推断**——`00_金句精选` 的子项是
        # `上下文/呼应关系`、`00_情感节点` 的是 `为什么重要`，混进来后每个
        # 正文章节都显得「缺一半子项」（实测 until-august 9 个正文章节全被误判）
        if re.match(r'^0\d[_. ]', name) or name.startswith('00'):
            continue
        for _, seg in bl:
            for lab in labels_in('\n'.join(seg)):
                lab_count[lab] = lab_count.get(lab, 0) + 1
    n_blocks_all = sum(len(b) for nm, _, b in per_file_blocks
                      if not re.match(r'^0\d[_. ]', nm)) or 1
    # 主流子项 = 出现在 ≥15% 块里的标签（15% 而非 50%：一本书里常有
    # 导航/概览类块只带部分标签，用 50% 会把真子项也滤掉）
    core = {l for l, c in lab_count.items() if c >= 0.15 * n_blocks_all}
    # 引语配额：正文章节（非 00_*）每文件块数的众数
    counts = [len(q) for nm, q, _ in per_file_blocks
              if q and not re.match(r'^0\d[_. ]', nm)]
    quota = max(set(counts), key=counts.count) if counts else 0
    return core, quota, per_file_blocks, lab_count, n_blocks_all


def chap_no(text, pats):
    for p in pats:
        m = re.search(p, text)
        if m:
            return int(m.group(1))
    return None


ANALYSIS_SECTIONS = re.compile(r'精读|逐句|选择性精读|Quote|Analysis', re.I)
DIGEST_SECTIONS = re.compile(r'金句|关键引语|速览|摘录|Quote\s*List', re.I)


def in_analysis_section(lines, lineno):
    """该行是否落在「精读/逐句精读」类节内（往上找最近的 H2/H3）。

    用来区分**孤儿块**（精读节里有引语无分析 = 缺陷）与
    **摘录节的裸引语**（`### 核心金句` 下的 `> "..."` = 正常）。
    """
    for i in range(lineno - 1, -1, -1):
        h = re.match(r'^#{2,4}\s+(.*)$', lines[i])
        if h:
            t = h.group(1)
            if DIGEST_SECTIONS.search(t):
                return False
            return bool(ANALYSIS_SECTIONS.search(t))
    return False


def main():
    args = sys.argv[1:]
    quiet = '--quiet' in args
    pos = [a for a in args if not a.startswith('--')]
    if not pos:
        raise SystemExit('用法: audit_structure.py "<书目录>" [--quiet]')
    book = pos[0]
    mds = sorted(glob.glob(os.path.join(book, '*.md')))
    if not mds:
        print('该目录下无 md 文件：%s' % book)
        return 2
    has_text = bool(glob.glob(os.path.join(book, 'text', '*.txt')))

    # 推断**本书自己的**主流子项集与引语配额（不套外部模板，见 book_profile 注释）
    book_core, book_quota, per_file_blocks, lab_count, n_blocks_all = book_profile(mds)
    per_file_quota = {nm: len(q) for nm, q, _ in per_file_blocks}

    # 先统计各画像在全书的普及率（必备节名判定用 ≥50% 口径）
    sec_count = {}
    for md in mds:
        body = open(md, encoding='utf-8', errors='ignore').read()
        for s in SECTIONS_CORE:
            if s in body:
                sec_count[s] = sec_count.get(s, 0) + 1
    majority_secs = [s for s in SECTIONS_CORE if sec_count.get(s, 0) >= 0.5 * len(mds)]

    errs, warns, mapping = [], [], []
    n_files = n_blocks = 0
    for md in mds:
        name = os.path.basename(md)
        body = open(md, encoding='utf-8', errors='ignore').read()
        lines = body.split('\n')
        n_files += 1
        is_overview = bool(re.match(r'^0\d[_. ]', name)) or name.startswith('00')

        # ── A. 引语块与子项（画像匹配）
        quotes = scan_quotes(lines)
        blocks = blocks_of(lines, quotes)
        n_blocks += len(blocks)
        if quotes and not is_overview and book_core:
            # 块内子项数与同书主流比较——判「书内不一致」而不是「不符合外部模板」
            thin = []
            orphan = []
            for ln, seg in blocks:
                labs = labels_in('\n'.join(seg))
                if not labs:
                    # **零标签的块不是「缺子项」**——`### 核心金句` 这类摘录节里
                    # 本就是裸 `> "..."` 无分析（实测 one-way-back 45 个文件各 3 处，
                    # 全是这个）。但落在精读节内的零标签块是**孤儿块**（有引语无
                    # 任何分析），那是真缺陷。
                    if in_analysis_section(lines, ln):
                        orphan.append(ln)
                    continue
                missing = book_core - labs
                # 容忍块里只写部分子项：只在「缺 ≥半数」时提示
                if missing and len(missing) * 2 >= len(book_core):
                    thin.append((ln, '、'.join(sorted(missing))))
            for ln in orphan:
                errs.append((name, '第 %d 行是孤儿块：有引语但无任何分析子项' % ln))
            if thin and len(thin) == len(blocks):
                errs.append((name, '全文件 %d 个块的子项都比同书主流少（主流：%s）'
                             % (len(blocks), '、'.join(sorted(book_core)))))
            elif thin:
                warns.append((name, '%d/%d 个块子项少于同书主流（缺：%s）'
                              % (len(thin), len(blocks), thin[0][1])))
            # 引语配额：与本书众数比（不用外部 3–8/10）
            if book_quota and name in per_file_quota:
                mine = per_file_quota[name]
                if mine * 2 < book_quota or mine > book_quota * 2:
                    warns.append((name, '引语 %d 个，与本书众数 %d 相差过大'
                                  % (mine, book_quota)))
        # 编号连续（圈数字口径）。圈数字是**单个 unicode 字符**，`int('①')`
        # 直接抛 ValueError——须走 CIRCLED 的序号映射。
        circled = [CIRCLED.index(c) + 1 for c in re.findall(
            '[' + CIRCLED + ']',
            '\n'.join(l for l in lines if RE_QUOTE_CIRCLED.match(l)))]
        if circled and circled != list(range(1, len(circled) + 1)):
            errs.append((name, '圈数字编号不连续：%s' % circled[:14]))
        # 重复引语块
        seen = {}
        for ln, q in quotes:
            k = norm(q).lower()[:60]
            if k in seen:
                errs.append((name, '第 %d 行引语与第 %d 行重复：%s' % (ln, seen[k], q[:44])))
            else:
                seen[k] = ln

        # ── B. 占位/垃圾行（§10.4）
        for i, l in enumerate(lines, 1):
            if PLACEHOLDER_PAT.search(l):
                errs.append((name, '第 %d 行含占位标注「%s」' % (i, PLACEHOLDER_PAT.search(l).group(0))))
            elif PLACEHOLDER_ROW.match(l):
                warns.append((name, '第 %d 行词表例句列为空' % i))

        # ── C. 四方映射（§10.6.1）
        m_src = re.search(r'^source_text:\s*ch(\d+)', body, re.M)
        fno = chap_no(name, [r'^ch(\d+)', r'^(\d{1,3})[.\-\s]', r'ch(\d+)'])
        m_h1 = re.search(r'^#{1,2}\s*(?:第\s*)?(\d{1,3})\s*[.、章 ]', body, re.M)
        hno = int(m_h1.group(1)) if m_h1 else None
        sno = int(m_src.group(1)) if m_src else None
        if is_overview:
            hno = None          # 总览无单一章节号，`00 情感节点.md` 被推成 ch00
            fno = None          # 再与 H1「第 1」比就是纯假红
        if fno is not None and sno is not None and fno != sno:
            mapping.append((name, '文件名 ch%02d ↔ source_text ch%02d 不一致' % (fno, sno)))
        if sno is not None and has_text and not glob.glob(
                os.path.join(book, 'text', 'ch%02d*.txt' % sno)):
            mapping.append((name, 'source_text 指向 ch%02d，但 text/ 无该章提取件' % sno))
        if hno is not None and fno is not None and hno != fno:
            mapping.append((name, 'H1「第 %d」↔ 文件名 ch%02d 不一致' % (hno, fno)))

        # ── D. 必备节名（多数派口径）
        if not is_overview:
            for s in majority_secs:
                if s not in body:
                    warns.append((name, '缺多数派必备节「%s」' % s))

    print('=== 精读结构扫描（%s）===' % os.path.basename(book.rstrip('/')))
    print('  扫 %d 个 md、%d 个引语块；多数派必备节：%s'
          % (n_files, n_blocks, '、'.join(majority_secs) or '（无，不判）'))
    print('  本书主流子项（自推断，不套外部模板）：%s ｜ 引语众数 %d'
          % ('、'.join(sorted(book_core)) or '（未推断出）', book_quota))
    print('  ❌ 结构缺陷 %d ｜ ⚠️ 提示 %d ｜ 🔀 映射不一致 %d' % (len(errs), len(warns), len(mapping)))
    if not quiet:
        for name, msg in errs:
            print('  ❌ %s  %s' % (name[:40], msg))
        for name, msg in warns:
            print('  ⚠️ %s  %s' % (name[:40], msg))
        for name, msg in mapping:
            print('  🔀 %s  %s' % (name[:40], msg))
    return 1 if errs else 0


if __name__ == '__main__':
    sys.exit(main())
