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
`## 选择性精读` / `## 词汇分级`、五子项含 `句子结构` 与 `表达方式`、`**①** "…"`），
于是对**每一本**非虚构论述档书籍**全量假红**（Ghost Tales of the UK 实测 140 处「缺陷」
而真实缺陷为 0；同型假红另见 `gate.sh` ⑬）。
**块数这一维在模板里并无规定**（2026-10-07 追记：`docs/新书启动模板.md` 对非虚构档只规定
「五子项 + 论证结构」，`docs/期刊精读模板.md` 的「五子项 10 处」只管期刊/短篇档），
所以下方 ⑤ 对该档位取**本书自己的众数**做参照，硬界 `(10,10)` 属工具自设、已撤。
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
    # ⚠️ 2026-10-02（The Best Short Stories 2026 五步审查）新增第三档：**短篇合集档**。
    # 症状：无此档时本类书回退 summary ⇒ summary 的 QRE 只认 `> **原句 N:**`，
    # 而本类用裸圈码 `① "…"` ⇒ **引语块恒为 0**，且 0 落在 3–8 之外
    # ⇒ 20 章全量报「引语块 0 个，超出 3–8 配额」**假红**，连带子项检查整段空转
    # （假阴性比假红更坏：它报 0 缺陷而实际没查）。
    # 与 nonfiction 同型：2026-09-30（An Army）已给 nonfiction 补了「两种抬头都认」，
    # 本档同样需要**认自己的抬头 + 用自己的块数配额**（本库体裁对应格式表：
    # 短篇合集＝逐篇精读 **10 处** 五子项，与长篇精简档的 3–8 处不是一回事）。
    # 特征节取本档**独有**的 `## 精读结束总结` + `## 可迁移表达`，两者皆须命中，
    # 避免与只写 `## 导航/## 精读/## 词汇/## 一句话总结` 的长篇小说精简档抢档。
    "anthology": {
        "H2": ["## 本章导航", "## 精读", "## 本章词汇", "## 精读结束总结", "## 可迁移表达", "## 一句话总结"],
        "READ": "## 精读",
        "SUB": ["中文理解", "句子结构", "关键词", "表达方式", "为什么这样写"],
        #    裸圈码 `① "…"`（同系列 2024 册与本书一致）；`>` 前缀形态不属本档。
        "QRE": re.compile(r'^([①-⑳])\s+"(.+)"\s*$', re.M),
        "NUM": lambda m: _circled_index(m.group(1)),
        "RANGE": (10, 10),
        "MARK": ["## 精读结束总结", "## 可迁移表达"],
    },
    # ⚠️ 2026-10-06（The Language of Knives 五步审查）新增第四档：**短篇合集档变体 B**。
    # 症状：体裁对应格式表对「短篇合集」只规定「逐篇精读（10 处 + 五子项 + 三档词汇 +
    # 一句话总结）」，**并未规定节名**；现有 anthology 档把「独有特征节」取成
    # `## 精读结束总结` + `## 可迁移表达`（Ken Liu 那套的节名）。
    # 本书 13 章用的是另一组合规节名：`## 本篇导航` + `## 精读` + `## 词汇分级` +
    # `## 一句话总结`，引语抬头是 `> **原句 N:**`。
    # ⇒ 两个档位特征节都不命中 ⇒ 回退 summary ⇒ **39 处全量假红**
    #   （13×「必备节本章导航 0 次」+ 13×「本章词汇 0 次」+ 13×「引语块 10 个超出 3–8 配额」）。
    # 修法不是改 md 去凑节名（体裁表没要求那些节名），而是**再加一档**。
    # 认档特征：`## 本篇导航` + `## 词汇分级`（这一组是短篇合集档 B 的独有节名组合）。
    "anthology2": {
        "H2": ["## 本篇导航", "## 精读", "## 词汇分级", "## 一句话总结"],
        "READ": "## 精读",
        "SUB": ["中文理解", "句子结构", "关键词", "表达方式", "为什么这样写"],
        "QRE": re.compile(r'^> \*\*原句 (\d+):\*\* (.+)$', re.M),
        "NUM": lambda m: int(m.group(1)),
        "RANGE": (10, 10),
        "MARK": ["## 本篇导航", "## 词汇分级"],
    },
}


def _has(s, h):
    """节名整行匹配；容忍尾随空格与「（N 处）」这类后缀（实测 a-most-angelic-death
    写 `## 选择性精读（6 处）：**`，严格整行匹配会漏判 ⇒ 档位认错）。"""
    return re.search(r'(?m)^' + re.escape(h) + r'(?:[（(（].*)?\s*$', s) is not None


def detect_profile(s):
    """按**特征节**认档位（不是比数量）。nonfiction → anthology → summary 依次判定。
    认不出 → None（退回 summary 原行为，见 main）。

    ⚠️ 顺序不可随意调：anthology 的特征节比 summary **更严**（两个独有节都要命中），
    但仍排在 summary 之前——若 summary 先判，`## 本章导航`+`## 精读` 会把短篇合集抢进
    3–8 配额档，重新制造 2026-10-02 修掉的那条假红。

    ⚠️ **2026-10-02 加负控（只约束新档位）**：特征节命中**不等于**该档位的引语抬头能被
    认出来。实测 the-passing-of-the-dragon-by-ken-liu 是**格式混杂的遗留书**（13 章里
    12 章用 `## 本篇导航` + `> **原句 N:**`，仅 1–2 章带 anthology 的两个特征节），
    按特征节认档会把它那 1–2 章判成 anthology，而它们用 `原句 N:` 抬头 ⇒
    **QRE 抽到 0 块 ⇒ 缺陷数 56 静默降到 54**。那个方向比假红更坏：**不是多报，是少查**。
    ⇒ anthology 必须**由「能解析它」自证**：QRE 认不出块就换下一档。

    ⚠️⚠️ **守卫只对 `anthology` 生效，绝不碰 nonfiction**（这是第一版写错的地方）：
    我一度对两个档案都加 QRE 守卫，结果 what-the-bees-see / why-we-read 两本**非虚构论述书**
    从 nonfiction 掉成 None —— 因为 nonfiction 的 QRE 只认粗体 `**①** "…"`，
    而那两本用**裸** `① "…"`，于是被守卫一票否决、缺陷数 70→118 / 50→173 乱跳。
    **nonfiction 一直是「按特征节认、不要求 QRE 自证」**，那是它的既定契约（也是 2026-09-30
    An Army 那次只给它补 QRE、不动认档逻辑的原因）。**修工具只改必要的那一处。**
    """
    for name in ("nonfiction", "anthology", "anthology2", "summary"):
        P = PROFILES[name]
        marks = P.get("MARK")
        ok_marks = all(_has(s, m) for m in marks) if name != "summary" \
            else any(_has(s, m) for m in marks)
        if not ok_marks:
            continue
        if name in ("anthology", "anthology2") and not P["QRE"].search(s):
            continue          # 负控只约束新增档位
        return name
    return None


SUB_LABEL_RE = lambda name: re.compile(
    r'^[ \t]*(?:[-*+]\s+)?\*{0,2}' + name + r'\*{0,2}[：:]', re.M)


def calibrate_sub(mds, prof):
    """按**本书实际**校准子项集，不套外部模板的子项名。

    ⚠️ 2026-10-02（The Alchemist 五步审查）：summary 档原把
    `读者视角提示` 硬编码为必备子项，而本库小说精简档实为
    `中文理解 / 句子结构 / 关键词 / 为什么这样写`（**无**读者视角提示），
    于是 4 章 × 8 块 = **38 处假红**（每块各报「读者视角提示 出现 0 次」）。
    `audit_structure` 本就「按书内主流子项集自校准，不套外部模板」，
    本脚本却套模板 ⇒ 两把尺子口径打架，且打架方向是**制造假红**。

    判据：候选子项 = 档案 SUB ∪ 常见标签；某子项在 **≥60% 的块**里出现
    才算本书必备。**算不出（不足 2 个）就回退档案 SUB**——
    宁可维持旧行为，也不要用一个猜出来的集合把真缺陷判成「齐」。
    """
    P = PROFILES.get(prof) or PROFILES["summary"]
    cand = list(dict.fromkeys(
        P["SUB"] + ["中文理解", "句子结构", "关键词", "表达方式", "为什么这样写"]))
    qre, total, hit = P["QRE"], 0, {c: 0 for c in cand}
    pos_in_blk = {}
    for md in mds:
        try:
            s = md.read_text(encoding="utf-8")
        except OSError:
            continue
        marks = list(qre.finditer(s))
        for i, m in enumerate(marks):
            end = marks[i + 1].start() if i + 1 < len(marks) else len(s)
            if i + 1 == len(marks):
                nxt = re.search(r'(?m)^## ', s[end:])
                if nxt:
                    end = end + nxt.start()
            blk = s[m.end():end]
            total += 1
            for c in cand:
                mm2 = SUB_LABEL_RE(c).search(blk)
                if mm2:
                    hit[c] += 1
                    pos_in_blk.setdefault(c, []).append(mm2.start())
    if not total:
        return None
    keep = [c for c in cand if hit[c] >= 0.6 * total]
    if len(keep) < 2:
        return None
    # ⚠️ 顺序必须取**块内实际出现顺序**，不能沿用候选表顺序：候选表是
    # `档案 SUB + 常见标签`，与书里的书写次序无关。The Alchemist 实为
    # `中文理解→句子结构→关键词→为什么这样写`，而候选表把它排成
    # `中文理解→关键词→为什么这样写→句子结构` ⇒ 38 处「子项顺序错」假红。
    # 判据：按「各子项首次出现位置的中位数」排序，即书里实际的书写次序。
    def med(v):
        v = sorted(v)
        return v[len(v) // 2]
    return sorted(keep, key=lambda c: med(pos_in_blk.get(c, [10**9])))


S_ANTH_SHORT_SRC = 20000


def _short_piece(md: Path, book_dir: Path) -> bool:
    """短篇合集档：**源文本归一后短于 S_ANTH_SHORT_SRC 时下限不适用**。

    判据与第一实现 `check_block_keywords.py:ANTH_SHORT_SRC` 逐字一致，属**结构性**
    判据（不点名某书某篇）：合集里的引言/后记类篇目篇幅只有正篇的零头，凑满 10 块
    必然违反「一条引语只取一个自然段」的硬禁令。上限不受影响。
    """
    m = re.match(r"ch(\d+)", md.name)
    if not m:
        return False
    pat = f"ch{int(m.group(1)):02d}"
    cands = sorted(book_dir.glob(f"text/{pat}*"))
    if not cands:
        return False
    t = re.sub(r"\s+", "", cands[0].read_text(encoding="utf-8"))
    return len(t) < S_ANTH_SHORT_SRC


_NF_MODE_CACHE = {}


def _nf_mode(book_dir: Path, qre):
    """本书**非虚构章**（`**①** "…"` 形态）块数的众数；无合格样本返回 None。

    为什么取众数而不是写死 10：模板对非虚构档只规定「五子项 + 论证结构」，
    **没有规定块数**（见 `check()` 里 ⑤ 的 2026-10-07 注）。块数的合理参照只能是
    **这本书自己的其余各章**——与第一实现 `audit_structure.py` 同一口径。
    排除「原句 N:」形态的章：那些走期刊逐句档配额，不与本档比。
    ⚠️ **必须缓存**：本函数每次读全书 ch*.md，而 `check()` 逐章调用——
    365 章的书不缓存就是 365×365 ≈ 13 万次读取，门禁会被自己拖死。
    """
    key = (str(book_dir), id(qre))
    if key in _NF_MODE_CACHE:
        return _NF_MODE_CACHE[key]
    cnts = []
    for m in sorted(book_dir.glob("ch*.md")):
        try:
            s = m.read_text(encoding="utf-8")
        except OSError:
            continue
        if detect_profile(s) != "nonfiction" or "原句" in s:
            continue
        cnts.append(len(qre.findall(s)))
    mode = None if not cnts else max(set(cnts), key=lambda c: (cnts.count(c), c))
    _NF_MODE_CACHE[key] = mode
    return mode


def check(md: Path, sub_override=None, book_dir: Path = None):
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
    if sub_override:            # 见 calibrate_sub()：按本书实际子项集，不套模板
        SUB = sub_override
    LO, HI = P["RANGE"]
    # --- ④ 必备 H2 / 三档标题 ---
    for h in H2:
        n = s.count("\n" + h + "\n") + (1 if s.startswith(h + "\n") else 0)
        if n != 1:
            out.append(f"[{prof}] 必备节「{h}」出现 {n} 次（须恰 1）")
    # ⚠️ 2026-10-03 口径订正：本项原先判「三档标题必须齐备」，与写作规则
    #    「空档**留空**、不插占位行」直接冲突（AGENTS 8.3 / build_vocab_section.py
    #    只写非空档；`check_vocab` 反而把 `（本章无X词）` 判 FAIL）。
    #    真缺陷是**空档位表头**（有标题、档内无词条）——本书 7 篇韵文当初被人工
    #    整改掉的正是这个，不是「缺标题」。⇒ 判据改为反方向：标题**至多一次**且
    #    **出现即须有词条**；短章只有一档合法。
    # ⚠️ 同日二次修正：词条有两种排版——**表格**（`| 词 | 释义 | 例句 |`）与
    #    **列表**（`- **word** …`，the-dream-hotel 全书法）。只认表格行会让该书的
    #    每一档都报「空表头」（实测 +21 条假红）——与「新判据只适配多数派排版」
    #    这条老坑同形，两种排版都要认。
    def vocab_rows(start):
        for ln in lines[start + 1:]:
            if ln.startswith("## ") or ln.startswith("### "):
                break
            if re.match(r"^[-*+]\s+\*\*", ln):
                return True
            if ln.startswith("|") and not re.match(r"^\|[\s:-]+\|", ln) \
                    and "词/短语" not in ln and "词汇" not in ln:
                return True
        return False

    for t in TIER:
        hits = [i for i, ln in enumerate(lines) if ln.strip().startswith(t)]
        if len(hits) > 1:
            # ⚠️ 同为提示型：全库实测 39 处，抽样核看是「同档拆两段写」的合法排版
            #    （all-the-lies / the-last-thing / book-of-heartbreak 均如此），
            #    不构成阻断型。
            out.append(f"⚠ [{prof}] 词汇档位标题「{t}」出现 {len(hits)} 次")
            continue
        if not hits:
            continue
        if not vocab_rows(hits[0]):
            # ⚠️ 2026-10-03 全库实测：这一项在 380 本里报出 **348 处**（书级整本成片，
            #    如 phone-box 58 / teacher 50）。这个量级说明它是「新判据撞上多数派
            #    既有排版」的老坑形态——空表头是否算缺陷**未在全库裁决过**，
            #    不能由一次审查顺手升为硬缺陷。⇒ 先作 ⚠️ 提示型只记不改，
            #    不进 `缺陷` 计数、不影响退出码；要升级为阻断型须先做全库裁决。
            out.append(f"⚠ [{prof}] 词汇档位「{t}」为空表头（该档无词条）")
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
    elif prof == "nonfiction":
        # ⚠️ 2026-10-07（Life in Three Dimensions 五步审查 c 步实测）：模板:147 的
        # 「10 处」是**期刊/短篇合集**档的配额，非虚构档模板只规定「五子项 + 论证结构」，
        # **从未规定块数**。`(10,10)` 因此是本工具按某几本书的写作习惯**自造的硬界**：
        # 本书 ch15（9 块）/ch16（4 块）各报一条 ❌，而 ch16 的源文本只有 2 个够长自然段，
        # 凑满 10 块必然违反「一条引语只取一个自然段」的硬禁令（禁令 5）。
        # 第一实现 `audit_structure.py` 用的是**本书众数**比对且只给 ⚠️，两实现口径不一致。
        # 改法：块数与**本书非虚构章的众数**比，偏离 ⇒ ⚠️ 提示型（只记不改，不进缺陷数、
        # 不影响退出码）；**0 块仍是阻断型**——那才是真的结构断裂，与本豁免无关。
        mode = _nf_mode(book_dir, QRE) if book_dir is not None else None
        # lo_hi 置为恒真区间：本分支已自行判完，避免与下方通用配额**重复报同一条**
        # （第一版就漏了这一步，9 块的书会同时收到 ⚠️ 与 ❌）。
        lo_hi = (0, 10 ** 9)
        if not nums:
            out.append(f"[{prof}] 引语块 0 个（该档必须有精读块）")
        elif mode is not None:
            # ⚠️ 上限**必须先判**：若把 `len(nums) != mode` 放在前面，12 块的书会走进
            # 「偏离众数」分支而**永不触发**上限判据——第一版就是这样写成了死代码
            # （AGENTS 第 10 条「自写检查器第一版是死代码」同型坑）。
            if len(nums) > HI:
                out.append(f"[{prof}] 引语块 {len(nums)} 个，超出上限 {HI}")
            elif len(nums) != mode:
                out.append(f"⚠ [{prof}] 引语块 {len(nums)} 个，与本书非虚构章众数 {mode} 不符")
        elif not LO <= len(nums) <= HI:
            out.append(f"[{prof}] 引语块 {len(nums)} 个，超出 {LO}–{HI} 配额")
    if prof == "anthology" and book_dir is not None and _short_piece(md, book_dir):
        # ⚠️ 2026-10-04（Fold Catastrophes 五步审查 c 步实测）：第一实现
        #    `check_block_keywords.py` 早已有「短篇合集短篇目」豁免（ANTH_SHORT_SRC
        #    ＝20000，判据同为**结构性**：源文本归一后短于此则下限不适用、上限照旧），
        #    本第二实现**漏搬**该豁免 ⇒ 本书 ch01 引言（源文本 5806 字符 / 6 块）被报
        #    「超出 10–10 配额」，实测 1 处假红。两实现口径必须一致，此处补齐——
        #    只放下限，**上限照旧**（注水的 12 块仍要报）。
        lo_hi = (0, HI)
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
    bad, warn = [], []
    cal = {p: calibrate_sub(mds, p) for p in ("summary", "nonfiction")}
    for md in mds:
        for msg in check(md, cal.get(detect_profile(
                md.read_text(encoding="utf-8")) or "summary"), book_dir=book):
            (warn if msg.startswith("⚠") else bad).append(f"{md.name}: {msg}")
    for b in bad:
        print("  ❌ " + b)
    for w in warn:
        print("  ⚠️ " + w)
    print(f"=== 独立结构扫描：{len(mds)} 个 md，缺陷 {len(bad)} 处"
          f"（另有提示型 {len(warn)} 条，不计入缺陷、不影响退出码）===")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())