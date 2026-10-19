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

**实测数据（2026-10-19）**
------------------------
    书                                      块   纯英文理解  中英夹杂  敷衍句构  缺中文理解
    bruja-s-nest                          1091        1030       49       797          0
    as-you-wake                           1056         833      158         0          0
    armor-for-liars                        472         146      304        17          0
    bright-girl                            370          86      271         0          0
    maybe-next-time                        381         210       77         0         29
    breathe-me-in                          166         119       21         5          1
    captain-s-dinner                       152         110       30         0          0
    the-book-of-the-dead                   179          81       90         0          0
    battle-of-the-round-house               31          12       18         0          0
    beware-the-abbott-boys                 127           5        0         0        122
    —— 旧书基线（this-time-tomorrow / incarnate / under-the-same-stars）纯英文 0 ——

**判定分档（照 AGENTS 第 3 条四档）**
-----------------------------------
  ❌ 阻断型（必须改）
     ① 「中文理解」**整段无中文**——字段写成英文，等于没写
     ② 引语块**缺「中文理解」**——该字段根本没有
        （⚠️ 仅当**本书已在用**该子项时才算缺陷；某些体裁按格式表本就不设它）
     ③ 「句子结构」是敷衍模板（"两句话。" / "简单陈述句。"）——零信息量
  ⚠️ 提示型（只记不改）
     ④ 中英夹杂：字段有中文，但**英文单词字符占比 > 35%**——典型如
        "朋友们放下 reservations 来 wish Godspeed"（reservations / wish Godspeed 未译）
     ⑤ 「为什么这样写」整段无中文
  ❓ 跳过型
     本书一个引语块都没解析出来 → **不算通过**，报「无法判定」

**为什么 ④ 只报不判红**
----------------------
中英夹杂没有客观边界：专有名词（Mignonette / Godspeed / doomsayers）本来就该保留英文，
人名地名更不能译。35% 是启发式阈值，**必然有误判**，所以只作提示不作门禁。
但 ❌①③ 是**二元事实**（有没有中文、是不是空话），可以判红。

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


def is_lazy_struct(text):
    body = (text or "").strip().rstrip("。．.！!？? 　")
    return body in LAZY_TEMPLATES


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


def mix_ratio(text):
    """英文单词字符数 /（英文 + 中文）字符数。引号内的原文不计入。"""
    text = re.sub(r'[“"][^”"]*[”"]', "", text)
    han = len(HAN.findall(text))
    en = sum(len(w) for w in ENW.findall(text))
    total = en + han
    return en / total if total else 0.0


def scan(book_dir):
    blocks = []
    for path in sorted(glob.glob(os.path.join(book_dir, "*.md"))):
        name = os.path.basename(path)
        if name.startswith("00_"):
            continue
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
            blocks.append({"file": name, "line": text[:start].count("\n") + 1,
                           "quote": quote, "sec": sec})
    return blocks


def main():
    ap = argparse.ArgumentParser(description="中文层体检：分析字段必须是中文、不能是空话")
    ap.add_argument("book_dir")
    ap.add_argument("--quiet", action="store_true", help="只输出汇总数字")
    ap.add_argument("--max-list", type=int, default=12, help="每类最多列出几条明细")
    args = ap.parse_args()

    if not os.path.isdir(args.book_dir):
        print(f"❓ 书目录不存在：{args.book_dir}")
        return 2

    blocks = scan(args.book_dir)
    print(f"=== 中文层体检（check_chinese_layer）：{os.path.basename(args.book_dir.rstrip('/'))} ===")
    if not blocks:
        print("❓ 无法判定：未解析出任何引语块（引语格式可能不是 `> **原句 N:**`）")
        print("   ⚠️ 这不是「干净」，是「没查」——不得据此判通过。")
        return 2

    blocking = {"英文理解": [], "缺中文理解": [], "敷衍句构": []}
    hinting = {"夹杂理解": [], "英文为什么": [], "夹杂为什么": []}
    uses_zh = any(
        (b["sec"].get("中文理解") or b["sec"].get("理解") or "").strip() for b in blocks
    )

    for b in blocks:
        sec = b["sec"]
        zh = sec.get("中文理解")
        if zh is None:
            zh = sec.get("理解")
        if zh is None or not zh.strip():
            # ⚠️ 只有**本书已在用**「中文理解」这个子项时，缺它才是缺陷。
            #    体裁对应格式表（docs/新书启动模板.md）允许某些体裁只挂
            #    关键词 / 叙事视角 / 人物弧线而不设「中文理解」——
            #    对那种书报「缺中文理解」是假红（实测 flashlight 149/149、
            #    lady-of-the-lake 368/368、the-man 377/377 全是这一类）。
            if uses_zh:
                blocking["缺中文理解"].append(b)
        elif not HAN.search(zh):
            blocking["英文理解"].append(b)
        else:
            if mix_ratio(zh) > 0.35:
                hinting["夹杂理解"].append(b)

        st = sec.get("句子结构", "")
        if is_lazy_struct(st):
            blocking["敷衍句构"].append(b)

        why = sec.get("为什么这样写", "")
        if why:
            if not HAN.search(why):
                hinting["英文为什么"].append(b)
            elif mix_ratio(why) > 0.35:
                hinting["夹杂为什么"].append(b)

    n_block = sum(len(v) for v in blocking.values())
    n_hint = sum(len(v) for v in hinting.values())

    for label, items in blocking.items():
        print(f"❌ {label}：{len(items)} 处")
        if not args.quiet:
            for b in items[: args.max_list]:
                print(f"     {b['file']}:{b['line']}")
            if len(items) > args.max_list:
                print(f"     …… 另有 {len(items) - args.max_list} 处")
    for label, items in hinting.items():
        print(f"⚠️ {label}：{len(items)} 处（提示型，不判红）")
        if not args.quiet:
            for b in items[: args.max_list]:
                print(f"     {b['file']}:{b['line']}")
            if len(items) > args.max_list:
                print(f"     …… 另有 {len(items) - args.max_list} 处")

    total = len(blocks)
    print(f"=== 汇总：{total} 个引语块 | 阻断型 {n_block} | 提示型 {n_hint} ===")
    if n_block:
        print("=== 结论：有阻断型，必须改（中文层不是中文 = 精读内容缺失）===")
        return 1
    print("=== 结论：无阻断型 ===")
    if n_hint:
        print("⚠️ 仍有提示型（中英夹杂），按 AGENTS 第 3 条「只记不改」，但需在报告里写明。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
