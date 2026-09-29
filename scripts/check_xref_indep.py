#!/usr/bin/env python3
"""check_xref_indep.py — 跨章引用回查的**独立实现**（第 10 条 d 步）

为什么需要它（2026-09-29 实测，两条都验过）：
 ① `check_crossref.py` **只认** `chNN "引语"` 这一种英文模式，中文式引用
    （`chNN 里那句…`、`chNN 的店主`）完全在其口径外 ⇒ 它报「0 报警」是**真空绿**。
 ② 我先写的自建检查器**第一版是死代码**：它只在同一句含拉丁证据词时才判，
    而本书跨章引用绝大多数是中文式、句内没有可机检的英文 ⇒ 对 266 处引用报「0 疑似」，
    注入 3 处错章引用（改 ch16→ch30 等）**一条都不报**。
    ——这是 AGENTS 8c「现写检查器先验该报的报了再信它的 0」的又一个实例。

本脚本的判据（只用**可机检**的证据，不猜中文语义）：
  A. 同一句里 `chNN` 附近出现的**被引号包裹的英文**（「…」 或 "…"）→ flat 比对目标章
  B. **紧跟** `chNN` 的**英文短语**（≥3 个拉丁词）→ flat 比对目标章
     ⚠️ 不可放宽到「同句内任何引号英文」——同句引文常属本章或句中另提到的章，
     那样会对正确引用全报警（2026-09-29 实测 14 条假红）
  C. 中文式引用**不做自动判定**，而是导出「待人判清单」（含所在句全文）——
     语义判定不是脚本能做的，硬判会制造假阳（见纪律 4）。

退出：0 = A/B 无报警（C 的清单条数不代表缺陷）；1 = A/B 有报警。
用法：python3 scripts/check_xref_indep.py "<书目录>" [--list] [--max N]
"""
import re, sys
from pathlib import Path

SENT = re.compile(r'[^。！？\n]*ch\d\d[^。！？\n]*[。！？]?')
# A: 被引号包裹的英文
QEN = re.compile(r'[「“"]([^」”"]{12,})[」”"]')
# B: 连续拉丁词组成的短语
LAT = re.compile(r"[A-Za-z][A-Za-z'’\-]*(?:[ ,]+[A-Za-z][A-Za-z'’\-]*){2,}")
STOP = {'Jess', 'Alison', 'Caitlin', 'Julia', 'Kyle', 'Ryan', 'Parker', 'Linda',
        'Jim', 'Chris', 'Beth', 'Kim', 'Nina', 'The', 'Chapter', 'Chatham', 'Boston',
        'Neptune', 'Middleton', 'Squire', 'Campbell', 'Brinker', 'Main', 'Street',
        'Lee', 'Nancy', 'Meghan', 'Ashley', 'Gina', 'Edith', 'Winslow', 'Marcy',
        'Marian', 'Rich', 'Blair', 'Wheaton', 'Kyle', 'Sunday', 'Monday', 'Tuesday',
        'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Bermuda', 'York', 'Virginia'}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    want_list = '--list' in sys.argv
    mx = 10 ** 9
    if '--max' in sys.argv:
        mx = int(sys.argv[sys.argv.index('--max') + 1])
    if not args:
        print(__doc__); return 2
    B = Path(args[0])
    book = {int(re.search(r'ch(\d+)', p.name).group(1)): p.read_text(encoding='utf-8')
            for p in (B / 'text').glob('ch*.txt')}
    flat = {k: re.sub(r'[^a-z0-9]', '', v.lower()) for k, v in book.items()}
    tot = bad = 0
    todo = []
    for md in sorted(list(B.glob('ch*.md')) + list(B.glob('00_*.md'))):
        s = md.read_text(encoding='utf-8')
        for m in SENT.finditer(s):
            sent = m.group(0)
            for c in re.finditer(r'ch(\d\d)', sent):
                nn = int(c.group(1)); tot += 1
                line = s[:m.start()].count('\n') + 1
                # ⚠️ 只认**紧跟 chNN 引用**的那一段引号英文（相距 ≤3 字符）。
                # 2026-09-29 修正：第一版把同句里所有引号英文都当本引用的证据，
                # 对 14 条**正确**的跨章引用全报警（假红型）——同句的引文常属本章
                # 或句中提到的**另一个**章，归属只有语义能定。
                ev = []
                for e in QEN.finditer(sent):
                    if 0 <= e.start() - c.end() <= 3:
                        ev.append(e.group(1))
                for e in LAT.finditer(sent):
                    if 0 <= e.start() - c.end() <= 1 and e.group(0) not in STOP:
                        ev.append(e.group(0))
                hit = [e for e in ev if re.sub(r'[^a-z0-9]', '', e.lower()) in flat.get(nn, '')]
                miss = [e for e in ev if e not in hit]
                if ev and miss:
                    bad += 1
                    print(f"  ❌ {md.name}:{line} → ch{nn:02d}：证据 {miss} 在该章查无")
                    print(f"        句：{sent.strip()[:100]}")
                elif not ev:
                    todo.append((md.name, line, nn, sent.strip()))
    print(f"=== chNN 引用 {tot} 处：英文证据报警 {bad} 处 ／ 中文式待人判 {len(todo)} 处 ===")
    if want_list and todo:
        print("--- 中文式待人判清单（前 %d 条）---" % min(mx, len(todo)))
        for f, l, n, sent in todo[:mx]:
            print(f"  {f}:{l} → ch{n:02d}｜{sent[:86]}")
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
