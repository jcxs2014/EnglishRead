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
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_vocab import word_hits_corpus, FUNC_STOP  # 同一实现，避免口径漂移
from build_vocab_table import load_chapter, sentences, is_complete_sentence
from chapter_text_path import find_chapter_text

TIER_PAT = re.compile(r'^###\s*(⭐{1,3})')
ROW_RE = re.compile(r'^\|\s*(.+?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$')


def split_words(head):
    ws = [w.lower() for w in re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", head)]
    return [w for w in ws if w not in FUNC_STOP]


def head_in_chapter(head, corpus):
    ws = split_words(head)
    if not ws:
        return True
    return all(word_hits_corpus(w, corpus) for w in ws)


def token_forms(w):
    """一个词头的可接受词形集合（与 word_hits_corpus 的屈折口径同向）。

    2026-10-17 修：原实现只匹配**词头本身**的整词，导致 text/ 里只有屈折形式
    （sucks / crying / approachable）时抽不到例句，词条被误删。本函数把
    -s/-es/-ed/-ing/-ly、y→ies/ied、以及 -able/-ably 等派生后缀一并纳入候选词形，
    匹配时按整词匹配（前后不能是字母），避免 'suck' 命中 'sucker'。
    """
    out = {w}
    if w.endswith('y') and len(w) > 3:
        out.add(w[:-1] + 'ies')
        out.add(w[:-1] + 'ied')
    for suf in ('s', 'es', 'ed', 'ing', 'ly'):
        if w.endswith(suf) and len(w) > len(suf) + 2:
            base = w[:-len(suf)]
            out.add(base)
            out.add(base + 'e')
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


def repair_file(md_path, ch, dry_run=False):
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

    new_section = '\n'.join(out_lines)
    if new_section != section and not dry_run:
        open(md_path, 'w', encoding='utf-8').write(text[:i] + new_section + text[j:])
    return {'dropped': dropped, 'replaced': replaced, 'kept': kept,
            'rows_after': len(kept) + len(replaced)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('book_dir')
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    mds = sorted(f for f in os.listdir(a.book_dir)
                 if f.endswith('.md') and re.match(r'ch\d+', f))
    tot_drop = tot_rep = 0
    for f in mds:
        p = os.path.join(a.book_dir, f)
        cm = re.match(r'ch(\d+)', f)
        if not find_chapter_text(a.book_dir, cm.group(1)):
            print(f'⚠️ {f}: text/ 无对应件，跳过')
            continue
        r = repair_file(p, cm.group(1), a.dry_run)
        if r is None:
            continue
        if r['dropped'] or r['replaced']:
            print(f"{f}: 例句重写 {len(r['replaced'])} ｜ 删除 {len(r['dropped'])} "
                  f"｜ 原样保留 {len(r['kept'])} ｜ 剩 {r['rows_after']} 行")
            for h, t, why in r['dropped']:
                print(f"    ✗ 删 [{t}] {h} —— {why}")
        tot_drop += len(r['dropped'])
        tot_rep += len(r['replaced'])
    print(f"\n合计：例句重写 {tot_rep} ｜ 删除 {tot_drop}"
          + ('（dry-run，未写盘）' if a.dry_run else ''))


if __name__ == '__main__':
    main()
