#!/usr/bin/env python3
"""
check_anchor.py — 关键词锚定自查（方案 P1 第 2 个脚本，AGENTS 第 8 条 e 项 / 第 9 条 b）

为什么需要
----------
AGENTS 第 8 条 e 项早就规定「**关键词** 里的英文词须能在本块引语中找到」，
但**规则存在而工具不在 `scripts/`**——attic 里 8 份近重复实现全是按单本书
硬编码的（`kw_anchor_afs.py` / `_am.py` / `_df.py` / `_ksr.py` / `review.py`
/ `keyword_anchor.py` / `keyword_anchor_aoy.py` / `check_anchoring.py`），
各认一种引语格式、各硬编码一种子项清单。本脚本是收敛版。

判定口径 = AGENTS 第 9 条 b 的原文，不收紧也不放宽
-------------------------------------------------
第 9 条 b 说的是两件事，本脚本照办：

1. 「块内关键词的英文词必须能在**该块引语**中找到（允许词形变化）」
2. 「**语境延伸词必须在「为什么这样写」中有呼应**，否则替换为引语逐字词」

所以一个英文词**落在引语里或落在本块分析正文里都算过**。
第一版只查引语，实测在 memories-like-fangs 上 4 处**全是假阳**，且是同一类：
关键词行同时装「引语锚定词」与「语境延伸词（带中文括号说明）」，例如

    **关键词**：won't get off easy（不会轻易脱身）/ He's ours（他归我们管）
    **为什么这样写**：……Quinn 的回应是划主权——"He's ours" 三个字……

`He's ours` 不在本块引语里，但它是**另一句引语**，在本块分析里被明确讨论——按
第 9 条 b 属合法。只查引语会把规则允许的写法判成缺陷，比没检查更坏。

三个已修的坑（都是第一版实跑才暴露的，记录在此防止回退）
--------------------------------------------------------
1. **拼接分支的 group 编号**：三个引语格式分支用 `|` 拼成一个 pattern 后，
   `m.group(1)` 只归属第一分支，另两个分支命中时它是 `None`，
   `if m and m.group(1)` 把有效引语**静默丢弃** → 整轮 0 报警（假绿）。
   改用命名 group + 取非空值，不依赖下标。
2. **配对必须按块，不能全文件取「最近前置引语」**：没有引语行的块会把关键词
   配到**上一个块**的引语上，凭空造出缺陷。本版以标题行为块边界重扫。
3. **中文括号说明要被剥掉**：`serious（Cole 的判断：同时叫=大事）` 里
   `Cole` 是人名不是关键词，剥括号后只剩 `serious`。

空跑防护（照搬 verify_quotes「0 提取」教训）
-------------------------------------------
关键词行 0 条、或关键词行 >0 但引语 0 条，都**不算通过**——报 ❓ 无法判定。
实测 the-morningside 有 585 条引语却 0 条 `**关键词**` 行，若照常报「0 处违规」
就是**真空通过**：书没被检查，却显示干净。

严重度分级（照 A/B 裁决纪律，2026-09-26 实测 11 本定档）
------------------------------------------------------
| 层 | 判据 | 判定 | 11 本实测 |
|----|------|------|-----------|
| 凭空造词 | 词不在引语、不在本块分析，且**全书参照集查无** | **FAIL** | **0 处** |
| 松散关键词 | 词不在引语、不在本块分析，但**全书参照集内** | 提示，不判红 | 24 处 |
| 仅中文注释 | 词带中文括号注释、无英文呼应 | 提示，不判红 | 随书 |
| 空跑 | 0 条关键词行，或有关键词行但 0 个引语块 | **❓ 无法判定**，退出码 2 | 2 本 |

**为什么凭空造词才是 FAIL**：本库通行写法是**关键词写中文理解的中译英**，
而非引语逐字词——`the lowest point of my life` 对应中文「我在我生命的最低点」，
而引语只说 `two years ago`。这类词逐条字面都违反 AGENTS 第 9 条 b，但**每个词
都在本书 `text/` 里**（11 本 24 处实测 24/24），不是造词。只按引语判会把它们
全判成缺陷，产出上百条批量假红；因此按 A/B 裁决（与 check_vocab 同源）分两层，
**只有全书查无才判红**。

参照集优先级：`text/`（逐章口径，最权威）→ epub → 都没有则该层**无法判定**。

用法
----
    python3 scripts/check_anchor.py "<书目录>" [--quiet]

退出码：凭空造词 >0 → 1；空跑 / 无法判定 → 2；否则 0。
"""
import os
import re
import sys
import glob

STOP = set("""the a an of to in for and or is are was were be been being it its i you we they he she
him her his hers their our your my me not no do does did done have has had having will would shall
should can could may might must if then than that this these those there here as at by from with
about into over under again further once all any both each few more most other some such only own
same so too very s t just don now""".split())

CIRCLED = '①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕'

# ⚠️ 命名 group + 取非空值。**不能用 m.group(1)**：分支拼接后 group(1) 只归属
# 第一分支，另两分支命中时为 None，会静默丢弃有效引语（见文件头坑 1）。
RE_QUOTE = re.compile(
    r'^\s*(?:>\s*)?\*{0,2}[' + CIRCLED + r']\*{0,2}\s*["“]?(?P<q1>.+?)["”]?\s*$'
    r'|^\s*>\s*\*{0,2}原句\s*\d+[:：]?\*{0,2}\s*["“]?(?P<q2>.+?)["”]?\s*$'
    # 裸 `> …`：排除中文开头、排除 `> **中文理解**：…` 这类标签行（以 `**` 开头）
    r'|^\s*>\s*(?!\*\*)(?![一-鿿])(?P<q3>.+?)\s*$', re.M)
# 关键词行：**两种都是库内合法写法**——粗体 `**关键词**：…`（176 本）与
# 裸 `关键词：…`（24 本，含 jane-eyre）。只认粗体会让这 24 本整册触发空跑
# 防护（`n_qblocks` 要求块内同时有引语与关键词行，两者都缺 → 报「无法判定」），
# 而 AGENTS 8.3 明写「格式自成一派的书是合法的」。故 `\**` 可选，向后兼容。
RE_KW = re.compile(r'\**(?:关键词|Key\s?words?)\*{0,2}\s*[:：]\s*(.+)$')
# 标题内嵌引语：`### 第N处「…」`。**N 须兼容中文数字**——本库通行写法是
# `### 第三处「…」` 而非 `### 第3处「…」`，只写 `\d+` 会整类漏收
# （第一版因此把这类块判成「无引语块」而跳过，等于没检查）。
RE_TITLE_Q = re.compile(
    r'^#{2,4}\s*第\s*[0-9一二三四五六七八九十百廿卅]+\s*处[^「\n]*「([^」]+)」')
RE_HEADING = re.compile(r'^#{1,6}\s')
RE_CN_PAREN = re.compile(r'[（(][^）)]*[一-鿿][^）)]*[）)]')
SUFFIXES = ('ing', 'ed', 'es', 's', 'd', 'ly', 'er', 'est', 'ment', 'ness')


def norm(s):
    s = (s.replace('’', "'").replace('‘', "'")
          .replace('“', '"').replace('”', '"'))
    return re.sub(r'\s+', ' ', s).strip().lower()


def quote_of(m):
    """从 RE_QUOTE 的 match 里取引语正文；取不到返回 None。刻意不接受下标。"""
    if not m:
        return None
    for val in m.groupdict().values():
        if val and val.strip():
            return val.strip()
    return None


def is_quote_line(ln):
    body = quote_of(RE_QUOTE.match(ln))
    if body and re.search(r'[A-Za-z]{3,}', body):
        return body
    m = RE_TITLE_Q.match(ln.strip())
    if m and re.search(r'[A-Za-z]{3,}', m.group(1)):
        return m.group(1)
    return None


def words_of(phrase):
    """抽英文词：先剥中文括号说明，再按分隔符切，只留实词。

    返回 [(词, 是否带中文注释)]——`serious（Cole 的判断：同时叫=大事）` 里的
    `serious` 带注释，`gone`（没了）里的 `gone` 也带注释；注释是「作者自己知道
    这词什么意思」的证据，故与「凭空造词」区别对待。
    """
    out = []
    # 记下**哪些词出现在中文括号里**（这些是释义正文，不是关键词），
    # 再把括号整体剥掉后抽词——顺序反了会让括号里的 `tell sb. sth.` 被
    # 中文逗号切成独立 part 且失去括号标记 → sb./sth. 被当关键词
    # 报「凭空造词」（2026-09-27 五步审查实证）。
    in_paren = set()
    for m in RE_CN_PAREN.finditer(phrase):
        in_paren |= set(re.findall(r"[a-z]+(?:['-][a-z]+)*", norm(m.group(0))))
    stripped = RE_CN_PAREN.sub(' ', phrase)
    for part in re.split(r'[,，、;；/／|]+', stripped):
        # **词头与释义的分界**：本库关键词一律是「词头——中文释义」，
        # 破折号之后常夹带**词性标记与词源引证**（dispense ＝ 发放、iterate），
        # 它们不是关键词、也不在引语里。
        part = re.split(r'——|—{1,2}(?=\s*\S)', part)[0]
        for w in re.findall(r"[a-z]+(?:['-][a-z]+)*", norm(part)):
            if w in STOP or len(w) <= 2:
                continue
            if w.endswith("'s") or w in ("n't", "'s"):
                continue
            out.append((w, w in in_paren))
    return out


def toks(h):
    """把一段文本切成词元集合。**不用子串匹配**——`all` 会匹配上 `calling`
    内部、`art` 匹配上 `start`，短词因此大面积假阴性（第一版就栽在这）。"""
    # 撇号只允许出现在词内部（don't），不得吞尾部标点——旧式 [a-z'-]* 会把
    # 引语末尾的 darling'? 粘成一个词元，导致"全书查无"假红（2026-09-26 实证）
    # 撇号与连字符均只允许出现在词内部（don't / ever-growing）——尾部标点
    # 不得粘连成词元：旧式 [a-z'-]* 会把引语末尾的 darling'? 粘成 darling'，
    # 导致「全书查无」假红（2026-09-26 实证，ch18 Chapter 17）
    tk = set(re.findall(r"[a-z]+(?:['-][a-z]+)*", h))
    # **所有格形式须同时产出裸词元**：`Payback's a bitch` 切成 `payback's`，
    # 关键词侧写 `payback` 时就查无 → 假红（2026-09-27 五步审查实证，ch18）。
    # 只在词尾是 `'s` 时补一条，不动 `don't`（其 `'t` 不是所有格）。
    for w in list(tk):
        if w.endswith("'s") and len(w) > 3:
            tk.add(w[:-2])
    return tk


def anchored(word, *haystacks):
    """词是否作为**完整词元**落在任一 haystack 里，容忍屈折变化。"""
    for h in haystacks:
        tk = toks(h)
        if word in tk:
            return True
        for suf in SUFFIXES:
            if word.endswith(suf):
                stem = word[:-len(suf)]
                if len(stem) > 2 and (stem in tk or (stem + 'e') in tk):
                    return True
        for suf in ('ing', 'ed', 'es', 's', 'ly'):
            if (word + suf) in tk:
                return True
    return False


def book_ref(book):
    """取全书的参照词集，用于判定「凭空造词」。

    返回 (词元集合 or None, 来源说明)。`text/` 优先（逐章口径，最权威），
    否则退回 epub。两者都没有 → None，该层判**无法判定**而非通过。

    分级依据与 check_vocab 的 A/B 裁决同源：
      词在参照集内 → 只是「不在本块」，不是造词（多半是中译英或章内他处）
      词全书查无     → 凭空造词 / 陈旧关键词，这才是要拦的
    """
    t = sorted(glob.glob(os.path.join(book, 'text', '*.txt')))
    if t:
        s = ' '.join(open(p, encoding='utf-8', errors='ignore').read() for p in t)
        return toks(norm(s)), 'text/（%d 个提取件）' % len(t)
    e = sorted(glob.glob(os.path.join(book, 'library', '*.epub')))
    if e:
        try:
            from verify_quotes import flat_alpha, epub_flat_text
            return toks(norm(flat_alpha(epub_flat_text(e[0])))), 'epub'
        except Exception as ex:
            return None, 'epub 读取失败（%s）' % ex
    return None, '无 text/ 且无 epub'


def scan_file(path):
    """返回 (hits, n_kw_lines, n_blocks_with_quote)。

    hits: [(行号, 关键词片段, 未锚定词)]
    以标题行为块边界；块内有引语则关键词向「引语 + 本块正文」两处求锚定。
    """
    lines = open(path, encoding='utf-8', errors='ignore').read().split('\n')
    hits = []
    gloss_only = []
    n_kw = 0
    blocks = []            # (quote_text, quote_lineno, [(行号, 关键词行内容)])
    cur_quote, cur_ln, cur_kws = None, -1, []

    def flush():
        if cur_quote is not None or cur_kws:
            blocks.append((cur_quote, cur_ln, cur_kws))

    for i, ln in enumerate(lines, 1):
        # 标题里也可能内嵌引语（`### 第三处：…「…」`）——先判引语再判标题，
        # 否则这种块会被当成纯标题丢掉（第一版 n_qblocks 少算 1 的原因）
        q = is_quote_line(ln)
        if q:
            flush()
            # 标题内嵌引语（`### 第三处：…「…」`）**不立即 flush**——它下面的
            # 中文理解/关键词/为什么这样写都属于这条引语，由下一个标题来收尾。
            cur_quote, cur_ln, cur_kws = q, i, []
            continue
        if RE_HEADING.match(ln):
            flush()
            cur_quote, cur_ln, cur_kws = None, -1, []
            continue
        mk = RE_KW.search(ln)
        if mk:
            n_kw += 1
            cur_kws.append((i, mk.group(1)))
    flush()

    n_qblocks = 0
    for quote, qln, kws in blocks:
        if not quote or not kws:
            continue                       # 无引语的块不判（绝不跨块配对）
        n_qblocks += 1
        qn = norm(quote)
        # 本块正文 = 引语行之后、下一个引语行/标题之前的全部内容，但
        # **排除关键词行本身**——否则每个关键词词都在「正文」里找到自己，
        # 检查自我满足、恒为 0（第一版合成样本抓不到的根因）。
        # 关键词行用 continue 跳过而非 break 截断：本库通行顺序是
        # 引语 → 中文理解 → **关键词** → 为什么这样写，而 AGENTS 第 9 条 b
        # 要的「语境延伸词呼应」恰恰写在**关键词之后**的「为什么这样写」里，
        # 一 break 就把这唯一合法的豁免证据切掉了（实测假阳 4→7 的根因）。
        seg = []
        for ln in lines[qln:]:
            if RE_HEADING.match(ln) or is_quote_line(ln):
                break
            if RE_KW.search(ln):
                continue                   # 跳过但不截断
            seg.append(ln)
        body_norm = norm(' '.join(seg))
        for ln, text in kws:
            for w, glossed in words_of(text):
                if anchored(w, qn, body_norm):
                    continue
                if glossed:
                    gloss_only.append((ln, text.strip()[:40], w))
                else:
                    hits.append((ln, text.strip()[:40], w))
    return hits, n_kw, n_qblocks, gloss_only


def main():
    args = sys.argv[1:]
    quiet = '--quiet' in args
    pos = [a for a in args if not a.startswith('--')]
    if not pos:
        raise SystemExit('用法: check_anchor.py "<书目录>" [--quiet]')
    book = pos[0]
    mds = sorted(glob.glob(os.path.join(book, '*.md')))
    if not mds:
        print('该目录下无 md 文件：%s' % book)
        return 0

    total = n_kw = n_qblocks = n_gloss = 0
    n_fab = n_loose = n_undet = 0
    ref, ref_src = book_ref(book)
    fab, loose, undet = [], [], []
    for md in mds:
        hits, k, qb, gloss = scan_file(md)
        n_kw += k
        n_qblocks += qb
        n_gloss += len(gloss)
        name = os.path.basename(md)
        if hits and not quiet:
            for ln, phrase, w in hits:
                print('  %s:%d  未锚定 关键词「%s」中的「%s」既不在引语、也不在本块正文'
                      % (name, ln, phrase, w))
        if gloss and not quiet:
            for ln, phrase, w in gloss:
                print('  %s:%d  提示   关键词「%s」中的「%s」仅有中文注释、无英文呼应'
                      % (name, ln, phrase, w))
        for ln, phrase, w in hits:
            item = (name, ln, phrase, w)
            if ref is None:
                undet.append(item)
            elif w in ref:
                loose.append(item)
            else:
                fab.append(item)
    total = len(fab) + len(loose) + len(undet)
    n_fab, n_loose, n_undet = len(fab), len(loose), len(undet)

    name = os.path.basename(book.rstrip('/'))
    print('=== 关键词锚定自查（%s）===' % name)
    print('  扫 %d 个 md，%d 个引语块，%d 条关键词行' % (len(mds), n_qblocks, n_kw))
    if n_kw == 0:
        print('  ❓ **无法判定**：0 条关键词行 —— 本书未被检查，不等于通过。')
        print('     （实测 the-morningside 有 585 条引语却 0 条 `**关键词**` 行，')
        print('      该书用的是 `**中文**` / `**情绪**` 等自造标签，需按该书格式另行适配）')
        return 2
    if n_qblocks == 0:
        print('  ❓ **无法判定**：有 %d 条关键词行但 0 个引语块 —— 引语格式未覆盖。' % n_kw)
        return 2
    print('  判定口径：引语 **或** 本块分析正文（AGENTS 第 9 条 b 的语境延伸词豁免）')
    print('  参照集：%s' % ref_src)
    print('  ❌ 凭空造词 %d 处（词全书查无）' % n_fab)
    print('  ⚠️ 松散关键词 %d 处（词在全书内、只是不在本引语块——多半是中译英或章内他处）' % n_loose)
    if n_undet:
        print('  ❓ 无法判定 %d 处（无参照集，不能断言造词）' % n_undet)
    if n_gloss:
        print('  ⚠️ 仅中文注释 %d 处' % n_gloss)
    if n_fab and not quiet:
        print('  ── 凭空造词明细 ──')
        for md, ln, phrase, w in fab:
            print('     %s:%d  「%s」← 关键词「%s」' % (md, ln, w, phrase))
    return 1 if n_fab else 0


if __name__ == '__main__':
    sys.exit(main())
