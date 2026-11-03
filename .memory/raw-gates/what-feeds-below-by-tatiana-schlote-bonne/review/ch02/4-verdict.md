# ch02 判定表（R4 逐块 + 断言）

> 覆盖声明：本章 **全章人判**（R1→R4 完整），10/10 块逐块核对「引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写」并逐块问施事三问（谁做的／谁的／谁说的）；引语逐字由 R2（2-machine.json）与 verbatim 全量复核（全书 204/208，另 4 条已证为 epub `<img alt>` 插页转写，非伪造）。

| 块 | 引语 ↔ 分析对应 | 施事三问（谁做/谁受/谁说） | 跨章引用/数字 | 档位 |
|---|---|---|---|---|
| 1 | ✓ 插页：紫羽大鸟「Beak taped shut.」→ 无人格化的美与被封住的口 | 做＝（插页转写，出版方拟人化的鸟）；说＝插页文字 | 无跨章引用 | 通过 |
| 2 | ✓ 游客惊叹「I love this moment」→ 地表观光客的单纯与井下对照 | 说＝Henry；受＝Petra/Jade；做＝亨利惊叹 | five-hundred-foot cliff 在块 10 ✓ | 通过 |
| 3 | ✓ Mica 六个月死于 parrot flu → 失去弟弟的来由 | 说＝Petra；受＝Mica；做＝（疫情） | 六个月＝原文「just six months old」✓ | 通过 |
| 4 | ✓ Void Core 与 Obscuris 千年文献 → 世界观的第二块砖 | 说＝Petra（回答 Henry）；受＝Henry；做＝（叙述） | Core／Obscuris 命名与后文一致 | 通过 |
| 5 | ✓「bring back the whole world」→ 孤儿院孩子的处境 | 说＝Petra；受＝孤儿院孩子；做＝（回忆） | sweet kids ✓ | 通过 |
| 6 | ✓ 母亲「I have a daughter」→ 被抵出去的恐惧 | 说＝母亲；受＝Petra；做＝母亲示好路人 | eleven years old ✓（text:82/94） | 通过 |
| 7 | ✓ Jade 讲童奴船队与十年合同 → 孤儿院同款遭遇 | 说＝Jade；受＝Jade 自己；做＝Jade 讲 | “a ten-year contract” ✓（text:98） | 通过 |
| 8 | ✓「I don’t ‘garden.’ I create.」→ 她的身份不是照料而是生产 | 说＝Jade；受＝Petra；做＝Jade 解释 | 引号内嵌 garden 为原文 ✓ | 通过 |
| 9 | ✓ 鱼被 trap vine 活活吃掉 → 地表生态的温柔版暴力 | 做＝trap vine；受＝鳗鱼；说＝旁白 | 无跨章引用 | 通过 |
| 10 | ✓ 五百尺崖下 Jade 的誓词 → 第二次把「带你回到顶上」说出口 | 说＝Jade；受＝Petra；做＝Jade 承诺 | 呼应 ch01 :27 的同一句 ✓（跨章引用章号正确） | 通过 |

**关键词锚定**：10 块关键词均取自本块引语（gate ⑱ 阻断 0；check_vocab 全书 FAIL 0 / WARN 0）。

## 已核实为正确（防误修；后续不得以「读着不对」改动）
- 紫色大鸟插页：`text/ch02_chapter_two.txt:6`「She was a beautiful bird. Massive, as big as a grown man… Beak taped shut.」——md 引语逐字。
- parrot flu 在 Main Street 爆裂：`text/ch02_chapter_two.txt:29` 附近；Mica 六个月：`:16`「Mica succumbed to the illness when he was just six months old.」
- 母亲雨夜卖女：`text/ch02_chapter_two.txt:94`「I have a daughter」；Petra 当时十一岁见 `:82`「I was eleven years old」。
- Jade 巷中救 Petra 与童奴船队：`text/ch02_chapter_two.txt:98`「some sketchy crew that was going to send her into tight Void caves only kids could fit into… a ten-year contract with all the pay going to her dad」。
- 父亲下第五层只带回背包、母亲给 compass：同章 `:82` 段。
