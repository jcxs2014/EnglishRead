# ch12 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句8 中文理解含引语外内容（纸作品清单） | `text/ch12_chapter_twelve.txt:208` | 删去清单，只留问话 | 阻断 |
| 原句3 “乱伦式的宫廷腐坏”措辞失准（原文无乱伦） | `text/ch12_chapter_twelve.txt:85` | 宫廷的腐坏 | 提示 |
| 原句7 夹生英文（say liar） | `text/ch12_chapter_twelve.txt:184` | 狼歪头说“骗子” | 提示 |
| 原句9 读者提示把“被捏碎的纸花”记在 ch08（实为 ch04） | `text/ch12_chapter_twelve.txt:0` | ch04 被捏碎的纸花 | 提示 |

## 覆盖率

- 逐字：R2 全块核验通过（`2-machine.json`）
- 对应：本章逐块 R4 已做（9 块）
- 形态：`chapter.sh` 报告 H1 / 导航 / 子项 / 块数 均合规
- 断言：R3 与 R1 素读 10 条逐条比对

## 已核实为正确（防误修）

- 药瓶算计：`text/ch12_chapter_twelve.txt:13` 原文 `knock them over` —— 回原文核对成立，后续不得以“读着不对”改动
- 更好的公主：`text/ch12_chapter_twelve.txt:19` 原文 `a better princess` —— 回原文核对成立，后续不得以“读着不对”改动
- Chaos：`text/ch12_chapter_twelve.txt:223` 原文 `Chaos` —— 回原文核对成立，后续不得以“读着不对”改动
