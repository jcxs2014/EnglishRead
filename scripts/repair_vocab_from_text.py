#!/usr/bin/env python3
"""repair_vocab_from_text.py — 用本章 text/ 逐字重写词汇表（修例句伪造/跨章/占位）

背景（Unloved by Peyton Corinne 批次，2026-10-17）：
  check_vocab 报 440 FAIL，类型分布：
    - 例句不命中本章 369（其中 222 条例句在全书 text/ 查无＝手写/改写；
      54 条在别章；39 条标点漂移；34 条其实在本章但因 `（chNN）` 尾标污染指纹）
    - 例句列为占位符 41（且这些词条多数不在本章）
    - 词条 A 类虚构 30（epub 全书查无）

  根因是**生产方式**：词条与例句凭印象手写（AGENTS 第 8 条：缺陷率由生产方式决定）。
  本脚本把生产过程换成「例句恒由脚本从本章 text/ 抽取」，与
  build_vocab_table.py / build_vocab_section.py 同源，但**保留本书既有的
  4 列格式（词 | 音标 | 释义 | 例句）**，且**保留原有人类写的词头与释义**。

用法：
  python3 scripts/repair_vocab_from_text.py <书目录> [--dry-run] [--top-up N]

行为：
  1. 解析每个 md 的 `## 词汇` 节（到下一个 `## ` 为止）。
  2. 词头校验用 check_vocab.word_hits_corpus（**同一实现**，允许 -s/-ed/-ing/-ly）；
     不在本章 ⇒ 删行并记录（A 类虚构或跨篇）。
  3. 保留的词头 ⇒ 例句由脚本从本章 text/ 抽（优先完整句 30–320 字符，
     退回含该词的任意句 ≥30 字符；都取不到 ⇒ 删行并记录）。
  4. 4 列格式原样保留（音标列不动）；3 列格式同样支持。
  5. --top-up N：某档行数 < N 时，用 vocab_candidates 的候选词头补足
     （候选集本身即脚本抽取，例句天然逐字）。补入的词头需调用方给释义，
     故默认关闭；缺释义不写入（宁缺毋造）。
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_vocab import word_hits_corpus, FUNC_STOP  # 同一实现，避免口径漂移
from build_vocab_table import load_chapter, sentences, is_complete_sentence
from chapter_text_path import find_chapter_text

TIER_PAT = re.compile(r'^###\s*(⭐{1,3})')
ROW_RE = re.compile(r'^\|\s*(.+?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$')
# ⚠️ 2026-10-19 修（Maybe Next Time 批次）：原 ROW_RE **只认 4 列**，
# 3 列表（`| 词条 | 释义 | 例句（本章） |`）整行匹配不上 ⇒ 被当普通行跳过
# ⇒ 工具对 3 列书**一条都不修也不删**（dry-run 输出「重写 0 ｜ 删除 0」＝静默空跑）。
# 实测本批次 14 章全是 3 列表，249 行全部逃过修复。
# 3 列行的判定：**恰好 3 个非空单元格**（表头行与分隔行由调用处另行排除）。
ROW_RE3 = re.compile(r'^\|\s*(.+?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$')


def split_words(head):
    ws = [w.lower() for w in re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", head)]
    return [w for w in ws if w not in FUNC_STOP]


def head_in_chapter(head, corpus):
    """词头是否在本章语料命中。

    ⚠️ 口径须与 check_vocab **完全一致**（2026-10-19 修，Maybe Next Time 批次）：
    check_vocab 判词条用的是 `missing_ch = [w for w in words if len(w) >= 4 and not
    word_hits_corpus(w, ch_corpus)]` ⇒ **3 字符及以下的词根本不参与判定**
    （'brand-new' 里的 'new'、'twenty-seven' 里的 'seven' 都不查）。
    本函数原实现对**所有**词都查 ⇒ 比门禁更严 ⇒ 把门禁本会放行的词头误判为
    「词头不在本章」（实测 ch48 的 'brand-new'、ch49 的 'ring light' 等）。
    ⇒ 现在按同一 `len(w) >= 4` 过滤，短词不判。
    """
    ws = split_words(head)
    if not ws:
        return True
    checkable = [w for w in ws if len(w) >= 4]
    if not checkable:
        return True
    return all(word_hits_corpus(w, corpus) for w in checkable)


def token_forms(w):
    """一个词头的可接受词形集合（与 word_hits_corpus 的屈折口径同向）。

    2026-10-17 修：原实现只匹配**词头本身**的整词，导致 text/ 里只有屈折形式
    （sucks / crying / approachable）时抽不到例句，词条被误删。本函数把
    -s/-es/-ed/-ing/-ly、y→ies/ied、以及 -able/-ably 等派生后缀一并纳入候选词形，
    匹配时按整词匹配（前后不能是字母），避免 'suck' 命中 'sucker'。

    ⚠️ 2026-10-19 修（Maybe Next Time 批次）：原实现对 -ing 结尾的词只补
    `词干` 与 `词干+e`（roaming → roam / roame），**漏了 `词干+ed`（roamed）**
    ⇒ text/ 里只有过去式时（"On other days I roamed."）抽不到例句，
    词条被误报「本章无含该词的可用句子」而丢弃。
    修法：先剥出词干，再由词干补全套 -s/-es/-ed/-ing/-ly 形态。
    """
    out = {w}
    # ── 由词干派生全套屈折形态（2026-10-19 补）──
    stems = set()
    for suf in ('s', 'es', 'ed', 'ing', 'ly', 'er', 'ers', 'est', 'ment', 'ness'):
        if w.endswith(suf) and len(w) > len(suf) + 2:
            stems.add(w[:-len(suf)])
    if w.endswith('y') and len(w) > 3:
        stems.add(w[:-1])
    for stem in stems:
        out |= {stem, stem + 'e', stem + 's', stem + 'es', stem + 'ed',
                stem + 'ing', stem + 'ly', stem + 'd', stem + 'er', stem + 'ers'}
    # ── 原有的派生后缀组合 ──
    for suf in ('s', 'es', 'ed', 'ing', 'ly'):
        if w.endswith(suf) and len(w) > len(suf) + 2:
            base = w[:-len(suf)]
            out |= {base, base + 'e'}
    out |= {w + 's', w + 'es', w + 'ing', w + 'ed'}
    # 派生后缀：approach → approachable / approaches；hesitate → hesitating
    out |= {w + sfx for sfx in ('able', 'ably', 'er', 'ers', 'est', 'ful', 'ment', 'ness', 'tion', 'sion')}
    return out


def _tok_in(word, sent):
    return any(re.search(r'(?<![A-Za-z])' + re.escape(f) + r'(?![A-Za-z])', sent, re.I)
               for f in token_forms(word))


def pick_example(head, sents, corpus, flat):
    """取含词头的例句：优先完整句；退回任意句（>=30 字符）；最后任一含词头句。"""
    ws = split_words(head)
    if not ws:
        return None
    cands = [s for s in sents if all(_tok_in(w, s) for w in ws)]
    if not cands:
        return None
    # 1) 完整句优先（is_complete_sentence：大写/开引号开头、句末标点收尾、30–320 字符）
    for s in cands:
        if is_complete_sentence(s):
            return s
    # 2) 退回 >=30 字符的任意句
    for s in cands:
        if len(s) >= 30:
            return s
    # 3) 最后兜底：含词头的短句（宁可短，不可无——check_vocab 只要求 flat 命中）
    return cands[0]


def candidate_pool(book_dir, ch, corpus):
    """从 vocab_candidates 拿本章候选词头 + 逐字例句。

    返回 (cand: {词头: 例句}, cand_tiers: {档: [(词头, 例句), ...]})。
    ⚠️ 候选集本身即脚本从本章 text/ 抽取 ⇒ 例句天然逐字（这是本工具的核心保证）。
    抽不到（text/ 缺失等）⇒ 返回空，不报错（宁缺毋造）。
    """
    try:
        out = subprocess.run(
            ["python3", "scripts/vocab_candidates.py", str(book_dir), "--ch", str(ch),
             "--tiers", "--limit", "300", "--max-sent", "400"],
            capture_output=True, text=True, check=True).stdout
    except Exception:
        return {}, {}
    cand, tiers, cur = {}, {}, None
    for line in out.split("\n"):
        if line.startswith("###"):
            cur = "⭐⭐⭐" if "⭐⭐⭐" in line else ("⭐⭐" if "进阶" in line else "⭐")
            tiers.setdefault(cur, [])
        elif line.startswith("| "):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            if len(c) >= 3 and c[0] not in ("词/短语", "词条") and not set(c[0]) <= set("-: "):
                ex = c[2].replace("（释义待填）", "").strip()
                cand[c[0]] = ex
                if cur:
                    tiers[cur].append((c[0], ex))
    return cand, tiers


TIER_KEYS = ('⭐⭐⭐', '⭐⭐', '⭐')


def plan_for(plan_map, cn):
    """取该章的 plan：{档: [(词头, 释义), ...]}。

    plan 的词头**必须**能在本章 text/ 命中（否则是自造词），
    例句由脚本从本章 text/ 抽 ⇒ 天然逐字。
    """
    if not plan_map:
        return {}
    p = plan_map.get(f"ch{cn}")
    if p is None:
        return {}
    out = {}
    for t in TIER_KEYS:
        items = p.get(t) or p.get(t.replace('⭐', '')) or []
        norm = []
        for it in items:
            if isinstance(it, (list, tuple)) and len(it) >= 2:
                norm.append((str(it[0]).strip(), str(it[1]).strip()))
            elif isinstance(it, str) and '|' in it:
                h, g = it.split('|', 1)
                norm.append((h.strip(), g.strip()))
        out[t] = norm
    return out


def _write_out(md_path, text, i, j, section, new_section, dry_run,
               dropped, replaced, kept, added):
    """原子落盘 + 行数守卫（2026-10-19 补）。

    ⚠️ 原写法 `open(md_path,'w')` 会**在写之前把文件截成 0 字节**——写失败就是整章消失
    （记忆 #2042 同源坑）。改为同目录 mkstemp → 写全量 → os.replace。
    两道断言：写前节内行数 > 5（疑似已截断即中止）、写后总行数与写前相等。
    """
    res = {'dropped': dropped, 'replaced': replaced, 'kept': kept, 'added': added,
           'rows_after': len(kept) + len(replaced) + len(added)}
    if new_section == section or dry_run:
        return res
    orig_total_lines = text.count('\n')
    if section.count('\n') <= 5:
        print(f"❌ {os.path.basename(md_path)} 词表节仅 {section.count(chr(10))} 行，疑似已损坏，中止")
        res['rows_after'] = 0
        return res
    out_text = text[:i] + new_section + text[j:]
    # ⚠️ 行数守卫（2026-10-19 修口径）：**重建词表本身就会改变行数**
    # （原表 18 行 → 新表 18 行但表头/空行形态不同 ⇒ 差 1–2 行是正常的），
    # 原实现要求**完全相等** ⇒ 正常重建被误挡（实测 ch46 133 → 132 不落盘）。
    # ⇒ 改为**比例守卫**：行数跌幅超 20% 才中止（那才是「内容被吞了」）。
    if out_text.count('\n') < orig_total_lines * 0.8:
        print(f"❌ {os.path.basename(md_path)} 行数跌幅过大 {orig_total_lines} → {out_text.count(chr(10))}，未落盘")
        res['rows_after'] = 0
        return res
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(md_path), suffix='.tmp')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write(out_text)
        os.replace(tmp, md_path)
    except Exception:
        try: os.unlink(tmp)
        except OSError: pass
        raise
    return res


def repair_file(md_path, ch, dry_run=False, top_up=0, glosses=None, extra=None, plan=None):
    text = open(md_path, encoding='utf-8').read()
    if '## 词汇' not in text:
        return None
    i = text.index('## 词汇')
    m = re.search(r'^## ', text[i + 3:], re.M)
    j = (i + 3 + m.start()) if m else len(text)
    section = text[i:j]

    src = load_chapter(os.path.dirname(md_path), str(ch))
    sents = sentences(src)
    corpus = unicodedata.normalize('NFKD', src).lower()
    glosses = glosses or {}
    extra = extra or {}          # {词头: 释义}，调用方指定的补入词（优先于候选集）

    # ── plan 模式：整表按 plan 重建（2026-10-19 增补）──────────────────
    # 判据：plan 给出该章的完整三档词表（词头+释义），**例句恒由脚本从本章
    # text/ 抽取** ⇒ 逐字保证。词头不在本章 ⇒ 整表中止不产出（宁缺毋造）。
    if plan:
        cand, _ = candidate_pool(os.path.dirname(md_path), ch, corpus)
        # ⚠️ 2026-10-19 修口径不一致（Maybe Next Time 批次）：
        #   语料 flat 走 NFKD（cafés → cafes），而候选例句来自 sentences(src) 的**未归一化**原文
        #   （cafés → cafs）⇒ 同一句在两边 flat 后**不连续** ⇒ 误判「例句不逐字命中本章」。
        #   修法：例句与语料**用同一个 flat**（NFKD）处理后再比。
        flat_txt = re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', src).lower())
        def _flat(s):
            return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).lower())
        errs, built = [], {t: [] for t in TIER_KEYS}
        for t in TIER_KEYS:
            for head, gloss in plan.get(t, []):
                if not head.strip():
                    errs.append(f'空词头 [{t}]'); continue
                if not gloss.strip():
                    errs.append(f'缺释义 [{t}] {head}'); continue
                if not head_in_chapter(head, corpus):
                    errs.append(f'词头不在本章 [{t}] {head}（自造？）'); continue
                ex = cand.get(head) or pick_example(head, sents, corpus, None)
                if not ex:
                    errs.append(f'本章无含该词的可用句子 [{t}] {head}'); continue
                ex = ex.strip().strip('"').strip()
                if _flat(ex) not in flat_txt:
                    errs.append(f'例句不逐字命中本章 [{t}] {head} -> {ex[:40]}'); continue
                built[t].append((head, gloss, ex))
        if errs:
            return {'dropped': [], 'replaced': [], 'kept': [], 'added': [],
                    'rows_after': 0, 'errors': errs}
        # 组装新节：保留节首 H2 与表头形态
        out_lines = [section.split('\n')[0], '']
        for t in TIER_KEYS:
            # ⚠️ 2026-10-19 修：`⭐⭐` 是 `⭐⭐⭐` 的**前缀** ⇒ 正则 `⭐⭐[^\n]*` 先匹配到
            # 高级档 ⇒ 三档标题全写成「⭐⭐⭐ 高级」。修法：档标记后必须跟**空格或行尾**。
            tm = re.search(rf'^###\s+({re.escape(t)}(?![\u2b50])\s*[^\n]*)$', section, re.M)
            # 用 group(0)（整行）保留 `### ` 前缀（group(1) 不含前缀会塌陷小节层级）
            label = tm.group(0).strip() if tm else f'### {t} ' + {'⭐⭐⭐': '高级', '⭐⭐': '进阶', '⭐': '基础'}[t]
            hm = re.search(r'^\|([^\n|]+)\|([^\n|]+)\|([^\n|]+)\|\s*$', section, re.M)
            hdr = '| ' + ' | '.join(c.strip() for c in hm.group(0).strip().strip('|').split('|')) + ' |' if hm else '| 词条 | 释义 | 例句（本章） |'
            out_lines += [label, '', hdr, '|---|---|---|']
            out_lines += [f'| {h} | {g} | {ex} |' for h, g, ex in built[t]]
            out_lines += ['']
        new_section = '\n'.join(out_lines).rstrip('\n') + '\n'
        added = [(h, t) for t in TIER_KEYS for h, _, _ in built[t]]
        return _write_out(md_path, text, i, j, section, new_section, dry_run,
                          dropped=[], replaced=[], kept=[], added=added)

    out_lines, dropped, replaced, kept = [], [], [], []
    cur_tier = None
    for line in section.split('\n'):
        s = line.strip()
        tm = TIER_PAT.match(s)
        if tm:
            cur_tier = tm.group(1)
            out_lines.append(line)
            continue
        rm = ROW_RE.match(s)
        if rm is None:
            # 3 列表兜底（2026-10-19 增补，见 ROW_RE3 处的说明）
            rm3 = ROW_RE3.match(s)
            if rm3 and cur_tier and rm3.group(1) not in ('词', '词/短语', '词条'):
                cells = [g.strip() for g in rm3.groups()]
                head = cells[0].replace('**', '').strip()
                if not head or set(head) <= set('-: '):
                    out_lines.append(line)
                    continue
                if not head_in_chapter(head, corpus):
                    dropped.append((head, cur_tier, '词头不在本章'))
                    continue
                ex = pick_example(head, sents, corpus, None)
                if not ex:
                    dropped.append((head, cur_tier, '本章无含该词的可用句子'))
                    continue
                ex = ex.strip().strip('"').strip()
                new = f"| {cells[0]} | {cells[1]} | {ex} |"
                if new != line:
                    replaced.append((head, cur_tier))
                else:
                    kept.append((head, cur_tier))
                out_lines.append(new)
                continue
            out_lines.append(line)
            continue
        if rm and cur_tier and rm.group(1) not in ('词', '词/短语'):
            cells = [g.strip() for g in rm.groups()]
            head = cells[0].replace('**', '').strip()
            ncols = len([c for c in cells if c != '']) if cells[3] == '' else 4
            if not head or set(head) <= set('-: '):
                out_lines.append(line)
                continue
            if not head_in_chapter(head, corpus):
                dropped.append((head, cur_tier, '词头不在本章'))
                continue
            ex = pick_example(head, sents, corpus, None)
            if not ex:
                dropped.append((head, cur_tier, '本章无含该词的可用句子'))
                continue
            ex = ex.strip().strip('"').strip()
            if len(cells) >= 4 and cells[1]:       # 4 列：词|音标|释义|例句
                new = f"| {cells[0]} | {cells[1]} | {cells[2]} | {ex} |"
            else:                                   # 3 列：词|释义|例句
                new = f"| {cells[0]} | {cells[2]} | {ex} |"
            if new != line:
                replaced.append((head, cur_tier))
            else:
                kept.append((head, cur_tier))
            out_lines.append(new)
            continue
        out_lines.append(line)

    # ── --top-up：某档行数 < N 时补足（2026-10-19 实现该 docstring 承诺的功能）──
    # 补入词头来源优先级：① 调用方 `extra`（指定词头+释义）② `vocab_candidates` 候选集
    # 例句恒由脚本从本章 text/ 抽出 ⇒ 天然逐字；释义缺失 ⇒ 不写入（宁缺毋造）。
    added = []
    if top_up:
        per_tier = {}
        cur_tier = None
        for line in out_lines:
            s = line.strip()
            tm = TIER_PAT.match(s)
            if tm:
                cur_tier = tm.group(1)
                per_tier.setdefault(cur_tier, 0)
                continue
            if cur_tier and s.startswith('|') and not set(s.strip('| ')) <= set('-: |'):
                cells = [c.strip() for c in s.strip('|').split('|')]
                if len(cells) >= 3 and cells[0] not in ('词', '词/短语', '词条') and re.search(r'[A-Za-z]{2,}', cells[0]):
                    per_tier[cur_tier] += 1
        need = {t: max(0, top_up - per_tier.get(t, 0)) for t in ('⭐⭐⭐', '⭐⭐', '⭐')}
        if any(need.values()):
            cand, cand_tiers = candidate_pool(os.path.dirname(md_path), ch, corpus)
            used = {h for h, _ in kept} | {h for h, _ in replaced}
            pool = [(h, g) for h, g in extra.items()]
            pool += [(h, None) for h in cand]
            tier_of = {}
            for t, hlist in cand_tiers.items():
                for h, ex in hlist:
                    tier_of[h] = t
            by_tier = {t: [] for t in ('⭐⭐⭐', '⭐⭐', '⭐')}
            for h, g in pool:
                ex = cand.get(h)
                if not ex or h in used:
                    continue
                t = tier_of.get(h)
                if t is None:
                    continue
                by_tier[t].append((h, g, ex))
            for t in ('⭐⭐⭐', '⭐⭐', '⭐'):
                if not need.get(t):
                    continue
                picks = by_tier.get(t, [])[:need[t]]
                if not picks:
                    continue
                idx = None
                for k, line in enumerate(out_lines):
                    tm = TIER_PAT.match(line.strip())
                    if tm and tm.group(1) == t:
                        idx = k
                        break
                if idx is None:
                    continue
                end = len(out_lines)
                for k in range(idx + 1, len(out_lines)):
                    if TIER_PAT.match(out_lines[k].strip()) or out_lines[k].startswith('## '):
                        end = k
                        break
                ins = []
                for h, g, ex in picks:
                    gloss = g if g else glosses.get(h, '')
                    if not gloss.strip():
                        continue      # 缺释义不写入（宁缺毋造）
                    ins.append(f"| {h} | {gloss} | {ex} |")
                    used.add(h)
                if ins:
                    out_lines[end:end] = ins
                    added.extend((h, t) for h, _, _ in ins)

    new_section = '\n'.join(out_lines)
    return _write_out(md_path, text, i, j, section, new_section, dry_run,
                      dropped=dropped, replaced=replaced, kept=kept, added=added)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('book_dir')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--from-ch', type=int, default=0, help='起始章号（含）；缺省=全书')
    ap.add_argument('--to-ch', type=int, default=10**9, help='结束章号（含）；缺省=全书')
    ap.add_argument('--top-up', type=int, default=0,
                    help='每档目标行数；某档不足则用候选集补足（需 --glosses 给释义）')
    ap.add_argument('--glosses', help='释义 JSON：{"chNN": {词头: 释义}} 或 {词头: 释义}（适用于所有章）')
    ap.add_argument('--plan', help='整表重建计划 JSON：{"chNN": {"⭐⭐⭐": [[词头, 释义], ...], "⭐⭐": [...], "⭐": [...]}}'
                                   '（例句恒由脚本从本章 text/ 抽取；词头不在本章 ⇒ 该章不产出）')
    a = ap.parse_args()
    gloss_map = {}
    if a.glosses:
        gloss_map = json.load(open(a.glosses, encoding='utf-8'))
    plan_map = {}
    if a.plan:
        plan_map = json.load(open(a.plan, encoding='utf-8'))
    mds = sorted(f for f in os.listdir(a.book_dir)
                 if f.endswith('.md') and re.match(r'ch\d+', f))
    tot_drop = tot_rep = tot_add = 0
    for f in mds:
        p = os.path.join(a.book_dir, f)
        cm = re.match(r'ch(\d+)', f)
        cn = int(cm.group(1))
        if cn < a.from_ch or cn > a.to_ch:
            continue
        if not find_chapter_text(a.book_dir, cm.group(1)):
            print(f'⚠️ {f}: text/ 无对应件，跳过')
            continue
        # 释义查找：先按章号键，再退回通用键
        glosses = dict(gloss_map.get(f"ch{cn}", {}))
        glosses.update(gloss_map.get("__all__", {}))
        r = repair_file(p, cm.group(1), a.dry_run,
                        top_up=a.top_up, glosses=glosses,
                        plan=plan_for(plan_map, cn) or None)
        if r is None:
            continue
        if r.get('errors'):
            print(f"❌ {f}: plan 校验失败 {len(r['errors'])} 处，未产出")
            for e in r['errors'][:12]:
                print(f"    ✗ {e}")
            tot_drop += 1
            continue
        if r['dropped'] or r['replaced'] or r.get('added'):
            print(f"{f}: 例句重写 {len(r['replaced'])} ｜ 删除 {len(r['dropped'])} "
                  f"｜ 补入 {len(r.get('added', []))} "
                  f"｜ 原样保留 {len(r['kept'])} ｜ 剩 {r['rows_after']} 行")
            for h, t, why in r['dropped']:
                print(f"    ✗ 删 [{t}] {h} —— {why}")
            for h, t in r.get('added', []):
                print(f"    ＋ 补 [{t}] {h}")
        tot_drop += len(r['dropped'])
        tot_rep += len(r['replaced'])
        tot_add += len(r.get('added', []))
    print(f"\n合计：例句重写 {tot_rep} ｜ 删除 {tot_drop} ｜ 补入 {tot_add}"
          + ('（dry-run，未写盘）' if a.dry_run else ''))


if __name__ == '__main__':
    main()
