# ch09 Unemployably Terrible Work Jokes 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，9 块；`chapter.sh` rc=0。

## 逐块对应（9 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 躲票 | :15 | 是：conductor 双义 | conductor ✅ | 躲＝我 ✅ | 通过 |
| 2 日历厂 | :20 | 是：took too many days off | days off ✅ | 被解雇＝我 ✅ | 通过 |
| 3 氦气厂 | :30 | 是：not having a lighter 双义 | lighter ✅ | 辞职＝我 ✅ | 通过 |
| 4 伐木工 38,612 | :53 | 是：log 双义 | log ✅ | 数＝伐木工 ✅ | 通过 |
| 5 酒吧里的段子手 | :107 | 是：场景说明 | bar / quips ✅ | 讲＝我 ✅ | 通过 |
| 6 兽医家的狗 | :112 | 是：pet 双义 | patient / pet ✅ | 带＝农夫 ✅ | 通过 |
| 7 宇航员 launch | :179 | 是：launch 双义 | launch ✅ | 吃＝宇航员 ✅ | 通过 |
| 8 杂工 odd jobs | :157 | 是：odd 双义 | odd jobs ✅ | 雇＝我 ✅ | 通过 |
| 9 殡葬工圣诞 | :147 | 是：undertaker 的冷幽默 | undertaker ✅ | 请＝我 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 约四十条 | 44 非空段 − 2 标题 − 1 脚注 = 41 条 | 正确（"约"） | 通过 |
| 38,612 棵 | `:53` 逐字 | 正确 | 通过 |
| 字符数 4,830 | `len(text)`=4,830 | 正确 | 通过 |
| 末尾脚注属 ch12 | `:223` 带 `*`；ch12 :99–111 三处同句 | 正确 | 通过 |

## 已核实为正确

- 原句 8 的清单编号：`:157` `he hadn’t done numbers 2, 4, 6, 8 or 10 on the list`，md 释义"只做奇数编号"有据。
- 原句 4 的 `38,612` 出现在伐木工致辞里，md 未把数字归给作者旁白。
- 「soda pressing ≈ soul-destroying」：`:72` 原文，md 证据链未夸大。

## 结论

阻断 0 / 提示 0 / 假红 0。
