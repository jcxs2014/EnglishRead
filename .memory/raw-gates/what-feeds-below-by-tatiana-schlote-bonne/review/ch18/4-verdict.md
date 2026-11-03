# ch18 判定表（R4 逐块 + 断言）

> 覆盖声明：本章 **全章人判**（R1→R4 完整），10/10 块逐块核对「引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写」并逐块问施事三问（谁做的／谁的／谁说的）；引语逐字由 R2（2-machine.json）与 verbatim 全量复核（全书 204/208，另 4 条已证为 epub `<img alt>` 插页转写，非伪造）。

| 块 | 引语 ↔ 分析对应 | 施事三问（谁做/谁受/谁说） | 跨章引用/数字 | 档位 |
|---|---|---|---|---|
| 1 | ✓「真正的朋友不会让你做你不想做的事」→ 遗言的定义 | 说＝手写留言；受＝Petra；做＝（读） | 无跨章引用 | 通过 |
| 2 | ✓ 历史书那句 → 掠夺的既成史 | 说＝旁白（引历史书）；受＝Petra；做＝翻找房屋 | 「The history books are right…」✓（:7） | 通过 |
| 3 | ✓「at least fifteen thousand nox」+ 对分的争执 → 钱与亏欠 | 说＝Flint；受＝Petra；做＝两人对分 | 与 ch19 的 20,000 nox 一脉相承 ✓ | 通过 |
| 4 | ✓ 绞杀根挡不住感染 → 药到力竭 | 说＝旁白；受＝Flint；做＝（判断） | 与 ch14 的 sanaroot 同线 ✓ | 通过 |
| 5 | ✓ 脑震荡与眩晕 → 她也在坏下去 | 说＝旁白；受＝自己；做＝（自评） | 无跨章引用 | 通过 |
| 6 | ✓「I think this might be—」→ 认出前的迟疑 | 说＝Petra；受＝自己；做＝（掀甲片） | 与 ch11 的 fiend 同一疑问 ✓ | 通过 |
| 7 | ✓「It's him」+「Mom and I had a funeral for Dad」→ 迟到的葬礼 | 说＝Petra；受＝Flint（靠肩）；做＝Petra 确认 | 与 ch11 的表同线 ✓ | 通过 |
| 8 | ✓「I've already had a funeral for him before」→ 拒绝与和解 | 说＝Petra；受＝自己；做＝摘表 | 表背刻字未译（见错 1） | 通过 |
| 9 | ✓「I'll get you back to the top」→ 誓词的第三次兑现 | 说＝Petra；受＝Flint；做＝（抚他的头发） | 与 ch01:27／ch02:254 同一句 ✓（跨章引用正确） | 通过 |
| 10 | ✓ 掌心发红、痒到骨头 → 感染也在她体内 | 说＝旁白；受＝自己；做＝（擦汗） | 与 ch19 藤蔓出指尖同线 ✓ | 通过 |

**关键词锚定**：10 块关键词均取自本块引语（gate ⑱ 阻断 0；check_vocab 全书 FAIL 0 / WARN 0）。

## 已核实为正确（防误修；后续不得以「读着不对」改动）
- 手写留言：`text/ch18_chapter_eighteen.txt:5`「I don’t regret going to the Sixth. I only regret the circumstances that… true friends don't let you do things you don't want to do.」
- 表背刻字：同章 :105-106「With you every second, / Love, Sapphire and Petra」；`/usr/bin/grep -rn "Sapphire" text/` → 仅此一处。
- 父亲的表与老鹰纹身：R1 事实6/7 锚点 [5855:5899]、[7241:7288]。
- 誓词第三次出现：同章 :148「I'll get you back to the top」——与 `text/ch01_chapter_one.txt:27`、`text/ch02_chapter_two.txt:254` 同句。
