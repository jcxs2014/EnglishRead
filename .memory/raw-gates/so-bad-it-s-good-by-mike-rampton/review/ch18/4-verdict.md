# ch18 Terrible Travel Jokes 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，10 块；`chapter.sh` rc=0。

## 逐块对应（10 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 穿凉鞋的法国人 | :20 | 是：flip-flop | sandals / Phillipe Floppe ✅ | 叫＝人 ✅ | 通过 |
| 2 俄罗斯套娃 | :28 | 是：full of themselves | Russian dolls ✅ | 自满＝套娃 ✅ | 通过 |
| 3 瑞士国旗 | :33 | 是：大加号 | flag / a big plus ✅ | 说＝作者 ✅ | 通过 |
| 4 飞机上争座 | :38 | 是：你来开飞机 | fly the plane ✅ | 让座＝对方 ✅ | 通过 |
| 5 Nunavut | :43 | 是：having none of it | Nunavut ✅ | 拒绝＝她 ✅ | 通过 |
| 6 Split | :53 | 是：分着吃 | Split ✅ | 点＝我 ✅ | 通过 |
| 7 Eerie | :58 | 是：伊利/诡异 | Lake Michigan / Eerie ✅ | 看见＝我 ✅ | 通过 |
| 8 bayou/non-bayou | :68 | 是：洗衣粉 | Louisiana / non-bayou ✅ | 买＝我 ✅ | 通过 |
| 9 serviette union | :165 | 是：餐巾工会 | serviette union ✅ | 入会＝我 ✅ | 通过 |
| 10 Bucharest | :175 | 是：book arrest | Bucharest ✅ | 读＝人 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 约 30 条（实测 32 条） | 34 段 − 2 标题 | 正确（"约"） | 通过 |
| 515 词 | `len(text.split())`=515 | 正确 | 通过 |
| 字符数 3,080（md 写"约 3,000"） | `len(text)` | 正确 | 通过 |
| Split 是克罗地亚第二大城 | `:53` 原文 | 正确 | 通过 |

## 已核实为正确

- 原句 4 的 `Eventually he stood up and said, ‘Fine, you fly the plane.’` 出自 `:38` 的占座故事，施事是"我"（让位者），md 未把台词安给对方。
- 原句 5 的 `She was having Nunavut`（`:43`）与 md"她对此没兴趣"一致。
- 原句 10 的 "give the Bucharest" 在 `:175` 原句里，md 的关键词只留 Bucharest（T3 前已有同类教训：关键词不写释义）。

## 结论

阻断 0 / 提示 0 / 假红 0。
