# ch22 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句10 中英夹杂（他’d meant it）与“两本书” | `text/ch22_chapter_twenty_two.txt:205` | ——他把这句话刻进了骨髓。/本书的开头与中段 | 提示 |

## 覆盖率

- 逐字：R2 全块核验通过（`2-machine.json`）
- 对应：本章逐块 R4 已做（10 块）
- 形态：`chapter.sh` 报告 H1 / 导航 / 子项 / 块数 均合规
- 断言：R3 与 R1 素读 12 条逐条比对

## 已核实为正确（防误修）

- 一拳：`text/ch22_chapter_twenty_two.txt:130` 原文 `cracked against his father’s cheekbone` —— 回原文核对成立，后续不得以“读着不对”改动
- 人质：`text/ch22_chapter_twenty_two.txt:148` 原文 `have him transferred here` —— 回原文核对成立，后续不得以“读着不对”改动
- 违抗月亮：`text/ch22_chapter_twenty_two.txt:202` 原文 `I’ll defy the moon` —— 回原文核对成立，后续不得以“读着不对”改动
