# ch23 Red Galoshes — 三单对账（漏 / 编 / 错）

> 素读底稿：`1-suread.json`（9 条）；机器层：`2-machine.json`（rc=0，4 块，4 段引语全 ok，1097 词，查无 0 / 空引号 0 / 子项缺 0）。
> 素读先落盘，之后才打开 md（`notes/books/novels/life-out-of-order-by-audrey-niffenegger/ch23 red galoshes.md`）。

## 素读补充句（作业单要求）

本章的转折点进没进这几条？——**进了一半**。"未来自己回来"进来了；但真正把噩梦转成预言的**那三问三答**（"Was it real?" / "I'm pretty sure it's real. It's a long time from now." / "It wasn't safe. You were right to stay inside the house." / "Just the wind… Nothing but the dark and the wind."）**没有进任何一块**，只在词汇表里剩下一句 "Just the wind" 的例句（md:85）。这是本章最大的一处漏。

## 一、漏（素读有、md 无）

| # | 素读条目 | md 情况 | 档 |
|---|---|---|---|
| 1 | 噩梦是真的、且发生在很远的将来：`text/ch23_red_galoshes.txt:216` "“Yes,” she says. “I’m pretty sure it’s real. It’s a long time from now.”"；`:224` "“It wasn’t safe. You were right to stay inside the house.”"；`:232` "“Just the wind,” she says. “Nothing but the dark and the wind.”" | md 搜 `真的`=0、`很久以后`=0；4 块无一块覆盖 `text:206-232`。**而 md:15 自己写着「噩梦的意象在末尾被重新提起，前后扣住」——这个"末尾重提"在 md 的块里并不存在**，只有 md:85 词汇表借 "Just the wind" 做过例句 | **阻断** |
| 2 | 那本书是外公送的圣诞礼物——勋伯格《和声学》；「对八岁小孩不是好礼物，但你十五岁会爱上它」（`text/ch23_red_galoshes.txt:165、173`） | md 搜 `勋伯格`=0、`和声`=0、`十五岁`=0；这块是"未来自己认识童年的我"最具体的一件证物，且与 ch20 的琴课线呼应 | 提示 |
| 3 | 「有些人在黑暗里说话更容易……就像你在我脑子里说话，我在你脑子里」与「她就是我，但我还不是她」（`text/ch23_red_galoshes.txt:190、198、202`） | 未进块；md:15 只说"触觉被用来分辨人"，未收这层 | 提示 |
| 4 | 年龄坐标：抬头 "Alba is 8 and 46"（`text/ch23_red_galoshes.txt:18`），即回来的那个 Alba 四十六岁 | md 只写"八岁"与"2047"，未给 46；读者算不出她比这一刻的自己大三十八岁 | 提示 |
| 5 | 秘密的坏处说得更细：「Daddy might feel unhappy… He might feel . . . left out.」（`text/ch23_red_galoshes.txt:140`），以及「you might resent that」（`:106`） | md:90 只写"必须瞒着爸爸"，"被落下"与"怨恨"未收（`怨恨`=0、`resent`=0） | 提示 |

## 二、编（md 有、原文无）

| # | md 位置 | 原文 | 判 | 档 |
|---|---|---|---|---|
| 1 | md:13「反转『访客』：**推门进来**的不是鬼魂也不是陌生人，而是她自己」 | `text/ch23_red_galoshes.txt:28` "Other Alba is sitting in my chair with the reading lamp on" —— 她**早就坐在椅子上**，小 Alba 醒来就看见她，没有任何人推门 | 动作是套语，非原文情节 | 提示（不改情节走向，但"推门进来"与"已经坐在那里"是两种场面） |

## 三、错（两边都有但不一致）

| # | md 位置 | 原文 | 判 | 档 |
|---|---|---|---|---|
| 1 | md:31「亮着的只是**床头**那盏阅读灯」 | `text/ch23_red_galoshes.txt:28` "Other Alba is sitting in **my chair** with the reading lamp on" —— 灯在椅子上那个人手边/身旁，不在床头 | 位置微错 | 提示 |

> 说明：本章未发现数字、时序、归属方向的实质性错误；日期（4 月 7 日）、年份（2010 / 2047）、时刻（two a.m.）、"两周后的圣诞"均与原文一致。

## 四、R4 逐块对应（人判）

| 块 | 引语 | 中文是否在讲这句引语 | 主语/受事/归属 | 档 |
|---|---|---|---|---|
| 原句 1 | 黄房子/乐谱/去捡 | 是；"整段没有一句交代这是梦"限于引语范围内成立（引语前的 "The bad dream again." 未收） | 主语：她（捡）；受事：乐谱 | 通过 |
| 原句 2 | 以为是早上、其实是灯 | 是（"床头"见错 1） | 归属：椅子/台灯/浴袍都是 **Mama 的**，md 明确，未错 | 通过 |
| 原句 3 | 守密的负担 | 是 | 主语：她（分不清/怕）；受事：对 Daddy 说的话 | 通过 |
| 原句 4 | 死荫幽谷、作见证 | 是；"圣经回声"判断准确（诗篇 23） | 主语：未来的她（说）；受事：小 Alba | 通过 |

**结论**：4 块对应全部成立。问题仍是"块太少、被跳过的段落太长"——本章 1097 词只给 4 块（机器层 block_target 2–3，未报警），而对话体的关键在"她确认那个梦是真的"这一段，恰好没块。
