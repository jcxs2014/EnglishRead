# ch10 · T3 判定表

- 章：`ch10 the sealed parchment.md`；原文 `text/` 本章提取件
- R1 素读：`1-suread.json`（**independent-suread**；8 条人工事实 + 转折点，锚点经中央脚本 `t3_suread_fix.py` fail-closed 核验）
- R2 机器层：`2-machine.json`（verdict=ok；5 块 / 15 片段 / segment_miss=0）
- R3 对账：`3-diff.md`
- 覆盖：**抽样 3/5 块逐块 R4**（首/中/末块）＋ 全章机器层 ＋ §0.2 类级扫描 ＋ 词汇层/导航层全量锚定；其余块未做逐块人判。

## R4 逐块对应（抽样：首 / 中 / 末块）

| 块 | 词数 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|
| 原句1 | 50 | ✓ | 羊皮纸 → 关门攥紧，忠实 | 无反转 | 通过 |
| 原句3 | 58 | ✓ | 她的家 vs Agency 房间 → 抱住她才不黯然，忠实 | 无反转 | 通过 |
| 原句5 | 58 | ✓ | 六句话观察表 → 交回期限，忠实 | 无反转 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 ＋ 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 导航「百年冷面被一个人融化」 | `text/ch10_chapter_nine.txt:15`："The Agency—where I have dwelled for more than a century—is all blank walls and sterile, featureless rooms." | 这是 trope 名（中文习语），不是对原文的事实断言；原文对应量级为 more than a century | 提示（假红） |

## 分组计数（只报四组）

- **逐字**：5/5 块整串命中，查无 0（`2-machine.json` verdict=ok；15 片段逐条回查，segment_miss=0）
- **对应**：阻断 0，提示 1（抽样块的中文均在讲本块引语，施事/受事无反转）
- **形态**：阻断 0（导航 5 项齐 · 4 子项齐备 · 编号连续无撞车 · 块词数 50–66 落库内常见区间）
- **断言**：阻断 0，提示 0，未核 0

## 提示（只记不改）

- **提示** 导航「百年冷面被一个人融化」 —— 这是 trope 名（中文习语），不是对原文的事实断言；原文对应量级为 more than a century
