# ch02 4-verdict（R4 逐块 + R5 判定）

R2 机器层：2-machine.json rc=0，10 块 10 引语，issues 全空。
R4 人判：10/10 块逐对核 + 施事三问。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 块4 读者视角把 Nate 的伤系于「五年前 Duck Lake Massacre」、卖车系于「中枪昏迷期间」 | text/ch02_1_crow_guts_anonymous.txt:41「It had been **four months** since the **wreck** that would eventually kill his friend down the hall」；块4 引语「shattered pancreas and spleen」（车祸伤型）；素读#2/#3 | 伤与昏迷均为**四个月前车祸**；五年前枪击是另一次（已愈）事件 | **阻断** |
| 块6 点火故事亲属链（曾祖父迷路/曾祖母发起/年幼的父亲点火） | text 原句6「my dad's dad…my dad's grandma…she got my dad to use the lighter…to show her son」 | 三代称谓自洽（说话人=Nate，my dad=Victor） | 已核实为正确 |
| 导航 12 概括漏「Then it got me run over」 | text/ch02:624 | 压缩转述可接受 | 提示（不修） |
| Seine 「读了两遍笔记本」（素读#5）与导航「顺走皮袋和笔记本」 | 素读#5 anchor；text「first thing she spirited away」暗示另有物件 | 一致 | 已核实为正确 |

取证命令记录：
- `/usr/bin/grep -n "four months" text/ch02_1_crow_guts_anonymous.txt` → 行41；退出码 0
- `/usr/bin/grep -n "tried" text/ch02_1_crow_guts_anonymous.txt` → 行200/624/633；退出码 0

## 已核实为正确

- 块6 亲属链（my dad's dad＝Nate 曾祖父、my dad's grandma＝Nate 曾祖母、点火的孩子＝年幼的 Victor）——口语化原文经说话人定位（Nate 转述父亲）后自洽，后续不得以「读着别扭」改动。
- 块8「他那时九岁」为男孩年龄（He was nine. Nine years old.），与素读#6「父亲死后九年」是两个不同「九」，md 未混淆。
- 块10「somebody all the way up here」译「远在这儿的某个人」方向无误（Seine 指 Carlisle 方向的存在）。

**结论：阻断 1（块4 时间线）、提示 1（不修）。**
