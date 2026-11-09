# ch18 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句4 中文理解含引语外内容（父亲讽刺他不给新娘拉椅） | `text/ch18_chapter_eighteen.txt:94` | 删去引语外动作，只留“他反手把她按跪在脚边” | 阻断 |
| 原句5 中文理解含引语外内容（脚踩餐具位）＋英文误引（spoil food） | `text/ch18_chapter_eighteen.txt:115` | 删去脚踩动作；“spoil food”改为“spoiled food” | 阻断 |
| 原句6 中文理解含引语外内容（倒完酒想坐下、靴子勾椅） | `text/ch18_chapter_eighteen.txt:139` | 只留引语内的毁约台词 | 阻断 |
| 原句8 中文理解含引语外内容（血溅上脸、大脑空白） | `text/ch18_chapter_eighteen.txt:243` | 只留引语内的动作 | 阻断 |
| 原句2 错字（着辱戏） | `text/ch18_chapter_eighteen.txt:70` | 宴会的羞辱戏 | 提示 |
| 原句9 计数断言（bored 模式第四次）不可核 | `text/ch18_chapter_eighteen.txt:252` | 又一次登场 | 提示 |

## 覆盖率

- 逐字：R2 全块核验通过（`2-machine.json`）
- 对应：本章逐块 R4 已做（10 块）
- 形态：`chapter.sh` 报告 H1 / 导航 / 子项 / 块数 均合规
- 断言：R3 与 R1 素读 12 条逐条比对

## 已核实为正确（防误修）

- 跪、斟酒、抽椅：`text/ch18_chapter_eighteen.txt:112` 原文 `pour every pack member’s drink` —— 回原文核对成立，后续不得以“读着不对”改动
- 递叉暗号：`text/ch18_chapter_eighteen.txt:195` 原文 `pass the utensil to Sterling` —— 回原文核对成立，后续不得以“读着不对”改动
- Talia 之死：`text/ch18_chapter_eighteen.txt:246` 原文 `yanked his claws from Talia’s torn throat` —— 回原文核对成立，后续不得以“读着不对”改动
