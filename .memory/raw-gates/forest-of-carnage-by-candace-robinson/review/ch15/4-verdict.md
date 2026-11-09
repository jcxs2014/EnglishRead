# ch15 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句12 读者提示伪造 ch12 引语（his eyes glowed with their own cruelty 只在 ch15 出现） | `text/ch15_chapter_fifteen.txt:295` | 删去伪造引语与章号，只保留父子同源的判断 | 阻断 |
| 原句1 读者提示悬空分号 | `text/ch15_chapter_fifteen.txt:16` | …拉到顶。 | 提示 |
| 原句11 夹生英文（her words hit something） | `text/ch15_chapter_fifteen.txt:271` | 她那句话扎到了他——失控的前兆被动词出卖 | 提示 |

## 覆盖率

- 逐字：R2 全块核验通过（`2-machine.json`）
- 对应：本章逐块 R4 已做（13 块）
- 形态：`chapter.sh` 报告 H1 / 导航 / 子项 / 块数 均合规
- 断言：R3 与 R1 素读 12 条逐条比对

## 已核实为正确（防误修）

- 一箭金眼：`text/ch15_chapter_fifteen.txt:16` 原文 `between its golden eyes` —— 回原文核对成立，后续不得以“读着不对”改动
- 五头狼：`text/ch15_chapter_fifteen.txt:43` 原文 `the five wolves` —— 回原文核对成立，后续不得以“读着不对”改动
- 两晚后仪式：`text/ch15_chapter_fifteen.txt:319` 原文 `Two nights from now` —— 回原文核对成立，后续不得以“读着不对”改动
