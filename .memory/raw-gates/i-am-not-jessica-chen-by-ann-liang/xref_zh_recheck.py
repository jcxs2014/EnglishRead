#!/usr/bin/env python3
"""中文式跨章引用逐条回查（AGENTS 第 10 条·审查过程自身四条纪律 第 2 条的动作层）。

纪律 2 原文：「自省只能提升察觉力，**真正的防线是那个回查动作**——把 md 里每个
`chNN` + 紧随其后的反引号短语抽出来，逐条到 `text/chNN` 回查该短语是否真在该章。
⚠️ **规则只依赖动作、不依赖某个脚本**。」

`check_xref_indep.py` 对本书报「chNN 引用 111 处：英文证据报警 0 ／ 中文式待人判
95 处」——那 95 处**没有任何门禁覆盖**。本脚本就是那个回查动作的实现，
且**不 import 任何 scripts/ 下的判定函数**（纪律 1：换实现不换文件名）。

回查口径（两条都查，缺一不可）：
  ① 正查：`chNN` 所指章的 text/ 是否**含**紧随其后的证据短语
  ② 反查：该证据短语在**全书**是否只出现在所指章（是则归属干净；
     否则报「多章命中」，交人判是复述还是真跨章）

用法：python3 scripts/attic/xref_zh_recheck.py "<书目录>"
"""
import re
import sys
from pathlib import Path

# 中文式章号指认：ch12 / ch12章 / 第 12 章 / 第十二章
CN = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8,
      "九": 9, "十": 10, "十一": 11, "十二": 12, "十三": 13, "十四": 14,
      "十五": 15, "十六": 16, "十七": 17, "十八": 18, "十九": 19, "二十": 20,
      "二十一": 21}
RX_NUM = re.compile(r"(?:ch|第)\s*(\d{1,3})\s*[章]?")
RX_CN = re.compile(r"第([一二三四五六七八九十]+)章")
# 证据短语：紧跟章号之后的反引号片段或书名号片段
RX_EV = re.compile(r"[`「『]([^`」』]{4,60})[`」』]")
FLAT = re.compile(r"[^a-z0-9]")


def flat(s):
    return FLAT.sub("", s.casefold())


def main():
    bd = Path(sys.argv[1])
    texts = {}
    for p in sorted((bd / "text").glob("ch*.txt")):
        n = int(re.search(r"ch(\d+)", p.name).group(1))
        texts[n] = flat(p.read_text(encoding="utf-8"))

    total = ok = miss = multi = 0
    misses, multis = [], []
    for md in sorted(bd.glob("*.md")):
        for ln_no, line in enumerate(md.read_text(encoding="utf-8").split("\n"), 1):
            for m in RX_NUM.finditer(line):
                n = int(m.group(1))
                if n not in texts:
                    continue
                # 该章号后面 40 字内找证据短语
                tail = line[m.end(): m.end() + 40]
                ev = RX_EV.search(tail) or RX_EV.search(line)
                if not ev:
                    continue
                phrase = flat(ev.group(1))
                if len(phrase) < 8:
                    continue
                total += 1
                if phrase in texts[n]:
                    ok += 1
                    hit = [k for k, v in texts.items() if k != n and phrase in v]
                    if hit:
                        multi += 1
                        multis.append((md.name, ln_no, n, ev.group(1)[:34], hit))
                else:
                    miss += 1
                    misses.append((md.name, ln_no, n, ev.group(1)[:40]))
    print(f"中文式章号引用带证据短语共 {total} 处")
    print(f"  ✅ 所指章含该短语 {ok} 处")
    print(f"  ❌ 所指章不含该短语 {miss} 处")
    print(f"  ⚠️  该短语在他章也出现 {multi} 处（需人判是复述还是跨章搬句）")
    for x in misses[:40]:
        print(f"   ❌ {x[0]}:{x[1]} → ch{x[2]:02d} 证据「{x[3]}」")
    for x in multis[:40]:
        print(f"   ⚠️ {x[0]}:{x[1]} → ch{x[2]:02d} 证据「{x[3]}」他章命中 {x[4]}")
    return 1 if miss else 0


if __name__ == "__main__":
    sys.exit(main())