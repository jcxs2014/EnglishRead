# ch21 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句1 中文理解含引语外内容（“他盼着我们放了你”） | `text/ch21_chapter_twenty_one.txt:16` | 引语扩至 I can promise you that. | 阻断 |
| 原句2 中文理解含引语外内容（背对折纸、纸森林垂挂） | `text/ch21_chapter_twenty_one.txt:22` | 只留引语内的纸雕内容 | 阻断 |
| 原句4 中文理解整段是上一段她的话（引语是他的一句） | `text/ch21_chapter_twenty_one.txt:40` | 只留他抽身与问话 | 阻断 |
| 原句7 中文理解含引语外内容（“为了救你”“表情会很难看”） | `text/ch21_chapter_twenty_one.txt:76` | 只留引语内的拆穿句 | 阻断 |
| 原句2 计数断言（纸艺第五次出场）不可核 | `text/ch21_chapter_twenty_one.txt:28` | 纸艺又一次出场 | 提示 |

## 覆盖率

- 逐字：R2 全块核验通过（`2-machine.json`）
- 对应：本章逐块 R4 已做（10 块）
- 形态：`chapter.sh` 报告 H1 / 导航 / 子项 / 块数 均合规
- 断言：R3 与 R1 素读 12 条逐条比对

## 已核实为正确（防误修）

- 纸雕无惧：`text/ch21_chapter_twenty_one.txt:28` 原文 `walking without fear` —— 回原文核对成立，后续不得以“读着不对”改动
- 我忠于 Winter：`text/ch21_chapter_twenty_one.txt:216` 原文 `I’m true to Prince Winter` —— 回原文核对成立，后续不得以“读着不对”改动
- 最脏一句：`text/ch21_chapter_twenty_one.txt:219` 原文 `The way your grandmother did` —— 回原文核对成立，后续不得以“读着不对”改动
