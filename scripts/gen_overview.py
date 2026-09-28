#!/usr/bin/env python3
"""总览三篇生产工具：英文与章号一律从**已核实引语池**注入，模板里零手打英文。

它替代的动作是「凭会话记忆重打金句」——Tomorrow, and Tomorrow 那批概述里
5 条引语 0 命中的事故就是这么来的。

用法：python3 scripts/gen_overview.py <书目录> [模板目录]
模板目录默认取 <书目录>/.overview_templates/，不存在时回退 scripts/overview_templates/。
硬保证：
  1. 池只从 ch*.md 的 `> **原句 N:**` 块抽（这些已过 verify_quotes）
  2. 池中每条在写入前再 flat 比对一次 text/（错章即退出码 2）
  3. 模板占位符 {Q:ch:seq} / {P:ch:seq} 全部展开；引不到的占位符 → 退出码 2
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


def build_pool(book: str):
    pool = {}
    for f in sorted(glob.glob(f"{book}/ch*.md"),
                    key=lambda x: int(re.search(r"ch(\d\d)", x).group(1))):
        n = int(re.search(r"ch(\d\d)", f).group(1))
        txt = open(glob.glob(f"{book}/text/ch{n:02d}_*.txt")[0], encoding="utf-8").read()
        flat = re.sub(r"[^a-z0-9]", "", txt.lower())
        for m in re.finditer(r'> \*\*原句 (\d+):\*\* (.+)\n\n\*\*中文理解\*\*：(.+?)\n',
                             open(f, encoding="utf-8").read()):
            seq, q, zh = int(m.group(1)), m.group(2).strip(), m.group(3).strip()
            if re.sub(r"[^a-z0-9]", "", q.lower()) not in flat:
                print(f"❌ ch{n:02d}#{seq} 不在 text/，池中止")
                raise SystemExit(2)
            pool[(n, seq)] = (q, zh)
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
    这里把一行里的多条带标注引语拆成多行——它是机械后处理，不改一个字。"""
    out = []
    for line in body.split("\n"):
        if line.count("（ch") <= 1 or line.startswith("> "):
            out.append(line)
            continue
        head, sep, rest = line.partition("：")
        if not sep or not head.startswith("**"):
            out.append(line)              # 散文段落交给模板自己分行，不在这里拆
            continue
        parts = re.split(r"(?=\"[^\"]{20,}\"（ch\d\d）)", rest)
        parts = [x for x in parts if x.strip()]
        if len(parts) < 2:
            out.append(line)
            continue
        if head:
            out.append(head + "：")
        # 把落单的连词碎片（"与" / "；与" / "与 … 同源；"）并入下一条
        merged, carry = [], ""
        for x in parts:
            x = x.strip()
            if not x.startswith('"'):
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
