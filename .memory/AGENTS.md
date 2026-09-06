---
name: englishread-memory-index
description: EnglishRead 工作区跨会话记忆索引
metadata:
  type: user
---

# EnglishRead 记忆索引

> 本文件 = **记忆索引**（不包含规则内容，规则见根 AGENTS.md 和 docs/新书启动模板.md）。
> 新会话读取顺序：system-reminder → docs/新书启动模板.md → 根 AGENTS.md。

## 核心规则文档

| 文档 | 位置 | 用途 |
|------|------|------|
| 精读执行规则 | `AGENTS.md`（根目录） | 完整执行规则（格式/门禁/工具链/git 策略） |
| **新书启动模板** | `docs/新书启动模板.md` | **每本新书开工前必读**，含执行规则速查 + 历史坑表 |
| 协作消息板 | `COLLABORATION.md` | 跨 IDE 实时消息（newest first） |

## 重要记忆（按时间倒序）

### 2026-09-06 新增

- **The Last Thing（Bethany Monaco Smith）言情长篇 contemporary romance**：32 章（Chapter 1-31 + Epilogue），双 POV（Hallie/Deck 交替），逐章精读格式 + 3 篇总览。核心主题：命运 vs 选择、爱的勇气、家庭的多样性。Hallie 从"反爱情"到"说出我爱你"，Deck 从"控制狂"到"fun partner"。独立五步审查零缺陷。verify 355/355 ✅ / vocab FAIL=0 / entities 0。
- **No Take Backs（Taylor Wilson-West）逆后宫超自然言情**：29 章 + Epilogue，4 POV（Moraine/Soren/Rhea/Benny），逐章精读精简格式 + 3 篇总览。独立五步审查零缺陷。verify 219/219 ✅ / vocab FAIL=0 / entities 0。
- **Taken by Sinistre Ange（Sinistre Ange）言情长篇 erotic romance**：14 章 + 3 篇总览，含绑架/性支配/斯德哥尔摩综合征题材。独立五步审查修复 7 处缺陷。verify 133/133 ✅ / vocab FAIL=0 / entities 0。
- **Memories Like Fangs（Chelsey J. León）奇幻言情**：44 章 + 3 篇总览，双时间线（1960s/1990s），Rina/Emilio 跨种族恋爱。独立五步审查整改 27 处。verify 248/248 ✅ / vocab FAIL=0 / entities 0。

### 2026-09-05 新增
- **Wild Dark Shore（Charlotte McConaghy）言情长篇小说**：75 章（6 POV：Rowan/Fen/Dominic/Orly/Raff/Alex），逐章精读精简格式 + 3 篇总览。核心主题：爱与牺牲、家庭与血缘、自然与文明。Rowan 为寻夫来到 Shearwater 岛，融入 Salt 一家，最终为保护 Orly 淹死在竖井中。独立审查修复 31 个 FAIL + 5 处实体误判。verify 386/386 ✅ / vocab FAIL=0 / entities 0。
- **The Lack of Light（Nino Haratischwili）文学小说**：25 章，逐章精读精简格式 + 3 篇总览。四人友谊与创伤叙事（Dina/Keti/Ira/Nene），横跨第比利斯 1987 至布鲁塞尔 2019。独立审查修复 30 处词汇例句未命中 + ch09 重复引语块。verify 191/191 ✅ / vocab FAIL=0 / entities 0。
- **A Sea of Unspoken Things（Adrienne Young）推理悬疑奇幻**：32 章（含 ch18 "Twenty Years Ago" 闪回章节），逐章精读 + 3 篇总览。格式为推理/悬疑/奇幻精简格式（frontmatter + 本章导航 + 3-8 处精读 + 三档词汇 + 一句话总结）。独立审查发现并修复 5 处问题（ch01 编号、ch23 跨章错植、01_quotes 3 处 A 类虚构引语）。
- **Ten Bridges I've Burnt（Brontë Purnell）诗歌回忆录**：31 首自由诗，逐章精读 + 诗歌技法专项。格式按"随笔集逐篇精读"框架适配，新增"诗歌技法专项"章节分析跨行连续/括号自反/通感联觉/自造词等。
- **Addie LaRue 词汇精简**：ch098-108 词汇表从 ~1638 WARN 精简至 87 WARN（每章 25-30 词条）
- **Getaway Girl 双 POV**：Addison/Elijah 交替视角，需注意引语归属和人物弧线的对称性
- **Butcher of the Forest 场景节分章**：无章节号的中篇可按 `* * *` 场景分隔分章
- **文件命名修正**：Ten Bridges 初版用 `NN Title.md`（缺 ch 前缀），后统一重命名为 `chNN Title.md` 对齐其他书规范

### 2026-08-31 新增
- **Ligotti 第四次复查整改**（commit ba9b2e0）：
  - check_vocab全书词频口径盲区——A类虚构（如ch33 nullify/ch52占位符/ch73 night）在别章出现即通过check_vocab FAIL=0，但verify_quotes仍100%
  - check_chapter_quotes按flat文本匹配，省略号/标点差异导致误报（如ch22 PLACE引语"the diseased waters await his embrace"因无whose匹配失败）
  - 旧格式章节（①编号→`> **原句 N:**`）转换时缺冒号后空格导致引语提取失败
  - 49章旧格式转换后仍残留全部标为"原句1"（ch22/27/28/29）——圈数字映射bug
  - 详见 `docs/新书启动模板.md` 第9条规则说明

### 2026-08-30 新增
- **Barron's 批次 928 条 A 类虚构**：`check_vocab` 工具盲区——"（未出现在原文）"标注绕过工具检测，52篇全部存在。修复后 FAIL=0 ✅，WARN=72（B类）。详见 `docs/新书启动模板.md` 第5条。
- **check_vocab 标注盲区**：工具只检词频/例句前20字符/分档，不识别中文单元格。独立审查时必须 grep "（未出现在原文）"全文，有输出即 A 类虚构。

### 2026-08-29 新增
- **Room in the Ground 审查整改**：19 文件名偏移 + 5 跨章错植 + 7 cross-ref 联动修复 + 总览 8 处说话人反转。verify 235/235 ✅，FAIL=0。
- **AGENTS.md 第 10 条固化**：独立审查 SOP 五步法 + 完成报告硬要求 + 七类高发坑位。

### 历史教训
- Book Lovers 言情用逐句格式写到 35 篇崩坏重做
- 100 Great 两次大量生成后期衰减实证
- ~20 处"引语换新句、分析停旧句"在 verify_quotes 全绿下漏网
- NS 报告"101/101 ✅"重跑实为 108/109 含 1 FAIL
- 多 IDE 并行：git add -A 裹挟 / COLLABORATION.md 覆写 / amend 改写他实例 commit

## 工具链

| 工具 | 用途 |
|------|------|
| `extract_chapters.py` | epub → 逐章 text/ |
| `verify_quotes.py` | 引语逐字门禁 |
| `check_vocab.py` | 词汇表真实性（FAIL=0 才推进）|
| `check_entities.py` | 梗概实体一致性 |
| `check_chapter_quotes.py` | 逐章归属校验（凡有 text/ 必跑）|
| `audit_book.py` | 一键总账（commit 前必跑）|

## 推送策略
- commit 自由；push 仅限批次定稿/重大交付/明确指令
- **默认不推送，等用户指令统一 push**
- 多 IDE 并行时禁止 `git add -A` / `git add .`
