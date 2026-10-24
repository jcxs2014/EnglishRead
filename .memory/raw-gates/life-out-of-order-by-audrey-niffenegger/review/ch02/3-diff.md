# ch02 对账（R3）

素读：`1-suread.json`（12 条，全部带 `text/ch02_random_driveway_winter_day.txt:行` + 逐字，脚本校验 12/12 命中本行）。
机器：`2-machine.json` rc=0；块数 10；引语 10 块 / 11 段全 ok（第 4 块两段拼接）；空引号 0；结构 0；`block_hint` 仍只是「块数 10 高于本书中位 6」。
md 155 行，10 块 + 5 条导航 + 词汇 17 条。

## 一、漏（素读有、md 无）

### 1. 【提示】时间旅行的规则整段未落（只在词汇里露半句）

- 原文 `text/ch02_random_driveway_winter_day.txt:119`（整段）：
  「My doctor calls it a bias—the past is easier, I have a much clearer idea of what things look like, of who might be there. **Time travel is like memory. It’s hard to remember forward**, though you might imagine a future that’s pretty close to reality. Sometimes I can use an object or a person as a destination, but other times I just end up in a random time.」
- md 侧：10 块无一块讲这段；5 条导航也未提「像记忆／偏过去／可用人或物当锚点」。只有词汇表 `md:151` 收了 `bias` 的例句（`My doctor calls it a bias—the past is easier…`），即机制只以「一个生词例句」的形式出现。
- 判断：这是本章唯一的机制说明段（也解释了她为什么落在随机车道），不进任何块或导航属实质缺失；但它是说明而非事件，**降为提示**，建议补一块。

### 2. 【提示】Nadia 追查链的人名与提示语全部未落

| 素读项 | 原文 | md 侧 |
|---|---|---|
| 谁下的任务 | `:447`「I have been tasked with this by **Isadora**, who was very insistent about it.」；`:457`「I see **Isadora Hardwick**, sitting in a booth in an empty virtual museum cafeteria」 | `grep -n "Isadora"` md → 0 命中 |
| 藏身处与接人者 | `:431`「I drove her to a house in **Miller Beach**…on **Forest Avenue**」；`:441`「That’s Nadia’s father, **David Kendrick**. The house is their vacation home.」 | `grep -nE "Miller\|Kendrick"` → 0 命中；md:89 只保留 `:457` 那句「我们会找很多年」 |
| 唯一线索 | `:526`「“**Flowers**,” I tell him. “Something about flowers.”」 | `grep -n "Flowers"` → 0 命中 |
| 与 Nick 同行 | `:431`「Nadia and Nick left Miller Beach together」 | 块 8 引语含 Nick，但中文只写「找 Nadia 和 Nick」 |

- 判断：主行动（托这家人追查 Nadia）已进导航 md:11，缺的是链条细节，判提示。

### 3. 【提示】遗传学/克隆那段世界观解释未落

- 原文 `:597`：「David has a whole lab working out the genetics, doing something with cloning. When Alba’s dad, Henry, died, research slowed for a while because **Clare wouldn’t let him use Alba as a test subject**, but once Alba turned eighteen she jumped back into the study.」
- 另 `:606` 政府压下时间旅行知识、Alba 裸奔视频从 YouTube 消失。
- md 侧：`grep -n "克隆"` = 0；导航与块内均无。属世界观补丁，判提示（可与第 1 条合并补一块）。

## 二、编（md 有、原文无）

无。逐条核过 md 的 5 条导航与 10 块中文，未发现原文没有的情节、关系或数字。

## 三、错（两边都有但不一致）

无硬错。两处措辞已核，判**成立**（不修）：

- md:11「她回 Mama 家借衣服」：原文 `:169`「filch one of Mama’s vintage winter coats」＋`:169`「I pick through the pile for underwear, tights, jeans and a sweater」——「借」是本意（她说过明天会还给自己），不是偷。
- md:41「她站在自己二十一岁的房门口」：2022 年 12 月她 21 岁（ch01 `:18` 抬头「Alba is 21」；本章 `:18` 抬头 2029 年 27 岁，中间生日落在 7 月底—12 月底之间，两个数字自洽），写法成立。

## 四、R4 逐块对应（10 块）

| 块 | 引语（text 行） | 是否在讲这句引语 | 三问要点 |
|---|---|---|---|
| 1 | `:23` 第三句起 | 是。宿醉、坐起、视野糊、往后倒、砸在冰水泥上 | 主语 I；落点＝icy cement，不是雪 |
| 2 | `:42` | 是。脱大衣—拉起—裹住—塞进车—开暖气—抢在垃圾车前开走 | 施事 Zach，受事 Alba；「没有商量的余地」＝`I let him` |
| 3 | `:169` | 是。乱房间＋床脚一叠干净衣服＋为「抑郁的年轻自己」羞耻 | 归属清楚：干净衣服是 Mama 放的 |
| 4 | `:224`（两段拼接） | 是。手套箱清单＋那封俄克拉何马公函 | 受事＝清单物件；「被解放的未成年人」＝`emancipated minor` |
| 5 | `:252` | 是。四个 delusion（破产/沙发客半年/不吃菜/不给母亲电话）＋不要施舍 | 说话人 Zach，听者 Alba；「他想约会的人」＝Alba |
| 6 | `:304` | 是。开门第一句「等了你一整周」＋接大衣＋抱＋握手＋让进厨房 | 施事 Charisse；「不问」＝原文确实没问 |
| 7 | `:421` | 是。两次握手＋瞟向写他名字的文件夹＋她皱眉 | 方向：他看文件夹、她否决，未反 |
| 8 | `:457` | 是。找很多年＋未来自己递碎片＋Nadia 被要求消失 | 「so brilliantly」译成「漂亮」保留双义 |
| 9 | `:533` | 是。Zach 视角：站起后仰、Gomez 扶、Charisse 像套索甩问题、人没了 | 施事多为旁人，「gone」是她的 |
| 10 | `:651` | 是。旧卧室清单（四缸鱼、鬣蜥 Maisie、打字机、书）＋「家的回声」 | 括号内＝从前，括号外＝现在 |

密度：10 块中文均 90–120 字，无一块只复述字面（块 9 对「lasso」「just like that」都有拆解）。
