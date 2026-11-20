# ch10 4-verdict（T3 深审）

R1：review/ch10/1-suread.json（8 条，子代理盲读，自检 PASS）。
R2：review/ch10/2-machine.json（chapter.sh --json verdict=ok，rc=0；9 块 10 片段逐字全 ok）。

## R4 逐块对应（人判）

| 块 | 引语↔中文理解 | 关键词 | 施事三问 | 结论 |
|---|---|---|---|---|
| 1 | 被举高的噩梦 | holding me aloft/jaws snapping up/toss me down 在引语 | Grenault 举她、群狼咬空、他 toss——方向全部自 him to her ✓ | 对应 |
| 2 | 开棺 | fought the nausea/pale blue dress/mostly skeleton 在引语 | I=她开盖 ✓ | 对应 |
| 3 | 葬礼誓言 | coffin lid echo/funeral mass/I would end it 在引语 | 宣言者=她（I declared）✓；省略号两段各为 text 相邻完整段 ✓ | 对应 |
| 4 | 远不止如此 | far more than that/blessed in learning/made them fear you 在引语 | 说话人=Father Vestille（text 邻域 he stepped closer）✓；受语者=她 ✓ | 对应 |
| 5 | 无条件祝福 | I always bless you/Whether I agree/what is best 在引语 | he=神父 ✓；La Rue Sauvage 街名在引语内 ✓ | 对应 |
| 6 | 大卫讲道 | a shepherd/a lion and a bear/rescued a lamb 在引语 | "The scriptures say" 转述链 ✓ | 对应 |
| 7 | 买裙让步 | I'll tell you/pay you for them/convince Andre to order more 在引语 | 说话人=Madame Denue（text 邻域）✓；受惠者=Leóne ✓ | 对应 |
| 8 | 情报投递 | bolts quickly, in abundance/access to silver/He's hunting you 在引语 | 转述者=Touraine、猎物=她 ✓；"licked his lips" 施事 Touraine ✓ | 对应 |
| 9 | found Pierre | He's found Pierre/ran/whistling for Crimson 在引语 | "No, I thought" 思维主语=她 ✓ | 对应 |

跨章引用核章号：块4 分析"对 ch09 结尾全盘自我否定的外部校正"——ch09 原句8 ✓；块6 分析 "'can't stop him' 的哭腔"=同章 text "Father Vestille, what if I can't stop him?" ✓；块9 分析"下一章的战场"=ch11 铁匠铺 ✓。
数字回原文：T1 已修的"那场葬礼弥撒上的誓言"不再绑定时间量——素读确认 two months 修饰的是 stormed the doors（text/ch10_10.txt），md 现状无误 ✓。

## 查出与处置

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 天数细节/不杀嘱托/护送动作/缺席原因/Filliene 名 未入块 | 铺陈与导航覆盖 | 不修 | 提示×5（依据：无 md 断言落空；Filliene 与 Leóne 二选一由块9 收束于后者，逻辑自洽） |

无修复动作。chapter.sh rc=0。

## 已核实为正确

- 块5 分析引用 "can't condone killing innocent men"——text/ch10_10.txt 逐字（同章对话）✓。
- 块6 分析"先给原型再给许可——你不是杀人，你是大卫打狼"——属讲道效果的解读，锚在引语三句上。
- 块7 中文"价钱你说了算，合理就好"="whatever you think is reasonable"（引语内逐字）✓。
- 块8 提示"他连传话的人都在品味这场追猎的兴奋"——"licked his lips" 在引语内，非越权。
