# ch27 判定表

机器层 rc=0，**4 块**（`block_target=[2,4]`、`block_limit=[2,15]`、`block_count=0` 未判红）。人判结论：**漏 8 · 编 0 · 错 4 · 提示 10**（表内 12 行，其中阻断 2 行）；阻断 2 条（L1 漏、E1 错）。

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| Isadora 场景整段未进任何块，也没进导航/总结 | `text/ch27_speculations_upon_the_nature_of_love.txt:37`「But this morning, when I arrived at my studio later than usual, Isadora asked me where I'd been, and before I could answer, she said, “You were with Clare.”」；`:44`「Isadora said, “Clare is a wild thing.”」；`:52`「Isadora replied, “Wild thing, you make everything groovy,” and then I started to cry, as though we're going to live happily ever after, after all.」；md 侧 `/usr/bin/grep -c -F "Isadora"` → `1`（仅 `:75` 词汇例句）、`"groovy"` → `0` | 漏：第一则短记的情绪落点整体缺失 | **阻断** |
| 导航把「先问『现在？』」记在 Clare 头上 | 4/24 那则署 `Clare:`（`:65`「Clare: We have to get a little drunk beforehand…」），段内 `:65`「finally **she** says, “Now?” and **I** say, “Yes,”」⇒「she」＝Beck、「I」＝Clare | 错：说话人归属反转（「先笑」与「先邀」确为 Clare，唯独这一件不是） | **阻断** |
| 「You're perfect.」／「Don't burden me with that.」整段未引 | `:75`「I say, “You're perfect.”」；`:79`「“Don't burden me with that. Sooner or later I'll disappoint you and what then?” … “Don't worry. Let's just be, here.”」；md `grep -c -F "perfect"` → `0`、`"burden"` → `0` | 漏：他把「理想的爱人」与真人分开的那一刀没落地 | 提示 |
| 「I love you」卡在喉咙里未引 | `:84`「“Here and now,” I say. I want to say I love you but it catches in my throat.」 | 漏（总结 `:90` 有转述） | 提示 |
| 「I've been waiting for Henry since I was a child. It's hard to stop.」「I'd like to live in the present, with you.」只活在词汇例句 | `:162`「She says, “I've been waiting for Henry since I was a child. It's hard to stop.”」；`:171`「“You're here now. I'd like to live in the present, with you.”」；md `grep -c -F "waiting for Henry"` → `0`；`"present"` → `1`（`:86` 词汇例句） | 漏：全章最重的一组台词没有块 | 提示 |
| Henry 会「在早饭时出现」与黑人／女人的玩笑未引 | `:111`「“It's weirder than that. I don't want you running into him at breakfast.”」；`:120`「“Henry wouldn't have been minded about the brown, it's the lady part that would have surprised him.”」；md `grep -c -F "breakfast"` → `1`（`:85` 词汇例句）、`"shacking up"` → `1`（`:76` 词汇例句） | 漏（只在词汇例句） | 提示 |
| 日期年龄不齐 | `:18`「Sunday, April 18, 2010 (Beck is 34, Clare is 38)」；md 只有「四月十八日」等，无年份、无 34／38 | 形态不齐（同批 ch24 亦缺） | 提示 |
| Alba 八岁、住外公或 Mrs. Kim 的前提缺失 | `:97`「she's only eight … So Alba stays with her grandfather or Mrs. Kim, and Clare comes to my apartment.」；md `grep -c -F "八岁"` → `0`、`"Kimy"` → `0`、`"grandfather"` → `0` | 漏（Beck 为何要问「couldn't I come over?」失去前提） | 提示 |
| O'Hare 表亲午饭缺失 | `:33`「we meet my cousins for lunch near O'Hare one day when they have a layover, and she gets along with them immediately—we are joking around together before the drinks arrive.」 | 漏 | 提示 |
| 「两个月后」不实 | `:60`「Saturday, April 24, 2010」→ `:92`「Sunday, May 30, 2010」＝36 天 | 数字松散 | 提示 |
| 中文层两个「她」指两个人 | `:21`「她急切又客气，怕自己冒犯了她，为她担心」对 `:28`「who is afraid she's offended **me**, who worries about **me**」 | 指代不清 | 提示 |
| 原句 3 把一个「我」拆成两个「她」 | `:41`「她不再是从前那个和 Henry 做爱的人，她也不是原来那个自己」对 `:65`「**I am not the same me** that used to make love to Henry」 | 释义走了形（原文是同一个我的前后两版） | 提示 |

**报数（四组）**

- **逐字**：4 块全部命中（`segment_miss=0`、`empty_quote=0`）；四处起点/终点均与原文对齐（`:28`/`:33`/`:65`/`:145`）→ **逐字 0 缺陷**
- **对应**：4 块逐块过 R4 均答「这段中文在讲这句引语」；问题不在错译，而在**该有的块没有**（L1/L4 两条台词被降级成词汇例句）→ **对应 0 阻断、2 提示（L1、L4）**
- **形态**：H1 `27. Speculations Upon the Nature of Love` ✓；导航 5 项 ✓；子项 4 项齐 ✓；4 块在 `block_target=[2,4]` 内 ✓；三日期结构在 md 里以「四月十八日／四月二十四日／五月三十日」保留 ✓ → **形态 1 提示（年龄与年份）**
- **断言**：唯一硬错是 E1 的说话人归属 → **断言 1 阻断**

## R4 逐块对应（人判）

| 块 | 引语 | 主语 / 宾语 / 归属核查 | 结论 |
|---|---|---|---|
| 原句 1 | `:28`「Instead I found Clare—…Clare who listens and Clare who understands.」 | 说话人＝Beck（4/18 署 Beck）✓；「who is afraid she's offended me」的 me＝Beck ✓。md 中文层两个「她」混用（E3），但方向没反 | 对应；释义层需改指代 |
| 原句 2 | `:33`「Is it love? It feels too easy—…」 | 自问者＝Beck ✓；「she doesn't give me a look as though I should have already known」的 she＝Clare ✓ | 对应，密度足（把「顺」读成可疑信号） |
| 原句 3 | `:65`「It's all so different because she is she and I am not the same me that used to make love to Henry…」 | 说话人＝Clare（4/24 署 Clare）✓；「she」＝Beck、「I」＝Clare ✓；「my future beloved」＝从未来回来的 Henry ✓（md `:47` 解成「那时有人从未来回来，替她担保结局」，方向正确） | 对应；E4 只影响中文层措辞 |
| 原句 4 | `:145`「He used to, when I was a kid. I know of a few occasions in the future—Alba has told me, or Henry mentioned that he'd seen me…」 | 答话人＝Clare ✓；「He」＝Henry ✓；信息来源三分的对应（Alba 说的／Henry 提的／她不知道的）在 md `:55` 里逐个交代 ✓ | 对应 |

## 已核实为正确（防下一轮误修）

| 看着可疑的写法 | 原文 | 核实结果 |
|---|---|---|
| 导航 `:14`「先笑出声」记在 Clare 头上 | `:70`「And **I** start laughing, just out of relief, and joy」（4/24 段署 Clare） | **正确**，别跟 E1 一起改掉——错的只有「先问『现在？』」一项 |
| 导航 `:14`「最后先发出邀请」记在 Clare 头上 | `:179`「but a few days later Clare says, “Would you like to come over for lunch on Saturday? And meet Alba?”」 | 正确 |
| 导航 `:13`「反转『鬼魂』：Henry 的时空跳跃被 Beck 叫作闹鬼，Clare 只答「也许」」 | `:158`「“Is it like being haunted?” I ask.」（Beck 问）；`:160`「“Maybe?” Clare turns onto her side」 | 正确：问的是 Beck、答的是 Clare |
| 「三则标了日期的日记，两则出自 Beck、一则出自 Clare」 | `:18` Beck / `:65` Clare / `:97` Beck | 正确 |
| 「她是寡妇、灰眼睛里有戒备」 | `:28`「a widow with a guarded expression in her gray eyes」 | 正确；Alba 八岁见 `:97`，与 ch25 `:18` 的「Alba is 8」一致 |
| 「Henry 从未来回来替她担保结局」的读法 | `:65`「I have no assurance from my future beloved that this will all be okay」 | 正确释义，不是编 |
