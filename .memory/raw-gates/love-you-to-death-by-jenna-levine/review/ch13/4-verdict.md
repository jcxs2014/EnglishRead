# ch13 · T3 判定表

- 章：`ch13 monday.md`；原文 `text/` 本章提取件
- R1 素读：`1-suread.json`（**machine-anchors**；8 条机械锚点，唯一性实测；无人工事实描述 ⇒ R3「漏」只作抽样级判断）
- R2 机器层：`2-machine.json`（verdict=ok；11 块 / 33 片段 / segment_miss=0）
- R3 对账：`3-diff.md`
- 覆盖：**抽样 3/11 块逐块 R4**（首/中/末块）＋ 全章机器层 ＋ §0.2 类级扫描 ＋ 词汇层/导航层全量锚定；其余块未做逐块人判。

## R4 逐块对应（抽样：首 / 中 / 末块）

| 块 | 词数 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|
| 原句1 | 54 | ✓ | 周一犹豫三十分钟，忠实 | 无反转 | 通过 |
| 原句6 | 86 | ✓ | 「他抱着我的时候感觉有多好」，忠实 | 无反转 | 通过 |
| 原句11 | 86 | ✓ | 去喝一杯 → 套近乎，忠实 | 无反转 | 通过 |

## R5 判定表

| 断言 | 证据（text/ 文件:行 ＋ 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 词汇层/正文「sad little cardboard box」三个词 | `text/ch13_chapter_twelve.txt:169`："I am safely out of the building with my sad little cardboard box" | **真缺陷**：原文是「sad little cardboard box」＝**四个词**（sad/little/cardboard/box），md 原写「"sad little"三个词」既指代错、词数也错 ⇒ 改为「sad little cardboard box 这个四词短语」 | 阻断（已修） |

## 分组计数（只报四组）

- **逐字**：11/11 块整串命中，查无 0（`2-machine.json` verdict=ok；33 片段逐条回查，segment_miss=0）
- **对应**：阻断 1，提示 0（抽样块的中文均在讲本块引语，施事/受事无反转）
- **形态**：阻断 0（导航 5 项齐 · 4 子项齐备 · 编号连续无撞车 · 块词数 39–86 落库内常见区间）
- **断言**：阻断 1，提示 0，未核 0

## 阻断

- **[断言]** 词汇层/正文「sad little cardboard box」三个词
  - 证据：`text/ch13_chapter_twelve.txt:169`："I am safely out of the building with my sad little cardboard box"
  - 处理：**真缺陷**：原文是「sad little cardboard box」＝**四个词**（sad/little/cardboard/box），md 原写「"sad little"三个词」既指代错、词数也错 ⇒ 改为「sad little cardboard box 这个四词短语」

## 提示（只记不改）

- （无）
