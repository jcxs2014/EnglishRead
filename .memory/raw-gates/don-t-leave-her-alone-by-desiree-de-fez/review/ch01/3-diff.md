# 第 1 章 R3–R4 差异单（人工审查）

- 审查对象：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch01 chapter 1.md`（成品，153 行，8 个引语块）
- 唯一真值：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch01_chapter_1.txt`（原文，30 行，6,308 字符）
- 机器层：`bash scripts/chapter.sh "…/ch01 chapter 1.md" --json` → **退出码 0**，`verdict: ok`，`issues` 四组全空（复核输出落在 `/tmp/ch01_machine_recheck.json`；仓库内 `review/ch01/2-machine.json` 未改动、未覆盖）
- 流程：R1 素读（`review/ch01/1-suread.json`，先读原文后开 md；该文件已存在且已提交，**本次未覆盖、未修改**）→ R2 机器层 → R3 三张单子 → R4 逐块＋固定三问
- 行号约定：`text:NNN` = 原文行号；`md:NNN` = 成品 md 行号；字符区间为原文 UTF-8 解码后的 `[start, end)`
- 取证口径：全部用显式路径 `/usr/bin/grep`（`text/` 被 `.gitignore` 忽略，`git grep` 对它永远查无），短词用 `-w`，括号匹配用 `-E`
- **本单状态**：`§〇` 的 6 条已由作者在审查过程中改好并提交（记为**已修复**）；`§一` 的 L1–L3 与 `§三` 中标「待改」的 W3／W4／W8／W9 及 W6 残余仍是**待改**项。本单只出指令，**未改动任何成品 md 文件**；`git` 未执行任何操作（未 add / 未 commit / 未 push）。

---

## 〇、本轮已修复（记录用，不再需要动）

| # | 位置 | 原写法 | 现写法 | 原文依据 | 复核命令（期望退出码） |
|---|---|---|---|---|---|
| F1 | `md:11` | 错过了女儿的**第一场**演出 | 错过了女儿的演出 | `text/ch01:12`「missed a school play」是往年旧例；`/usr/bin/grep -nw "first" text/ch01_chapter_1.txt` → 仅 `:30`（"or that the kids in the other year had gone first" 与 "The only child not singing"），本章无「第一场」 | `/usr/bin/grep -n "第一场" "…/ch01 chapter 1.md"` → 期望 exit=1 |
| F2 | `md:12` | 欲望线与恐惧线都还没**露面** | 欲望线与恐惧线都还没**成形** | `00_情感节点.md:58`「节点六：恐惧越过家门（ch06-ch07）」⇒ 恐惧线在 ch01–05 尚在家门内，到 ch06–07 才跨出门 | `/usr/bin/grep -n "都还没露面" "…/ch01 chapter 1.md"` → 期望 exit=1 |
| F3 | `md:37` | 真女王正站在**楼下**为一只插头发疯 | 真女王正**走在去学校的路上**，为一只插头发疯 | `text/ch01:15`「But halfway there, her heart started pounding in her ears.」＋「So she hurried back up Balmes, teary-eyed, embarrassed.」（区间 `[1664,1721)`、`[2848,2902)`）——心慌在半路／巴莱姆街，不在楼下 | `/usr/bin/grep -n "站在楼下" "…/ch01 chapter 1.md"` → 期望 exit=1 |
| F4 | `md:51` | Brisa 在**本章里唯一一次**自己做主 | Brisa **在台上第一次**自己做主 | `text/ch01:6`「Failing to see her mom in the crowd, she decided to stop looking.」（`[652,716)`）；`:30`「Stung by her mother's absence, she had sunk into the choir.」（`[6164,6222)`）另是一次自主动作 ⇒ 「本章唯一」不可核 | `/usr/bin/grep -n "唯一一次" "…/ch01 chapter 1.md"` → 期望 exit=1 |
| F5 | `md:97` | **破折号**后那句自我辩解用 sure 开场 | **分号**后那句自我辩解用 sure 开场 | `text/ch01:21`「…she wasn't ridiculous; sure, she had missed the start of the play…」（`[3982,4072)`）；`/usr/bin/grep -c ";" text/ch01_chapter_1.txt` → 1（本章唯一分号） | `/usr/bin/grep -n "破折号" "…/ch01 chapter 1.md"` → 期望 exit=1 |
| F6 | `md:111` | 那里是**别人给她戴上的耳环**，她连自己身上多了什么都不知道 | 那里是**她自己身上多了九只从没见过的耳环**，连多出来的是什么都说不清 | `text/ch00:21`「she saw that her ears were covered in new piercings, full of earrings she'd never seen before. She counted nine hoops, all different sizes, five in one ear and four in the other…」（`[1535,1628)`、`[1630,1712)`）——是**新扎的耳洞**，她数清了九个，不是别人给她戴的 | `/usr/bin/grep -n "别人给她戴上" "…/ch01 chapter 1.md"` → 期望 exit=1 |

---

## 一、漏（L）

### L1｜块 5 的「他」从头到尾没有身份——是谁、他在哪儿、谁能替她拿主意，全篇未交代｜档：提示（漏）

**原文侧**（`text/ch01_chapter_1.txt:12`，字符区间 `[818,908)`）：

> "Her partner was going to be in Madrid all day, so a classmate's mom was picking up her son."

**原文侧**（`text/ch01_chapter_1.txt:15`，字符区间 `[2521,2546)`、`[2548,2595)`、`[2825,2846)`）：

> "She turned halfway around. She called Carlos to tell him what had happened." / "But he didn't pick up."

**原文侧**（`text/ch01_chapter_1.txt:15`，字符区间 `[2597,2657)`）：

> "She wanted him to pick up and tell her what she knew already: that she hadn't left the straightener on, or the door open, or the lock unlocked. She wanted him to make the decision for her, tell her not to go back home to check."

**md 侧**（`ch01 chapter 1.md:69`、`md:71`、`md:73`、`md:75`）：

> 她想让他接电话，告诉她那些她自己本来就知道的事：直发夹没开着，门没开着，锁没落下。她想让他替自己做决定，叫她别回去查看。可他没接。

> **关键词**：tell her what she knew already · make the decision for her · But he didn't pick up

**影响**：块 5 的全部解读（`md:73`「她要的不是信息，是一个能替她背书的人」、`md:75`「记住她要的两样东西：确认和决定」）都建立在这个「他」身上，但成品 md 的**分析层**从头到尾没说他是谁、为什么接不到电话。读者读完块 5 只知道「有个男人没接电话」，无法把「外部担保缺席」这一层读实。姓名与身份只出现在词汇表的例句里（`md:145`），不能替代分析层的交代。

**修法（建议）**：在块 5 的「中文理解」或「为什么这样写」里补一句身份与处境：「他＝她的伴侣 Carlos（原文用 *Her partner*），当天整天在 Madrid；接走儿子的是儿子同班同学的妈妈（:12）」。

### L2｜出门前她已经检查过、并且复查过（一个小时前）——这条没进 md，而它正是「焦虑无据」的证据｜档：提示（漏）

**原文侧**（`text/ch01_chapter_1.txt:21`，字符区间 `[4368,4431)`）：

> "Everything was in order. Everything had been checked, and checked again, an hour earlier."

**md 侧**（`ch01 chapter 1.md:11`）：

> ……母亲 Diana 忽然想起自己可能把直发夹开着没关，硬是折返回家查证；一切安然无恙……

**md 侧**（`ch01 chapter 1.md:93`、`md:99`）：

> 她甚至盼着有一场无害的小火……是啊，她错过了演出开头，但她也避免了一场大祸。

> 记住这个愿望（盼一场小火）。它解释了后面她推开门那一刻的心情：什么都没发生，等于什么都没被证明。

**影响**：原文里她**已经查过两遍**（`:21`），出门前一个小时就查完了；这正是后面「白跑一趟」式自嘲的来源，也让「折返」显得多余。成品 md 只写「硬是折返回家查证」，把「她本已查过」这一层丢了，读者会误以为她出门前根本没查过。

**修法（建议）**：在 `md:11` 或块 7 的中文理解里补一句「（其实出门前一个小时她已经查过一遍、又复查了一遍，:21）」。

### L3｜她本来准备好的「两个人的一天」——去看演出，然后带 Brisa 去吃点东西——没进 md｜档：提示（漏）

**原文侧**（`text/ch01_chapter_1.txt:12`，字符区间 `[910,1058)`）：

> "She had blocked off the afternoon weeks in advance: She'd go to the performance, then take Brisa out for a treat. A girls' day, just the two of them."

**md 侧**（`ch01 chapter 1.md:11`、`md:14`）：

> ……她却因此错过了女儿的演出，只能独自坐在最后一排，看女儿把金色皇冠折成面具蒙住自己。

> Diana 从「工作提前交稿、准备做完美妈妈」一路掉到「坐在最后一排独自看台」……

**影响**：`md:11` 与 `md:14` 写的是「错过演出」这一半损失；原文里她精心空出来的下午是「一场两个人的约会」（a girls' day, just the two of them），成品完全没提这个约定。这样一来「Diana 坐在最后一排独自看台」读起来只是「来晚了」，原文那层「精心安排却只剩她一个」的落差就薄了一层。

**修法（建议）**：`md:11` 补「（她连空出整个下午、带女儿去吃点东西的『两个人一天』都提前几周排好了，:12）」。

---

## 二、编（C）

**无。** 已逐条核对成品 md 的全部 5 条导航（`md:11-15`）、8 个引语块的四个子项（`md:19-111`）、词汇表 21 条（`md:113-149`）、一句话总结 1 条（`md:153`）中的**事实性断言**（人名、数字、时间、亲属关系、事件、地点、次数），未发现「md 有、原文无」的杜撰事实。命中疑点的 9 处全部属于「错」（措辞／地点／时序／归属／不可核计数）或「漏」，已分别落在下面两张单子里。核对面记要：

- **人物**：md 出现的 Diana、Brisa、「他（伴侣，Carlos）」三个具名／具指人物，在原文均有出处；md 未给 Carlos 写「丈夫」——原文本章用的是 `Her partner`（`:12`），md 的处理是对的。
- **关系**：`md:14`「Brisa 从「在台上四处找妈妈」到「用皇冠做成面具、蒙住自己」」— 与 `:6`（scan the room for her mother）、`:30`（made a mask of the golden crown）一致。
- **数字**：md 涉及的全部数量（几周前排好、练了几周、半米、一个小时前、一百倍）— 逐条对到原文（`:12` `weeks in advance`、`:6` `spent weeks preparing`、`:21` `half a meter`、`:21` `an hour earlier`、`:30` `multiplied by one hundred`）。
- **时间**：md 未给本章标日期；原文内部无日期字面（日期只在 epub 分隔页，见 `1-suread.json`）。
- **事件**：`immaculate white`、圣诞诗、`playback`、`temperature gauge`、`But he didn't pick up`、`dishrag`、`harmless flame`、`felon in a lineup`——八块引语与 md 的转述逐句对得上，无新增情节。
- **体例用词**：`md:13`「圣诞舞台剧这一节令场景」属 `Tropes 兑现/反转` 栏的分析标签，不是事实断言，本单不作事实判定（列入 `4-verdict.md` 判定表为「跳过」）。

---

## 三、错（W）

### W1｜`md:97`「破折号后那句自我辩解」——原文那里是分号，不是破折号｜档：提示｜**已修复**

**原文侧**（`text/ch01_chapter_1.txt:21`，字符区间 `[3982,4072)`）：

> "to prove to herself that she wasn't ridiculous; sure, she had missed the start of the play, but she'd also averted a total catastrophe."

**md 侧（修前）**（`ch01 chapter 1.md:97`）：

> ……破折号后那句自我辩解用 sure 开场……

**md 侧（修后）**（`ch01 chapter 1.md:97`）：

> ……分号后那句自我辩解用 sure 开场……

**影响（修前）**：`md:97` 指的是分号后那句自我辩解——这是原文唯一的分号（`/usr/bin/grep -c ";" text/ch01_chapter_1.txt` → 1）。写成「破折号」会把读者引向块 7 引文里并不存在的破折号，而块 7 引文本身（`md:91`）也没有破折号（引文起点在 "She longed for…"）。属于标点层面的指针错位。

**修法**：已按建议改成「分号后」——本条关闭。

### W2｜`md:37`「真女王正站在楼下为一只插头发疯」——她发疯的地方是**半路**，不是楼下｜档：提示｜**已修复**

**原文侧**（`text/ch01_chapter_1.txt:15`，字符区间 `[1664,1721)`、`[2848,2902)`）：

> "But halfway there, her heart started pounding in her ears." / "So she hurried back up Balmes, teary-eyed, embarrassed."

**md 侧（修前）**（`ch01 chapter 1.md:37`）：

> 孩子演的是「女王」，而真女王正站在楼下为一只插头发疯。

**md 侧（修后）**（`ch01 chapter 1.md:37`）：

> 孩子演的是「女王」，而真女王正走在去学校的路上，为一只插头发疯。

**影响（修前）**：心跳擂耳、折返、涨红脸这一串发生在**去学校的半路上／巴莱姆街上**（"halfway there"、"hurried back up Balmes"）；「楼下」会被读成公寓楼下或舞台侧幕，而原文里「楼下」（自家楼门口）是她**已经赶回去确认完**、发现一切正常之后的位置（`:21`）。

**修法**：已按建议改成「走在去学校的路上」——本条关闭。

### W3｜`md:37`「观众（父母们）会为这段稚气台词喝彩，母亲听见的却是自己缺席的证据——同一段台词，两种读法」——父母喝彩的是**那首歌**，母亲听见的是**歌**、诗她已错过｜档：提示｜**待改**

**原文侧**（`text/ch01_chapter_1.txt:30`）：

> "Diana's eyes clouded and her legs shook when, from the hallway, she heard the Christmas song Brisa had been humming at home for weeks."

**原文侧**（`text/ch01_chapter_1.txt:30`）：

> "After the poem, the kids launched into a loosely religious version of a Taylor Swift song. The parents laughed loudly, eager to show they recognized a song so famous that even an alien would know it."

**md 侧**（`ch01 chapter 1.md:37`，修后仍在）：

> 作者把它原样搬进母亲的视野里，于是同一句童谣同时是背景音乐和反讽……观众（父母们）会为这段稚气台词喝彩，母亲听见的却是自己缺席的证据——**同一段台词，两种读法**。

**影响**：原文里 Diana 从**走廊**听见的是「the Christmas song」（那首 Taylor Swift 版歌），而「After the poem」明写她进厅时**诗已经结束**；父母们喝彩（"laughed loudly"）也是在**歌**上，不在「稚气台词」上。块 2 引的正是那首诗。⇒ md 说「同一段台词，两种读法」，而母亲那一侧根本没听到这段台词；「背景音乐」这个说法也只能对应歌，不能对应诗。

**修法（建议）**：`md:37` 改为「……观众（父母们）会为那首 Taylor Swift 版的歌喝彩；而母亲从走廊里听见的也是这首歌——**诗她已经错过了**，同一场演出，两种读法」。

### W4｜`md:39`「而妈妈错过了整场」——原文她只错过了**开场**，Brisa 那段她是在场的｜档：提示｜**待改**

**原文侧**（`text/ch01_chapter_1.txt:21`）：

> "sure, she had missed the start of the play, but she'd also averted a total catastrophe."

**原文侧**（`text/ch01_chapter_1.txt:30`，字符区间 `[5594,5630)`、`[6039,6162)`）：

> "Diana sat down alone in the last row…" / "The only child not singing, she had crossed her arms and made a mask of the golden crown her classmates wore on their heads."

**md 侧**（`ch01 chapter 1.md:39`）：

> Brisa 练了整周，而妈妈错过了整场。

**影响**：原文两处明写她只错过**开始**（"missed the start of the play"），随后她坐进最后一排，**亲眼看见** Brisa 折皇冠做面具、独自退进合唱队。md 的「整场」与成品自己的 `md:11`／`md:14`（「看女儿把金色皇冠折成面具蒙住自己」「坐在最后一排独自看台」）自相矛盾，也与原文冲突。

**修法（建议）**：`md:39` 改为「Brisa 练了整周，而妈妈**错过了开场那一段诗**」。

### W5｜`md:51`「这是 Brisa 在本章里唯一一次自己做主」——不可核的绝对计数，且 :30 的动作同样是自主动作｜档：提示｜**已修复**

**原文侧**（`text/ch01_chapter_1.txt:6`，字符区间 `[652,716)`）：

> "Failing to see her mom in the crowd, she decided to stop looking."

**原文侧**（`text/ch01_chapter_1.txt:30`，字符区间 `[6164,6222)`）：

> "Stung by her mother's absence, she had sunk into the choir."

**md 侧（修前）**（`ch01 chapter 1.md:51`）：

> 这是 Brisa 在本章里**唯一一次**自己做主，也是她后面那个面具动作的前奏。

**md 侧（修后）**（`ch01 chapter 1.md:51`）：

> 这是 Brisa 在台上**第一次**自己做主，也是她后面那个面具动作的前奏。

**影响（修前）**：①「唯一一次」属不可核的绝对计数（本任务的写法铁律亦禁止「唯一／全书唯一」这类断言），原文里「she decided to stop looking」与「she had sunk into the choir」两处都是 Brisa 自己下的决定；② md 自己也说这是「那个面具动作的前奏」，等于承认后面还有一次自主动作。

**修法**：已按建议改成「在台上第一次自己做主」——本条关闭。

### W6｜`md:111`「序章里……别人给她戴上的耳环，她连自己身上多了什么都不知道」——序章里是**她自己新扎的耳洞**，而且她数得清清楚楚｜档：提示｜**主体已修复，残余待改**

**原文侧**（`text/ch00_prologue.txt:21`，字符区间 `[1535,1628)`、`[1630,1712)`、`[1815,1895)`）：

> "she saw that her ears were covered in new piercings, full of earrings she'd never seen before. She counted nine hoops, all different sizes, five in one ear and four in the other… The appointment she couldn't remember must have been long, unhygienic, and cruel."

**md 侧（修前）**（`ch01 chapter 1.md:111`）：

> 记住这条闪亮纸带：拿东西把自己遮住这个动作，序章里也出现过一次——只不过那里是别人给她戴上的耳环，她连自己身上多了什么都不知道。

**md 侧（修后）**（`ch01 chapter 1.md:111`）：

> 记住这条闪亮纸带：拿东西把自己遮住这个动作，序章里也出现过一次——只不过那里是她自己身上多了九只从没见过的耳环，连多出来的是什么都说不清。

**影响（修前）**：原文三处与 md 相反：① `new piercings` ＝**新扎的耳洞**，不是现成耳环被「别人给她戴上」；②「她连自己身上多了什么都不知道」过头——她**数清了九个耳环**（一边五个、另一边四个），她不知道的只是「预约那天的过程」；③序章那个女人是带着 **Brigitte** 的母亲（`text/ch00_prologue.txt:15`「the last time she'd been here, with Brigitte」，区间 `[354,424)`），即 Alba 线，与本章 Diana/Brisa 不是同一条线。

**残余（待改）**：修后句首「**拿东西把自己遮住这个动作**，序章里也出现过一次」仍无出处——序章里她没有用任何东西遮住自己，她只是在**镜子里看见自己**（`text/ch00:21`「She caught her reflection in one of those mirrors where girls admired their ballet slippers.」），脸上是血、头发打结。且序章属 Alba 线，读者若不点明，会把 Brigitte 与 Brisa 混成一人。

**修法（建议）**：`md:111` 改为「……序章里也出现过一次——只不过那里是她**自己新扎了九个耳洞（一边五个、另一边四个），醒来时对着镜子数了半天**（`ch00:21`），而序章的女人是带着 **Brigitte** 的母亲，不是本章这条线」。

### W7｜`md:12`「欲望线与恐惧线都还没露面」——与总览的恐惧线起点冲突｜档：提示｜**已修复**

**总览侧**（`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/00_情感节点.md:58`）：

> ## 节点六：恐惧越过家门（ch06-ch07）

**md 侧（修前）**（`ch01 chapter 1.md:12`）：

> ……欲望线与恐惧线都还没**露面**，本章先把母亲的焦虑机制摆上台面。

**md 侧（修后）**（`ch01 chapter 1.md:12`）：

> ……欲望线与恐惧线都还没**成形**，本章先把母亲的焦虑机制摆上台面。

**影响（修前）**：「恐惧线」是全书体例里的既有线索，而总览把它明写为「**从家里**走到学校」——「家里」这一端就是本章；说本章「恐惧线还没露面」与总览直接打架。修后改「成形」与 `00_情感节点.md:58`「恐惧越过家门（ch06-ch07）」自洽。

**残余（提示，可不改）**：`md:97` 自己就把这一章的焦虑写成「反向欲望」，因此「欲望线还没成形」与同章 `md:97` 有一层张力；属用词口径问题，不影响事实判定。

### W8｜`md:109`「开头它是「象征纯洁」的道具」——「象征纯洁」属于**纯白**，不属于金色皇冠｜档：提示｜**待改**

**原文侧**（`text/ch01_chapter_1.txt:6`，字符区间 `[142,218)`）：

> "The idea was that everything should be immaculate white, to symbolize purity, but a few pairs of beige Decathlon pants and threadbare T-shirts kept the scene from flawlessness."

**md 侧**（`ch01 chapter 1.md:109`）：

> 皇冠在这里完成了闭环：开头它是「象征纯洁」的道具，现在被她折成面具蒙住自己——**同一件道具，从装饰变成了遮蔽物**。

**md 侧**（`ch01 chapter 1.md:25`，同一份 md 内部，读法正确）：

> 作者先立一个童话标准（天使、洁白的翅膀、象征纯洁），再用一个现实细节把它戳破……

**影响**：`to symbolize purity` 修饰的是 `everything should be immaculate white`；皇冠在原文里只是天使戏服的装束（`golden crowns`，与 `wings made of cardboard and cotton` 并列），不承载「纯洁」。md:109 把这个归属挪给了皇冠，与 md:25 自己的正确读法也冲突。

**修法（建议）**：`md:109` 改为「皇冠在这里完成了闭环：开头它是**天使戏服的装束**（连同那一身 immaculate white 的纯洁标准），现在被她折成面具蒙住自己」。

### W9｜`md:15`「舞台上的道具与序章那家童趣店互相呼应」——属于读者联想，原文没有给出呼应信号｜档：提示｜**待改**

**原文侧**（`text/ch01_chapter_1.txt:6`）：

> "They wore wings made of cardboard and cotton, golden crowns, glitter on her chubby cheeks."

**原文侧**（`text/ch00_prologue.txt:18`）：

> "rows of tutus splattered with red, red-stained butterfly wings and plush earmuffs… all covered in a now-stiff crust of dried blood."

**md 侧**（`ch01 chapter 1.md:15`）：

> ……结尾把镜头交还舞台，用「犯人列队」式的比喻收束。**舞台上的道具与序章那家童趣店互相呼应。**

**影响**：两处确有表面重合（都有翅膀、都有头饰），但序章那批道具在原文里是**血壳**，语义与本章的「纯白天使」正好相反；把这种表面重合断言成作者层面的「互相呼应」，是解读而非事实，且容易盖住 W6 指出的归属错位（序章是 Alba 线）。

**修法（建议）**：`md:15` 加限定词，例如「**读作**呼应：舞台上的纸板翅膀与皇冠，对上序章童趣店里被血壳盖住的蝴蝶翅膀与发箍——同一批道具，两种下场」。

---

## 四、交叉说明

1. **称呼链（决定 W6 的档位）**
   - `text/ch00_prologue.txt:15`：「the last time she'd been here, with Brigitte, trying on plastic tiaras.」＋ `:18`「in her daughter's favorite store, where Brigitte mistook cheap jewelry for the real thing」⇒ 序章的女人是带 **Brigitte** 的母亲。
   - `text/ch01_chapter_1.txt:6`／`:12`／`:30` ⇒ 本章是 **Brisa** 一侧（母亲 Diana）。
   - `text/ch02_chapter_2.txt:468`「the girls' noses had both bled dramatically」＋ `text/ch02_chapter_2.txt:477`「while her cousin was at gymnastics, Brisa was sleeping in her room」⇒ Brisa 与 Brigitte 是表姐妹，两人分属 Diana 线与 Alba 线。
   - 结论：`md:111` 借序章作类比时，必须点明那是**另一条线**（Alba），否则读者会把两个孩子当成同一个。
2. **时间轴链（决定 W3、W4 的档位）**
   - `text/ch01_chapter_1.txt:15`「But halfway there」＝ 半路心慌；`:18` 撞见家长；`:21` 回到自家楼下确认；`:27` 独立成段「Diana arrived at the Christmas play late, her pinkie toes raw.」（区间 `[4438,4499)`）；`:30` 进厅——「After the poem」也在 `:30`，即**诗在她到时已结束**，她从**走廊**听见的是「the Christmas song」。
   - 结论：她**只错过开场**（`:21`「she had missed the start of the play」），Brisa 折皇冠那一段她**在场**。
3. **「更脏的样子回来」不是无出处（推翻既有怀疑）**
   - `text/ch02_chapter_2.txt:471`：「The neckline of her leotard, white with silver trim, was soaked with blood.」（区间 `[35880,35955)`）——纯白 + 血，落点明确。
   - `text/ch00_prologue.txt:18`：「rows of tutus splattered with red… a now-stiff crust of dried blood.」
   - 结论：`md:27`「记住这个纯白标准。它在本章是幼儿园舞台的装饰，后面还会以更脏的样子回来」**成立**，不得改动（另见 `4-verdict.md` 的「已核实为正确」）。
4. **绝对计数类断言的取证结果**
   - `/usr/bin/grep -nw "first" text/ch01_chapter_1.txt` → 仅 `:30`（"or that the kids in the other year had gone first" 与 "The only child not singing"）⇒ 「第一场演出」在原文无据（`md:11` 已改，记为**已修复** F1）。
   - `/usr/bin/grep -nwE "only|sole" text/ch01_chapter_1.txt` → 仅 `:30` 的 "The only child not singing" ⇒ `md:51` 的「唯一一次自己做主」在原文亦无据（F4 已修复）。
5. **标点与拼写取证（W1）**
   - `/usr/bin/grep -c ";" text/ch01_chapter_1.txt` → 1（唯一分号在 `:21` 的 "she wasn't ridiculous; sure, …"）。
   - `/usr/bin/grep -n "破折号" "ch01 chapter 1.md"` → 修前命中 `md:97`（本书该词只此一处），修后无命中。
   - ⚠️ 取证注意：`text/` 里的弯引号是 U+2019；在 `LC_CTYPE=C` 的环境下 `/usr/bin/grep -o "she.d"` **匹配不到**（实测退出码 1），必须直接写 U+2019 字面量或改用 `-E` 与 Unicode 类匹配，不要拿 `she.d` 下取证结论。

---

## 五、修后复核（改稿后按此复核）

1. L1：块 5 补「他＝伴侣 Carlos，当天在 Madrid，儿子的同班同学的妈妈替他接孩子」（`:12`、`:15`）。
2. L2：`md:11` 或块 7 补「出门前一个小时她已查过一遍、又复查了一遍」（`:21`）。
3. L3：`md:11` 补「带 Brisa 去吃点东西的『两个人一天』提前几周就排好了」（`:12`）。
4. W3：`md:37` 改成母亲听见的是那首 Taylor Swift 版的歌、诗她已错过。
5. W4：`md:39`「错过了整场」→「错过了开场那一段诗」。
6. W6 残余：`md:111` 补「她自己新扎了九个耳洞（一边五个、另一边四个）」并点明序章是 Alba 线、不是「拿东西遮住自己」。
7. W8：`md:109`「象征纯洁」的归属改回「纯白」。
8. W9：`md:15`「互相呼应」加限定词。
9. 复核命令：
   - `/usr/bin/grep -nE "站在楼下|错过了整场|别人给她戴上|象征纯洁」的道具" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch01 chapter 1.md"` → 期望退出码 1（改后无输出）。
   - `/usr/bin/grep -nE "第一场|唯一一次|破折号|都还没露面" "…/ch01 chapter 1.md"` → 期望退出码 1（已修复项，改后无输出）。
   - `/usr/bin/grep -n -w "first" "…/text/ch01_chapter_1.txt"` → 期望仍只命中 `:30`（原文不需改）。
   - `bash scripts/chapter.sh "…/ch01 chapter 1.md" --json` → 期望退出码 0、`issues` 仍全空。
10. 本单只出指令，**未改动任何成品 md 文件**；`git` 未执行任何操作（未 add / 未 commit / 未 push）。
