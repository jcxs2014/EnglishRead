# ch15 4-verdict（R4 逐块 + R5 判定）

R2 机器层：2-machine.json rc=0，15 块 15 引语，issues 全空。
R4 人判：15/15 块逐对核 + 施事三问。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 素读#5「soaked up the blood」未入块12 引语 | 素读 anchor 命中 True | 相邻语义自明 | 提示（不修） |
| 块14 施事表述「Nate（现在是 Christian 的身体）正在亲手杀死」 | 引语「he was the mummy now」「You catch him by the ankle, Nate sort of heard from inside」 | 行动身体=Nate（被占据），表述与原文视角一致 | 已核实为正确 |
| 块5「Seine 系 Francis Heavy Runner 表亲」 | 引语「If she was Francis Heavy Runner's cousin like she definitely was?」；素读#6 | 一致 | 已核实为正确 |

取证命令记录：
- `/usr/bin/grep -c "the kind a kid and his grandmother build to pull a lost hunter in" text/ch15_14_criss_cross_applesauce.txt` → 1；退出码 0
- `/usr/bin/grep -c "It was what he’d been the night of the Duck Lake Massacre" …` → 1；退出码 0（直撇号变体 0，词表撇号形态正确）
- 素读 anchor 偏移验证 True ×8

## 已核实为正确

- 块4「criss-cross-applesauce」的章名解读（盘腿坐姿势＋Nate 与 D 反复分手复合的比喻）——引语原文「the Romeo and Juliet of the reservation, just, Indian-style, criss-cross-applesauce」双重含义均在原文内。
- 块7 X 形皮绳与 Christian 圣经的连接（「Christian who tied his bible with that X of bootlace」）——块13 引语自证。
- 块15「the stout Indian…flat eyes」保持悬念不作指认——原文未揭示身份，md 同样不指认。

**结论：阻断 0、提示 1（不修）。本章干净。**
