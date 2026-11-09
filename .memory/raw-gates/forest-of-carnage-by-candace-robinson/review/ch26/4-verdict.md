# ch26 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句4 中文理解含引语外内容（缓步下小径、口袋里的礼物） | `text/ch26_epilogue.txt:52` | 删去引语外动作 | 阻断 |
| 原句7 中文理解含引语外内容（他把她拉进储藏室） | `text/ch26_epilogue.txt:79` | 只留引语内台词 | 阻断 |
| 原句6 跨章引用章号错（ch09 → ch04） | `text/ch26_epilogue.txt:0` | 对照 ch04 | 提示 |

## 覆盖率

- 逐字：R2 全块核验通过（`2-machine.json`）
- 对应：本章逐块 R4 已做（12 块）
- 形态：`chapter.sh` 报告 H1 / 导航 / 子项 / 块数 均合规
- 断言：R3 与 R1 素读 12 条逐条比对

## 已核实为正确（防误修）

- 满月宴是幌子：`text/ch26_epilogue.txt:16` 原文 `it was all a ruse` —— 回原文核对成立，后续不得以“读着不对”改动
- 两小时前到齐：`text/ch26_epilogue.txt:25` 原文 `arrived two hours ago` —— 回原文核对成立，后续不得以“读着不对”改动
- 婚戒由来：`text/ch26_epilogue.txt:162` 原文 `the key to your cage reforged` —— 回原文核对成立，后续不得以“读着不对”改动
