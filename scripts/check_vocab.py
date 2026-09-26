#!/usr/bin/env python3
"""
check_vocab.py — 词汇表真实性/分档检测（逐章版）

用法：
  python3 scripts/check_vocab.py "<书目录>" [--verbose]

改动（v2 vs v1）：
  1. 词频逐章口径：每个词条查本章 text/chNN.txt，而非全库合并语料
  2. 例句整句+省略号分段：例句整句先比对本章；不命中则依省略号分段，
     每片段（≥12 字符）均命中本章才算 PASS；都不命中判 FAIL（不再是 WARN）
  3. 占位/自标判 FAIL：例句列 = "—" / "no" / 释义含"可略"/"未出现"等自标注
     → 直接 FAIL，不再是 silent pass

检查（对应根 AGENTS.md 核验规则第 4 条 + 第 8 条内联验证精神）：
  1. 词条真实性：三档词汇表每个词条的实词（≥4字母）须在本章出现
     （允许 -s/-ed/-ing 屈折变化；全书有而本章无 → 跨篇词条，降级处理）
  2. 例句逐字锚定：整句 + 省略号分段均须命中本章 text（FAIL）
  3. 分档合理性：⭐ 基础档含超纲生僻词 / ⭐⭐⭐ 高级档混入高频常用词 → WARN
  4. 占位/自标注：例句列"—"/"no"/释义含"可略"/"未出现" → FAIL
退出码：存在 fail 则非 0。

改动（v3，方案 P0-2 / P0-2b，2026-09-26）
------------------------------------------------
1. **节边界（P0-2b）**：旧实现 tier 一旦命中就**再也不复位**，同一文件里
   `## 可迁移表达` / `## 论证结构`（证据链）/ `## 概览` 等任意表格的行都被当词条行
   计数。现只扫 `## 词汇` 节（兼容英文 `## Vocabulary`）。全库实测排除 4716 行
   （2.6%），并对**词汇节外的词条形行显式报 WARN**——静默丢弃会造新盲区。
   无 `## 词汇` 节标题的文件**回退全文件扫描** + 格式 WARN，不丢覆盖。
2. **按表头名定位列（P0-2）**：旧口径 `cells[:3]` 遇 4 列表
   （`词汇|音标|释义|例句` / `词汇|词性|释义|例句`）会把音标/词性当例句，
   **真例句列从不校验**。全库实测此类表 264+ 张命中此盲区。
   现按表头名（词/释义/例句）定位列号；表头行取 sentinel **之前**那一行
   （标准 markdown 是「表头 → |---| → 数据行」）。
3. 本版同时修掉两个自伤：resolve_cols 回退候选未排除词头列（中文例句列会让
   xi 落到词头上 → 假 FAIL）；表头行识别方向搞反（把数据行当表头）。

改动（v4，方案 P0-3 / P0-4，2026-09-26）
------------------------------------------------
4. **P0-3 例句须含词头**（判 WARN）：例句 flat 后须含词条任一实词。停用词表
   **不排介词与小品词**——短语动词（be up for sth / check out）的中心词正是
   小品词，排掉就永远配不上。实测近 28 日本 20431 可判定行中 943 行（4.62%）
   不含词头，涉 26/28 本。**判 WARN 不判 FAIL**：这些例句本身是原文逐字
   （不是造假），属"例句没配到词"的质量问题；判 FAIL 会一次性卡住 26 本。
   升级只需把 warns.append 改到 fails（一行）。
5. **P0-4 必备章节 + 空文件**（判 FAIL）：
   - <200 字节判空/近空。实测抓到全库唯一 0 字节文件
     （night-circus ch68，其 text/ 有 6885 字节真实文本——提取了却从未写；
     三门禁在空文件上全绿：0 引语 / 0 词条行 / 0 FAIL）。
   - 必备角色**按书多数派自校准**（该角色须在本书 ≥50% 文件中出现），**不
     硬编码体裁**。理由：节名变体太多（`## 10 Quote Blocks with Five
     Sub-items`、`## 逐句精读（10处）`、英文 `## Vocabulary`），且 open-secrets
     8 篇内部格式不统一（6 篇无概览 / 2 篇有）。一刀切要求"概览"必假红。
     多数派只抓"这一篇缺了同侪都有的章节"——正是空文件那类真缺陷。
   - 阈值 50% 与 60% 实测结果完全相同（不敏感）。
   - 总览三篇排除：前缀 `00_` / **`00 `（空格，实测存在）** / 裸名（概述.md）。
"""
import re, sys, glob, os, zipfile, html as htmlmod, unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_quotes import epub_flat_text, read_html

flat = lambda s: re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).lower())

# ~200 个最高频英文词（分档合理性检测用）
COMMON = set("""the be to of and a in that have i it for not on with he as you do at this but his
by from they we say her she or an will my one all would there their what so up out if about who get
which go me when make can like time no just him know take people into year your good some could them
see other than then now look only come its over think also back after use two how our work first well
way even new want because any these give day most us man find here thing great little world own life
still small large next early young important few public bad same able tell something nothing each every
must such again change off turn play hand part room case ask last around need better big old right left
end home read lot name water money fact place hear kind best sure top done heart black white blue
green red house dog cat book word mother father sister brother son girl boy child war city street
table chair door window light night morning water head face eye nose mouth arm leg hand foot tree
sun moon star sky rain snow wind fire""".split())

TIER_PAT  = re.compile(r'^#+\s*[⭐★]*\s*(高级|进阶|基础)')
SENTINEL  = re.compile(r'^\s*\|[-\s|]+\|\s*$')
PH_HIT    = re.compile(r'^[—\-]\s*$')            # 例句列 = 纯占位
NO_HIT    = re.compile(r'^\s*no\s*$', re.I)      # 例句列 = no
ANN_HIT   = re.compile(r'[（()](可略|未出现|未在|此处未用|可省|略|见高级|见ch)[)）]')  # 释义自标（含全角/半角括号 + 扩展关键词）
EPUB_SENTINEL = re.compile(r'\[以下例句未出现在原文，[^\]]+\]', re.IGNORECASE)

# ── P0-2b 词汇表节边界（2026-09-26）────────────────────────────────────────
# 旧实现 tier 一旦被 TIER_PAT 命中就**再也不复位**，于是同一文件里
# 「可迁移表达」「论证结构」「段落脉络」等任意表格的行都被当词条行计数。
VOCAB_SEC = re.compile(r'^##\s.*(词汇|vocab|word\s*list|lexicon)', re.I)
H2_PAT    = re.compile(r'^##\s')

# 表头角色定位（P0-2）。全库表头实测：3 列 `词/短语|释义|例句` 为主，
# 另有 `词汇|音标|释义|例句` / `词汇|词性|释义|例句` 两类 4 列——旧口径
# cells[:3] 会把「音标/词性」当例句，**真例句列从不校验**。
HDR_ENTRY = ('词/短语', '词条', '单词/短语', '单词', '词汇', '短语', '表达', 'word', 'term', 'phrase')
HDR_MEAN  = ('释义', '含义', '意思', '解释', 'definition', 'meaning', 'gloss')
HDR_EXAM  = ('例句', '原文例', '例 句', 'example', 'sentence', 'citation')

# P0-3「例句须含词头」用。**不排介词与小品词**——短语动词（be up for sth /
# check out / give in）的中心词正是小品词，排掉就永远配不上。
FUNC_STOP = {'the', 'a', 'an', 'and', 'or', 'it', 'its', 'is', 'are', 'was', 'were',
             'be', 'been', 'being', 'do', 'does', 'did', 'has', 'have', 'had',
             'that', 'this', 'these', 'those', 'there', 'he', 'she', 'they'}

# ── P0-4 必备章节（2026-09-26）─────────────────────────────────────────────
# 最初想按体裁硬编码（AGENTS 的短篇合集格式不含「概览」，一刀切会全量假红），
# 实测后改为**按书多数派自校准**——见 expected_roles_for_book 的 docstring。
VOCAB_ROLE = (r'^词汇分级', r'^本章词汇', r'^本篇词汇', r'^Vocabulary', r'^Word List')
# 别名按实测补：open-secrets ch03 用英文 `## 10 Quote Blocks with Five Sub-items`
ROLE_PATS = {
    '概览': (r'^概览', r'^本章导航', r'^篇目概要', r'^Overview'),
    # 允许可选的前导计数（实测 `## 10 Quote Blocks with Five Sub-items`）
    '精读': (r'^精读$', r'^逐句精读', r'^选择性精读', r'^逐段精读',
             r'^(?:\d+\s+)?Quote\s+Blocks', r'^(?:\d+\s+)?Close\s+Reading', r'^Reading'),
    '词汇': VOCAB_ROLE,
    '总结': (r'^一句话总结', r'^精读结束总结', r'^精读总结', r'^Summary', r'^One-Sentence'),
}
# 总览三篇：前缀是 `00_`（多数）或 `00 `（少数），另有裸名 `概述.md`
OVERVIEW_RE = re.compile(r'^00[ _]|^(概述|金句精选|情感节点|金句)')
MIN_MD_BYTES = 200   # 低于此值视为空/近空文件（实测全库唯一 0 字节文件）
MAJORITY = 0.5       # 角色须在本书过半文件中出现，才算每篇的必备项


def roles_in(headings):
    hs = [h.lstrip('#').strip() for h in headings]
    return {r for r, ps in ROLE_PATS.items()
            if any(any(re.match(p, h) for p in ps) for h in hs)}


def expected_roles_for_book(paths):
    """按书**多数派**自校准必备角色，不硬编码体裁。

    理由（实测 28 本 919 文件）：节名变体极多（`## 10 Quote Blocks with
    Five Sub-items`、`## 逐句精读（10处）`、英文 `## Vocabulary`），而 open-secrets
    8 篇内部格式还不统一（6 篇无概览 / 2 篇有）。一刀切要求「概览」必假红。
    多数派规则只抓「这一篇缺了同侪都有的章节」——正是空文件那类真缺陷。
    """
    if not paths:
        return set()
    per = []
    for p in paths:
        hs = [l.strip() for l in open(p, encoding='utf-8', errors='ignore')
              if re.match(r'^#{1,3} ', l.strip())]
        per.append(roles_in(hs))
    return {r for r in ROLE_PATS
            if sum(1 for s in per if r in s) / len(per) >= MAJORITY}


def resolve_cols(cells):
    """按**表头名**定位 entry/meaning/example 列号。返回 (ei, mi, xi)。

    找不到可识别的表头时返回 None，由调用方回退旧口径 (0, 1, 2)。
    分档表头行（`⭐⭐⭐ 高级 | 释义 | 例句`）无 entry 列 → entry 缺省 0。

    ⚠️ 回退候选**必须排除已定位的 entry/释义列**：否则一行
    `epiphany | 顿悟 | （本章未出现，预估后续章节）` 会被解析成 xi=0
    （唯一含 ≥8 字母数字的列就是词头自己），例句变成词头 → 假 FAIL。
    """
    def find(kws, skip=()):
        for i, c in enumerate(cells):
            if i in skip:
                continue
            cl = c.strip().lower()
            if any(k in cl for k in kws):
                return i
        return None
    ei = find(HDR_ENTRY)
    mi = find(HDR_MEAN, skip=(ei,) if ei is not None else ())
    xi = find(HDR_EXAM, skip=tuple(i for i in (ei, mi) if i is not None))
    if xi is None:
        # 无「例句」表头 → 最后一个含 ≥8 字母数字的列（兼容 4 列无名表头）
        skip = {i for i in (ei, mi) if i is not None}
        cands = [i for i, c in enumerate(cells)
                 if i not in skip and len(re.findall(r'[A-Za-z0-9]', c)) >= 8]
        if not cands:
            return None
        xi = cands[-1]
    if mi is None:
        mi = 1 if xi != 1 else 0
    if ei is None:
        ei = 0 if mi != 0 else 1
    if not (0 <= ei < len(cells) and 0 <= mi < len(cells) and 0 <= xi < len(cells)):
        return None
    if xi == ei:                      # 例句列与词头列重合 → 判定不可信，回退
        return None
    return ei, mi, xi



def load_epub_book(epub_path):
    """Return flat-alpha of entire epub (for全书口径 fallback)."""
    try:
        return flat(epub_flat_text(epub_path))
    except Exception:
        return ''


def load_chapter_corpora(book_dir):
    """Return {nn: flat_alpha_text} for all text/chNN*.txt in book_dir."""
    text_dir = os.path.join(book_dir, 'text')
    corpora = {}
    if os.path.isdir(text_dir):
        for f in glob.glob(os.path.join(text_dir, 'ch*.txt')):
            m = re.match(r'ch(\d+)', os.path.basename(f))
            if m:
                nn = int(m.group(1))
                corpora[nn] = flat(open(f, encoding='utf-8', errors='ignore').read())
    return corpora


def load_epub_if_needed(book_dir, chapter_corpora):
    """Return full-book flat-alpha (for跨书/跨篇 fallback only)."""
    epubs = glob.glob(os.path.join(book_dir, 'library', '*.epub'))
    if epubs:
        return load_epub_book(epubs[0])
    return ''


CONTRACTIONS = {"i've","i'm","he'd","she'd","we'd","they'd","it's","that's","don't","won't","can't","didn't","wasn't","i'll","he'll","she'll","we'll","they'll","you'd","you'll","you've","we've","they've","there's","what's","let's","couldn't","shouldn't","wouldn't","hadn't","hasn't","haven't","aren't","isn't"}

def word_hits_corpus(word, corpus):
    """Check if word (or its stem) hits corpus. Returns True if found.

    2026-09-06 修撇号误报：I've/he'd 去撇号后为 ive/hed（3字符），旧逻辑
    len>=4 下限直接失配 -> A类虚构误报（Up in Molten Lights ch54 十条实证）。
    缩写词按 3 字符下限匹配（flat 语料本无撇号，3 字符已足够特异）。
    """
    w = word.replace("'", "").replace("\u2019", "").lower()
    min_len = 3 if word.lower().strip() in CONTRACTIONS else 4
    # Allow -s / -ed / -ing / -s after s / -lier etc.
    for stem in (w, w.rstrip('s'), w.rstrip('ing')+'e' if w.endswith('ing') else w,
                 w.rstrip('ed') if not w.endswith('e') else w,
                 w.rstrip('ly') if w.endswith('ly') else None):
        if stem and len(stem) >= min_len and stem in corpus:
            return True
    return len(w) >= min_len and w in corpus


def example_ok(example, corpus):
    """Check example sentence against corpus. Returns (ok, detail).

    2026-09-06 增补：
    a) 引号分段——"A," she said. "B" 跨标签行拆引号内各段独立验证；
    b) 后缀锚定——整句前缀指纹失败时，尝试例句的后缀片段（去掉首个词），
      应对页码污染点落在句首的假 FAIL（Helm 实证），后缀仍须逐字连续。
    """
    if not example or len(re.findall(r'[A-Za-z0-9]', example)) < 8:
        return False, '例句过短或为空'
    eq = flat(example)
    # 整句匹配（取前 60 字符作为指纹）
    if eq[:60] in corpus:
        return True, '整句命中'
    # 引号内分段（对话体跨标签实证）
    qparts = re.findall(r'["\u201c]([^"\u201d]{8,})["\u201d]', example)
    if len(qparts) >= 2 and all(flat(p)[:40] in corpus for p in qparts):
        return True, f'引号分段({len(qparts)}段)命中'
    # 省略号分段：每段（>=12 字符）都必须命中（… 与 ... 两种写法）
    frags = [p.strip() for p in re.split(r'\u2026|\.\.\.', example)
             if len(re.findall(r'[A-Za-z0-9]', p)) >= 12]
    if frags and all(flat(p)[:40] in corpus for p in frags):
        return True, f'省略号分段({len(frags)}段)命中'
    # 后缀锚定：去首个词再试（页码污染点假 FAIL，Helm 实证）
    m = re.match(r'^\s*[A-Za-z]+\s+(.+)$', example)
    if m:
        eq2 = flat(m.group(1))
        if len(eq2) >= 40 and eq2[:60] in corpus:
            return True, '后缀锚定命中'
    return False, '例句未命中本章'


def check_book(book_dir, verbose=False):
    chapter_corpora = load_chapter_corpora(book_dir)
    book_corpus = load_epub_if_needed(book_dir, chapter_corpora)

    fails, warns = [], []
    total_rows = 0

    md_files = sorted(glob.glob(os.path.join(book_dir, '*.md')))
    # P0-4 前置：本书的「必备角色」按多数派自校准（排除总览三篇）
    expected = expected_roles_for_book(
        [p for p in md_files if not OVERVIEW_RE.match(os.path.basename(p))])

    for f in md_files:
        name = os.path.basename(f)
        if OVERVIEW_RE.match(name):
            continue  # 总览三篇（00_ / `00 `空格 / 裸名）无词汇表，格式另定

        # 读 frontmatter（优先）：source_text: chNN 或 chapter: N
        fm = {}
        in_fm = False
        for line in open(f, encoding='utf-8'):
            if line.strip() == '---':
                in_fm = not in_fm; continue
            if in_fm and ':' in line:
                k, v = line.split(':', 1)
                fm[k.strip()] = v.strip()
        # source_text: ch04 → 优先使用，覆盖文件名章号
        st = fm.get('source_text', '')
        sm = re.match(r'ch(\d+)', st)
        nn = int(sm.group(1)) if sm else None
        if nn is None:
            # 回退：从文件名提取章号
            cm = re.match(r'ch(\d+)', name)
            nn = int(cm.group(1)) if cm else None
        if nn is None:
            nn = int(fm['chapter']) if fm.get('chapter', '').isdigit() else None
        ch_corpus = chapter_corpora.get(nn, '') if nn is not None else ''

        tier = None
        n_rows = 0
        # ── P0-2b 两遍：先判本文件有无词汇节，再决定扫描范围 ──────────
        lines = open(f, encoding='utf-8').read().splitlines()
        # ── P0-4 必备章节 / 空文件 ────────────────────────────────
        headings = [l.strip() for l in lines if re.match(r'^#{1,3} ', l.strip())]
        body_bytes = sum(len(l.encode('utf-8')) for l in lines)
        if body_bytes < MIN_MD_BYTES:
            # 空/近空文件：三门禁全绿（0 引语 / 0 词条行 / 0 FAIL），
            # 只有这里拦得住。实测全库唯一 0 字节文件 = night-circus ch68，
            # 其 text/ 有 6885 字节真实文本——提取了却从未写。
            fails.append((name, None,
                          f'空/近空文件（{body_bytes} 字节，<{MIN_MD_BYTES}）——'
                          f'若 text/ 有对应提取件则该章尚未动笔', ''))
        else:
            have = roles_in(headings)
            miss = sorted(expected - have)
            if miss:
                fails.append((name, None,
                              '缺必备章节（同侪多数派有）：' + '、'.join(miss), ''))
        has_vocab_sec = any(VOCAB_SEC.match(l.strip()) for l in lines)
        if not has_vocab_sec:
            # 无节标题 → 回退全文件扫描（宁可多查不可静默丢覆盖），并报格式 WARN。
            # 实测 14 个真章节属此情形（natural-selection / unearthed 用英文
            # `## Vocabulary` 者已由 VOCAB_SEC 覆盖，此处是连节标题都没写）。
            warns.append((name, None, '无 `## 词汇` 节标题，已按全文件扫描（格式应补节标题）', ''))
        in_vocab = not has_vocab_sec          # 无节标题时全文件都算
        sec_name = '(全文)'
        stray = {}                            # 节名 → 被排除的词条形行数
        hdr = None                            # 表头定位结果 (ei, mi, xi)
        prev_cells = None                     # sentinel 之前那一行 = 候选表头
        for line in lines:
            s = line.strip()
            # ── 节边界：H2 切换 in_vocab；H3 分档切 tier ──
            if H2_PAT.match(s):
                in_vocab = (not has_vocab_sec) or bool(VOCAB_SEC.match(s))
                sec_name = s.lstrip('#').strip()
                tier = None; hdr = None; prev_cells = None
                continue
            hm = TIER_PAT.match(s)
            if hm:
                tier = hm.group(1); hdr = None; prev_cells = None
                continue
            if not s.startswith('|'):
                prev_cells = None
                continue
            if SENTINEL.match(s) or '|---' in s:
                # 标准 markdown 顺序是「表头 → |---| → 数据行」，故表头是
                # sentinel **之前**那一行。取到就定位列号（第一版误把 sentinel
                # 之后的行当表头，导致数据行被解析 → 假 FAIL）。
                hdr = resolve_cols(prev_cells) if prev_cells else None
                prev_cells = None
                continue
            cells = [c.strip() for c in s.strip('|').split('|')]
            if len(cells) < 2:
                prev_cells = None
                continue
            prev_cells = cells                   # 供下一条 sentinel 回填用
            ei, mi, xi = hdr if hdr else (0, 1, 2)
            if ei >= len(cells) or not re.search(r'[A-Za-z]{2,}', cells[ei]):
                continue
            if not in_vocab:
                # 词汇节之外的词条形行：不计入，但**必须显式报出**——
                # 静默丢弃会造新盲区（§8.6）。典型成因是同一文件里
                # `## 精读` 下又摆了一份重复词汇表（Addie Laud ch36 实测 348 行）。
                stray[sec_name] = stray.get(sec_name, 0) + 1
                continue
            entry = cells[ei]
            meaning = cells[mi] if mi < len(cells) else ''
            example = cells[xi] if xi < len(cells) else ''
            words = [w.lower() for w in re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", entry)]
            words = [w for w in words if w not in ('the','a','an','of','in','on','to','and','or')]
            if not words:
                continue
            n_rows += 1

            # ── FAIL 层 ──────────────────────────────────────────
            # 1. 例句列占位
            if PH_HIT.match(example.strip()) or NO_HIT.match(example.strip()):
                fails.append((name, tier, '例句列为占位符（—/no）', entry))
                continue
            # 2. 释义自标绕过（"（可略）"/"（本篇未出现）"等）
            if ANN_HIT.search(meaning) or EPUB_SENTINEL.search(example):
                fails.append((name, tier, '释义含自标绕过注释（未出现在原文/可略）', entry))
                continue
            # 3. 例句不命中本章（省略号分段也不命中）
            if example and len(re.findall(r'[A-Za-z0-9]', example)) >= 8:
                ok, detail = example_ok(example, ch_corpus)
                if not ok:
                    fails.append((name, tier, f'例句未命中本章({detail})', example[:60]))
                    continue
            # 4. 词条实词不在本章（全书中也不存在 → 真虚构；有但不在本章 → 跨篇词条，降级 WARN）
            missing_ch = [w for w in words if len(w) >= 4 and not word_hits_corpus(w, ch_corpus)]
            if missing_ch:
                if ch_corpus and not any(word_hits_corpus(w, book_corpus) for w in missing_ch):
                    fails.append((name, tier, f'词条(A类虚构，全书查无)', entry))
                else:
                    warns.append((name, tier, f'词条跨篇(本章无，全书有)', entry))
            # ── WARN 层 ──────────────────────────────────────────
            # 5. 分档合理性
            key = min(words, key=len) if words else ''
            if tier == '基础' and words and all(w in COMMON for w in words if len(w) >= 4):
                pass  # 全常用词在基础档：合理
            elif tier == '基础' and any(len(w) >= 9 and w not in COMMON for w in words):
                warns.append((name, tier, '基础档疑含超纲词', entry))
            elif tier == '高级' and words and all(w in COMMON for w in words):
                warns.append((name, tier, '高级档混入常用词', entry))
            # 6. P0-3 例句必须含词头（判 WARN 不判 FAIL，理由见下）
            #    实测 28 本近两日书：20431 可判定行中 943 行（4.62%）例句
            #    不含词条任一实词，涉 26/28 本。若判 FAIL 会一次性卡住
            #    26 本——而这些例句本身是**原文逐字**（不是造假），属
            #    「例句没配到词」的质量问题，不是真实性问题，故降级 WARN。
            #    升级为 FAIL 只需把 append 换到 fails，改一行。
            if example and len(re.findall(r'[A-Za-z0-9]', example)) >= 8:
                heads = [w for w in words if len(w) >= 3 and w not in FUNC_STOP]
                if heads:
                    ef = flat(example)
                    if not any(w in ef or word_hits_corpus(w, ef) for w in heads):
                        warns.append((name, tier, '例句不含词头', entry))

        total_rows += n_rows
        for sec, k in sorted(stray.items(), key=lambda x: -x[1]):
            warns.append((name, None,
                          f'词汇节外有 {k} 行词条形表格（`{sec}`）已排除——'
                          f'格式应把词汇表归入 `## 词汇` 节，否则等于重复登记', ''))

    return {'fails': fails, 'warns': warns, 'rows': total_rows}


def main(book_dir, verbose=False):
    r = check_book(book_dir, verbose)
    print(f'词条行合计: {r["rows"]}')
    print(f'\n--- FAIL ({len(r["fails"])}) ---')
    for x in r['fails']:
        print(f'  {x[0]} [{x[1] or "?"}] {x[2]}')
        print(f'      「{x[3][:70]}」')
    print(f'\n--- WARN ({len(r["warns"])}) ---')
    for x in r['warns']:
        print(f'  {x[0]} [{x[1] or "?"}] {x[2]}「{x[3][:70]}」')
    sys.exit(1 if r['fails'] else 0)


if __name__ == '__main__':
    main(sys.argv[1], '--verbose' in sys.argv)
