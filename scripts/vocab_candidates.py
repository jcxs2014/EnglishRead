#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""词表候选 → **可直接粘贴的三档表格行**（从 text/ 里抽，不靠回忆）

为什么有这个脚本（2026-09-26 the-glass-girl 六章实测）：

  AGENTS 8.2 的禁令 1 / 1a / 1a-2 / 1a-3 / 1b **全部是「检查型」规则**——
  它们要求「写完验」「逐条验」「用原形」。实测六章词表初稿缺陷率
  **14%–43%，补齐 1a-2 之后是 43% → 42%，几乎没变**：

      ch33 2/14 · ch45 3/17 · ch05 3/13 · ch11 6/22 · ch24 6/19
      ch04 9/21 · ch06 10/24

  1a-2 改变的只是**发现时机**（当场 vs 写完），不是**缺陷率**。
  ⇒ **检查型规则不可能让缺陷不发生。**

  而缺陷的唯一来源是同一个动作：**凭印象写词条**。
  逐条比对证实——凡是从「候选搜索的输出」里抄的条目，缺陷 0；
  凡是「候选只给 6–9 条、为凑满三档而从记忆里补」的，缺陷全在那里
  （ch04 的伪造 `dissolve`/`hunched`/`belch` + 跨章污染；
   ch06 的 10 条伪造同理）。

  ⇒ 治法不在「加一条检查」，在**删掉回忆这一步**：
  **让本脚本直接把表格行打出来，词条与例句都来自 text/，我只填释义。**
  这样「例句伪造」与「词头非原形」两种缺陷**在结构上不可能发生**
  （两者都由脚本从原文取），我唯一可能写错的只剩释义——那是 WARN 不是 FAIL。

用法：
    python3 scripts/vocab_candidates.py "<书目录>" --ch 8 [--min-len 8] [--tiers]
    python3 scripts/vocab_candidates.py "<书目录>" --ch 8 --words-only

输出：markdown 表格行（含三档分组），直接粘进 `## 本章词汇` 即可。
分档是**建议**（按长度 + 常见词表启发式），可自行调换；档位错了只报 WARN。
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chapter_text_path import require_chapter_text

# ── 高频常见词：出现在这里的不算「高级」 ────────────────────────────────
COMMON = set("""
the and you that have this for not with but they from like was were been being
have has had does did will would can could should shall may might must
about after again against all almost along already also always am among another
any anyone anything are around because been before behind below beneath beside
between both but by came can cannot come could did do does doing done down
during each either else enough even ever every everybody everyone everything
few first for from further get give go going gone good got great had half has
have her here hers herself him himself his how however i if in indeed instead
into is it its itself just keep kept last least less let like little long look
looked looking looks made make many may maybe me might mine more most much must
my myself never next no nobody none nor not nothing now of off often on once
one only or other others otherwise ought our ours ourselves out over own per
perhaps put quite rather really said same say says seem seemed seems seen self
shall she should since so some somebody someone something sometimes soon still
such sure take taken than that the their theirs them themselves then there these
they thing things think this those though through thus time to too under until
up upon us use used very was way we well went were what whatever when whenever
where whereas whether which while who whoever whom whose why will with within
without would yet you your yours yourself yourselves
""".split())

# 明显不是"生词"的形态/专名噪声（按需增补）
NOISE = set("""
because chapter every chapter sunday monday tuesday wednesday thursday friday
saturday prologue epigraph author copyright isbn www http https com org
""".split())

# ── 透明词（2026-09-26 ch07 实测后新增）─────────────────────────────
# 症状：脚本的基础档给出 `find` / `file` / `drawer` / `grab` / `room` /
# `front` / `calls` —— 这些是**透明词**（读者不需要查），我嫌它们
# 「太像不值当列进词表」，**整档换成了从记忆里写的词**（`pack` / `throw up` /
# `hang out` / `make up` / `stare at`），结果 8 条里 5 条出缺陷
# （1 伪造 + 4 词典式词头）。
#
# ⇒ **根因是黑名单漏了透明词，不是使用者的疏忽。**
# 与 COMMON 的区别：COMMON 挡的是「高频语法功能词」，TRANSPARENT 挡的是
# 「高频但仍被当词表候选吐出来的内容词」——两者都要挡。
# ⚠️ 增补 TRANSPARENT 时注意：把某个**本章真实要收录的词**加进来会造成漏，
#   所以只加「任何一章都不值得单列」的那类。
TRANSPARENT = set("""
find finds found grab grabs grabbed file files filed drawer drawers room rooms
front fronts call calls called calling keep keeps kept put puts putting
look looks looked come comes came get gets got give gives gave
take takes took make makes made move moves moved open opens opened close closes
closed sit sits sat stand stands stood wait waits waited try tries tried
want wants wanted need needs needed know knows knew think thinks thought
feel feels felt say says said tell tells told ask asks asked
work works worked live lives lived walk walks walked talk talks talked
play plays played turn turns turned help helps helped start starts started
leave leaves left begin begins began happen happens believe believes
remember remembers understand understands mean means meant seem seems
""".split())


def chapter_text(book_dir, ch):
    """定位 text/chNN*.txt —— 收口到 chapter_text_path（唯一共用实现）。

    本函数此前内联一份判定（只认 `_`/`chNN` 前缀），与 gen_overview、
    check_chapter_quotes 的同一缺陷在一个批次里复发三次：
    根 AGENTS.md 规定精读文件名唯一分隔符是**空格**（`ch01 1 the house.md`），
    而三份代码都只认下划线 ⇒ 用空格命名的书一律 SystemExit「找不到 chN 的提取件」
    （假红型：工具坏了而内容没问题）。
    共用实现见 scripts/chapter_text_path.py：分隔符 `_` / `.` / 空格 + 章号 1/2/3/4 位。
    """
    return require_chapter_text(book_dir, ch)


# ⚠️ 2026-10-06 修（In the Woods They Wait ch07 实测）：小数点被当成句号。
# 原文 `1.2 million acres of mountainous terrain`，旧正则切出「句」=
# `2 million acres of mountainous terrain, almost two thousand square miles…`
# —— 它**确实是逐字子串**（所以 V2 过、check_vocab 过、六道门禁全绿），
# 但**把数字说错了**（1.2 million 变成 2 million）。
# 这是「词中截断」盲区在**数字**上的同型，而且比词中截断更坏：词断错读者能看出来，
# 数字断错是一句通顺的假话。
# 修法：`.` 前后都是数字时**不切**（负数/缩写如 U.S. 同样受益）。
#
# ⚠️ 2026-10-06 修（ch18 实测，同型第三例）：**单字母缩写**的点号也被当句末。
# 原文 `The digital clock read 3:15 a.m.` 被切成 `… 3:15 a.`——
# 逐字为真（V2/六道门禁全绿）但**缩写被腰斩**。
# 判据：`.` 的**前一个字符是单个字母、且那个字母本身前面是词边界**（即 `a.` `m.` `p.`）
#       时不切。`U.S.` 这类连续单字母的点号也已覆盖（每段都满足该判据）。
# ⚠️ 2026-10-06 修（ch18 实测，同型第三例）：**单字母缩写**的点号也被当句末。
# 原文 `The digital clock read 3:15 a.m.` 被切成 `… 3:15 a.`——逐字为真
# （V2/六道门禁全绿）但**缩写 `a.m.` 被腰斩成 `a.`**。
# 变长 lookbehind 在纯正则里做不到（`(?<!X\.)` 定长不够），所以改为：
# **先按点号全切，再把「以单字母缩写点结尾」的碎片与下一片合并**（见 _merge_abbrev）。
# 判据：片段以 `词边界+单字母+.` 结尾（a. m. p.）⇒ 该点是缩写的一部分。
_SENT_RE = re.compile(r'[^.!?\n]*?\.(?![0-9])[.!?]*|(?:[^.!?\n]*[!?]+)(?=\s|$)')
_ABBREV_TAIL = re.compile(r'\b[A-Za-z]\.$')


def _merge_abbrev(parts):
    """把以「单字母缩写点」结尾的片段与下一片段合并（a. + m. => a.m.）。

    ⚠️ 返回的列表**比输入短**（合并吞并了下一条），所以**不能**再拿它和
    输入的等长 starts 列表 zip——那会把合并点之后的每个偏移**整体错位一格**。
    实测（Some Other Time ch28）：`Thursday, 12:01 a.` + `m.` 合并后，
    `zip(segs, starts)` 把 segs[1] 配到了 starts[1]（指向 'm.'），
    于是 real_sentence('custodial') 返回的是**另一句** "Bunny is indeed sick."。
    ⇒ 需要偏移时必须用 _merge_abbrev_spans()，不要用本函数的返回值配 starts。
    """
    merged, i = [], 0
    while i < len(parts):
        cur = parts[i]
        # 连续吞并：a. | m. | She… ⇒ a.m. She…
        while (_ABBREV_TAIL.search(cur) and i + 1 < len(parts)
               and re.fullmatch(r'[A-Za-z]\.', parts[i + 1])):
            cur += parts[i + 1]
            i += 1
        merged.append(cur)
        i += 1
    return merged


def _merge_abbrev_spans(pairs):
    """同 _merge_abbrev，但输入/输出都带**起始偏移**：(seg, start) 列表。

    合并时保留**组内第一个片段**的 start（缩写还原后该句仍从原处开始）。
    """
    out, i = [], 0
    while i < len(pairs):
        cur, st = pairs[i]
        while (_ABBREV_TAIL.search(cur) and i + 1 < len(pairs)
               and re.fullmatch(r'[A-Za-z]\.', pairs[i + 1][0])):
            cur += pairs[i + 1][0]
            i += 1
        out.append((cur, st))
        i += 1
    return out


# ⚠️ 2026-10-20 修（Ebenezer Scrooge 实测，13 章共 25 条例句引号不闭合）：
# **对话引号内的句点被当成句末** ⇒ 例句被腰斩在引号内。
#   原文 `“Splendid.” Tap, tap, tap went…` 被切成 `“Splendid.` + `” Tap, tap…`；
#   原文 `“But I should say … as soon as we drew near to our destination.` 被切成
#   一个**没有闭引号**的半句话（那段的引号要到几段之后才闭合）。
#   ⇒ 例句**确实是原文的连续子串**（所以 V2 / check_vocab / 六道门禁全绿），
#   但**引号不闭合**、后半句被当成独立的下一句 ⇒ 词表里出现「半句话」。
#   实测全库 `notes/books/` 词表例句 123,031 行里 1,729 行（1.4%）引号不闭合，
#   涉及 613 个文件 ⇒ **既有工具缺陷，不是某一本书的问题**。
#
# 修法（**只调整引号字符的归属，不增删任何实词，也不塌陷候选**）：
#   ① **贴尾**：片段以 `.`/`!`/`?` 结尾、而原文紧随其后的字符是 `”` ⇒ 把那个 `”` 算进本片段
#      （`“Splendid.` ⇒ `“Splendid.”`）。这是**把本来就在原文里、紧挨着的字符算进来**，
#      不是新增。
#   ② **去首游离引号**：片段**开头**的 `“` 或 `”` 若在本片段内找不到配对 ⇒ 去掉它
#      （`“But I should say…` ⇒ `But I should say…`；`” he murmured.` ⇒ `he murmured.`）。
#      去掉后仍是原文的**连续子串**（少一个开头的字符），且引号立刻成对。
#   ③ 若仍不成对 ⇒ `pick_sentence` **放弃**该条（宁可少一条，也不造半句话）。
#
# ⚠️ **已否决的两条路线**（实测都会塌陷候选）：
#   · 屏蔽引号内的点号 ⇒ 整段对白并成一句 → 超 maxlen → ch09 候选 91 → 38；
#   · 向后合并到闭引号 ⇒ 同上（整段对白成为一句）→ 候选 91 → 13。
#   ⇒ 本修法**不改变切句边界**，只处理引号字符的归属。
_QUOTE_PAIRS = {'“': '”'}


def _quotes_balanced(seg):
    """片段里的**双引号**是否成对。

    ⚠️ **不检查 `‘`/`’`**（2026-10-20 实测踩坑）：ch09 原文 `‘` 8 个、`’` **29 个**——
    `’` 绝大多数是**撇号**（`I’m` / `don’t`）。若把 `’` 当闭引号计数，
    几乎每个含撇号的片段都被判成「引号不闭合」，实测候选从 91 条塌到 **2 条**。
    本库 text/ 里引号全是弯引号（直引号 `"` 计数为 0）。
    """
    for o, c in _QUOTE_PAIRS.items():
        if seg.count(o) != seg.count(c):
            return False
    return True


def _split_unbalanced(seg, st):
    """把**引号不成对**的片段切成若干**引号成对**的连续子串。

    切法：**在每一个引号字符处切开，并跳过该引号** ⇒ 每一片都无引号 ⇒ 必然成对。
    切出的每片仍是原文的**连续子串**（只少了那个引号字符本身）。

    ④ 为什么必须这么做（2026-10-20 实测）：`pick_sentence` 有「引号不成对就放弃」的守卫，
    而切句正则把**对话引号内的句点**当句末 ⇒ 大量句子被整条丢弃，
    **词头凭空消失**（实测 `ground` / `pavement` / `scene` / `spirit` 在工具输出里查无）。
    ⇒ 丢弃 ⇒ 写作侧退化成「凭印象手写词表」——正是缺陷率最高的老路。

    例：
      `Upon the pavement, Scrooge asked the lady: “Are you absolutely certain…`
        ⇒ `Upon the pavement, Scrooge asked the lady:` / `Are you absolutely certain…`
      `Although…” She cast her eyes towards the ground.`
        ⇒ `Although…` / `She cast her eyes towards the ground.`
    """
    pieces, start, i, n = [], 0, 0, len(seg)
    while i < n:
        ch = seg[i]
        if ch in ('“', '”'):
            head = seg[start:i]
            if head.strip():
                # ⚠️ 必须 lstrip：pick_sentence 有「句首须是字母/开引号」的守卫，
                # 带前导空格的片段会被它整条丢弃（实测 `ground` 就是这样丢的）。
                off = len(head) - len(head.lstrip())
                pieces.append((head.strip(), st + start + off))
            start = i + 1          # 跳过这个引号字符
        i += 1
    tail = seg[start:]
    if tail.strip():
        off = len(tail) - len(tail.lstrip())
        pieces.append((tail.strip(), st + start + off))
    return pieces


def _fix_fragment_quotes(seg, st, src):
    """修一个片段的引号归属，返回**片段列表** [(文本, 起点), ...]。

    ① **贴尾**：片段以 `.`/`!`/`?` 结尾、而原文紧随其后的字符是 `”` ⇒ 把那个 `”` 算进本片段
       （`“Splendid.` ⇒ `“Splendid.”`）。这是**把本来就在原文里、紧挨着的字符算进来**，
       不是新增。
    ② 片段若已引号成对 ⇒ 原样返回（保留 `“Splendid.”` 这类带引号的完整引语）。
    ③ 仍不成对 ⇒ 走 `_split_unbalanced` 切开。
    """
    # ① 贴尾
    tail = st + len(seg)
    if tail < len(src) and src[tail] == '”' and seg.count('“') > seg.count('”'):
        seg = seg + '”'
    # ② 已成对 ⇒ 原样
    if _quotes_balanced(seg):
        return [(seg, st)]
    # ③ 切开
    return _split_unbalanced(seg, st)


def sentences(src):
    """按句号/问号/叹号切句，保留原文标点（例句必须逐字）

    **小数点不是句号**（见 _SENT_RE 注释）：否则例句会从数字中间开始，
    造出「逐字但数字说错」的例句——这类损坏所有子串式门禁都看不见。
    **单字母缩写点也不是句末**（a.m. / U.S. / p.m.）：由 _merge_abbrev 合并还原。

    ⚠️ 小数点的真实坑（ch07 `1.2` ⇒ 切出 `2 million`）：
    正则 `(?![0-9])` 只在「点号后紧跟数字」时拒绝该切点，但**引擎会把匹配起点
    后移到那个数字**，于是产出「从数字中间起头」的碎片——是逐字子串，却把数字说错。
    ⇒ **切句前把「数字.数字」的点号换成哨兵字符（不出现在正文里），切完再换回**。
       这样点号彻底不参与切分，`1.2 million` 自然留在同一句，且**不会误伤**完整句。
    """
    SENT = '\x00'          # 哨兵：正文中不可能出现，避免与任何字符冲突
    src2 = re.sub(r'(?<=\d)\.(?=\d)', SENT, src)      # 1.2 -> 1<SENT>2
    raw = []
    for m in _SENT_RE.finditer(src2):
        s = m.group(0).replace(SENT, '.').strip()     # 还原
        if s:
            raw.append((s, m.start()))
    # 合并缩写：把 a. | m. 还原成 a.m.
    # ⚠️ 必须用**带偏移**的合并版：segs 比 raw 短，用 zip(segs, starts)
    # 会把合并点之后的偏移整体错位（实测 ch28 custodial 取到别的句子）。
    merged = _merge_abbrev_spans(raw)
    # 修引号归属（2026-10-20）：贴尾 `”`、不成对则按引号切开
    out = []
    for seg, st in merged:
        out.extend(_fix_fragment_quotes(seg, st, src))
    return out


def pick_sentence(sents, pos, src, maxlen=140):
    """取包含 pos 的那句；太长就放弃（宁可少一条，也不造碎片）"""
    for s, st in sents:
        if st <= pos < st + len(s) + 2:
            # 必须像个完整句子：以字母或开引号开头，且不是引号残片
            if not re.match(r'^[“‘\'A-Za-z0-9]', s):
                return None
            # ⚠️ 2026-10-06 补左边界守卫（ch07 `2 million` 实测）：
            # 即使切句正则漏了，若「句首」紧贴在数字之后，说明仍是从数字中间起的
            # （如 `1.2` 被切成 `2`）。左边界紧邻数字 ⇒ 判为碎片，直接放弃。
            if st > 0 and src[st - 1].isdigit():
                return None
            if st > 0 and src[st - 1] == '.' and st > 1 and src[st - 2].isdigit():
                return None
            if len(s) > maxlen:
                return None
            # ⚠️ 2026-10-20：引号必须成对。原文本身引号残缺时**放弃**这条，
            # 而不是「补一个闭引号」——补出来的字符原文里没有，是伪造。
            if not _quotes_balanced(s):
                return None
            return s
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('book_dir')
    # ⚠️ type=str：本库有 `ch02a` 型后缀章号（韵文/插叙节挂在上一章后面）。
    # type=int 会让这类章**根本取不到候选集**，写作侧只能退化成「凭印象手写词表」——
    # 而那正是缺陷率最高的老路（AGENTS 第 8 条 8.2 禁令 1a）。章号串交给
    # chapter_text_path.split_chapter_key 拆「数字 + 后缀字母」。
    ap.add_argument('--ch', type=str, required=True)
    ap.add_argument('--min-len', type=int, default=8)
    ap.add_argument('--max-sent', type=int, default=140)
    ap.add_argument('--words-only', action='store_true', help='只列词，不带例句/表格')
    ap.add_argument('--tiers', action='store_true', help='按启发式分三档输出')
    ap.add_argument('--limit', type=int, default=40)
    a = ap.parse_args()

    # ⚠️ 章号参数归一化：CLI 传 `--ch 18` 与 `--ch ch18` 都应可用。
    # 原实现直接 a.ch 透传给 require_chapter_text，后者对 'ch18' 做 int() ⇒ ValueError 崩。
    # 判据（一行）：**CLI 参数不该要求调用方记住「传数字不传前缀」**——
    #   带不带 ch 前缀是同义词，工具自己该吸收这个差异。
    s_arg = str(a.ch).strip()
    key = s_arg[2:] if s_arg.lower().startswith('ch') else s_arg
    # ⚠️ 2026-10-17 修（The Unsolvable Case 实测）：后缀字母**必须保留**。
    #   原实现对 `digits` 做 `int()` ⇒ `--ch 01b` 直接 SystemExit「只接受章号」，
    #   于是**带插叙节的书（ch01b/ch03b…，此前还有 Everything Is Poison 的
    #   ch02a/ch18a）拿不到候选集**，`build_vocab_section.py` 只能退 2：
    #   词汇层对这类章节整体不可生产。而 `chapter_text_path.split_chapter_key`
    #   本来就收 `02a`（它专门为此写过 docstring）⇒ 是本 CLI 自设的窄口。
    if not re.fullmatch(r'\d+[a-z]?', key, re.I):
        raise SystemExit('❌ --ch 只接受章号（18 / ch18 / 02a），收到：%r' % a.ch)
    a.ch = key.lower()

    path = chapter_text(a.book_dir, a.ch)
    src = open(path, encoding='utf-8').read()
    sents = sentences(src)

    seen, rows = set(), []

    # ── 基础档：优先「短名词短语 / 介词短语」（2026-09-26 ch07 实测后加）──
    # 症状：基础档原本按「4..min_len-1 的单词」抽，给出 find / file / drawer /
    # grab / room / front / calls —— 全是**透明词**，我因此整档换成记忆里的词，
    # 8 条里 5 条出缺陷。
    # ⇒ 基础档改为抽**短语**：`a doctor's note` / `on probation` /
    # `an extension` / `file drawer` 这类**学习者真会查的块**。
    # 短语按出现次数降序（出现多次 = 本章更核心），且限定 2–3 词。
    PHRASE_RE = re.compile(
        r"\b(?:a|an|the|my|your|his|her|their|our)\s+"
        r"([a-z][a-z'-]*(?:\s+[a-z][a-z'-]*)?)"
        r"|\b(on|in|at|to|for|of|with|without|from|by|into|out of|off|down|up)\s+"
        r"([a-z][a-z'-]*(?:\s+[a-z][a-z'-]*)?)", re.I)
    ph_count, ph_pos = {}, {}
    for m in PHRASE_RE.finditer(src):
        tail = (m.group(1) or m.group(2) or '').strip()
        words = tail.split()
        if not words or len(words) > 2:
            continue
        if any(w.lower() in COMMON or w.lower() in TRANSPARENT for w in words):
            continue
        if any(len(w) < 3 for w in words):
            continue
        key = ' '.join(words).lower()
        ph_count[key] = ph_count.get(key, 0) + 1
        ph_pos.setdefault(key, m.start())

    sents_cache = sents
    # 末词是动词性词时**整条丢弃**（实测产出过垃圾块 `bench trying`：
    # 原文 `...over the bench trying to get out` —— 介词 + 名词 + 动词
    # 不构成可学的短语）。宁可少一条，也不给假短语。
    VERBY = {'trying', 'getting', 'going', 'doing', 'saying', 'telling', 'looking',
             'working', 'sitting', 'standing', 'walking', 'talking', 'being',
             'having', 'making', 'taking', 'putting', 'using', 'letting',
             'coming', 'feeling', 'thinking', 'knowing', 'seeing',
             'wanting', 'needing', 'giving'}
    for key in sorted(ph_count, key=lambda k: (-ph_count[k], k)):
        if sum(1 for r in rows if r[0] == '⭐') >= max(8, a.limit // 3):
            break
        words = key.split()
        _orig = key          # 保底：查 ph_pos 用原短语键
        if words[-1].lower() in VERBY:
            continue
        # ⚠️ 二词短语的末词若是分词/副词/过去式，说明**名词短语还在继续**
        # （实测 ch09 原文 `the bell ending lunch rings` 被抽成 `bell ending`
        #  ——伪块）。**截断为一词**而不是丢弃（`bell` 本身仍是合格基础词）。
        if len(words) == 2 and re.search(r'(ing|ly|ed)$', words[1]):
            words = words[:1]
            if words[0] in seen:
                continue
            # ⚠️ **只改展示用的 key，不改 ph_pos 的查表键**——否则
            # `pos = ph_pos['bell']` 会 KeyError（ph_pos 是按原短语建的）。
            # 这个 bug 让 ch09 直接崩溃，而我的回归脚本把崩溃当成
            # 「0 条候选、0 缺陷」——**"0" 又一次来自工具坏掉**。
            key = words[0]
        pos = ph_pos[_orig]
        ex = pick_sentence(sents_cache, pos, src, a.max_sent)
        if not ex:
            continue
        # 短语必须在例句里**逐字**出现（保留原文大小写与撇号形态）
        m2 = re.search(r'\b' + r'[\s\S]{0,12}?'.join(
            re.escape(w) for w in re.findall(r"[A-Za-z][A-Za-z'-]*", key)) + r'\b', ex)
        if not m2:
            continue
        surface = m2.group(0).strip()
        rows.append(('⭐', surface, ex, pos))
        seen.update(w.lower() for w in key.split())

    # 高级/进阶：min_len 以上的"生词"候选
    for lo, hi, tiers in ((a.min_len, 0, True),):
        # ⚠️ 实现坑：无上限时必须用 `{lo-1,}`，不能写 `{lo-1,0}`
        #（min > max 会抛 re.PatternError: min repeat greater than max repeat，
        #  位置 19）。第一版就这么写错了一次。
        quant = (r"[A-Za-z'-]{%d,}" % (lo - 1)) if not hi \
            else (r"[A-Za-z'-]{%d,%d}" % (lo - 1, hi - 1))
        for m in re.finditer(r"[A-Za-z]" + quant, src):
            w = m.group(0)
            lw = w.lower()
            if lw in COMMON or lw in NOISE or lw in TRANSPARENT or lw in seen:
                continue
            ex = pick_sentence(sents, m.start(), src, a.max_sent)
            # ⚠️ 实现坑：必须用**词边界**判词头是否在例句里，不能用 `w in ex`
            # —— 否则截断词 `poundin` 会被 `pounding` 命中而通过。
            # 实测第一版就这样产出了 `poundin` / `favorit` 两个截断词条，
            # 而 AGENTS 早就写明「短词/词根 grep 必须加词边界」。
            if not ex or not re.search(r'(?<![A-Za-z])' + re.escape(w) + r'(?![A-Za-z])', ex):
                continue
            seen.add(lw)
            if not tiers:
                tier = '⭐'
            else:
                tier = '⭐⭐⭐' if len(w) >= 10 else '⭐⭐'
            rows.append((tier, w, ex, m.start()))
    # 每档限量，避免某一档（例如 4 字母短词）淹没其余两档
    cap = {'⭐⭐⭐': a.limit, '⭐⭐': a.limit, '⭐': max(8, a.limit // 3)}
    kept = []
    for t in ('⭐⭐⭐', '⭐⭐', '⭐'):
        n = 0
        for r in [x for x in rows if x[0] == t]:
            if n >= cap[t]:
                break
            kept.append(r)
            n += 1
    rows = kept

    if a.words_only:
        for t, w, ex, _ in sorted(rows, key=lambda r: (r[0], r[3])):
            print('  %-4s %-16s %s' % (t, w, ex[:a.max_sent]))
        print('\n  共 %d 个候选' % len(rows))
        return

    # 按档分组输出（否则档位表头会重复出现，实测踩过）
    order = ['⭐⭐⭐', '⭐⭐', '⭐']
    grouped = {t: [r for r in rows if r[0] == t] for t in order}
    if a.tiers:
        for t in order:
            if not grouped[t]:
                continue
            name = {'⭐⭐⭐': '高级', '⭐⭐': '进阶', '⭐': '基础'}[t]
            print('\n### %s %s\n' % (t, name))
            print('| 词/短语 | 释义 | 例句 |')
            print('|---|---|---|')
            for _, w, ex, _pos in grouped[t]:
                print('| %s | （释义待填） | %s |' % (w, ex))
    else:
        for t, w, ex, _pos in sorted(rows, key=lambda r: (r[0], r[3])):
            print('| %s | （释义待填） | %s |' % (w, ex))
    print('\n<!-- 候选 %d 条（高级 %d / 进阶 %d / 基础 %d）｜ 全部来自 %s ｜'
          ' 词头与例句均为原文逐字 -->'
          % (len(rows), len(grouped['⭐⭐⭐']), len(grouped['⭐⭐']), len(grouped['⭐']),
             os.path.basename(path)))


if __name__ == '__main__':
    main()
