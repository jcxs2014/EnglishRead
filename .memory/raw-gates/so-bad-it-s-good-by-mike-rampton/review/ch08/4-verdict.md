# ch08 Unhealthily Horrible Doctor Jokes 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，8 块；`chapter.sh` rc=0。

## 逐块对应（8 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 丛林阿司匹林 | :17 | 是：parrots eat 'em all=paracetamol | aspirins / parrots ✅ | 吃＝鹦鹉 ✅ | 通过 |
| 2 兔子 type-O | :22 | 是：O 型/typo | blood bank / type-O ✅ | 说＝兔子 ✅ | 通过 |
| 3 精神科 two tents | :28 | 是：teepee/two tents/too tense | teepee / two tents ✅ | 说＝病人 ✅ | 通过 |
| 4 十秒倒数 | :86 | 是：Ten→9→8 | straight / Ten ✅ | 说＝医生 ✅ | 通过 |
| 5 小马失声 | :61 | 是：horse/hoarse | voice / horse ✅ | 说＝小马 ✅ | 通过 |
| 6 产房喊声 | :66 | 是：Toni can't/Bill won't=Braxton-Hicks | labour ward / contractions ✅ | 喊＝产房外听到的人 ✅ | 通过 |
| 7 六十秒 | :165 | 是：六十秒 vs 一分钟后 | sixty seconds / in a minute ✅ | 安抚＝医生 ✅ | 通过 |
| 8 头上青蛙 | :203 | 是：spot 双义（痘/看见） | growing / spot ✅ | 说＝青蛙 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 41 条 | 43 非空段 − 2 标题 = 41 | 正确 | 通过 |
| "Doctor, doctor" 27 条 | `grep -o "Doctor, doctor" \| wc -l` = 27 | 正确 | 通过 |
| 字符数 4,993 | `len(text)`=4,993 | 正确 | 通过 |

## 已核实为正确

- 原句 1 的拼写：`:17` `the parrots eat ’em all`（'em 用弯撇号），md 未改成 them。
- 原句 6 的三个名字：`:66` `‘Toni can’t! Bill won’t!’`，md 保留原拼写。
- 原句 8 的青蛙台词：`:203` 末尾青蛙说 `‘It all started with a spot on my bottom’`，md「中文理解」保留 spot 的双义。

## 结论

阻断 0 / 提示 0 / 假红 0。
