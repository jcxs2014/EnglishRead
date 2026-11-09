# ch25 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句1 中文理解含引语外内容（狼群不会像他那样宽容） | `text/ch25_chapter_twenty_five.txt:16` | 删去该句 | 阻断 |
| 原句5 中文理解含引语外内容（“那他不就没有继承人了？”） | `text/ch25_chapter_twenty_five.txt:49` | 删去该问句 | 阻断 |
| 原句6 中文理解含引语外整段对白（Rawling 撞门、我杀了他、浴室剧本） | `text/ch25_chapter_twenty_five.txt:61` | 只留引语内的王权宣告 | 阻断 |
| 原句10 中文理解含引语外内容（wear this、署名） | `text/ch25_chapter_twenty_five.txt:151` | 引语补全至 But, if you do come, wear this.（含中间句，保持连续） | 阻断 |

## 覆盖率

- 逐字：R2 全块核验通过（`2-machine.json`）
- 对应：本章逐块 R4 已做（12 块）
- 形态：`chapter.sh` 报告 H1 / 导航 / 子项 / 块数 均合规
- 断言：R3 与 R1 素读 13 条逐条比对

## 已核实为正确（防误修）

- 妻子不弃夫：`text/ch25_chapter_twenty_five.txt:34` 原文 `A wife doesn’t abandon her husband` —— 回原文核对成立，后续不得以“读着不对”改动
- Rawling 跪拜：`text/ch25_chapter_twenty_five.txt:70` 原文 `You are my alpha` —— 回原文核对成立，后续不得以“读着不对”改动
- 两周：`text/ch25_chapter_twenty_five.txt:97` 原文 `for two weeks` —— 回原文核对成立，后续不得以“读着不对”改动
