# ch22 Ho-ho-horribly Bad Christmas Jokes 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，10 块；`chapter.sh` rc=0。

## 逐块对应（10 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 雪橇多少钱 | :17 | 是：on the house 双义 | on the house ✅ | 付＝圣诞老人 ✅ | 通过 |
| 2 腹肌雪人 | :22 | 是：abdominal/abominable | abdominal ✅ | 叫＝人 ✅ | 通过 |
| 3 stollen | :35 | 是：stollen/stolen | stollen ✅ | 送＝朋友 ✅ | 通过 |
| 4 Miss Sled | :40 | 是：misled | misled / Miss Sled ✅ | 说＝朋友 ✅ | 通过 |
| 5 三博士 | :48 | 是：gold guy/frankincense fellow/myhrh man | frankincense ✅ | 遇见＝我 ✅ | 通过 |
| 6 no thyme like the present | :53 | 是：thyme/time | thyme ✅ | 送＝人 ✅ | 通过 |
| 7 advent colander | :58 | 是：colander/calendar | advent colander ✅ | 买错＝我 ✅ | 通过 |
| 8 elf-esteem | :68 | 是：self-esteem | elf-esteem ✅ | 害羞＝助手 ✅ | 通过 |
| 9 Scrooge 进球 | :98 | 是：passed | passed ✅ | 传＝鬼 ✅ | 通过 |
| 10 Slade | :128 | 是：sleighed/sledded | Slade / sleighed ✅ | 听＝我 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 约 30 条（实测 29 条） | 31 段 − 2 标题 | 正确（"约"） | 通过 |
| 603 词 | `len(text.split())`=603 | 正确 | 通过 |
| 字符数 3,442（md 写"约 3,440"） | `len(text)` | 正确 | 通过 |
| 三博士三样礼物 | `:48` 逐条 | 正确 | 通过 |

## 已核实为正确

- 原句 5 是本章唯一超过 80 词的长块（三博士三段式），md 未拆分但机器校验通过；引语按原文的分句顺序保留。
- 原句 10 的 `Wizzard` 拼写：`:128` 原文为乐队名 Wizzard（双 z），md 未写成 Wizard。
- 原句 6 的 `no thyme like the present`（`:53`）与 md"没有比现在更好的百里香"一致，thyme/time 双关在中文里以引号保留。

## 结论

阻断 0 / 提示 0 / 假红 0。
