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

QUOTE_RE = re.compile(r'^> \*\*原句 (\d+)[：:]\*\* "(.*)"$', re.M)
BLOCK_RE = re.compile(r'^> \*\*原句 (\d+)[：:]\*\* ', re.M)
# ⚠️ 2026-10-01 新增：编号 + 引语头的整体迭代器。编号、引语、关键词三者必须同源切分，
# 否则切块与取号口径不一致会让 zip() 错位（详见 check() 内注释）。
BLOCK_ITER = re.compile(r'^> \*\*原句 (\d+)[：:]\*\* (.*)$', re.M)
# ⚠️ 2026-10-04 新增：短篇合集档用**裸圈码** `① "…"` 作引语块头（本库短篇合集
# 体裁对应格式表＝逐篇精读 10 处五子项，与长篇精简档的 `> **原句 N:**` 不是一套）。
# 而本工具三张正则只认 `原句 N:` ⇒ 圈码书 nq 恒 0 ⇒ 走到「未找到任何引语块」就 return，
# **关键词越界与拼接检查整段空转**（假阴性比假红更坏：它报 0 缺陷而实际没查）。
# 与 `check_struct_indep.py` 的 anthology 档同口径（特征节 `## 精读结束总结` +
# `## 可迁移表达` + 圈码能解析），判据本身一处不改，只补抬头识别。
CIRCLED = '①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕'
CIRC_BLOCK_RE = re.compile(r'^([' + CIRCLED + r'])\s+["\']', re.M)
# 圈码是**单行**形态（引语整段写在一行，分析子项另起行）⇒ 不需要续行合并。
# ⚠️ 计数与切块走**同一张**正则（只差有没有捕获引语体），与 BLOCK_RE / BLOCK_ITER
# 同构——否则又是一次「切块与取号口径不一致」的 zip() 错位（2026-10-01 已修过一次）。
CIRC_ITER = re.compile(r'^([' + CIRCLED + r'])\s+["\'](.*)$', re.M)
# 短篇合集档的**独有特征节**（两者皆须命中才认档，避免与长篇精简档抢档）。
ANTH_MARKS = (r'^## 精读结束总结', r'^## 可迁移表达')
# ⚠️ 2026-10-06 新增（The Language of Knives 批1 实测 4 章假红）：
#   短篇合集在库里有**两套 H2 形态**，只认一套 ⇒ 另一套全部落进「言情精简 3–8」误判：
#   ① Ken Liu / Fold Catastrophes 变体：`## 精读` + `## 精读结束总结` + `## 可迁移表达`
#     （the-passing-of-the-dragon / fold-catastrophes，见上 ANTH_MARKS）
#   ② **体裁对应格式表的短篇合集档**（docs/新书启动模板.md:1101）：
#     `## 本篇导航` + `## 精读` + `## 词汇分级` + `## 一句话总结`
#     （the-language-of-knives；权威判据是**四个特征节同时在**）
#   ⇒ 两套都认；配额同为固定 10（ANTH_RANGE）。
ANTH_MARKS_V2 = (r'^## 本篇导航', r'^## 精读', r'^## 词汇分级', r'^## 一句话总结')
# 短篇合集里**篇幅显著短于正篇**的篇目（引言/后记一类）按体裁表凑不出 10 处时，
# 块数下限不适用的源文本长度阈值（正文归一后字符数）。写成结构性判据而非「某章特例」。
ANTH_SHORT_SRC = 20000
# 该档块数配额：**固定 10 处**（体裁对应格式表：短篇合集＝逐篇精读 10 处五子项）。
ANTH_RANGE = (10, 10)
# ⚠️ 2026-10-01 修正：原式 ^\*\*关键词\*\*：  行首锚定，只认「顶格」形态；
#    而本库通行形态是列表项 `- **关键词**：…`（行首是 `- `）⇒ 47 章全报「关键词行 0」，
#    整类假红。改为接受「行首可选列表符号」。
# ⚠️ 2026-10-02 修正（Beach Read 实测）：上一版只认 `**关键词**：`（冒号在粗体**外**），
#    而本书全书用 `**关键词：**`（冒号在粗体**内**）⇒ 28 个文件全报「关键词行 0 ≠
#    引语块 N」。全库两种形态并存（实测 8220 文件用外置 / 1964 用内置），
#    与 gen_overview 2026-09-28 修的 `**中文理解**：` 是**同一个**已记录故障：
#    单形态正则静默抽 0 条，症状是「结构对账失败」而非「格式错」，极难回溯。
#    ⇒ 两种形态都必须接受（判据不变，只放宽形态）。
#   实测：本库 ch09 该正则 15 命中 = 引语块 15，两种形态混写时计数仍等于块数。
# ⚠️ 2026-10-04 第四次（Give Me Butterflies 实测，306 条假红）：上面那次只改了**前缀**，
#   忘了**收尾**——`**关键词：** absorb，branded` 里 `\*\*关键词[：:]` 匹配掉 `**关键词：`
#   之后，剩下的正好是 `** absorb，branded`，捕获组**恒以 `** ` 开头** ⇒ 每个关键词首词
#   都变成 `**`，于是「关键词不在本块引语内」**整类假红**（参考章 ch01 同样命中）。
#   ⇒ 收尾的 `**` 必须一起消费掉。判据不变，只补收尾。
KW_RE = re.compile(r'^[ \t]*(?:[-*+][ \t]+)?\*\*关键词[：:]\*\*[ \t]*(.*)$', re.M)
#   上面 KW_RE 只认 `**关键词**：`（冒号在粗体**外**）……但**它自己写错了**：
#   正则里 `\*\*关键词[：:]` 把冒号放进了**同一个**粗体里，匹配的是 `**关键词：**`
#   （即下面那条注释 2026-10-02 记的「冒号在粗体内」形态）。
#   于是「冒号在粗体外」的 `**关键词**：X`（本库 8220 文件的通行形态）
#   **两条正则都不认**：KW_RE 要求 `**关键词：`，KW_RE_PLAIN 被 `(?!\*\*)` 排除
#   ⇒ 关键词行恒 0 ⇒ 9 章全报「结构对账失败 —— 关键词行 0 ≠ 引语块 N」。
#   症状与注释里 2026-10-01 / 10-02 / 10-04 三次记的**完全同族**（单形态正则静默抽 0 条），
#   只是这次错在被当成「已修好的那一半」。⇒ 补第四条：`**关键词**：` 显式形态。
#   实测：本库 ch09 该正则 15 命中 = 引语块 15，两种形态混写时计数仍等于块数。
KW_RE_BOLD_OUT = re.compile(r'^[ \t]*(?:[-*+][ \t]+)?\*\*关键词\*\*[：:][ \t]*(.*)$', re.M)
# ⚠️ 2026-10-04 第三种形态（短篇合集档实测，the-best-short-stories-2026 20/20 命中）：
#   该档写**裸** `- 关键词：…`（不加粗）。前两种都是「冒号在粗体外/内」的**加粗**形态，
#   裸形态一条都认不到 ⇒ 关键词行恒 0 ⇒ 「结构对账失败」+ 关键词检查整段空转。
#   与上面两次修的是**同一个**故障：单形态正则静默抽 0 条。
#   全库实测（14080 个 ch*/0* md）：加粗外置 65819 / 加粗内置 17715 / **裸形态 12005**
#   （分布在 1532 个文件）⇒ 裸形态不是孤例，是第三大通行写法。判据不变，只补形态。
#   ⚠️ 裸形态正则**必须排除** `**关键词` 前缀与 `**关键词：**` 形态（否则与上面两条
#   重复计数 ⇒ nkw 翻倍 ⇒ 反过来制造新的「对账失败」）：下面用 `(?!\*\*)` 与
#   `(?<!\*\*)` 双向排除，实测三形态在同一文件里混写时计数仍等于块数。
KW_RE_PLAIN = re.compile(r'^[ \t]*(?:[-*+][ \t]+)?(?!\*\*)关键词：(?!\*\*)[ \t]*(.*)$', re.M)

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


# ⚠️ 2026-10-02（另一实例回报 the-beasts-we-bury 整类假红后定位）：
#   ① 分隔符集合 `[；;／/·、]` **漏了逗号**——该书 224/225 行关键词用 `,` 分隔，
#      整行被当成**一个**关键词去引语里找，必报不在（全库 79754 条关键词行里逗号 15491）。
#      但逗号**不能无条件当分隔符**：`（her, 2003）` 这类括号注释内部含逗号，
#      切开会得到「（her」这种残片 ⇒ 判据改成**括号外才算分隔符**（括号内含逗号者全库仅 11 条）。
#   ② 原实现只对**关键词**剥括号，命中判据是「剥括号后的关键词 ∈ 引语」——`(she?)` 这类
#      **分析者自加的旁注**因此能匹配。但它**不能反过来剥引语的括号**：括号也可能是
#      **原文自带的插入语**（ch17 `(whether intentionally or not)`、ch20 `(as punishment…)`
#      都在 text/ 里逐字存在）⇒ 剥引语会把原文内容删掉，真实关键词反而报不在。
#      正解是**或**关系：关键词原样命中、或剥括号后命中，任一成立即算命中。
_BRACKET = re.compile(r"（[^）]*）|\([^)]*\)")
# ⚠️ 2026-10-04 补全角逗号（Give Me Butterflies 实测，306 条假红）：本库**关键词行的通行写法
#   是全角 `，`**（参考章 ch01 与该书 47 章全部如此），而这里只收半角 `,` ⇒ 整行被当成
#   **一个**关键词去引语里找，必然查不到 ⇒ 又一整类假红。与上面四次同型：
#   **分隔符/形态的单一实现静默失配**，症状一律是「关键词不在引语内」而非格式错。
#   判据不变（关键词须落在本块引语内），只把两种逗号都认。
_SEP = set("；;／/·、,，")


def _split_kw(s: str) -> list:
    """按 `；;／/·、` 与**括号外**的 `,` 切分关键词；括号深度内的字符一律并入当前词。"""
    out, buf, depth = [], [], 0
    for ch in s:
        if ch in "（(":
            depth += 1
        elif ch in "）)":
            depth = max(0, depth - 1)
        if depth == 0 and ch in _SEP:
            out.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    out.append("".join(buf))
    return [x.strip() for x in out if x.strip()]


def _flat(x: str) -> str:
    return re.sub(r"[^a-z0-9]", "", x.lower())


def _kw_in_quote(k: str, qflat: str) -> bool:
    """关键词是否落在这条引语里（判定口径：逐字 + 允许词形外的标点/空白差异）。

    ⚠️ 2026-10-03 修正（The Boy from the Sea ch01 实测的假红）：原实现只有
    `_flat(k) not in _qflat` 一条判据，而 `_flat` **剥掉所有空格** ⇒ 任何**跨空格
    短语**（`eyed suspiciously` / `mined Mersey coal` / `sea to eternity`）被压成
    `eyedsuspiciously` 去找，而引语里 `eyed` 与 `suspiciously` 之间隔着别的词
    ⇒ **两个词都逐字在引语内，仍被判「不在本块引语内」**。
    实证：`Eunan eyed Ambrose suspiciously.` + 关键词 `eyed suspiciously`
    ⇒ 报假红（而 `eyed`/`suspiciously` 各自 flat 命中均为 True）。

    修法（**判据不放宽，只让跨空格短语能按其真实形态成立**）：
      ① 原样/剥括号的整串命中（保持既有判据，行为不变）；或
      ② 关键词按空白切成词序列，**每个词按序**在引语的 flat 串里出现。
    ⚠️ 与 AGENTS「剥括号类归一不能两侧同剥」同源：归一必须问「这个差异是
    分析者加的还是原文自带的」——空格被 `_flat` 剥掉是**工具的归一副作用**，
    不是原文形态差异。
    """
    if _flat(k) in qflat or _flat(_BRACKET.sub("", k)) in qflat:
        return True
    words = [w for w in re.split(r"\s+", k.strip()) if w]
    if len(words) < 2:
        return False
    pos = 0
    for w in words:
        fw = _flat(w)
        if not fw:
            continue
        i = qflat.find(fw, pos)
        if i < 0:
            return False
        pos = i + len(fw)
    return True


# ⚠️ 2026-10-03 修正（Everything Is Poison ⑱ 报 31 块「关键词不在本块引语内」实测）：
#   本书的长引语采用**引用块内多行**形态——引语正文换行后仍以 `> ` 起头，段间空行写成 `>`：
#     > **原句 1[：:]\*\* "It should, perhaps, not come as such a shock … record inventory.
#     >
#     > “What are you doing?” Carmela gasps, unclear whether she’s talking to … occur."
#   而 `BLOCK_ITER` 是 `^…$` 单行式，捕获的 body **只有第一行** ⇒ 挂在第二行的
#   关键词（gasps / the very bones of the apothecary …）**逐字都在块里却全报越界**。
#   三个写作代理各自独立回报同一条 ⇒ 是工具口径，不是内容缺陷（AGENTS 第 3 条假红型）。
#   ⚠️ 修法必须**排除**另一类既有形态：the-dream-hotel 那种「整块（含分析子项）都包在
#   引用块里」的书——若把它的 `> **中文理解：**` 一并并入引语，就会凭空造出「引语跨自然段」
#   的新假红。因此续行判据取**两个负条件**：不含中文字符、不含 `**` 粗体标记
#   （本库所有分析子项标签都带粗体或中文）。命中即停，不跨越第一个分析行。
_CONT_STOP = re.compile(r'[\u4e00-\u9fff]|\*\*')


def _sec_text(block: str, header: str) -> str:
    """取出块内某个分析子项（`**为什么这样写**` / `**读者视角提示**`）到下个子项之间的正文。"""
    i = block.find(header)
    if i < 0:
        return ""
    tail = block[i + len(header):]
    j = tail.find("\n**")
    return tail if j < 0 else tail[:j]


# ⚠️ 2026-10-05 新增（Heirs of the Cursed 五步审查 d 步）：**第 9 条 b 的语境延伸词豁免**。
#   规则原文：「块内『关键词』的英文词必须能在该块引语中找到（允许词形变化）；
#   **语境延伸词必须在『为什么这样写』中有呼应**，否则替换为引语逐字词。」
#   本脚本原先只实现了前半句 ⇒ 把后半句**明文允许**的词与真缺陷同色报 ❌。
#   实测（Heirs 五步审查）：17 条真缺陷整改完后仍报 23 条，逐词裁决**全部**满足该豁免。
#   处置：命中豁免的降为 `⚠️ 提示` 并**单独计数**（不静默隐藏），未命中的仍判 ❌ 阻断。
#   ⚠️ 两侧仍走同一个 `_flat`（与引语判定同口径）；`_flat < 4` 字符的不豁免，
#     免得 `the` / `and` 这类虚词靠一次巧合命中就把真缺陷洗白。
def _echoed(kw: str, block: str) -> bool:
    f = _flat(_BRACKET.sub("", kw))
    if len(f) < 4:
        return False
    for h in ("**为什么这样写", "**读者视角提示"):
        sec = _sec_text(block, h)
        if sec and f in _flat(sec):
            return True
    return False


def _join_quote_lines(body: str, block: str):
    """把引用块内换行书写的引语续行并入首行，返回 (完整引语串, 是否并到了续行)。"""
    parts = [body.strip()]
    for ln in block.split("\n"):
        raw = ln.strip()
        if raw in ("", ">"):
            continue
        if not raw.startswith(">"):
            break
        cont = raw[1:].strip()
        if not cont or _CONT_STOP.search(cont):
            break
        parts.append(cont)
    return " ".join(parts), len(parts) > 1


def check(md: Path, book: Path):
    # ⚠️ 2026-10-03 修正（Evie ch01a/ch04a/ch11a 实测假红）：原式 `ch(\d+)` **丢掉插叙节的
    # 字母后缀** ⇒ ch01a 被取数字 1 ⇒ find_chapter_text 命中 `text/ch01_chapter_1.txt`
    # ⇒ 用**正章**的 text 当参照集，本章逐字正确的引语全报「引语跨自然段（拼接红线）」。
    # find_chapter_text 本身支持 "02a" 写法（见其 docstring），是调用方丢了信息。
    m = re.search(r'ch(\d+)([a-z]?)', md.name)
    if not m:
        return [f"{md.name}: 文件名缺 chNN 前缀，无法定章"]
    n = int(m.group(1))
    suffix = m.group(2)
    s = md.read_text(encoding="utf-8")
    out = []
    # --- 结构计数对账（先做，因为它最便宜且能兜住一切后续判断）---
    # ⚠️ 2026-10-03 修正：`Pattern.findall(string, *pos)` 的第二个位置参数是 **pos**，不是 flags；
    #   原写法 `findall(s, re.M)` 等于从第 8 个字符开始找——若某文件的引语块头落在前 8 字符内
    #   （负控实测：无 frontmatter 的裸块文件），首个块会被整块跳过、nq 少 1。
    #   re.M 已在 compile() 里烘进 pattern，此处第二个参数应删除。
    nq = len(BLOCK_RE.findall(s))
    nkw = (len(KW_RE.findall(s)) + len(KW_RE_PLAIN.findall(s))
           + len(KW_RE_BOLD_OUT.findall(s)))
    # ⚠️ 2026-10-02 假红型修正（本工具写死言情格式 `## 本章词汇` + 3–8 块配额，
    #   而非虚构论述格式用 `## 词汇分级` + 10 处 `## 选择性精读`）。全库非虚构书
    #   （nexus / an-expert-witness / down-girl / herlands …）逐个复跑全部报同两条，
    #   证实是**工具的格式假设**而非内容缺陷。按 AGENTS 第 3 条「假红型先修工具」处置：
    #   词表节标题认两种体裁；块数配额按体裁判（言情 3–8 / 非虚构上限 10，见体裁对应格式表）。
    is_nonfic = bool(re.search(r'^## 选择性精读', s, re.M))
    # ⚠️ 2026-10-04 加第三档：**短篇合集档**（特征节 `## 精读结束总结` + `## 可迁移表达`
    #   **且**圈码抬头能解析——与 check_struct_indep 的 anthology 档同口径，负控同款：
    #   认出档位不等于能解析它，解析不出就不认档，避免「少查」）。
    # 两套变体各自配自己的负控（脚本原原则「认出档位不等于能解析它」）：
    #   v1 Ken Liu 变体用圈码抬头 → 负控 = CIRC_BLOCK_RE 能解析出块；
    #   v2 体裁表短篇合集档用 `> **原句 N:**` → 负控 = BLOCK_RE 数得到块（本行 nq）。
    anth_v1 = (all(re.search(p, s, re.M) for p in ANTH_MARKS)
               and bool(CIRC_BLOCK_RE.search(s)))
    anth_v2 = (all(re.search(p, s, re.M) for p in ANTH_MARKS_V2)
               and nq > 0)
    is_anth = anth_v1 or anth_v2
    # ⚠️ 2026-10-06 修正（本条是**假阴性**，比假红更坏）：
    #   原式 `if is_anth: nq = len(CIRC_BLOCK_RE...)` **无条件用圈码覆盖**块数。
    #   它成立的前提是「短篇合集档＝圈码书」（Ken Liu / Fold Catastrophes 变体）。
    #   而体裁对应格式表的短篇合集档（docs/新书启动模板.md:1101）用的是
    #   `> **原句 N:**` ⇒ 覆盖后 nq 恒 0 ⇒ 走到下面 `if nq == 0: return`
    #   ⇒ **关键词越界 / 拼接红线整段空转，却报成「未找到任何引语块」**
    #   （The Language of Knives 批1 实测：4 个真实文件全落这条）。
    #   ⇒ 改为**按文件实际使用的抬头计数取大者**，两种形态都真查。
    n_circ = len(CIRC_BLOCK_RE.findall(s))
    if n_circ > nq:
        nq = n_circ
    nvocab = len(re.findall(r'^## (?:本章词汇|词汇分级)', s, re.M))
    nsum = len(re.findall(r'^## 一句话总结', s, re.M))
    if nq == 0:
        return [f"{md.name}: 未找到任何 `> **原句 N:**` 引语块"
                f"（短篇合集圈码 `① \"…\"` 同样计；本文件判为"
                f"{'短篇合集' if is_anth else '非短篇合集'}档）"]
    if nkw != nq:
        out.append(f"{md.name}: 结构对账失败 —— 关键词行 {nkw} ≠ 引语块 {nq}（内容可能被整段复制）")
    if nvocab != 1:
        out.append(f"{md.name}: 结构对账失败 —— 词表节（`## 本章词汇`/`## 词汇分级`）出现 {nvocab} 次（应为 1）")
    if nsum != 1:
        out.append(f"{md.name}: 结构对账失败 —— `## 一句话总结` 出现 {nsum} 次（应为 1）")
    # ⚠️ 2026-10-02 收口：原只认 chNN_*.txt，空格命名的书恒 0 命中（假红型）
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).resolve().parent))
    from chapter_text_path import find_chapter_text
    _p = find_chapter_text(str(book), "%02d%s" % (n, suffix))
    if _p is None:
        return out + [f"{md.name}: 找不到 text/ch{n:02d}{suffix}*.txt（分隔符已兼容 _ . 空格）"]
    t = Path(_p).read_text(encoding="utf-8")
    ps = paras(t)
    tn = norm(t)
    pn = [norm(x) for x in ps]
    if is_anth:
        lo, hi = ANTH_RANGE
        kind = "短篇合集格式的 10"
    else:
        lo, hi = (3, 10 if is_nonfic else 8)
        kind = "非虚构论述格式的 3–10" if is_nonfic else "言情精简格式的 3–8"
    if not lo <= nq <= hi:
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
        # ⚠️ 2026-10-04 加短篇合集档的第二个豁免（Fold Catastrophes ch01 引言实测）：
        #   短篇合集体裁表要求每篇 10 处，但合集里的**引言/后记类篇目**篇幅只有正篇的
        #   零头（ch01 4766 字符 vs 正篇 22k–66k）⇒ 凑 10 处必然违反「一条引语只取一个
        #   自然段」的硬禁令。判据同样写成结构性的：**源文本归一后短于 ANTH_SHORT_SRC
        #   字符时，下限不适用**（上限照旧——注水的 12 块仍要报）。
        src_paras = [p for p in ps if len(norm(p)) >= MIN_SRC_PARA]
        if len(src_paras) < 3:
            out.append(f"{md.name}: ⚠️ 提示·源文本仅 {len(src_paras)} 个够长自然段"
                       f"（<{MIN_SRC_PARA} 字符），块数下限不适用（现有 {nq} 块）")
        elif is_anth and len(tn) < ANTH_SHORT_SRC:
            out.append(f"{md.name}: ⚠️ 提示·短篇合集短篇目（源文本 {len(tn)} 字符"
                       f"<{ANTH_SHORT_SRC}），10 处下限不适用（现有 {nq} 块）")
        else:
            out.append(f"{md.name}: 引语块 {nq} 个，超出{kind}配额")

    # ⚠️ 2026-10-01 修正（本书 ch02 触发）：原实现用 BLOCK_RE 切块、却用 QUOTE_RE 取
    # 「编号 + 引语」，**两者口径不一致**——QUOTE_RE 要求引语被直双引号包裹，而引语行
    # 同样常见「原文弯引号」或「完全不加引号」两种形态。那类文件 BLOCK_RE 切出 N 块、
    # QUOTE_RE 只取到 M<N 个，`zip()` 随即**错位配对**：把靠前块的关键词报在靠后块的
    # 编号名下。实测 ch02（10 块里 2 块用弯引号）把原句 1 的关键词报成「原句 3」，
    # 偏移量恰为 N−M。
    # 危害不止噪音：错位会让**真实的关键词越界被报在别的块名下**，复核时极易被当成假阳放过。
    # 处置：按块整体切分（编号 / 引语 / 关键词三者同源），配对不再跨口径；并剥掉包裹引号。
    # ⚠️ 2026-10-04：短篇合集档换用圈码迭代器（抬头不同，**判据与后续处理一字不改**）。
    if is_anth:
        _iter = CIRC_ITER

        def _next_head(pos):
            mm = CIRC_BLOCK_RE.search(s, pos)
            return mm.start() if mm else len(s)
    else:
        _iter = BLOCK_ITER

        def _next_head(pos):
            i = s.find("\n> **原句 ", pos)
            return i if i != -1 else len(s)

    for m in _iter.finditer(s):
        num, body = m.group(1), m.group(2)
        # body 到下一个引语块头（或文件末）为止
        block = s[m.end(): _next_head(m.end())]
        q, q_multi = _join_quote_lines(body, block)
        # ⚠️ 2026-10-02 修正（Bird of a Thousand Stories 终验实测，ch18 原句5 假红）：
        # 本库**同一批书**里存在两种写法 —— `> **原句 1[：:]\*\* "…"` 与
        # `> **原句 1: "…"**`（整行含引号的部分被粗体包住）。后者下 `BLOCK_ITER`
        # 捕获的 body 末尾带 `**`，剥引号后仍剩一个 `**` ⇒ 归一后与原文对不上
        # ⇒ 报「非逐字子串」或「跨自然段」。
        # 处置：**先剥行尾粗体标记，再剥包裹引号**（顺序不能反）。
        if q.endswith("**"):
            q = q[:-2].strip()
        # ⚠️ 2026-10-03 修正（Deathless ch14 原句 1/3 实测假红）：上面只剥**一对**引号。
        # 本库通行形态是 `> **原句 N:** "“原文…"` —— 外层直引号包裹 + 内层原文弯引号
        # （且引语常在段落中途截断，只剩开引号）。剥一次之后首尾仍各剩一个引号字符，
        # 归一串以 `"` 开头 ⇒ 在原文里查不到 ⇒ 报「引语跨自然段」。
        # 处置：**剥掉首尾所有引号字符**（而不是成对剥），顺序无关、结果唯一。
        q = q.strip().strip('"“‘”’').strip()
        qn = norm(q)
        # ⚠️ 2026-10-02 修正（Bird of a Thousand Stories 终验实测，10 条假红）：
        # 原实现拿**整串**（含 `…`）去判 `qn not in tn`。但带省略号的引语按定义
        # 就**不是**原文的连续子串——省略号两侧各自才是。
        # ⇒ 判据改为「或」关系：**整串命中** 或 **按 `…` 切开后每段都命中**
        # （跨段拼接由紧随其后的 `pn` 自然段计数判据负责，本项只管「逐字」这一半）。
        # 回归：Bird 10 → 0；真实伪造（伪造引语 / 跨段拼接 / 词替换）仍照报——
        # 投毒验证见该次终验记录。
        if qn not in tn and q_multi and _flat(qn) in _flat(tn):
            # ⚠️ 2026-10-03 修正（Everything Is Poison 修完续行合并后新暴露 21 条）：
            #   本库的多行块有两种包裹形态——① 外层一对引号包住整段多行引语；
            #   ② **每个自然段各自成对**：`> "第一段"` / `>` / `> "第二段"`。
            #   形态②并入后会在段界多出一个**写作者加的** `"`，而 `norm()` 不剥引号
            #   ⇒ `qn not in tn`，报「引语跨自然段（拼接红线）」——可这段在原文里
            #   就是**相邻自然段连续**存在的，verify_quotes 与 sweep_full 都判它逐字命中。
            #   这是 ⑱ 与同批门禁的**口径不一致**，不是内容缺陷（假红型）。
            #   兜底只在 `q_multi` 时启用：单行块的行为**一字不变**（其余书零回归）；
            #   判据放宽的是「相邻自然段可以同块」，**不是**「可以乱拼」——
            #   `_flat` 剥掉全部标点与空白，跨**非相邻**段拼接与凭空造句在 flat 下同样查无，
            #   负控见本次修正记录。
            pass
        elif qn not in tn:
            _parts = [x for x in re.split(r"\s*…\s*", q) if x.strip()]
            _same_para = bool(_parts) and any(
                all(norm(x) in p for x in _parts) for p in pn)
            if _same_para:
                # 同段内含全部省略号片段 ⇒ 合法单段引语，不是拼接，放行
                pass
            elif len(qn) < SHORT_Q:
                # 极短引语结构上不可能是两段拼接 ⇒ 判据不适用，降级为提示
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
        # ⚠️ 2026-10-04：关键词行取三形态之一（加粗外置 / 加粗内置 / **裸**），
        # 优先取加粗形态、没有再取裸形态——两处计数与取词必须用**同一套**形态表，
        # 否则又是一次「计数与取值口径不一致」。
        _mk = KW_RE.search(block)
        if _mk is None:
            _mk = KW_RE_BOLD_OUT.search(block)
        if _mk is None:
            _mk = KW_RE_PLAIN.search(block)
        kws = _split_kw(_mk.group(1)) if _mk else []
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
        _qflat = _flat(qn)
        miss = [k for k in kws
                if not _kw_in_quote(k, _qflat)
                and not _kw_in_quote(_BRACKET.sub("", k), _qflat)]
        if miss:
            blocked = [k for k in miss if not _echoed(k, block)]
            echoed = [k for k in miss if _echoed(k, block)]
            if blocked:
                out.append(f"{md.name} 原句{num}: 关键词不在本块引语内 → {blocked}")
            if echoed:
                out.append(f"{md.name} 原句{num}: ⚠️ 提示·语境延伸词"
                           f"（第 9 条 b 允许：已被「为什么这样写」呼应）→ {echoed}")
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
    # ⚠️ 2026-10-05 修正：**退出码原先只看 `bad` 非空**，而 `bad` 同时装着 ❌ 与 ⚠️
    #   ⇒ 一条提示型也会让本脚本 exit=1（三档里提示型「只记不改」，不该阻塞）。
    #   与上一条「提示型不得打 ❌ 前缀」是同一条纪律的两半：前缀对了，退出码也得对。
    blocked = [b for b in bad if "⚠️ 提示" not in b]
    hinted = [b for b in bad if "⚠️ 提示" in b]
    for b in blocked:
        print("  ❌ " + b)
    for b in hinted:
        print("  ⚠️ " + b.split("⚠️ 提示", 1)[1].join(["提示", ""]).lstrip("·"))
    print(f"=== 引语块覆盖度：{len(mds)} 个 md，"
          f"阻断型 {len(blocked)} 处 ／ 提示型 {len(hinted)} 处 ===")
    return 1 if blocked else 0


if __name__ == "__main__":
    sys.exit(main())
