# ch54 The Blizzard of 1979 —— R3 三张单（漏 / 编 / 错）

- 章 md：`notes/books/novels/life-out-of-order-by-audrey-niffenegger/ch54 the blizzard of 1979.md`（111 行，6 块）
- 原文：`notes/books/novels/life-out-of-order-by-audrey-niffenegger/text/ch54_the_blizzard_of_1979.txt`（364 行 / 2167 词）
- 机器层：`2-machine.json` verdict=ok，rc=0；6 块 6 引语全逐字（segment_miss=0 / empty_quote=0 / struct_bad=0）
- 判定口径：漏＝阻断，除非 md 导航或一句话总结写明该段取舍理由；编＝阻断；错＝阻断

## 一、漏（原文有、md 无）

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| **本章转折点（合奏施特劳斯 → 求婚）没有任何引语块承载**；导航只说「夜里合奏之后，他求婚」，一句话总结复述情节，两处均未写「为什么不立块」的取舍理由 | `text/ch54_the_blizzard_of_1979.txt:343` "It’s Richard Strauss’s Violin Sonata in E-flat Major, Opus 18."；`:356` "Strauss wrote this duet when he was first in love with Pauline de Ahna, the soprano who became his wife."；`:360` "“Will you marry me?” I ask."；`:364` "“Yes,” she says. “I will. Yes.”" | 转折点（她答应求婚＝本章情感落点）只以中文转述存在，无一处可回溯的逐字锚点；6 块中 6 块全落在前半章（雪、流程、街景、柜子、文件夹、发抖），末段 40 行（:326-364）零覆盖。块数 6 < 硬上限 10，不适用「块满降提示」 | **阻断** |
| 「A sonata. Make it difficult.」与「Are you asking for something you already know exists?」这对问答（本章全部张力的起点）未进任何块，仅由导航转述为「一首她将来写过、此刻还不存在的曲子」 | `text/ch54_the_blizzard_of_1979.txt:38` "“A sonata. Make it difficult.”"；`:42` "“You don’t want much,” I say. “Are you asking for something you already know exists?”" | 情节在导航里有交代，逐字不在；「make it difficult」这个定语全篇未出现 | 提示 |
| 壁橱里三个文件夹名（Chaos Monkey / Ravenswood Sonata / A History of the Weather）与「许多有名字的文件夹是空的」未提；原句 5 只留下「四摞 / 按年 / 马尼拉纸」 | `text/ch54_the_blizzard_of_1979.txt:231` "I smile at the familiar names. Chaos Monkey; Ravenswood Sonata; A History of the Weather. Many of the named files are empty." | 这三个名字是全书曲名的首次登记，漏掉后「Ravenswood Sonata」在后文的回响失去锚点 | 提示 |
| 取稿机制只写了一半：md 一句话总结说「他负责在对的日期把文件取出来」，漏掉「她把文件从壁橱门下塞回去」（自我隐藏的那一半） | `text/ch54_the_blizzard_of_1979.txt:263` "My task is to retrieve files from the cabinet on the right dates and leave them out for Alba. She slides them under the closet door when she wants to hide them from herself." | 机制是双向的（他取出／她塞回），单向叙述使「她为什么要躲自己」这一层消失 | 提示 |
| 超市购物清单（猪排、金枪鱼罐头、茶、米、冷冻玉米、冷冻披萨、两个苹果、黄油、植脂奶精、最后一盒鸡蛋）未列 | `text/ch54_the_blizzard_of_1979.txt:134` "We end up with pork chops, canned tuna fish, tea, rice, frozen corn, frozen pizza, two apples, butter and powdered nondairy creamer, ugh. Oliver finds the last carton of eggs sitting forlorn in the refrigerated section." | 清单是本章「过日子」的物证，但一句话总结已写「牛奶和面包都空了」，属可接受的压缩 | 跳过 |

## 二、编（原文无、md 有）

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 未发现 md 增添了原文没有的人、事、物或对话 | 逐块比对 6 块 + 导航 5 条 + 一句话总结，均可在 `text/ch54_the_blizzard_of_1979.txt` 找到对应（`/usr/bin/grep -nE` 见 4-verdict.md 的「已核实为正确」节） | 无编造 | 跳过 |

## 三、错（主语 / 受事 / 因果 / 数字 / 时序）

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 一句话总结把「不给提示」写成奥利弗的条件（「奥利弗要阿尔芭为他写一首奏鸣曲，还说不许给提示」）；原文里这是**阿尔芭自己**历来的严格规矩，奥利弗只是照办 | `text/ch54_the_blizzard_of_1979.txt:99` "“Are you allowed to give me any hints about this sonata I am writing for you?”"；`:104` "He laughs. “No, you have been strict about that. No hints.”" | 主语归属偏移：规矩的制定者是 Alba（"you have been strict"），md 读作 Oliver 提条件。人物性格指向相反（她的严格 vs 他的控制），但不改变事件 | 提示 |
| 「占位的女主人带着警察上门」中的「占位」修饰无误，但 md 未交代这条街坊规矩叫 dibs，而原句 4 的落点恰是 Dibs | `text/ch54_the_blizzard_of_1979.txt:281` "In Chicago, when it snows a lot and people have to shovel out their cars, they put things in the spaces so that other people don’t park there. The things aren’t valuable, but people get mad if you mess with their stuff. It’s called ‘dibs.’" | md 在读者视角提示里明说「这个词的意思要等别人来解释」，属有意留白，不算错 | 假红 |
| 时序：md 导航「回程在街上捡到」与实际相符（去程空手、回程推柜） | `text/ch54_the_blizzard_of_1979.txt:219` "We walk to the Yellow House, put the groceries away, retrieve the dolly from the basement, and go back to the parking space where our filing cabinet is patiently waiting for us." | 时序正确 | 跳过 |
| 数字：四抽屉 / 四摞 / 一百美元 / 1979 均与原文一致 | `:186` "four drawers tall"；`:231` "four piles of file folders"；`:297` "“One hundred dollars.”"；`:18` "Saturday, January 13, 1979, and Sunday, January 14, 1979 (Alba is 25, Oliver is 24)" | 数字无误 | 跳过 |

## 四、归属方向复核（by / to / from / of）

| 块 | 中文句 | 原文 | 方向判定 |
|---|---|---|---|
| 原句 1 | 「她出去铲门前小路时被它割得脸疼」 | `:28` "cut my face when I tried to shovel the front walk" | 施动＝雪，受事＝我的脸；md 用「被它割得」保持被动，正确 |
| 原句 2 | 「她躲进房间写，他送咖啡和吃的」 | `:121` "you hide in your room and write and I bring you coffee and food" | by＝Alba 写 / Oliver 送；md 的「他送咖啡」方向正确 |
| 原句 5 | 「她的乐谱被整齐地分成四摞文件夹」 | `:231` "Alba’s music is stacked neatly in four piles" | of＝Alba 的音乐；md 未错置成「他的」 |
| 原句 6 | 「他起身走过去，两只手搭在她肩上」 | `:356` "I stand up, go to her and put my hands on her shoulders. She is trembling." | 施动＝Oliver（I＝Oliver），受事＝Alba 的肩；md 正确 |
