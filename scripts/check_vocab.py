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
"""
import re, sys, glob, os, zipfile, html as htmlmod

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_quotes import epub_flat_text, read_html

flat = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())

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


def word_hits_corpus(word, corpus):
    """Check if word (or its stem) hits corpus. Returns True if found."""
    w = word.replace("'", "")
    # Allow -s / -ed / -ing / -s after s / -lier etc.
    for stem in (w, w.rstrip('s'), w.rstrip('ing')+'e' if w.endswith('ing') else w,
                 w.rstrip('ed') if not w.endswith('e') else w,
                 w.rstrip('ly') if w.endswith('ly') else None):
        if stem and len(stem) >= 4 and stem in corpus:
            return True
    return len(w) >= 4 and w in corpus


def example_ok(example, corpus):
    """Check example sentence against corpus. Returns (ok, detail)."""
    if not example or len(re.findall(r'[A-Za-z0-9]', example)) < 8:
        return False, '例句过短或为空'
    eq = flat(example)
    # 整句匹配（取前 60 字符作为指纹）
    if eq[:60] in corpus:
        return True, '整句命中'
    # 省略号分段：每段（≥12 字符）都必须命中
    frags = [p.strip() for p in re.split(r'…|\.\.\.', example)
             if len(re.findall(r'[A-Za-z0-9]', p)) >= 12]
    if frags and all(flat(p)[:40] in corpus for p in frags):
        return True, f'省略号分段({len(frags)}段)命中'
    return False, '例句未命中本章'


def check_book(book_dir, verbose=False):
    chapter_corpora = load_chapter_corpora(book_dir)
    book_corpus = load_epub_if_needed(book_dir, chapter_corpora)

    fails, warns = [], []
    total_rows = 0

    for f in sorted(glob.glob(os.path.join(book_dir, '*.md'))):
        if os.path.basename(f).startswith('00_'):
            continue  # 总览文件无词汇表
        name = os.path.basename(f)

        # 从文件名提取章号
        cm = re.match(r'ch(\d+)', name)
        nn = int(cm.group(1)) if cm else None
        ch_corpus = chapter_corpora.get(nn, '') if nn else ''

        tier = None
        n_rows = 0
        for line in open(f, encoding='utf-8'):
            hm = TIER_PAT.match(line.strip())
            if hm:
                tier = hm.group(1); continue
            if SENTINEL.match(line) or '|---' in line:
                continue
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if len(cells) < 2 or not any(re.search(r'[A-Za-z]{2,}', c) for c in cells[:1]):
                continue
            entry, meaning, example = (cells + ['', ''])[:3]
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

        total_rows += n_rows

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
