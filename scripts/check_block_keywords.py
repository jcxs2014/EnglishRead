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

⭐ **同时做结构计数对账**（2026-09-29 补，起因是一次批量改写脚本损坏 15 章）：
`audit_structure.py` 对「分析块被整段复制」这类损坏**报 0**（它按块内子项判，不看块数与子项数
是否一一对应）。本脚本按文件核对四个数：
  `> **原句 N:**` 行数 == `**关键词**：` 行数 ｜ `## 本章词汇` 出现 1 次
  `## 一句话总结` 出现 1 次 ｜ 引语块数在 3–8 之间（言情精简格式配额）
损坏的形态是**内容重复 + 后半段整体漂移**（`zip()` 静默截断的典型产物），
此时 `## 本章词汇` / `## 一句话总结` 会出现两次、关键词行数会多于引语块数——四项里至少一项对不上。
"""
import re
import sys
from pathlib import Path

QUOTE_RE = re.compile(r'^> \*\*原句 (\d+):\*\* "(.*)"$', re.M)
BLOCK_RE = re.compile(r'^> \*\*原句 (\d+):\*\* ', re.M)
# ⚠️ 2026-10-01 新增：编号 + 引语头的整体迭代器。编号、引语、关键词三者必须同源切分，
# 否则切块与取号口径不一致会让 zip() 错位（详见 check() 内注释）。
BLOCK_ITER = re.compile(r'^> \*\*原句 (\d+):\*\* (.*)$', re.M)
# ⚠️ 2026-10-01 修正：原式 ^\*\*关键词\*\*：  行首锚定，只认「顶格」形态；
#    而本库通行形态是列表项 `- **关键词**：…`（行首是 `- `）⇒ 47 章全报「关键词行 0」，
#    整类假红。改为接受「行首可选列表符号」。
KW_RE = re.compile(r'^[ \t]*(?:[-*+][ \t]+)?\*\*关键词\*\*：(.*)$', re.M)


def paras(text: str):
    return [p.strip() for p in text.split('\n\n') if p.strip()]


def check(md: Path, book: Path):
    m = re.search(r'ch(\d+)', md.name)
    if not m:
        return [f"{md.name}: 文件名缺 chNN 前缀，无法定章"]
    n = int(m.group(1))
    s = md.read_text(encoding="utf-8")
    out = []
    # --- 结构计数对账（先做，因为它最便宜且能兜住一切后续判断）---
    nq = len(BLOCK_RE.findall(s, re.M))
    nkw = len(KW_RE.findall(s))
    nvocab = len(re.findall(r'^## 本章词汇', s, re.M))
    nsum = len(re.findall(r'^## 一句话总结', s, re.M))
    if nq == 0:
        return [f"{md.name}: 未找到任何 `> **原句 N:**` 引语块"]
    if nkw != nq:
        out.append(f"{md.name}: 结构对账失败 —— 关键词行 {nkw} ≠ 引语块 {nq}（内容可能被整段复制）")
    if nvocab != 1:
        out.append(f"{md.name}: 结构对账失败 —— `## 本章词汇` 出现 {nvocab} 次（应为 1）")
    if nsum != 1:
        out.append(f"{md.name}: 结构对账失败 —— `## 一句话总结` 出现 {nsum} 次（应为 1）")
    if not 3 <= nq <= 8:
        out.append(f"{md.name}: 引语块 {nq} 个，超出言情精简格式的 3–8 配额")
    hits = sorted((book / "text").glob(f"ch{n:02d}_*.txt"))
    if len(hits) != 1:
        return out + [f"{md.name}: 期望恰好 1 个 text/ch{n:02d}_*.txt，实得 {len(hits)}"]
    t = hits[0].read_text(encoding="utf-8")
    ps = paras(t)
    # ⚠️ 2026-10-01 修正（本书 ch02 触发）：原实现用 BLOCK_RE 切块、却用 QUOTE_RE 取
    # 「编号 + 引语」，**两者口径不一致**——QUOTE_RE 要求引语被直双引号包裹，而引语行
    # 同样常见「原文弯引号」或「完全不加引号」两种形态。那类文件 BLOCK_RE 切出 N 块、
    # QUOTE_RE 只取到 M<N 个，`zip()` 随即**错位配对**：把靠前块的关键词报在靠后块的
    # 编号名下。实测 ch02（10 块里 2 块用弯引号）把原句 1 的关键词报成「原句 3」，
    # 偏移量恰为 N−M。
    # 危害不止噪音：错位会让**真实的关键词越界被报在别的块名下**，复核时极易被当成假阳放过。
    # 处置：按块整体切分（编号 / 引语 / 关键词三者同源），配对不再跨口径；并剥掉包裹引号。
    for m in BLOCK_ITER.finditer(s):
        num, body = m.group(1), m.group(2)
        # body 到下一个引语块头（或文件末）为止
        nxt = s.find("\n> **原句 ", m.end())
        block = s[m.end(): nxt if nxt != -1 else len(s)]
        q = body.strip()
        if len(q) > 1 and q[0] in '"“‘' and q[-1] in '"”’':
            q = q[1:-1]
        if q not in t:
            out.append(f"{md.name} 原句{num}: 引语非本章 text/ 逐字连续子串")
            continue
        if sum(1 for p in ps if q in p) != 1:
            out.append(f"{md.name} 原句{num}: 引语跨自然段（拼接红线）")
        # ⚠️ 2026-10-01 修正：原实现只按「；」切分，而本库关键词的**通行写法是 ` / `**
        # （实测跨书抽样：`stunned / flabbergasted / so shocked he'll faint`）⇒ 未命中分隔符的
        # 整串「a / b / c」被当成**一个**关键词去引语里找，必然查无 ⇒ 7/7 块全假红。
        # 判据不变（每个关键词须能在本块引语内逐字找到），只是把分隔符补齐。
        # ⚠️ 2026-10-01 第二次补（The Ghost of You 五步审查实测）：上次补了 ` / `，
        # 但全库主流关键词分隔符还有 ` · `（间隔号，Last Girl Breathing 系 24 章
        # 全部如此）⇒ 整串「a · b · c」被当成一个关键词，24 文件 169 块全假红。
        # 把 `·` 补进切分类；判据不变（每个关键词须能在本块引语内逐字找到）。
        kws = [k.strip() for k in re.split(r"[；;／/·]", KW_RE.search(block).group(1)) if k.strip()] \
            if KW_RE.search(block) else []
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
