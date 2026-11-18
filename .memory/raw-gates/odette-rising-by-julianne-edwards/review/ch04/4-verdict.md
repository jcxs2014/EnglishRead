# 4-verdict · ch04 the blue door（T3 深审 2026-11-18）

R1：子代理盲读 8/8（区间验证 0 失败）。R2：chapter.sh --json rc=0。R3：漏 1（轻微，提示不修）/ 编 0 / 错 0。

## 逐块判定（5 块）

| 块 | 断言 | 证据（text/ch04_chapter_4.txt） | 结论 | 档位 |
|---|---|---|---|---|
| 原句1 Merry | 施事：点灯生火搬补给＝Merry；「有母亲在巴黎」＝原文 | "It had not occurred to her that he might belong to anyone, that he might have a mother, in Paris." | 对应 | ✅ |
| 原句2 pulped | 说话人＝Merry；受创＝父亲；「pulped」逐字 | "He was pulped, head swollen. I had to lift him into the carriage" | 对应 | ✅ |
| 原句3 kitchen table | 施事：抬桌＝Merry+Dendron；剪衣＝Dendron；『Shhh』＝Dendron | "We put him on the table, and she inspected him... She went, ‘Shhh, shhh.’" | 对应 | ✅ |
| 原句4 brown | 时间轴翻转＝叙述层（她的自我修正） | "If she had been asked to choose a color that represented him, she would have said brown. But that was before." | 对应 | ✅ |
| 原句5 anger | 施事：发怒＝她；对象＝「知道得比她多的人」 | "With Merry, with her father, with everyone who knew more than her." | 对应 | ✅ |

## 修复

无阻断。轻微漏（六七岁上街的前史）记录为提示：出厂前史闭环由 ch10「十一岁被停带出门」承担。

## 已核实为正确

- 原句2 「时间是去年初、冬天」：原文 "Early last year. It was winter."——md 分析「去年初冬」逐字对应。
- 原句4 「Whatever this was」为原文句（"and now this. Whatever this was."），md 保留其迟疑语气。
- 原句5 「smothered」为原文逐字（"before she was quietly smothered by it?"），非译文增饰。
- 导航「Dr. Vaissier」拼写：text/ch04 "I was sent to get Dr. Vaissier."——与 md 一致。

已核实为正确（R5.5 固定节）：以上各条后续不得以「读着不对」为由改动，除非给出反证。
