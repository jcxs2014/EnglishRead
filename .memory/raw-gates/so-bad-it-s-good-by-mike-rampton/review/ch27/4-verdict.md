# ch27 How to Write Your Own Rubbish Joke 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，11 块；修后 `chapter.sh` rc=0。

## 逐块对应（11 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 方法因人而异 | :15 | 是：门路一样多 | creative ✅ | 写＝人 ✅ | 通过 |
| 2 倒着推 | :15 | 是：cheerfully bad | backwards ✅ | 推＝作者 ✅ | 通过 |
| 3 You massive idiom | :22 | 是：Everything must go | idiom ✅ | 取＝你 ✅ | 通过 |
| 4 Smash it up | :33 | 是：同音/同形/首音互换 | homophone ✅ | 拆＝你 ✅ | 通过 |
| 5 Abandon most | :41 | 是：大多要丢 | so bad they’re good ✅ | 丢＝你 ✅ | 通过 |
| 6 Tudors/Stuarts | :41 | 是：Phwoar of the Noses | Phwoar ✅ | 打仗＝两朝 ✅ | 通过 |
| 7 reverse engineering | :52 | 是：铺垫不含关键词 | reverse engineering ✅ | 搭＝你 ✅ | 通过 |
| 8 Super calloused… | :52 | 是：fragile mystic | calloused ✅ | 说＝人 ✅ | 通过 |
| 9 Will people get this wrong | :64 | 是：站到首次听众位置 | confusing ✅ | 检查＝你 ✅ | 通过 |
| 10 The Germinator | :64 | 是：germinate/Terminator | Germinator ✅ | 说＝作者 ✅ | 通过 |
| 11 Enjoy the groans | :72 | 是：再写一百个 | another hundred ✅ | 要求＝作者 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 六节 17–134 词（原写 40–120） | 各节词数实测 | 改后正确 | 提示已修 |
| 六个编号小节 | 段 3/5/7/9/11/13 | 正确 | 通过 |
| 595 词 | `len(text.split())`=595 | 正确 | 通过 |
| 字符数 3,380 | `len(text)` | 正确 | 通过 |

## 已核实为正确

- 原句 5 的 `There are jokes that are so bad they’re good, and jokes that are just bad`（`:41`）是作者区分"坏到好处"与"只是坏"，md 未把它读成作者自夸。
- 原句 8 是 `Super calloused fragile mystic vexed by halitosis`（`:52`），对照的是 Mary Poppins 的 supercalifragilistic，md 未写成另一首歌词。
- 原句 10 的 `germinate` 生僻性：`:64` 原文自评"not a joke as much as a noise"，md 保留该自评。

## 结论

阻断 0 / 提示 1（已修）/ 假红 0。
