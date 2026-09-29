#!/usr/bin/env python3
"""引语块覆盖度自检：引语是否短于它所支撑的分析（AGENTS 第 9 条 a2）。

**发现的缺陷类（2026-09-29《The Bookshop by the Bay》实测）**：
写作时先写分析、再从同一段落里挑 1–2 句当引语，于是

  ① **引语截短**——引语逐字正确（verify_quotes 100% 绿），但短于中文理解/关键词
     所覆盖的**同段连续原文**。六道引语门禁结构上全部看不见（它们只验「引语在不在
     原文」，不验「引语够不够撑起分析」）；
  ② **关键词在块外**——AGENTS 第 9 条 b 要求关键词能在该块引语中找到，但
     `check_anchor` 只在**词全书查无**时判红；词在原文里、只是不在本块 ⇒ 只报 ⚠️ 不判红。
  ③ **关键词的词替换型语义反转**——`Parker is on the guest list` 被写成
     `not on the guest list`。flat 归一化、指纹、逐章归属全部通过（两串词都在原文里），
     只有「关键词必须在块内」这一条能抓到。

三项都是**写作期可预防**的：先定引语全文再写分析（8.1 第 2 步的顺序），
或让关键词只从已注入的引语里挑。本脚本是事后兜底，不替代那个顺序。

判定（三条都要过）：
  - 引语是本章 text/ 的**逐字连续子串**（raw，不用 flat 归一化）；
  - 引语只来自**一个自然段**（跨段拼接红线）；
  - 该块**每个关键词**都能在这条引语里逐字找到。

⚠️ **投毒自证结果（2026-09-29，写入时实测）——不要高估它的覆盖面**：
  - ✅ 已证明可触发：①「关键词不在块内」②「引语非本章逐字子串」
    （各注入 1 例，均如实报出；还原后复跑回到 0）。
  - ⚪ **「跨段拼接」这一条在本书的 md 格式下结构上不可触发**——`> **原句 N:**` 是单行，
    写不进段落分隔符 `\n\n`。它是**防御性守卫**：若将来改成多行引语块才生效。
    跨段/跨标签拼接的真防线是 `sweep_full` 的 🔶 通道与写作期的逐块摘录，不是本脚本。

用法:  python3 scripts/check_block_keywords.py "<书目录>" [md ...]
退出:  0 全过 ｜ 1 有问题 ｜ 2 参数/环境错误
"""
import re
import sys
from pathlib import Path

QUOTE_RE = re.compile(r'^> \*\*原句 (\d+):\*\* "(.*)"$', re.M)
BLOCK_RE = re.compile(r'^> \*\*原句 (\d+):\*\* ', re.M)
KW_RE = re.compile(r'^\*\*关键词\*\*：(.*)$', re.M)


def paras(text: str):
    return [p.strip() for p in text.split('\n\n') if p.strip()]


def check(md: Path, book: Path):
    m = re.search(r'ch(\d+)', md.name)
    if not m:
        return [f"{md.name}: 文件名缺 chNN 前缀，无法定章"]
    n = int(m.group(1))
    hits = sorted((book / "text").glob(f"ch{n:02d}_*.txt"))
    if len(hits) != 1:
        return [f"{md.name}: 期望恰好 1 个 text/ch{n:02d}_*.txt，实得 {len(hits)}"]
    t = hits[0].read_text(encoding="utf-8")
    ps = paras(t)
    s = md.read_text(encoding="utf-8")
    out = []
    chunks = re.split(r'^> \*\*原句 \d+:\*\* ', s, flags=re.M)[1:]
    nums = [x for x in QUOTE_RE.findall(s)]
    for (num, q), chunk in zip(nums, chunks):
        if q not in t:
            out.append(f"{md.name} 原句{num}: 引语非本章 text/ 逐字连续子串")
            continue
        if sum(1 for p in ps if q in p) != 1:
            out.append(f"{md.name} 原句{num}: 引语跨自然段（拼接红线）")
        kws = [k.strip() for k in KW_RE.search(chunk).group(1).split("；") if k.strip()] \
            if KW_RE.search(chunk) else []
        miss = [k for k in kws if k.lower() not in q.lower()]
        if miss:
            out.append(f"{md.name} 原句{num}: 关键词不在本块引语内 → {miss}")
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    book = Path(sys.argv[1])
    mds = [Path(x) for x in sys.argv[2:]] or sorted(book.glob("ch*.md"))
    if not mds:
        print(f"❌ {book} 下没有 ch*.md")
        return 2
    bad = []
    for md in mds:
        bad += check(md, book)
    for b in bad:
        print("  ❌ " + b)
    print(f"=== 引语块覆盖度：{len(mds)} 个 md，问题 {len(bad)} 处 ===")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
