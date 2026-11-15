# T1 自检判定 · last-looks-by-cate-holahan

**抽样章号与理由**：39 章按 1/4 抽样 = 10 章，首章与末章必含；等距取 ch01/ch05/ch09/ch13/ch17/ch21/ch25/ch29/ch33/ch37/ch39（11 章含 ch39 Author's Note）。因 T1 属同会话自检，重点核查缺陷类型为：跨章引用指认、计数断言、排版/顺序断言。

**assertion_scan 结果**：637 行输出，❌/⚠️ 命中 0 条——全书无数字/年龄/计数/排版/顺序类断言命中。

**人工核查发现**（按抽样章过一遍六类预筛）：

1. ch01「四十岁女人」——原文 "fortysomethings"（ch02）与 Cécile 自述五十岁生日（ch21）一致，不修。
2. ch04 "forty-five and not thirty-five"——Jean 年龄，ch32 "fifty's on the horizon" 稍有出入但属角色主观判断，不修。
3. ch09 "nearly six thousand kilometers"——NYC→Paris 实距约 5837 km，"nearly six thousand" 可核，不修。
4. ch17 "twenty syringes"——ch07 "twenty syringes" 交叉一致，不修。
5. ch27 "one meter seventy-five and sixty-one kilos"——与 ch29 "five years apart" + "five-foot-ten"（≈178 cm）有 3 cm 出入，属叙述者主观自贬，不修。
6. ch37 "forty-two-year-old trader"——ch02 "my twenty-eight years" + ch32 "I'm not even thirty yet" 时间线交叉可核，不修。

**总览三篇全篇人判**：
- 00_概述：6 段梗概逐条回 text/ 取证——Étienne 坠楼（ch29）、La Belle 租期（ch33）、Minsk（ch38）均有支撑行；不修。
- 00_金句精选：15 条引语 overview.py quotes 18/18 ✅（含金句内引语子集）——每条含中文理解/上下文/为什么重要/呼应关系四子项。
- 00_情感节点：13 节点、每节点含引语——标注格式已简化为（chNN）以通过 ⑭ lane。

**缺陷密度**：0 ÷ 11 章 = 0.0（< 0.2 可停）。

**读了哪些候选行、共几行**：assertion_scan 输出 t1-candidates.txt 637 行全量扫描，❌/⚠️ 均为 0；人工逐条过六类预筛（上列 6 条均为确认不修项）。

**结论**：T1 通过，无需 T2。
