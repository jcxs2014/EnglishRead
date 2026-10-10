#!/usr/bin/env python3
"""
sweep_analysis_inline.py — 分析层行内英文逐字核查（方案 P1 第 4 个脚本）

为什么需要
----------
**现有六道门禁都不看分析层。** `verify_quotes` 只抽引语行，`check_chapter_quotes`
同样，`check_vocab` 查词表，`check_entities` 查梗概实体——于是
`**为什么这样写**` / `**关键词**` / `**读者视角提示**` 里引用的英文片段
可以任意改写、漏字、错引号而全部绿灯。

本库已实证的缺陷（attic `inline_verbatim_audit.py` 文件头自记）：
  · `a string of tomorrows`        实为原文 `the same string of tomorrows`（漏词）
  · `let them see my wolf's tooth` 全书查无（凭空造词）

**归属分工**：引语行由 `verify_quotes` / `check_chapter_quotes` 负责，本脚本
一律跳过；这里只查**分析层**行内英文。方案 §八 采纳项 1 指出「分析层行内英文
不只在总览，正文章节也有」，故**全部 md 都扫**，不限 `00_*.md`。

三处对 attic 的修正
-----------------
1. **双引号也收**。attic 两份是割裂的：`inline_verbatim_audit` 只看反引号
   `` `x` ``，`inline_check` 看双引号 `"x"` 但**只扫 `00_*.md`**。而本库
   通行写法是双引号——`**为什么这样写**：……——"He's ours" 三个字……`
   （memories-like-fangs ch19 实证）。只查反引号会整类漏收。→ 两类都收，
   且正文章节与总览一视同仁。
2. **文件名不按形态过滤**。attic 用 `ch[0-9][0-9]_*.txt` 与 `ch*.md`，
   漏掉 `01-…md` / `04. Chapter Three.md` / `ch25_byrds_of_a_feather.txt`
   等命名变体（AGENTS 有专条实证：Lost&Found ch22→ch25 特殊文件名）。
   → `text/*.txt` 与 `<书目录>/*.md` 全收，靠内容判定而非文件名。
3. **整串 flat 比对 + 跨章定位**。attic 只做子串 `in ALL`，报「查无」但
   不告诉你**它其实在哪一章**——而「跨章搬用」与「凭空造词」是两种缺陷、
   两种处置。本脚本额外给出定位，并把两种匹配路径都记下来。

七档判定（**顺序即优先级**，2026-09-26 实测 11 本定档）
------------------------------------------------------
| 档 | 判据 | 判定 | 11 本实测 |
|----|------|------|-----------|
| ✅ 逐字 | 整串 flat 在本章 `text/` | 通过 | 8802 |
| ⚠️ 跨章 | 整串在**别的章** | 提示 | 399 |
| 🔶 拼接 | 整串查无但分段都在 / 整串跨标签 | 提示 | 154 |
| 🔧 B 类 | `text/` 查无**但 epub 有** | 提示：语料提取缺失 | 2 |
| 🟠 部分命中 | 内容词部分命中、整串不连续 | 提示：疑漏词或改写 | 136 |
| 🟡 词形 | 内容词零命中、但有形态邻居 | 提示：`trembled` vs `trembling` | 12 |
| ⚪ 术语 | 零命中且仅 ≤2 内容词 | 提示：术语/语法记法，非引文 | 2 |
| ❌ 零命中 | 零命中且 ≥3 内容词 | **FAIL** | **0** |

**三处顺序/范围上的坑，都是第一版实跑才暴露的**

1. **B 类必须最先判**：片段在 `text/` 查无但在 epub 命中 ⇒ 提取环节丢内容，
   不是分析层缺陷。不裁决就报成凭空造词（实测 floating-hotel 2 处）。
2. **partial 必须排在 stem 之前**：partial（"内容词在书里、整串不在"）比 stem
   （"存在某个形态邻居"）具体得多。`all_stems` 在大词库里近乎恒真——任何词都是
   某个书内词的形态邻居——stem 放前面会把 194 处全吸走、partial 直接归零，
   **信号被自己毁掉**。
3. **frontmatter 必须跳过**：`title: "One Way Back · 03 The Physics of Waves"`
   这类书名/章名不是引文（实测 one-way-back 60 处误报全来自这里）。带 `·`
   的片段一并排除（书眉签名）。

「拼接」这一档另有必要：flat 整串查无 ≠ 造词（AGENTS 有 12 处实证——两半逐字
都在原文、中间叙述标签被换成句号，flat 口径天然对拼接假阴为「查无」，直接判
A 类会误杀真引语，2026-09-22 实证）。

**已实证的缺陷样例**（attic 文件头自记，本脚本可抓）：
`a string of tomorrows` 实为 `the same string of tomorrows`（漏词，落 🟠 部分命中）；
`let them see my wolf's tooth` 全书查无（落 ❌ 零命中）。

用法
----
    python3 scripts/sweep_analysis_inline.py "<书目录>" [--quiet]

退出码：有「零命中」则 1；无 md / 无参照集 → 2（无法判定，不等于通过）。
"""
import glob
import os
import re
import sys
import unicodedata

# 参照集：从 text/ 逐章取；无 text/ 则退回 epub
STOP_FRAG = re.compile(r'[*_/|]|ch\d|text/|\.md\b|\.txt\b|\.epub\b|^\s*$')
# 通用虚词——算「内容词命中比例」时剔除
STOPW = set("""the a an of to in for and or is are was were be been being it its i you we they he she
him her his hers their our your my me not no do does did done have has had having will would shall
should can could may might must if then than that this these those there here as at by from with
about into over under again further once all any both each few more most other some such only own
same so too very s t just don now what which who whom whose when where why how""".split())
# 占位/模板串不是引文：`p0NN-supN`、`TBD`、`XXX`
PLACEHOLDER = re.compile(r'\bp\d*NN|\bTBD\b|\bXXX+\b|\bTODO\b|supN|\bNN\b', re.I)


def n(s):
    """归一：NFKC + 撇号/引号形态统一 + 空白折叠。源书用弯 ‘ ’ “ ”，
    分析层常写成直 ' "，形态差异不算差异。"""
    t = unicodedata.normalize('NFKC', s)
    for a, b in [('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'),
                 ('—', '-'), ('–', '-')]:
        t = t.replace(a, b)
    return re.sub(r'\s+', ' ', t).strip()


def nc(s):
    return n(s).lower()


def flat(s):
    """只留字母数字与空格（小写），用于整串比对。保留空格才有词边界——
    删空格的 flat 会让 'ice' 命中 'price'（AGENTS 有专条实证）。"""
    return re.sub(r'[^a-z0-9 ]+', ' ', nc(s))


def flat_tight(s):
    """删空格的整串——用于跨标签拼接的第二轮比对。"""
    return re.sub(r'[^a-z0-9]+', '', nc(s))


def is_quoteish(x):
    """只统计「看起来是引文」的反引号/引号片段。"""
    if re.search(r'[一-鿿]', x):
        return False
    if STOP_FRAG.search(x) or PLACEHOLDER.search(x):
        return False
    # 书眉/标题签名：`One Way Back · 03 The Physics of Waves` 这类是本文件自己的
    # 标题、不是引文（实测 one-way-back 60 处误报全来自 frontmatter 的 title:）
    if '·' in x or '•' in x:
        return False
    words = re.findall(r"[A-Za-z][A-Za-z']*", x)
    letters = sum(c.isascii() and c.isalpha() for c in x)
    if letters < 5:
        return False
    return len(words) >= 3 or (len(words) == 2) or (len(words) == 1 and len(words[0]) >= 6)


# 分析层英文片段的两种载体：反引号 与 双引号
SPAN = re.compile(r'`([^`\n]{4,})`|"([^"\n]{4,})"|“([^”\n]{4,})”')

# ⚠️ 2026-10-06（ITW 五步审查）新增**裸英文通道**：
# 原 SPAN 只切取**被引号/反引号包裹**的片段 ⇒ 分析层里**裸写的英文**（无任何包裹符）
# 压根不会被收进检查范围，而该脚本仍报「❌ 零命中 0」——
# **「0 异常」此时代表「没查」，不是「查过是绿的」**。
# 实测抓到两处真实阻断型：`remind him that this is over`（删掉 it doesn't mean 致语义反转）、
# `ice slipped through her veins`（引语是 Audrey's veins）。
# ⇒ 分析层三行（中文理解/为什么这样写/读者视角提示）里，
#    凡**连续 ≥4 个英文词**且不被任何包裹符覆盖的，一律作为候选送去比对。
_BARE = re.compile(r'(?<![A-Za-z])([A-Za-z][A-Za-z’\x27-]*(?:\s+[a-z][A-Za-z’\x27-]*){3,})(?![A-Za-z])')
_BARE_MIN = 4          # 连续英文词数下限
_BARE_MIN_FLAT = 16    # flat 长度下限（低于此多为普通术语，不报）


def bare_fragments(line):
    """裸英文候选：先剥掉已包裹部分，剩下的连续英文段。

    ⚠️ 2026-10-10 修正（october-daye-20 实证 3 处假红）：直引号行的引号配对会漂移
    （奇数引号/短于 4 字的对），SPAN 捕获到**纯中文**的伪 span；若照样剥掉，会把
    两侧的中文分隔符一并吞掉 ⇒ 两段独立英文被粘成一句（如
    `rich red garden roses were never going to be a comfort to me again`）。
    只剥**含字母**的 span；伪 span 就地保留，中文照样能断句。
    """
    def _strip(m):
        g = next((x for x in m.groups() if x), '')
        return ' ' if re.search(r'[A-Za-z]', g) else m.group(0)
    stripped = SPAN.sub(_strip, line)
    for m in _BARE.finditer(stripped):
        seg = m.group(1)
        if len(re.sub(r'[^a-z0-9]', '', seg.lower())) >= _BARE_MIN_FLAT:
            yield seg


def fragments(line, bare=False):
    for m in SPAN.finditer(line):
        for g in m.groups():
            if g:
                yield g
    if bare:
        for seg in bare_fragments(line):
            yield seg


def is_quote_line(line):
    """引语行由 verify_quotes / check_chapter_quotes 负责，这里必须跳过——
    否则同一句会被两个口径各判一次，报重复缺陷。"""
    s = line.strip()
    if s.startswith('>'):
        # `> **原句 N:** …` / `> …` 都是引语行；但 `> **中文理解**：…` 是分析层
        return not re.match(r'^>\s*\*\*[^*]+\*\*\s*[:：]', s)
    return bool(re.match(r'^\*{0,2}[①-⑳㉑-㉕]', s))


def load_ref(book):
    """返回 (逐章 [(章号, flat, flat_tight)], 来源说明)。

    **同时**载入 epub 作为第二参照（若存在）。理由：片段在 `text/` 查无但在
    epub 命中 ⇒ **B 类语料缺失**（提取环节丢内容），不是分析层缺陷。
    不做这一步交叉验证，会把提取缺口报成凭空造词——正是 AGENTS 第 5 条
    A/B 裁决要求避免的冤枉。
    """
    txs = sorted(glob.glob(os.path.join(book, 'text', '*.txt')))
    eps = sorted(glob.glob(os.path.join(book, 'library', '*.epub')))
    epub_flat = ''
    if eps:
        try:
            from verify_quotes import epub_flat_text
            epub_flat = flat(epub_flat_text(eps[0]))
        except Exception:
            epub_flat = ''
    if txs:
        out = []
        for p in txs:
            m = re.search(r'ch(\d+)', os.path.basename(p))
            num = int(m.group(1)) if m else -1
            raw = open(p, encoding='utf-8', errors='ignore').read()
            out.append((num, flat(raw), flat_tight(raw)))
        src = 'text/（%d 个提取件）' % len(txs)
        if epub_flat:
            src += ' + epub 交叉验证'
        return out, src, epub_flat
    if epub_flat:
        return [(-1, epub_flat, flat_tight(epub_flat))], 'epub（整书，无章级定位）', ''
    return None, '无 text/ 且无 epub', ''


def content_toks(x):
    return [w for w in re.findall(r"[a-z][a-z'-]*", nc(x))
            if w not in STOPW and len(w) > 2]


def stems_of(word):
    """一个词的词干集合（原形 + 去后缀 + 去后缀补 e）。"""
    out = {word}
    for suf in ('ing', 'ed', 'es', 's', 'd', 'ly', 'er', 'est', 'en'):
        if word.endswith(suf) and len(word) - len(suf) >= 3:
            out.add(word[:-len(suf)])
            out.add(word[:-len(suf)] + 'e')
    return out


RE_HEADING = re.compile(r'^#{1,6}\s')
RE_CELL_EN = re.compile(r"[A-Za-z][A-Za-z',\-]*(?:\s+[A-Za-z][A-Za-z',\-]*)+")


def is_table_row(line):
    """表格行（以 `|` 开头）。**落点 #14**：`sweep_analysis_inline` 的扫描范围
    显式扩到「所有二级标题节的表格单元格」。

    为什么必须显式做、不能靠顺带：原先 SPAN 正则只抓**引号/反引号内**的片段，
    表格行因此只是「碰巧」被覆盖到，而**表里大量英文并不带引号**——
    `| 两颗珍珠 | ch02 祖母的比喻 | ch18 珍珠生成机制讲学；ch27 Ursula 复述… |`
    里的 `Anita Hill`、`Ursula` 这类**裸英文单元格**一个都抓不到。
    故对表格行额外做**单元格级**扫描（带引号的单元格仍交回 SPAN，避免重复计）。
    """
    return line.lstrip().startswith('|')


def table_cells(line):
    """切出表格单元格内容。跳过 `---` 分隔行。"""
    raw = line.strip()
    if not raw.startswith('|'):
        return []
    body = raw.strip('|')
    if re.fullmatch(r'[\s\-:|]+', body):
        return []
    return [c.strip() for c in body.split('|') if c.strip()]


def cell_fragments(cell):
    """表格单元格里的**裸英文短语**（不含引号/反引号/粗体者）。

    含引号或反引号的单元格交回 SPAN 处理，否则同一段文字会被计两次。
    """
    if '"' in cell or '“' in cell or '`' in cell or '**' in cell:
        return []
    m = RE_CELL_EN.search(cell)
    return [m.group(0)] if m else []


def classify(frag, chap_num, chap_flat, chap_toks, ref, all_tight, all_toks,
             all_stems, epub_flat=''):
    """返回 (判定, 定位)。定位为空串表示全书无。

    `chap_num` / `chap_flat` / `ref` 全部显式传入——不靠模块级全局传递
    （全局被 main 的循环覆写后，classify 读到的是最后一章的值）。

    七档，**顺序即优先级**（按实测证据定，逐档对应不同处置）：
      ok      整串在本章                        通过
      cross   整串在别的章                      提示：多引了相邻章
      splice  整串查无但分段都在 / 整串跨标签   提示：省略号或跨标签拼接
      partial 内容词部分命中                   提示：疑漏词或改写
      stem    内容词零命中、但存在形态邻居      提示：trembled vs trembling
      term    内容词零命中、仅 ≤2 个内容词      提示：术语或语法记法，非引文
      miss    内容词零命中、≥3 个内容词        **FAIL**：凭空造词

    ⚠️ **partial 必须排在 stem 之前**：partial（"这个短语的内容词在书里但整串
    不在"）比 stem（"存在某个形态邻居"）具体得多。前一版把 stem 放前面，
    而 `all_stems` 在大词库里近乎恒真（任何词都是某个书内词的形态邻居），
    于是 194 处全被吸进 stem 档、partial 直接归零——**信号被自己毁掉**。
    """
    f, t = flat(frag), flat_tight(frag)
    if not f.strip():
        return 'skip', ''
    if chap_flat and f in chap_flat:
        return 'ok', '本章'
    hits = [str(num) for num, cf, _ in ref if num != chap_num and f and f in cf]
    if hits:
        return 'cross', '实为 ch' + ','.join(hits[:4])
    if t and t in all_tight:
        return 'splice', '整串（跨标签拼接）'
    parts = [x for x in re.split(r'…|\.\.\.', frag) if x.strip(' ,;')]
    if len(parts) > 1:
        seg = [flat_tight(p) for p in parts]
        if all(s and s in all_tight for s in seg):
            return 'splice', '分段命中'

    ct = content_toks(frag)
    if not ct:
        return 'skip', ''
    # ⓪ B 类裁决：`text/` 查无但 epub 命中 ⇒ **语料提取缺失**，不是分析层缺陷。
    #    必须在所有缺陷档之前判，否则提取缺口会被报成凭空造词（AGENTS 第 5 条）。
    if epub_flat and f and f in epub_flat:
        return 'textgap', 'text/ 缺、epub 有 → B 类语料缺失'
    # ① partial：内容词部分命中——最具体，先判
    got = [w for w in ct if w in all_toks]
    if got:
        return 'partial', '内容词 %d/%d 命中（%s）——疑漏词或改写' % (
            len(got), len(ct), '/'.join(sorted(got)[:4]))
    # ② stem：零命中但存在形态邻居。词干必须**两侧都算**再求交——只拆片段侧
    #    去找完整词元集是恒不相交的（`trembled`→`trembl`，书里是 `trembling`）。
    f_stems = set().union(*[stems_of(w) for w in ct]) if ct else set()
    if f_stems & all_stems:
        return 'stem', '词形不符，原书词干 ' + '/'.join(sorted(f_stems & all_stems)[:3])
    for w in ct:
        if len(w) >= 5:
            hit = [t for t in all_toks if t.startswith(w) or w.startswith(t)]
            if hit:
                return 'stem', '疑派生词，原书作 ' + '/'.join(sorted(hit)[:3])
    # ③ 零命中：单词/双词多半是**分析者自撰术语或语法记法**（`neither-nor`、
    #    `how + adj`、`It wasn't X. It was Y.`、`pre-marketing`），不是引文——
    #    实测 10 处零命中里 9 处属此类，逐条判红即批量假红。≥3 内容词才当引文。
    if len(ct) <= 2:
        return 'term', '仅 %d 个内容词，判为术语/语法记法而非引文' % len(ct)
    return 'miss', '内容词零命中'


def main():
    args = sys.argv[1:]
    quiet = '--quiet' in args
    pos = [a for a in args if not a.startswith('--')]
    if not pos:
        raise SystemExit('用法: sweep_analysis_inline.py "<书目录>" [--quiet]')
    book = pos[0]
    mds = sorted(glob.glob(os.path.join(book, '*.md')))
    if not mds:
        print('该目录下无 md 文件：%s' % book)
        return 2
    ref, ref_src, epub_flat = load_ref(book)
    if ref is None:
        print('=== 分析层行内英文逐字核查（%s）===' % os.path.basename(book.rstrip('/')))
        print('  ❓ **无法判定**：无 text/ 且无 epub —— 参照集缺失，不等于通过。')
        return 2
    all_tight = ''.join(t for _, _, t in ref)
    by_chap = dict((num, f) for num, f, _ in ref)
    tokset = {}
    for num, f, _t in ref:
        tokset[num] = set(re.findall(r"[a-z][a-z'-]*", f))
    all_toks = set().union(*tokset.values()) if tokset else set()
    all_stems = set().union(*[stems_of(w) for w in all_toks]) if all_toks else set()

    n_ok = n_cross = n_splice = n_miss = n_skip = n_stem = n_partial = n_term = n_gap = 0
    n_table_rows = n_table_frags = 0
    misses, crosses, splices, stems, partials, terms, gaps = [], [], [], [], [], [], []
    for md in mds:
        name = os.path.basename(md)
        mnum = re.search(r'ch(\d+)', name)
        chap_num = int(mnum.group(1)) if mnum else -1
        chap_flat = by_chap.get(chap_num, '')
        chap_toks = tokset.get(chap_num, set())
        if not chap_flat:                      # 该 md 无对应章文本 → 用全书
            chap_flat = ' '.join(f for _, f, _ in ref)
            chap_toks = all_toks
        in_fm = False                          # YAML frontmatter 内
        for ln, line in enumerate(open(md, encoding='utf-8', errors='ignore'), 1):
            s = line.strip()
            if ln == 1 and s == '---':
                in_fm = True
                continue
            if in_fm:
                if s == '---':
                    in_fm = False
                continue                       # frontmatter 不是分析层
            if is_quote_line(line):
                continue
            # 落点 #14：表格行额外做**单元格级**扫描（裸英文），并单独计数
            # ⚠️ bare 通道**只对非表格行开启**（2026-10-06 五步审查后修）：
            #    表格行（词表例句）已有 cell_fragments 单元格通道在扫；
            #    若再叠一遍 bare，行内中文引号 `“…”` 两侧会被拼成一句
            #    （实测 3 条伪影：`but only got out the words   before she choked on them`），
            #    制造「疑漏词或改写」假红。
            #    反之**分析层散文行**（中文理解/为什么这样写/读者视角提示）此前零覆盖，
            #    正是两处真实阻断型藏身处 ⇒ 只在那里开 bare。
            is_tbl = is_table_row(line)
            cands = list(fragments(line, bare=not is_tbl))
            if is_tbl:
                n_table_rows += 1
                for cell in table_cells(line):
                    for f2 in cell_fragments(cell):
                        cands.append(f2)
                        n_table_frags += 1
            for frag in cands:
                if not is_quoteish(frag):
                    n_skip += 1
                    continue
                kind, where = classify(frag, chap_num, chap_flat, chap_toks,
                                       ref, all_tight, all_toks, all_stems,
                                       epub_flat)
                if kind == 'ok':
                    n_ok += 1
                elif kind == 'cross':
                    n_cross += 1
                    crosses.append((name, ln, frag, where))
                elif kind == 'splice':
                    n_splice += 1
                    splices.append((name, ln, frag, where))
                elif kind == 'stem':
                    n_stem += 1
                    stems.append((name, ln, frag, where))
                elif kind == 'partial':
                    n_partial += 1
                    partials.append((name, ln, frag, where))
                elif kind == 'term':
                    n_term += 1
                    terms.append((name, ln, frag, where))
                elif kind == 'textgap':
                    n_gap += 1
                    gaps.append((name, ln, frag, where))
                elif kind == 'miss':
                    n_miss += 1
                    misses.append((name, ln, frag, line.strip()[:56]))
                else:
                    n_skip += 1

    print('=== 分析层行内英文逐字核查（%s）===' % os.path.basename(book.rstrip('/')))
    print('  参照集：%s ；扫 %d 个 md（引语行与 YAML frontmatter 已跳过）'
          % (ref_src, len(mds)))
    print('  落点 #14 表格单元格：%d 个表格行、%d 条裸英文单元格片段（带引号的单元格'
          '由引号/反引号通道覆盖，不重复计）' % (n_table_rows, n_table_frags))
    print('  ✅ 逐字 %d ｜ ⚠️ 跨章 %d ｜ 🔶 拼接 %d ｜ 🟠 部分命中 %d ｜ 🟡 词形 %d ｜ ⚪ 术语 %d ｜ 🔧B类语料缺 %d ｜ ❌ 零命中 %d ｜ 跳过 %d'
          % (n_ok, n_cross, n_splice, n_partial, n_stem, n_term, n_gap, n_miss, n_skip))
    if not quiet:
        for name, ln, frag, where in crosses:
            print('  ⚠️  %s:%d  「%s」→ %s' % (name, ln, frag[:56], where))
        for name, ln, frag, where in splices:
            print('  🔶 %s:%d  「%s」→ %s' % (name, ln, frag[:56], where))
        for name, ln, frag, where in stems:
            print('  🟡 %s:%d  「%s」→ %s' % (name, ln, frag[:56], where))
        for name, ln, frag, where in partials:
            print('  🟠 %s:%d  「%s」→ %s' % (name, ln, frag[:56], where))
        for name, ln, frag, where in terms:
            print('  ⚪ %s:%d  「%s」→ %s' % (name, ln, frag[:56], where))
        for name, ln, frag, where in gaps:
            print('  🔧 %s:%d  「%s」→ %s' % (name, ln, frag[:56], where))
        for name, ln, frag, ctx in misses:
            print('  ❌ %s:%d  「%s」内容词全书零命中' % (name, ln, frag[:56]))
            print('       %s' % ctx)
    return 1 if n_miss else 0


if __name__ == '__main__':
    sys.exit(main())
