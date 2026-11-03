# ch17 对账（R3）

> R1 素读：`review/ch17/1-suread.json`（facts 8，锚点 8/8 命中 text/，start-end 一致）
> R2 机器层：`review/ch17/2-machine.json`（chapter.sh --json，verdict=ok；块 10 / 引语 10 / segments 11 / segment_miss 0）
> R4 人判：`review/ch17/4-verdict.md`（10/10 块逐块核对）

## 漏（R1 有、md 无）
- 无。R1 8 条（藏宝图瓶夹带捷径便条、追踪器 121 小时、沾血石头砸头、承认想杀 Henry、割臂摆同心圆、女神条款、刺死 Jade、Flint 取脑样本）全部由导航或块覆盖。

## 编（md 有、原文无）
- 无。Core、Obscuris、 Goddess 的条款、six years、exoskeleton 等均可回原文命中。

## 错（两边都有但不一致）
- 错 1【提示级】导航 `:10`「说出她才是 surfacewalker」：原文 `:203` Jade 说的是「Long ago, I was a citizen of this great city. We mined too much, took too much from the Void, and the Goddess is spiteful. She destroyed the city, but rather than kill us, she turned us into Void creatures… every six years, if we bring a sacrifice to her, she will grant us a human body to live with on the surface.」——**她没有自称 surfacewalker**；`/usr/bin/grep -n -i walker text/ch17_chapter_seventeen.txt` 仅 `:189`（Petra「Surfacewalkers aren't real. Jade always laughed at the idea of them.」）与 `:389`（Flint 说 Mr. Stone 要研究 surfacewalker 的大脑）两处。

## 结论
R3 三单：漏 0、编 0、错 1。漏 0、编 0、错 1（导航层措辞，提示级）。已列入修复指令。
