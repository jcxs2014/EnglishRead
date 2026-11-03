# ch13 判定表（R4 逐块 + 断言）

> 覆盖声明：本章 **全章人判**（R1→R4 完整），10/10 块逐块核对「引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写」并逐块问施事三问（谁做的／谁的／谁说的）；引语逐字由 R2（2-machine.json）与 verbatim 全量复核（全书 204/208，另 4 条已证为 epub `<img alt>` 插页转写，非伪造）。

| 块 | 引语 ↔ 分析对应 | 施事三问（谁做/谁受/谁说） | 跨章引用/数字 | 档位 |
|---|---|---|---|---|
| 1 | ✓ 淤泥中摸索却分不清左右上下 → 失重与失序 | 说＝旁白；受＝Petra；做＝（摸索） | 无跨章引用 | 通过 |
| 2 | ✓「possibly Jade, possibly a monster」→ 概率式决策 | 说＝Petra（内心）；受＝自己；做＝选择跟走 | 无跨章引用 | 通过 |
| 3 | ✓「They're gone」耳塞＋对方没戴面罩 → 两个物证揭穿幻象 | 说＝旁白；受＝Petra；做＝（摸耳塞） | 与 ch12 立下的耳塞规矩呼应 ✓（跨章引用正确） | 通过 |
| 4 | ✓ mindripper「feeding off my worst feelings about myself」→ 怪物的食物是自我厌恶 | 说＝Petra（内心）；受＝自己；做＝（识破） | 无跨章引用 | 通过 |
| 5 | ✓「Wrong choice」＋上百次微型刺 → 犯错与批注同时发生 | 说＝Petra；受＝自己；做＝撕扯 | 无跨章引用 | 通过 |
| 6 | ✓ 两名潜水员被刺死 → 道德决定写成护理判断 | 做＝Jade 刺死；受＝两名潜水员；说＝Petra 后悔 | 无跨章引用 | 通过 |
| 7 | ✓ 定位器哔声 → 呼救信号同时是开饭铃 | 说＝Petra（内心）；受＝自己；做＝循声 | Mr. Stone 卖定位器 ✓ | 通过 |
| 8 | ✓ 出水前就抱住他 → 身体比理智先原谅 | 做＝Petra 抱；受＝Flint；说＝旁白 | 与 ch13 块 9 的怀疑同章并列 ✓ | 通过 |
| 9 | ✓ Jade「'Flint' here might be its meat puppet」→ 归来者要验货 | 说＝Jade；受＝Flint；做＝Jade 质疑 | 与 ch16 的不信任同线 ✓ | 通过 |
| 10 | ✓「Seeing Coltan again really threw me」→ 失败归因于欲望 | 说＝Flint；受＝自己；做＝Flint 自陈 | Coltan 只提名字，未指长幼 ✓（本块中文写「想再和弟弟说一次话」见错 4） | 通过 |

**关键词锚定**：10 块关键词均取自本块引语（gate ⑱ 阻断 0；check_vocab 全书 FAIL 0 / WARN 0）。

## 已核实为正确（防误修；后续不得以「读着不对」改动）
- 验明方式：`:117`「Jade pinches my arm, twisting the skin.」；`:129` Jade 下刀割下 mindripper；`:157` 两人各抓一端撕成两半。
- 口令查无于本章：`/usr/bin/grep -rn -i "codswallop" text/` → 仅 `text/ch04_chapter_four.txt:217/219` 与 `text/ch10_chapter_ten.txt:13`。
- 插页人物：`text/ch13_chapter_thirteen.txt:3` 为 Breccia（第六层潜水员）谈命名法 ⇒ md `:14`「插页是 Breccia 谈命名法」成立。
- 找到 Flint：`:201` 定位器哔声；`:207`「Before my head breaks the surface, I throw my arms around him.」；`:215` Jade 的 meat puppet；`:221`「All I wanted was the chance to talk to him one more time」。
