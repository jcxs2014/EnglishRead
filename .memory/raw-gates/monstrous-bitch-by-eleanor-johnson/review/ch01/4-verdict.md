# ch01 判定表（R5）

章：`ch01 preface.md`（216 行，9 块）
原文：`text/ch01_preface.txt`（49 行 / 2,245 词 / 10,804 字符去空白）
机器：`2-machine.json` rc=0；块数 9；引语 9 段全 ok；空引号 0；子项齐全；中文密度合格；本书前 3 章内块数按配额 [5,10] 判，9 在区间内。
素读：`1-suread.json` 6 条，`quote in content && count==1` 脚本校验 6/6。

## 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| md:15「约 10,804 字符（去空白）」 | `python3 -c` 去空白计数 = 10804 | 准确 | 通过 |
| md:18/结构列表 9「她自陈惯常写十至五十年的题材」 | `text/ch01_preface.txt:40`「I tend to write books about periods of time ranging between about ten and fifty years」 | 「十至五十年」成立（原文为 between about ten and fifty years，非 ten to fifty） | 通过 |
| md:26「那样的女性多半也不会特别不满」 | `:25`「And that would have been all I expected from my reality, so I probably wouldn't have been especially unhappy with my lot.」 | 成立（是「大概不会特别不满」，非「满意」） | 通过 |
| md:51 可质疑处 1「『七百年』只给了约数、没有出处」 | `:31`「That deterioration bucks a trend that's about seven hundred years old, in which things have slowly been getting better for women.」该句后无脚注标号（全章脚注标号只有 `.1 .2 .3 .4` 四处，均不在本句） | 成立：确为约数、本句无注 | 通过 |
| md:18「父权由家庭、教会、政府、大学、法律制度、医学、军队与交易市场共同支撑」 | `:29`「(the family, the church, the government, the universities, the legal system, medicine, the military, the trade marketplace)」 | **八项，逐项对上，顺序一致** | 通过 |
| md:28 结构列表 8「生育自由、求偿权与投票权都在流失」 | `:31`「women have been losing their reproductive freedoms」＋「losing their ability to seek redress for crimes committed against them」＋`:33`「seeing their voting rights erode before their eyes」 | 三项对上 | 通过 |
| md:32 结构列表 11「Monstrous Bitch 是父权的涌现属性，因此她也要大写」 | `:45`「not a real entity but rather an emergent property of Patriarchy, and she evolves in lockstep with that Patriarchy. So I'm going to go ahead and capitalize her, too」 | 成立 | 通过 |
| md:33 结构列表 12「近几十年作品把她改写成反抗的图标」 | `:49`「the works of art … do so precisely in order to confer extra power, legitimacy, and resilience on her」＋「the Monstrous Bitch has begun to appear less as a monster and more as an icon of feminist resistance and survival」 | 成立（「1970 年代起」亦在 `:47`「especially since the 1970s」） | 通过 |
| md:18 概览「中世纪女性…可能死于分娩、避孕只能靠接生婆与草药、家庭之外不会有职业」 | `:25`「I would very possibly have died in childbirth」；`:23`「aided by midwives and herbs」；`:25`「I would probably not have had a career outside the home」 | 三处逐条对上 | 通过 |
| md:27 结构列表 6「男孩们被更认真地对待、得到更多自由、被鼓励读书识字、并被交付财产继承与手艺技艺的钥匙」 | `:23`「the little boys around me were somehow taken more seriously. Given more freedom. Encouraged in some cases to study and learn to read. Given the keys to the kingdom, in terms of property inheritance, learning trades and crafts」 | 四项对上 | 通过 |
| md:18「近年的『回归』让感恩变成恐惧」 | `:29`「It's the feeling of that gratitude morphing into fear.」＋「an era of regression」 | 成立 | 通过 |
| md:34 方法论「长时段分析加个案作品研究」 | `:47`「As we perform this longue durée analysis … also at moments in which specific cultural objects—poems, epics, plays, narratives, theological treatises, novels, and eventually films—affected the cultural ecosystem」 | 成立（七类文本逐项对上） | 通过 |
| R4 块 1–9：中文理解 ↔ 引语 ↔ 关键词 ↔ 为什么这样写 | 逐块核：9 块中文理解均是该块引语的直译或紧邻概括，无引语外扩写；关键词逐条在本块引语内（机器层亦 0 缺）；「为什么这样写」均以引语内可指认的措辞（almost none／see around its edges／bucks／whole-cloth／emergent property／recoded）立论 | 9/9 对应 | 通过 |
| 施事三问（9 块） | 块 1 说话人＝作者本人（I was born…）；块 2 反事实主语＝作为女性的作者；块 3 受事＝中世纪女性，施事＝父权与八类制度（`supported by`）；块 4 施事＝deterioration（bucks）；块 5 施事＝Patriarchy（has been terrified by）；块 6 施事＝Patriarchy，受事＝四项女性特质；块 7 施事＝Patriarchy／现代西方文化（inherited）；块 8 本体论断言（is not…but rather）；块 9 受事＝Monstrous Bitch（gets recoded，被动） | 9/9 方向正确，无施受反转 | 通过 |
| 漏：Caro／Klein 类比段未落 | `:40` 整段；`/usr/bin/grep -n "Caro\|Klein" ch01*.md` → 无命中（退出码 1） | 可选细节未落 | 提示（漏，降档） |
| 编 | 全章具名断言逐条回原文，均能在 `text/ch01_preface.txt` 找到对应句 | 0 条 | — |
| 错 | 数字、专名、施受方向逐条比对一致 | 0 条 | — |

计数（只数阻断档）：漏 0 · 编 0 · 错 0；提示 1。

## 已核实为正确

以下看着可疑、回原文核对后**成立**，下一轮不要误修：

1. 「十至五十年」不是笔误：原文 `:40` 就是「between about ten and fifty years」，别改成「十年到五十年」以外的数字。
2. 「七百年」是原文的约数（`about seven hundred years old`），不是从「四千年」推算出来的。
3. 「多半也不会特别不满」是原文的双重弱化（`probably wouldn't have been especially unhappy`），不要改成「很满足」或「毫无怨言」。
4. 八类制度是**八**项（family, church, government, universities, legal system, medicine, military, trade marketplace），不要合并成「七项」或漏掉 trade marketplace。
5. 四项恐惧是**四**项（aggression, sexuality, reproductive power, voices），顺序照原文。
6. 「Monstrous Bitch 是涌现属性」与「她也要大写」是同一句里的两件事（`:45`），不是两处主张。
7. 「1970 年代起」的重编码是原文 `especially since the 1970s`，不是「1970 年代以后才开始」的强断言。
8. 字符数 10,804 为去空白计数，与本章 `text/` 实算一致。
