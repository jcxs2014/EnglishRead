# ch11 4-verdict（R4 逐块 + R5 判定）

R2 机器层：2-machine.json rc=0，12 块 12 引语，issues 全空。
R4 人判：12/12 块逐对核 + 施事三问。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 块1「蓝星呼应 ch04 Conrad 连体服上的珠饰」 | text/ch04:95 对假人仅记「fringed gloves and a chalky helmet with a gold face shield」；ch11 引语「never wore the suit you're wearing」 | ch04 无珠饰、Conrad 未穿过该套装——联想无据 | 提示（建议修：删「珠饰」或改「金面罩头盔」） |
| 块2 读者视角引「It's a good time to be awake again」 | text/ch11:74/77 两处 | 有据 | 已核实为正确 |
| 块11 读者视角「带着孩子的一家四口」 | text/ch11:260「A family of four, two parents and…twins of no more than eight」 | 有据 | 已核实为正确 |
| 块10「铁钉不会粘面罩——那是磁铁」 | 引语「iron studs…won't adhere to your face shield」；ch10 舌头磁铁设定（素读#4） | 解读自洽 | 已核实为正确 |

取证命令记录：
- `/usr/bin/grep -in "blue star\|stars" text/ch04_3_pretty_good_for_an_indian.txt` → 行95（无蓝星）；退出码 0
- `/usr/bin/grep -n "awake" text/ch11_10_indian_evel_knievel.txt` → 行74/77；退出码 0
- `/usr/bin/grep -in "family\|four of them\|whole family" text/ch11_10_indian_evel_knievel.txt` → 行260/371；退出码 0

## 已核实为正确

- 块6「糖浆」归属 Seine 的链路：块6 引语「One of these occupants knows this color」→ ch12 她吸食骨粉（下一章）——md 未点名「Seine」而是保留原文的悬念指称，处理正确。
- 块9 假留言内容「Mom, Mom… I saw Dad…」与素读#7 逐字一致；「别让窃笑被录进去」的恶意机制（故意中断留白）转述无误。
- 块3「That still does」译「现在依然如此」——泥土仍持有血与腐坏的记忆，时态无误。

**结论：阻断 0、提示 1（建议修，非事实错误）。本章基本干净。**
