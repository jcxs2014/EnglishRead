# ch12 判定表（R4 逐块 + 断言）

> 覆盖声明：本章 **全章人判**（R1→R4 完整），10/10 块逐块核对「引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写」并逐块问施事三问（谁做的／谁的／谁说的）；引语逐字由 R2（2-machine.json）与 verbatim 全量复核（全书 204/208，另 4 条已证为 epub `<img alt>` 插页转写，非伪造）。

| 块 | 引语 ↔ 分析对应 | 施事三问（谁做/谁受/谁说） | 跨章引用/数字 | 档位 |
|---|---|---|---|---|
| 1 | ✓「thirty minutes」与「weeks in complete darkness」的对照 → 孤独的计量 | 说＝Petra（内心）；受＝自己；做＝（回想） | thirty minutes ✓（:73） | 通过 |
| 2 | ✓「smarter than you are」→ 死者书被没收的争辩 | 说＝Flint；受＝Jade；做＝Flint 抢回书 | 无跨章引用 | 通过 |
| 3 | ✓「You never had to go hungry」→ 旧账被翻出 | 说＝Jade；受＝Flint；说＝Petra 反驳「I'm not lying」 | no 跨章引用 | 通过 |
| 4 | ✓「send Gimm off to his grave」＋只留下署名地图 → 善意的偷窃 | 做＝Flint 送别并收地图；受＝Gimm 遗体；说＝Flint | 沉水而非入土（见错 3）；署名地图来自 :127/:129 ✓ | 通过 |
| 5 | ✓「there's always going to be time to think about the bad things」→ 逃不掉 | 说＝Petra（内心）；受＝自己；做＝（承认） | 与 ch14 的 mindripper 余波同线 ✓ | 通过 |
| 6 | ✓「his dad stole the relic from yours」→ 两个家族的对立（**中文主语错位，见错 1**） | 说＝Jade；受＝Petra（点头）；做＝Jade 断言 | 原文 :199 ✓；:207 Jade 的实际指控 ✓ | 阻断 |
| 7 | ✓「Don't look into the eyes of anything… keep these in your ears」→ 三条规矩 | 说＝Flint；受＝Petra/Jade；做＝Flint 立规 | 与 :247/:251 连成三条 ✓ | 通过 |
| 8 | ✓ 多锚点打结 → 规矩的技术细节 | 说＝Flint；做＝Flint 示范打结；受＝Petra/Jade | 无跨章引用 | 通过 |
| 9 | ✓「he's letting it unspool」→ 第一个破规矩的人 | 做＝Flint 松绳；受＝Petra（拽住）；说＝旁白 | 与 :345「which means Flint must've let go」✓ | 通过 |
| 10 | ✓ 绳被猛地拽走 → 她最守的东西被夺 | 做＝未知之物；受＝Petra（绳被夺）；说＝旁白 | 「The line is ripped from my hands.」✓（:381） | 通过 |

**关键词锚定**：10 块关键词均取自本块引语（gate ⑱ 阻断 0；check_vocab 全书 FAIL 0 / WARN 0）。

## 已核实为正确（防误修；后续不得以「读着不对」改动）
- 沉水而非入土：`text/ch12_chapter_twelve.txt:165`「We'll have to send Gimm off to his grave」；`:169`「Flint nudges Gimm off the rock. The bag slides into the water, and for a moment it floats there, until the fabric soaks through, then it sinks into the darkness.」
- 主语依据：同章 :199「And his dad stole the relic from yours and left him for dead.」；`:207`「Flint's a selfish thief, just like his dad. That's why he stole from my donations.」；`:209`「Slowly, I nod.」
- 层级与时序：同章 :29（第三层水下通道）、:59-73（Gimm 尸体在第四层小岩岛）、:305/:307（进入 Blackout Sea，97% 水下、最深两千英尺）。
- 「他会害死我们」查无：`/usr/bin/grep -n -i "kill us|kill you|get us killed" text/ch12_chapter_twelve.txt` → 无输出，退出码 1。
- 三条规矩：同章 :239（不看眼睛、戴耳塞）、:247（绳永不放手）、:251（多点打结）。
