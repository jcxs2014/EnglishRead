# ch17 More Classic Joke Formats Explained 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，10 块；`chapter.sh` rc=0。

## 逐块对应（10 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 几种类型 | :19 | 是：spoonerism、说到一半 | spoonerisms / trail off ✅ | 换＝讲者 ✅ | 通过 |
| 2 勇敢士兵与面包师 | :19 | 是：darts into the foe | darts into the foe ✅ | 冲＝士兵 ✅ | 通过 |
| 3 足球队与茶包 | :19 | 是：茶包泡得久 | teabag / stays in the cup ✅ | 待＝茶包 ✅ | 通过 |
| 4 鱼与自行车 | :19 | 是：both swim / except for the bicycle | both swim ✅ | 游＝鱼 ✅ | 通过 |
| 5 爱尔兰与波兰 | :30 | 是：历史靶子 | the Irish / the Polish ✅ | 当靶子＝笑话作者 ✅ | 通过 |
| 6 "一个白痴" | :30 | 是：效率与偏见 | efficiency / bigotry ✅ | 建议＝作者 ✅ | 通过 |
| 7 灯泡＝一人活 | :41 | 是：不是 1 才有戏 | one-person job ✅ | 换＝群体 ✅ | 通过 |
| 8 圈内梗 | :41 | 是：行业刻板印象 | in-jokey / baffling ✅ | 讲＝讲者 ✅ | 通过 |
| 9 书名＋作者 | :52 | 是：I. P. Knightley | puns / cheerfully rubbish ✅ | 编＝作者 ✅ | 通过 |
| 10 警告 | :52 | 是：词会失去意义 | a word of warning / mush ✅ | 警告＝作者 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 四个 H2 小节 | What's the difference／Foolish group／Lightbulb／Batty book | 正确 | 通过 |
| 582 词 | `len(text.split())`=582 | 正确 | 通过 |
| 字符数 3,481（md 写"约 3,500"） | `len(text)` | 正确 | 通过 |
| 灯泡笑话 5 人 = 1 + 4 | `:41` 原文 | 正确 | 通过 |

## 已核实为正确

- 原句 3 的"茶包在杯里待得更久"是本章唯一靠双关的例子（`:19`），md 未把它归入 spoonerism。
- 原句 6 的 `From an efficiency perspective, ‘An idiot’…` 说明作者主张用泛称取代族群靶子，md 未写成作者认同族群笑话。
- 原句 9 的三个书名实例（Rusty Bedsprings、Attempting to… 等）在 `:52` 段内，md 只取一个作引语、其余进证据链，属取舍。

## 结论

阻断 0 / 提示 0 / 假红 0。
