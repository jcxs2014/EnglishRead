# ch09 No Place Like Home — 判定（R5）

- 机器层：`bash scripts/chapter.sh "…/ch09 no place like home.md" --json` → **rc=0**，verdict=ok，块数 6、words 1818、segments 8、查无 0、空引号 0、子项缺 0、关键词缺 0、形态偏离 0，`issues` 全空。
- 素读锚点：8/8 命中。
- 报数：**逐字 0 / 对应 0 / 形态 0 / 断言 0 阻断、5 提示 + 1 形态提示**——漏 3、编 0、错 2。

## 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 漏：Zach 整段「为何不告家人」独白无块，且「不是羞于你」「让他们知道我还活着」「Tulsa」「改了姓」在 md 中零命中 | `text/ch09_no_place_like_home.txt:42` “I mean, I’m not ashamed of you. Quite the opposite. I’ve screwed this up.”；`:34` “I let them know I’m alive every now and then. Anything more than that would just encourage them.”；`:43` “how we’d get them up here from Tulsa safely… my parents don’t even know I changed my name.” | 导航 :14 只列 5 条理由；`grep -nF "ashamed"/"Tulsa"/"changed my name"` 三次退出码 1、零输出。定性句缺失 | 提示 |
| 漏：婚礼当天全员戴口罩（疫情又起）＋到场名单（Miriam、Kendrick 一家、互助组织朋友）＋缺席者（Nadia、Nick、Kimy、祖父）全无 | `:62` “We are all wearing masks because the pandemic is surging again.”；`:62` “Caralora and her date, Miriam; Celia and Lucinda”；`:63` “David and Nancy Kendrick, with their son, Colin.”；`:63` “How I miss Nadia today, and Nick, too. I wish Kimy and my grandfather could be here.” | `grep -nF "口罩"/"Miriam"/"Kendrick"/"Nadia"` 四者皆零命中（退出码 1）。疫情这层外部背景在本章无锚点 | 提示 |
| 漏：「梯形阳光里持琴、第一次像属于这所房子」与「拿他当压舱物」 | `:103` “I saw Alba standing in a trapezoidal band of sunlight, her eyes closed, arms outstretched, her violin in one hand, bow in the other… For the first time, Alba seemed to belong in the house”；`:108` “Alba held my hand almost continuously, as though she were using me as ballast.” | `grep -nF "阳光"/"小提琴"/"压舱"` 三者皆零命中（退出码 1）；「home」主题的实证只在导航 :14 的「看后门」一句上 | 提示 |
| 错：md :13「最显眼的一件家具是前任房主去世的**那张床**，被扔掉了」 | `:131` “Alba insisted that we throw out Beatrice’s **mattress**”；同段 “we are left with all her Heywood-Wakefield furniture” | 扔的是床垫（:11 写对，:13 滑成「床」）；「最显眼的一件家具」与原文相反——留下的几乎全是她的家具 | 提示 |
| 错：md :14「Alba 在这一章几乎没有推动任何事，她做的动作只有等」 | `:29` “A few weeks before the wedding **I asked him**…?”；`:57` “**I let my mother and Beck take me shopping**”；`:131` “**Alba insisted** that we throw out Beatrice’s mattress” | 至少三次主动发起；同段末尾又承认两件，前后略打架 | 提示 |
| 形态：6 块 / 1818 words，`block_target [3,6]` 已到上限 | `2-machine.json`：`block_range [3,10]`、`block_count` 无 issue | 块数在本书常见区间内，但中段（Zach 独白、名单、阳光持琴）三处只能靠导航，说明块的选取偏「婚礼仪式＋首尾」 | 提示（结构观察，非缺陷） |
| 11 条词汇例句 | 脚本整串比对：`rows=11 miss=0` | 逐字无误、未跨章 | 假红（核后成立） |
| 抬头 `Alba is 23, Zach is 24` | `:18` “Saturday, August 2, 2025 (Alba is 23, Zach is 24)” | 原书原文；md 未写年龄，不与 ch06 的 42 相涉 | 假红（按派工方口径延伸） |

## 处置建议（只报不改）

1. 导航 :14 补一句定性：「他说自己不是羞于示人，是把这事搞砸了；他只让家里偶尔知道他还活着」。
2. 导航 :11 补六个字级信息：「全员戴口罩」「到场二十来人」；如篇幅允许，加一句「她站在一道梯形阳光里拉琴，第一次像属于这所房子」。
3. `:13` 改「床」→「床垫」，删「最显眼的一件家具」（改「留下的家具几乎全是她的」）。

## 已核实为正确

- **Clare 即 Mama**：`:99` “a wedding present from **Clare and Beck**”；md :11 用「Clare 和 Beck」，与正文他处的「Mama」不矛盾。
- **年龄线**：`:18` “(Alba is 23, Zach is 24)”，与 ch07（22/23）、ch08（23/23）自洽；md 未写年龄，未与 ch06 的 `Alba is 42` 冲突。
- **九十六岁**：`:99` “at the age of ninety-six”；md「九十六岁」正确。
- **戒指方向**：`:82` “Zach slides a wedding band onto my finger, then I slip his ring onto his finger.”；md :41 两个方向都对，未互换。
- **11 条词汇**：全部落本章（`miss=0`），`inconspicuous`／`ordained`／`split-level`／`coral lipstick` 例句均为原句。
- **曲名**：`:73` “A Kiss to Build a Dream On”、`:82` “You’re the Cream in My Coffee”、`:89` “Pet Sounds”／“Wouldn’t It Be Nice”；md 引用的三处均无误（`Cream in My Coffee` md 未引，不算漏——本章未选它作块）。
- **门槛迷信方向**：`:118` “for fear of **demons getting in**”；md :65「恶魔要防的方向：门里」与原文一致。
- **「we are home」非对白**：`:149` 为叙述句；md :71 处理为「收在一句陈述上」，未加引号。
- **标题俗语出自 Alba 之口**：`:144` “‘There’s no place like home.’” 是她的台词（对着他的新纹身说的）；md :13/:15/:77 三处表述一致，未误标为叙述者结论。
