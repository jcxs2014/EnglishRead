# fabulous-bodies-by-chuck-tingle · 复核判定表（2026-10-21）

抽样章型：ch01 首章 / ch10 对话密集+反派演讲 / ch11 重述章 / ch16 末章。
机器层：全书 16 章 + 总览三篇全量（见 `2-machine.log`）。

## 机器层
| lane | 结果 |
|---|---|
| gate.sh 20 lane | **EXIT=0，阻断型 0** |
| 引文逐字 | 全绿 |
| `overview.py quotes` | 41/41（100%），金句 22/22 |
| `overview.py full` | 整串 27 命中 / 拼接 0 / 查无 0 / 16 章全覆盖 |
| 中文层 | 169 块 / 密度 100% / 夹杂 0 / 阻断 0 |
| 词汇 | 249 条例句逐字校验通过 |

## 人判层（R1 素读 → R3 对账 → R4 逐块）

| # | 位置 | 断言/问题 | 原文依据 | 档位 |
|---|---|---|---|---|
| F1 | `ch10 Date Night.md:63` | 「解释了他为什么能活**四百年**还乐在其中」 | `text/ch10_10_date_night.txt:151` "Best I've had in … **four hundred years** maybe?" —— 说的是**这一夜的乐趣**，不是年龄；年龄见 `text/ch11:52`（guest 约一千七百年前到来） | 阻断 |
| F2 | `ch10 Date Night.md:81` | 「dad 这个身份与**「活了四百年」**之间的矛盾」 | 同上：把体验年限当成寿命；真正的矛盾是「他活了千年以上 vs Poppy 二十几岁」 | 阻断 |
| F3 | `ch11 Get Ready with Me.md:42` | 「她还有**十二个**兄弟姐妹，其中一个…已经死了」 | `text/ch11:76` "You have **twelve** siblings… It **used to be thirteen** siblings, but one of them died" ⇒ 12 个**活着**、原有 13；md 读成「12 个里死了 1 个」（=11 活着），且与同文件 `:9`「十三个兄弟姐妹，其中一个已死」自相矛盾 | 阻断 |
| F4 | `ch11:124`（一句话总结） | 「一只活了**千年**的寄生生物」 | 同文件 `:9` 已写「一千七百年」；`text/ch11:52` 为 seventeen hundred years | 提示 |
| F5 | `ch05 Follow for Follow.md`（全章） | **漏**「假驾照 Alice Roosevelt」：`text/ch05:145` Eddie 从钱包抽出驾照念出该名，Poppy 只当他随口一念；`text/ch10:154` 靠这一处成立（"he never mentioned it again" ⇒ 他早知道她是谁）——ch05 只在词汇表收了 driver's license，精读与总结均未提 | 见左 | 提示（漏，低优先） |

## 结论
- 阻断型 **3**（F1–F3，全部是「事实断言 / 数字关系」，机器层结构上查不到）。
- 提示型 **2**（F4 数字口径不一、F5 伏笔漏挖）。
- 与 2026-10-20 那轮已修的 6 项（块序、frontmatter、五→四词、十四个孩子、跨章 chNN 标注、金句编号外移）**无回归**：本次复核未再发现同类问题。
