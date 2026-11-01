# ch14 The Dad Joke Connection 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，9 块；`chapter.sh` rc=0。

## 逐块对应（9 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 污名的起点 | :15 | 是：dad=terrible 蔓延到 jeans/bods/rock | dad jokes ✅ | 叫＝人们 ✅ | 通过 |
| 2 喜剧变精致 | :21 | 是：需要区分 | sophisticated / differentiation ✅ | 变＝喜剧界 ✅ | 通过 |
| 3 带不走的小段子 | :21 | 是：无法复述 | bite-sized ✅ | 讲＝观众 ✅ | 通过 |
| 4 旧式父亲 | :28 | 是：握手、晚安、一码威士忌 | hangover ✅ | 回家＝父亲 ✅ | 通过 |
| 5 关系建设 | :28 | 是：autopilot 的俏皮话 | relationship-building ✅ | 讲＝父亲 ✅ | 通过 |
| 6 不再不可触碰 | :31 | 是：家庭绕着他转 | untouchable / orbited ✅ | 看待＝家人 ✅ | 通过 |
| 7 地位下降 | :31 | 是：20 世纪后半叶两条线 | influx / a peg ✅ | 拉低＝媒体与就业 ✅ | 通过 |
| 8 情景喜剧爸爸 | :31 | 是：bumbling 刻板印象 | slobby / infallible ✅ | 演＝电视 ✅ | 通过 |
| 9 妈妈也无聊 | :35 | 是：爸爸更爱讲 | tediously / mushroom ✅ | 讲＝爸爸 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 443 词、9 段 | `len(text.split())`、非空段 | 正确 | 通过 |
| 字符数 2,601（md 写"约 2,600"） | `len(text)` | 正确 | 通过 |
| 20 世纪后半叶 | `:31` 逐字 | 正确 | 通过 |
| 包袱在插图里 | 正文末句 "The big question is:"；alt 文本即 punchline | 正确 | 通过 |

## 已核实为正确

- 原句 3 的"可以笑出眼泪、但带不走什么"与 `:21` 原文 `you might weep tears of laughter, but there isn’t necessarily anything you can take away from it and repeat to your friends` 逐字对应（T3 总览层曾据此改正 `00_概述.md`）。
- 原句 9 的 `unable to see a mushroom without pointing out that…` 说明爸爸是施事，md 未把笑话安到作者头上。
- 插图说明（`f087-01` alt）与正文末句的关系，md「概览」已写明"文字页读到半空"。

## 结论

阻断 0 / 提示 0 / 假红 0。
