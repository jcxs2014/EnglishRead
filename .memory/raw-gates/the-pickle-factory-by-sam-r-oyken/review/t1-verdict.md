抽样章（先定后读，70/5=14，实取 15）：ch01, ch06, ch11, ch16, ch21, ch26, ch31, ch36, ch41, ch46, ch51, ch56, ch61, ch66, ch70（首末必含，其余约等距；ch70=DIGESTIF 为全书最后一件）

## T1 自检 + T2 断言全扫（the-pickle-factory-by-sam-r-oyken，2026-10-29，审查方=自检）

### 一、阻断型（4 处，已修）

1. 00_概述.md:53-54 | BUTTONFLY 弧光「起点/落点」两行为空 | 补 ch13#7「I guess you might say I'm the Ghost of CIA Past…」/ ch68#3「…there hasn't been a Pickle Factory… But there will be now…」| text/ch13、ch68
2. 00_概述.md:38 | KRAY 弧光起点误用 ch05#1（该句写的是 Wacker 入场「He waddled into the conference room…」）| 改 ch05#4「In a far corner a fit, dark-haired, Mediterranean-looking man in his mid-forties stood up…」| text/ch05 第 4 块
3. 00_金句精选.md:215 | 「全书最后一句」错 | ch69 之后仍有 ch70 DIGESTIF | 改「主线叙述的最后一段」| text/ch70 存在
4. 00_概述.md:16 / 00_情感节点.md:62 | 「接头人不是迟到就是失约」「每个站点都以荒诞收场」错 | ch40 明写 MYPLACEORYOURS「right on time」| 改「常常迟到或失约（也有准时赴约的）」「多数站点以荒诞收场」| text/ch40

### 二、7c 类可数/排名断言（9 处，已修）

5. ch02.md:32 「唯一反复叠加的数量词」→ 删「唯一」| text/ch02 声明段
6. ch16.md:90 「KRAY 第一次主动帮 Cooper 撬动情报」→「主动帮 Cooper 撬动情报的一步」| text/ch16
7. ch58.md:10 「全书…第一次翻面」→「一次…一次翻面」| text/ch58
8. 00_金句.md:171 「全书第一次有人正面评价 KRAY」→「全书少有的正面评价」| text/ch18/55
9. 00_金句.md:178 「唯一机会」→「关键机会」| text/ch57
10. 00_金句.md:185 「全书唯一一次明确说出」→「少有的明确道德选择」| text/ch57
11. 00_概述.md:49 「全书最清醒的人」→「少有的清醒旁观者」| text/ch09/18/69
12. 00_情感节点.md:86 「全书唯一一次明确的道德选择」→「少有的」| text/ch57
13. ch36 关键词 plywood（在上一句，不在本块引语）→ ventilation holes；ch65 空「常用」档 → 删表头（gate 已抓，属机器层整改，一并记账）

### 三、T2 断言全扫（候选 607 行，实读 607）

①相对章号 16 / ②绝对断言 68 / ③年龄数字 395（「岁」类 16 条全部回 text 核中）/ ④亲属身份 9 / ⑤方向施受 110 / ⑥场景方位 9，全量读完。
- 保留（提示，不修）：ch53「Wacker 摊出 FBI 在 Ballston 盯梢点拍下的照片」把两句原文合并（Comfort Inn in Ballston + FBI stakeout point），原文未明说两者同一地点，属可接受合并推断。
- 保留（评析类）：「本章唯一」「全章唯一一处」约 20 处，均单章内可数且与原文相符，按「可数排名必改、评析从宽」留。

### 四、素读复用

15 章 `suread.py --check` 锚点 0 失败（6–9 条/章）；抽 ch11/ch46/ch61 事实回源，语义一致。

### 五、回灌与复验

本轮章节修复不涉及总览中的年龄/年份/数量/亲属/谁做什么，无需回灌（grep plywood/Dunning 于 00_* 为空）。修复后 ch02/ch16/ch58 复跑 chapter.sh rc=0；gate 重跑 EXIT=0，总览引文 89/89。

结论：13 处整改（阻断 4 + 7c 类 9）；T2 全量覆盖后无新增阻断；T1 为同会话自检。
