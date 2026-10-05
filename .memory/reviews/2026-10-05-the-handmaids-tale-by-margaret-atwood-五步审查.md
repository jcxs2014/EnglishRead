# The Handmaid's Tale 五步审查报告（2026-10-05）

- **审查方**：ZCode-Mac（同会话审查——执行方与审查方同一实例，a–e 完整执行、未自我豁免；已知局限见文末）
- **对象**：`notes/books/novels/the-handmaids-tale-by-margaret-atwood/`（47 章正文 + 总览三篇 = 50 md）
- **触发**：用户于完工当日发起（合规路径）
- **整改 commit**：`3bed4d7ae`（d 步机械 13 处）→ `dc12699ca`（语义二审 93 处）
- **原始逐行输出**：`.memory/raw-gates/the-handmaids-tale-by-margaret-atwood/`（审查 a–e 步 7 件 + 完工期 30 件）

## a｜第 3 条门禁全量重跑（全部重跑，不信此前数字）

verify_quotes **407/407**（100%，干净 49/49）· --full 整串取证 0 偏差 · check_vocab **830 行 FAIL 0**（WARN 64 逐条看过：长度启发式＋例句不含词头，均正当/质量级，只记）· check_entities 0 · corruption_scan 0 · sweep_full 369 命中/0 查无 · check_short_quotes 1 条兜底全中 · 块覆盖 47 文件全入校验 · nav 层 ❌0。

**🔶 3 条跨标签拼接（人判通道）**：ch38 原句 3/8、ch47 原句 4——均为省略号引语，逐段核验**各段逐字、省略段连续**（ch38:8 跳过一句、ch47:4 跳过两句连续叙述），判定合法，不改。

## b｜逐章归属

- 标准工具逐章模式：47/47 章**全部 X/X in 本章 text**。
- **第二实现**（独立解析器：剥引号→flat→按 … 切段→本章 text 逐段匹配）：373 引语行，查无 **0**；省略号引语 4 条（ch38×2/ch44/ch47）各段逐字且省略段连续，合法。

## c｜结构扫描（双实现）

audit_structure 缺陷 0／check_struct_indep（第二实现）缺陷 0／check_quote_blocks 前缀·编号·孤儿·泄漏全 ✓／H1 三方交叉核对（文件号↔H1 编号↔语义）47 文件错配 0／check_nav_layer ❌0／check_block_keywords 问题 0。

## d｜语义二审

**机械子项（第二实现）**：
- `check_xref_indep`：初报 1 条（ch10:44「valid objects 的区分术」→ch09）。**定性过程留痕**：先疑假红（工具把中文标签并入证据串），grep ch09 真值后**证实为真错章**（valid objects 在 ch06 原句 7）——「先读行复核」的读行必须落到 grep，不能停在语气判断。已改 ch09→ch06。复跑报警 0。
- `check_analysis_indep`：初轮 5 条＋复轮 ❌1＋⚠️6 = **12 处分析层非逐字**（Anglo-Saxon tomb carving／faces like burning paper／positions of power 漏 such／漏 always／blow up 语形／MAD 术语／fade 漏 finally×2／reproach and necessity 压缩×2／willing hearts 漏 duties／pain or pleasure 漏 extreme×2），全部改回逐字或改纯中文。复跑 365 片段全逐字。
- `check_xref_zh` 248 命中 0 错 · `audit_numbers` 4 ⚪ 年龄类逐条回源核实（三十三岁/二十岁/十四岁×2 均有据）· `check_anchor` 凭空造词 0 · `check_crossref` 0 报警。

**子代理语义二审（5 批并行：4 批正文 12+12+12+11 文件＋1 批总览；任务书附 4 类历史失败案例＋防幻觉条款）**：
- **投毒测试**：批 A 埋 1 条假线索（ch05 原句 8 说话人），代理独立核实后如实报「提示不成立」并给出完整取证链——未顺从假线索编造缺陷。
- 报警合计：**阻断型 22**、提示型 18、存疑 15（存疑逐条复核后或整改或记录，未凑数）。子代理报告逐条回源复核后才改（未照单全改）。

## e｜总览层事实核对

- **说话人窗口**：金句 25＋节点 10 共 35 条引语逐条定位本章原文 ±200 字符窗口（存档 `2026-10-05-审查e步-说话人窗口.txt`），说话人均符（Aunt Lydia／Commander／Ofglen／新 Ofglen／Luke／Serena Joy／Cora 等）。
- **事实断言回源**：概述四幕＋主题＋人物弧光的四类断言逐条 grep（两位 Fred、Serena Joy 恶意虚构、约三十盘磁带、2195、tail 双关、Ofglen 自缢、真名交割等全中）；发现并整改 2 处（「Harry」无源断言删除、Mayday 地点错挂 ch27 橱窗→散步途中）。
- **跨书污染自检**：Offred/Serena Joy/Pieixoto/Nunavit 全库无他书命中；「Gilead」他书命中均为圣经习语 Balm in Gilead，非泄漏。

## 缺陷清单（整改 106 处 = 机械 13 + 语义 93）

| # | 类别 | 数量 | 代表例 |
|---|---|---|---|
| 1 | **跨章引用错章** | 20 | ch10「valid objects」ch09→ch06；ch14 眨眼 ch08→ch04；ch17/18/23 触摸饥渴 ch05→ch02（3）；ch21 酵母 ch12→ch08；ch22 sororize ch09→ch02；ch25 whim ch19→ch05；ch28 hold ch26→ch14；ch30 containers ch12→ch17；ch31 黑罐 ch12→ch08；ch34 水仙 ch25→ch17；ch35 ghosts ch18→ch30；ch39 怪物 ch29→ch24；ch44 choose ch41→本章；ch45 signed up ch11→ch16；ch46 宝藏 ch14→ch24；金句①⑦⑫⑱ 呼应章号 4 处 |
| 2 | **自指式跨章引用**（「与 chNN 连读」的 NN＝当前章，证据串在本章故机检放行＝**门禁盲区**） | 9 | ch28×3、ch30×2、ch31、ch32、ch36×2 |
| 3 | **部名映射系统偏差** | 5 | ch20–23 误标 IX: Night（实为 VIII: Birth Day）、ch24 误标 X: Soul Scrolls 起始（实为 IX: Night 单章）——根因：写作期任务表凭记忆转录 spine，错一格；日志映射同步修正 |
| 4 | **计数断言错** | 12 | ch04 三句五动作、ch10 五短句、ch11 三疑问、ch27 No 两字母、ch28 八词、ch32 三词、ch36 三问句、ch40 三句俏皮话＋三句 I would like、ch41 五个 I wish、ch45 十个 I'll |
| 5 | **语义反转/主体错配** | 3 | ch27「没法不信」→「不敢信」（与同块分析自相矛盾）；ch41「月经没来」→（卫生巾按月发放＝月经来了）；ch09 Rita 自称「孩子」被误读为使女等级 |
| 6 | **无源细节/凭空意象** | 5 | ch13「汽车展」、ch18「三百年墓石」、ch24「喷嚏」（实为口哨）、ch23 Valance 误注「四联胎」、概述「Harry」 |
| 7 | **顺序/口径/归属** | 6 | ch17 Bullshit 顺序、ch22 hasn't yet 口径、ch46「杀妻」→杀 Serena、ch44「说漏」→试探、ch38「全书前半」→后段、ch47 悬空指引 |
| 8 | **引点/拼写/语病** | 8 | ch04 Must→May、ch08 do not、ch12 supposedly、ch10 语病、ch11 sugestión、ch47 Serene Joy、ch33「she 的」、金句⑱ 人物归属措辞 |

## 提示型（只记不改，逐条看过）

🔶 省略号引语 4 处（合法）· WARN 64（长度启发式/例句不含词头，正当或质量级）· audit_numbers 4 ⚪（已核）· Nolite 跨章命中（有意标首现章）· ch16 大写排版解读（章首惯例，解读已加限定语前为裸断言——已随 d 步顺手限定）· 节点四「为庆幸感到恐惧」解读性添加（已改为贴原文转述）· 概述「船票」「别告诉丈夫」（已改泛化/删除）· 概述四幕范围标注（已改并注明穿插）。

## 复验（整改后）

corruption_scan 0 · verify_quotes **407/407** · sweep_full 0 查无（🔶3 合法省略号）· check_analysis_indep 365 片段全逐字 · check_xref_indep 0 报警 · nav ❌0 · block_keywords 0 · audit_structure 0 · struct_indep 0 · 总览 35/35＋标签 35/0＋H1 0 · vocab FAIL 0 · entities 0 · **gate.sh 0 阻断 exit 0**。

## 同会话审查的已知局限（如实标注）

1. 子代理语义二审以「引语↔分析逐对」为主，对**全章通读级**的语气/节奏/隐喻一致性覆盖有限；
2. 说话人核对覆盖总览 35 条＋子代理抽查的对话块，正文 373 块未逐块人工开窗；
3. 部名映射的根因（任务表转录错误）提示同类「系统性一格偏移」可能存在于其他凭记忆转录的结构断言——本次仅修正了被点名处。
如需最高保证，建议另派异实例复核（尤其第 3 点）。
