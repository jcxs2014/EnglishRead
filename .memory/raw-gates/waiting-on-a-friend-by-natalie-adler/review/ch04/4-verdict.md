# ch04 判定表（R5）

**覆盖声明**：完整 R1（22/22）+ R2（ok）+ R3 + R4（7 块全查）。

## 一、逐块 R4
- B1：主语 Mark（was/had）；「不吓人的蓝眼睛」为 Renata 的判断；对应 ✓。
- B2：主语 Mark 的冷父母（raised）；受事 Mark；对比面 Renata 的瘾母亲；方向未倒置（"loved me but also loved heroin" 属母亲）✓。
- B3：主语 Renata（smitten）；受事 Mark；straight guys/jocks 为「人人」名单；Hank 为跨块伏笔（B4–B5），非归属错 ✓。
- B4：主语谣言（had come on to）；受事 Hank；「踢碎头盖骨」为谣言措辞（分析保持引号归属）✓。
- B5：主语 Hank（coldcocked）；受事 Mark；"kind enough to do" 是 Mark 的慷慨（分析未反转为 Hank）✓。
- B6：主语 Mark（accepted apology）；受事 Hank 的道歉与握手；bony handshake 属 Hank ✓。
- B7：主语 Renata 的记忆；受事 Mark 的脸（先硬后软）；对应 ✓。
- 施事全章：施暴者=Hank、接受道歉者=Mark、讣告登载=Times，全部与原文一致。

## 二、判定表
| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| osculation 无原文 | /usr/bin/grep -c osculation text/*.txt → 0（exit 1） | 分析层英文无据 | 阻断（已修） |
| 七岁 Lisa 事件未设块 | text:1297 段 | 逸事，非关键事件 | 提示（取舍） |
| name-far B3（Hank） | 探针 | 跨块伏笔 | 假红 |

## 三、已核实为正确（防误修）
- B4「Hank 是冰箱、额头是一整块大陆」= 原文 "a real refrigerator of a guy with a continent for a forehead."，勿改喻体。
- B6 引文 "I’m sorry for what I did, but hey, I’m paying for it now" 为 Hank 原话（text: 约 3530 段），归属勿移。
- B7 "hard…then soft" 的主语是 Mark 的脸，勿改为叙述者的心情。
