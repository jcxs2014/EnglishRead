---
name: englishread-memory-index
description: EnglishRead 工作区跨会话记忆索引
metadata:
  type: user
---

# EnglishRead 记忆索引

> 本文件 = **记忆索引**（不包含规则内容，规则见根 AGENTS.md 和 docs/新书启动模板.md）。
> 新会话读取顺序：system-reminder → docs/新书启动模板.md → 根 AGENTS.md。

## 架构说明：为什么规则留在根 AGENTS.md 而不是本文件

> **结论先行**：执行规则必须留在根 AGENTS.md。本文件只承担"记忆索引"角色。

**加载机制**：根 AGENTS.md 通过 system-reminder 被加载到每个会话上下文（ZCode harness 固定行为，不可配置）。`.memory/AGENTS.md` 不在这个加载路径上，需要主动 Read 才能看到。把"精读格式/门禁三件套/引语逐字规则"搬到 memory 意味着新会话开工时这些执行规则不在上下文里，等于丢失。

**三个文件的分工**：
- **根 AGENTS.md** = 执行规则（"必须怎么做"）—— 格式、门禁、引语规则、git 策略。每次作业都须遵守，必须被自动加载
- **docs/新书启动模板.md** = 新书开工入口（执行规则速查 + 历史坑表）—— 通过 system-reminder 摘要或用户指令加载
- **.memory/AGENTS.md** = 记忆索引（本文件，"之前发生过什么"）—— 各书完工记录、经验教训、跨书互证坑位、工具盲区速查。跨会话积累，按需主动 Read

**长度不是迁移理由**：根 AGENTS.md 的膨胀靠去重收口解决（已收敛 `00_*.md` 重复、9f/10d 重复），不靠搬走内容。

**引用完整性**：模板、脚本、协作板大量引用"AGENTS.md 第 9/10 条"——迁移会破坏交叉引用链。

**怎么判断一条信息该放哪**：
- 如果删掉它，新会话开工会不知道怎么干活 → 放根 AGENTS.md
- 如果删掉它，只是少了"上次怎么踩坑"的参考 → 放本文件



## 核心规则文档

| 文档 | 位置 | 用途 |
|------|------|------|
| 精读执行规则 | `AGENTS.md`（根目录） | 完整执行规则（格式/门禁/工具链/git 策略） |
| **新书启动模板** | `docs/新书启动模板.md` | **每本新书开工前必读**，含执行规则速查 + 历史坑表 |
| 协作消息板 | `COLLABORATION.md` | 跨 IDE 实时消息（newest first） |

## 重要记忆（按时间倒序）

### 2026-09-10 新增

- **Don't Make Me Laugh（Julia Raeside）非虚构 #MeToo 幽默回忆录**：42 章（ch01-41 + Epilogue）+ 总览三篇（概述/金句精选28句/情感节点9节点）。**体裁提示：用户拍板用非虚构论述格式写小说**（与 it-comes-from-the-river 同类已知偏差，永久保留）。verify_quotes 388/388 ✅ / vocab 1058 词条 FAIL=0 WARN=0 / entities 0 / 逐章 388/388（100%）。**关键经验**：①论证结构证据链表格第三列含 ≥8 拉丁字符即被当例句判 FAIL（证据链单元格必须纯中文）；②总览候选句凭记忆 short-hand 多次 MISS（必须从已验证的章节文件原文复制）；③说话人窗口核验抓到 ch40 "I don't know" 命中 usher 台词；④生成期混入西里尔/越语/法语等珍稀语料（已全清）。16 commits 未 push。
- **Cabin Fever（Riley Parker）言情中篇 established couple**：7 章 + 概述一篇（含10 金句+7 节点+6 表达）。独立五步审查零缺陷。短篇结构，9 commits 未 push。
- **Burn for You（Bridie Charles）言情长篇 enemies-to-lovers**：43 章 + Epilogue + 总览三篇（概述/金句精选30句/情感节点10节点）。独立五步审查通过。
- **Adrift（Ellie Pond）言情长篇**：47 章 + 总览三篇。独立五步审查通过。文本/提取件零偏移。
- **How to Tell a True Story（Tricia Springstubb）middle-grade 当代小说**：58 章 + 总览三篇（概述/金句精选25句/情感节点10节点）。独立五步审查通过。LoC Cataloguing "LCGPT: Novels" 是体裁判断的权威信号。
- **Lady of The Lake（C.N. Crawford & Alex Rivers）奇幻言情**：61 章正文（ch02-ch62 = Chapter 1-61）+ 总览三篇。ch01=A Recap / ch63=Timeline / ch64=Sample 不精读。独立五步审查通过（22 commits 未 push）。总览引语跨叙述标签（如 "I understand why you lied," he says softly.）须逐字含标签文本，否则 flat 匹配失败。
- **Meet Me at Midnight（Brianna Bourne）YA contemporary romance + magical realism**：48 章（Chapter One → Chapter Forty-Eight）+ 总览三篇（概述/金句精选25句/情感节点12节点）。独立五步审查通过。
- **Pretty Bossy（Arini Vlotman）言情长篇 enemies-to-lovers + fake relationship**：22 章（ch01-ch22 = Chapter 1-21 + Epilogue）+ 总览三篇（概述/金句精选25句/情感节点10节点）。独立五步审查通过（11 commits 未 push）。**教训**：词汇表例句必须逐章 grep 验证，不可凭印象编写；总览引语格式（**关键引语：**）不在 verify_overview_quotes 口径内，须人工 grep 兜底。
- **The Bucket List（Ali Parker）言情长篇 contemporary romance**：43 章 + 总览三篇（Opencode-Mac 等多 IDE 接力）。25 commits 未 push。
- **The Sweet Chef and the Corporate Queen（Susanne Ash）言情长篇（age gap, forced proximity）**：13 章（ch01-ch12 + Epilogue）+ 总览三篇（概述/金句精选25句/情感节点9节点）。独立五步审查通过（9 commits 未 push）。**教训**：导航栏英文 trope 名称（Grumpy/Sunshine/Forced Proximity/Truth-Teller）须改中文，否则触发 check_entities 误报。
- **根目录 10 本新 epub 归档（260908 第二批）**：用户拍板"抽检内容后再分类"，按 OPF spine 取首章正文（混淆文件名 fallback 到扫 HTML 找 >800 字符非 boilerplate 页）。最终格局：**novels 61 / mystery-thriller 21 / non-fiction 18 / short-story-anthologies 20 = 120 本**。**关键判断**：①不要凭书名/作者印象分类；②Praise/营销文案含修辞夸张（Don't Make Me Laugh 标 "thriller" 是修辞非体裁）；③opus epub 用混淆文件名（c9.xhtml/cM.xhtml 等），须扫 HTML fallback。

### 2026-09-07 新增

- **The Wrong Sister（Claire Douglas）心理悬疑惊悚**：53 章（ch00 Prologue + ch01-51 + ch12b Interlude）+ 总览三篇（CommandCode-Mac）。独立五步审查放行。verify 272/274 ✅ / vocab 460 词条 FAIL=6（ch12b 工具盲区）/ entities 0 / 结构扫描 53/53。核心揭示：Bonnie=Holly（30 年前被绑架婴儿）/ Alice 是 chimera（嵌合体两套 DNA）/ Alice 杀害 Kyle（轮胎扳手）/ Tasha 选择沉默（"turning a blind eye"）。19 commits 未 push。
- **Falling into Place（Allison Ashley）言情长篇 contemporary romance**：34 章（Carly/Brooks 交替 + ch33 短信体 + ch34 Epilogue）+ 3 篇总览（Opencode-Mac）。独立五步审查两轮放行。verify 258/258 ✅ / vocab 732 词条 0/0 / entities 0 / overview 21/21。核心主题：稳定 vs 心动、说 vs 躲、翻篇 vs 传承。15 commits 未 push。
- **⚠️ Read 输出异物混入（本轮头号教训）**：ch23 Read 中段混入办公室/frames/centerfold/pizza 整段、ch33 Read 混入 ch31 pitch 段（franchise/Nashville/Riza），文件 grep 实测查无——Read 输出≠文件实况，凡写必先 grep，记忆与单次读取皆不可信。ch19 "bailed"/"fluke"亦为记忆漂移虚构。
- **verify fail-closed**：epub 路径拼错时报全 0/X——先查路径，不怀疑文件。
- **分析层数字断言**：年龄（三十三岁×4）、时长（九个月）、章数（九章/十九章）凡无原文支撑一律 soften/删除；推算的不写。
- **gag 计数链**：跨章"见下/下章见/over/哈哈"计数梗后期失控（三文件约 40 处），行级正则批量清理（禁 re.S 跨块）。

### 2026-09-06 新增

- **⚠️ 工具口径盲区速查（2026-09-05/06 十余本书交叉固化，详见 docs/新书启动模板.md 坑表新增节）**：
  1. verify_quotes/check_chapter_quotes 对无编号言情格式（`> "..."`）抽到 0/0——言情书须自备 flat 分段脚本
  2. <20 flat 字符短引语被工具静默跳过（Perfection/Forest of Scars/Rookie Season 三书互证）——grep 行数 vs 提取数不一致即信号
  3. check_vocab 撇号缩写词条（I've/he'd）误报 A类虚构；例句起点避开页码污染点；词条头必须本章原词形（torn≠tore）
  4. 跨标签拼接是 7 本书互证的最高频引语缺陷——多段台词严禁 `...` 连接
  5. verify_overview_quotes 只认行首圈数字且 CIRCLED 止于㉕——金句 ≤25 条/文件，其余人工脚本兜底
  6. 分析层 cross-ref 章号/数字断言/说话人是三道门禁的共同盲区——写前当场 grep 所指章
- **Up in Molten Lights（E.B. Golden）奇幻言情双 POV**：79 章 + 总览三篇（2026-09-06，ZCode-Mac）。流程=质量评估→修复不重做（尾部 ch49-54 词汇崩坏重写+引语 3 处）→续写 25 章 8 批→五步审查 12 处整改→词汇表全库清理（跨篇 59 处+移档+去重 68 行，FAIL=0 WARN=0）。终态引语 1006/1006（引号分段口径）。新工具盲区：check_vocab 撇号词条误报 A类、verify_quotes 对无编号言情格式抽不到、verify_overview 只认行首圈数字。约 35 commits 未 push。
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
| `verify_quotes.py` | 引语逐字门禁（支持言情无编号格式；短引语提示人工 grep）|
| `check_vocab.py` | 词汇表真实性（FAIL=0 才推进）|
| `check_entities.py` | 梗概实体一致性 |
| `check_chapter_quotes.py` | 逐章归属校验（凡有 text/ 必跑；`--book-dir` 全书扫描）|
| `verify_overview_quotes.py` | 总览引文门禁（00*.md 独立盲区）|
| `check_crossref.py` | 分析层 chNN "引语" 引用校验（2026-09-06 新增）|
| `audit_book.py` | 一键总账（commit 前必跑；不含 crossref）|

各工具口径盲区速查见根 AGENTS.md 工具表下方"工具已知盲区速查"。

## 推送策略
- commit 自由；push 仅限批次定稿/重大交付/明确指令
- **默认不推送，等用户指令统一 push**
- 多 IDE 并行时禁止 `git add -A` / `git add .`
