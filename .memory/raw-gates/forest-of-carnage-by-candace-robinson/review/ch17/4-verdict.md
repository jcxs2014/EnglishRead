# ch17 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句2 关键词 carnival 不在本块引语内（在上一段叙事） | `text/ch17_chapter_seventeen.txt:34` | 关键词：expect / servant；并在分析中标明“上文那句” | 提示 |
| 原句6 残句（“露出地 下面”） | `text/ch17_chapter_seventeen.txt:145` | 在语言层露出地表 | 提示 |

## 覆盖率

- 逐字：R2 全块核验通过（`2-machine.json`）
- 对应：本章逐块 R4 已做（8 块）
- 形态：`chapter.sh` 报告 H1 / 导航 / 子项 / 块数 均合规
- 断言：R3 与 R1 素读 14 条逐条比对

## 已核实为正确（防误修）

- 全程有观众：`text/ch17_chapter_seventeen.txt:40` 原文 `All of it` —— 回原文核对成立，后续不得以“读着不对”改动
- 石沿保证：`text/ch17_chapter_seventeen.txt:109` 原文 `I won’t let you fall` —— 回原文核对成立，后续不得以“读着不对”改动
- 不是狼/不是人类：`text/ch17_chapter_seventeen.txt:0` 原文 `why couldn’t you have just been a fucking wolf` —— 回原文核对成立，后续不得以“读着不对”改动
