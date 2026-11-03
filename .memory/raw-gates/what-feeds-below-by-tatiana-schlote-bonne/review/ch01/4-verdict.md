# ch01 判定表（R4 逐块 + 断言）

> 覆盖声明：本章 **全章人判**（R1→R4 完整），10/10 块逐块核对「引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写」并逐块问施事三问（谁做的／谁的／谁说的）；引语逐字由 R2（2-machine.json）与 verbatim 全量复核（全书 204/208，另 4 条已证为 epub `<img alt>` 插页转写，非伪造）。

| 块 | 引语 ↔ 分析对应 | 施事三问（谁做/谁受/谁说） | 跨章引用/数字 | 档位 |
|---|---|---|---|---|
| 1 | ✓ 尸体嘴唇被撕、牙齿外露 → 中文写「哪只怪物干的」；四子项全围绕尸体与追查 | 死者＝Gunther；做＝某只 Void 怪物；说＝旁白（Petra 视角） | five hundred consecutive hours 之类不在本章；无跨章引用 | 通过 |
| 2 | ✓「I'll always get you back to the top」+ since our first Void dive together five years ago → 誓词与五年 | 说＝Petra（对 Jade）；受＝Jade；做＝立誓 | 「五年前」＝本章原文五年前首次下潜 ✓ | 通过 |
| 3 | ✓ Gunther 吹牛 thirty-thousand-foot mountain → 壮胆话与「游客」身份 | 说＝Gunther（回忆中）；受＝Petra/Jade；做＝吹牛 | thirty-thousand-foot ✓ 原文 | 通过 |
| 4 | ✓ Jade 说「Thank you for offering your life to the Void」并顺手在尸体下方摸走东西 → 偷表 | 做＝Jade；受＝死者（物件归 Jade）；说＝Jade | 银表＝R1 事实2（text:4320 附近）✓ | 通过 |
| 5 | ✓ 诊所＋温室＋药草清单（turmeric/ginseng/milk thistle）→ 她的目标 | 说＝Petra（内心）；受＝未来病人；做＝开诊所计划 | 五千 nox（text:17998）✓；孤儿院挂靠 ✓ | 通过 |
| 6 | ✓ 提到弟弟 Mica 与 Void parrot flu → 失去弟弟的动机 | 说＝Petra；受＝Mica（已故）；做＝（回忆） | Mica 六个月死于疫情＝ch02 原文 :16 ✓ | 通过 |
| 7 | ✓ 风险与回报的对仗句 → 潜水的赌注 | 说＝旁白（Petra 权衡）；做＝下潜 | 数字与本章无冲突 | 通过 |
| 8 | ✓ 手写便条：Henry 出 150 nox 请人带路取 pink glowjem → 委托来源 | 说＝便条文字；付＝Henry；做＝Jade 撕下便条 | 150 nox／Henry Pembroke Winchester IV／第三层 ✓（R1 事实4） | 通过 |
| 9 | ✓「Around six months ago, he showed up to work with this prosthetic」→ 义肢与疏远 | 说＝Petra 转述 Flint；做＝Flint 换义肢；受＝Flint | since we were eleven ✓ 原文（text:263） | 通过 |
| 10 | ✓ 吊笼被风吹晃、Henry 尖叫 → 第一次带人下潜 | 做＝Henry/Jade/Petra；说＝旁白 | no 跨章引用 | 通过 |

**关键词锚定**：10 块关键词均取自本块引语（gate ⑱ 阻断 0；check_vocab 全书 FAIL 0 / WARN 0）。

## 已核实为正确（防误修；后续不得以「读着不对」改动）
- 死者是独自下到第二层一半的游客：`text/ch01_chapter_one.txt:13`「We lost his pulse a minute ago. Looks like the poor bastard went in by himself. Barely made it halfway through the Second Layer.」
- 山的高度：`text/ch01_chapter_one.txt:35`「thirty-thousand-foot mountain」——md「三万英尺」逐字对应。
- Jade 偷表：`text/ch01_chapter_one.txt:59` 附近「Her hand swipes low by the body」；R1 事实2 锚点 [4320:4377]。
- 誓词与五年前：`text/ch01_chapter_one.txt:27`「I’ll always get you back to the top.」＋同段「since our first Void dive together five years ago」。
- 诊所与五千 nox：`text/ch01_chapter_one.txt:17998` 段「we’ll need five thousand nox to get the permits and supplies」；Ms. Opal 十八岁条件见同章 :10450 段。
- 义肢与疏远：`text/ch01_chapter_one.txt:249/253/263`「Around six months ago, he showed up to work with this prosthetic and a newfound sadness.」＋「we haven’t been friends since we were eleven」。
