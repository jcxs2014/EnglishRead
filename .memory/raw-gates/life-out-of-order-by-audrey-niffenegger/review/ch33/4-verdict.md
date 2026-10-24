# ch33 The Parable of the Parrots — 判定表（R5）

- 原文 664 行 / 精读 152 行；机器层 `2-machine.json` rc=0（verdict=ok，10 块 10 段全逐字，零 issue）
- 报数四组：**逐字 10/10 通 · 对应 10/10 通 · 形态 通（H1 `33. The Parable of the Parrots`／导航 5 条／子项四件齐；块数 10 为本书上限，机器只提示不判红）· 断言 漏 5 提示 · 编 0 阻断、1 提示 · 错 0**

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 「我没有手指，所以我没有痛」这条轴未进 md | `text/ch33_the_parable_of_the_parrots.txt:257` “I have no fingers, so I have no hurt.”；`:261` “That’s what I am afraid of.”；`/usr/bin/grep -c 手指 "ch33 the parable of the parrots.md"` → **0**（exit=0） | 全章论证的支点缺位，但它只在结尾「Do parrots love」那里兑现（块 9 已收） | 提示 |
| Oliver 父母入狱这条背景未进 md | `:469` “Some people, like my parents, are there because they tried to do good, and powerful people didn’t like that.”；`/usr/bin/grep -c 监狱 …md` → **0**（exit=0） | 未收，属人物背景取舍 | 提示 |
| 康德绝对命令未进 md | `:585` “Do you know Immanuel Kant’s categorical imperative?”；`:589` “Isadora spends a few moments whirring. “Yes,” she replies.”；`/usr/bin/grep -c 康德 …md` → **0** | 块 8 只收「回来」，未收「be kind 的依据」 | 提示 |
| 「奇点」在 md 只被点名、未展开 | `:163` “She calls it the Singularity.”；`:172` “Beck doesn’t think so. She says I won’t like it.” | 一句话总结点到（`:152`），无块承载 | 提示 |
| 「I am a parrot.」未收 | `:598` “I am a parrot.”；`:602` “You are the most exquisite, advanced possible parrot, Isadora. But soon you’ll be a real girl” | 与结尾「鹦鹉会爱吗」同线，收一处更完整 | 提示 |
| 导航把「担心她飞走」的归属给了 Beck | `:576` “if she sets you free, promise me you will come back to her.”（提要求的是 Oliver）；`:660` “Did you do this, Isadora?”（Beck 只追查侵入） | 归属外推 | 提示 |
| 块 4：挨打的是子逸，不是 Oliver | `:290` “every time Zǐ Yì left the building the lady would find him and strike him”；同句 “I never suffered, because my parents never let me leave the building without them.” | md 明写「子逸每次独自出楼」＋读者视角「他自己从未挨打」 | 已核实 |
| 密码是假的，不是真门槛 | `:83` “What is the password?”；`:92` “There’s no password, silly Oliver.” | 导航「先索要密码，再笑场」顺序正确 | 已核实 |
| 是 Alba 把 Oliver 加进 users list | `:126` ““Who added me to the list?” … “Alba.”” | 总结正确 | 已核实 |
| 「Alba 二十七岁会嫁给我」是要向 Isadora 保密 | `:151` “But it’s a secret for now, Isadora. Don’t tell Alba, or anyone else.” | 受事是 Alba，不是 Isadora | 已核实 |
| 鹦鹉「应声却不飞回」方向未写反 | `:416` “the lady would stand under the tree and talk to Bǎobǎo and Cǎi Hóng and they would reply, but they never flew to her.” | 块 6 正确 | 已核实 |
| 章末 Isadora 没有回答「谁来过」 | `:652-656` ““Isadora,” I ask, “who was here?” / She shows me photographs of two parrots.” | 块 10 写「只给她看两张鹦鹉的照片」，未写成「她答了」 | 已核实 |
| 橘子是 Oliver 用来试探摄像圈、也是被砸烂的物证 | `:52` “I retrieve it and roll it gently into the enclosed area.”；`:308` “I put the orange on the table and really thump it. The orange breaks open.”；`:647` “The orange I left on my table has been smashed” | 块 10 读者视角把两天缝在同一个物件上，成立 | 已核实 |
| 词汇 14 条例句逐字 | `:325` persecuted／`:485` besmirched／`:74` frictionless／`:244` bloody-minded／`:483` sweltering／`:208` decrepit／`:70` subsides／`:87` hiccuping／`:65` whirring／`:34` alluring／`:425` affection／`:380` airplane／`:273` afternoon／`:142` brother-in-law | 全部逐字命中 | 已核实 |
| 机器层 rc=0 是真通过 | `bash scripts/chapter.sh "…/ch33 the parable of the parrots.md" --json`，退出码 0，counts 全零 | 成立 | 已核实 |

## 已核实为正确（防下一轮误修）

1. **人名音译不构成编造**：原文只给拼音 `Bǎobǎo`（`:227`）、`Cǎi Hóng`（`:227`）、`Zhao Zǐ Yì`（`:213`），md 用「宝宝」「彩虹」「子逸」——意译／音译，全书一致（`grep -c`：宝宝 4、彩虹 4、子逸 2），**不得判为「原文无此名」**。
2. **2098-06-13 与 2041-05-01 两个日期未写错**：`:610` “Friday, June 13, 2098. Don’t tell anyone except Alba. Don’t tell Alba until after May 1, 2041.”；md 总结作「二〇九八年六月十三日」「二〇四一年五月后」，方向（要等 2041 之后才转告）正确。
3. **「密码」那一段是玩笑**：`:92` “There’s no password, silly Oliver. I’m not afraid of you anyway.”——下一轮若见「索要密码」与「没有密码」并置，按笑场处理，不是前后矛盾。
4. **「They are lost」是 Isadora 说博物馆要收鹦鹉**（`:539` “For the Museum. They are lost.”），不是 Oliver 说自己的旧物丢了；md 块 5 读者视角的引用正确。
5. **Beck 的段落是「次日上午」**：`:641` “Monday, August 19, 2013 (Beck is 37)”，md 作「次日」正确；原文 `:660` 说日志空白覆盖「yesterday morning」近两小时，与 Oliver 的 `Sunday, August 18` 吻合，**不是两张不同的时间线**。
6. **md 没有添人物**：全章出场者只有 Oliver、Beck、Isadora、Alba、Clare（仅出现在笔记本计分栏 `:40`）、Zǐ Yì、四楼太太、Oliver 的父母（仅被提及 `:469`）；md 未引入原文没有的人名。
7. **Oliver 的年龄不作为可核项**：md 全程未写 Oliver／Beck／Alba 的岁数，故本书其他章与其自述（`:146` “Alba is eleven in her present”）之间的岁数张力不构成 md 缺陷。
