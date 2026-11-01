# ch04 Refreshingly Terrible Walks Into a Bar Jokes 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，9 块，引语查无 0。

## 逐块对应（9 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 北极熊 | :17 | 是：pause/paws | pause ✅ | 问＝酒保，答＝熊 ✅ | 通过 |
| 2 汉堡 | :33 | 是：身份错位，非谐音 | serve ✅ | 拒＝酒保 ✅ | 通过 |
| 3 屎壳郎 | :50 | 是：stool 双义 | stool ✅ | 问＝屎壳郎 ✅ | 通过 |
| 4 Times New Roman | :60 | 是：type 双义 | type ✅ | 赶人＝酒保 ✅ | 通过 |
| 5 螺丝刀 | :77 | 是：named after 的语法歧义 | named after ✅ | 说话＝螺丝刀 ✅ | 通过 |
| 6 长颈鹿 | :104 | 是：lying/lion（本轮已修） | lying / lion ✅ | 喊＝酒保，答＝男人 ✅ | 通过 |
| 7 绳子 | :126 | 是：frayed knot=afraid not | frayed / knot ✅ | 拦＝门卫 ✅ | 通过 |
| 8 搭电线 | :131 | 是：start 双义 | jumper cables / start ✅ | 说＝搭电线 ✅ | 通过 |
| 9 时间旅行者 | :65 | 是：因果倒置 | time travellers ✅ | 说＝酒保、进＝旅行者 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 全章 26 条、无解说 | 28 非空段 − 2 标题 = 26；正文无解说句 | 正确 | 通过 |
| 字符数 6,033/6,034 | `len(text)`=6,034 | 正确 | 通过 |
| 汉堡条是全章最短、绳子条近 60 词 | :33 一句；:126 五句 | 正确 | 通过 |
| 螺丝刀条的名字是 Melanie | `:77` `‘You have a drink called Melanie?’` | 正确 | 通过 |

## 已核实为正确

- 原句 1 的省略号是原文所有：`:17` `‘I’ll have a pint ………… of lager please.’`，不是截断标记。
- 原句 9 的倒序：`:65` 酒保先说"You don't serve time travellers"，:67 才写旅行者走进来 —— md「中文理解」的"因果顺序被倒置"有原文位置依据。
- 「Times New Roman 那条靠 type 双义」：`:60` 原文 `We don’t want your type in here!`，type 兼指字体与"你这类人"。

## 结论

阻断 0 / 提示 1（已修）/ 假红 0。`chapter.sh` rc=0（修后复跑）。
