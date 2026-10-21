# R5 判定表 · 第 13 章《Don't Leave Her Alone》

- 唯一真值：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch13_chapter_13.txt`
- 受审稿：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch13 chapter 13.md`（下文 **md:行号**）
- 配套文件：`3-diff.md`（R3 三张单子 ＋ R4 逐块对应 ＋ 专题 A 取证）、`1-suread.json`（R1）、`2-machine.json`（R2）
- 机器层：`bash scripts/chapter.sh "…/ch13 chapter 13.md" --json` → **退出码 0**（无阻断；注意 2=无法判定才算未通过，本轮不是 2）
- 本轮**只出指令不改稿**：未改任何 `ch*.md` / `00_*.md`，未 git add/commit/push。

**档位约定（本轮）**：阻断＝与原文不符/缺失（必须改）｜提示＝已核、写法正当或仅措辞/覆盖层可优化（记一行，不据此改稿）｜假红＝工具误报（本轮 0 条）｜跳过＝本轮未查。
**证据约定**：每条阻断都给 `text/<文件>:<行>` 与该处原文逐字；无逐字证据者一律写「未核」，不判阻断。

---

## 组一 · 逐字（引语逐字、块序、例句逐字）

| 断言 | 证据(章:区间) | 结论 | 档位 |
|---|---|---|---|
| A1 原句1 引语逐字且无省略号缝合 | text/ch13_chapter_13.txt:6 [233,599)｜"She backed away from the railing… knowing full well how much it bothered her." | 通过：366 字符连续全等，2 句/69 词（§3 硬线 1–3 句、30–70 词） | 提示 |
| A2 原句2 引语逐字 | text/ch13_chapter_13.txt:12 [2140,2363)｜"The laughter was getting louder…were unfiltered, completely real." | 通过：223 字符全等，37 词 | 提示 |
| A3 原句3 引语逐字 | text/ch13_chapter_13.txt:15 [4172,4358)｜"It went on and on and on…Stained with blood." | 通过：186 字符全等，35 词 | 提示 |
| A4 原句4 引语逐字 | text/ch13_chapter_13.txt:18 [7221,7487)｜"The child had an old man's face…you could barely separate." | 通过：266 字符全等，52 词 | 提示 |
| A5 原句5 引语逐字 | text/ch13_chapter_13.txt:63 [12438,12717)｜"The woman was wearing a Primark robe…Alba's wedding dress." | 通过：279 字符全等，47 词 | 提示 |
| A6 原句6 引语逐字 | text/ch13_chapter_13.txt:156 [15505,15852)｜"She needed someone—most of all, Carmen—…in shop mirrors." | 通过：347 字符全等，59 词 | 提示 |
| A7 原句7 引语逐字 | text/ch13_chapter_13.txt:198 [20412,20602)｜"At one point the silvery, shining appendages…split in half." | 通过：190 字符全等，32 词 | 提示 |
| A8 块序与原文顺序一致、词数全在 30–70 | 2-machine.json 落点 233 < 2140 < 4172 < 7221 < 12438 < 15505 < 20412 | 通过：偏移严格递增＝无倒置；词数 32–69 全部合规 | 提示 |
| A9 词汇表 24 条例句均为本章原句且各命中 1 次 | md:89–128；脚本 `例句 in text` 24/24 True，逐条命中数=1 | 通过：0 漏、无手写编造 | 提示 |

## 组二 · 对应（逐块＋总结层）

| 断言 | 证据(章:区间) | 结论 | 档位 |
|---|---|---|---|
| B1 原句1 四子项是否在讲这句引语 | text/ch13:6 [233,599)；引语外两句＝[7,229) | 不通过（对应）：md:25／md:27 依赖引语外的「楼下脏白球鞋和装手柄的盒子」＝S2①截短；但引语已 69 词，扩引语会破创建卡 §3 的 70 词硬线 ⇒ 取提示级，修法＝改写分析或另选自足引语 | 提示 |
| B2 原句2 四子项是否在讲这句引语 | text/ch13:12 [2140,2363) | 通过：四子项全在引语内（金属笑声／录音 vs 窸窣脚步两层） | 提示 |
| B3 原句3 四子项是否在讲这句引语 | text/ch13:15 [4172,4358) | 通过：长度→角度→尺寸→血；提示明确标注回指上一段，属读者引导 | 提示 |
| B4 原句4 四子项是否在讲这句引语 | text/ch13:18 [7221,7487) | 通过：主体＝队尾巨型婴儿、受事＝its eyes、"in the line" 归属一致（量词错与提示层矛盾另计 D2/D11） | 提示 |
| B5 原句5 四子项是否在讲这句引语 | text/ch13:63 [12438,12717) | **不通过**：md:65「为什么这样写」含原文没有的断言（D3）与冲突断言（D4） | 阻断 |
| B6 原句6 四子项是否在讲这句引语 | text/ch13:156 [15505,15852) | 通过：四子项落在引语内；"三个还不够"为标明出处的上下文引用，不判截短 | 提示 |
| B7 原句7 四子项是否在讲这句引语 | text/ch13:198 [20412,20602) | 通过：动作链 join→squeeze×3→split 逐动作对上；"紧接的下一句"标注清楚 | 提示 |
| B8 导航 5 项＋一句话总结是否与原文一致 | text/ch13:6/12/63/198/204/207/210 | **不通过**：漏章末尖叫与剪影（D7）、编购买动作（D5）、错灯亮状态（D4）、错交付顺序（D6） | 阻断 |

## 组三 · 形态

| 断言 | 证据(章:区间) | 结论 | 档位 |
|---|---|---|---|
| C1 H1／导航项数／子项集／块数／frontmatter 是否合本书众数 | 2-machine.json form 段；本书 ch00–ch13、ch16、ch17 逐章比对 | 通过：H1 `# 13. Chapter 13` 同形；导航 5 项；子项集＝中文理解/关键词/为什么这样写/读者视角提示；块数 7＝本书中位 7（范围 5–8）；frontmatter 与 ch12/ch16 逐字同形 | 提示 |

## 组四 · 断言（事实／归属／覆盖）

| 断言 | 证据(章:区间) | 结论 | 档位 |
|---|---|---|---|
| D1 原句1 末句 "her" 指谁（md:21「最招母亲的气」） | text/ch13_chapter_13.txt:6 [498,598)｜"the way **her kids** took their shoes off when they got home, knowing full well how much it bothered **her**." | **不通过（错·归属反转）**：her＝Alba 自己（"her kids"＝她的三个孩子，分词局部主语是孩子们，"were hurting her" 同段已用 her＝Alba）⇒ md 把被气的人与"知道"的主语都搬到了 Alba 的母亲 | 阻断 |
| D2 原句4「队伍里别的婴儿都是秃的」（md:51） | text/ch13_chapter_13.txt:18｜"**Some** of the babies in the line were bald, but not this one." | **不通过（错·数量）**：Some≠都；且与同块 md:55「秃头这个常规」自相矛盾 | 阻断 |
| D3 「买打折时节的婚纱」（md:65） | text/ch13_chapter_13.txt:63｜"The woman's dress was her dress from **Rosa Clará**. Her white crepe dress—now stiff and stained—…" | **不通过（编）**：原文是自家 Rosa Clará 白色绉纱婚纱，无"打折"性质 | 阻断 |
| D4 「在一座熄了灯…的商场里」（md:65） | text/ch13_chapter_13.txt:204｜"**The Christmas lights were on, as were the lights in the stores she usually went to.**"；:9｜"the light from the street was filtering in" | **不通过（错·场景状态）**：商场亮着灯，"没人影"成立、"熄了灯"不成立 | 阻断 |
| D5 「给自己买了一双芭蕾平底鞋」（md:11／md:132） | text/ch13_chapter_13.txt:204｜"she **found the ballet flats**… she chose the most understated pair—even they were encrusted with silver studs… She sat on the floor and put them on." | **不通过（编）**：原文只有找到→挑→坐下穿上；ch13+ch14 查无 bought/pay/purchase/cash/register/receipt（exit=1） | 阻断 |
| D6 导航「先看见拖尾→再看见四只小手→最后才看清那是个披睡袍的女人」（md:15） | text/ch13_chapter_13.txt:12｜"**She saw a woman**, her back to her, emerge from under the bridge."；:15｜"…caught sight of the hands that were holding it. Four tiny hands…" | **不通过（错·时序）**：女人最先被看见（:12），拖尾同段，小手在 :15 | 阻断 |
| D7 章末尖叫与剪影是否收录；"恐惧因此在章末转成落空"是否成立（md:11/12/132） | text/ch13_chapter_13.txt:207｜"She heard a scream that seemed suspended in time."；:210｜"The scream was coming from her right…she saw silhouettes. **Who were they? What was stirring there?**" | **不通过（漏＋错）**：md 无结尾尖叫/剪影；原文结尾不是"落空"而是新悬念 | 阻断 |
| D8 拍掌让圣诞灯重亮、沿血迹与脚印下楼是否收录 | text/ch13_chapter_13.txt:201｜"She lifted her arms and clapped at the sky… and the Christmas lights came back on."；:204｜"…a trail of blood… blurred at points by tiny footprints" | 覆盖不全（md grep「拍掌\|掌声\|灯亮\|重新亮\|clap」exit=1；「血迹\|脚印\|血径」exit=1）；非关键转折 ⇒ 提示级 | 提示 |
| D9 巨型婴儿体重/走路方式与队伍人数是否收录 | text/ch13_chapter_13.txt:18｜"those **thirteen- or fourteen-pound** babies who end up in the Guinness World Records books, except it was **walking like an adult**"；:27｜"**about fifteen of them**" | 覆盖不全（md grep「磅\|pound\|thirteen\|十四\|体重」exit=1）；md 未写出冲突数字 ⇒ 提示级 | 提示 |
| D10 原句5「一直挡着主角的视线」（md:61） | text/ch13_chapter_13.txt:63｜"The long train… had **distracted her** up till this moment." | 措辞级：原文＝分心，md＝物理遮挡；主结论不受影响 | 提示 |
| D11 原句4 读者视角提示「她看得出那里有东西在看」（md:57） | text/ch13_chapter_13.txt:18｜"eyes that looked like a boxer's after a fight: two straight lines you could barely separate"；同块 md:55「眼睛被肿得看不见了」 | 与本块引语及自身「为什么这样写」自相矛盾 | 提示 |
| D12 原句7／总结里的「触手」归属是否点明（md:81／md:132） | text/ch13_chapter_13.txt:21｜"the tentacles strangled **her** from within"；:162｜"the tentacles shot upward from **her belly**"；:180、:204 同指 Alba | 归属缺失（未写反，但读者会误以为触手属于那个女人） | 提示 |
| D13 原句6「在橱窗镜子里看看自己」（md:71） | text/ch13_chapter_13.txt:156｜"her desire to look at herself in **shop mirrors**" | 镜种不符：商场试衣镜 ≠ 橱窗镜 | 提示 |
| D14 女孩的耳环是否被写成本章事实 | text/ch13_chapter_13.txt 全文 `/usr/bin/grep -icE "earring"` → 0，exit=1 | 本章原文无耳环（女孩只以 "a dirty, worn-out white sneaker"（:6）与 "one Victoria sneaker"（:201）＋手柄盒出现），md 亦未涉及耳环 ⇒ 无错 | 提示 |
| D15 章末尖叫的来源是否被写成本章已知事实 | text/ch13_chapter_13.txt:207–210（本章只写"从右边来的尖叫""剪影""谁在那儿？"） | 本章不交代来源（跨章旁证：text/ch16_chapter_16.txt:18 "the same sound Alba had heard before, which had brought her here in the first place"）；md 未作来源断言 ⇒ 无错，只是整段漏收（见 D7） | 提示 |
| D16 原句6「尤其是母亲」是否等于 Carmen | text/ch13_chapter_13.txt:156｜"She needed someone—**most of all, Carmen**—to confirm she was still around"；:147｜"But you are like her. And like your mom." | 通过：Carmen 确为 Alba 的母亲，md 写法正确 | 提示 |
| D17 原句5「睡袍底下压着她的婚纱／那是主角自己的婚纱」 | text/ch13_chapter_13.txt:63｜"beneath it was **her wedding dress**… But it was her wedding dress—**Alba's wedding dress**." | 通过：婚纱归属＝Alba，md 未安错 | 提示 |
| D18 原句7 动作链（挤进来→一下一下勒腰→裂成两半） | text/ch13_chapter_13.txt:198｜"the silvery, shining appendages also joined in the embrace… squeezed and squeezed and squeezed the woman's waist, until the woman **split in half**" | 通过：md 的中文理解逐动作对上，没有把相邻动作并成一件，也没有把"看到的"写成"发生的" | 提示 |
| D19 原句4 三问（主语／受事／归属） | text/ch13_chapter_13.txt:18｜"**The child** had an old man's face… **its** eyes… the babies **in the line**" | 通过：主语＝队尾那只巨型婴儿，受事＝its eyes，归属＝队伍中的一员 | 提示 |
| D20 原句5 三问（主语／受事／归属方向） | text/ch13_chapter_13.txt:63｜"**The woman** was wearing a Primark robe… **her wedding dress**—Alba's wedding dress." | 通过：主语＝那个女人（Alba 的镜像），受事＝Alba 的婚纱，方向由 "Alba's" 锁定，md 未写反 | 提示 |
| D21 三篇总览（00_概述／00_金句精选／00_情感节点）对本章的断言一致性 | — | 未查：本轮范围＝单章 md 的 R0–R5；边界亦禁改总览 | 跳过 |

---

## 报数（只报四组）

| 组 | 阻断 | 提示 | 假红 | 跳过 | 小计 |
|---|---|---|---|---|---|
| 逐字 | 0 | 9 | 0 | 0 | 9 |
| 对应 | 2 | 6 | 0 | 0 | 8 |
| 形态 | 0 | 1 | 0 | 0 | 1 |
| 断言 | 7 | 13 | 0 | 1 | 21 |
| **合计** | **9** | **29** | **0** | **1** | **39 行** |

- 判定表共 **39 行**；阻断 **9**、提示 **29**、假红 **0**、跳过 **1**。
- 假红 0 的原因：机器层（chapter.sh）本轮无任何报警（issues 全空），不存在"工具报错而原文正确"的情形；被机器放过的才是人判区（漏／对应／施事归属／事实断言）。

---

## 阻断级清单（9 条，逐条：断言 | 证据区间 | 为什么阻断）

1. **原句1 末句 "her" 被安到 Alba 的母亲身上**（md:21）｜text/ch13_chapter_13.txt:6 [498,598)｜S3 第 ⑥ 类施事/归属反转：主语（谁在"知道"）与受事（谁被气）两处都反了；引语逐字、机器全绿，只有 R4 第三问能抓。
2. **原句4「队伍里别的婴儿都是秃的」**（md:51）｜text/ch13_chapter_13.txt:18｜"Some of the babies in the line were bald"＝有些，被写成"都"，且与同块 md:55 自相矛盾。
3. **「买打折时节的婚纱」**（md:65）｜text/ch13_chapter_13.txt:63｜原文婚纱＝自家 Rosa Clará 白色绉纱婚纱，"打折"凭空；与同句"两件日常衣服／降级成道具"也自相矛盾。
4. **「在一座熄了灯、没有人影的商场里」**（md:65）｜text/ch13_chapter_13.txt:204 与 :9｜原文圣诞灯与常去店铺的灯都亮着，"熄了灯"与原文冲突；且它是该段论证的前提。
5. **「给自己买了一双芭蕾平底鞋」**（md:11／md:132）｜text/ch13_chapter_13.txt:204｜原文只有找到→挑→坐下穿上，没有购买动作；ch13+ch14 零命中（exit=1）。
6. **导航"叙事手法"把交付顺序写反**（md:15）｜text/ch13_chapter_13.txt:12 与 :15｜原文先见披睡袍的女人（:12），再见拖尾（:12），最后见四只沾血小手（:15）。
7. **章末尖叫与剪影整段漏收，且"恐惧因此在章末转成落空"与原文冲突**（md:11／12／132）｜text/ch13_chapter_13.txt:207 与 :210｜cliffhanger 章的收尾钩子缺席；原文结尾是"Who were they? What was stirring there?"，不是落空。
8. **原句5 的"为什么这样写"整体不可信**（md:65）｜text/ch13_chapter_13.txt:63｜同一条子项里含 2 处原文无/冲突的断言（见第 3、4 条），R4"这段中文是不是在讲这句引语"不通过。
9. **总结层（导航＋一句话总结）与原文不一致**（md:11／12／132）｜text/ch13_chapter_13.txt:6/12/63/198/204/207/210｜同时含漏（第 7 条）、编（第 5 条）、错（第 4、6 条），总结层不可整体通过。

（以上每条均已给出 `text/<文件>:<行>` 与该处原文逐字，满足 R5 硬约束。）

---

## 零命中类断言的自证（R5-补）

全部使用 `/usr/bin/grep` 对**显式文件路径**执行（`text/` 被 `.gitignore:132` 排除，`git grep` 永远查无且退出码 1 与真查无不可区分）：

```
$ /usr/bin/grep -n -iE "bought|pay|purchase|cash|register|receipt" \
    notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch13_chapter_13.txt \
    notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch14_chapter_14.txt
（无输出）                                                        → exit=1
$ /usr/bin/grep -n -icE "earring" .../text/ch13_chapter_13.txt
0                                                                → exit=1
$ /usr/bin/grep -n -E "磅|pound|thirteen|十四|体重" "…/ch13 chapter 13.md"
（无输出）                                                        → exit=1
$ /usr/bin/grep -n -E "拍掌|掌声|灯亮|重新亮|clap" "…/ch13 chapter 13.md"
（无输出）                                                        → exit=1
$ /usr/bin/grep -n -E "血迹|脚印|血径" "…/ch13 chapter 13.md"
（无输出）                                                        → exit=1
$ /usr/bin/grep -n -E "scream|尖叫" "…/ch13 chapter 13.md"
85:…恐怖在这里没有尖叫…
101:| instinctively | … | The woman's adult screams got mixed up with the children's… |   → exit=0
$ /usr/bin/grep -n -E "买" "…/ch13 chapter 13.md"
11:…给自己买了一双芭蕾平底鞋。 / 65:…买打折时节的婚纱… / 132:…买了一双芭蕾平底鞋。       → exit=0
$ /usr/bin/grep -n -E "触手" "…/ch13 chapter 13.md"
81:…那几根银亮的触手也挤了进来… / 132:…被触手挤成两半…                                  → exit=0
$ /usr/bin/grep -n -o -E ".{0,40}Rosa Clar.{0,60}" .../text/ch13_chapter_13.txt
63: The woman's dress was her dress from Rosa Clará. Her white crepe dress—now stiff and stained—with its   → exit=0
$ /usr/bin/grep -n -o -E "The Christmas lights were on, as were the lights in the stores she usually went to" .../text/ch13_chapter_13.txt
204:…                                                                                    → exit=0
$ /usr/bin/grep -n -o -E "Some of the babies in the line were bald, but not this one" .../text/ch13_chapter_13.txt
18:…                                                                                     → exit=0
```

---

## 已核实为正确

> 本节所列写法**看起来像错、回原文核对后成立**。后续任何人不得以"读着不对"为由改动，除非能给出反证。

1. **原句6 的「尤其是母亲」＝Carmen**（md:71）。text/ch13_chapter_13.txt:156："She needed someone—most of all, Carmen—to confirm she was still around, with their presence, their shouting, their affection."；同章 :147 女人对 Alba 说 "But you are like her. And like your mom." ⇒ Carmen 确为 Alba 的母亲，md 的写法正确。
2. **原句5 的「睡袍底下压着她的婚纱／那是主角自己的婚纱」**（md:61）。text/ch13_chapter_13.txt:63："and beneath it was her wedding dress… But it was her wedding dress—Alba's wedding dress." ⇒ 婚纱归属＝Alba，md 未安错。
3. **原句1 的「猛地拽掉帆布鞋」「用另一只脚的脚趾去踩自己的鞋跟」「孩子回家脱鞋」**（md:21）。text/ch13_chapter_13.txt:6："yanked her shoes off… stepped on each heel with the toes of her other foot, the way her kids took their shoes off when they got home" ⇒ 三个动作逐个对上；**唯一错的是末句 her 的归属（见阻断第 1 条），前半段不动**。
4. **原句2 的「金属般的质感／老录音机」「未经加工的，真实得不能再真实」**（md:31）。text/ch13_chapter_13.txt:12："had a metallic quality, as if it had been recorded and was coming from an old tape player… were unfiltered, completely real." ⇒ 逐句对上。
5. **原句3 的「拖尾没有尽头→布料被怯怯掀起→四只极小的手、两边各两只→全都沾着血」**（md:41）。text/ch13_chapter_13.txt:15："It went on and on and on… the fabric lift timidly… Four tiny hands, children's hands—two on each side. Stained with blood." ⇒ 交付顺序与数量都对（数量词错在原句4，不在此处）。
6. **原句4 的「所有婴儿都是这样」「两道几乎分不开的直线」**（md:51）。text/ch13_chapter_13.txt:18："like all babies… two straight lines you could barely separate" ⇒ 对上；**错的是"队伍里别的婴儿都是秃的"那一处量词（见阻断第 2 条），"所有婴儿都是这样"这句不动**。
7. **原句7 的「一下、一下、一下地勒紧那个女人的腰」「从中间裂成两半」**（md:81）。text/ch13_chapter_13.txt:198："They squeezed and squeezed and squeezed the woman's waist, until the woman split in half." ⇒ 逐动作对上，md 没有把相邻动作并成一件，也没有把"看到的"写成"发生的"。
8. **原句7 读者视角提示「紧接的下一句就是一声轻响、全场灯灭，对方连同孩子们的哭声一起从她怀里消失」**（md:87）。text/ch13_chapter_13.txt:198："There was a snap, all the lights went out, and she vanished completely from Alba's arms. The children and their cries disappeared with her." ⇒ 对上。
9. **导航「对方睡袍底下压着 Alba 自己那件婚纱，两个长着同一张脸的女人抱在一起，那个女人最终被挤成两半、在灯灭中消失」**（md:11）。text/ch13_chapter_13.txt:63＋:198 ⇒ 对上；**错的是同句的"买了一双"（见阻断第 5 条）**。
10. **导航「孩子一个接一个被生出来，排成一条队伍，而队伍后面始终还排着一个」**（md:13）。text/ch13_chapter_13.txt:18："Just one more." ＋ :27 队尾接续 ⇒ 对上。
11. **原句3 读者视角提示回指上一段「那条拖尾被比作晚礼服」**（md:47）。text/ch13_chapter_13.txt:12："It looked like an evening gown." ⇒ 对上；该提示已自带"回到上一段"的标记，属读者引导，**不按 S2①截短判**。
12. **原句1 读者视角提示里的「楼下那只脏白球鞋和装手柄的盒子」本身正确**（md:27）。text/ch13_chapter_13.txt:6："down below where she remembered seeing the girl for the last time, there was a dirty, worn-out white sneaker and the box with the Switch controllers inside" ⇒ 场景细节属实（该块的问题是分析引用了引语外的句子，见 B1，不是这两样东西写错了）。
13. **形态类**（md 全文）。H1 `# 13. Chapter 13`、导航 5 项、子项集（中文理解/关键词/为什么这样写/读者视角提示）、块数 7、frontmatter（`状态: 未读` / `modified: "2026-10-21"` / `source_text: ch13`）与本书 ch00–ch13、ch16、ch17 同形 ⇒ **不必改**。
14. **词汇表 24 条**。例句逐条为本章原句且各命中 1 次，分档未见注水 ⇒ **不必改**。
