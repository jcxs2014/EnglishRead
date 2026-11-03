# ch03 判定表（R4 逐块 + 断言）

> 覆盖声明：本章 **全章人判**（R1→R4 完整），10/10 块逐块核对「引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写」并逐块问施事三问（谁做的／谁的／谁说的）；引语逐字由 R2（2-machine.json）与 verbatim 全量复核（全书 204/208，另 4 条已证为 epub `<img alt>` 插页转写，非伪造）。

| 块 | 引语 ↔ 分析对应 | 施事三问（谁做/谁受/谁说） | 跨章引用/数字 | 档位 |
|---|---|---|---|---|
| 1 | ✓ Spine Woods 得名于第一批采矿队 → 地名的来历 | 说＝旁白；做＝第一批采矿队；受＝读者 | Fissure Lake／Spine Woods 命名一致 | 通过 |
| 2 | ✓「five hundred consecutive hours」与「ten surface hours to detox」换算 → detox 经济学 | 说＝Petra 回答；受＝Henry；做＝Petra 换算 | 全书唯一含省略号的引语，同段内省略 ✓（text:113） | 通过 |
| 3 | ✓ 星鼻鼬「the size of a jaguar」→ 体量对比 | 说＝旁白；受＝众人；做＝（出现） | Beast-Away Repellent Spray 属选材取舍 | 通过 |
| 4 | ✓ 巨钳与黑蜘蛛腿从活板门窜出 → 陷阱的第一次亮相 | 做＝巨钳（做陷阱的生物）；受＝Henry；说＝旁白 | 无跨章引用 | 通过 |
| 5 | ✓ tassala 花与《Field Guide of Void Botany》→ 她的植物学 | 说＝旁白；做＝Petra 采花；受＝Herbalist（同行） | Compendium/Field Guide 命名一致 | 通过 |
| 6 | ✓ 挖出宝石、「not pink, but it’s valuable」→ 收益与欲望的错位 | 做＝Petra 挖；受＝（宝石）；说＝Petra | at least fifty nox ✓ | 通过 |
| 7 | ✓ Henry 要「a bigger one for my wife, and pink」＋“Consider it a tip” → 贪心与人情 | 说＝Henry；受＝Jade/Petra；做＝Henry 再挖一铲 | 「Consider it a tip」✓（text:245 附近） | 通过 |
| 8 | ✓ shadow fox 肋骨外露、绿真菌 → 死的怪物与活的威胁 | 做＝（描述）；受＝（观察）；说＝旁白 | 无跨章引用 | 通过 |
| 9 | ✓ 假 Jade 声音「not the one talking」→ 幻象的破绽 | 说＝假 Jade 的声音；受＝Petra；做＝幻象模仿 | 呼应 ch13 的 mindripper ✓（跨章章号未写死，表述安全） | 通过 |
| 10 | ✓ 四只瘦手抓脚踝、背包带被扯断 → 第一条命线断 | 做＝假 Jade/四手；受＝Henry；说＝旁白 | 无跨章引用 | 通过 |

**关键词锚定**：10 块关键词均取自本块引语（gate ⑱ 阻断 0；check_vocab 全书 FAIL 0 / WARN 0）。

## 已核实为正确（防误修；后续不得以「读着不对」改动）
- 层级与地名：`text/ch03_chapter_three.txt:21`「Spine Woods got its name from the first mining team…」；第二层入口见 `:5`「The moment my feet touch the ground of the Second Layer」。
- 星鼻鼬：`text/ch03_chapter_three.txt:41`「It stretches its neck… the size of a jaguar」。
- 宝石顺序：挖出宝石在 `:239`，Henry 再挖在 `:245`「I want a bigger one for my wife, and pink」；四手拖走在 `:307`。
- 省略号引语：`text/ch03_chapter_three.txt:113` 内两处原文同段；`/usr/bin/grep -n "five hundred consecutive hours" text/ch03_chapter_three.txt` 与 `grep -n "ten surface hours to detox"` 均命中第 113 行 ⇒ 属同段省略号图式，非拼接。
