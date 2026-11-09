# ch10 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句8 读者提示称 ch01 Winter 以狼形扑击 Sterling，原文扑击者是狼群（非 Winter） | `text/ch10_chapter_ten.txt:0` | ch01 外婆家那一夜的扑杀（Sterling 被大狼按在地上） | 提示 |
| 原句9 夹生英文（ annoyed ex） | `text/ch10_chapter_ten.txt:138` | 从“烦人的前任”升级 | 提示 |

## 覆盖率

- 逐字：R2 全块核验通过（`2-machine.json`）
- 对应：本章逐块 R4 已做（10 块）
- 形态：`chapter.sh` 报告 H1 / 导航 / 子项 / 块数 均合规
- 断言：R3 与 R1 素读 10 条逐条比对

## 已核实为正确（防误修）

- 第一声惨叫不是她：`text/ch10_chapter_ten.txt:13` 原文 `too rough to belong to Sterling` —— 回原文核对成立，后续不得以“读着不对”改动
- 数十狼：`text/ch10_chapter_ten.txt:0` 原文 `sacrificed dozens of wolves` —— 回原文核对成立，后续不得以“读着不对”改动
- 仪式前夜被绿：`text/ch10_chapter_ten.txt:177` 原文 `The night before their mating ceremony` —— 回原文核对成立，后续不得以“读着不对”改动
