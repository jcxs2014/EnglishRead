# T1 自检（同会话）

抽样章：ch01（首章）、ch05（中位等距）、ch09（末章）——9 章 ≤16，按 §6.1 抽 1/3（至少 3 章），首末必含，其余等距取 ch05。

## 一、抽样章 suread 复验
- ch01：9/9 锚点全命中（suread.py --check EXIT=0）
- ch05：8/8 锚点全命中（suread.py --check EXIT=0）
- ch09：8/8 锚点全命中（suread.py --check EXIT=0）
- 回源抽查：ch01（考场/前馈网络/That's ok nobody does）、ch05（But I was wrong/青霉素/Brad Bird）、ch09（WarGames 台词/核冲突无赢家/only losing move）全部在 text/ 找到原句邻域。
- 引语块邻域抽查：ch01 原句1 与 text L4 逐字一致；ch05 原句3（图灵测试）与 text L37 逐字一致；ch09 原句4（We are not at war）与 text L28 逐字一致。

## 二、总览三篇全篇人判
- 三篇 45 条引语（金句 21 + 情感节点 19 + 概述 5）逐条回 text/ 校验支撑行：44 条脚本自动命中 + 概述方案层 1 条手工复核命中（"We are not at war with AI. We are raising it." 在 ch09 text 逐字存在）。
- 修复 3 处（提示/事实级，非阻断）：
  1. 00_金句精选.md ⑧ 为什么重要：原「它说明…AI 能产生人类从未用过的策略」把 AlphaStar 的成就安到 AlphaZero 引语上 → 改为「接近人类式的棋风而非蛮力；后文又以 AlphaStar…为例」。
  2. 00_金句精选.md ⑧ 呼应关系：原「与 ch04 的『AlphaGo Move 37』」→ 改为「与 ch08 的『AlphaGo Move 37』『ANI 窄任务惊喜』、ch05 的 AlphaStar 例子呼应」（Move 37 实际在 ch08）。
  3. ch05 md 结构列表第 6 条：原「资深律师 Schwartz 被罚」→ 改为「被法官要求说明为何不应受制裁」（原文为 ordered to show cause why he shouldn't be sanctioned）。

## 三、assertion_scan 六类预筛
- 候选共 237 行（输出 249 行含标题/合计）：①相对章号 21 行、②绝对断言 27 行、③年龄数字 169 行、⑤方向施受 8 行、④亲属身份 12 行、⑥场景方位无命中。
- ①②③⑥ 全量人读，④⑤ 全量（各 <20 行）人读。
- 结果：① 0 问题；② 2 处已修（见上 1、3）；③ 0 问题；④ 0 问题；⑤ 0 问题；⑥ 无命中。
- 复跑 gate.sh：EXIT=0，0 条阻断。

读了哪些候选行：assertion_scan 全部 237 行命中候选（六类合计）+ 三篇总览 45 条引语 + 3 个抽样章 suread 25 条事实及引语邻域。
