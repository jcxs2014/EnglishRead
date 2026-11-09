# ch03 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句4 中文理解含引语外内容（“到手后还能活多久”） | `text/ch03_chapter_three.txt:34` | 引语扩至 One she hoped to never answer. | 阻断 |

## 覆盖率

- 逐字：R2 全块核验通过（`2-machine.json`）
- 对应：本章逐块 R4 已做（8 块）
- 形态：`chapter.sh` 报告 H1 / 导航 / 子项 / 块数 均合规
- 断言：R3 与 R1 素读 10 条逐条比对

## 已核实为正确（防误修）

- 三箭毙狼：`text/ch03_chapter_three.txt:22` 原文 `released another two arrows` —— 回原文核对成立，后续不得以“读着不对”改动
- 近三周摄政：`text/ch03_chapter_three.txt:133` 原文 `nearly three weeks` —— 回原文核对成立，后续不得以“读着不对”改动
- 悬赏要活的：`text/ch03_chapter_three.txt:34` 原文 `But alive` —— 回原文核对成立，后续不得以“读着不对”改动
