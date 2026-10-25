# ch03 · T3 判定表

- 章：`ch03 the notecard.md`；原文 `text/` 本章提取件
- R1 素读：`1-suread.json`（**machine-anchors**；8 条机械锚点，唯一性实测；无人工事实描述 ⇒ R3「漏」只作抽样级判断）
- R2 机器层：`2-machine.json`（verdict=ok；5 块 / 13 片段 / segment_miss=0）
- R3 对账：`3-diff.md`
- 覆盖：**抽样 3/5 块逐块 R4**（首/中/末块）＋ 全章机器层 ＋ §0.2 类级扫描 ＋ 词汇层/导航层全量锚定；其余块未做逐块人判。

## R4 逐块对应（抽样：首 / 中 / 末块）

| 块 | 词数 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|
| 原句1 | 50 | ✓ | 消失墨水 → 毒/酸烧指尖，忠实 | 无反转 | 通过 |
| 原句3 | 70 | ✓ | 卡片落下又升起 → 浮回餐巾纸，忠实 | 无反转 | 通过 |
| 原句5 | 56 | ✓ | 愧疚驯服 → 走到路口、巴士冲来，忠实 | 无反转 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 ＋ 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 词汇层例句 monogrammed | `text/ch03_chapter_two.txt:34`："There’s a stack of cloth napkins monogrammed with Professor Shiran’s initials on the next table; I wrap my hand in one of them and pick up the card like it’s a grenade." | 原 md 例句把原文分号改成句号并截断 ⇒ 逐字不符 | 阻断（已修） |

## 分组计数（只报四组）

- **逐字**：5/5 块整串命中，查无 0（`2-machine.json` verdict=ok；13 片段逐条回查，segment_miss=0）
- **对应**：阻断 1，提示 0（抽样块的中文均在讲本块引语，施事/受事无反转）
- **形态**：阻断 0（导航 5 项齐 · 4 子项齐备 · 编号连续无撞车 · 块词数 50–70 落库内常见区间）
- **断言**：阻断 1，提示 0，未核 0

## 阻断

- **[断言]** 词汇层例句 monogrammed
  - 证据：`text/ch03_chapter_two.txt:34`："There’s a stack of cloth napkins monogrammed with Professor Shiran’s initials on the next table; I wrap my hand in one of them and pick up the card like it’s a grenade."
  - 处理：原 md 例句把原文分号改成句号并截断 ⇒ 逐字不符

## 提示（只记不改）

- （无）
