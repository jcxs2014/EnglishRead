#!/usr/bin/env python3
"""总览三篇生产工具：英文与章号一律从**已核实引语池**注入，模板里零手打英文。

它替代的动作是「凭会话记忆重打金句」——Tomorrow, and Tomorrow 那批概述里
5 条引语 0 命中的事故就是这么来的。

用法：python3 scripts/gen_overview.py <书目录> [模板目录]
模板目录默认取 <书目录>/.overview_templates/，不存在时回退 scripts/overview_templates/。
硬保证：
  1. 池只从 ch*.md 的 `> **原句 N:**` 块抽（这些已过 verify_quotes）
  2. 池中每条在写入前再 flat 比对一次 text/（错章即退出码 2）
  3. 模板占位符 {Q:NN:seq} / {P:NN:seq} 全部展开（**NN 是纯数字章号**，不是 chNN）；引不到的占位符 → 退出码 2
  4. 一行只放一条带章号标注的引语（check_overview_full 取「引语前 40 字窗口内
     第一个 chNN」，一行两条必然张冠李戴——Tomorrow and Tomorrow 批次实证）
  5. 金句编号止于 ㉕（verify_overview_quotes 的 CIRCLED 口径）
"""
import glob
import json
import os
import re
import sys

CIRCLED = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕"

# 中文理解标记：冒号可在粗体内（`**中文理解：**`）也可在粗体外（`**中文理解**：`）
_ZH_LABEL = re.compile(r"^\*\*中文理解[：:]?\*\*[：:]?\s*")


def build_pool(book: str):
    pool = {}
    for f in sorted(glob.glob(f"{book}/ch*.md"),
                    key=lambda x: int(re.search(r"ch(\d+)", x).group(1))):
        found = 0
        n = int(re.search(r"ch(\d+)", f).group(1))
        # 章号位数不定：2 位（ch08_）与 3 位（ch076_，全书连号）都要认。
        # 2026-09-28 i-have-some-questions-for-you 实测：'%02d' 匹配不到 ch076，
        # 脚本直接 IndexError。真源是文件名自带的位数，不是 ch 的位数。
        hits = [g for w in (3, 2, 1)
                for g in glob.glob(f"{book}/text/ch{n:0{w}d}_*.txt")]
        if not hits:
            raise SystemExit(f"❌ text/ 里找不到 ch{n} 的提取件")
        txt = open(sorted(hits)[0], encoding="utf-8").read()
        flat = re.sub(r"[^a-z0-9]", "", txt.lower())
        # ⚠️ 2026-09-28 修正：本工具原写 `\*\*中文理解\*\*：`（冒号在粗体**外**），
        # 而 Paris Deception 全书用 `**中文理解：**`（冒号在粗体**内**）——
        # 正则静默匹配 0 条，症状是「引语池无 chNN#1」：**池空**而非格式错。
        # 且 build_pool 不校验命中数，错误一路拖到 expand() 才以
        # 「这本书的引语池里没有它」的面目报出，极难回溯到格式。
        # ⚠️ 2026-09-29 修正（本批次实测）：上一版把 `**中文理解**` 标记写成**必需**，
        # 而本库相当一部分精简格式书的"中文理解"是**无标记的整段**（The Lack of
        # Light ch01、I Am Homeless ch01 全部如此）⇒ 静默抽 0 条，症状仍是
        # 「引语池无 chNN#1」。现改为：**标记可选**；无标记时取引语块后第一段正文，
        # 并在它以 `**` 开头（即其实是别的子项）时跳过该块。
        for m in re.finditer(r'> \*\*原句 (\d+):\*\* (.+)\n\n(.+?)\n',
                             open(f, encoding="utf-8").read()):
            seq, q, seg = int(m.group(1)), m.group(2).strip(), m.group(3).strip()
            if seg.startswith("**中文理解"):
                zh = _ZH_LABEL.sub("", seg, count=1).strip()
            elif seg.startswith("**"):
                continue            # 紧跟的是别的子项行，不是中文理解
            else:
                zh = seg            # 无标记形态：整段就是中文理解
            # ⚠️ 2026-09-30 修正（The Secret Wife 实测 22 条）：含 `…` 的引语
            # **整串**永远 flat 匹配不上——flat 化会把省略号连同两侧空白全删掉，
            # 于是「A … B」被拼成「AB」，而原文里 A 与 B 之间隔着整段文字。
            # 后果：build_pool 在第一个带省略号的块上就 SystemExit，
            # **该书任何模板都生成不出来**，而实际两侧逐字都在（已逐条取证）。
            # 按 AGENTS 第 5 条「判 A 前必须拆 fragment 分段取证」的口径，
            # 这里同样分段验证：每一片段单独 flat 命中即算通过。
            _q = re.sub(r"[^a-z0-9]", "", q.lower())
            if _q not in flat:
                _frags = [re.sub(r"[^a-z0-9]", "", p.lower())
                          for p in re.split(r"…|\.\.\.", q)]
                _frags = [f for f in _frags if f]
                if _frags and all(f in flat for f in _frags):
                    pass                      # 分段全部命中 ⇒ 合法省略
                else:
                    print(f"❌ ch{n:02d}#{seq} 不在 text/，池中止")
                    raise SystemExit(2)
            pool[(n, seq)] = (q, zh)
            found += 1
        if not found:
            print("❌ %s 抽到 0 条引语——多半是**子项标记形态**与本正则不符" % f)
    return pool


def expand(tpl: str, pool) -> str:
    def q(m):
        key = (int(m.group(1)), int(m.group(2)))
        if key not in pool:
            raise SystemExit(f"❌ 引语池无 ch{key[0]:02d}#{key[1]}")
        return pool[key][0]
    out = re.sub(r"\{Q:(\d+):(\d+)\}", q, tpl)
    left = re.findall(r"\{[QP]:\d+:\d+\}", out)
    if left:
        raise SystemExit(f"❌ 未展开的占位符: {left[:3]}")
    return out



def one_quote_per_line(body: str) -> str:
    """check_overview_full 取「引语前 40 字窗口内的第一个 chNN」判归属，
    同一行放两条带章号标注的引语必然张冠李戴（Tomorrow and Tomorrow 批次实证）。
    这里把一行里的多条带标注引语拆成多行——它是机械后处理，不改一个字。

    ⚠️ 2026-09-28 三处修正（Paris Deception 批次实测，6 处标注错位降到 0）：
      ① 拆点正则原来只认**直引号** `"..."`，而池里注入的是**弯引号**——
         对弯引号书稿整段是死代码。症状极隐蔽：文件照写、expand 全展开、
         verify 全绿，只有 check_overview_full 的标签对账才报。
      ② 原来只拆 `**` 开头的行，**散文行原样放过**——而叙事概括里恰恰
         引用最多（"……也先出卖了所有人。{引语A}……因为她要的是「不改」：{引语B}"）。
      ③ 拆点要求引语段以引号起首，但**台词中段的引语没有开引号**
         （如 ch22 那句 `I couldn't allow her to become some—some Nazi Hausfrau…`
         源文本里本就没有开引号），于是拆点错位、前一条的标注被后一条继承。
         ⇒ 改为**以 `（chNN）` 标注为锚点**拆，而不是以引号为锚点：
         标注是模板作者唯一必写、且必写对的东西。
    """
    out = []
    for line in body.split("\n"):
        if line.count("（ch") <= 1 or line.startswith("> "):
            out.append(line)
            continue
        head, sep, rest = line.partition("：")
        if not sep:
            head, rest = "", line          # 无冒号的散文行：整行都是 rest
        # 以 chNN 标注为锚点，**在标注之后**切——模板形态是 `{引语}（chNN）`，
        # 标注在引语**后面**；按标注前切会把引语与自己的标注劈到两行（实测）。
        parts = re.split("(?<=（ch\\d\\d）)", rest)
        parts = [x for x in parts if x.strip()]
        if len(parts) < 2:
            out.append(line)
            continue
        if head:
            out.append(head + "：")
        # 落单的引导语（「与」／「他离开德国的理由，是直接因果。」）并入下一条
        merged, carry = [], ""
        for x in parts:
            x = x.strip()
            if "（ch" not in x:
                carry += x
                continue
            merged.append("- " + (carry + x).strip())
            carry = ""
        if carry:
            merged.append(carry)
        out.extend(merged)
    return "\n".join(out)


def main() -> int:
    book = sys.argv[1]
    pool = build_pool(book)
    here = os.path.dirname(__file__)
    # 模板按书隔离：优先 <书目录>/.overview_templates/，否则用全局目录。
    # ⚠️ 2026-09-28 补：模板原本只有全局一处，而模板内容是**书专属**的
    # （占位符 {Q:ch:seq} 指向该书自己的章号）——两本书共用目录时，
    # 为 A 书写的模板会被拿去给 B 书生成，于是两本书都被写坏。
    tpl_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.join(book, ".overview_templates")
    if not os.path.isdir(tpl_dir):
        tpl_dir = os.path.join(here, "overview_templates")
    tpls = sorted(glob.glob(os.path.join(tpl_dir, "ov_*.md.tpl")))
    if not tpls:                     # 空 glob 会让循环静默跳过并退出 0 —— 那是「假成功」
        raise SystemExit(f"❓ 未找到模板：{tpl_dir}/ov_*.md.tpl")
    for tpl_path in tpls:
        name = os.path.basename(tpl_path)[3:-len(".tpl")]
        tpl = open(tpl_path, encoding="utf-8").read()
        if name.startswith("00_金句") and tpl.count("**中文**") > len(CIRCLED):
            raise SystemExit(f"❌ {name} 超过 ㉕，超出 verify_overview_quotes 口径")
        body = one_quote_per_line(expand(tpl, pool))
        path = os.path.join(book, name)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(body)
        print(f"✅ 写入 {path}（引语全部来自已核实池，零手打英文）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
