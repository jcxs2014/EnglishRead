#!/usr/bin/env python3
"""把新一章的 md 骨架 + 占位符 + 词表小节一次性生成（生产工具，省掉手搭结构）。

用法:
  python3 scripts/new_chapter.py "<书目录>" <NN> '<h1 标题>' '<一句话概括>' \
      '<情感弧线位置>' '<tropes>' '<人物弧线>' '<叙事手法>' \
      --quotes 'Q1=@prefix;Q2=@prefix*;Q3=@prefix+2' \
      --blocks 'Q1=主题1|中文理解1|关键词1|为什么这样写1|读者视角提示1; ...'

行为:
  - 写 frontmatter（状态: 未读 + modified: 首 commit 日期）与全部 H2/H3 骨架；
  - 立刻调用 inject_by_para 把引语按坐标逐字注入；**注入失败时不保留半成品 md**
    （⚠️ 2026-09-29 修正：原实现先落盘再注入，注入失败退出 2 却把带 `«Q1»` 占位符的
      半成品留在磁盘上——与本 docstring 宣称的「不落文件」矛盾，且半成品会被后续
      rename/commit 当成正常章节。实测 ch47 首次生成失败后留下 `ch47 chapter 46.md`）；
  - 本章词汇小节留空（随后由 build_vocab_section.py 填）。

⚠️ 五子项／四子项里的**英文必须由分析者从 text/ 复制**，本脚本不生成任何英文。
   引语本身由 inject_by_para 从 text/ 逐字取出（零手打）。
"""
import re
import subprocess
import sys
from pathlib import Path

args = sys.argv[1:]
book = Path(args[0])
nn = args[1]
h1 = args[2]
nav = args[3:8]
quotes = ""
blocks = ""
for a in args[8:]:
    if a.startswith("--quotes="):
        quotes = a.split("=", 1)[1]
    elif a.startswith("--blocks="):
        blocks = a.split("=", 1)[1]

src = sorted((book / "text").glob(f"ch{int(nn):02d}_*.txt"))
if not src:
    print(f"❌ text/ch{int(nn):02d}_*.txt 不存在")
    sys.exit(2)
tag = src[0].stem.split("_", 1)[1].replace("_", " ")
fname = book / f"ch{int(nn):02d} {tag}.md"

lines = ["---", "状态: 未读", 'modified: "2026-09-29"', "---", "", f"# {h1}", "", "## 本章导航", ""]
for label, body in zip(
    ("一句话概括", "情感弧线位置", "Tropes 兑现/反转", "人物弧线", "叙事手法"), nav
):
    lines += [f"**{label}**：{body}", ""]
lines += ["---", "", "## 精读", ""]

for i, blk in enumerate([b for b in blocks.split(";") if b.strip()], 1):
    fields = [x.strip() for x in blk.split("|")]
    if len(fields) < 5 or not re.fullmatch(r"Q\d+", fields[0]):
        print(f"❌ 块 {i} 格式错（须 5 段：Q编号|中文理解|关键词|为什么这样写|读者视角提示）"
              f"，实得 {len(fields)} 段：{blk[:60]!r}")
        sys.exit(2)
    cn, kw, why, reader = fields[1:5]
    lines += [f"> **原句 {i}:** «Q{i}»", "", f"**中文理解**：{cn}", "",
              f"**关键词**：{kw}", "", f"**为什么这样写**：{why}", "",
              f"**读者视角提示**：{reader}", "", "---", ""]

lines += ["## 本章词汇", "", "### ⭐⭐⭐ 高级", "", "| 词/短语 | 释义 | 例句 |", "|---|---|---|", "",
          "### ⭐⭐ 进阶", "", "| 词/短语 | 释义 | 例句 |", "|---|---|---|", "",
          "### ⭐ 基础", "", "| 词/短语 | 释义 | 例句 |", "|---|---|---|", "",
          "## 一句话总结", ""]

fname.write_text("\n".join(lines) + "\n", encoding="utf-8")

specs = []
for q in quotes.split(";"):
    q = q.strip()
    if not q:
        continue
    tag_, loc = q.split("=", 1)
    loc = "@" + loc.strip().lstrip("@")          # inject_by_para 用 'QN=@前缀' 解析
    specs.append(f"{tag_.strip()}={loc}")
if specs:
    # ⚠️ 2026-09-29 修正：此前此处调用的是 inject_quotes.py，而它把第二段参数当成
    # **引语全文**（只做 flat 断言后原样注入）⇒ 传「定位前缀」时它把前缀当引语注入，
    # 产出**截短的引语**（`Althea saw the torchlight` 而非整句）且 flat 全绿 ⇒
    # 六道门禁结构上看不见（AGENTS 9a2 引语截短）。本脚本 docstring 与
    # WRITING_RULES §3.3 描述的「前缀 → 整句」语义由 inject_by_para.py 实现。
    r = subprocess.run(
        ["python3", "scripts/inject_by_para.py", str(fname), str(src[0]), *specs],
        capture_output=True, text=True)
    sys.stdout.write(r.stdout)
    sys.stderr.write(r.stderr)
    if r.returncode != 0:
        # 注入失败 ⇒ 删掉半成品再退出。留着带 `«Q1»` 占位符的 md 会被后续
        # rename_chapters / commit 当成正常章节，且占位符永远不会被填上。
        fname.unlink(missing_ok=True)
        print(f"🧹 已删除半成品 {fname.name}（注入失败，不留占位符文件）")
        sys.exit(r.returncode)
print(f"✅ 已生成 {fname.name}（{len(specs)} 条引语逐字注入）")
