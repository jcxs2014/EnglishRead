# ch03 对账（R3）

素读：`1-suread.json`（14 条，全部 `text/ch03_fallout.txt:行` + 逐字，脚本校验 14/14）。
机器：`2-machine.json` rc=0；块数 10；引语 10 段全 ok；空引号 0；结构 0；关键词全中；`block_hint`「块数 10 偏离本书常见区间 3–9」——本书 71 章中位 6、最高 10，本章 10 属并列最高，不判红。
md 153 行，10 块 + 5 条导航 + 词汇 15 条。
块→原文行：1 `:23`、2 `:34`、3 `:273`、4 `:297`、5 `:456`、6 `:527`、7 `:710`、8 `:766`、9 `:838`、10 `:1079`。

## 一、漏（素读有、md 无）

### 1. 【阻断】追兵是谁、为什么要跑：全章零字

md 的 5 条导航与 10 块里，`grep -nE "Junior|七|朋友" "ch03 fallout.md"` → **0 命中**（`/usr/bin/grep`，exit=1）。于是「Caralora 拉响火警、三人钻隧道」在 md 里没有原因。

- 原文 `text/ch03_fallout.txt:101`：「“Well, you know, Zach’s car is pretty conspicuous. It was noticed, and **there are some guys waiting for you out there**.”」
- 原文 `:109`：「“**Large guys. Friends of Junior’s**.”」
- 原文 `:1042`：「**Junior and his friends killed seven people** that I know about, and they had allies in the police, so that was the only way we could get them.」
- md 侧对应：仅 md:11「快到午夜，Caralora 拉响火警」（无事由）；md:13「白马王子的马车被烧掉」（无纵火者）。
- 判断：这是本章所有动作的触发点，也是全书主线的敌手首次以「一伙人」的规模出现（七条命）。未进任何块或导航，且 md 未写取舍理由 ⇒ 阻断。

### 2. 【提示】进门暗号「jellyfish paradox」未落

- 原文 `:34`：「Zach gives the password, **jellyfish paradox**, and we're in.」
- md：`grep -n "jellyfish"` → 0。
- 判断：细节，但它是本章唯一的「地下/私密空间」信号，与后文隧道成对；提示。

### 3. 【提示】「另一个 Alba」怎么出现、怎么消失，全没进块

- 原文 `:242`：「“Hey, guys.” My knees almost buckle. / **It’s me. Of course.**」＋`:244`「“Hush,” my other self murmurs. “There’s a security guard around somewhere. **I brought a ladder.** Here.”」＋`:247`「“**The floor is rotted out.** I’m afraid to stand on it.”」
- 原文 `:375`：「**She steps back inside, but I see her vanish before the door closes.**」
- md：块 4 只取 `:297` 的「抬下巴交接」；「梯子」全章仅出现在 md:27 的读者视角提示里一句「未来的她递梯子」；`:375` 的当面消失无块无导航（`grep -n "消失"` 命中 12/14/95 行，都不是这一处）。
- 判断：md 把「交接」写足了，但把「她当场消失」这个与结尾 Alba 消失互文的关键动作漏掉；提示。

### 4. 【提示】Caralora 交底的内容只剩半句

- 原文 `:983`：「“I was agonizing over the—you know—**the other you told me I would start again. She knew my real name**, she knew things about me that I’d never told anybody…”」（Caralora 讲的是「另一个 Alba」先叫出她的真名、预言她会重新开始，她才敢离开 Alba）
- md:14：「Caralora 从警告者变成司机兼救援者，顺路交代了自己为什么离开 Alba——她厌倦了当那套支撑系统。」
- 判断：md 保留了「为什么离开」，丢了「谁让她敢走」（年长 Alba 的干预）——这是全书「未来自我推动现在」的第二次实证；提示。

## 二、编（md 有、原文无）

无。10 块中文的每一处情节断言都能在 text 中找到落点（详见「已核实为正确」）。

## 三、错（两边都有但不一致）

### 1. 【提示】「元旦早上」把凌晨与早上并成一场

- md:11：「元旦早上两人回到她家喝茶，她当面指出他改过名字」；md:15：「元旦早上那一行 `Zach:` 明着换人，于是**同一个早上被写了两遍**——先喝茶、谈婚姻，再醒来、拉琴、放水、取车。」
- 原文：逃出后仍是跨年夜，`:412`「I can see and hear fireworks to the east, along the lakefront.」`:401`「Come back tomorrow and pick it up.」`:419`「my date has been patient; she's waiting for me up in Evanston.」`:421`「Inside, the house is silent and chilly.」→ `:638`「**We fall asleep in the New Year**, content with our beginning.」→ `:641`「**Zach: I wake up happy.** The light around the edges of the blinds is white.」
- 结论：喝茶、谈婚姻发生在 1 月 1 日凌晨（烟花仍在、屋里冷），「醒来—拉琴—放水—取车」是他睡醒之后的同一个上午；不是「同一个早上被写了两遍」。日期没错，错在时段并置，**提示**（建议改「凌晨喝茶／早上醒来」）。
- 附注：`:639`「Today is day five of quitting」证明 Zach 段已在睡醒之后，与「凌晨」相隔一夜。

## 四、R4 逐块对应（10 块）

| 块 | 引语（text 行） | 是不是在讲这句引语 | 三问要点 |
|---|---|---|---|
| 1 | `:23`–`:26` | 是。怕这一天的理由（父亲忌日）＋仍赴约＋主题 1923＋借 Mama 的裙子 | 主语 I；「借」是借，不是买 |
| 2 | `:34` | 是。Uptown 街面、停 Lawrence、紧邻 St. Boniface 墓园、隔窗喊叫分不清敌友 | 受事＝车与街；「朋友还是敌人」保留歧义，未硬译 |
| 3 | `:273` | 是。「没有长椅的教堂」＋「影院睡美人」＋2081 年回来看 | 主语 it＝影院；「睡满一百年」正是 1981→2081 |
| 4 | `:297` | 是。另一个 Alba 抬下巴→她滑过去→Zach 张臂裹住＋万花筒天窗 | 施事链：Other Alba 示意→我→Zach；未反 |
| 5 | `:456` | 是。父亲在那儿读书、母亲在工作室做艺术、只要同时看见两人就安全 | 「她」＝母亲，md 明确；未与父亲混 |
| 6 | `:527` | 是。预制房 vs gut rehab＋「所以我很困惑」 | 说话人 Zach；「她」＝年长的 Alba，md 括注正确 |
| 7 | `:710` | 是。裸体是壳、演奏是灵魂；从小裸着跑，只能不去在意 | 主语 I；「die of shame」译「羞死」 |
| 8 | `:766` | 是。听水声太久→敲门→没人应（Zach 声部） | 主语已是 Zach，md 的读者视角提示明说换人 |
| 9 | `:838` | 是。先「空」后「在」：窗碎、胎熔、灰白铁壳 | 受事＝车；md:105 补出后备箱里的被子/书/相册，原文 `:861` 逐字有 |
| 10 | `:1079` | 是。摔下床、砸地板、骂人、床空而淋浴在响、他出来时她已站好 | 反写「水在响人不在」；27/28 岁与抬头 `:1074` 一致 |

密度：10 块中文「中文理解」39–107 字、「为什么这样写」101–124 字，全部就句论句，无一块铺垫全书主旨。
