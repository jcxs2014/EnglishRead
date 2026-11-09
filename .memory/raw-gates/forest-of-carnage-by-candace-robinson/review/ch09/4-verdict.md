# ch09 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句6 中文层夹生英文（whatever） | `text/ch09_chapter_nine.txt:145` | 眼底的情绪深藏不露 | 提示 |
| 原句7 读者提示“昨日撞墙”与原文不符（ch08 只回了一个 No） | `text/ch09_chapter_nine.txt:0` | 前一次一个“不”字、这一次直接摔墙 | 提示 |

## 覆盖率

- 逐字：R2 全块核验通过（`2-machine.json`）
- 对应：本章逐块 R4 已做（12 块）
- 形态：`chapter.sh` 报告 H1 / 导航 / 子项 / 块数 均合规
- 断言：R3 与 R1 素读 11 条逐条比对

## 已核实为正确（防误修）

- Bael 死讯两个弹着点：`text/ch09_chapter_nine.txt:58` 原文 `An arrow to the eye and another to the neck` —— 回原文核对成立，后续不得以“读着不对”改动
- 笼子是余生居所：`text/ch09_chapter_nine.txt:139` 原文 `primary quarters until the day you die` —— 回原文核对成立，后续不得以“读着不对”改动
- 石头首杀：`text/ch09_chapter_nine.txt:259` 原文 `slammed down the rock` —— 回原文核对成立，后续不得以“读着不对”改动
