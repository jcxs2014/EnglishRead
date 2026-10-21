# 第 15 章 R3–R4 差异单（人工审查）

- **审查对象**：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch15 chapter 15.md`（111 行，7 个引语块，modified 2026-10-21）
- **唯一真值**：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch15_chapter_15.txt`（141 行 / 8270 字符）
- **机器层**：`review/ch15/2-machine.json`（已存在，未改动）——`verdict: ok`；7 块 `ok=true`；`counts`：blocks 7 / quote_long 0 / segments 7 / segment_miss 0 / struct_bad 0 / empty_quote 0 / keyword_bad 0 / cjk_low 0 / template 0 / keyword_long 7 / hole 0；`issues` 仅 `keyword_long` 7 条（非阻断）。
- **流程**：先素读原文并落 `review/ch15/1-suread.json`（R1），再开成品 md 对照（R3–R4）；本轮只出指令，**未改动任何 md 文件，git 未执行任何操作**。
- **行号约定**：`text/ch15_chapter_15.txt:NNN`＝原文行号；`ch15 chapter 15.md:NNN`＝成品 md 行号。字符区间为原文 UTF-8 解码后的 `[start,end)`。
- **本轮口径**：这两章的 md 已经过一轮修复，本单只报**当前版本**仍存在的问题；父代理已代修的四处（ch15 子项前缀统一为 `**中文理解**：`）记为**已修复**，不重复报错。

---

## 一、漏（L）

### L1【提示】Alba 当晚被困在 Splau 的洗手间——全章因果的起点，md 全文未出现

- **原文侧**（`text/ch15_chapter_15.txt:9`，字符区间 [1463,1607)）：`"I told you, I was at Splau. I got stuck in the bathroom," Alba answered. Then she opened the pizza box.`
- **md 侧**（`ch15 chapter 15.md`）：全文检索 `洗手间` / `厕所` / `浴室` / `bathroom` 命中数均为 **0**。md:11 只写「圣诞夜商场关门之后，戴安娜、妹妹阿尔巴和母亲卡门坐在 Splau 外的草地上吃剩下的披萨」。
- **影响**：读者拿不到本章唯一的「因」——Alba 为什么会在商场关门后才出来、为什么一身伤、为什么 Diana 后面要问「What happened in there?」。md 目前的因果链是「三人在草地吃披萨 → 谈伤口」，缺了「Alba 刚从洗手间出来」这一环，块 3（md:35）的「一样脏」就没有对照物。
- **修法**：在 md:21 或 md:35 的中文理解里补一句原文事实，例如在 md:21 段末加「阿尔巴那句『I got stuck in the bathroom』是这一夜的原点：商场关门时她还在洗手间里」；或在 md:11 一句话概括里把「商场关门之后」改成「商场关门之后、阿尔巴被关在洗手间里才出来」。**加完须保持中文句读得通**。

### L2【提示】Alba 的耳朵被撕裂——本章唯一直接指认她遭遇的证据，md 全文未出现

- **原文侧**（`text/ch15_chapter_15.txt:84`，字符区间 [4711,4917)）：`"My God, what's happened to your sister's ears? They look like cold cuts."`；紧接 `:87`（区间 [4920,5052)）：`"Alba, why are your ears all fucked up? What happened in there?"`
- **md 侧**（`ch15 chapter 15.md`）：全文检索 `耳朵` / `耳` 命中数均为 **0**。
- **影响**：md 只呈现了 Diana 与 Carmen 的两处腹部伤口，Alba 自己的伤完全没落地；读者会以为「被消耗」是这一夜之后才发生的事，ch16 的「树里的第三个人」「被切掉的残根」就失去铺垫。
- **修法**：在 md:49（块 5 中文理解，跨代转变那段）或 md:56 补一句原文事实，例如「同一段里卡门掀起毛衣说『你姐姐的耳朵怎么了，像冷切肉』——Alba 的伤是被看见的、只是没人肯先说」。

### L3【提示】手柄（controllers）在本章台词里出现，md 全文未出现

- **原文侧**（`text/ch15_chapter_15.txt:81`，字符区间 [4509,4708)）：`"No, I agree. I mean, I don't know… And she did get the controllers in the end."`（这句的 `she`＝Alba，即 :78 Carmen 问的「your sister」）
- **md 侧**（`ch15 chapter 15.md`）：全文检索 `手柄` / `controllers` 命中数均为 **0**。
- **影响**：这是本章唯一被确认的「胜利」（Alba 拿到了手柄），也是 ch10–ch12 主线与 ch16:48/60/66 收尾之间的接头。md 缺了它，「Holding the controllers」这条线在 md 里断了一章。
- **修法**：在 md:52 或 md:56 的分析里补一句，例如「Diana 在这一章唯一说出口的肯定句是『她最后还是拿到手柄了』——本章关于超自然的争论全部落空，落地的却是手柄」。

### L4【提示】Cornellà 与「你在这儿住到二十七岁」——本章唯一的地点与年龄锚点，md 全文未出现

- **原文侧**（`text/ch15_chapter_15.txt:102`，字符区间 [5696,5805)）：`"It's not the middle of nowhere. It's Cornellà. And don't forget you lived here until you were twenty-seven."`
- **md 侧**（`ch15 chapter 15.md`）：全文检索 `Cornellà` / `科尔` 命中数均为 **0**。
- **影响**：`twenty-seven` 是全书唯一一处（已 grep 全书确认），是「Diana 记得母亲的来路」这层意思的落点；地点 Cornellà 则是全书地名的固定写法（ch02/ch04/ch05/ch08/ch12/ch14 均出现）。md 缺这两条，等于把本章发生的地理坐标删了。
- **修法**：在 md:11 一句话概括里把「Splau 外的草地」写成「Cornellà 的 Splau 外草地」；并在 md:56 或 md:52 补一句「卡门一句『你别忘了你在 Cornellà 一直住到二十七岁』把三个女人拉回同一片地面」。

### L5【提示】Alba 在商场里跟店员发生过冲突（an argument with a clerk），md 全文未出现

- **原文侧**（`text/ch15_chapter_15.txt:78`，字符区间 [4330,4506)）：`"You think we just happened into this mess at the same exact time by coincidence? Have you seen your sister? It looks like she went through more than an argument with a clerk!"`
- **md 侧**（`ch15 chapter 15.md`）：全文检索 `店员` / `clerks` 命中数均为 **0**。
- **影响**：这是原文里唯一交代 Alba 在商场遭遇的「事件性」细节，也是 Carmen 断言「不是巧合」的对照面。md 缺它，「商场里到底出了什么事」只剩一个空壳。
- **修法**：在 md:52（块 5 读者视角提示）补一句，例如「卡门说 Alba 看起来像刚跟店员大吵过一架——这是原文给出的唯一一条现场线索」。

### L6【提示】平安夜叫不到车这一段（出租车 / App 显示「looking for drivers」/ 沉默等了几分钟），md 全文未出现

- **原文侧**（`text/ch15_chapter_15.txt:90`，区间 [5055,5423)）：Alba「Come on, let's go home. Let's call a taxi now so we get back before them… Tell them they can come in half an hour.」；`:93`（区间 [5425,5513)）Diana「There won't be any taxis now, especially not out here. It's Christmas Eve,」；`:96`（区间 [5516,5653)）Carmen「There are people who work on Christmas Eve,」；`:105`（区间 [5808,5891)）`Diana took out her phone and called them a car. "It says it's looking for drivers…"`；`:108`（区间 [5894,6029)）`They waited in silence for a few minutes.`
- **md 侧**（`ch15 chapter 15.md`）：全文检索 `出租车` / `taxi` 命中数均为 **0**。
- **影响**：本章的外部压力（平安夜没车、回不了家）整段缺失；这段还承担一个重要事实——**当晚确实没叫到车**（ch17:6「Since there were no taxis after all…」是它的直接后果）。md 里三个女人在草地上吃完披萨就进了「母亲自白」，中间的现实压力被抹平。
- **修法**：在 md:66 或 md:63 补一句，例如「三个人叫不到车，在草地上一边等一边把话说完——原文里她们等了好几分钟」。

### L7【提示】Brisa 与 Brigitte 是谁的孩子，md 只给了名字没给关系

- **原文侧**（`text/ch15_chapter_15.txt:30`，区间 [2585,2873)）：`It was telepathic, like the day Brisa and Brigitte got bloody noses within minutes of each other.`（Brisa 是 Diana 的女儿、Brigitte 是 Alba 的女儿；ch02:465–483 有正面交代）
- **md 侧**（`ch15 chapter 15.md:42`）：「……这就像心灵感应，就像布里萨和布里吉特那次在几分钟之内先后流鼻血。」——只出现名字，没有身份。
- **影响**：读者不知道这是两个母亲各自的孩子，也就读不出「同刻出血＝两代人共有的怪事」这一层——而这正是 Diana 口中「心灵感应」的根据。
- **修法**：把 md:42 改成「……就像心灵感应，就像戴安娜的女儿布里萨和阿尔巴的女儿布里吉特那次在几分钟之内先后流鼻血」（人名与关系均出自原文与 ch02）。

### L8【提示】Alba 为什么不解释自己经历了什么，md 未给出由头

- **原文侧**（`text/ch15_chapter_15.txt:90`，区间 [5055,5423)）：`Alba was exhausted, and she didn't have the energy or confidence to explain what she had gone through.`
- **md 侧**（`ch15 chapter 15.md:65`）：「……在这一章里，戴安娜是那个一路追问的人，而真正握着答案的人一句话都没说。」——只写了结果（不说），没写原因（不敢说 / 没力气说）。
- **影响**：结尾的沉默被写成性格，读者会以为 Alba 是在「端着」；原文给的是更朴素的解释——她既没有力气也没有自信去解释。补上这一句，:141 那两个「没有说」才不显得刻意。
- **修法**：在 md:65 或 md:66 补一句「原文给的理由很朴素：她筋疲力尽，既没有力气也没有自信去解释自己经历过什么」。

---

## 二、编（C）

**无。**

已核过的断言（逐条对照原文，全部成立，故不列缺陷）：

1. md:11「母亲的腹部伤口和戴安娜的伤口在同一刻出现」→ `text/ch15:42`「The wound showed up on both of us at the same time.」（`both of us`＝Carmen 与 Diana 两人，不含 Alba）——成立。
2. md:11「卡门最后承认自己当年肚子里也曾有过一只章鱼」→ `text/ch15:111`、`text/ch15:117`——成立。
3. md:12「戴安娜……面对怪事不知道该怎么反应」→ `text/ch15:132`「I never know how to react.」——成立。
4. md:12「阿尔巴从被追问的一方，变成握着答案却选择不说的一方」→ `text/ch15:141`——成立。
5. md:13「戴安娜刚说「你不是不信这种事吗」，卡门反问「哪一种？」，阿尔巴接着说「你刚才还在讲心灵感应」」→ `text/ch15:51`、`:54`、`:60`，顺序与归属均成立。
6. md:13「卡门抱了小女儿，却几乎立刻退开」→ `text/ch15:36`（`her youngest daughter`＝Alba）、`text/ch15:39`——成立。
7. md:15「一角是亮灯的厢式车，另一角是三个女人和写着 Splau 的红色招牌」→ `text/ch15:6`——成立。
8. md:21「十一月廿八日……都到寒假最后一天为止」→ `text/ch15:6`——成立。
9. md:24「多年赶不上主显节前的最后一块」→ `text/ch15:6`「Not once had she managed to set down the last piece before Epiphany, and it depressed her.」——成立。
10. md:35「阿尔巴说着，看了看母亲和姐姐的手——一样脏」→ `text/ch15:15`——**归属正确**（Alba 说的，她看的是母亲和姐姐的手）。
11. md:42「「妈妈也是。」戴安娜说」→ `text/ch15:30`——**归属正确**（说话人是 Diana）。
12. md:51「上一代的人感受得到爱，却既不习惯用身体表达，也不习惯用语言表达」→ `text/ch15:36`「they had always felt loved by Carmen, but it hadn't been easy for her to express it physically or verbally」——成立。
13. md:59「……紧接的下一段写她嗓音在抖。两个女儿都明白：即使那只是妄想，对母亲来说也真的发生过。」→ `text/ch15:120`——成立。
14. md:111 一句话总结里的「卡门说出当年营地的那个夏天」「女儿笨拙地说你们真勇敢」「妹妹只是温柔地看着姐姐，什么也没有说」→ `text/ch15:117`、`:132`、`:141`——成立。
15. md 词汇表 24 条例句已用脚本逐条比对（规范化引号/破折号/省略号后做本章 text 子串匹配）：`rows checked=24 not_verbatim=0`——无编造例句。
16. md 七个引语块经 `bash scripts/chapter.sh` 判定 `ok=true`，且 7 段引文逐字与 `text/ch15` 对应（块 1/2 在 :6，块 3 在 :15，块 4 在 :30，块 5 在 :36，块 6 在 :117，块 7 在 :141）——无改写、无拼接。

---

## 三、错（W）

### W1【提示】md:13 把「拆掉超自然」的那句反问的力度记在了卡门身上，原文里拆掉它的是 Alba

- **原文侧**（`text/ch15_chapter_15.txt:54`、`:57`、`:60`、`:63`、`:75`）：
  - `:54` Carmen：`"What kind of thing?"`（**只是要求澄清**，不是反驳）
  - `:57` Diana：`"You know, supernatural stuff…You always say we're crazy! And now this?"`（**卡门这句之后，争论还在继续**）
  - `:60` Alba：`"Wait a second, Diana. You're the one who was just talking about telepathy," Alba said`（**这一句才是把「心灵感应」拆掉的反问**）
  - `:63` Diana：`"Yeah, but I believe. I've experienced things."`／`:75` Diana：`"Very funny."`（**Diana 并没有被掀翻**）
- **md 侧**（`ch15 chapter 15.md:13`）：`「超自然被一句反问拆掉」的套路在此兑现——戴安娜刚说「你不是不信这种事吗」，卡门反问「哪一种？」，阿尔巴接着说「你刚才还在讲心灵感应」`
- **影响**：读者会把「拆掉超自然」记在卡门的「哪一种？」上。但原文里卡门这句只是让 Diana 把话说清楚，随后 Diana 反而更硬地表态「我信，我经历过一些事」。真正完成拆解的是 Alba 的 :60。差别不小：它决定读者理解本章母女与姐妹关系的落点。
- **修法**：把 md:13 改成 `「超自然被一句反问拆掉」的套路在此兑现——戴安娜刚说「你不是不信这种事吗」，卡门追问了「哪一种？」（可这一句只是让她把话说完），真正把「心灵感应」拆掉的是阿尔巴那句「你刚才还在讲心灵感应」`；同一句里的 `阿尔巴接着说` 改为 `阿尔巴把话头扳回来` 之类，避免读成「卡门的反问在拆、阿尔巴在附和」。

### W2【提示】md:44 说「后面母亲一句反问就能掀翻」，原文里掀翻的是 Alba，母亲的质疑并没有推翻任何东西

- **原文侧**（`text/ch15_chapter_15.txt:72`、`:75`、`:81`）：
  - `:72` Carmen（转向 Diana）：`"How do you explain it then?" "What do you think happened? We just ate something that didn't agree with us?"`
  - `:75` Diana：`"Very funny."`（**没被说服**）
  - `:81` Diana：`"No, I agree. I mean, I don't know… And she did get the controllers in the end."`（**反而顺着母亲走**）
- **md 侧**（`ch15 chapter 15.md:44`）：`……作者不给机制，只给一个类比——旧日那桩几分钟内先后流鼻血的小事。读者由此明白，戴安娜口中的「相信」其实是在没有更好说法时的应急，也正是后面母亲一句反问就能掀翻的东西。`
- **影响**：两处偏差叠在一起：一是把 Diana 的「相信」降格成「应急」（原文里她是先斩后奏地宣称自己相信，只是对「经历过什么」含糊其辞，`:63`、`:69`）；二是把掀翻者记成母亲，而原文里母亲的两次质疑（`:54`、`:72`）都没能动摇她，掀翻它的是 Alba 的 `:60`。
- **修法**：把 md:44 末句改为 `……读者由此明白，戴安娜口中的「相信」是拿旧事作类比、而不是给出机制——而这一句类比正是后面阿尔巴一句反问就能掀翻的东西（母亲两次追问都没能撼动她）`。
  （与 W1 同源，但落在不同 md 行、不同断言面，故分列两条。）

---

## 四、交叉说明

1. **称呼链**：本章的 `your sister` / `her youngest daughter` / `mom` 各自指谁，必须回原文核：
   - `:36`「she gave her **youngest daughter** a sad look. She wrapped her into a hug」→ 被抱的是 **Alba**（Carmen 的小女儿），不是 Diana。
   - `:78`「Have you **your sister**?」→ 说话人是 Carmen，`your sister`＝**Alba**（Diana 在对母亲说话）。
   - `:81`「And **she** did get the controllers in the end.」→ 说话人是 Diana，`she`＝**Alba**（承上一句 Carmen 问的那个「your sister」）。
   - `:84`「what's happened to **your sister's** ears?」（Carmen 对 Diana 说）→ `your sister`＝**Alba**。
   - `:42`「The wound showed up on **both of us**」→ 说话人是 Carmen，`both of us`＝**Carmen 与 Diana** 两人，**不含 Alba**。
   - `:132`「**Both of you** are so brave.」→ 说话人是 Diana，`both of you`＝**Carmen 与 Alba**。
   - `:87`「**Alba**, why are your ears all fucked up?」→ 说话人是 **Diana**。
   - 成品 md 的称呼链现状：md:35、md:42 两处归属均正确（见「二、编」第 10、11 条），本单不再改动。
2. **时间轴链**：本章 = 平安夜当晚，Splau 关门之后。三处互证：`text/ch15:18`「What a Christmas Eve dinner」、`:93`「It's Christmas Eve」、`:96`「There are people who work on Christmas Eve」。**本章内部另有一个更早的时间点**：`:117`「Our first summer at the campsite. The year I fainted on the beach.」＋`:111`「It was years ago.」——这是 Carmen 自白的营地夏天，与本章当晚不是同一时间层，md 在 md:56/md:111 提到它时用的是「当年／那个夏天」，口径正确。
3. **跨章事实（跨章引用必须标章号）**：
   - `text/ch15:30` 的 Brisa / Brigitte 流鼻血旧例，成因与「两代人同时出血」的正面交代在 **ch02:465–483**；md:42 引这两个名字时没标章号（见 L7）。
   - `text/ch15:81` 的 controllers 承 **ch10:93–96**（Alba 为 Switch 手柄折回 MediaMarkt）与 **ch11:99**（`one red and the other blue`，两只手柄），收在 **ch16:48/60/66** 与 **ch17:48**（Alba 把手柄扔进大垃圾袋）。
   - `text/ch15:111/117` 的章鱼与 ch12:96（「the fucking octopus」）、ch15:27/30/33/114、ch17:201/252/285 是同一条线；ch17:282 的 Alba「It was a tentacle, Mom. I had two.」与 ch17:285 Diana 的「an octopus tentacle」是本章母亲的「章鱼」在正文里的正式命名。md 本章**未出现**「章鱼」以外的推断表述，方向正确。
   - `text/ch15:102` 的 Cornellà 与 **ch02:42、ch04:24/33/183/198/369/372、ch05:705/714、ch08:6、ch12:162、ch14:270** 是同一地名写法，全书一致。
   - `text/ch15:117` 的「营地」在 **ch10:384/414/423/435/438** 有专名 **Camp La Tortuga Ligera**；本章只写 `the campsite`，未点名，md 沿用「营地」正确，**不必**在 md 里补专名（补了反而是本章没有的事实）。
4. **称呼／命名的体例一致性**：本章 md 的 `Splau` 写法与全书一致（ch10/ch13/ch15/ch16/ch17 及三篇总览均用 `Splau`），无需改动。

---

## 五、修后复核

改完 `ch15 chapter 15.md` 后，按顺序跑下面这组命令。

```bash
# 1) L1–L8 的补充句落地：洗手间 / 耳朵 / 手柄 / Cornellà / 店员 / 出租车 / 关系 / 解释
/usr/bin/grep -n "洗手间" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch15 chapter 15.md"   # 期望 exit=0 且命中 ≥1
/usr/bin/grep -n "耳朵" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch15 chapter 15.md"      # 期望 exit=0 且命中 ≥1
/usr/bin/grep -n "手柄" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch15 chapter 15.md"      # 期望 exit=0 且命中 ≥1
/usr/bin/grep -n "Cornellà" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch15 chapter 15.md"   # 期望 exit=0 且命中 ≥1
/usr/bin/grep -n "店员" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch15 chapter 15.md"      # 期望 exit=0 且命中 ≥1
/usr/bin/grep -n "出租车" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch15 chapter 15.md"    # 期望 exit=0 且命中 ≥1

# 2) W1 / W2 的旧措辞必须消失（期望 exit=1）
/usr/bin/grep -n "阿尔巴接着说「你刚才还在讲心灵感应」" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch15 chapter 15.md"   # 期望 exit=1
/usr/bin/grep -n "也正是后面母亲一句反问就能掀翻的东西" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch15 chapter 15.md"   # 期望 exit=1

# 3) 关键归属不得被改坏（期望 exit=0，命中仍在）
/usr/bin/grep -n "阿尔巴说着，看了看母亲和姐姐的手" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch15 chapter 15.md"   # 期望 exit=0
/usr/bin/grep -n "「妈妈也是。」戴安娜说" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch15 chapter 15.md"             # 期望 exit=0

# 4) 门禁
bash scripts/chapter.sh "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch15 chapter 15.md" --json   # 期望退出码 0
```

补充说明：

- 补写 L1–L8 的句子时，每条都应挂在**已有的四个子项行**（中文理解 / 为什么这样写 / 读者视角提示）上，**不要新开子项、不要改块数**（块数 7，落在 3–10 内）。
- 补写后请重跑本轮用过的词汇逐字校验脚本思路：`## 本章词汇` 的 24 条例句必须仍然是本章 text 的逐字子串（补写不涉及词表，但若顺手改了词表，须重新核对）。
- 本单只出指令，未改动任何 md 文件；git 未执行任何操作（未 add / 未 commit / 未 push）。
