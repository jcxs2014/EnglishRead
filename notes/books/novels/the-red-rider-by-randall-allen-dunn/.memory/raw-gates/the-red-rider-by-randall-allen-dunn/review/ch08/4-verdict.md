# ch08 4-verdict（T3 深审）

R1：review/ch08/1-suread.json（8 条，子代理盲读，自检 8/8）。
R2：review/ch08/2-machine.json（chapter.sh --json verdict=ok，rc=0；8 块 9 片段逐字全 ok）。

## R4 逐块对应（人判）

| 块 | 引语↔中文理解 | 关键词 | 施事三问 | 结论 |
|---|---|---|---|---|
| 1 | 嫉妒→原则 | shook off/didn't deserve/No one did 在引语 | I=她甩开念头 ✓；"they didn't deserve" 的 they=Denue 一家 ✓ | 对应 |
| 2 | 母亲怒骂三连 | fine clothes/brawling in the mud/that knife 在引语 | 说话人=Madame Denue、受斥者=Jacque ✓；"where did you get that knife" 落点=赃物 ✓ | 对应 |
| 3 | 静音潜入 | stood ajar/splintered/slipped inside 在引语 | They=狼（撬门）✓；I=她闪身 ✓ | 对应 |
| 4 | 一弩放倒 | dropped/a single bolt 在引语 | "Until I dropped the first one" 施事=她、受事=第一头狼 ✓；Tumier 名由提示从 text 引入 ✓ | 对应 |
| 5 | 三态怪物 | on all fours/ears scraping the ceiling/a genuine monster 在引语 | he=Grenault ✓ | 对应 |
| 6 | 口诀直瞄 | echoed in my mind/aimed between his eyes/Be careful what you wish for 在引语 | "Papa's voice echoed"=内心声音（非在场发言）✓；"Be careful what you wish for" 说话人=她 ✓；多段省略号两段各为 text 相邻完整段 ✓ | 对应 |
| 7 | 三段撤离 | spun away/rolled sideways/threw open the window latch 在引语 | I=她 ✓；"放一头狼扑空冲过"=letting one wolf rush past me ✓ | 对应 |
| 8 | 人质悬念 | all be dead/in seconds 在引语 | They=刚下床的 Denue 一家 ✓ | 对应 |

跨章引用核章号：块6 提示 "'No hesitation.'"（ch05 家训）——text/ch05_5.txt "You—cannot—hesitate" 与块6 引语 "You cannot hesitate." 同义回响；块6 引语自身在 text/ch08_8.txt 逐字 ✓。块1 提示 "No one did." 在引语内 ✓。
数字回原文：near twice the size（未入 md）；three bolts（未入 md，提示语"每一步都在还债"无数值）——md 无计数断言落空。

## 查出与处置

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 监视布置/来意宣言/四狼数/Prime 时限/挡三箭 未入块 | 均为铺陈或跨章动机线（Prime 线由 ch01 原句9 提示与 ch12 块2 承接） | 不修 | 提示×5（依据：转折层与施事层全收，无 md 断言落空） |

无修复动作。chapter.sh rc=0。

## 已核实为正确

- 块6 引语两段 "Papa's voice echoed in my mind. You cannot hesitate." 与 "I stepped forward and aimed between his eyes. "Be careful what you wish for."" 为 text/ch08_8.txt 相邻完整段，… 连接合法（fragments 独立取证命中）。
- 块7 分析"撤离写成三段流水线：放空、捡械、开门"——三动作均在引语内（spun/rolled/threw open），计数一致。
- 块8 中文"她逃出来了，却把战场留给了无辜者"——由"翻了出去"（原句7）+ "They would all be dead"（原句8）支撑，非越权断言。
