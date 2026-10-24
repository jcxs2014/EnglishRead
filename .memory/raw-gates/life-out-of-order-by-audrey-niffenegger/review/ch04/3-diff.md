# ch04 对账（R3）

素读：`1-suread.json`（13 条，全部 `text/ch04_in_spring_a_young_man_s_fancy_lightly_tu.txt:行` + 逐字，脚本校验 13/13）。
机器：`2-machine.json` rc=0；块数 10；引语 10 段全 ok；空引号 0；结构 0；关键词全中；`block_hint`「块数 10 偏离本书 3–9」——本书 71 章中位 6、最高 10，并列最高，不判红。
md 155 行，10 块 + 5 条导航 + 词汇 22 条。
块→原文行：1 `:23`、2 `:28`、3 `:34`、4 `:108`、5 `:108`（同一长段内两处，非重复）、6 `:128`、7 `:199`、8 `:287`、9 `:328`、10 `:418`。

## 一、漏（素读有、md 无）

### 1. 【阻断】Lucinda 与 Isadora 的整段来历全缺

本章词数 3132，其中约 1/5（`:302`–`:399`）就是这场对话：Clare 临走想起「Isadora！Lucinda 大概正坐在我们家门口」，随后 Zach 追问「谁是 Lucinda 和 Isadora」，Alba 逐一定义。md 里 `grep -nE "Isadora|Lucinda"` 只命中 `md:151` 一行词汇表（`anti-darling` 的例句），叙事层零字。

- 原文 `:302`：「“Mama, it’s almost three o’clock,” and Clare says, “Is it? Oh, my gosh, **Isadora! Lucinda’s probably sitting on our doorstep**.”」
- 原文 `:361`：「“**Lucinda is my mom’s friend Celia Attley’s daughter. Foster daughter.** You saw her once, at the party, the night we met. She was asleep on the bed, in that room upstairs.”」
- 原文 `:370`：「“**She’s the baby of the whole group of us. She’s our darling.**”」
- 原文 `:378`：「“**Isadora is the anti-darling. We’re all terrified of her.**”」
- 原文 `:386`：「“You might say she’s my stepsister. **She’s Beck’s daughter.** I’m going to do my best to make sure you never meet her, because she gets wildly jealous of me and wants everything I have and anyone I date. **She had a serious fixation on Caralora.** It was scary and stalkerish.”」
- 原文 `:397`：「“They love each other. They were made for each other, they’re inseparable… They spend every Saturday afternoon together, at our place.”」
- md 侧：导航五条无一字；块 10 之后直接进词汇表。md 也未写取舍理由。
- 判断：这是本章唯一的新人物登记处（一个「心头肉」、一个「反心头肉」，后者还是 Beck 的女儿、盯过 Caralora），后续章节要用到；整段未进任何块或导航 ⇒ 阻断。

### 2. 【提示】Zach 的新车（2012 银色 Jetta）与「想起 Nash 就失落」未落

- 原文 `:413`：「**It’s a very ordinary, not-attention-attracting 2012 silver Jetta**, and every time I see it I think of my lost Nash and feel bereft.」
- md：`grep -nE "Jetta|银色"` = 0；md:12 只写「两人开车向东」。
- 判断：上一章 Nash 被烧，这一章换了代步工具且点明「不起眼」——正是他躲人的处境；属细节遗漏，提示。

### 3. 【提示】Clare 的外貌整段未落

- 原文 `:34`：「She’s a little shorter than Alba, and more curvaceous; she has a heart-shaped, Pre-Raphaelite face, **waist-length red hair, coppery and streaked with white**, and her enormous eyes are **pale gray, like Alba’s**. She’s wearing a mint-green knit dress… Her skin is surprisingly rough.」
- md：`grep -nE "红发|头发|Pre-Raphaelite|灰眼"` 全 0——她是全书第一次正面出场，外貌（尤其「和 Alba 一样的浅灰眼睛」）被整段跳过。
- 判断：提示。

### 4. 【提示】抬头里的年龄（Alba 23 / Zach 22 / Clare 51）未抄

- 原文 `:18`：「Saturday, April 15, 2023 (**Alba is 23, Zach is 22, Clare is 51**)」；md:11 只写日期。
- 为什么值得提：Alba 的 23 本身就是伏笔（正主 2023 年应 21 岁，23 是 2025 年的她），md 靠对白把伏笔讲清了，但整行年龄被略去；提示（非阻断）。

## 二、编（md 有、原文无）

无。逐条核过：见「已核实为正确」。

## 三、错（两边都有但不一致）

无。三处易错点复核后均成立：

- md:11「Clare 先关掉手机才起身」＝`:34`「hurriedly **shuts off** her phone and rises」——是关机，不是收起来；md 还专门点出「不是收起」。
- md:11「二十岁才在 Newberry 图书馆正式「第一次」见他」＝`:108`「By then I was twenty, and he was twenty-eight… He was a librarian at the Newberry Library」。
- md:13「二十岁的她在图书馆才见到那个「第一次」见她的人」＝`:108`「That was when Henry met me for the first time.」——方向没反。

## 四、R4 逐块对应（10 块）

| 块 | 引语（text 行） | 是不是在讲这句引语 | 三问要点 |
|---|---|---|---|
| 1 | `:23` | 是。连日反常暖＋花瓣提前落＋Alba 骂夏天＋「四月中旬天天八十度很邪门」 | 主语：天气/Alba/Zach；eerie 的判给人是 Zach |
| 2 | `:28` | 是。过街进小广场、干喷泉、空演奏台、光剑小女孩撞人、父亲回头道歉 | 施事＝孩子，受事＝Zach；md 未把道歉者写成母亲 |
| 3 | `:34` | 是。领位穿过满座餐厅→角落桌→中年女人慌忙关机起身→笑里带提防 | 「她」＝Clare；关的是手机电源 |
| 4 | `:108` 前段 | 是。六岁、密歇根乡下屋后草地、高草里藏着一个裸体的人、她停住 | 说话人 Clare，听者 Zach；「他」＝Henry |
| 5 | `:108` 后段 | 是。借沙滩巾→他说明规则（什么都带不来）→要她备衣放草地→不断出现→她 20 他 28 | 受事＝衣服；「保管衣物」是她的任务，方向未反 |
| 6 | `:128` | 是。我们本来会选对方、一天一刻在选、爱过也被爱过、他死后很长一段不是自己 | 说话人 Clare；「wasn't myself」译「不是原来的自己」保住了含糊 |
| 7 | `:199` | 是。Alba 离席→Clare 递事先写好的号码→「任何紧急情况，尤其需要解释很久的」 | 施事 Clare，受事 Zach；「written out beforehand」是重点 |
| 8 | `:287` | 是。还担心 Henry、「你大概以为他不需要了」、希望不必担心 Zach、你是稳住局面的那种人 | 说话人 Clare；「steady people」既肯定又被听成「无聊」 |
| 9 | `:328` | 是。另一个她在 1980 年代陪父亲、这个来自 2025 年 7 月、互相替班、不想放你鸽子 | 两个「她」指代清楚：在场者／正主 |
| 10 | `:418` | 是。Lake Shore Drive 放窗、Bowie《Heroes》、黑发乱飞、墨镜后表情不明、未来可能辉煌 | 主语 I＝Zach；「despite the abnormal weather」的让步关系保留 |

密度：10 块「中文理解」45–110 字、「为什么这样写」100–130 字，均扣句内字词（disconcertingly/eerie、written out beforehand、wasn't myself、steady），没有一块转去讲全书主旨。
