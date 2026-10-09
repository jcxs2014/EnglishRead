# Love, Theoretically（Ali Hazelwood）独立五步审查报告

- 审查日期：2026-10-09 ｜ 审查方：本会话实例（ZCode-Mac，用户同会话发起）
- 对象：notes/books/novels/love-theoretically-by-ali-hazelwood/（28 章 + 总览三篇 = 31 md）
- lane：**完整 lane**（epub 在位，epub 口径判定全部成立）

## 五步执行摘要

**a. 第 3 条门禁全量重跑**（全部重跑，不采信报告数字）：verify_quotes **184/184（100%）**、--full 整串取证 0；check_vocab **FAIL 0 / WARN 40**（40 条全为「基础档疑含超纲词」长度 ≥9 启发式——**提示型，只记不改**）；check_entities 0；corruption_scan FAIL 0；sweep_full 查无 0（🔶 跨标签拼接 2 条：ch04/ch12 既存项，各段逐字都在，**提示型**）。总览两文件 0 提取为 verify_quotes 已知盲区，由 d/e 步独立核验兜底。

**b. 逐章归属**：check_chapter_quotes 逐章跑 28 文件，**28/28「✅ 全部引语均归属正确章节」**；cliffhanger 边界抽查无跨章场景。

**c. 结构扫描**：audit_structure 结构缺陷 0/提示 0/映射 0；第二实现 check_struct_indep **28 md 缺陷 0**；check_overview_full A 整串命中 72/查无 0/拼接 0，B 章节标签**对 14 / 不符 1（修复后 0）**，H1 语义错配 0。

**d. 语义二审**：第二实现三脚本（check_analysis_indep / check_xref_indep / check_xref_zh）+ 带防幻觉条款与真实失败案例的只读子代理分批核对（批 1：ch01–14 全量 79 块；批 2：ch15–16；批 3：ch17–19；批 4：ch20–23 共 24 块；ch24–28 由审查方主会话逐块取证）。共发现并修复 **17 处缺陷**（明细见下）。

**e. 总览层事实核对**：三篇总览 93 条英文引语逐条对 epub 全书 flat 比对 **0 查无**；金句 24 条逐条说话人窗口核对；概述情节断言逐条回源（含章号偏移修复）；跨书污染自检 10 名全部排除（Millicent/Jell-O 为常见专名，本书 text/ 有原文支撑，非污染）。

## 缺陷清单与整改（17 处阻断型，全部修复并复跑清零）

| # | 位置 | 问题 | 类型 | 修法 |
|---|---|---|---|---|
| 1 | ch12:10/48/49/119 | "half brother" 译「同母异父」，原文 ch12:475 明证 Caroline 非 Jack 生母（同父异母） | A（事实矛盾） | 同母异父→同父异母 ×4 |
| 2 | ch07:63 | 关键词 "channel surfing" 不在该块引语内（原文 ch07:669 在截断之后） | B | 改引语内词 "Figure out who they are, what they want" |
| 3 | ch15:51 | 分析层引语 'Shh. It's okay'——"Shh" 在 ch15 全文 0 次（原文 ch15:489 为 "Hey. It's okay. You already apologized."，Jack 所说） | C（杜撰引语） | 改逐字原句 |
| 4 | ch18:50 | 「她一开始以为 J.J. 是真心，直到对方的前女友回来才被告知」与原文矛盾（"It was a fuzzy plan. But I said yes"——明知是假才答应；前女友是起因非揭穿者） | C | 按原文重写该段 |
| 5 | ch18:57 | 「听他不喜欢的音乐」无原文依据（原文仅 "I told myself Dream Theater was good"） | C | 改「说服自己也觉得 Dream Theater 好听」 |
| 6 | ch21:36 | 行内英文 "reserved for..." 非逐字（原文 "the one he reserves for..."） | C（改写） | 改逐字 |
| 7 | ch21:57 | 呼应章号 ch19 错（"Be gentle with me" 在文件 ch20） | 交叉引用 | ch19→ch20 |
| 8 | ch21:11/14/23 | 三处 "ch19 的首次亲密" 章号错（impedance = 文件 ch20） | 交叉引用 | ch19→ch20 ×3 |
| 9 | ch22:50 | 行内引语 "I don't want to be work" 全书查无（杜撰） | C | 改 ch20 逐字原句 |
| 10 | ch23:62/85 | "eleven-fifteenths" 译「十一分之十一」（=11/11，误），实为 11/15 | C（误译） | 十五分之十一 ×2 |
| 11 | ch24:58 | "ch19 那句 I risk being rejected" 章号错（在文件 ch20） | 交叉引用 | ch19→ch20 |
| 12 | ch24:65 | "呼应 ch19 的 two things can be true at once" 章号错（在文件 ch20） | 交叉引用 | ch19→ch20 |
| 13 | ch25 引语块 9 个 | 超言情 3–8 配额（写作期 gate 已修） | 结构 | 删减重排（本审查前已清零） |
| 14 | ch26:44 | "ch24 那个 very careful not to forget it" 章号错（在文件 ch25） | 交叉引用 | ch24→ch25 |
| 15 | ch27 导航 | 两句原句拼接「I want you. All. The. Fucking. Time.」（写作期 gate 已修） | 拼接 | 改逐字原句（本审查前已清零） |
| 16 | ch28:23 | "ch19 'scared to be seen'" 章号错 + 非逐字（原文 ch24 "how scared I am to be seen"） | 交叉引用 | ch19→ch24 + 逐字短语 |
| 17 | 00_概述:27 / 00_金句 / 00_情感节点 | ① 概述情节主线末四段章号偏移（24/25/26/27→23/24/25/26）② 金句 10 处出处/呼应章号混杂（文件号 vs 书内章号差 1，统一为文件号口径）③ 金句 #4 跨自然段拼接（ch06 text:136 与 "He slowly breaks into a smile." 为两个独立段落）→ 拆分 ④ 节点 4 个标题范围与引语实章不符 | C/结构 | 全部修复 |

**ch25/ch27/ch28 写作期门禁已修的 3 处（#13/#15 及 ch28 导航英文非逐字）在本审查 a 步复跑时已确认清零，计入本表仅为完整记录。**

## 提示型（只记不改）

- check_vocab WARN 40 条：全为「基础档疑含超纲词」启发式（candidate/impressed/overwhelmed/tartiflette/insurance 等），均为基础档正当词。
- sweep_full 🔶 跨标签拼接 2 条（ch04 "I've never hated anybody… I'm mild mannered" / ch12 "Never showing anyone who you really are." He）——各段逐字都在，省略号/跨段图式，verify_quotes 判 ✗ 但 sweep 判 🔶；属既存项，两处引语均真实存在于原文相邻段落。
- check_block_keywords 提示 1（配额口径）；verify_overview_quotes 对 "1." 编号格式提取 0 条（工具口径，已由独立 flat 核验 93/93 兜底）。

## 复验（修复后全量重跑）

- gate.sh：**正门 0 条阻断型，EXIT=0**；引语块覆盖度 28 md，阻断型 0 / 提示型 0
- check_xref_indep：英文证据报警 **0 处**（修复前 6）；check_xref_zh：错 0
- check_analysis_indep：未命中 0（修复前 1）；🟠 拼接/改写待人判 2 条（ch03:36 "Nickelback vs Coachella、Laughing Cow vs pule cheese"——四词均逐字在 ch03 text，"vs"为分析连接词，**正当列举，提示型**）
- check_overview_full：整串命中 72/查无 0/**标注不符 0**/H1 错配 0
- corruption_scan（每次批量修复后必跑）：FAIL 0
- 独立 flat 核验：总览三篇 93 条英文引语 **0 查无**

## 结论

**五步审查完整执行，17 处阻断型缺陷全部修复并复跑清零，复验 14 项全绿。** 已知局限：本审查为同会话审查（审查方=执行方），说话人/事实核对已按「换检查路径」（第二实现脚本 + 只读子代理 + 人工回源取证）执行，子代理报告均经审查方逐条复核后采信；如需异实例复核，可另行指派。未 push（等用户指令）。
