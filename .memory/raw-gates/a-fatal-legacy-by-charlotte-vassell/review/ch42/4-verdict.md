# 4-verdict.md · ch42 判定表

> 审查员：独立审查（只审 ch42）｜书：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell`
> 原文：`text/ch42_42.txt`（= epub `OPS/s058-Chapter-042.xhtml`，已逐字比对一致）
> md：`ch42 mel is the voice and eulalia is the face.md`
> 机器层：`2-machine.json`（`verdict: ok`；`counts`：blocks 8 / segments 8 / segment_miss 0 / struct_bad 0 / empty_quote 0 / keyword_bad 0 / cjk_low 0；**四道探针全绿**）
> 落盘目录：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch42/`（本轮只写此处，未改书目录任何 md，未 git add/commit）

## 0. 四组数（只报这四组）

| 组 | 数 | 说明 |
|---|---|---|
| **逐字** | **8/8 引语逐字命中，0 缺陷**（另有词汇例句 **30/30** 逐字命中，自建核对；`text/` 未被 `.gitignore` 干扰，用显式路径 + Python 读取） | `2-machine.json` 的 `quotes` 全部 `ok:true`、`segment_miss:0`；8 段均为单段引语，无省略号缝合、无跨话轮拼接 |
| **对应** | **8/8 块对应成立**（每块的"这段中文是不是在讲这句引语"＝是）；**施事/受事/归属 8/8 正确，0 处写反**；但 **1 块内部口径自相矛盾**（块 8：中文理解时序对、为什么这样写时序反） | 逐块见 `4-correspondence.md` |
| **形态** | **0 偏离**（H1 / 导航项名与项数 / 子项集 / 块数四项全部符合，无需理由） | H1 `42. Frithsden Old Hall`＝epub `42 Frithsden Old Hall` ✔；导航 5 项＝本书众数 5（`nav_count_ok:true`，`nav_counts:[5]`）✔；子项集 {中文理解, 关键词, 为什么这样写, 读者视角提示}＝`profile_subitems`（mystery-thriller）✔；块数 **8** vs 本书众数 **7**、区间 [5,10] ✔ |
| **断言** | **16 条**：**阻断 2**（同一原文行、md 两处）＋ 提示 14 | 见下表 |

**阻断型条数：2**（同一根因、两个 md 位置；均非机器可判——引语逐字、中文是中文、关键词成立、形态正常，四探针全绿）

## 1. 判定表（断言 | 证据 | 结论 | 档位）

| # | 断言（md 位置） | 证据（章:区间·原文逐字） | 结论 | 档 |
|---|---|---|---|---|
| A1 | 导航·人物弧线：「她**先**替对方开脱（"她必须这样才撑得住"），**再**被自己冒出的那句"她一直在说谎吗"吓一跳」 | `text/ch42_42.txt:252`：`‘She talks the talk,’ Callie said. She vividly remembered Eulalia waxing lyrical about her creative process and performing. Had she really been lying? ‘I guess she has to, to pull it off, but maybe she’s a bit delusional.’`（问句 `Had she really been lying?` 在**前**，开脱 `I guess she has to` 在**后**） | 反应**先后写反** | **阻断** |
| A2 | 块 8·为什么这样写：「表层是**立刻**替对方找补，**深处**是一句没人回答的问句」 | 同上 `:252`（且与**本块自己的中文理解**——「问自己：她真的在撒谎吗？**随即又**替对方开脱」——自相矛盾） | 时序写反 + 块内口径打架 | **阻断** |
| B1 | 块 3·中文理解：「一边往下翻那篇配着照片的文章，一边**摊手**」 | `text/ch42_42.txt:123`：`Callie scrolled through the article that was linked to the picture of Eulalia moseying around Primrose Hill in the baggiest clothes that she could find.`（无摊手/摊臂动作） | 凭印象加动作 | 提示 |
| B2 | 块 3·中文理解：「约定在新专辑和新造型公布之前不吐露任何**与身份有关的消息**」 | `:123`：`It was around her identity and not revealing anything about the **process** until the new album and look have dropped.`（NDA 涉身份 ＋ 不透露**流程**直到专辑/造型公布；md 把时间状语挂到了身份那一句） | NDA 对象改写 | 提示 |
| B3 | 块 7·中文理解：「**她把照片上的人认成了 Eulalia**，其实那是她姐姐 Mel」 | `:237`：`she’s not that old though. Mid-twenties.`→`scroll through the graduates of their Vocal & Opera course`；`:240`：`‘Wait, that’s her,’ Callie said…`；`:243`：`‘That’s Eulalia?’ Caius asked, surprised.` | 原文两读并存（A：卡莉先当是欧拉莉亚后改口；B：卡莉一眼认出梅尔、凯厄斯误认）。md 采 A，且 A 有 `:237`/`:240` 支撑（她正在找欧拉莉亚；"Wait, that's her" 非 "that's Mel"）⇒ **不判阻断**，但 md 未标歧义 | 提示 |
| B4 | 块 7·读者视角提示：「发现这句话的是 Callie，**第一个愣住的也是她**」 | `:243`：`‘That’s Eulalia?’ Caius asked, **surprised**.`（此刻被写为 surprised 的是**凯厄斯**；卡莉的震动出现在块 8 `:252`，**晚于**本块） | 反应先后与人称待作者定夺 | 提示（接近阻断） |
| B5 | 块 7·为什么这样写「用**一张照片**替他把结论坐实」＋ 导航·一句话概括「在一张**毕业照**上认出」＋ 导航·线索结构「毕业**照**名单」 | `:237`/`:240` 原文只有 `the graduates of their Vocal & Opera course`、`pointing at a young woman who had graduated five years ago`，**无"照片/毕业照"字样**；epub `s058-Chapter-042.xhtml` 内 `<img>` 数为 **0** | 物证类型被升级（名录页 → 照片） | 提示 |
| B6 | 块 5·中文理解：「**凯厄斯放下刀叉，先说** Eulalia 演出时戴的头套」 | `:204`：`‘The heads she wears when she performs.’ Caius put his cutlery down.`（先说后放） | 两个相邻动作次序对调 | 提示 |
| B7 | 块 8·中文理解：「不过她大概有点**自我陶醉**」（译 `delusional`） | `:252`：`maybe she’s a bit delusional.` | 释义偏移（delusional＝妄念/不切实际的自我认知） | 提示 |
| B8 | 块 8·读者视角提示：「注意那个问句**后面没有答案**」 | `:252`：问句后紧接 `‘I guess she has to, to pull it off…’`＝卡莉自己给出的宽解 | 「没有外部答案/没有定论」成立，「没有答案」略强 | 提示 |
| B9 | 导航·叙事手法：「**前三分之一**用早餐、散步、露台闲聊……再让一部手机把外面的世界插进来」 | `text/ch42_42.txt` 中 `Callie’s phone rang` 位于 offset 4891 / 全文 10757 ＝ **45.5%** | 比例数字与原文不符 | 提示 |
| B10 | 导航·视角：「**Dotty 负责插不上话**」 | `:23`：`‘Dotty, we’ll let you set today’s agenda,’ Callie said.`；`:26`：提议绕 duck pond；`:57`/`:87`：自述孕晚期身体与两次流产；`:162`：`You’ve got to be careful now you’re together. There are more “Lauras” out there than you’d think…` | 概括偏窄（Dotty 本章有实质贡献） | 提示 |
| B11 | 块 1·读者视角提示：「一座**什么房间都齐全**、却没人按它的用途使用的房子」 | `:20`：`Breakfast for once was in the breakfast room. Caius and his family were still not used to eating anywhere other than the kitchen.` | 原文未说"什么房间都齐全" | 提示 |
| B12 | 块 2·中文理解：「于是有许多女人带着这种悲伤走在路上，**装的**却像它根本不存在」 | `:96`：`There are so many women just walking around with that grief like it’s nothing.` | 原文无"装/伪装"这一层 | 提示 |
| B13 | 全章：md **未出现 PCQV** | `:135`：`Venetia from Ceramics 101 was there though. She works for PCQV now.` | 漏·次要（因未提，**不存在"PCQV＝唱片公司"的混淆**；硬事实③在本章自动满足）。另 `Mel was fine the first time I met her but she was really off with me when I presented yesterday` 这一"梅尔为何古怪"的因果线索亦未进入 md | 提示 |
| B14 | 块 6·为什么这样写：「**刑侦**上被撵开的人」 | `:210`：`He was still aggrieved that he’d had to walk away from the Priory Square case and was trying to get his fix elsewhere.` | 措辞发挥，方向无误 | 提示 |

## 2. 待核点逐条回答

| 待核点 | 结论 |
|---|---|
| ① 老宅早餐这一场里每个人是谁、说了什么 | md 的**施事归属全部正确**：Dotty＝Caius 的母亲（`:32` `'Don’t encourage my mother,’ Caius said.`）、Georgie＝Dotty 的伴侣（`:108` `'Darling, go help Caius carry lunch out.’`）、Callie＝Caius 的伴侣且怀孕（`:75`/`:78`/`:84`）、Eulalia 未到场（`:111` 仅为来电）。md 未把 Dotty 的流产自述安到 Callie 头上（`:87` vs `:96`），未把头套/假唱推断安到别人头上（`:204`）。**唯一不足是导航层把 Dotty 概括成"插不上话"**（B10）。 |
| ② 「声音与脸」这个结论是谁说的、语境、听者 | **说的人是 Callie**（`:246`：`‘No, that’s Mel, her sister.’ Callie looked up at Dotty and Georgie. ‘You’re right, it’s a scam… Mel’s the voice. Eulalia is the face…’`），语境＝午餐桌、Caius 刚抛完"真声在后台"的推断之后（`:210`），听者＝Dotty 与 Georgie（Caius 也在场）。**md 归属正确**（不是欧拉莉亚说的、不是梅尔说的、也不是凯厄斯说的）；`Mel's the voice / Eulalia is the face` 的**方向也没写反**。 |
| ③ 那张照片里是谁 | 本章有两处视觉物，**md 两处都没认错人**：① 块 3 的文章配图＝**Eulalia**（`:123` `the picture of Eulalia moseying around Primrose Hill`）→ md 写"照片里是 Eulalia"✔；② 毕业名录上 five years ago 的"年轻女人"＝**Mel**（`:240`→`:243`→`:246`）→ md 写"其实那是她姐姐 Mel"✔。md 的问题只是把 ② 的物证叫成"照片/毕业照"（B5，原文无 photo 字样）。 |
| ④ 导航与总结对"错位揭晓"的概括 | 分部名「SATURDAY」＝**书里真名**（epub `s056-Part-009.xhtml` = SATURDAY，ch42 = `s058-Chapter-042.xhtml`；全书十二分部中只有第一部叫 A FRIDAY IN MAY）✔；"台前的是脸，台后的是声音"与 `:246` 一致✔；**但「人物弧线」把揭晓后的反应顺序写反（A1，阻断）**，另有"前三分之一"（B9）、"Dotty 插不上话"（B10）、"毕业照"（B5）三处偏。 |

## 3. 硬事实核查

- **分部名**：md 写「SATURDAY」——ch42 在 epub 中位于 `Part-009 SATURDAY`，**正确**（取证：unzip epub 后读 `OPS/TOC.xhtml`，导航项 `s056-Part-009.xhtml | SATURDAY` → `s058-Chapter-042.xhtml | 42`）。
- **机器全绿 ≠ 没缺陷**：本轮 2 条阻断型**全部是时序/前后关系写反**，四道探针（引语逐字、中文是中文、关键词成立、形态正常）**对这类缺陷结构性无能**——已由第 3 步的三问（每块问"这段中文在讲这句引语吗 / 引语是谁说的 / 分析有没有讲引语之外的东西"）看出。
- **PCQV 与唱片公司是两个实体**：本章 md **未出现 PCQV**；块 5 把 `no label` 译作"厂牌"（唱片公司），**未把 PCQV 当唱片公司**；全书 ch36 的导航已明写"法国奢侈集团 PCQV"与"欧拉莉亚自己的唱片公司是另一方"——本章与之**不冲突**。

## 4. 已核实为正确（防误修 · 后续任何人不得以"读着不对"为由改动）

| 写法 | 原文逐字（`text/ch42_42.txt`） |
|---|---|
| 块 7「Mel 是声音，Eulalia 是脸」方向 | `:246` `Mel’s the voice. Eulalia is the face.` |
| 块 4 未指派"谁是女神谁是毕加索" | `:147` `one of them, as you can see, looks like a goddess and the other looks like a Picasso.`（原文本就未指派） |
| 块 2「她讲起自己接受过心理咨询」＝Callie | `:96` `I had counselling.`（Dotty 的流产在 `:87` `I had two miscarriages before …`） |
| 块 3 照片里的人是 Eulalia | `:123` `the picture of Eulalia moseying around Primrose Hill in the baggiest clothes that she could find.` |
| 块 7 毕业名录上的人是 Mel | `:240`/`:243`/`:246` `‘Wait, that’s her,’ Callie said, pointing at a young woman who had graduated five years ago.` / `‘That’s Eulalia?’ Caius asked, surprised.` / `‘No, that’s Mel, her sister.’` |
| 块 5「厂牌藏不住一张漂亮脸」＝ the label | `:204` `Realistically, no label is going to hide a pretty face.` |
| 块 6 提问者是 Caius、被问的是 Callie | `:210` `‘All right, then the real voice is stood offstage singing live?’ Caius asked. … ‘What do you know about her, Callie?’` |
| 块 3 把 `baggiest clothes that she could find` 的 she 读成欧拉莉亚本人 | `:123`（离 `Eulalia moseying` 最近，且与"仍被认出"自洽） |
| 导航「Georgie 负责起哄」「凯厄斯负责推演」 | `:189` `‘Is she hot?’ Georgie asked.`；`:210`（Caius） |

## 5. 覆盖声明

- 本次**只审 ch42**（一部书一章），未审其余 53 章；书内其余章**只有机器层**（`gate.sh`/`chapter.sh` 的既有结果），**不得写成"通过"**。
- ch42 的机器层已**重跑**（`bash scripts/chapter.sh … --json`，退出码 0，`verdict: ok`），未采信此前任何贴过的数字。
- 逐块人判 8/8 全做（含块 7、块 8 两块最重的归属与时序核对）；词汇例句 30/30 逐字自核；语料层已把 `text/ch42_42.txt` 与 epub `s058-Chapter-042.xhtml` 逐字比对（仅页码 token 不同）——**无跨章搬句、无提取边界错**。
- 未读的项：**无**（md 全文 124 行、原文 261 行均已读完）。
