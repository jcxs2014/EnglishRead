#!/usr/bin/env python3
"""
check_vocab.py — 词汇表真实性/分档检测

用法：
  python3 scripts/check_vocab.py "<书目录>"

检查（对应根 AGENTS.md 核验规则第 4 条）：
  1. 词条真实性：三档词汇表每个词条的各实词都应能在语料（text/*.txt 合并，缺则 epub 展平）
     中找到——抓 "spear | 矛 | 例句: the arts of war" 式张冠李戴；
  2. 例句抽检：例句指纹前 20 字符须在语料中命中（未命中记 warning，不计 fail——
     例句允许"原文真实短语组合"的轻度改写）；
  3. 分档合理性：⭐ 基础档含超纲生僻词 / ⭐⭐⭐ 高级档混入高频常用词 → warning。
退出码：存在 fail 则非 0。
"""
import re, sys, glob, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_quotes import flat_alpha, epub_flat_text, read_html

# ~200 个最高频英文词（用于粗查分档注水；判断的是词条而非释义）
COMMON = set("""the be to of and a in that have i it for not on with he as you do at this but his by from
they we say her she or an will my one all would there their what so up out if about who get which go me
when make can like time no just him know take people into year your good some could them see other than
then now look only come its over think also back after use two how our work first well way even new want
because any these give day most us man find here thing great little world own life still small large next
early young important few public bad same able tell something nothing each every must such again change
off turn play hand part room case ask last around need better big old right left end home read lot name
water money fact place hear kind best sure top done heart black white blue green red house dog cat book
word mother father sister brother son girl boy child war city street table chair door window light night
morning water head face eye nose mouth arm leg hand foot tree sun moon star sky rain snow wind fire""".split())

TIER_PAT = re.compile(r'^#+\s*[⭐★]*\s*(高级|进阶|基础)')
SENTINEL = re.compile(r'^\s*\|[-\s|]+\|\s*$')

def load_corpus(book_dir):
    texts = sorted(glob.glob(os.path.join(book_dir, 'text', '*.txt')))
    if texts:
        return flat_alpha(''.join(open(p, encoding='utf-8', errors='ignore').read() for p in texts)), 'text/'
    epubs = glob.glob(os.path.join(book_dir, 'library', '*.epub'))
    if epubs:
        return flat_alpha(epub_flat_text(epubs[0])), 'epub'
    return '', 'none'

def check_book(book_dir, verbose=False):
    corpus, src = load_corpus(book_dir)
    fails, warns = [], []
    total_rows = 0
    for f in sorted(glob.glob(os.path.join(book_dir, '*.md'))):
        name = os.path.basename(f)
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
            entry, meaning, example = (cells + ['',''])[:3]
            words = [w.lower() for w in re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", entry)]
            words = [w for w in words if w not in ('the','a','an','of','in','on','to','and','or')]
            if not words:
                continue
            n_rows += 1
            # 1. 词条真实性：所有 >=4 字母的实词都必须出现
            def hit(w):
                w = w.replace("'", "")
                if len(w) >= 5 and w[:len(w)-1] in corpus:   # 允许 -s/-ed/-ing 等屈折变形
                    return True
                return len(w) >= 4 and w in corpus
            missing = [w for w in words if len(w) >= 4 and not hit(w)]
            if missing:
                fails.append((name, tier, f"词条不在语料: {missing}", entry))
            # 2. 例句抽检（warning 级）
            eq = flat_alpha(example)
            if len(eq) >= 20 and eq[:20] not in corpus:
                warns.append((name, tier, f"例句片段未命中(可组合改写)", example[:50]))
            # 3. 分档合理性（warning 级）
            key = min(words, key=len) if words else ''
            if tier == '基础' and words and all(w in COMMON for w in words if len(w)>=4):
                pass  # 基础档全是常用词，合理
            elif tier == '基础' and any(len(w) >= 9 and w not in COMMON for w in words):
                warns.append((name, tier, f"基础档疑含超纲词", entry))
            elif tier == '高级' and words and all(w in COMMON for w in words):
                warns.append((name, tier, f"高级档混入常用词", entry))
        total_rows += n_rows
    return {'fails': fails, 'warns': warns, 'rows': total_rows, 'src': src}

def main(book_dir, verbose=False):
    r = check_book(book_dir, verbose)
    print(f"语料来源: {r['src']}   词条行合计: {r['rows']}")
    print(f"\n--- FAIL ({len(r['fails'])}) ---")
    for x in r['fails']:
        print(f"  {x[0]} [{x[1] or '?'}] {x[2]}")
        print(f"      「{x[3][:60]}」")
    print(f"\n--- WARN ({len(r['warns'])}) ---")
    for x in r['warns']:
        print(f"  {x[0]} [{x[1] or '?'}] {x[2]}「{x[3][:60]}」")
    sys.exit(1 if r['fails'] else 0)

if __name__ == "__main__":
    main(sys.argv[1], '--verbose' in sys.argv)
