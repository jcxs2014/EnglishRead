# ch12 Shaggy Dog Stories That Need Putting Down 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，10 块；修后 `chapter.sh` rc=0。

## 逐块对应（10 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 Britpop 对峙 | :57 | 是：反复要求 | no, no, no ✅ | 要求＝朋友 ✅ | 通过 |
| 2 我是 Suede | :63 | 是：荒诞落点 | Suede ✅ | 变成＝我 ✅ | 通过 |
| 3 尽责玉米片 | :68 | 是：一直保持顶层 | conscientious ✅ | 是＝玉米片 ✅ | 通过 |
| 4 Then it got eaten | :92 | 是：四字收尾 | eaten ✅ | 吃＝人 ✅ | 通过 |
| 5 修道院怪声 | :99 | 是：半夜怪声 | monastery / noise ✅ | 听到＝推销员 ✅ | 通过 |
| 6 受戒当天 | :111 | 是：答案被星号抽掉 | ordained / abbot ✅ | 告知＝方丈 ✅ | 通过 |
| 7 婚礼清单 | :116 | 是：队伍越堆越长 | queue / table ✅ | 排队＝宾客 ✅ | 通过 |
| 8 punchbowl | :131 | 是：有 punchbowl 无 punch line | punch line ✅ | 说＝作者 ✅ | 通过 |
| 9 Jimmy 与绿球 | :139 | 是：五岁起反复要 | green ping-pong ball ✅ | 要＝Jimmy ✅ | 通过 |
| 10 临终追问 | :175 | 是：只说"告诉了他" | told him ✅ | 告诉＝Jimmy ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 五个故事 | 55 段 − 2 标题，按空行分组为 5 组 | 正确 | 通过 |
| 篇幅 204–435 词 / 5–17 段（原写"三十行到一百余行"） | 逐组计数 | 改后正确 | 提示已修 |
| 字符数 8,457 | `len(text)`=8,457 | 正确 | 通过 |
| 脚注不属于本章正文 | ch12 正文 :111 带 `*`，脚注落在 ch09 :223 | 正确 | 通过 |

## 已核实为正确

- 原句 2 `And eventually I was Suede.` 是原文末句（`:63`），md 未把 "Suede" 误成 "swayed"（那是全章另一处谐音梗的材料，未选入）。
- 原句 5 的 `We can’t tell you, you’re not a monk` 在正文 :99–111 反复出现三次，md 把它作为"没有包袱"的结构证据成立。
- 原句 9 的九十岁：`:175` 前文 `Just before turning ninety`，md 写"临终前"与原文一致。

## 结论

阻断 0 / 提示 2（篇幅计数，已修）/ 假红 0。
