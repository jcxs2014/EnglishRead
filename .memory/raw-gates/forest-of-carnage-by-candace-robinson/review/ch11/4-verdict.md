# ch11 · R5 判定表

报数四组：**逐字**（R2）/ **对应**（R4）/ **形态**（R2）/ **断言**（R3）。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 原句11 中文理解含引语外内容（“她裹着毛巾走出浴室”） | `text/ch11_chapter_eleven.txt:214` | 他削木刀的手停了 | 阻断 |
| 原句5 读者提示把气味段说成“这段”，实际在下一段 | `text/ch11_chapter_eleven.txt:109` | 紧接着的叙事里（她贴着他的胸口上楼时）…冒头 | 提示 |
| 原句8 中文理解“一刻钟”为无据细化（原文 a moment） | `text/ch11_chapter_eleven.txt:175` | 就让你见弟弟一面 | 提示 |

## 覆盖率

- 逐字：R2 全块核验通过（`2-machine.json`）
- 对应：本章逐块 R4 已做（11 块）
- 形态：`chapter.sh` 报告 H1 / 导航 / 子项 / 块数 均合规
- 断言：R3 与 R1 素读 11 条逐条比对

## 已核实为正确（防误修）

- 四名罪犯：`text/ch11_chapter_eleven.txt:13` 原文 `four criminals` —— 回原文核对成立，后续不得以“读着不对”改动
- 两处割伤：`text/ch11_chapter_eleven.txt:16` 原文 `only gained two cuts` —— 回原文核对成立，后续不得以“读着不对”改动
- 拒认赢局：`text/ch11_chapter_eleven.txt:37` 原文 `win. On your own` —— 回原文核对成立，后续不得以“读着不对”改动
