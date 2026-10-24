# ch24 深审 R3 三张单子（漏 / 编 / 错）

> 章：`text/ch24_chapter_24.txt` ↔ `ch24 two dresses and a carriage.md`
> 流程：R1 素读（`1-suread.json`，178 条证据片段全部为原文子串，`BAD=0`）→ R2 机器 → R3 本文件 → R4 逐块对应（§四）→ R5 判定（见 `4-verdict.md`）

---

## 〇、结构底账

| # | 事实 | 证据（`text/ch24_chapter_24.txt`） |
|---|---|---|
| 1 | 正文体范围 `:35`–`:258`（`:258` `I’m coming, Helena.` 为最后一句） | `:35` `Cynthia sank onto her bed…` |
| 2 | **双半单视角**：前半贴辛西娅 `:35`–`:134`，后半贴海伦娜 `:150`–`:258`，各自限知 | 通读；`:35` 起无海伦娜内感知，`:150` 起无辛西娅内感知 |
| 3 | 换场空白带 `:135`–`:149`（15 行空白） | 逐行核：`:134` 末句 `…from the Devil of Seven Dials.` → `:150` `Helena was dying.` |
| 4 | 推广／版权残留行 0 条 | `/usr/bin/grep -ci lokepub` → `0`，rc=1（§六 A） |
| 5 | 场一＝**辛西娅自己的卧室／更衣室**（地图上仍是“我的家，至少还两天”） | `:50` `This is my home… for two more days, at least.`；`:86` `Cynthia’s empty dressing room` |
| 6 | 场二＝**五铃街土耳其浴场的干热桑拿房** | `:150` `the hellish room`；ch25 `:35` `5 Bell Street`／`:92` `The final sauna…cedar-planked interior` |
| 7 | 时间锚：舞会只剩一天；她**次日早晨**去乡间庄园、不打算再回伦敦 | `:35` `The duchess’s ball was only a day away. She left for her country manor the morning after and had no plans to return to London.` |
| 8 | 科茨沃尔德＝她将独居之地 | `:41` `If she were destined to live alone in the wilds of the Cotswolds…` |
| 9 | 埃莉带来的讯息：辛克莱抓了海伦娜；罗温随拉克兰去了巴斯 | `:59`／`:65`／`:71` `She went to Bath with Uncle Lachlan.` |
| 10 | 幻象内容：两人并肩面对辛克莱＋一处大水池；室内、白石与彩砖 | `:77`／`:101` |
| 11 | 五铃街：几个月后开张、设计师 Roger Evans、面向劳动者、只收一先令 | `:104` |
| 12 | 两条裙子：旅行装＋爵夫人当天送来的舞会礼服；埃莉称礼服“绝不是哀悼服” | `:86`／`:89`（全书 ch24 仅此一处 `mourning`） |
| 13 | 辛克莱着装：脱去外套与马甲，只剩亚麻衬衫与马裤 | `:183` `He wore only a linen shirt and breeches.` |
| 14 | 巨人：低头进门、卷发、身躯庞大；海伦娜联想到 Benandonner 与罗温的睡前故事 | `:213` |
| 15 | 辛克莱只说“我要的东西”，**未说是什么**；他索要的期限＝回来后 | `:243` `you will give me what I seek` |
| 16 | 无引号心声 3 处：`:162`、`:177`、`:225`；章末 `:258` 同样无引号 | `:162` `She’ll never know how much I love her.`／`:177` 祈祷／`:225` `Hamlet!`／`:258` `I’m coming, Helena.` |
| 17 | 有引号台词全用单弯 `‘…’`；最暴烈一段在 `:207` | 逐行核 |
| 18 | md：13 块（`md:17/27/37/47/57/67/77/87/97/107/117/127/137`）、词表 24 行 9/9/6、导航 5 项 | `2-machine.json`：`blocks=13`、`block_target=[4,7]`、`words=2302`、**`block_hint`＝「块数 13 偏离本章篇幅建议 4–7（本章 2302 词）」**、`segments=18`、`segment_miss=0`、`issues` 全空 |

---

## 一、漏

| # | 原文事实 | md 现状 | 判定 |
|---|---|---|---|
| L1 | `:156` `Surely her aunt and cousins would avenge her. They would ensure Damien Sinclair paid for killing one of their coven` | md:10 只写“她一一想到不能再见的人与事”，未记复仇念头 | 提示 |
| L2 | `:213` 巨人形象借 Benandonner 神话，且是 **罗温讲给女孩们哄睡的童年故事** | md:10/190 只写“巨人低头进门” | 提示 |
| L3 | `:252` `While she had no tears to shed, her soul bled as freely as her wrists.` | 无 | 提示 |
| L4 | `:192` 探向体内 `finding nothing but dust`（与 ch23 的 “mist and memory”、ch24 `:150` 的 “seeped out” 构成三阶段） | md:73 只写“往外渗”，未记“只剩灰” | 提示 |

---

## 二、编

**本节无新增凭空人物／地点／事件。** md 与原文冲突的两处——“箱子飞起来”与“雪松与尤加利”——记在 §三。

**成立取证表（md 事实主张逐条回原文）**

| md 主张 | 原文 |
|---|---|
| 前半打包完毕、舞会只剩一天、次日去乡间、不再回伦敦 | `:35` |
| 佛手柑茶“要了却不喝” | `:35` `the tea she asked for and would not drink` |
| 手帕绣蜜蜂与樱花、从箱中取出 | `:38` `the white linen embroidered with bees buzzing over cherry blossoms` |
| 埃莉连睡裙都没换 | `:56` `clearly a nightgown` |
| 妖风把男仆推出、门被顶死 | `:47` |
| 埃莉说辛克莱抓了海伦娜 | `:65` |
| 罗温随拉克兰去巴斯 | `:71` |
| 幻象：两人并肩面对辛克莱＋大水池 | `:77` |
| 水池在室内、白石与彩砖、都柏林土耳其浴室 | `:101` |
| 五铃街：几个月后开张、Roger Evans、面向劳动者、一先令 | `:104` |
| 白鼬奥菲莉亚跳上颈子打转、她当作证实 | `:107`／`:110` |
| “我会把哈姆雷特安全带回来” | `:110` |
| 只穿衬裙、不穿长袜 | `:80` `threw on a chemise`／`:116` `not bothering with stockings` |
| 让埃莉通知克莱奥与托马斯、苏格兰场带人 | `:116` |
| “你看见的是我们一起面对辛克莱，我没时间可浪费” | `:122` |
| 三个贬义形容词 stubborn／infuriating／ridiculous | `:128` ✔（恰 3 个） |
| 上车后放话“等你被我救出来，我们要谈谈你对爱情的误解” | `:131` |
| “灵魂伴侣”“七铃区的魔鬼” | `:134` |
| 海伦娜力量外渗、视线对不上焦、不知被锁多久 | `:150` |
| 庆幸腕上是皮带不是金属、铁链会烫焦皮肉 | `:153` |
| 罗温与表亲会替她复仇 | `:156` |
| 淡褐色眼睛（hazel） | `:159` |
| 心语“她永远不会知道我有多爱她” | `:162` |
| 三个“尽管”（誓言／恐惧／疮痍） | `:165` ✔ |
| 母亲对铁匠＝绝望的欲求；他的回报＝中毒般的占有 | `:168` |
| “那不是爱”（That wasn’t love.） | `:168` 首句 |
| 叙述者短评“直到永远够不着才懂爱” | `:171` |
| 灵交织、织在时间开始之前的锦缎里 | `:174` |
| 祈祷：愿灵留下、守着爱人直到寿终 | `:177` |
| 冷风涌入、辛克莱只穿衬衫与马裤、额上冒汗 | `:180`／`:183` |
| 她骂“魔鬼的杂种” | `:198` |
| “或许我该去问问她”（暴露他知道辛西娅） | `:201` |
| 威胁：肺从喉咙扯出、尖叫磨成匕首、心切千块 | `:207` |
| 血里最后一丝魔法让声音带回响 | `:207` |
| 巨人报信“是那只狐狸” | `:222` |
| “暂时没事，接下来怎样全看你” | `:231` |
| “等我回来你要给我我要的东西” | `:243` |
| 门关后通风口灌热；若哈姆雷特遇险她不能先死 | `:246` |
| 用体重挣皮带、血流无用 | `:249` |
| 求女神别抛下她、女神沉默 | `:252` |
| 章末“另一个声音…如夏风”＋`I’m coming, Helena.` | `:255`／`:258` |
| “十五行空白” | `:135`–`:149` 恰 15 行 ✔ |
| “第一句只有三个词”（Helena was dying.） | `:150` ✔ |
| “时态用过去完成”（had fallen） | `:165` ✔ |
| Roger Evans 全章只出现 1 次 | §六 C：`grep -o` → `1` ✔ |

---

## 三、错

| # | md 位置 | md 说法 | 反证 | 判据 | 判定 |
|---|---|---|---|---|---|
| E1 | `md:19` | 原句 1 的中文理解：“……**箱子**升到空中，像幽灵一样飞过昏暗的房间，轻轻落在她膝上。” | `:38` 的 `It` 指**手帕**：`Her handkerchief was folded neatly in the chest… Cynthia imagined the chest opening… she carefully pictured the white linen… It rose into the air…`；md:10 自己也写“把…白手帕用意念取了出来”、md:23 也写“手帕像幽灵一样飞过来” | 受事写错，且与同 md 另两处自相矛盾 | **阻断** |
| E2 | `md:14` | “全章反复用气味做记号：佛手柑…、烧焦糖与鼠尾草…、**雪松与尤加利**” | ch24 全书 `grep -i "cedar\|eucalyptus"` → **0 命中，rc=1**；雪松与尤加利只在 ch23 `:198` | 引语外新增本章不存在的情境事实（跨章串味） | **阻断（轻）** |
| E3 | `md:184`＋`md:186` | 词表 `vent` 例句＝`She desperately grasped at the last hint of fresh air…`；`nightgown` 例句＝`Cynthia threw on a chemise…` | 两句都**不含词头**：`vent` 在 `:246` 前一句（`a rush of scalding heat from a vent above her head`）；`nightgown` 在 `:56`（`clearly a nightgown`）。例句实际讲的是 fresh air 与 chemise/corset | S4 词表（例句不illustrate 词头；`check_vocab` v5 只堵“例句=词头”，不堵“词头缺席”） | **阻断（轻）** |
| E4 | `md:10` | “辛克莱…**嘲笑她抬出地狱与埃及沙漠**都比不过这间屋子” | `:195` 是**辛克莱自己**在形容房间：`I’m sure you’re wondering why I have you here in a room that is hotter than hell and more arid than an Egyptian desert.`——海伦娜并未提地狱或埃及 | 施事归属反了 | 提示 |
| E5 | `md:10` | “辛克莱只穿衬衫**短裤**” | `:183` `breeches`＝**马裤**（md:182 词表自己也写“马裤，及膝裤”），不是短裤 | 与本章词表自相矛盾 | 提示 |
| E6 | `md:12` | “辛西娅却把它读成**自己必须单独到场**，把预言实现的方式由‘并肩’改成‘我先去’” | `:122` 她明说 `Helena and I face Sinclair together.`——她并没有把幻象读成“单独到场”，只是让埃莉去搬兵、自己先赶路（md:65 的表述才是对的） | 分析层把行动策略误写成对幻象的解读 | 提示 |
| E7 | `md:33` | “实际上**整章后半证明**这个‘附近’是**同处一室**” | 本章后半海伦娜在桑拿房，辛西娅还在卧室／马车上（`:150`–`:258` 无辛西娅到场）；“同处一室”要到 ch25 才发生 | 跨半章事实提前 | 提示 |
| E8 | `md:13` | “她唯一没松口的是‘我不该被爱’，所以**承认之后仍是求死**” | `:246` 她已改口：`If Hamlet was in danger, she couldn’t die without first saving him.`；`:252` 又求 `Don’t abandon me, goddess. Not now.`——与 md:10 的“她不能先死”自相矛盾 | 弧线收尾写反（只覆盖 `:171`–`:177` 一段） | 提示 |
| E9 | `md:13` | “**辛克莱第一次**单独与海伦娜共处一室” | ch23 `:122` 店已打烊、店内只有海伦娜与哈姆雷特，辛克莱进店后两人独处对话（`:125`–`:164`）——那才是第一次 | (j) 跨章“第一次”未取证 | 提示 |
| E10 | `md:14` | “**前半全知**贴辛西娅” | 前半是**第三人称限知**：只给辛西娅能看到／想到的（`:41` 的假设念头、`:101` 埃莉的描述、`:128` 她的自责）；全知叙述者不会受此限制 | 叙事学术语用错 | 提示 |
| E11 | `md:45` | “这一章**两次**把‘哀悼的规矩’摆上台面” | 全章 `mourning` 只出现 1 次：`:89` `That is certainly not a mourning gown.` | (f) 计数断言无据 | 提示 |
| E12 | `md:83` | “**四个‘再也’**从视觉排到味觉、触觉” | 原文 `:159` 只有 3 个 `never`（`never see`／`Never watch`／`never kiss`）；md:79 的中译也只有 3 个“再也” | (f) 计数断言 | 提示 |
| E13 | `md:83` | “**全章第一次**直接给出这个字” | `love` 在本章更早已出现：`:35` `doomed love`、`:131` `misguided notions on love`、`:165` `the devastation love left` | (i) 唯一性断言有同章反证 | 提示 |
| E14 | `md:93` | “把上一章那句‘我错了’的时间点**往前推回辛西娅还在的那个夜里**” | ch23 全章辛西娅**不在场**（她在 ch22 已离场），`I’m wrong.` 发生在店里打烊后的盘点夜；过去完成 `had fallen` 只能说明“坠入”早于“承认”，不能推出“辛西娅还在的那个夜里” | 跨章时间点无据 | 提示 |
| E15 | `md:190` | “（辛克莱）**问她为何不是那副凶狠口气**” | `:189` `Hardly the tone to take with a man who holds your life in his hands`＝“这可不是跟握着你性命的人说话该有的口气”——他嫌她**太凶**，不是问她为何不凶 | 语义方向反 | 提示 |

---

### 说话人与引号链底账（R4 归属核对用）

前半：`:35` 叙述 → `:47` 埃莉 → `:50` 辛西娅 → `:59` 埃莉 → `:62` 辛西娅 → `:65` 埃莉 → `:68` 辛西娅 → `:71` 埃莉 → `:74` 辛西娅 → `:77` 埃莉 → `:83` 辛西娅 → `:89` 埃莉 → `:92` 辛西娅 → `:95` 埃莉 → `:98` 辛西娅 → `:101` 埃莉 → `:104` 辛西娅 → `:110` 辛西娅 → `:116` 辛西娅 → `:119` 埃莉 → `:122` 辛西娅 → `:125` 辛西娅 → `:128` 叙述 → `:131` 辛西娅 → `:134` 叙述。
后半：`:150` 叙述／海伦娜内感知 → `:162` 海伦娜（心语）→ `:165`–`:177` 叙述＋海伦娜（祈祷，无引号）→ `:186` 海伦娜 → `:189` 辛克莱 → `:192` 叙述 → `:195` 辛克莱 → `:198` 海伦娜 → `:201` 辛克莱 → `:207` 海伦娜 → `:213` 叙述 → `:216` 巨人 → `:219` 辛克莱 → `:222` 巨人 → `:225` 海伦娜（心语）→ `:228` 海伦娜 → `:231` 辛克莱 → `:234` 巨人 → `:237` 辛克莱 → `:243` 辛克莱 → `:249`–`:252` 海伦娜（祈祷）→ `:255`–`:258` 另一声音。

⇒ md 的 13 块说话人**零错**；`md:135` 明确说辛克莱“只在这一句暴露他知道辛西娅”，正确。

### 块序单调性

`38 < 77 < 86 < 104 < 128 < 150 < 159 < 165 < 168 < 174 < 177 < 207 < 246` ⇒ **13 块 0 调转**。

---

## 四、R4 逐块对应表

| 块 | md | 原文 | 动词主语 | 受事 | 归属方向 | 结论 |
|---|---|---|---|---|---|---|
| 1 | :17 | `:38` | Cynthia（needed to distract／imagined）／It（rose／flew／landed） | 她的思绪／**手帕** | `It`＝白手帕 ✔；md:19“箱子”⇒ **E1** | 对应 ✔（译文错） |
| 2 | :27 | `:77` | I（saw）／she（must be） | you both／pool | 说话人＝埃莉 ✔；md:33“同处一室”⇒ **E7** | 对应 ✔ |
| 3 | :37 | `:86` | There were（two dresses）／Cynthia（dragged／spun） | 两条裙子 | 施事＝辛西娅 ✔ | 对应 ✔ |
| 4 | :47 | `:104` | Cynthia（had read）／The article（mentioned） | 五铃街浴场 | “我喊出街名”＝辛西娅 ✔ | 对应 ✔ |
| 5 | :57 | `:128` | Cynthia（called／nearly crawled）／she（couldn’t prevent） | 马车／可怕的事 | “拒绝了她”＝海伦娜 ✔ | 对应 ✔ |
| 6 | :67 | `:150` | Helena（was dying）／Her powers（seeped）／her vision（refused） | 她自己 | 主体＝海伦娜 ✔；md:73“三个词”✔ | 对应 ✔ |
| 7 | :77 | `:159` | Helena（would never see／watch／kiss） | Cynthia 的脸／眼／唇 | 受事＝辛西娅 ✔；md:83“四个再也”⇒ **E12** | 对应 ✔ |
| 8 | :87 | `:165` | she（had fallen in love） | — | 主体＝海伦娜 ✔；md:93 时间点⇒ **E14** | 对应 ✔ |
| 9 | :97 | `:168` | What Mother felt／what he gave | 心／力量／魔法／灵魂 | 施事＝母亲与铁匠 ✔ | 对应 ✔ |
| 10 | :107 | `:174` | Cynthia（would never try）／they（were laced）／the love（could never warp） | 海伦娜的灵魂 | “她给爱设的条件”✔ | 对应 ✔ |
| 11 | :117 | `:177` | I（will suffer）／Let me（watch） | 她的灵／爱人 | 祈祷主体＝海伦娜 ✔ | 对应 ✔ |
| 12 | :127 | `:207` | you（Don’t touch）／I（will rip／steal／cut／damn） | Cynthia／辛克莱的肺等 | 施事＝海伦娜、受威胁者＝辛克莱 ✔ | 对应 ✔ |
| 13 | :137 | `:246` | The click（was followed）／she（couldn’t die）／Cynthia（would need） | 热气／哈姆雷特 | “共同的魔宠”✔；章末声音未点名 ✔ | 对应 ✔ |

---

## 五、形态层

| # | 检查项 | 结果 |
|---|---|---|
| 1 | 导航 5 项齐全 | ✔ |
| 2 | 13 块格式 `> **原句 N:**` 连续、外层 `"…"` 首尾闭合 | ✔ 13/13 |
| 3 | 四子项齐全（含「读者视角提示」） | ✔ 13/13 |
| 4 | 词表标准 Markdown 表格、9/9/6＝24 行 | ✔ |
| 5 | 词头在正文命中 | ✔ 24/24（`maudlin` `:38`、`diaphanous` `:56`、`inexplicably` `:47`、`endeavoured` `:98`、`luminescent` `:159`、`spectre` `:177`、`arid` `:195`、`vestiges` `:207`、`scalding` `:161`、`extricated` `:110`、`acrobatics` `:107`、`landau` `:128`、`heeded` `:125`、`croak` `:186`、`whoreson` `:198`、`sheening` `:183`、`cloying` `:174`、`hulking` `:175`、`footman` `:44`、`waistcoat` `:183`、`breeches` `:183`、`vent` `:246`、`hanger` `:86`、`nightgown` `:56`） |
| 6 | 例句含词头 | **✘ 2 条**：`vent`（md:184）、`nightgown`（md:186）⇒ **E3** |
| 7 | 块数档位：13 vs `block_target=[4,7]` ⇒ **超限** | 提示型（rc 仍 0）⇒ **禁止增第 14 块**，补漏只进导航或现有块 |
| 8 | H1 | `# 24. Chapter Twenty-Four` ✔ |

---

## 六、实跑取证

**A. 本章推广残留**
```
$ /usr/bin/grep -ci lokepub notes/books/novels/the-hexing-miss-helena-by-darcy-mcguire/text/ch24_chapter_24.txt
0
rc=1
```

**B. 雪松／尤加利（E2）**
```
$ /usr/bin/grep -in "cedar\|eucalyptus" notes/books/novels/the-hexing-miss-helena-by-darcy-mcguire/text/ch24_chapter_24.txt
（无输出）
rc=1
$ /usr/bin/grep -n "cedar\|eucalyptus" text/ch23_chapter_23.txt
198:Cedar and eucalyptus created an incongruently pleasant scent…
```

**C. Roger Evans 计数（md:55 成立）**
```
$ /usr/bin/grep -o "Roger Evans" notes/books/novels/the-hexing-miss-helena-by-darcy-mcguire/text/ch24_chapter_24.txt | wc -l
1
```

**D. 哀悼与 never 计数（E11／E12）**
```
$ /usr/bin/grep -in "mourning\|mourn" text/ch24_chapter_24.txt
89:Ellie raised a brow…‘That is certainly not a mourning gown.’
$ /usr/bin/sed -n '159p' text/ch24_chapter_24.txt | /usr/bin/grep -o "never" | wc -l
2
（另有句首大写 `Never` 一次，合计 3 次；md 称“四个”）
```

**E. 词表例句缺词头（E3）**
```
$ python3 - …（逐行拆 `| 词 | 释义 | 例句 |`，判 head.lower() in ex.lower()）
L184: HEAD='vent'  NOT IN EXAMPLE
L186: HEAD='nightgown'  NOT IN EXAMPLE
```

**F. 逐字（R2 ＋ 两把独立尺子）**
`chapter.sh --json`：`verdict ok`、13 块全 `ok`、`segment_miss=0`、`issues` 全空；`/tmp/hx_md_frag.py` → `checked=13 BAD=0`；R1 底稿 `/tmp/hx_frag_check2.py` → `checked=178 BAD=0`。

---

## 七、悬置

| # | 悬置点 | 取证 |
|---|---|---|
| U1 | 章末那个“温柔如夏风的声音”是谁 | `:255` 只写“另一个声音”；`:258` 无名；全书后文才揭，本章不裁决 |
| U2 | 辛克莱“要的东西”是什么 | `:243` 只说 `what I seek`；本章未说 |
| U3 | 哈姆雷特到底出了什么事 | `:222` 只报 `It’s the fox.`；`:231` 只说“暂时没事” |
| U4 | 辛克莱进店前是否已知海伦娜是女巫／如何得知辛西娅 | `:201` 暴露他知道辛西娅，但不知途径 |
| U5 | 罗温“去巴斯帮朋友”的具体事由 | `:71` 只有一句转述 |
| U6 | 五铃街与七铃区的地缘关系 | 本章只有 `:134` “Devil of Seven Dials”；ch25 `:40` `She was in the Devil’s playground now` 最接近，仍未给地图级事实 |
