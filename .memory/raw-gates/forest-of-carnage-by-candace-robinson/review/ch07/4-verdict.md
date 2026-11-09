# ch07 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句5 读者提示称 Bael 在 ch06“执行绑票”，原文只写他指认肉店位置 | `text/ch07_chapter_seven.txt:0` | ch06 在肉店外盯梢定位 | 提示 |
| 原句9 读者提示的英文非逐字（I let you go） | `text/ch07_chapter_seven.txt:0` | “If I let you go” | 提示 |
| 原句10 读者提示“翻转两本书”（本书只有一本） | `text/ch07_chapter_seven.txt:256` | 这一句同时翻转两代人的账 | 提示 |

## 覆盖率

- 逐字：R2 全块核验通过（`2-machine.json`）
- 对应：本章逐块 R4 已做（11 块）
- 形态：`chapter.sh` 报告 H1 / 导航 / 子项 / 块数 均合规
- 断言：R3 与 R1 素读 10 条逐条比对

## 已核实为正确（防误修）

- 两箭杀 Bael（穿眼+穿颈）：`text/ch07_chapter_seven.txt:130` 原文 `piercing the shifter straight through the eye` —— 回原文核对成立，后续不得以“读着不对”改动
- 吊笼：`text/ch07_chapter_seven.txt:205` 原文 `a large metal cage hanging from the ceiling` —— 回原文核对成立，后续不得以“读着不对”改动
- 外婆猎人首领：`text/ch07_chapter_seven.txt:256` 原文 `once the leader of the hunters` —— 回原文核对成立，后续不得以“读着不对”改动
