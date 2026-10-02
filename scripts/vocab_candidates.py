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


def sentences(src):
    """按句号/问号/叹号切句，保留原文标点（例句必须逐字）"""
    out = []
    for m in re.finditer(r'[^.!?\n]*[.!?]+(?=\s|$)', src):
        s = m.group(0).strip()
        if s:
            out.append((s, m.start()))
    return out


def pick_sentence(sents, pos, src, maxlen=140):
    """取包含 pos 的那句；太长就放弃（宁可少一条，也不造碎片）"""
    for s, st in sents:
        if st <= pos < st + len(s) + 2:
            # 必须像个完整句子：以字母或开引号开头，且不是引号残片
            if not re.match(r'^[“‘\'A-Za-z0-9]', s):
                return None
            if len(s) > maxlen:
                return None
            return s
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('book_dir')
    ap.add_argument('--ch', type=int, required=True)
    ap.add_argument('--min-len', type=int, default=8)
    ap.add_argument('--max-sent', type=int, default=140)
    ap.add_argument('--words-only', action='store_true', help='只列词，不带例句/表格')
    ap.add_argument('--tiers', action='store_true', help='按启发式分三档输出')
    ap.add_argument('--limit', type=int, default=40)
    a = ap.parse_args()

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
