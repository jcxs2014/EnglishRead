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
# A': 「引文」（chNN）——标注在引文**之后**的配对写法（2026-09-30 增补，见下方注释）
#    ⚠️ 必须要求引文**以拉丁字母为主**（≥60%）：中文句里嵌一两个英文术语的表格单元
#    （如「1948 年战争是…的 initiator 与 progenitor」（ch03））也会命中本式，
#    而它们本就该走「中文式待人判」，不该按英文 flat 比对判红。
QAFTER = re.compile(r'[「“"]([^」”"]{12,})[」”"]\s*[（(]\s*ch(\d\d[a-z]?)\s*[）)]')


def _mostly_latin(s):
    letters = sum(ch.isascii() and ch.isalpha() for ch in s)
    return letters >= 0.6 * max(1, sum(not ch.isspace() for ch in s))
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
    # ⚠️ 2026-10-03 修（假红型）：本脚本此前按**整数章号**建参照集，于是带字母后缀的
    # 提取件（ch11a 韵文）与编号章（ch11）**同键相撞**，glob 排序里后缀件在后 ⇒ 编号章的
    # 文本被韵文覆盖。本书 25 组相撞，5 条「该章查无」全由此来（引语确在该编号章内）。
    # 收口：按 chapter_text_path 的 (章号, 后缀) 建键，引用侧同步支持 `chNN[后缀]`。
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from chapter_text_path import split_chapter_key
    book = {}
    for p in sorted((B / 'text').glob('ch*.txt')):
        m_key = re.match(r'ch(\d+[a-z]?)', p.stem)
        if not m_key:
            continue
        num, suffix = split_chapter_key(m_key.group(1))
        book[f'{int(num):0{max(2, len(num))}d}{suffix}'] = p.read_text(encoding='utf-8')
    flat = {k: re.sub(r'[^a-z0-9]', '', v.lower()) for k, v in book.items()}
    tot = bad = 0
    n_splice = 0
    todo = []
    for md in sorted(list(B.glob('ch*.md')) + list(B.glob('00_*.md'))):
        s = md.read_text(encoding='utf-8')
        for m in SENT.finditer(s):
            sent = m.group(0)
            # ⚠️ 2026-10-03 降噪：每章 md 第 4 行的**来源标签**（`来源: chNN｜source_text: …`）
            #    里的 chNN 是**本章自己**的文件信息，不是跨章引用；本书 193 条「待人判」里
            #    有 65 条是它，把真正需要人判的 128 条淹掉。判据要窄而准，不能靠人再筛一遍。
            if 'source_text' in sent or re.match(r'^\s*(\*\*)?来源', sent):
                continue
            for c in re.finditer(r'ch(\d\d[a-z]?)', sent):
                nn = c.group(1); tot += 1
                line = s[:m.start()].count('\n') + 1
                # ⚠️ 只认**紧跟 chNN 引用**的那一段引号英文（相距 ≤3 字符）。
                # 2026-09-29 修正：第一版把同句里所有引号英文都当本引用的证据，
                # 对 14 条**正确**的跨章引用全报警（假红型）——同句的引文常属本章
                # 或句中提到的**另一个**章，归属只有语义能定。
                ev = []
                # ⚠️ `“引文”（chNN）` 这一写法里**标注在引文之后**，原文是**引文的后两个字符
                # 紧跟（chNN）**。2026-09-30 An Army like No Other 五步审查实测：同句并列 5 个
                # 「标签」（ch07）、real “victim”（ch08）、“Security”（ch12）、“making kosher”（ch14）
                # 时，旧逻辑只扫 chNN **之后** ≤3 字符的引文，于是把 `“making kosher”` 挂到了
                # **前一个** ch12 上 ⇒ 假红型（实证：该短语全书仅 ch14 命中，标注本就正确）。
                # 修法（最小改动）：先吃掉「引文紧跟（chNN）」这类配对，剩下的引文才走旧窗口，
                # 且被吃掉的引文不得再作为**任何** chNN 的证据。
                own = list(QAFTER.finditer(sent))          # (引文, chNN) 成对出现
                own_spans = [(e.start(), e.end()) for e in own]
                # ⚠️ 只在**配对的章号就是当前这个 chNN** 时计入，否则等于把同一段引文
                # 同时算给句中每一个 chNN（第一版就这样，报警 5→9）。
                for e in own:
                    if e.group(2) == nn and _mostly_latin(e.group(1)):
                        ev.append(e.group(1))
                for e in QEN.finditer(sent):
                    if 0 <= e.start() - c.end() <= 3 and not any(
                            a <= e.start() and e.end() <= b for a, b in own_spans):
                        ev.append(e.group(1))
                for e in LAT.finditer(sent):
                    if 0 <= e.start() - c.end() <= 1 and e.group(0) not in STOP:
                        ev.append(e.group(0))
                # ⚠️ 2026-10-07 修正（本书五步审查 d 步实测，3 条假红）：带 `…` 的拼接引语
                #   按定义**不是**该章文本的连续子串（`flat()` 把省略号一起剥掉，于是
                #   「A…B」被当成「AB」去找，而原文 A、B 之间隔着别的词）⇒ 同一条引语在
                #   `verify_overview_quotes` / `sweep_full` 里 ✅、在本脚本里 ❌，
                #   **两个门禁口径不一致**（AGENTS 第 3 条假红型，同 check_block_keywords
                #   2026-10-02 那条同源：判据放宽的是「整串」，**不是**「可以乱拼」）。
                #   修法与全库同口径：**按 `…` 切开，每段都必须在被引章里 flat 命中**——
                #   段数 ≥2 且全中 ⇒ 记为命中（另计一条 🔶 拼接提示，不判红）；
                #   任一段查无 ⇒ 照旧 ❌（凭空造句与移章同样查无，负控见本次修正记录）。
                def _hit(e):
                    ch_flat = flat.get(nn, '')
                    if re.sub(r'[^a-z0-9]', '', e.lower()) in ch_flat:
                        return True, False
                    segs = [x for x in re.split(r'\s*…\s*', e)
                            if len(re.sub(r'[^a-z0-9]', '', x.lower())) >= 8]
                    if len(segs) >= 2 and all(
                            re.sub(r'[^a-z0-9]', '', x.lower()) in ch_flat
                            for x in segs):
                        return True, True
                    return False, False
                hit, splice = [], 0
                for e in ev:
                    ok, sp = _hit(e)
                    if ok:
                        hit.append(e)
                        splice += sp
                miss = [e for e in ev if e not in hit]
                if ev and miss:
                    bad += 1
                    print(f"  ❌ {md.name}:{line} → ch{nn}：证据 {miss} 在该章查无")
                    print(f"        句：{sent.strip()[:100]}")
                elif splice:
                    n_splice += 1
                elif not ev:
                    todo.append((md.name, line, nn, sent.strip()))
    print(f"=== chNN 引用 {tot} 处：英文证据报警 {bad} 处 ／ 中文式待人判 {len(todo)} 处"
          f" ／ 🔶 同章省略号拼接（提示，不判红）{n_splice} 处 ===")
    if want_list and todo:
        print("--- 中文式待人判清单（前 %d 条）---" % min(mx, len(todo)))
        for f, l, n, sent in todo[:mx]:
            print(f"  {f}:{l} → ch{n}｜{sent[:86]}")
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
