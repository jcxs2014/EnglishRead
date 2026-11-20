# ch09 4-verdict（T3 深审 · 边审边改）

R1：review/ch09/1-suread.json（8 条，子代理盲读，自检 PASS）。
R2：review/ch09/2-machine.json（chapter.sh --json verdict=ok，rc=0；8 块 12 片段逐字全 ok）。

## R4 逐块对应（人判）

| 块 | 引语↔中文理解 | 关键词 | 施事三问 | 结论 |
|---|---|---|---|---|
| 1 | 英雄定义 | A hero/stands up/All I did was stand up 在引语 | "he had said"=Francois ✓；"All I did was stand up"=Francois 自谦 ✓ | 对应 |
| 2 | 破窗引敌 | punched my gloved fist/shattered/seizing the wolves' attention 在引语 | I=她砸窗 ✓；受引者=狼群 ✓ | 对应 |
| 3 | 射爪毙 Jareau | lower paw/yelp of pain/Dead from the single silver-tipped wound 在引语 | "I fired at his lower paw" 的 his=举托盘逼近之狼=Jareau（text 邻域 "the other wolf…his wooden tray"）✓；"Jareau!" 喊者=Grenault ✓ | 对应 |
| 4 | 数箭 | sooner or later/He had been counting/my last bolt 在引语 | he=Grenault ✓；"他劝她'再来一发'时心里已算清那发不存在"——两段省略号各为 text 相邻完整段 ✓ | 对应 |
| 5 | 纪念品 | mantle/dislodging/souvenir 在引语 | He=Grenault 取箭 ✓；受物=my bolt=她的箭 ✓ | 对应 |
| 6 | 醉酒否认 | wolf carcasses/half-empty wine bottle/You've been drinking 在引语 | 说话人=Monsieur Denue、受斥者=Marguerite（其妻）✓ | 对应 |
| 7 | 忘装填 | forgotten to reload/scrambled/pouch of silver-tipped bolts 在引语 | I=她 ✓ | 对应 |
| 8 | 单边透明 | a single weakness/every one of mine/kill me slowly 在引语 | "他"=Grenault 毁她 ✓；promise 回指 ch05 宣判 ✓ | 对应 |

跨章引用核章号：块8 分析 "kill me slowly 从 ch05 的宣判回响"——text/ch05_5.txt "Then I'll kill you—slowly—in front of the entire order." ✓；块3 提示 Devereaux 名单与 ch05 "You killed Gregor and Thayer and Robillet" 三名吻合（Tumier 属 ch08）✓。
数字回原文：十箭（块4 分析）="only fire ten bolts in succession"（text/ch09_9.txt）✓；三匹（未入 md，无断言）。

## 查出与处置

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 块3 提示 "childhood friends" 词序不成立 | text 为 "friends since childhood"（grep exit 0） | 校正词序 | 提示→当场修 |
| "meant to rule by my side"/整夜受苦威胁未入块 | 动机线由块3 提示（friendship）与 ch12 块2（空屋动机全量）承接 | 不修 | 提示（依据：动机跨章递进，ch12 已收束） |
| 六七匹 vs 三匹更正未入块 | 数字账跨 ch08/ch09 一致（1+2=3），md 无冲突断言 | 不修 | 提示（依据：计数层无落空） |
| 开局围困/逃生未入块 | 导航+块8 链条覆盖 | 不修 | 提示 |

## 修复动作（边审边改）

块3 提示词序校正（"childhood friends"→"friends since childhood"）。修后 chapter.sh rc=0，pathspec 提交。

## 已核实为正确

- 块4 中文"他劝她'再来一发'的时候，心里已经算清那发不存在"——引语两段分别含挑衅与 "He had been counting"，解读锚在原文 ✓。
- 块6 分析"三具狼尸抵不过一只酒瓶"——carcasses（复数）+ wine bottle 均在引语内，计数 3 与本章两次击杀+ch08 Tumier 一致 ✓。
- 块7 分析"刚才数着箭、报着账的冷静猎人"——"数箭"在块4 引语内，跨块回指成立。
