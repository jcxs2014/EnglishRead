# ch29 Rubbish Jokes Too Silly for Any Other Chapter 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，10 块；`chapter.sh` rc=0。

## 逐块对应（10 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 棕色且粘 | :30 | 是：字面答案 | a stick ✅ | 说＝答者 ✅ | 通过 |
| 2 绿色红漆味 | :52 | 是：同义反复 | green paint ✅ | 说＝答者 ✅ | 通过 |
| 3 Rupert the Fridge | :89 | 是：无故答案 | tartan ✅ | 穿＝Rupert ✅ | 通过 |
| 4 sea weed | :114 | 是：seaweed 谐音 | sea weed ✅ | 笑＝海滩 ✅ | 通过 |
| 5 vowel movement | :119 | 是：bowel movement | vowel movement ✅ | 吃＝你 ✅ | 通过 |
| 6 Mercury in Uranus | :129 | 是：行星/肛门 | Uranus ✅ | 说＝医生 ✅ | 通过 |
| 7 围栏与七十三 | :94 | 是：口号式重复 | seventy-three ✅ | 喊＝围栏里的人 ✅ | 通过 |
| 8 戳眼与七十四 | :94 | 是：数字加一 | seventy-four ✅ | 戳＝对方 ✅ | 通过 |
| 9 公交丑婴儿 | :207 | 是：猴子 | monkey ✅ | 说＝乘客 ✅ | 通过 |
| 10 kidley | :212 | 是：kidney 拼错 | kidley ✅ | 说＝顾客 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 约 40 条（实测 38 条） | 40 段 − 2 标题 | 正确（"约"） | 通过 |
| 651 词 | `len(text.split())`=651 | 正确 | 通过 |
| 字符数 3,716（md 写"约 3,800"） | `len(text)` | 正确（"约"） | 通过 |
| 四条长叙事 | 段 10（43 词）/17（62）/38（72）/39（37） | 正确 | 通过 |

## 已核实为正确

- 原句 6 的 `Mercury is in Uranus`（`:129`）在 T1 时被缩短成 `Mercury is in Uranus.` 才与原文match，本次 suread 锚点同样用该句，已核。
- 原句 7/8 的拆分（`:94` 一段劈两块）符合"块内连续、不跨段"要求。
- 原句 10 的 `kidley` 是原文故意拼错（kidney→kidley 的谐音），md 词汇释义未把它当正字。

## 结论

阻断 0 / 提示 0 / 假红 0。
