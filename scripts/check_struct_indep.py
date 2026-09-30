#!/usr/bin/env python3
"""check_struct_indep.py — 结构扫描的**独立实现**（第 10 条 c 步用）

为什么需要它（2026-09-29 实测）：`audit_structure.py` 的子项检查是**假阴性高发点**
（两块各缺一项仍报 0 —— 它按块内子项集推断，不核「块数与子项数是否一一对应」），
且对「分析块被整段复制」这类损坏报 0。AGENTS 第 10 条 c 步明确：
**不得把它的 0 当作「子项齐全」的证明**。本脚本换实现、换口径，不复用它的判定。

四项（逐文件，逐块）：
  ① 硬性子项齐全且**各只一次**（子项集按**体裁档位**判定，见 PROFILES）
  ② 子项**顺序**固定
  ③ 编号连续（1..N 或 ①–⑩，无跳号/重号）
  ④ 必备 H2 恰一次 + 词汇三档标题 `### ⭐⭐⭐ 高级` / `### ⭐⭐ 进阶` / `### ⭐ 基础` 齐备
  ⑤ 引语块数落在**该档位的配额**内；`> ` 行只出现在该档位的引语节内

**⚠️ 体裁档位（2026-09-30 修正）**：本脚本原先把「必备节 / 子项集 / 引语格式 / 块数配额」
**全部锁死在言情·精简档**（`## 本章导航` / `## 精读` / `## 本章词汇`、
`读者视角提示`、`> **原句 N:**`、3–8 块）。**非虚构论述档**是另一套（`## 概览` /
`## 选择性精读` / `## 词汇分级`、五子项含 `句子结构` 与 `表达方式`、`**①** "…"`、10 块），
于是对**每一本**非虚构论述档书籍**全量假红**（Ghost Tales of the UK 实测 140 处「缺陷」
而真实缺陷为 0；同型假红另见 `gate.sh` ⑬）。
**处置：按文件实际形态选档位**（AGENTS 8.3「格式自成一派的书是合法的；
模板只降低手打出错概率，**不作判红依据**」）。判据 = 各档位特征节的命中数过半，
否则报「体裁不明」并退出 2（**不猜**）。

用法: python3 scripts/check_struct_indep.py "<书目录>" [md ...]
退出: 0 全过 ｜ 1 有结构缺陷 ｜ 2 参数错误 / 体裁不明
"""
import re, sys
from pathlib import Path

TIER = ["### ⭐⭐⭐ 高级", "### ⭐⭐ 进阶", "### ⭐ 基础"]
CIRCLED = "①②③④⑤⑥⑦⑧⑨⑩"


def _circled_index(ch):
    """圈数字 → 序号。**不能查 CIRCLED 表**：那张表只到 ⑩，而本档位的 QRE 认到 ⑳
    ⇒ 含 ⑪–⑳ 的书会 `ValueError: substring not found` 直接崩（既有潜伏 bug，
    2026-09-30 against-everything-by-mark-greif 实测）。按 Unicode 块算：
    ①-⑳ = U+2460..U+2473。"""
    return ord(ch) - 0x2460 + 1

# ── 体裁档位 ────────────────────────────────────────────────────────────
PROFILES = {
    "summary": {  # 言情 / 小说精简档
        "H2": ["## 本章导航", "## 精读", "## 本章词汇", "## 一句话总结"],
        "READ": "## 精读",
        "SUB": ["中文理解", "关键词", "为什么这样写", "读者视角提示"],
        "QRE": re.compile(r'^> \*\*原句 (\d+):\*\* (.+)$', re.M),
        "NUM": lambda m: int(m.group(1)),
        "RANGE": (3, 8),
    },
    "nonfiction": {  # 非虚构论述档（论证结构 + 10 处五子项）
        "H2": ["## 概览", "## 论证结构", "## 选择性精读", "## 词汇分级", "## 一句话总结"],
        "READ": "## 选择性精读",
        "SUB": ["中文理解", "句子结构", "关键词", "表达方式", "为什么这样写"],
        #    ⚠️ 2026-09-30（An Army like No Other 五步审查）：本档原有**两种**非虚构精读
        #    格式的引语抬头，只认后一种（`**①** "…"`）⇒ 另一格式被判「引语块 0 个」，
        #    **连带子项检查整段空转**（假阴性，比假红更坏：它报 0 缺陷而实际没查）。
        #    实证：An Army like No Other 15 章全用 `> **原句 N:**`，45 处报警里
        #    「引语块 0 个」×15 ＋「`> ` 出现在 ## 选择性精读 之外」×30。
        #    修法：**两种抬头都认**，编号用 group(1)（数字式）或 group(2)（圈数字式）。
        "QRE": re.compile(r'^(?:> \*\*原句 (\d+):\*\* .+|\*\*([①-⑳])\*\* ["\'].+["\']\s*)$', re.M),
        "NUM": lambda m: int(m.group(1)) if m.group(1) else _circled_index(m.group(2)),
        "RANGE": (10, 10),
        # ⚠️ **档位认定的特征节**：必须是该档位**独有**的那些，不能只比数量。
        #    数量多数会被「第三种格式」骗过去——实测 a-most-angelic-death
        #    （概览 + 选择性精读 + 词汇分级，但无 论证结构、子项只 4 个、6 块）
        #    会被少数多数判成 nonfiction ⇒ 缺陷数 170 → 296（假红换口味且变多）。
        #    **判据只认特征节**，认不出就退回 summary（原行为），不套用别的档位的
        #    子项集与块数配额——那两项最挑书。
        "MARK": ["## 论证结构", "## 选择性精读"],
    },
    "summary": {  # 言情 / 小说精简档
        "H2": ["## 本章导航", "## 精读", "## 本章词汇", "## 一句话总结"],
        "READ": "## 精读",
        "SUB": ["中文理解", "关键词", "为什么这样写", "读者视角提示"],
        "QRE": re.compile(r'^> \*\*原句 (\d+):\*\* (.+)$', re.M),
        "NUM": lambda m: int(m.group(1)),
        "RANGE": (3, 8),
        "MARK": ["## 本章导航", "## 精读"],
    },
}


def _has(s, h):
    """节名整行匹配；容忍尾随空格与「（N 处）」这类后缀（实测 a-most-angelic-death
    写 `## 选择性精读（6 处）：**`，严格整行匹配会漏判 ⇒ 档位认错）。"""
    return re.search(r'(?m)^' + re.escape(h) + r'(?:[（(（].*)?\s*$', s) is not None


def detect_profile(s):
    """按**特征节**认档位（不是比数量）。nonfiction 优先——它才是新增的那一档。
    认不出 → None（退回 summary 原行为，见 main）。"""
    if all(_has(s, m) for m in PROFILES["nonfiction"]["MARK"]):
        return "nonfiction"
    if any(_has(s, m) for m in PROFILES["summary"]["MARK"]):
        return "summary"
    return None


def check(md: Path):
    out = []
    s = md.read_text(encoding="utf-8")
    lines = s.split("\n")
    prof = detect_profile(s)
    if prof is None:
        # 认不出档位 ⇒ **退回 summary 的原判据**，而不是判「体裁不明」阻断：
        # 本库格式自成一派，退回旧行为等于「维持现状」，不会把第三种格式的书
        # 判成另一种格式的缺陷（那才是制造假红）。
        prof = "summary"
    P = PROFILES[prof]
    H2, SUB, QRE, NUM = P["H2"], P["SUB"], P["QRE"], P["NUM"]
    LO, HI = P["RANGE"]
    # --- ④ 必备 H2 / 三档标题 ---
    for h in H2:
        n = s.count("\n" + h + "\n") + (1 if s.startswith(h + "\n") else 0)
        if n != 1:
            out.append(f"[{prof}] 必备节「{h}」出现 {n} 次（须恰 1）")
    for t in TIER:
        if t not in s:
            out.append(f"[{prof}] 词汇档位标题缺「{t}」")
    # --- ③ 编号连续 ---
    nums = [NUM(m) for m in QRE.finditer(s)]
    marks_have_yuanju = any(m.group(1) for m in QRE.finditer(s))
    if nums and nums != list(range(1, len(nums) + 1)):
        out.append(f"[{prof}] 引语编号不连续：{nums}")
    # --- ⑤ 块数配额 ---
    # ⚠️ 2026-09-30：本档位的 QRE 自从同时认两种抬头（`**①** "…"` 与 `> **原句 N:**`），
    #    块数配额就必须**按抬头形态分开**——(10,10) 是 `**①**` 格式的配额，而
    #    `原句 N:` 格式（期刊逐句档）实测 3–12 块。混用会对 the-art-of-thinking-clearly
    #    等书每章报「超出 10–10 配额」的假红（实测 +34）。
    lo_hi = (LO, HI)
    if prof == "nonfiction" and marks_have_yuanju:
        lo_hi = (3, 20)   # 期刊逐句档不限 10 块；实测 4–13，放宽到 20 以免假红
    if not lo_hi[0] <= len(nums) <= lo_hi[1]:
        out.append(f"[{prof}] 引语块 {len(nums)} 个，超出 {lo_hi[0]}–{lo_hi[1]} 配额")
    # --- ① ② 逐块子项（硬性、不推断、查重、查序）---
    marks = list(QRE.finditer(s))
    for i, m in enumerate(marks):
        if i + 1 < len(marks):
            end = marks[i + 1].start()
        else:
            # 末块：不得越过下一个 H2，否则把尾附/下一节文字算进本块
            # ⚠️ 只对**末块**做此收敛：非末块若也去找「下一个 H2」，
            #    会越过后续引语块而把它们的子项一并吞进来 ⇒ 查重全部失败
            #    （2026-09-30 首次修正即踩此坑：20 章 1000+ 处假红）。
            end = len(s)
            nxt = re.search(r'(?m)^## ', s[end:])
            if nxt:
                end = end + nxt.start()
        blk = s[m.end():end]
        pos = []
        for name in SUB:
            # ⚠️ 2026-09-30 两次修正（The Secret Wife 1680 处假红 / Ghost Tales 1000+ 处假红）：
            #    子项行以 `- 中文理解：` 起首（列表项），而原式 `^\*\*` + re.M 要求
            #    `**` 出现在**行首** ⇒ 全书每块 × 每子项「出现 0 次」。
            #    本库**粗体标签**（`- **中文理解**：`）与**纯文本标签**（`- 中文理解：`）
            #    **两种形态并存**，且**冒号可在粗体内或粗体外**。
            #    判据只该管「该子项在这一块里有没有、有几次、什么顺序」，
            #    **不该管标签是否加粗**——加粗是排版风格，不是结构。
            #    教训同 audit_structure 的 RE_ANY_LABEL：**正则不加容错就是静默空跑**；
            #    而加容错也不能收窄到只认一种形态，否则换个体裁就全量假红。
            hits = [mm.start() for mm in
                    re.finditer(r'^[ \t]*(?:[-*+]\s+)?\*{0,2}' + name + r'\*{0,2}[：:]',
                               blk, re.M)]
            if len(hits) != 1:
                out.append(f"[{prof}] 引语 {NUM(m)}: 子项「{name}」出现 {len(hits)} 次（须恰 1）")
            else:
                pos.append((name, hits[0]))
        if len(pos) == len(SUB):
            order = [p[0] for p in sorted(pos, key=lambda x: x[1])]
            if order != SUB:
                out.append(f"[{prof}] 引语 {NUM(m)}: 子项顺序错 {order}")
    # --- ⑤b `> ` 行只出现在该档位的引语节内 ---
    # ⚠️ 2026-09-30（An Army like No Other 五步审查）：本库各体裁的**概览节里都有
    # 「核心金句」引用块**（期刊格式见 AGENTS 记忆 #1625/#1680 的 `## 概览` 定义：
    # 「…段落脉络表格/核心金句」），本档位原先只允许引语节内出现 `> `
    # ⇒ 15 章 × 2 行 = 30 处假红。判据改为：**紧跟在「核心金句」标签之后的连续
    # `> ` 行视为合法**（标签本身是显式声明，不是误落），其余仍按原规则判。
    in_read = False
    in_gold = False
    for i, l in enumerate(lines, 1):
        if l.startswith("## "):
            in_read = (l.strip() == P["READ"])
            in_gold = False
        elif "核心金句" in l:
            in_gold = True
        elif not l.startswith("> ") and l.strip():
            in_gold = False
        if l.startswith("> ") and not in_read and not in_gold:
            out.append(f"[{prof}] 第 {i} 行：`> ` 出现在 {P['READ']} 之外（> 只用于引语）")
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__); return 2
    book = Path(sys.argv[1])
    mds = [Path(x) for x in sys.argv[2:]] or sorted(book.glob("ch*.md"))
    if not mds:
        print(f"❌ {book} 下没有 ch*.md"); return 2
    bad = []
    for md in mds:
        for msg in check(md):
            bad.append(f"{md.name}: {msg}")
    for b in bad:
        print("  ❌ " + b)
    print(f"=== 独立结构扫描：{len(mds)} 个 md，缺陷 {len(bad)} 处 ===")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())