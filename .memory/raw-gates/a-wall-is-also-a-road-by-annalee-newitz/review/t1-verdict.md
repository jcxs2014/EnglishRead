# T1 自检 verdict · a-wall-is-also-a-road-by-annalee-newitz（2026-11-02，同会话自检）

抽样章（全书 48 章 >40 ⇒ 1/5 且 ≥10 章；首末必含，其余等距）：
**ch01, ch06, ch11, ch16, ch21, ch26, ch31, ch36, ch41, ch46, ch48（共 11 章）**
理由：48/5=9.6 ⇒ 取 11 章覆盖五部（I:1,6 / II:11,16 / III:21,26 / IV:31,36 / V:41,46）+ 作者注（48）。

## 1. 总览三篇全篇人判（六类断言逐条回 text/）

- 概述「七十万颗星盘行星」→ ch02 text「seven hundred thousand planets」✓
- 概述「Pompeii 的墙沉入灰烬之海」→ ch36「the gray radioactive sea」✓
- 概述「文化与科学平权」→ ch47「culture and science would carry equal weight」✓
- 概述「Wainscot 唯一留在 Old Memory」→ ch47「the only person from their original covert action group who had decided to remain」✓（原文自带 only，断言有据）
- 金句 25 句全部经 gen_overview 从已过门禁章节块抽取（零手打英文）；overview.py quotes 96/96 ✅、labels 51/51 ✅
- 金句唯一数自查（Counter）：25 句无重复收录；圈码 ①–㉕ 各一次
- 情感节点 10 节点引语均出自已核章块；「第一千次确认」→ ch01「For the thousandth time」✓
- 中文叙述断言抽查：Murtis 十五年奴隶（ch17「a slave for fifteen years」✓）、Mactar 迦太基西（ch13「west of Carthage」✓）、四颗行星（ch47「four planets in Skiff」✓）

## 2. assertion_scan 六类预筛（t1-candidates.txt 共 558 行）

- ①相对章号 50 行：全读。相对指认（上一章/下一章/本章）与写作期素读记录一致；抽 2 处回原文复核：
  ch02:37「上一章只用预感打掩护」→ ch01「I have a hunch…」✓；ch18:79「Spring→几乎入夏→Harvest」→ ch17「It's almost summer now」+ ch18「set for Harvest」✓
- ②绝对断言 179 行 + ③年龄数字 262 行：全量模式扫描；「唯一/第一次/最高」类命中均为评析修辞（从宽只记），无「可数排名类」断言需改
- ④亲属身份 4 行：Julia Felix 之夫/之母、Flavia 之夫 → 均有 ch13/ch24 text 支撑 ✓
- ⑤方向施受 44 行：抽 8 行（ch17/29/36/41/46 高风险章）无施受倒置 ✓
- ⑥场景方位 5 行：全读，无方位断言缺陷 ✓

## 3. 改过的数字/事实回灌总览

- 生产期修改均为结构/词表层（块序、词表例句、拼接修复），无数字/亲属/因果类事实修改 ⇒ 无需回灌；grep 复核总览三篇无「resiliency/priceless/glamorous/refuge（单数）」等已删词形 ✓

## 4. 抽样章复用素读清单

- 11 个抽样章全部有 production/chNN-suread.json（锚点命中均 8/8 或 7/7）；抽 ch01/ch29/ch44 各 2 条事实回源复核 ✓
- 重点读引语块邻域：ch01（行 69–99 交锋段）、ch29（浴池坦白段）、ch44（答辩爆发段）——块序、块界与原文事件序一致

## 结论

- 抽样 11 章 + 总览三篇 + 六类预筛：**阻断 0 条**；评析修辞类「唯一/最」记录在案（从宽）
- 缺陷密度 0/11 < 0.2 ⇒ 可停；无需进 T2
- ⚠️ 本 T1 为同会话自检，不构成「已通过审查」；T3 深审未做（待用户发起）
