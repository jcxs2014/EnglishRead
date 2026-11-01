# ch06 Deliciously Terrible Food Jokes 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，10 块；`chapter.sh` rc=0。

## 逐块对应（10 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 chew-chew | :17 | 是：chew-chew/choo-choo | chew ✅ | 问＝听者 ✅ | 通过 |
| 2 Heinz | :22 | 是：spill the beans | spill the beans ✅ | 拒说＝工人 ✅ | 通过 |
| 3 佛系热狗 | :32 | 是：one with everything | everything ✅ | 说＝佛 ✅ | 通过 |
| 4 oysters | :42 | 是：shellfish/selfish | shellfish ✅ | 不借＝牡蛎 ✅ | 通过 |
| 5 impasta | :58 | 是：impostor | impasta ✅ | 问＝听者 ✅ | 通过 |
| 6 ambidextrose | :65 | 是：ambidextrous+dextrose | ambidextrose ✅ | 自称＝我 ✅ | 通过 |
| 7 cantaloupe | :85 | 是：can't elope | cantaloupe ✅ | 坚持婚礼＝甜瓜 ✅ | 通过 |
| 8 Tortilla | :95 | 是：wrap 双义 | wrap ✅ | 拍片＝剧组 ✅ | 通过 |
| 9 两根香肠 | :145 | 是：元笑话/WHO | sizzling / WHO ✅ | 说＝香肠 ✅ | 通过 |
| 10 nacho | :200 | 是：nacho/not your | nacho ✅ | 问＝听者 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 正文 30 条 + 奶酪 6 条 = 36 条 | 40 非空段 − 2 标题 − 2 个“Cheese jokes” = 36 | 改后正确 | 阻断已修 |
| 字符数 3,219 | `len(text)`=3,219 | 正确 | 通过 |
| 奶酪小节标题出现两次 | `:167` 页眉、`:177` 小节标题 | 正确 | 通过 |

## 已核实为正确

- 原句 8 的 `That’s a wrap!` 双义（拍摄收工 / 卷饼）在 `:95` 原文成立。
- 原句 2 的 `Spill the beans` 与 Heinz 烤豆工厂对应：`:22` 原文。
- 「两根香肠」条的大写 "WHO"（`:145`）是原文强调，非 md 添加。

## 结论

阻断 1（计数 37→36，已修）/ 提示 0 / 假红 0。修后 `chapter.sh` rc=0。
