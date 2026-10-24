# ch35 Unhuman Music —— R3 对账（三张单）

- 素读：`review/ch35/1-suread.json`（12 条事实，仅读 `text/ch35_unhuman_music.txt`，488 行）
- 机器层：`review/ch35/2-machine.json`，rc=0，verdict=ok，blocks=7，segments=7，segment_miss=0，empty_quote=0，struct_bad=0，keyword_bad=0，cjk_low=0，words=2656
- 精读：`ch35 unhuman music.md`（122 行，7 个引语块 + 5 条导航 + 14 条词汇）
- 原文三段：`text/ch35_unhuman_music.txt:18` 2014-04-19（Alba 12, Isadora 5）／`:109` 2014-05-06（Alba 12）／`:285` 2014-07-16（Alba 39, Beck 38）

---

## 一、漏（素读有 / md 无）

### L1 「你只是台机器」→「goodbye」→道歉这一回合没有任何块承载

- 原文 `:179`：““You’re only a machine.””
- 原文 `:183`：““If I’m only a machine then you won’t mind if I get on with my machine work, goodbye.” The monitor goes black again.”
- 原文 `:187`：“I press Return. “I’m sorry, Isadora. I know you’re not just a machine.””
- md 侧：7 个块里没有一句引这三行；只有 `ch35 unhuman music.md:14` 在「人物弧线」里以「她对伊莎多拉从「你只是台机器」走到「她是你的女儿」」十四个字带过，读者看不到伊莎多拉怎样用「那你就别妨碍我做机器活」反击、也看不到阿尔芭按回车道歉。
- 影响：这是本章标题主题（机器/人）的第一次正面交锋，也是全局弧线的起点（ch35 末「她是你的女儿」正是对这里的回答）。
- 档：**提示**（导航有指认，故不判阻断；建议把 `:183` 补成一块）。

### L2 「I made a new Nina Simone song.」被整段丢掉

- 原文 `:267`：““That’s the idea,” Isadora says. “I made a new Nina Simone song. Would you like to hear it?””
- 原文 `:277`：“After we eat, I’ll ask Isadora to sing her Nina Simone song, so she doesn’t think I didn’t want to hear it.”
- md 侧：`/usr/bin/grep -c Nina "ch35 unhuman music.md"` → **0**（exit=1）；块、导航、总结三处都没有。
- 影响：这是伊莎多拉第一次**以他人署名生成新作品**——后文「版权/博物馆/谁能拥有音乐」这条线的第一个实证，比「写自己的歌」更锋利；而且它被传送打断、成了阿尔芭心里的欠账。
- 档：**提示**。

### L3 Joseph Cornell 已死、Beck 说死人扫出来会太「uncanny」，这层反讽未收

- 原文 `:247`：““I think Joseph Cornell is dead, Isadora.””
- 原文 `:251`：““I’ll tell Beck,” Isadora says. “Do you think he will be scannable if he is dead?””
- 原文 `:255`：““I asked her that once, and she said dead people would be too uncanny.””
- 原文 `:259`：“Isadora stops working. “In that case, perhaps this can wait.””
- md 侧：块 4 的读者视角只说「她正用贝克给的模糊照片重建 Joseph Cornell 的画室」；`grep -c uncanny` → **0**，`grep -c 死` → 0（md 未提他已死）。
- 影响：一个死人的画室正在被一个不会死的存在重建，而「死人不可扫描」正是全书反复出现的边界（ch32 Richard 之死、后文 Beck 想扫描逝者）；现在这层被抹平成一个布景名。
- 档：**提示**。

### L4 「It’s part of a very large causal loop; it isn’t mine to disrupt」未收

- 原文 `:456`：““I’m sorry, Beck,” I tell her, more moved by her unhappiness than I expected. “It’s part of a very large causal loop; it isn’t mine to disrupt, I can only try to mitigate its effects.””
- md 侧：`grep -c 因果` → **0**；块 7 只引 `:487` 的门廊段，块 6 只到 `:371` 的封存要求。中间「Jasper 找不到」「这是巨大因果环、不归我拆」整段（`:442`–`:456`）无块。
- 影响：成年阿尔芭的唯一一次「我不能改」自陈——她前一句还在给贝克下指令，这一句立刻承认自己受限于环。
- 档：**提示**。

### L5 块 7 中文漏译 `sister`

- 原文 `:488`：“Whatever it takes, sister. But I never knew that one of the things Isadora needed to be protected from was Beck.”
- md `ch35 unhuman music.md` 块 7 中文（`:81` 行）：「她心里说了一句「无论要付出什么」；但她从没想到……」
- 影响：`sister` 是回声——ch33 里伊莎多拉说「Alba is my sister」，此处阿尔芭回叫她 sister，两人互认姐妹；中文一省，这层关系链断了（英文引语里 `sister` 仍在，`grep -c sister` → 1）。
- 档：**提示**。

---

## 二、编（md 有 / 原文无）

无独立的编造情节。逐条核过 7 个块的英文引语，均可回原文定位；导航里的人名（阿尔芭/贝克/伊莎多拉/娜迪亚/约瑟夫·康奈尔）、日期（4/19、5/6、7/16，二〇四一年六月十五日）、年龄（12、39、38、5）、数字（第三趟、两天、五个八度外的「好几个八度」）均与原文一致。
（唯一近似编造的是下面 E3 的「会关门」，但那是比喻性转写，归到「错」单里判提示。）

---

## 三、错（两边都有 / 不一致）

### E1 导航与总结把三个日期都写成「地下室」，第三段其实在厨房与前廊

- 原文 `:290`：“I’m standing in front of the open refrigerator in the kitchen of my childhood home, eating cheese directly out of the package.”
- 原文 `:487`：“I’m not sleepy, so I sit on the front porch, listening to the night noises…”
- md `ch35 unhuman music.md:11`：「**三个日期的地下室会面**」；`:15`「三个带日期的第一人称段落，**靠同一间地下室串起来**」。
- 事实：第三段（7/16）全程在厨房（冰箱、茶壶、餐桌）与前廊，没有下过地下室；伊莎多拉那晚在地下室，两人**没有见面**（`:464` “I don’t think Isadora can hear us from her basement”）。
- 档：**提示**（把「同一间地下室」改成「同一栋房子」即可）。

### E2 总结说伊莎多拉「谎称住在 Nowhere」

- 原文 `:38`：““I don’t know where ‘everybody’ is. I am Nowhere.””
- 原文 `:60`：““I like this better. I made it myself. I come here when I want to think.””——Nowhere 是她自己造的地方，**不是谎话**。
- 原文 `:100`：“Isadora says, “Is that you, Beck? I thought I heard burglars upstairs!””——她真正撒的谎是这一句（贝克就在楼上）。
- md `ch35 unhuman music.md:122`：「她**谎称**住在「Nowhere」，又替阿尔芭瞒下来访。」
- 档：**提示**（「谎称」把她的自造空间误读成欺骗；后半句「替阿尔芭瞒下来访」才是 `:95` 的真话）。

### E3 人物弧线说伊莎多拉「会关门」，原文没有门

- 原文 `:183`：“…goodbye.” The monitor goes black again.”
- 原文 `:101`（四月十九日）：“As Beck is unlocking the basement door…”——关门的是贝克，不是伊莎多拉。
- md `ch35 unhuman music.md:14`：「伊莎多拉从躲在纸箱里的猫，变成**会关门**、会写歌、会自己改代码的存在。」
- 档：**提示**（若是想说「会挂断」，原文是黑屏；若是想说「会挡住贝克」，原文没有这个动作）。

### E4 情感弧线以「被抓包」起笔，四月十九日她并没有被抓到

- 原文 `:100`：“Beck is unlocking the basement door, I hide behind some of my dad’s boxes of books. She comes downstairs, but she doesn’t say anything else to Isadora, she just types. I’m afraid to move. Beck finally goes away, turns out the lights.”
- md `ch35 unhuman music.md:12`：「从**被抓包**的窘迫和好奇开始」。
- 事实：贝克始终没看见她，也没跟她说话；「被抓包」的是七月十六日那一段（`Beck scares me out of my skin when she says, “Alba?”`），不是开头。
- 档：**提示**（可改「差点被抓包」）。

---

## 四、R4 逐块对应（7 块，人判）

| 块 | 引语 | 中文是否在讲这句 | 三问（主语/受事/归属） | 结论 |
|---|---|---|---|---|
| 1 | `:23` 在娜迪亚家过夜→裸身落地下室、两天第三趟 | 是 | 主语＝阿尔芭；受事＝她自己（被传送）；「贝克只在她也在时才准她待」✓ | 对应 |
| 2 | `:65` 又热又吵、找不到衣服、羡慕一身毛 | 是 | 主语＝阿尔芭（找、说）；伊莎多拉反问「为什么不给自己做毛」✓ | 对应 |
| 3 | `:101` 只想着伊莎多拉骗了贝克、该不该说 | 是 | 主语＝阿尔芭；受事＝那条情报；「另一个阿尔芭」＝Other Alba ✓ | 对应，读者视角补足现场（乐高、血、贝克只打字） |
| 4 | `:114` 屏幕黑、楼上静、担心几人去了密歇根 | 是 | 主语＝阿尔芭（猜、担心）；受事＝母亲/贝克/另一个阿尔芭的去向 ✓ | 对应 |
| 5 | `:224` 声音跨八度、无节奏、回不到主音（也许是 D#） | 是 | 主语＝伊莎多拉（唱）；受事＝阿尔芭（听）；「加乐团再听一遍」✓ | 对应，密度足（未把「难听」写成结论） |
| 6 | `:350` 房子可以不要，请把乐谱扫进博物馆 | 是 | 主语＝成年阿尔芭（请求）；受事＝乐谱；接收方＝贝克/博物馆 ✓ | 对应 |
| 7 | `:487` 前廊、夜声、记忆宫殿里年幼的伊莎多拉、要防的人里有贝克 | 是（漏 `sister`，见 L5） | 主语＝阿尔芭（坐、想）；受事＝伊莎多拉；「protected from Beck」方向 ✓ | 对应（一处漏译） |

密度：7 块无一是字面复述——块 3「手上的忙和心里的乱被摁在同一段里」、块 5「连调性都不肯落实，歌的好坏被悬置」、块 7「用 But 一折，把整章的暖意掀开」都落在引语内部；无一块跑向全书主旨或作者生平。
