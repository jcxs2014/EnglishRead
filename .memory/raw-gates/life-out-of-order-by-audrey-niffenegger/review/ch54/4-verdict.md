# ch54 The Blizzard of 1979 —— R5 判定

- 章：ch54（`text/ch54_the_blizzard_of_1979.txt`，364 行 / 2167 词；抬头 `:18` 1979-01-13/14，Alba 25、Oliver 24）
- md：`ch54 the blizzard of 1979.md`，111 行，**6 块**
- 机器层：`bash scripts/chapter.sh "<书 md>" --json` → **rc=0**，verdict=ok；6 引语 6 段全逐字；empty_quote=0；struct_bad=0；keyword_bad=0；cjk_low=0；block_target=[4,7]，实际 6，在区间内

## 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 转折点（合奏施特劳斯 → 求婚）无任何块承载；导航与一句话总结只复述情节，未写取舍理由 | `text/ch54_the_blizzard_of_1979.txt:343` "It’s Richard Strauss’s Violin Sonata in E-flat Major, Opus 18."；`:356` "Strauss wrote this duet when he was first in love with Pauline de Ahna, the soprano who became his wife."；`:360` "“Will you marry me?” I ask."；`:364` "“Yes,” she says. “I will. Yes.”" | 漏（转折点整段零逐字锚点；:326-364 共 39 行无覆盖；块数 6 未满上限 10，不适用块满降档） | **阻断** |
| 「A sonata. Make it difficult.」＋「Are you asking for something you already know exists?」未进块 | `:38` "“A sonata. Make it difficult.”"；`:42` "“Are you asking for something you already know exists?”" | 漏（情节在导航、逐字不在） | 提示 |
| 壁橱三个文件夹名（Chaos Monkey / Ravenswood Sonata / A History of the Weather）与「多为空」未提 | `:231` "I smile at the familiar names. Chaos Monkey; Ravenswood Sonata; A History of the Weather. Many of the named files are empty." | 漏（曲名首次登记处） | 提示 |
| 取稿机制只写「他取出」，漏「她塞回」 | `:263` "She slides them under the closet door when she wants to hide them from herself." | 漏（机制的另一半） | 提示 |
| 「奥利弗……还说不许给提示」——规矩制定者归属偏移 | `:99` "“Are you allowed to give me any hints about this sonata I am writing for you?”"；`:104` "He laughs. “No, you have been strict about that. No hints.”" | 错（主语：是 Alba 自己历来严格，非 Oliver 提条件） | 提示 |
| 超市清单未列（猪排/金枪鱼/茶/米/冷冻玉米/披萨/两苹果/黄油/植脂奶精/最后一盒鸡蛋） | `:134` "We end up with pork chops, canned tuna fish, tea, rice, frozen corn, frozen pizza, two apples, butter and powdered nondairy creamer, ugh. Oliver finds the last carton of eggs sitting forlorn in the refrigerated section." | 漏（一句话总结已写「牛奶和面包都空了」，属可接受压缩） | 跳过 |
| md 是否编造原文没有的人事 | 6 块 + 5 条导航 + 一句话总结逐条比对，全部可回溯（见下「已核实为正确」） | 无编 | 跳过 |
| `Dibs` 未在 md 解释 | `:281` "It’s called ‘dibs.’" | 读者视角提示已写明「这个词的意思要等别人来解释」，有意留白 | 假红 |
| 时序「回程捡柜」 | `:219` "we go back to the parking space where our filing cabinet is patiently waiting for us" | 正确 | 跳过 |
| 数字（四抽屉/四摞/一百美元/1979） | `:186` "four drawers tall"；`:231` "four piles"；`:297` "“One hundred dollars.”"；`:18` "Saturday, January 13, 1979, and Sunday, January 14, 1979" | 正确 | 跳过 |

## 报数（四组）

| 组 | 数 | 说明 |
|---|---|---|
| 逐字（引语 verbatim） | 6/6 ✅ | 机器层 segment_miss=0；另人工 `/usr/bin/grep -nE` 复核 6 条块首，全部命中（下方命令） |
| 对应（块 ↔ 所讲引语） | 6/6 ✅ | 逐块读中文，无一「讲这段、贴那句」 |
| 形态（结构/子项/块数/密度） | 6 块，子项四件齐（中文理解/关键词/为什么这样写/读者视角提示），导航 5 条，密度合法 | 通过 |
| 断言（中文层事实性） | 阻断 1 · 提示 3 · 假红 1 · 跳过 4 | 见判定表 |

## 判词

ch54 **1 阻断**。md 的六块把「雪 → 流程 → 街景 → 拾柜 → 文件夹 → 发抖」剪成一条干净的线，逐字全对、对应全对；但它停在发抖，没走到「Will you marry me?」。而本章正是靠合奏那首施特劳斯写给「后来的妻子」的奏鸣曲、才把求婚推出来的——那一层（曲子的来历 × 他的请求）整段没有块，只在一句话总结里以中文复述。修法：把 :343-364 立为原句 7（合奏 + 求婚两段或合为一块），并在导航的「一句话概括」里保留现有交代。

## 已核实为正确（防下一轮误修）

以下均经 `/usr/bin/grep -nE` 逐字命中（命令：`/usr/bin/grep -nE "It is snowing fast|Usually you hide in your room|Our frozen breath billows|I see it in my peripheral vision|Alba’s music is stacked neatly|When we stop, Alba stands" text/ch54_the_blizzard_of_1979.txt`，输出 6 行，**退出码 0**）：

- 原句 1 ＝ `:28` "It is snowing fast—nasty, icy, horizontal snow that cut my face when I tried to shovel the front walk."（md 只截到 "…into the blizzard."，截断处在句号上，合法）
- 原句 2 ＝ `:121` "“Usually you hide in your room and write and I bring you coffee and food and eventually you come out and ask me to play what you’ve written and then you tell me I am playing it wrong and then you disappear into your room again.”"
- 原句 3 ＝ `:134` "Our frozen breath billows and wafts before us. The city hasn’t plowed the streets; cars are stranded in strange places and hidden under mounds of snow—even the trains don’t seem to be running. Chicago is silent except for the sounds of shovels scraping sidewalks."
- 原句 4 ＝ `:186` "I see it in my peripheral vision: the filing cabinet is sturdy, four drawers tall, painted a rather military shade of green with brass handles. It is standing in a parking space with some broken chairs and a few plastic egg crates. Dibs."
- 原句 5 ＝ `:231` "Alba’s music is stacked neatly in four piles of file folders, anticipating the four drawers of the cabinet. The files are in chronological order. In the future they will be color-coded, though the age of decorative office supplies hasn’t yet begun, so all the files are manila now."
- 原句 6 ＝ `:356` "When we stop, Alba stands with her eyes closed for a moment, then lowers her violin. I stand up, go to her and put my hands on her shoulders. She is trembling."（叙述者＝Oliver，故中文「他起身」正确）

词汇例句（8 条，`/usr/bin/grep -nE` 各命中，rc=0）：`horizontal` :28；`spontaneously` :71；`inevitable` :134；`displacement` :257；`blizzard` :28；`unwelcome` :50；`anticipating` :231；`abruptly` :175；`satisfyingly` :356；`dolly` :199；`violin` :338；`cart` :146；`checkout` :175。

- 「她拿缪斯要不要脱光打趣，他真摆出一个姿势」（md:13）＝ `:76` "“If you’re my muse, maybe you could stand around naked?”" ＋ `:80` "Oliver strikes a cheesecake pose" → **正确**，非编造。
- 「自称是她的外置硬盘」（md:14）＝ `:248` "“Never,” I say. “It’s all in my head. I’m your external hard drive.”"（说者＝Oliver）→ **正确**。
- 「她夜里说要写快一点」（md:12）＝ `:320` "“It was so strange seeing all the files at once,” Alba says. “I have to write faster.”" → **正确**。
- 「占位的女主人带着警察上门，一百美元了事」＝ `:273` "That was the woman who owned the filing cabinet. She brought a policeman with her." ＋ `:297` "One hundred dollars." → **正确**。
