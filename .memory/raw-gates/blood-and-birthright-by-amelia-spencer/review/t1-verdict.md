# T1 自检判定 · blood-and-birthright-by-amelia-spencer

抽样章号与理由（先定后读）：全书 47 件（ch00–ch46）>40 章 → 1/5 且至少 10 章；首章 ch00 与末章 ch46 必含，其余等距取 ch01/ch10/ch18/ch24/ch29/ch35/ch40/ch44——共 10 章。抽样覆盖：序言、试产首章、Dilethisante 篇中点、玻璃图书馆、Atalanthya POV、Guardians 败选、龙之眼、战前会、Rotunda 高潮、后记——十种章节形态各有代表。

## 1. 素读清单复验（10/10 章锚点全命中）

ch00 5/5｜ch01 8/8｜ch10 10/10｜ch18 10/10｜ch24 9/9｜ch29 7/7｜ch35 7/7｜ch40 7/7（整改后）｜ch44 7/7｜ch46 2/2。

整改 1 处：ch40-facts 残留一条写作期的弯引号锚（"You're stuck with me…"），T1 复验时发现并替换为裸子串——系写作期 python replace 只修了部分行的残留，非正文缺陷（facts 文件属生产档案）。

## 2. 事实回源抽查（抽样章各 1–2 条，4/4 命中）

- 「Kaenan Moon」（ch04 误认）→ ch04 text 命中 ✓
- 「Sliced him in two from the top of his head to the tip of his cock」（Daiyu 终审）→ ch31 text 命中 ✓（大写 S 起句）
- 「seven bloodlines with a viable claim」→ ch36 text 命中 ✓
- 「twelve Council members」→ ch39 text 命中 ✓

## 3. 相对章号抽验（①类 32 行中抽 4 条，4/4 正确）

- ch03「上一章 Isaiah 报告的 closer」→ ch02#6 确为 Isaiah 报告 ✓
- ch05「ch04 里 Miles 喊过 Kaenan Moon」→ ch04#2 ✓
- ch30「Vincent 的 Run 口型」→ ch30 正文 "Run," he mouthed ✓
- ch40「对照 ch05 的三掌按肩入书」→ ch05#9 Three palms ✓

## 4. assertion_scan 六类预筛（t1-candidates.txt 678 行）

①相对章号 32 行：抽 4 验 4 正确（见上）；其余均为「上一章/下一章」例行跨章指认，与正文引语来源一致。
②绝对断言 144 行：多为「第一次/最」类评析修辞（按 7c 分级从宽只记）；抽查「第一次公主抱（Dhaholoseum）」「第一任 Catalogue 亲选馆长（Henry 证词）」均有原文支撑。
③年龄数字 328 行：五岁（ch14/ch28）、1386 年（ch13/ch18）、十一世纪（ch30）、三分四十二秒（ch34）等均与 text/ 一致；「二十四年 moratorium」为台词内数字（ch21 逐字）。
④亲属身份 115 行：Moon 姐妹/父子（Isaiah–Elias）/孪生（Kai）/母子（Atalanthya–Adrien）各线经 text 锚点复核无错置。
⑤方向施受 35 行（抽 20）：「他把她抱起/她把他拽下桥」等施受方向与原文动作主语一致。
⑥场景方位 10 行：Main Hall/East Wing/West Wing/North Wing 的位置叙述与 ch41–43 原文走廊路线一致。

## 5. 改过的数字/事实回灌总览检查

写作期整改均为「关键词越界、词表 A 类自造词、跨段拼接、引语形态」，未改过任何数字/亲属/事实断言 ⇒ 无需回灌。grep 抽查 00_*.md 中「1386」「十一世纪」「九比三」「二十四小时」与正文一致。

## 6. 总览三篇人判（六类逐条核）

概述 9 引语、金句 25 条（圈码 ①–㉕ 连续无跳号）、情感节点 12 节点 24 引语——全部经 gen_overview 从已过门禁章节块注入（零手打英文），verify_overview_quotes 66/66=100%。唯一数检查：54 唯一/54 出现，零重复（3 处重复已在交付前以圈码引用整改）。呼应关系圈码逐条回查：①↔㉕（火/home）、④↔⑮⑯（合同三部曲）、⑫↔⑬（革命因果）、⑰↔㉔（真实接住）均指向正确条目。

## 结论

阻断 0 条；提示类：绝对断言中的评析修辞（「第一次/最」）按 7c 分级从宽记录不构成阻断。缺陷密度 0/10 < 0.2，T1 通过（同会话自检，非独立审查）。
