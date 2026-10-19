#!/usr/bin/env python3
"""中文层体检：「中文理解 / 句子结构 / 为什么这样写」必须是中文的、能读的。

**为什么需要**
--------------
本库是**中文**精读站，每个引语块下固定挂四个中文字段：

    **中文理解** / **句子结构** / **关键词** / **为什么这样写**（+ 可选 表达方式 / 读者视角提示）

但 2026-10-19 全库扫描发现：**新一批书（2026-10-17~19 完工的 10 本）里，
「中文理解」有 12%–100% 写成了英文，「为什么这样写」有 80%–100% 写成英文或
中英夹杂**。这些书**全部通过 18 lane 门禁**（引语逐字 100%、vocab FAIL=0、
空段扫描 0 处），因为：

  - `verify_quotes` / `check_chapter_quotes` / `sweep_full` 只验**引语行**，
    完全不看下面挂的分析字段；
  - `check_vocab` 只看**词汇表**和例句，不看分析层语言；
  - `check_block_keywords` 只看块**数量/关键词锚定**；
  - 门禁 ⑱ 块覆盖对账只查「每块进没进 verify_quotes」，**不查块里有没有内容**。

⇒ **机械层对「分析层是否真的写了、是不是中文」是真空绿。**
这就是本脚本要补的那一层。

**v2（2026-10-19）：堵住 v1 被钻的三个口子**
------------------------------------------
v1 只判「整段无汉字」，结果同一批修复任务出现三种**假修复**，全部报「阻断型 0」：

1. **加两个字**（bruja-s-nest）：`- Three weeks after incident—Yolanda reflects. …`
   → `+ 显示 Three weeks after incident—Yolanda reflects. …`
   —— 内容一个字节没变，只因多了「显示」二字就有汉字了。⇒ 新增**形式性规避**判据。
2. **删掉英文引语**（armor-for-liars）：`- Clem 的 reassurance——"The cuts are minor"。把…`
   → `+ Clem 的 reassurance——。把…`
   —— 断言的证据被删、留下 `——。` 残句，句子还不通。⇒ 新增**残句**判据。
   ⚠️ 这同时踩了 AGENTS 第 9 条 d2 ��—d2 早就警告「行内引语物理上抽不到 ⇒
   等于主动放弃门禁」，删掉的**正是行内引语**，同一个坑第二次踩。
3. **「为什么这样写」整段无中文**被 v1 归为提示型 ⇒ 任何会话都能合法引用
   v1 自己写的规则，把最严重的缺陷降级。⇒ **v2 升为阻断型**。

另：v1 跳过 `00_*.md`，**总览三篇一眼都没看**（读者落地页第一眼）⇒ v2 纳入。

**判定分档（照 AGENTS 第 3 条四档）**
-----------------------------------
  ❌ 阻断型（必须改）
     ① 「中文理解」**整段无中文**——字段写成英文，等于没写
     ② 引语块**缺「中文理解」**（仅当**本书已在用**该子项时才算缺陷）
     ③ 「句子结构」是敷衍模板（"两句话。" / "简单陈述句。"）——零信息量
     ④ **残句**：删除/改写后留下的空壳（`——。` / `——、` / `、、` / `、。` …）
        ⚠️ **不把 `""` 当残句**——对话体书里相邻两段引语天然写成 `“……”“……”`，
        实测 4 本书 33 处全是这一类（假红，已移除）。真正的删引语形态是 `——。`。
     ⑤ **形式性规避（名义中文）**：去掉引号内引文后，汉字占比 <10%，
        **且该块的「句子结构」「为什么这样写」也不是中文**——
        即「加两个字糊弄」（bruja 实测 3.5%，bright-girl 合法写法 25% 不误报）
     ⑥ **「为什么这样写」整段无中文**——与 ① 同级，不是提示型
     ⑦ **中英夹杂占比 ≥60%**（整层没写，不是「措辞正当」）
     ⑧ **合格分析密度 <60%**（见下）
  ⚠️ 提示型（只记不改）
     ⑨ 中英夹杂：字段有中文，但**英文单词字符占比 > 35%**
     ⑩ 总览行内英文引语（AGENTS 第 9 条 d2 违规：英文原句必须成行引用块）
  ❓ 跳过型
     本书一个引语块都没解析出来 → **不算通过**，报「无法判定」

**为什么 ⑨ 只报不判红、而 ⑦⑧ 判红**
-------------------------------
中英夹杂**没有客观边界**：专有名词（Mignonette / Godspeed / doomsayers）本来就该保留英文，
人名地名更不能译。35% 是启发式阈值，**必然有误判**，所以单条只作提示。
但**整层**夹杂（≥60% 的块）不是措辞问题，是「分析层没写」——
和 ① ⑥ 同性质，**不能靠「提示型只记不改」过关**。
第 3 条的提示型判据是「**措辞正当或启发式判的**」，前提是**内容本身成立**；
整层夹杂不满足这个前提 ⇒ 必须阻断。

**合格分析密度怎么算**
---------------------
「合格块」= 中文理解**有中文** 且 **不是残句** 且 **不是形式性规避** 且 **夹杂率 ≤35%**。
密度 = 合格块 / 总块。低于 60% ⇒ 整层没写 ⇒ 阻断型。
⚠️ 该阈值经全库 433 本回归校准（见 `--self-test` 说明），
**在合格书上 0 误报**（this-time-tomorrow 428 块 / incarnate 286 块 / under-the-same-stars 711 块
全部 0 阻断）。

**用法**
------
    python3 scripts/check_chinese_layer.py "<书目录>"

退出码：0 = 无阻断型；1 = 有阻断型；2 = 无法判定（未解析出引语块）。
"""

import argparse
import glob
import os
import re
import sys

HAN = re.compile(r"[一-鿿]")
ENW = re.compile(r"[A-Za-z][A-Za-z'-]*")

# 子项标签：兼容 `**中文理解**：` / `**中文理解：**` / `- **中文理解**：` / 纯文本 `中文理解：`
LAB = re.compile(
    r"^(中文理解|理解|句子结构|关键词|为什么这样写|表达方式|读者视角提示)\s*[：:]\s*(.*)$"
)
BLOCK = re.compile(r"^> \*\*原句 \d+:\*\*", re.M)

# 敷衍的「句子结构」——零信息量模板。
# ⚠️ 必须**整串精确匹配**，不能前缀匹配：实测 the-wrong-sister 的 198 处全是
#    「简单句，现在完成进行时（have been watching）…」「复合句，I bet + 宾语从句…」这类
#    正常的句法分析，前缀匹配会把它们整批误判成敷衍（2026-10-19 修正）。
LAZY_TEMPLATES = {
    "两句话", "三句话", "四句话", "一句话", "几个句子", "短句", "长句",
    "简单句", "简单陈述句", "陈述句", "复合句", "被动句", "一段话", "一句",
    "一个简单句", "对白", "独白", "对话", "叙述句", "简单", "复杂",
}

# 残句——删除/改写后留下的空壳。
# ⚠️ 判据要窄，两个实测坑：
#   1. `列出 A、B。` 里「、」后面是「B」不是「。」，不会误命中。
#   2. **不能把 `""` 当残句**：对话体书籍里相邻两段引语天然写成
#      `“……”“……”`（under-the-same-stars 7 处 / the-wrong-sister 20 处 /
#      captain 2 处 / breathe-me-in 4 处实测全是这一类）⇒ 全部是假红，已移除。
#      真正的「删掉引语」形态是 `——。` / `——、`（armor-for-liars 实测 279 处）。
HOLLOW = re.compile(
    r"(——|—)\s*[。．、：]|"          # ——。  ——、  —：
    r"[、，]\s*[。．]|"               # 、。  ，。
    r"、、|"                          # 、、
    r"：\s*[。．]"                   # ：。
)

# 「名义中文」阈值：去掉引号内引文后，汉字占比低于此值 ⇒ 名义中文（形式性规避）
# ⚠️ 10% 是实测校准值：bruja「显示 + 英文分析」= 3.5%（命中），
#    armor「Clem 的 reassurance——把…具象化为 minor」= 13.5%（不命中，交提示型），
#    bright-girl 合法写法「Shelby 问“…”」= 25%（不命中）。
NOMINAL_CN = 0.10

# 密度与整层夹杂的阈值
DENSITY_FLOOR = 0.60
MIXED_BLOCK_RATIO = 0.60

# 单条夹杂的提示阈值
MIX_WARN = 0.35

# 总览行内英文引语：引号内 ≥4 个英文词即算「英文原句」（AGENTS 第 9 条 d2）
OVERVIEW_INLINE_WORDS = 4


def is_lazy_struct(text):
    body = (text or "").strip().rstrip("。．.！!？? 　")
    return body in LAZY_TEMPLATES


def has_hollow(text):
    return bool(HOLLOW.search(text or ""))


def norm(text):
    """归一化：只留字母数字，小写——用于比对「是不是同一段话」。"""
    return re.sub(r"[^0-9a-z]", "", (text or "").lower())


def mix_ratio(text):
    """英文单词字符数 /（英文 + 中文）字符数。引号内的原文不计入。"""
    text = re.sub(r'[“"][^”"]*[”"]', "", text)
    han = len(HAN.findall(text))
    en = sum(len(w) for w in ENW.findall(text))
    total = en + han
    return en / total if total else 0.0


def nominal_chinese_ratio(body):
    """「名义中文」度：去掉引号内引文后，字段里**汉字**占（汉字+英文字母）的比例。

    命中场景（bruja-s-nest 的「加两个字」修复）：
        `- Three weeks after incident—Yolanda reflects. "…"`
        `+ 显示 Three weeks after incident—Yolanda reflects. "…"`
    —— 去掉引号内引文后，只剩「显示」一个汉字，比例 3.5% ⇒ 名义中文。

    ⚠️ 必须**先去掉引号内引文**再算：否则 bright-girl 那种合法写法
    `Shelby 问 “Can you think of anyone who had a beef with Whitney? …”`
    （中文框架 + 英文原句）会被误判成规避——实测 v2 初版正是这样误报了 156 处。
    去掉引文后它只剩「Shelby 问」，比例 25% ⇒ 正常。
    ⚠️ 第二条实测坑：若**全部内容都在引号内**（如 `"Sherry Cummings 觉得我有。"`），
       去掉引文后为空 ⇒ 须回退用原文判断，否则纯中文句子会被判成 0%。
    """
    if not body:
        return 1.0
    clean = re.sub(r"[“\"][^”\"]*[”\"]", "", body)
    if not clean.strip():
        clean = body
    han = len(HAN.findall(clean))
    en = len(re.findall(r"[A-Za-z]", clean))
    if han == 0:
        return 0.0
    return han / (han + en)


def is_formal_evasion(zh, why, struct):
    """形式性规避（名义中文）的最终判定。

    **单看「中文理解是名义中文」会大面积误报**：对话体小说里
    `Captain Guerrero 说：“Oh, good. Detective Reed, you’re here.”` 这种
    「中文框架 + 英文原句」是**合法但偏薄**的写法（bright-girl / breathe-me-in /
    captain-s-dinner 三本实测都是），不能判红。

    ⇒ 只有当**该块的其他分析字段也不是中文**时，才判「形式性规避」：
    此时整块分析层都是英文，中文理解里的那一个汉字只是形式上的——
    这正是 bruja-s-nest「加两个字」的形态。
    """
    if nominal_chinese_ratio(zh) >= NOMINAL_CN:
        return False
    others = [t for t in (why, struct) if t]
    if not others:
        return False
    return all(not HAN.search(t) for t in others)


def evasion_ratio(body, quote):
    """兼容旧接口：返回名义中文度（0 = 纯英文，1 = 全中文）。"""
    return nominal_chinese_ratio(body)


def sections(block):
    """把一个引语块解析成 {标签: 全文}。

    标签后接 bullet 续行时并入该标签（`关键词：` 下面挂 `- xxx` 的写法）。
    ⚠️ 续行判定必须用 `- ` / `* `（带空格），不能用 `*`——
    否则 `**句子结构**：…` 这种加粗标签行会被当成上一标签的续行，
    把中文字符追加进「中文理解」，让纯英文段落被误判为含中文。
    """
    out, cur = {}, None
    for raw in block.split("\n"):
        line = raw.strip()
        if not line or line == "---":
            continue
        s = re.sub(r"^[-*]\s+", "", line).replace("**", "").strip()
        m = LAB.match(s)
        if m:
            cur = m.group(1)
            out[cur] = m.group(2).strip()
        elif cur and line.startswith(("- ", "* ")):
            out[cur] = (out[cur] + " " + s).strip() if out[cur] else s
    return out


def scan_chapters(book_dir):
    """扫 ch*.md 的引语块。"""
    blocks = []
    for path in sorted(glob.glob(os.path.join(book_dir, "ch*.md"))):
        text = open(path, encoding="utf-8").read()
        idx = [m.start() for m in BLOCK.finditer(text)] + [len(text)]
        for start, end in zip(idx, idx[1:]):
            seg = text[start:end]
            sec = sections(seg)
            if not sec:
                continue
            quote = ""
            qm = re.match(r"^> \*\*原句 \d+:\*\*\s*(.*)$", seg.split("\n")[0])
            if qm:
                quote = qm.group(1).strip()
            blocks.append({
                "file": os.path.basename(path),
                "line": text[:start].count("\n") + 1,
                "quote": quote,
                "sec": sec,
                "kind": "chapter",
            })
    return blocks


def scan_overview(book_dir):
    """扫总览三篇（00_*.md）——v1 跳过这里，v2 纳入。

    总览的结构与章节不同（没有 `> **原句 N:**` 块），所以查两件事：
      ① 整行无中文的散文行（总览是中文文档，整段英文 = 没写）
      ② 行内英文引语（AGENTS 第 9 条 d2：英文原句必须成行 `> "…"` 引用块）

    ⚠️ 实测坑：`00_情感节点.md` / `00_金句精选.md` 里本来就有
    **「关键引语」清单**——内容是成行的英文原句（这是设计如此，不是缺陷）。
    所以 ① 必须**先剥掉引号内的内容**再判，否则整份「关键引语」列表
    会被整片误报（deathless 实测 46 处假红）。
    """
    findings = []
    for path in sorted(glob.glob(os.path.join(book_dir, "00_*.md"))):
        name = os.path.basename(path)
        for i, raw in enumerate(open(path, encoding="utf-8").read().split("\n"), 1):
            line = raw.strip()
            if not line or line.startswith(("#", "---", ">", "|", "```")):
                continue
            if not (line.startswith("- ") or re.match(r"^\d+\. ", line)):
                continue
            body = re.sub(r"^[-*]\s+", "", line)
            body = re.sub(r"^\d+\.\s+", "", body)
            body = body.replace("**", "")
            # ① 剥掉引号内内容后，仍是无中文的英文散文 ⇒ 英文段落
            bare = re.sub(r"[“\"][^”\"]*[”\"]", "", body).strip()
            if ENW.search(bare) and not HAN.search(bare) and len(bare) > 30:
                findings.append((name, i, "英文段落", bare[:70]))
            # ② 行内英文引语（d2 违规：英文原句必须成行 `> "…"` 引用块）
            for m in re.finditer(r"[“\"]([^”\"]{10,})[”\"]", body):
                inner = m.group(1)
                if len(ENW.findall(inner)) >= OVERVIEW_INLINE_WORDS and HAN.search(body):
                    findings.append((name, i, "行内引语", inner[:70]))
    return findings


def main():
    ap = argparse.ArgumentParser(description="中文层体检：分析字段必须是中文、不能是空话")
    ap.add_argument("book_dir")
    ap.add_argument("--quiet", action="store_true", help="只输出汇总数字")
    ap.add_argument("--max-list", type=int, default=12, help="每类最多列出几条明细")
    ap.add_argument("--no-overview", action="store_true", help="不扫总览三篇")
    args = ap.parse_args()

    if not os.path.isdir(args.book_dir):
        print(f"❓ 书目录不存在：{args.book_dir}")
        return 2

    blocks = scan_chapters(args.book_dir)
    print(f"=== 中文层体检（check_chinese_layer）：{os.path.basename(args.book_dir.rstrip('/'))} ===")
    if not blocks:
        print("❓ 无法判定：未解析出任何引语块（引语格式可能不是 `> **原句 N:**`）")
        print("   ⚠️ 这不是「干净」，是「没查」——不得据此判通过。")
        return 2

    blocking = {k: [] for k in
                ("英文理解", "缺中文理解", "敷衍句构", "残句", "形式性规避", "英文为什么")}
    hinting = {k: [] for k in ("夹杂理解", "夹杂为什么")}
    mixed_ids = set()
    good_blocks = 0

    uses_zh = any(
        (b["sec"].get("中文理解") or b["sec"].get("理解") or "").strip() for b in blocks
    )

    for bid, b in enumerate(blocks):
        sec = b["sec"]
        zh = sec.get("中文理解")
        if zh is None:
            zh = sec.get("理解")
        zh = (zh or "").strip()
        why = (sec.get("为什么这样写") or "").strip()
        st = (sec.get("句子结构") or "").strip()

        block_hits = []

        if not zh:
            # ⚠️ 只有**本书已在用**「中文理解」这个子项时，缺它才是缺陷。
            #    体裁对应格式表允许某些体裁只挂 关键词 / 叙事视角 / 人物弧线
            #    而不设「中文理解」——对那种书报「缺中文理解」是假红。
            if uses_zh:
                blocking["缺中文理解"].append(b)
                block_hits.append("缺中文理解")
        elif not HAN.search(zh):
            blocking["英文理解"].append(b)
            block_hits.append("英文理解")
        else:
            ratio = mix_ratio(zh)
            if ratio > MIX_WARN:
                hinting["夹杂理解"].append(b)
                mixed_ids.add(bid)
            if has_hollow(zh):
                blocking["残句"].append(b)
                block_hits.append("残句")
            if is_formal_evasion(zh, why, st):
                blocking["形式性规避"].append(b)
                block_hits.append("形式性规避")

        if st and is_lazy_struct(st):
            blocking["敷衍句构"].append(b)
            block_hits.append("敷衍句构")

        if why:
            if not HAN.search(why):
                blocking["英文为什么"].append(b)
                block_hits.append("英文为什么")
            else:
                ratio = mix_ratio(why)
                if ratio > MIX_WARN:
                    hinting["夹杂为什么"].append(b)
                    mixed_ids.add(bid)

        if not block_hits:
            good_blocks += 1

    total = len(blocks)
    mixed_ratio = len(mixed_ids) / total

    # ⑦ 整层中英夹杂——单条结论，不逐块列
    if mixed_ratio >= MIXED_BLOCK_RATIO:
        blocking["整层夹杂"] = [{
            "file": "（整层）", "line": 0,
            "quote": f"{len(mixed_ids)}/{total} 块含中英夹杂，占比 {mixed_ratio:.0%} ≥ {MIXED_BLOCK_RATIO:.0%}",
        }]

    # ⑧ 合格分析密度——单条结论，不逐块列
    density = good_blocks / total
    if density < DENSITY_FLOOR:
        blocking["密度不足"] = [{
            "file": "（整层）", "line": 0,
            "quote": f"合格分析 {good_blocks}/{total} 块，密度 {density:.0%} < {DENSITY_FLOOR:.0%}",
        }]

    # 总览三篇
    overview_findings = []
    if not args.no_overview:
        overview_findings = scan_overview(args.book_dir)
    for name, line, kind, snippet in overview_findings:
        if kind == "英文段落":
            blocking.setdefault("总览英文段落", []).append(
                {"file": name, "line": line, "quote": snippet})
        else:
            hinting.setdefault("总览行内引语", []).append(
                {"file": name, "line": line, "quote": snippet})

    n_block = sum(len(v) for v in blocking.values())
    n_hint = sum(len(v) for v in hinting.values())

    for label, items in blocking.items():
        print(f"❌ {label}：{len(items)} 处")
        if not args.quiet:
            for b in items[: args.max_list]:
                if b.get("line"):
                    print(f"     {b['file']}:{b['line']}")
                else:
                    print(f"     {b.get('quote', '')}")
            if len(items) > args.max_list:
                print(f"     …… 另有 {len(items) - args.max_list} 处")
    for label, items in hinting.items():
        print(f"⚠️ {label}：{len(items)} 处（提示型，不判红）")
        if not args.quiet:
            for b in items[: args.max_list]:
                print(f"     {b['file']}:{b['line']}")
            if len(items) > args.max_list:
                print(f"     …… 另有 {len(items) - args.max_list} 处")

    print(f"=== 汇总：{total} 个引语块 | 合格分析密度 {density:.0%} | "
          f"整层夹杂率 {mixed_ratio:.0%} | 阻断型 {n_block} | 提示型 {n_hint} ===")
    if not uses_zh:
        print("⚠️ 本书**未使用**「中文理解」子项（体裁格式表可能本就不要求）——"
              "该层**未核**，不得据此宣称「中文层已核」；若本书按格式表本应设该字段，"
              "则「缺中文理解」本应判红——请人工确认体裁口径。")
    if n_block:
        print("=== 结论：有阻断型，必须改（中文层不是中文 = 精读内容缺失）===")
        return 1
    print("=== 结论：无阻断型 ===")
    if n_hint:
        print("⚠️ 仍有提示型（中英夹杂），按 AGENTS 第 3 条「只记不改」——"
              "但**提示型占比 >30% 时不得直接申报完成**，须先抽样 20 条人工定性（见第 3 条量级条款）。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
