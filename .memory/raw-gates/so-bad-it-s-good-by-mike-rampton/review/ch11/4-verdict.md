# ch11 Knock-knock Jokes to Guarantee You Aren't Welcome 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，10 块；`chapter.sh` rc=0。

## 逐块对应（10 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 I've eaten up | :17 | 是：吃光／追问 who | eaten up ✅ | 说＝敲门者 ✅ | 通过 |
| 2 Anita | :24 | 是：I need a | Anita ✅ | 说＝敲门者 ✅ | 通过 |
| 3 Cowsgo | :45 | 是：cows go | Cowsgo ✅ | 说＝敲门者 ✅ | 通过 |
| 4 Control freak | :52 | 是：抢话 | control freak ✅ | 命令＝敲门者 ✅ | 通过 |
| 5 Little old lady | :66 | 是：老太太式应答 | little old lady ✅ | 说＝敲门者 ✅ | 通过 |
| 6 Spell | :73 | 是：W-h-o | Spell ✅ | 拼＝敲门者 ✅ | 通过 |
| 7 Kanga | :80 | 是：kanga/roo | Kanga ✅ | 说＝敲门者 ✅ | 通过 |
| 8 Banana | :115 | 是：重复后换 orange | banana / orange ✅ | 说＝敲门者 ✅ | 通过 |
| 9 Cash | :136 | 是：cashew | Cash ✅ | 说＝敲门者 ✅ | 通过 |
| 10 Persephone | :150 | 是：放弃谐音，改问"你认识几个" | Twinkletoes ✅ | 问＝开门者 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 20 条 | 22 非空段 − 2 标题 = 20 | 正确 | 通过 |
| 字符数 2,113 | `len(text)`=2,113 | 正确 | 通过 |
| 全部以 "Knock, knock." 起头 | 逐条首句 | 正确 | 通过 |

## 已核实为正确

- 原句 8 的两次 knock 结构：`:115` 原文先 banana 一轮、再重新 "Knock, knock."，md 的"拖长形式"有据。
- 原句 9 的 cashew 双关：`:136` 原文 `No thanks, I’m allergic to nuts` 之类收尾，md 未写成"现金"字面义。
- 原句 10 的"认识好几个同名的人"：`:150` 原文以 `You … you know multiple people named Persephone Twinkletoes McGinty?` 收，md 释义一致。

## 结论

阻断 0 / 提示 0 / 假红 0。
