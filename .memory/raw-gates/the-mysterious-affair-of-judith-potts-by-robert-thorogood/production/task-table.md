# 任务表 · The Mysterious Affair of Judith Potts（Robert Thorogood）

- 书目录：`notes/books/mystery-thriller/the-mysterious-affair-of-judith-potts-by-robert-thorogood/`
- 体裁：mystery-thriller（推理 / 悬疑，长篇，精简格式）｜导航 5 项｜精读 4 子项｜总览 3 篇
- 语料：38 件（Prologue + Chapter 1–37），`text/ch01_prologue.txt` … `text/ch38_chapter_37.txt`
- 编号约定：**md 文件号 = 书内章号 + 1**（ch01=Prologue，ch02=书内 Chapter 1，…，ch38=书内 Chapter 37）
- 契约：`python3 scripts/bookform.py "<书目录>" --contract`

## 进度

| 章 | 书内 | 状态 | commit |
|---|---|---|---|
| ch01 | Prologue | ✅ 完工（7 块，chapter.sh rc=0） | 7f75c59e7 |
| ch02 | Chapter 1 | 🔄 派工中 | |
| ch03 | Chapter 2 | 🔄 派工中 | |
| ch04 | Chapter 3 | 🔄 派工中 | |
| ch05–ch38 | Chapter 4–37 | ⬜ 未开始 | |
| 00_概述 / 00_金句精选 / 00_情感节点 | — | ⬜ 未开始（全书完工后） | |
| T1 自检 | — | ⬜ 未开始（三件产物缺一不算完工） | |

## 剩余任务清单

1. ch05–ch38：每章走「素读清单 → suread.py → 写 md → vocab_candidates/build_vocab_section → chapter.sh rc=0 → 立刻按 pathspec commit」
2. 批次收口：`bash scripts/gate.sh "<书目录>"` 退出码 0
3. 总览三篇：引语从已过门禁的章节块程序化抽取，逐条 grep 回原文 + 说话人归属核验
4. T1 自检（创建卡 §6.1）：38 章 → 抽样 1/5 且至少 10 章、首末章必含；总览三篇全篇人判；assertion_scan 六类预筛；产出 t1-verdict.md / t1-candidates.txt / 台账一行
5. 协作板：仅 `python3 scripts/post_collab.py`（板每书一条）
6. push 须用户明确指令
