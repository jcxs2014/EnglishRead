# ch01 4-verdict（R4 逐块 + R5 判定）

R2 机器层：2-machine.json rc=0，10 块 10 引语，issues 九键全空。
R4 人判：10/10 块逐对核（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写），施事三问每块已问。

| 断言 | 证据（章:区间/行） | 结论 | 档位 |
|---|---|---|---|
| 块3 中文「朝腹腔涌去」方向与原文相反 | text/ch01_the_summer_indians.txt:101「surging away from what he knew now to call his abdominal cavity」；md 行30 | 应为「从腹腔涌离」；away from 被译成「朝…涌去」 | **阻断** |
| 素读#3「两名幸存者」未入 md | text:5253「one of only two to have made it through that night」 | 背景细节非关键转折，块3/块4 已间接覆盖 | 提示（不修） |
| 块9 读者视角「小钟砸中雪地小鹿」疑似虚构 | text/ch01:506「winced from what he was seeing in his head: that little clock landing out in the snow by the lake, right on top of one of those tiny deer」 | 原文确有（Nate 的想象画面），md 表述与原文一致 | 假红（疑似，实正确） |
| 词汇例句抽查（fluttering / winter-warrior / low-ceilinged） | /usr/bin/grep -c 各命中 1，退出码 0 | 逐字成立 | 已核实为正确 |

取证命令记录：
- `/usr/bin/grep -n "surging away from" text/ch01_the_summer_indians.txt` → 行101；退出码 0
- `/usr/bin/grep -n "clock" text/ch01_the_summer_indians.txt` → 行236/383/389/434/506；退出码 0
- `/usr/bin/grep -c "his eyelids fluttering" …` → 1；退出码 0（另两条同）

## 已核实为正确

- 块9 读者视角「小钟砸在雪地里、正砸中一只小鹿」：text/ch01_the_summer_indians.txt:506 明写 "that little clock landing out in the snow by the lake, right on top of one of those tiny deer, the other one looking inside to who did this"（Nate 脑中想象）。后续不得以「读着不对」改动。
- 块2 施事链：he=Sebby、his dad=Sebby 的父亲（素读#5 anchor「he didn't get his claim check last year when he turned eighteen」与 md 一致）。
- 块4「they were fourteen」译「当时他们十四岁」；「running to get Nate's mom」译「跑去找 Nate 的妈妈」——方向无误。

**结论：阻断 1（块3 方向反转）、提示 1（不修，有据）、假红转正确 1。**
