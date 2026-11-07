# ch01 The Card of the Visitor — R4/R5 判定

| 断言/块 | 证据（text/文件:区间或逐字） | 结论 | 档位 |
|---|---|---|---|
| 原句1 访客牌 | `text/ch01_1_the_card_of_the_visitor.txt` 含 “Finally, she flips the card…”（素读 chars 459-640） | 引语与中文理解对应；关键词在引语内；施事：老祖母翻牌/牌面呈现 | 通过 |
| 原句2 监护/天空战争 | 原文含 “My mother even arranged for Old Mother to accompany us as our legal guardian…” “a war started entirely by Hevalla.”（素读 chars 1298-1474 邻近语境） | 归因与否定句对应；无施事反转 | 通过 |
| 原句3 维克米外貌 | 原文 “He even looks reptilian…”（text/ch01） | 描写对应；主语为 Vikemy | 通过 |
| 原句4 情报/空域警告 | 原文 “We have received intelligence that military action is being planned in airspace near us…”（素读 chars 3193-3397） | 引语逐字；“won’t you?” 语气分析成立 | 通过 |
| 原句5 科斯默帮忙晾衣 | 原文 “He was still. He said, \”Let me help you.\” We pegged up the laundry together. He went home.” | 短句节奏与未竟情绪对应 | 通过 |
| 原句6 飞船升空成微点 | 原文 “the door closed, the ship rose, and he became a speck on the blue sea of the sky.”（素读 chars 8357-8538 邻近） | 动作序列与空间拉远对应；无跨章错指 | 通过 |
| 原句7 根除血脉/穹顶/议会口号 | 原文含 “The bloodline, and its magic will be eradicated. The dome will be broken…” 及 “The Assembly will prepare…”（素读 chars 13280-13731） | 说话人：维克米宣言 + 群众齐声回应，分析已区分 | 通过 |
| 原句8 Loathing | 原文 “Loathing.” 及胃部翻搅语境（text/ch01） | 情绪命名对应；无编造 | 通过 |
| 跨章引用/断言 | 导航与总结未做“第一次/唯一/上一章”等绝对或相对断言；无 chNN 错指 | 无风险 | 通过 |
| 词汇表 | 12 词条，例句均为原文语境；check_vocab/gate 无阻断 | 通过 | 通过 |

## 已核实为正确
- 原句4 中 Vikemy 的反问“won’t you?”在 md 中被解读为“把要求包装成礼服/礼貌下的布控要求”；回原文该句确为请求式反问，解读成立（`text/ch01_1_the_card_of_the_visitor.txt` chars 3193-3397 语境）。
- 原句7 把 Vikemy 宣言与群众“echo in unison”的口号分开归属，符合原文结构（素读 chars 13280-13731）。

## 分档汇总
- 逐字：机器层通过（chapter.sh/gate）
- 对应：8/8 块通过
- 形态：通过（2-machine.json）
- 断言：无阻断、无提示性事实错误
