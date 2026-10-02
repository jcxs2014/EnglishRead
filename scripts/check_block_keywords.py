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
# ⚠️ 2026-10-02 修正（Beach Read 实测）：上一版只认 `**关键词**：`（冒号在粗体**外**），
#    而本书全书用 `**关键词：**`（冒号在粗体**内**）⇒ 28 个文件全报「关键词行 0 ≠
#    引语块 N」。全库两种形态并存（实测 8220 文件用外置 / 1964 用内置），
#    与 gen_overview 2026-09-28 修的 `**中文理解**：` 是**同一个**已记录故障：
#    单形态正则静默抽 0 条，症状是「结构对账失败」而非「格式错」，极难回溯。
#    ⇒ 两种形态都必须接受（判据不变，只放宽形态）。
KW_RE = re.compile(r'^[ \t]*(?:[-*+][ \t]+)?\*\*关键词(?:\*\*：|：\*\*)[ \t]*(.*)$', re.M)

# 短引语阈值：与 check_short_quotes 的 <20 字符口径一致（同一概念只留一处数值，
# 两处各写一个数就会漂）。短于此长度的引语不适用「唯一命中 1 个自然段」判据。
SHORT_Q = 20

# 「够长自然段」阈值：短于此的自然段产不出有分析价值的引语块。
# 用于「源文本太短 ⇒ 块数下限不适用」判据（见 check() 内注释）。
MIN_SRC_PARA = 40

_TYPO = {'’': "'", '‘': "'", '“': '"', '”': '"',
         '—': '-', '–': '-', '…': '...'}


def norm(s: str) -> str:
    """md 与 text/ 的归一口径：撇号/引号/破折号统一 + 空白折叠。

    ⚠️ 2026-10-02（Beach Read ch02 原句 1 实测）：原实现拿**原样** q 去 `in` **原样** t，
    而 md 用直撇号 `'`、epub/text/ 用弯撇号 `’` ⇒ 逐字正确的引语被报「非本章 text/
    逐字连续子串」。这类假红最坏：它把**真缺陷与量具缺陷混在同一条消息里**。
    与 AGENTS「核含 U+2019 的串不可用 shell grep」是同一条纪律的代码形态。
    """
    for a, b in _TYPO.items():
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip()


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
    # ⚠️ 2026-10-02 收口：原只认 chNN_*.txt，空格命名的书恒 0 命中（假红型）
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).resolve().parent))
    from chapter_text_path import find_chapter_text
    _p = find_chapter_text(str(book), n)
    if _p is None:
        return out + [f"{md.name}: 找不到 text/ch{n:02d}*.txt（分隔符已兼容 _ . 空格）"]
    t = Path(_p).read_text(encoding="utf-8")
    ps = paras(t)
    tn = norm(t)
    pn = [norm(x) for x in ps]
    if not 3 <= nq <= 8:
        # ⚠️ 2026-10-02（Beach Read ch13 实测，用户裁定「删到 3-8 处」后暴露）：
        #   ch13 全文只有一句话（`I DREAMED ABOUT GUS Everett and woke up needing
        #   a shower.`，提取件 73 B / 1 个自然段）⇒ **物理上凑不出 3 块**。
        #   「一条引语只取一个说话轮次/一个自然段」是硬禁令，也不能为凑配额造块。
        #   判据写成**结构性**的而非「ch13 特例」：**源文本里够长的自然段不足 3 个时，
        #   下限不适用**（降为提示）。真实短章在别的书里也该自动豁免。
        #   ⚠️ 本判据必须放在 t/ps 已读出**之后**——第一版写在前面，
        #   ps 未定义 ⇒ UnboundLocalError 让整个工具崩掉；负控表现为
        #   「注水到 12 块也不报警」，差点被读成「判据被放松了」。
        #   **「从不报错」的第三种成因：工具自己崩了。**
        src_paras = [p for p in ps if len(norm(p)) >= MIN_SRC_PARA]
        if len(src_paras) < 3:
            out.append(f"{md.name}: ⚠️ 提示·源文本仅 {len(src_paras)} 个够长自然段"
                       f"（<{MIN_SRC_PARA} 字符），块数下限不适用（现有 {nq} 块）")
        else:
            out.append(f"{md.name}: 引语块 {nq} 个，超出言情精简格式的 3–8 配额")

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
        qn = norm(q)
        if qn not in tn:
            out.append(f"{md.name} 原句{num}: 引语非本章 text/ 逐字连续子串")
            continue
        if sum(1 for p in pn if qn in p) != 1:
            # ⚠️ 2026-10-02 修正（Beach Read ch18 原句 16 实测）：原判据对**所有**引语
            # 都要求「恰好命中 1 个自然段」，而 `Sorry.`（5 字符）在该章 3 个自然段里
            # 都出现 ⇒ 报「引语跨自然段（拼接红线）」。
            # 但**拼接红线要抓的是「用 … 把两段缝成一块」**——1 个词的引语**在结构上
            # 不可能**是两段的拼接（拼不出 `Sorry.`）。即：这是判据**不适用**，
            # 不是内容有问题，也不是「为过门禁而放宽」。
            # ⇒ 短于 SHORT_Q 的引语不适用本判据，降级为提示，由 check_short_quotes
            #   （<20 字符兜底）负责「是否逐字存在于书中」这一半。
            if len(qn) < SHORT_Q:
                out.append(f"{md.name} 原句{num}: ⚠️ 提示·短引语（{len(qn)} 字符）"
                           f"命中 {sum(1 for p in pn if qn in p)} 个自然段，拼接判据不适用")
            else:
                out.append(f"{md.name} 原句{num}: 引语跨自然段（拼接红线）")
        # ⚠️ 2026-10-01 修正：原实现只按「；」切分，而本库关键词的**通行写法是 ` / `**
        # （实测跨书抽样：`stunned / flabbergasted / so shocked he'll faint`）⇒ 未命中分隔符的
        # 整串「a / b / c」被当成**一个**关键词去引语里找，必然查无 ⇒ 7/7 块全假红。
        # 判据不变（每个关键词须能在本块引语内逐字找到），只是把分隔符补齐。
        # ⚠️ 2026-10-01 第二次补（The Ghost of You 五步审查实测）：上次补了 ` / `，
        # 但全库主流关键词分隔符还有 ` · `（间隔号，Last Girl Breathing 系 24 章
        # 全部如此）⇒ 整串「a · b · c」被当成一个关键词，24 文件 169 块全假红。
        # 把 `·` 补进切分类；判据不变（每个关键词须能在本块引语内逐字找到）。
        # ⚠️ 2026-10-02 第三次补（接进 gate.sh ⑱ 后对存量书回归实测）：全库分隔符实测
        # 频次 `/`28104 · `（`22608 · `,`15491 · `）、`6295 · `；`6207 · `·`4369 · `、`4050。
        # 漏掉 **`、`**（中文顿号）⇒ 写成「关键词（注释）、关键词（注释）」的书，
        # 整个 `a（甲）、b（乙）` 被当成**一个**关键词，恒查无 ⇒ 310 条假红
        # （the-wrong-sister 全书命中）。顿号不会出现在英文词组内部，可以安全切分；
        # **`,` / `，` 不加**——它们是英文短语自身的成分（`multi-claim, hedging` 是一个词条）。
        kws = [k.strip() for k in re.split(r"[；;／/·、]", KW_RE.search(block).group(1)) if k.strip()] \
            if KW_RE.search(block) else []
        # ⚠️ 2026-10-02（Beach Read 修完 text 侧后仍报 7 条时定位）：上一版只把**引语**归一
        # （qn），关键词却仍拿**原样** k 去比 **原样** q ⇒ md 用直撇号 `'`、正文用弯撇号
        # `’` 时必然查无。两侧必须走**同一个** norm()——判据不变，只统一口径。
        # 同批补：关键词尾部的**中文注释**（`HAVE（全大写强调）`）是本库通行写法，
        # 而注释部分按定义不在引语里 ⇒ 不剥就恒假红（实测 3 条）。
        # ⚠️ 2026-10-02（Beg, Borrow, or Steal ch03/07/08 实测）补第四类形态：
        # 关键词**自身带句内标点**时（`gently. Tenderly.`），norm() 只统一撇号/引号/
        # 破折号并折叠空白、**不剥句点与逗号** ⇒ 引语里逐字存在的词被报「不在块内」
        # （实测 5 条假红）。判据不变（每个关键词仍须能在本块引语内找到），
        # 只把两侧都归一到字母数字，与 check_chapter_quotes / sweep_full 同口径。
        def _flat(x: str) -> str:
            return re.sub(r'[^a-z0-9]', '', x.lower())
        miss = [k for k in kws
                if _flat(re.sub(r"（[^）]*）|\([^)]*\)", "", k)) not in _flat(qn)]
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
        # ⚠️ 2026-10-02：提示型**不得打 ❌ 前缀**——AGENTS 三档里提示型「只记不改」，
        #   而 gate.sh ⑱ 的退出码按「是否含 ❌」聚合 ⇒ 标错档会把提示变成阻断。
        #   判据用「含」不用 startswith：条目是 `文件名 原句N: ⚠️ 提示…`，前缀是文件名。
        if "⚠️ 提示" in b:
            print("  ⚠️ " + b.split("⚠️ 提示", 1)[1].join(["提示", ""]).lstrip("·"))
        else:
            print("  ❌ " + b)
    print(f"=== 引语块覆盖度：{len(mds)} 个 md，问题 {len(bad)} 处 ===")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
