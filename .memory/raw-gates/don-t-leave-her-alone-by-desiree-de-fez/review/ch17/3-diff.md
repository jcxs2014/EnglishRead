# ch17 审查工作底稿（R3 三张单子 + R4 逐块对应）

- 审查对象：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch17 chapter 17.md`（153 行）
- 唯一真值：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch17_chapter_17.txt`（3,232 词 / 18,353 字符 / 19,155 字节 / 378 行）
- 落盘目录：`.memory/raw-gates/don-t-leave-her-alone-by-desiree-de-fez/review/ch17/`
- 审查员：DSH-Mac（受托审查，**本轮只出指令不改稿**；未改任何 `ch*.md` / `00_*.md`，未 git add/commit/push）
- 章型：末章 → 重 S5（总结层 / 总览层）

---

## 0. R2 机器层（先看机器，再动眼睛）

`bash scripts/chapter.sh "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch17 chapter 17.md" --json > .memory/raw-gates/don-t-leave-her-alone-by-desiree-de-fez/review/ch17/2-machine.json`

- 退出码 **0**（0 无阻断 / 1 阻断 / 2 无法判定；2 才不是通过）
- verdict `ok`；8 块引语 `ok:true`；`segment_miss=0`、`struct_bad=0`、`keyword_bad=0`、`cjk_low=0`
- form：`h1 "17. Chapter 17"` / `h1_shape_ok=true`；`nav_count=5 ok`；子项集 `[中文理解, 关键词, 为什么这样写, 读者视角提示]`；`blocks=8`、`block_median=7.0`、`block_range=[5,8]`；profile `novels`；baseline `book`
- ⇒ **机器层无阻断，但机器查不出"这一句在讲什么/收束读成什么"**（本轮 5 条阻断全部落在 S5 总结层与 R4 对应层，机器全绿也照样成立）

---

## 1. R3 单子一 · 漏（素读有、md 无）

| # | md 侧 | text 侧（逐字） | 判 | 档 |
|---|---|---|---|---|
| **M1** | 全文零命中 `fryer / 空气炸锅 / 炸锅`（grep 退出码 1）；`md:111` 把章节"结尾"定位在副歌歌词「结尾那句"你在忘记我"…它会变成一句指控」 | `text/ch17_chapter_17.txt:372` `“Diana!” Carmen yelled.` → `:375` `“What?”` → `:378` `“Why don’t you get an air fryer like the one your sister has?”` | **末章最后一句（母亲对 Diana 的一句家常建议）在成品里零出现**；成品把收束位置交给了副歌的"指控"，把原文刻意的轻描淡写读成了"指控/悬疑" | **阻断** |
| M1b | `md:11`、`:153` 两处总结都收在"戴安娜…谜团正中间" | 同上 `:378` | 总结层没有把"轻收"写出来（收束＝笑声＋家常，不是悬念） | 并入 M1 |
| M2 | `bingo / Tortuga / 营地 / 阿姨` 各 0 命中 | `text/ch17_chapter_17.txt:216` `“The bingo lady and her friends. The women who played bingo at her camper.”`；`:234` `“Not very close, no. But they helped. Not just me—a lot of the women there. At least three others that summer alone.”`；`:255` `“They thought it was best to let them out, but they’d listen to your reasons… they’d tell you how to contain them—or if they were already partway out, how to get rid of them.”` | 母亲的营地口述**只收了"小尾巴/触手"半边**，"营地那批女人知道怎么收与除、那一夏至少还有三人"这层设定未收（本章最大的世界观翻面没进 md） | 提示 |
| M3 | `止痛 / 胶布 / 紧急门诊` 各 0 命中 | `text/ch17_chapter_17.txt:96` `…patching them up with gauze and tape, and she had even taken a painkiller—rare for her, since she avoided medication at all costs. But it hurt. She knew she’d have to go to urgent care tomorrow—Christmas—…` | 三个女人的身体状况里，**Alba 吃了止痛药（反常）、次日要去 urgent care** 未收 | 提示 |
| M4 | `电视 / 英寸 / 65 / 75` 各 0 命中 | `text/ch17_chapter_17.txt:75` `Carlos again looked away from the sixty-five-inch screen, thinking that number seemed too small, that it had to be more like seventy-five.`；`:186` `…watching a televised Christmas gala on the sixty-five-inch TV.` | 末章两个数字（65 寸实尺 / "其实更像 75 寸"）未收 | 提示 |
| M5 | `Santa / 圣诞老人` 各 0 命中 | `text/ch17_chapter_17.txt:57` `He explained that Santa might pass them by if he saw them playing in their bedroom so late.`；`:186` `…they came out every few minutes for snacks, or to ask when Santa would show up.` | "给孩子的圣诞夜掩护"这条日常线未收 | 提示 |

---

## 2. R3 单子二 · 编（md 有、原文无）

| # | md 侧 | text 侧 / 取证 | 判 | 档 |
|---|---|---|---|---|
| **C1** | `md:51` 读者视角提示：「想一下本章还有谁在轻描淡写——**阿尔巴在商场里说手柄"只是有点脏"**，那里的语气和这里正好相反。」 | 全书查无：`/usr/bin/grep -inE 'dirty' text/*.txt` → 仅 3 命中（`ch02:312` butt dirty / `ch08:192` get the car dirty / `ch08:207` "Dirty with what?"），退出码 0；原文里 Alba 只是在自家阳台**默默**擦手柄、没有任何台词：`text/ch17_chapter_17.txt:48` `She slid the Switch controllers out of her pocket, wiped them off with a towel lying nearby, and put them in the giant trash bag…` | 情节/台词凭空出现，且场景错了（商场→自家阳台） | **阻断** |
| **C2** | `md:75` 读者视角提示：「记住他没追问的那点犹豫——**那是下一章两个男人在车里抽烟时要说的话**。」 | 本书没有下一章：`ls text/` → 只有 `ch00_prologue.txt` … `ch17_chapter_17.txt`（18 个），md 侧同（`ch00`…`ch17`）。该场景实际在 `text/ch14_chapter_14.txt:156` `They left the car, and Juan lit a cigarette. Carlos asked for one.` | 指向不存在的"下一章"；末章不能外指 | **阻断** |

---

## 3. R3 单子三 · 错（两边都有但不一致）

| # | md 侧 | text 侧（逐字） | 判 | 档 |
|---|---|---|---|---|
| **W1** | `md:11`「…姐妹俩**才明白这不是错觉**…」；`md:153`「…**姐妹俩才明白那些东西是真的**…」 | `text/ch17_chapter_17.txt:201` `She still didn’t understand, but it didn’t really matter.`；`:228` `Now it was Alba who was confused, but instead of asking questions, she tried to steer the topic back in her favor.` | 两个女儿**都"明白了"**与原文相反：原文明确写 Diana "still didn't understand"、Alba "was confused" | **阻断** |
| **W2** | `md:153`「而戴安娜**也在同一刻发现**，自己一直站在谜团正中间」 | `:201`（Alba 提问 → Diana 领悟）早于 `:279`（母亲讲那一夏的营地口述） | 两个不同节拍被并成"同一刻"；且顺序被压平 | **阻断** |
| W3 | `md:11`「**三个浑身是血的女人分两趟回到阿尔巴家**」 | `text/ch17_chapter_17.txt:6` `they went to Alba’s apartment in two shifts. First Juan took Carlos and the kids. … Then, sometime after midnight, Juan went back to Splau for the women` | 分两趟的是**全体**；三个女人只在第二趟。主体错绑（`:21` 块内反而写对了） | 提示 |
| W4 | `md:21`「胡安先把卡洛斯和孩子们**送回家**」 | `:6` `they went to Alba’s apartment in two shifts. First Juan took Carlos and the kids.` | 目的地是 Alba 家的公寓，不是卡洛斯家 | 提示 |
| W5 | `md:57`「她住的公寓正好夹在中间，**离两个出口都不远**」 | `:48` `Her apartment was right in the middle, two exits away from each shopping center.` | `two exits` 是**距离**（离两个商场各两个出口），md 读成"两个出口（两扇门）都不远" | 提示 |
| W6 | `md:87`「还有两个女儿**同一分钟流鼻血**」 | `text/ch02_chapter_2.txt:468` `About a month ago, the girls’ noses had both bled dramatically, in different places and situations but at the same time.` | 事件有据（`:462` `Alba and Diana often got nosebleeds`），但"at the same time"≠"同一分钟"，且发生在"约一个月前"、跨章 | 提示 |
| W7 | `md:75`「卡洛斯是本章**唯一**觉得"不对"的成年人」 | `text/ch17_chapter_17.txt:183` `He thought it odd that Alba, who was still breastfeeding, wanted champagne.`；`:186` `they were trying—unsuccessfully—to process what had happened that night.` | Juan 同样在察觉/消化，越界解读 | 提示 |
| W8 | `md:39`「**真正的决定权始终握在三个女人手里**」 | `:33` `“All three of you should. The kids can’t see you like this. You can put all your clothes in the washer.”`；`:57` `Juan made them promise they’d come back out only when they had cleaned up.` | Juan 才是发号施令的一方（Alba 的 `“I’m not exhausted,” Alba said.` 是唯一一次顶回） | 提示 |
| W9 | `md:13`「完美靠谎话维持——藏血衣、藏耳朵、**藏疤、藏触手**」 | `:48`（手柄藏进垃圾袋）、`:33`（血衣进洗衣机）有据；但本章触手是**被说出口**的（`:282` `“It was a tentacle, Mom,” said Alba. “I had two.”`） | 只有按"对 Juan / Carlos 隐瞒"才成立；导航句未点明，易被读成"三人互相隐瞒" | 提示 |
| W10 | `md:109`「歌词里"**她已不在你身边**""你在忘记我"这两句」 | `text/ch17_chapter_17.txt:366` 引语只有 `“I long for you, you’re forgetting me.”` 等四句 | "她已不在你身边"不在引语内，是释义当引文 | 提示 |

---

## 4. R4 逐块对应（不看子项标题，只问"这段中文是不是在讲这句引语"）

| 块 | 引语（text 行） | 中文理解在讲这句引语？ | 为什么这样写 | 读者视角提示 | 结论 |
|---|---|---|---|---|---|
| 1 | `:6` no taxis / two shifts / pizza+heat | 基本在讲，但多讲了引语外的"深夜再折回商场接那三个女人" → **引语选短了** | 在（音量旋钮比喻） | 在 | 提示（B2/B4/W3） |
| 2 | `:33` Carmen 换衣 + 血鞋 | 多讲了引语外的"三个女人都得换 / 孩子不能看见" → **引语选短了** | 在（降格成家务） | 在，但"决定权始终握在三个女人手里"越界（W8） | 提示（B3/W8） |
| 3 | `:39` flayed ears / grabbing her wrist | **在** ✓ | 在（三步写尽一个丈夫） | 在，但"商场里说手柄只是有点脏"是编（C1） | **阻断**（C1） |
| 4 | `:48` billboards / right in the middle | **在** ✓ | 在（地理=凶案现场图） | 在（序章+第十二章同商圈，已核实为正确） | 提示（W5） |
| 5 | `:96` undone her ponytail / hair loose | **在** ✓ | 在（伪装是习惯） | 在，但"下一章"是编（C2）、"唯一觉得不对"越界（W7） | **阻断**（C2） |
| 6 | `:201` part of the mystery / same scar | **在** ✓（Alba 提问 → Diana 领悟，方向正确） | 在（转折点） | 在，"同一分钟流鼻血"措辞走样（W6） | 提示（W6） |
| 7 | `:279` tail / blood / horrific | **在** ✓（口述者＝母亲，方向正确） | 在（恐怖负责陪家人聊天） | 在，"第十一章、十二章"已核实为正确 | 通过 |
| 8 | `:366` chorus | 在讲这句引语 ✓，但 `md:111` 用"**结尾那句**"把章节收束位置钉在歌词上 | 在 | 在，但"指控"读法与原文末句冲突（M1） | **阻断**（M1） |

### 固定三问（施事 / 受事 / 归属方向）

| 块 | ① 动词主语 | ② 宾语/受事 | ③ 归属方向 | 与原文一致？ |
|---|---|---|---|---|
| 1 | "分两趟走"主语＝they（全体）；md 写"他们最后分两趟走" | "披萨+暖气让…发红又困"受事＝them（车里的人）；md 写"所有人" | "接那三个女人"＝Juan 接 | ✓（受事"所有人"偏宽 → W3） |
| 2 | Juan（商量的语气）；Carmen（脱鞋、扔垃圾桶） | those clothes / her blood-soaked sneakers | mother-in-law＝Carmen；three women＝Carmen+Alba+Diana | ✓ |
| 3 | Juan 捧脸、huff、摸头；Alba 抓手腕 | his wife's face / her flayed ears / her head | Alba 挡住 Juan 的手 | ✓ |
| 4 | "they'd changed the billboards"（无人称）；"Alba laughed and went back inside" | the two malls；her apartment | 公寓夹在 Finestrelles 与 Splau 中间 | ✓ |
| 5 | Carlos 察觉 → she（Alba）散开头发 | her ponytail / her ears | "so the kids wouldn't see her ears"＝Alba 的动机 | ✓（md:69 方向对） |
| 6 | She＝Diana；Alba 是提问者 | the same scar on her belly | "in due time, she would figure it out"＝Diana | ✓ |
| 7 | me＝Carmen（口述）；daughter 是听者 | her belly button / her legs | 母亲讲自己的那一夏 | ✓ |
| 8 | they＝母女三人 | the words | 副歌是三人共唱 | ✓ |

**三问结果：8/8 块施事方向与原文一致（未发现"施事/归属反转"型错误）；发现的是主语绑定、时序并置与结尾定位三类（S5 层），见 W1/W2/W3/M1。**

---

## 5. R5-补 · 取证命令（三件套：显式路径 / -E / 命令+输出+退出码）

工作目录：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/`（`text/` 被 .gitignore，**全程用 `/usr/bin/grep`，未用 git grep / rg**）

```
$ /usr/bin/grep -inE 'fryer' text/*.txt
text/ch17_chapter_17.txt:378:“Why don’t you get an air fryer like the one your sister has?”
→ 命中 1；退出码 0

$ /usr/bin/grep -inE 'fryer|空气炸锅|炸锅' "ch17 chapter 17.md"
（无输出）→ 命中 0；退出码 1

$ /usr/bin/grep -inE 'dirty' text/*.txt
text/ch02_chapter_2.txt:312:…so I wouldn’t get my butt dirty.
text/ch08_chapter_8.txt:192:…I didn’t want to get the car dirty.
text/ch08_chapter_8.txt:207:Dirty with what?
→ 命中 3，均与"手柄"无关；退出码 0

$ ls text/
ch00_prologue.txt … ch17_chapter_17.txt（共 18 个，无 ch18）→ 无"下一章"可对照

$ /usr/bin/grep -inE 'cigarette|smoking' text/*.txt
text/ch14_chapter_14.txt:156:They left the car, and Juan lit a cigarette. Carlos asked for one.
→ 命中（含 ch10:192）；退出码 0

$ /usr/bin/grep -inE 'bingo|La Tortuga|let them out|At least three' text/ch17_chapter_17.txt
text/ch17_chapter_17.txt:210 / :216 / :234 / :255 → 命中 4；退出码 0
$ /usr/bin/grep -cE 'bingo|Tortuga|营地|阿姨' "ch17 chapter 17.md"
0 / 0 / 0 / 0 → 退出码 1

$ /usr/bin/grep -inE 'painkiller|urgent care|gauze' text/ch17_chapter_17.txt
text/ch17_chapter_17.txt:96 → 命中 1；退出码 0
$ /usr/bin/grep -cE '止痛|胶布|紧急门诊' "ch17 chapter 17.md" → 0/0/0；退出码 1

$ /usr/bin/grep -inE 'sixty-five-inch|seventy-five' text/ch17_chapter_17.txt
text/ch17_chapter_17.txt:75 / :186 → 命中 2；退出码 0
$ /usr/bin/grep -cE '电视|英寸' "ch17 chapter 17.md" → 0/0；退出码 1

$ /usr/bin/grep -inE 'nose' text/*.txt
text/ch02_chapter_2.txt:357 / :462 / :468 → 命中 3；退出码 0

# 词汇 21 条例句逐字（Python，NFKC + 引号归一 + 空白归一）
vocab rows checked=21 verbatim_ok=21 miss=0
```

---

## 6. 修复指令（只出指令，不改稿）

1. **M1（阻断，末句）**：把 `text/ch17_chapter_17.txt:372–:378` 这一拍收进成品——不要新增第 9 个原句块（本书 `block_range=[5,8]`，本章已 8 块，加块即形态偏离），改为：① `md:111` 读者视角提示补上"本章真正的最后一句是母亲一句关于空气炸锅的家常话（`:378`），不是指控——整章用轻描淡写收尾"；② `md:11` 与 `md:153` 两处总结各加半句"末句是母亲一句关于空气炸锅的家常话"。
2. **C1（阻断，编）**：删 `md:51` 的"阿尔巴在商场里说手柄'只是有点脏'"。原文 `ch17:48` 是她在**自家阳台**默默用毛巾擦手柄、无台词；若要保留对照，改为"她回家路上在阳台把沾血的手柄默默擦干净放进藏礼物的垃圾袋"并改标点为原文没有的引语。
3. **C2（阻断，编）**：删 `md:75` 的"下一章"外指；改为"那是**本书后段**两个男人在车里抽烟时要说的话（ch14）"或直接删。
4. **W1/W2（阻断，错）**：`md:11` 与 `md:153` 的"姐妹俩才明白…"改成"Diana 明白自己也在这件事里、但母亲那一夏的讲法她还没听懂"；删"同一刻"，按原文顺序写"Alba 问 → Diana 明白自己身在事中（`:201`）→ 母亲讲那一夏（`:279`）"。
5. **M2–M5 / W3–W10（提示）**：按 §1、§3 表逐条补写或改措辞；`md:57` 的"离两个出口都不远"改为"离两个购物中心各两个出口"；`md:21` 的"送回家"改为"送去阿尔巴家的公寓"；`md:87` 的"同一分钟"改为"同一时刻（约一个月前）"；`md:11` 的"三个浑身是血的女人分两趟回到阿尔巴家"改为"分两趟回家：先送卡洛斯和孩子，再折回商场接三个女人"。
