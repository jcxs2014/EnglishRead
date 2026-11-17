# ch27 判定表（T3 深审 R1→R4 全覆盖）

覆盖声明：本书 35 章全部走 R1→R4（用户指令全量、无抽样）。R1 素读 9 条先于开 md；R2 机器 verdict=ok（rc=0）；R3 对账见 3-diff.md；R4 逐块人判（施事三问/对应/跨章章号/第一唯一数字）由主会话执行。

| 断言 | 证据（章:区间/命令） | 结论 | 档位 |
|---|---|---|---|
| 引语逐字（12 块） | quotes.py verbatim --full 411/411 · fragments 431 片段 0 MISS | 对应成立 | 通过 |
| 关键词 lane ⑱ | gate EXIT=0（修复后） | 成立 | 通过 |
| 原句1 读者视角提示：它与 ch15 的「二十个 angheal 幼崽」互为倒影 | 同 ch20 取证；与 ch20 同因跨章 | 已修复 → 它与 ch11 的「二十个 angheal 幼崽」互为倒影 | 阻断（已整改） |
| 原句7 读者视角提示：这是 Darragh 的第二次正式道歉（第一次在 ch19） | 取证：/usr/bin/grep -ln 'I apologize' text/ch1*.txt → ch17 命中（Darragh：My lady, I apologize）；ch19 无道歉 | 已修复 → 这是 Darragh 的第二次正式道歉（第一次在 ch17） | 阻断（已整改） |
| 原句10 读者视角提示：上一章她把嘴粘死 | 蜜嘴在 ch25，本书 ch27 的上一章是 ch26 | 已修复 → 前两章她把嘴粘死 | 阻断（已整改） |
| 原句5 关键词：driving me wild / swathed in crystals and satin / You're driving me wild tonight | 关键词包含关系重复 | 已修复 → driving me wild / swathed in crystals and satin / keep picturing | 提示（已整改） |

## 已核实为正确
- 21+9 伤亡 → text/ch27 'Twenty-one of Gabriel's soldiers…nine civilians'
- Darragh 衬衫浸血 → text/ch27 'his shirt was wet with blood'

## 已核实为正确（防误修护栏）
凡写入本节者，后续不得以「读着不对」为由改动，除非给出反证。
