# T1 自检判决 · the-intrigue-by-silvia-moreno-garcia（2026-10-25）

**抽样章（先定后读）：ch01 / ch12 / ch24（epilogue）。理由：ceil(24/8)=3，首章必含；ch12 是全书第一次「杀人落地」的结构枢纽（毒酒误杀）；ch24 是 epilogue（时间线跳跃最大、跨章指认最密），与末章重合。**

- **T1 为同会话自检**，非独立审查；有效率未测量。

## ① 素读清单复验（suread --check）
- ch01：8/8 锚点全命中（.memory/tmp/ch01-facts.txt）
- ch12：12/12（.memory/tmp/intrigue-ch12-facts.txt）
- ch24：8/8（.memory/tmp/intrigue-ch24-facts.txt）

## ② 总览三篇全篇人判（六类逐条回 text/）
- 引语层：overview.py quotes **107/107（100%）**、full EXIT=0（24 章全覆盖）、labels EXIT=0（0 待人判）。
- 重复收录：金句 25 条唯一、情感节点 32 条唯一（Counter 核对，0 重复；金句与节点的 14 处跨文件重叠均为模板设计的有编号呼应，合法结构意图）。
- 中文叙述断言（六类）逐条回源：生父死于 1942-03-03（ch11 "Buried on March third, 1942"）；四个化名（ch05）；八万七（ch09 "eighty-seven thousand pesos"）；藏信一年（ch11）；两千比索（ch11）；两万比索（ch19）；745-631（ch17）；三个儿子（ch01 "Three fuming, thirtysomething sons"）；提前三天（ch09 "back in three days"）；三周（ch08）；Cándido 目击+侦探回电（ch19）；Lulú 送三箱文件+Fito 吃玉米饼被解雇（ch21）；谵妄三日/父亲手杖/墙上两颗子弹（ch24）；周四起车（ch20）；「秘密订婚三年」（ch14）——**全部属实，0 阻断**。
- 说话人核验（窗口法）：ch23「你不能丢下我一个人！」＝Perla（上下文 "panic in her face"）；ch21「祝你好运」＝Inés（"she replied coolly"）——归属正确。

## ③ assertion_scan 六类预筛（t1-candidates.txt 共 463 行）
- ①相对章号 8 行：逐条回源（ch19「不行/再也不会」「两遍+呕吐」「车里见提议」；ch12「窗口看见」；ch13「shoves Encarnación」；ch01 脸红句；ch10「Las Tunas 下一章才去」）——全命中。
- ②绝对断言 94 行／③年龄数字 198 行（抽 20）／④亲属身份 109 行（全读）／⑤方向施受 27 行／⑥场景方位 13 行：人读高信号行约 60 行，**未发现凭空断言**；唯一存疑项「ch13 姨妈三十年前对妹妹喊过同一句」已回源证实（ch13:562 原句存在）。

## ④ 抽样章引语邻域人判（每章 2 块回源邻域）
- ch01 原句 10（Money was what mattered）：邻域「hideous hag」上文吻合，估值语境正确。
- ch12 原句 11（He drank it）：邻域「drag her out into the hallway」吻合，凶案现场语序正确。
- ch24 原句 7（"Bartolo," she replied smoothly）：邻域「You had a tail…You won't guess who it was」吻合，识破跟踪语境正确。

## 结论
- **阻断型：0 条**（无需 T2）。提示型若干（块数偏离建议区间的 ⚠️、总览行内引语 28 处提示）均已记录、不判红。
- 读了哪些候选行：t1-candidates.txt 全文 463 行过目；①全读（8）、④全读（109）、⑤⑥全读（40）、③抽 20、②抽高信号约 30——共约 210 行人读。
- 整书 gate.sh EXIT=0（收口于 commit 859f76401）。
