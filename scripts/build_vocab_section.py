#!/usr/bin/env python3
"""生成 md 的「本章词汇」三档小节（词头+例句由脚本从 text/ 逐字取出，释义由调用方提供）。

用法:
  python3 scripts/build_vocab_section.py <md> <NN> '<head> 释义' '<head> 释义' ...
  或 python3 scripts/build_vocab_section.py <md> <NN> '<json 串>'
  或 python3 scripts/build_vocab_section.py <md> <NN> --glosses <json 文件>

⚠️ 2026-09-27 修正：本脚本此前在**任何输入下都崩**（`glosses_arg` 未定义），且 docstring
声称的位置参数形式与代码的 json.loads 不一致——**该形式从未通过**。现按「第一个空格分隔」解析。

未提供释义的词头不会被写入（宁缺毋造），脚本会打印缺哪些释义。
"""
import json
import re
import subprocess
import sys
from pathlib import Path

md = Path(sys.argv[1])
ch = sys.argv[2]
gloss_arg = sys.argv[3:]

if gloss_arg and gloss_arg[0] == "--glosses":
    glosses = json.load(open(gloss_arg[1], encoding="utf-8"))
else:
    joined = " ".join(gloss_arg)
    if not joined.strip():
        glosses = {}
    else:
        try:
            glosses = json.loads(joined)
        except json.JSONDecodeError:
            glosses, bad = {}, []
            for one in gloss_arg:          # '<head> 释义'：第一个空格分隔
                if " " in one.strip():
                    h, g = one.strip().split(" ", 1)
                    glosses[h] = g.strip()
                else:
                    bad.append(one)
            if bad:
                print("⚠️ 位置参数需为 '<head> 释义'（中间有空格），以下已跳过: " + " ".join(bad))

try:
    out = subprocess.run(
        ["python3", "scripts/vocab_candidates.py", str(md.parent), "--ch", ch, "--tiers", "--limit", "300"],
        capture_output=True, text=True, check=True).stdout
except subprocess.CalledProcessError:
    if not str(ch).isdigit():
        print(f"❓ 章号 {ch!r} 非法"); sys.exit(2)
    print(f"❓ ch{ch} 取不到候选集——先查 text/ch{int(ch):02d}_*.txt 是否存在、cwd 是否在仓库根")
    sys.exit(2)
if not out.strip():
    print("❓ 候选集为空——先怀疑 cwd 是否在仓库根、--ch 章号是否越界"); sys.exit(2)

rows, cur = [], None
for line in out.split("\n"):
    if line.startswith("###"):
        cur = "高级" if "⭐⭐⭐" in line else ("进阶" if "进阶" in line else "基础")
    elif line.startswith("| "):
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) >= 3 and c[0] != "词/短语" and not set(c[0]) <= set("-: "):
            rows.append((cur, c[0], c[2].replace("（释义待填）", "").strip()))

# --- 硬断言：任一不满足即拒绝产出（宁缺毋造）---
# 来源：Two Wars and a Wedding 批次——手写词表初稿 40 余行是 `Not a real one.` 占位
# （AGENTS「凭印象手写词条」缺陷类，实测初稿缺陷率 14%–43%，脚本产出 0%）。
#
# ⚠️ 断言的对象是**本脚本将要写入的每一行**，不是调用方传来的东西——
# 例句恒由本脚本从 text/ 抽取，调用方只提供释义，所以「例句由调用方给错」这种情形
# 不存在；真正要防的是①`vocab_candidates` 抽错章②词表头被自造③释义留空。
# （2026-09-28 自证：曾把断言写成校验调用方传入的例句，结果**永远不可能触发**——
#  是死代码，不是防线。注入跨章例句后脚本照样退出 0。）
flat = re.sub(r"[^a-z0-9]", "", next(md.parent.glob(f"text/ch{int(ch):02d}_*.txt"))
              .read_text(encoding="utf-8").lower())
cand = {h: ex for _, h, ex in rows}
errors = []
for head, gloss in glosses.items():
    if head not in cand:
        errors.append(f"词头不在本章候选集内（自造？）: {head}")
    elif not gloss.strip():
        errors.append(f"缺释义: {head}")
for head, ex in cand.items():
    if re.sub(r"[^a-z0-9]", "", ex.lower()) not in flat:
        errors.append(f"例句不逐字命中本章（候选抽取异常）: {head} -> {ex[:40]}")
if errors:
    print("\n".join(errors))
    print(f"\n❌ {len(errors)} 处问题，未产出（宁缺毋造）")
    sys.exit(2)

missing = [h for _, h, _ in rows if h not in glosses]
if missing:
    shown = ", ".join(missing[:12]) + (f" …共 {len(missing)} 条" if len(missing) > 12 else "")
    print(f"⚠️ 候选集里 {len(missing)} 条未给释义（都不会写入，候选集已取全量故此数正常）: {shown}")

tables = {k: [] for k in ("高级", "进阶", "基础")}
for tier, head, ex in rows:
    if head in glosses:
        tables[tier].append(f"| {head} | {glosses[head]} | {ex} |")

# 空档留空——**不插占位行**：`| （本章无X词） | | |` 会被 check_vocab 判 FAIL
# （AGENTS「词汇表批量生成勿留占位行」）。三档是分类不是配额。
sec = ["## 本章词汇", ""]
for tier, star in (("高级", "⭐⭐⭐"), ("进阶", "⭐⭐ 进阶"), ("基础", "⭐ 基础")):
    sec += [f"### {star}", "", "| 词/短语 | 释义 | 例句 |", "|---|---|---|"]
    sec += tables[tier]
    sec += [""]

text = md.read_text(encoding="utf-8")
i = text.index("## 本章词汇")
j = text.index("## 一句话总结")
md.write_text(text[:i] + "\n".join(sec) + "\n" + text[j:], encoding="utf-8")
print(f"已写入 {md.name}: 高级 {len(tables['高级'])} / 进阶 {len(tables['进阶'])} / 基础 {len(tables['基础'])}"
      f"（共 {sum(len(v) for v in tables.values())} 条，3 项硬断言全过）")
