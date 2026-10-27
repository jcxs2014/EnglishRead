# ch17 4-verdict（R4 逐块 + R5 判定）

R2 机器层：2-machine.json rc=0，15 块 15 引语，issues 全空。
R4 人判：15/15 块逐对核 + 施事三问。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 块1 分析把滴答声解读为「记忆中的钟」，未及后文实体揭示 | text/ch17:83「The tick-tick-ticking that had brought Nate back was tapping, was Mooch's ice pick in her trapped right hand」 | 引语本身是 Nate 猜测（问号）无误；分析未跟后文揭示，建议补一句 | 提示（建议修，本轮不改稿） |
| 素读#2/#5 细节未入块（挂窗帘杆／Shell-Brady-Connie 认领） | 素读 anchor 命中 True ×2 | 细节级；Connie 认领与 ch13 呼应 | 提示（不修） |
| 块12 木马计因果链 | 引语「wooden-horse trick…infected blankets…came for the kids because they were better」；素读#8 | 一致 | 已核实为正确 |

取证命令记录：
- `/usr/bin/grep -n "tick-tick-ticking" text/ch17_16_war_party.txt` → 行83；退出码 0
- 素读 anchor 偏移验证 True ×8

## 已核实为正确

- 块5「That was for Trace」与素读#3 完全一致（含「most Blackfeet thing」的 Nate 评语）。
- 块13「tongue-stump spasming」译「舌根残端痉挛」——与 ch07 断舌设定一致，未误写为「舌头」。
- 块15「So long as you've got what I'm here for」——Benjamin 的动机句，与素读#8 后文「索回笔记本」一致（ch08 修复后引语头部已归并格式项）。

**结论：阻断 0、提示 2（1 建议修滴答声揭示、1 不修）。本章基本干净。**
