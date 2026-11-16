# R5 判定表 · ch01

| 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|
| 逐字 | chapter.sh --json verdict=ok；verbatim --full 221/221 | 6 块逐字 | 通过 |
| 对应 | R4 逐块 6/6：中文均讲本块引语；施事三问核对（possum 说话人=Dad；代发咨询=Eden 答应后 Gemma 抢手机） | 对应成立 | 通过 |
| 形态 | H1 ✅ 01. Chapter One；导航 5 项；4 子项；6 块（本书众数 8，区间内） | 正常 | 通过 |
| 断言① | `And if` 计数：引语块内 2 次，md 两处写「三连」 | 计数错 | 阻断 |
| 断言② | 结尾回农场预言：ch26 尾声在墨尔本 | 预言被推翻 | 提示 |
| 断言③ | 「妈妈那边多半也有类似称呼」：妈妈称 sweetie | 无据推测 | 提示 |
| 词汇 | 14 条例句逐条 `grep -F` 命中本章；分档无注水 | 通过 | — |

## R4 施事三问记录（6 块）
- 1：「告别是 Eden 的最难」= 原文 I 叙述，主语 Eden ✔；「两年学习两年离开」= 她自己的账 ✔
- 2：受害链主语=I（Eden），post-grad→PhD 方向与原文一致 ✔
- 3：adjoining rooms 是「我」与 Gemma 的双向 ✔；daunting 的主语是「从乡下独自进城的人」泛指 ✔
- 4：possum = Dad 说（引号内）✔；smell the farm 的主语=I ✔
- 5：凝视主体=Eden，被看者=照片中的 Oliver ✔；"Could be just what I need" 的主语=I ✔
- 6：groan/feigning = Eden；squeals/snatches/sends = Gemma ✔（方向未反）

## 已核实为正确
1. `text/ch01_chap1.txt:107` 的 `And if` 段全段共 3 次——md 若把「块内」写成三连才算错；本表已按块内 2 次判。
2. 「possum 是澳式爱称」属语言注释，非情节断言，保留。
3. 「Gemma 下一幕翻出家教名单」：同一章 ramen 段内确有 `Cory Donovan, Heath Carson, Jamil Sutherland`（`text:197`），成立。
4. 词表 `veranda` 例句来自本章 `The whole family has assembled on the front veranda.`（`text:77`），成立。
