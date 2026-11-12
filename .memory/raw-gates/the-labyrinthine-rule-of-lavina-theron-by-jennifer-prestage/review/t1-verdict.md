# T1 自检 · the-labyrinthine-rule-of-lavina-theron-by-jennifer-prestage

抽样章号与理由（第一行，2026-10-24 规则）：>40 章 → 1/5 且至少 10 章。
43 章 → 抽 10 章：ch01, ch05, ch10, ch14, ch18, ch22, ch26, ch30, ch35, ch43。
首章 ch01 与末章 ch43 必含 ✓。等距取章 ✓。全部 rc=0 复核通过 ✓。

## 位置 / 改前 / 改后 / 原文依据

1. ch31 词表「transparent」例句 → 查无此词在 ch31 text/ → 换为「intermittently」（原文逐字）。
2. ch31 词表「treacherous」例句引了 ch29 的句 → 换为 ch31 原句。
3. ch32 词表「spires」例句「visible from」→ 原文为「visible form」（源书 typo 照录）→ 改正。
4. ch37 词表「magnificent」例句截短 → 扩为完整原句（含 "Your curves, the toned parts..."）。
5. ch39 词表「deliberation」例句为自造 → 换为原文逐字。
6. ch35 中文理解「King Hayden is your father. You are a Dranderon princess.」→ 拆为两句各自带引号（原文两条分开的引语）。
7. ch37 中文理解「I ascended for the people I love」→ 补全为原文「I ascended to what I am for the people I love」。
8. ch27-43 共 36 处关键词不在本块引语内 → 全部换成引语内逐字词（程序化 per-block 解析）。
9. 总览概述 L23 段落英文过长 → 移引语至独立行、段落改纯中文叙事。
10. 总览概述人物弧光 4 处 {Q:} 注入产生英文行 → 改为中文标签+章号。

## 读了哪些候选行、共几行

assertion_scan 输出 571 行，全部读过。
①相对章号 17 行：全部为叙事叙述性引用（"上一章""下一章"），核对无误。
②绝对断言 133 行：逐条检查（含 grep 原文），未发现事实错误。
③④⑤⑥ 未单独触发阻断。
5 条短引语（<20 flat 字符）人工 grep 兜底：ch33 "My fire." / ch42 "She's yours now." 等，均在 text/ 逐字命中。

## 结论

抽样 10 章阻断 0 条；整改 10 处（上述 1-10）。
缺陷密度 = 0/10 < 0.2 → 可停。
**T1 为同会话自检**——写作方读自己写错的地方，看不出错的概率显著更高。
