# ch02 · T3 判定表

- 章：Chapter One（md：`ch02 chapter one a new person.md`；原文 `text/ch02_chapter_one.txt`，35,295 字符 / 6,356 词）
- R1 素读：`1-suread.json`（**独立子代理**，只读 `text/`；8 条，锚点 8/8 唯一且偏移自检通过）
- R2 机器层：`2-machine.json`（verdict=ok，13 块 / 15 片段，查无 0）
- R3 对账：`3-diff.md`（漏 3 提示 / 编 2 阻断（F1、F2）/ 错 0）
- 覆盖：**全章 13 块逐块 R4 + R5**

## R4 逐块对应

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 47 | crowded · forest-green · alone | ✓ | ✓ 讲「先写别人热闹、最后交代孤独」 | ✓ 她看别人 | 通过 |
| 2 | 44 | hardened · syllables · monster | ✓ | ✓ 讲发音即刑罚、une bête 的升级 | ✓ 法国人叫错**她**的名字 | 通过 |
| 3 | 43 | spaceship · astronaut · elevator | ✓ | ✓ 讲「把窘迫译成探险」 | ✓ 她住、她下行八层 | 通过 |
| 4 | 28 | wonder · heartbreak · clown | ✓ | ✓ 讲机翻信条的粗糙与「同时」 | ✓ 学校承诺教**她**（主语没错位） | 通过 |
| 5 | 57 | postcard · strip malls · honeymoon | ✓ | ✓ 讲「拆明信片」与王尔德把地理接成婚姻 | ✓ 她用本地人眼睛看 | 通过 |
| 6 | 45 | Ophelia · melody · dead and gone | ✓ | ✓ 讲戏词追上了她 | ✓ **她**演 Ophelia、老师让**她**写旋律 | 通过 |
| 7 | 45 | felled · hockey player · in his sleep | ✓ | ✓ 讲三下拆死亡、缺席的位置 | ✓ **父亲**被击倒（她被排除在外：she hadn't been home） | 通过 |
| 8 | 37 | unknowable · unreadable · extravagantly | ✓ | ✓ 讲「读不出」把悲痛写成表演 | ✓ **Elisabeth 看母亲**（不是母亲看女儿） | 通过 |
| 9 | 52 | Rothko · transformation · her paintings | ✓ | ✓ 讲「简化成一张画」与产权 | ✓ 她跑、她看、她认领画 | 通过 |
| 10 | 33 | empty-nester · useless · not needed | ✓ | ✓ 讲把私痛升级成词典定义 | ✓ 她宣布定义 | 通过 |
| 11 | 40 | twelve words · xo · doesn't love her | ✓ | ✓ 讲「用一个落款完成鉴定」 | ✓ **她**数**女儿的**词、她得出恐惧 | 通过 |
| 12 | 48 | perfect heart · sunset · punishable | ✓ | ✓ 讲事实兼武器、审美式残忍 | ✓ **Catherine** 说、她看对方的脸 | 通过 |
| 13 | 38 | pulls her forward · calm · no idea | ✓ | ✓ 讲把命运交给风景说 | ✓ 水「不知道」，她被念头拉着走 | 通过 |

形态（R2）：H1 `# 02. Chapter One` ✓｜导航 5 项 ✓｜子项齐全 ✓｜块数 13（建议 12–15，硬限内）｜中文密度全部达标。

## R5 判定表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| F1 | 「二十年来的第一个双程」 | `text/ch02_chapter_one.txt:442` `She’s closing her second loop…`；261 行 `First time in twenty years` 指独居 | 数字与事实归属双错 | **阻断** → 改「今天的第二个环」 |
| F2 | 「七英里之外的水边」 | ch02 全文无 mile/km 距离（grep 0 命中） | 凭空数字 | **阻断** → 改「湖湾尽头的那片水边」 |
| L1–L3 | 见 `3-diff.md` | — | 未收细节，非转折 | 提示（不修） |

## 四组报数

- 逐字：13 块 / 15 片段全可核实（R2 查无 0）；词汇例句抽 4 条全命中
- 对应：R4 13/13 通过（施事/受事 0 反转；第 8 块主语方向正确是「女儿看母亲」）
- 形态：H1 ✓ 导航 5 项 ✓ 子项齐全 ✓ 块数 13 在建议区间内
- 断言：2 条阻断（已修）+ 3 条提示

## 已核实为正确（防误修）

| 写法 | 原文 | 说明 |
|---|---|---|
| 「到巴黎五周」「八月一日抵达」 | `text/ch02_chapter_one.txt:7` `Elisabeth arrived five weeks ago, on the first of August.` | 成立，勿再改成「三个月」 |
| 「父亲死了三个月」 | `text/ch02_chapter_one.txt:184` 附近 `dead for three months` | 成立；与「离家五周」不矛盾 |
| 「十二个词、xo 而不是 love」 | `text/ch02_chapter_one.txt:303` 附近 | 成立 |
| 「王尔德一八八二年二月」 | 原句 5（`February of 1882`） | 成立 |
| 「十一平方米」「两百欧房租」「八层无电梯」 | 19 行附近 `It is a spaceship…No elevator`；16 行 `only two hundred euro` | 成立 |
| 「母亲清晨跑着看水天色块」 | 255 行 `Catherine runs early in the mornings` | 成立，但**不是**「二十年来的第一次跑步」 |
