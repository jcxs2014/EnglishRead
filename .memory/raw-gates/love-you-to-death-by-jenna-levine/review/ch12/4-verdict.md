# ch12 · T3 判定表

- 章：`ch12 the search history.md`；原文 `text/` 本章提取件
- R1 素读：`1-suread.json`（**independent-suread**；8 条人工事实 + 转折点，锚点经中央脚本 `t3_suread_fix.py` fail-closed 核验）
- R2 机器层：`2-machine.json`（verdict=ok；7 块 / 22 片段 / segment_miss=0）
- R3 对账：`3-diff.md`
- 覆盖：**抽样 3/7 块逐块 R4**（首/中/末块）＋ 全章机器层 ＋ §0.2 类级扫描 ＋ 词汇层/导航层全量锚定；其余块未做逐块人判。

## R4 逐块对应（抽样：首 / 中 / 末块）

| 块 | 词数 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|
| 原句1 | 51 | ✓ | 搜索记录 → 厌恶自己，忠实 | 无反转 | 通过 |
| 原句4 | 66 | ✓ | 半显形吓人 → 两人尖叫逃走，忠实 | 无反转 | 通过 |
| 原句7 | 62 | ✓ | 三小时内部邮递 → 地狱来找麻烦，忠实 | 无反转 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 ＋ 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 原句 7 中文理解「要是不在三小时内把它交进 Agency 的内部邮递系统」 | `text/ch12_chapter_eleven.txt:157`："If I don’t get this into the Agency’s interoffice mail system in three hours, there will be Hell to pay. Literally and metaphorically." | 成立：中文「字面意义上的，也有比喻意义上的」逐字对应 | 提示（已核实为正确） |
| 与 ch10 的六句话表单混淆之虞 | `text/ch10_chapter_nine.txt / text/ch12_chapter_eleven.txt:112`："Due: Six hours after receipt.（ch12 表单）／ch10 为 six sentences" | 两处表单不同（ch10＝六句话·住所反应；ch12＝五句话·弹球机），md 未混淆 | 提示（已核实为正确） |

## 分组计数（只报四组）

- **逐字**：7/7 块整串命中，查无 0（`2-machine.json` verdict=ok；22 片段逐条回查，segment_miss=0）
- **对应**：阻断 0，提示 2（抽样块的中文均在讲本块引语，施事/受事无反转）
- **形态**：阻断 0（导航 5 项齐 · 4 子项齐备 · 编号连续无撞车 · 块词数 51–74 落库内常见区间）
- **断言**：阻断 0，提示 1，未核 0

## 提示（只记不改）

- **提示** 原句 7 中文理解「要是不在三小时内把它交进 Agency 的内部邮递系统」 —— 成立：中文「字面意义上的，也有比喻意义上的」逐字对应
- **提示** 与 ch10 的六句话表单混淆之虞 —— 两处表单不同（ch10＝六句话·住所反应；ch12＝五句话·弹球机），md 未混淆
