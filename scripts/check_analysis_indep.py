#!/usr/bin/env python3
"""check_analysis_indep.py — 分析层行内英文 flat 复核（**第二实现**，换检查路径用）

为什么需要它（2026-09-29《The Bookshop by the Bay》实测）：
`sweep_analysis_inline.py` 对全书报 `🟠 部分命中 0 ｜ ❌ 零命中 0` 的同一批文件里，
本脚本抓出 **6 处真缺陷**，全部是**分析层英文走形**——引语与词表都完全正确，门禁全绿：

  ch06 "not going to let him off easy"   ← 原文 "wasn't going to..."（漏 was）
  ch08 "taking a deep breath, debating"  ← 原文 "took a deep breath, ..."（跨片段拼接）
  ch10 "She chose her words carefully"   ← 原文 "Jess chose ..."（主语替换 = the-boyfriend 类）
  ch13 "I have to do what feels right…"  ← 原文 "You have to ..."（人称反转，意思反了）
  ch13 "she was a little disappointed"  ← 原文 "Julia was ..."（主语替换）
  ch18 "then wanted to give you a…"     ← 原文 "but wanted to ..."（连词替换）

判据与 `sweep_analysis_inline` **刻意不同**（否则不构成「换路径」）：
  · 来源：扫**所有非引语行**（含表格外的正文行），不只扫反引号/双引号通道；
  · 口径：先试 flat **整串**命中；整串不中则退到**逐词**命中并列出未命中词——
    整串不中而逐词全中 = 走形/拼接/主语替换，正是上述 6 类的判据；
  · 抽词门槛：≥3 词且 flat ≥20 字符。
**它不替代 `sweep_analysis_inline`**（那是主门禁），而是 d 步「换检查路径」的当值工具。

用法: python3 scripts/check_analysis_indep.py "<书目录>"
退出: 0 全部命中 ｜ 1 有未命中（逐条列文件:行号、片段、未命中词）｜ 2 参数错误
"""
import re,sys
from pathlib import Path
B=Path(sys.argv[1])
book_flat=re.sub(r'[^a-z0-9]','',"".join(p.read_text() for p in sorted((B/'text').glob('ch*.txt'))).lower())
EN=re.compile(r"[A-Za-z][A-Za-z’,'\-]*(?:\s+[A-Za-z][A-Za-z’,'\-]*){2,}")
BAD=[]; RECON=set(); TERM_HIT=set(); tot=0
# 叙述学/修辞/语法元语言（小写）。只用于豁免「整串都是术语」的片段。
TERM = set("""free indirect discourse anaphora epizeuxis epistrophe polysyndeton asyndeton
chiasmus synecdoche metonymy irony enjambment caesura alliteration assonance consonance
onomatopoeia litotes antimetabole analepsis prolepsis diegesis focalization narrator
narrative voice present participle gerund infinitive subjunctive imperative
unreliable narrator stream consciousness foreshadowing motif refrain cadence meter
iambic trochaic dactylic couplet quatrain sonnet stanza verse prose colloquialism
neologism portmanteau euphemism dysphemism hyperbole understatement parallelism
antithesis juxtaposition register dialect idiom calque gloss allodynia kenning
apostrophe personification simile metaphor symbolism leitmotif subtext interiority
preposition prepositions conjunction conjunctions pronoun pronouns article articles
adverb adverbs adjective adjectives noun nouns verb verbs clause clauses sentence
syntax grammar tense tenses aspect mood voice word words phrase phrases
""".split())
for md in sorted(B.glob('ch*.md')):
    for i,line in enumerate(md.read_text().split('\n'),1):
        if line.startswith('> ') or line.startswith('|') or line.strip().startswith('#') \
           or line.startswith('状态:') or line.startswith('modified:') or line.startswith('---'):
            continue
        for m in EN.finditer(line):
            frag=m.group(0)
            if len(re.sub(r'[^a-z0-9]','',frag.lower()))<20: continue
            tot+=1
            if re.sub(r'[^a-z0-9]','',frag.lower()) in book_flat: continue
            # 2026-09-30 修假红：逐词判据原只剥 `’'-`，遇到 `dark, determined` 这类
            # 带逗号的词会因 `dark,` 查无而误报（整串 flat 其实命中，原文逐字相符）。
            # 判据是「该词是否出现在 flat 里」，标点本就不参与 flat，故一并剥掉。
            words=[re.sub(r'[^a-z0-9]','',w.lower()) for w in frag.split()]
            miss=[w for w in words if len(w)>2 and w not in book_flat]
            # 词全命中（miss 为空）= 整串因跨片段/跨位置而不连续，但每个词都真在原文 ⇒
            # 属「拼接」而非「走形」，不计入缺陷（否则词序调整就会永久误报）。
            #
            # 2026-09-30 补一档（**原静默豁免是本脚本最大的盲区**）：Cibola Burn 轮实证
            # 14 条伪造/改写式跨章引语（"advocates no sign"、"as if you don't like me right
            # now"、"make up lost time"…）**每一个词都在书里**，因此全部落进这条豁免、
            # 脚本却报「✅ 全部命中」。⇒ 这类片段改列为 ⚠️ 待人判并**逐条列出**，
            # 退出码不变（不判红），否则全库会涌入大量拼接假阳。
            if not miss:
                # 关键词行常是「A, B, C」逐条并列，每条各自逐字、只是整串不连续。
                # 按逗号/分号/斜杠分片后逐片核，只把**单片也查无**的留下，
                # 否则噪声（实测 465 条）会淹没真正的改写冒充逐字。
                for piece in re.split(r'[,;]|\s/\s', frag):
                    p=re.sub(r'[^a-z0-9]','',piece.lower())
                    if len(p)<20 or p in book_flat: continue
                    pw=[re.sub(r'[^a-z0-9]','',w.lower()) for w in piece.split()]
                    if any(len(w)>2 and w not in book_flat for w in pw): continue
                    RECON.add((md.name,i,piece.strip()))
                continue
            # ⚠️ 2026-10-03 补术语豁免（本书 d 步实证）：`free indirect discourse`、
            #    `anaphora of prepositions` 被判 ❌ 未命中——它们是**分析者的元语言**，
            #    本来就不该在原文里。判据只豁免「**全部**内容词都在术语表内」的片段，
            #    所以 `fretting`（同批报出、实为把 to fret 写成现在分词的**真缺陷**）
            #    照常判红。表外的自造说法一律不豁免。
            if all(w in TERM or len(w) <= 2 for w in words):
                TERM_HIT.add((md.name, i, frag.strip()))
                continue
            BAD.append((md.name,i,frag.strip(),miss))
print(f"抽出分析层英文片段 {tot} 条")
if BAD:
    print(f"❌ 未命中 {len(BAD)} 条：")
    for f,i,frag,miss in BAD: print(f"  {f}:{i}  {frag[:88]}\n      未命中词: {miss}")
else:
    print("✅ 全部片段在全书 text/ 逐字命中")
if RECON:
    print(f"⚠️ 整串查无但每个词都在书里（拼接 **或改写冒充逐字**）{len(RECON)} 条 —— 只报不判红，须人判：")
    for f,i,frag in sorted(RECON): print(f"  {f}:{i}  {frag[:88]}")
if TERM_HIT:
    print(f"⚪ 术语豁免 {len(TERM_HIT)} 条（内容词全在元语言表内，非引文）：")
    for f,i,frag in sorted(TERM_HIT): print(f"  {f}:{i}  {frag[:88]}")
sys.exit(1 if BAD else 0)
