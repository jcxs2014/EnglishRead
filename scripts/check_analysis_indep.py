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
BAD=[]; tot=0
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
            words=[w.strip('’\'-').lower() for w in frag.split()]
            miss=[w for w in words if len(w)>2 and w not in book_flat]
            BAD.append((md.name,i,frag.strip(),miss))
print(f"抽出分析层英文片段 {tot} 条")
if BAD:
    print(f"❌ 未命中 {len(BAD)} 条：")
    for f,i,frag,miss in BAD: print(f"  {f}:{i}  {frag[:88]}\n      未命中词: {miss}")
else:
    print("✅ 全部片段在全书 text/ 逐字命中")
sys.exit(1 if BAD else 0)
