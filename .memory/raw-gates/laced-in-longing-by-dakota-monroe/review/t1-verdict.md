# T1 自检裁定 — laced-in-longing-by-dakota-monroe

抽样章（先定后读）：27 件 → 17–40 章档按 1/4 ⇒ 7 章 = **ch00, ch04, ch09, ch13, ch17, ch22, ch26**（首 ch00 与末 ch26 必含；round(26i/6) 等距）。抽样章素读锚点复验 54/54 全命中（production/chNN-suread.json 程序化重验）。

## 预筛与覆盖

- assertion_scan 六类 430 行（t1-candidates.txt）：① 相对章号 15 行全读 · ② 绝对断言 179 行全读 · ③ 年龄数字 179 行全读 · ④ 亲属 3 行全读 · ⑤ 施受 37 行抽 20 · ⑥ 方位 3 行全读。
- 总览三篇全篇人判：数字断言 21 项探针全部回 text/ 命中（二十七岁/八年九城/第三次未遂/四个月/十八岁/二十英里/十四层/六层/两百万/一百级台阶/Two hundred seventeen/八百年/一千零三/number 638/第四百世/两朵郁金香/黑大丽花/四号寄养妈妈/seventy-two hour hold/forty hours 等）；说话人归属按写作时上下文窗口确认；唯一性 Counter 核（30 条无重复）。

## 阻断（2 条，均已整改）

| 位置 | 改前 | 改后 | 原文依据 |
|---|---|---|---|
| ch04 原句5 读者视角提示 | 「上一章对医生都只报假数据」 | 「第 2 章里她对医生报的全是假数据」 | 报假数据发生在 ch02（ch03 为威尼斯梦，无医生场景） |
| ch10 原句5 读者视角提示 | 「与上一章『越睡越累』构成同一条疲劳线」 | 「与本章后文的『越睡越累』构成同一条疲劳线」 | 「wake more tired」在本章（ch10 para 277），ch09 无此句 |

## 同一成因类（相对章号）跨 2 章 ⇒ 已执行 T2 断言全扫（实质）

assertion_scan ①类 15 行即全书全部相对章号引用——已逐条回原文核：2 错 2 修、其余 13 行核为正确（ch07 上章=水晶 ✓、ch16→ch11 Seyr 警告 ✓、ch20→ch08 引语逐字 ✓、ch21/ch23→ch19 召唤 ✓、ch14/ch19 前向模糊指认不涉事实）；⑯ check_xref 伪造 0、移章 0。**T2 新增阻断 0。**

## 数字/事实抽核（抽样章+总览）

ch00（信中三承诺：PMDD 不点病名/可能重复/healing 非线性 ✓）；ch04（Stockholm/performing humanity/foster care ✓）；ch09（almost-touch/no medication ever has ✓）；ch13（somewhere I am happy/never been enough ✓）；ch17（misfiled/fold like a lawn chair ✓）；ch22（set it on fire/You carry every single one ✓）；ch26（not why she is mine/I do not forgive him/Elise=Vorin's promised ✓）。

## 结论

阻断 2 条（同成因跨 2 章）→ T2 已实质执行、新增 0；未触发 T3 条件。**T1 为同会话自检**（非异会话验收）；T3 深审未做（待用户发起）。
