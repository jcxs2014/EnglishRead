# R5 判定表 · ch45（Priory Square）

- 权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch45_45.txt`
- 受审 md：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch45 the missing volume is found at priory square.md`
- 证据列格式：`ch45:<行>[<起-止字符>]`（原文字符区间）+ 原文逐字；`md:<行>`＝精读 md 行号
- 本次为**独立异实例审查**：R1 素读（`1-suread.json`）先落盘 → 再开 md；R2 机器层独立跑；R3/R4/R5 全部落盘在本目录。
- **覆盖声明**：本次只审第 45 章。本书其余 53 章**只有机器层**（`scripts/chapter.sh` 全书门禁），**不得记作「通过」**；本章结论不可外推到全书。

---

## 一、四组数（只报这四组）

| 组 | 计数 | 说明 |
|---|---|---|
| **逐字** | **7 / 7 ✅** | 7 条引语在 `text/ch45_45.txt` 中**连续逐字命中**（本人用 Python 归一化引号后独立 substring 复核，不复用门禁输出）；无省略号拼接、无跨话轮缝合、无跨章搬句。`scripts/verify_fragments_indep.py` 全书 782 条 / 850 片段 MISS 0、拼接未标省略号 0。**本组阻断 0** |
| **对应** | **6 / 7 块成立，1 块不成立**；总结层另 1 处不成立 → **本组阻断 2** | 不成立块＝原句 1（施事反转，见下 A1）；总结层不成立＝一句话总结把「假 Isolde」拆成两姐妹（A2） |
| **形态** | **0 偏离**（H1／导航／子项／块数四项全对）→ **本组阻断 0** | 见下「三、形态组」 |
| **断言** | 人工断言 **20 条：阻断 6、提示 14**；数字/日期 **14/14 全对**（阻断 0）；词汇例句 **29/29 逐字命中**（阻断 0） | 阻断 6 条＝A1、A2、B1、B2、B3、C1 |

**阻断型合计：6 条。**

---

## 二、断言判定表（逐条）

| # | 断言 | 证据（章:区间 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | md:20「罗比紧跟着蒂尼·西姆走上 35 号 Priory Square 的台阶」 | ch45:20[36-380]：`Robbie, closely followed by Tiny Simm who had been standing outside the Horatio Combe Institute while forensics trooped in and out all morning, was traipsing up the steps to 35 Priory Square.` | 原文＝Tiny Simm 紧跟 Robbie 身后；md 写成罗比跟在后，**跟随方向写反**，并凭空造出「两人从博物馆一起走来」的场景 | **阻断** |
| A2 | md:136「把「假 Isolde」拆成台上那张脸和台上的声音」 | ch45:153[7783-7867]：`‘She has to be “fake Isolde”,’ Matt said, taking a couple of evidence bags from Amy.`／ch45:54[2182-2667]：`…someone who was calculating enough to steal someone’s identity, dress up as Digby’s intern to enter the building and use a PO Box…`／ch45:78[3314-3427]：`‘So Eulalia, this dodgy popstar, is our little fanfic perv who stole that Isolde woman’s identity?’ Robbie asked.` | 原文「fake Isolde」处处**单数**，最终定性落在**一个人**（Jennifer Parkin）；Mel 是姐妹、是幕后有才华的那个，**不是冒名者本人**。md 把它拆成两个人，且与 md:10 自相矛盾 | **阻断** |
| B1 | md:12「那滩血则是这间屋子在夜里被人破门而入的结果」 | ch45:32[945-1470]：`They had to wait for an officer with an enforcer to appear and batter down the front door.`／ch45:96[3649-3833]：`‘She was just about breathing when we broke the door down. Her sister did this then.’` | 原文没有「夜里破门而入」这件事（门是白天被警方撞开的）；血泊是姐姐袭击妹妹的结果 | **阻断** |
| B2 | md:12「梳妆台抽屉里的奥氮平与锂」 | ch45:108[4906-5058]：`‘I found these in a drawer in Mel’s room.’ Amy walked in holding two packets of medication. ‘Olanzapine and lithium. All prescribed to Jennifer Parkin.’`／ch45:156[7870-8470]：`She turned to a huge pile of letters on the dressing table.` | 原文＝**Mel 房间**的抽屉；梳妆台在 **Jennifer 房间**（堆的是粉丝信）。地点与受事方向都反 | **阻断** |
| B3 | md:12「说明住在这屋里的两姐妹正各自被药物绑住」 | ch45:108[4906-5058]：`‘Olanzapine and lithium. All prescribed to Jennifer Parkin.’`／ch45:114[5241-5277]：`‘Mel had control of her medication.’`／ch45:117[5280-5368]：`‘Mel’s either really controlling or Jennifer sometimes comes off it when she shouldn’t.’` | 原文只有 Jennifer 一人服药、Mel 掌握药量；md 凭空给 Mel 也安上药物，抹平「谁控制谁」的方向 | **阻断** |
| C1 | md:10／md:136 全篇不点名倒地者与行凶者 | ch45:45[1753-1960]：`‘Melissa Parkin,’ Matt said, picking up an electricity bill from a side table in the hallway. … ‘Daughter of Beverley and Nigel Parkin of Harrogate.’`／ch45:93[3607-3646]：`‘How long was Mel down here like that?’`／ch45:96[3649-3833]：`‘She was just about breathing when we broke the door down. Her sister did this then.’`／ch45:99[3836-3930]：`‘Jennifer,’ Amy said, picking up another piece of post from the side table. ‘Jennifer Parkin.’` | 关键事件与身份枢纽在分析层缺失：「Melissa Parkin」全 md 只在词汇表例句出现 1 次（md:126），导航与总结两处以「年轻女子」代替。本章专属判据 ① 不成立 | **阻断**（漏） |
| A3 | md:40「尸体底下那摊新鲜的血」 | ch45:29[797-942]：`The pool of fresh blood under the body was glistening.`／ch45:96[3649-3833]：`‘She was just about breathing when we broke the door down. Her sister did this then.’` | 原文 `the body` 中性，人昏迷未死；md 写成「尸体」＝把状态写成确认，且与 md:46「这具身体」自相矛盾 | 提示 |
| A4 | md:70「她想停药就停，而且背着精神科医生」 | ch45:123[5435-6080]：`Her coming off some quite heavy antipsychotics whenever she fancied without a psychiatrist being involved would make her a massive liability.`／ch45:117[5280-5368]：`‘Mel’s either really controlling or Jennifer sometimes comes off it when she shouldn’t.’` | 原文是 Matt 的假设推演，且本章明说是二择一；md 写成既成事实 | 提示 |
| A5 | md:70「那会让**姐姐**变成一个巨大的麻烦；Mel 依赖着**姐姐**」 | ch45:123[5435-6080]：`Mel’s dependent on her. Well, they’re codependent. … Her career is reliant on her sister acting as the physical embodiment of her musical talent.` | 身份方向对（停药者/被依赖者＝Jennifer，Mel 依赖 Jennifer）；但 ch45 全文未给姐妹长幼，md 的「姐姐」是加出来的，且按 `her sister`（指 Mel）直译则与 md 自己的指派冲突 | 提示 |
| A6 | md:13「Amy … 把冒名者钉死」 | ch45:153[7783-7867]：`‘She has to be “fake Isolde”,’ Matt said, taking a couple of evidence bags from Amy.`／ch45:147[7421-7563]：`‘Jennifer was stalking Willow too?’ Amy put the cardigan in an evidence bag.` | 定性出自 Matt；Amy 的贡献是装袋与追问 | 提示 |
| A7 | md:30 原句 2 的句内次序 | ch45:26[571-794]：`‘Sir, there’s someone unconscious on the floor.’ He stepped out of the way for Robbie to see and called for back-up.` | 原文先报信、再让位、再叫人增援；md 把台词挪到末尾（说话人归属正确） | 提示 |
| A8 | md:11「Robbie 负责破门与调度」 | ch45:32[945-1470]：`They had to wait for an officer with an enforcer to appear and batter down the front door.` | 撞门的是持 enforcer 的警员；Robbie 只叫了增援并自己试撞（原文写明是 `for appearance’s sake`） | 提示 |
| A9 | md:11「屋里只剩 Matt 与 Amy 在场」 | ch45:102[3933-4094]：`‘Let’s spread out. See if we can find something that tells us where she might be right now,’ Robbie said, before heading down the stairs to the recording studio.` | 原文只交代 Robbie 下楼，Tiny Simm 去向未写；「只剩」属推断 | 提示 |
| A10 | md:54「她赌的是没人会把一张在 M&S Food 丢掉的卡和一封来信放到一起看」 | ch45:51[1987-2179]：`She told me she’d lost it in M&S Food and had stupidly left the PIN with it on a piece of paper.` | 丢卡是 Beverley 说的，原文没有「冒名者故意留卡」这层意图 | 提示 |
| A11 | md:80「混血流行歌手」 | ch45:156[7870-8470]：`She flicked through, merely glancing at their adoration for the hybrid popstar.` | `hybrid` 宜作「混合／双人组合」，「混血」易读成血统混血 | 提示 |
| A12 | md:12「四样东西串成一条链」后列五项、「血」出现两次 | ch45:29[797-942]／ch45:96[3649-3833]（血泊只有一处，原文是同一滩） | 清单自身不自洽，与 B1 同处一句，修 B1 时一并整理 | 提示 |
| B4 | md:10「顺着遗落的一张信用卡」 | ch45:51[1987-2179]：`She told me she’d lost it in M&S Food and had stupidly left the PIN with it on a piece of paper.` | 卡不是现场遗落物（是 Beverley 说丢在 M&S Food）；警方在现场只找到电费单与信件 | 提示 |
| B5 | md:20「Horatio Combe 博物馆」 | ch45:20[36-380]：`…standing outside the Horatio Combe Institute…` | 原文是 Institute，md 改称博物馆 | 提示 |
| C2 | 逃逸线索与若干物证未进分析层 | ch45:105[4097-4903]：`There was also a booking – please pay £60 in cash on arrival – from a taxi firm that she’d ordered forty-five minutes ago.`／ch45:150[7566-7780]：`Matt bent down and picked up a tote from The Purple Toad Bakery and a cheap brunette wig cut into a bob.` | 出租车预订（£60 现金／四十五分钟前下单）、PO Box 确认邮件、论坛登录、带血棉花球、假发、布袋均未进分析层；「谁在逃」是本章身份结论的支点 | 提示（漏） |
| C3 | 「谁在台上、谁在幕后」的依据未进分析层 | ch45:75[3158-3311]：`‘Possibly. Caius and Callie think that Mel was actually the one with the musical talent and that’s why Eulalia performs in those bobbleheads,’ Matt said.`／ch45:69[2947-3114]：`‘Callie was hired by Eulalia to do some creative consulting over the last week. Mel, her sister, is her manager. Eulalia was apparently desperate to work with Callie.’` | md:74 直接使用「台前／台后」这组概念而未给依据；Callie、memes 这条线全章未进分析层 | 提示（漏） |
| D1 | md:12「能确证的只有藏匿者身份（那个以「假 Isolde」之名做过实习生、因此进得去那栋楼的人）与藏匿地点（Jennifer 房间梳妆台上的信堆）」 | ch45:156[7870-8470]：`Amy sealed the cardigan up and began looking through Jennifer’s bookshelf. … She moved a drawing of Eulalia wearing a mermaid bobblehead straddling a very suggestive dolphin and found it. ‘Matt, it’s here. The missing volume.’` | 藏匿**地点**与原文完全一致（Jennifer 房间梳妆台／信堆／海豚画下）✅；藏匿**者**指向 Jennifer 也与 ch45:153 的单数定性一致 ✅；但原文并未明写藏者，md 用「能确证」过强 | 提示（措辞） |

---

## 三、形态组（H1／导航项／子项集／块数）

`bash scripts/bookform.py notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell` 输出：
`H1 写法：{'N.': 54}`｜`导航项（众数，5 项）：一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法`｜`子项集（众数，4 项）：中文理解 / 关键词 / 为什么这样写 / 读者视角提示`｜`每章块数：中位 7.0，范围 5–10`｜`体裁 profile：mystery-thriller`

| 维度 | 本章实测 | 本书众数 / profile | 偏离 |
|---|---|---|---|
| H1 | `45. Priory Square`（md:7） | `N.` 写法（54/54） | 无 |
| 导航项 | 5（md:10–14：一句话概括／视角／线索结构／人物弧线／叙事手法） | 众数 5，项名全同 | 无 |
| 子项集 | 4（中文理解／关键词／为什么这样写／读者视角提示） | 众数 4 ＝ profile 子项 4 | 无 |
| 块数 | 7（原句 1–7） | 中位 7.0，范围 5–10 | 无 |

**形态组：无偏离，无需理由行。**（`chapter.sh --json` 的 `form` 段独立给出同一结论：`h1_shape_ok: true`、`nav_count_ok: true`、`blocks: 7 = block_median 7.0`。）

## 四、机器层与独立取证记录

```
bash scripts/chapter.sh "<书目录>/ch45 the missing volume is found at priory square.md" --json > 2-machine.json
  → 退出码 0
  → quotes 7/7 ok；counts: blocks 7, segments 7, segment_miss 0, struct_bad 0, empty_quote 0, keyword_bad 0, cjk_low 0
  → issues: struct/empty_quote/keyword/cjk 全空
python3 scripts/verify_fragments_indep.py "<书目录>"
  → 引语 782 条 ｜受检片段 850 ｜MISS 0 ｜拼接未标省略号 0 ｜缺参照章 0（ch45 在内，无报警）
python3 scripts/bookform.py "<书目录>"     → 见上表
本人独立复核（不依赖门禁输出）：
  · 7 条引语归一化引号后 substring 判定 → 全部连续命中，位置 36 / 571 / 797 / 1987 / 5062 / 5560 / 8161
  · 29 条词汇例句逐条 substring 判定 → 全部命中本章原文（表头 3 行除外）
  · 14 个数字/日期逐条比对原文 → 全对
```

> ⚠️ **机器全绿 ≠ 无缺陷**：本任务预告的盲区（施事/受事/归属写反）在本章实际发生 1 例（A1），且四道探针对 A1、A2、B1–B3、C1 **全部无感**。

## 五、已核实为正确（防误修，不得以「读着不对」为由改动）

| 写法 | 原文逐字 | 判定 |
|---|---|---|
| md:70「Mel 依赖着姐姐…她们是相互依赖的」——**依赖方向** | ch45:123[5435-6080]：`Mel’s dependent on her. Well, they’re codependent.`（`her` ＝ Jennifer） | 方向正确：Mel 依赖 Jennifer；原文未写反。**「姐姐」二字另见 A5（提示）** |
| md:74「台前的人需要台后的人撑住自己，台后的人又需要台前的人继续唱下去」 | ch45:123[5435-6080]：`If Caius and Callie are right, and Mel’s the talent and Jennifer is the face, then Mel needs Jennifer to keep it together. … Her career is reliant on her sister acting as the physical embodiment of her musical talent.` | 台前＝Jennifer（the face）、台后＝Mel（the talent），指派与原文一致（依据句在引语外，属引语选短，非事实错） |
| md:11「发现的那一刻…诸人的反应只有 Amy 朝着 Matt 喊出的那一句，本章也在这一句上收住」 | ch45:156[7870-8470] 末：`‘Matt, it’s here. The missing volume.’` | 原文确无他人反应描写，章末即停在此句 ⇒ md 未编造「众人震动/欢呼」之类 |
| md:12 藏匿地点「Jennifer 房间梳妆台上的信堆」 | ch45:156[7870-8470]：`…began looking through Jennifer’s bookshelf. … She turned to a huge pile of letters on the dressing table. They were from fans. … She moved a drawing of Eulalia wearing a mermaid bobblehead straddling a very suggestive dolphin and found it.` | 地点**完全一致**（Jennifer 房间／梳妆台／粉丝信堆／海豚画下）——本章专属判据 ④ 之「地点」项成立 |
| md:84／md:86「她把它压在了画下面」「从一堆信底下挪开一张画——藏它的人把它塞进了自己那套追星收藏里」 | 同上 `She moved a drawing … and found it.` | 与原文动作一致（先挪画后得物） |
| md:10「把「假 Isolde」的真实身份指向这栋房子里的女人杰妮弗」 | ch45:153[7783-7867]：`‘She has to be “fake Isolde”,’ Matt said…`；ch45:105[4097-4903]：`He found a confirmation for the PO Box buried amongst the thousands of unopened emails.` | 单数定性，落点 Jennifer ⇒ **与 md:136 自相矛盾（见 A2）**，但本句本身正确 |
| md:60 原句 5「这剂量可不小…双相障碍，也可能带分裂情感性特征」 | ch45:111[5061-5238]：`Matt looked up. ‘That’s a lot. An antipsychotic and a mood stabiliser.’ … ‘I’d say she’s bipolar or possibly schizoaffective.’` | 逐字对应无误 |
| md:80 原句 7「挪开一张画：画上是戴着美人鱼摇头娃娃、跨骑在一头很挑逗的海豚上的 Eulalia——就在画下面，她找到了它」 | ch45:156[7870-8470]：`She moved a drawing of Eulalia wearing a mermaid bobblehead straddling a very suggestive dolphin and found it.` | 画中形象与「挪开画→找到」的动作还原准确 |
| md:14「敲三下、撬不开、等增援、撞开」 | ch45:20[36-380]：`Robbie knocked on the door, and then harder a second time.`／ch45:23[383-568]：`He banged again a third time to no avail.`／ch45:32[945-1470] | 四拍全部对上 |
| md:50 原句 4「是用 Beverley 的信用卡买的；她说自己把卡丢在了 M&S Food，还蠢到把 PIN 码写在纸条上，跟卡一起留着」 | ch45:51[1987-2179] | 归属方向对（卡属 Beverley、丢卡的是 Beverley）；与 A10 的「赌注」解读不同层，不算错 |
| 全部 29 条词汇例句 | 见 `2-machine.json` ＋本人 substring 复核 | 逐字命中，无手写编造、无跨章例句 |
| 全部 14 个数字/日期（35 Priory Square / six feet five / five minutes / last week / sixtieth / an hour ago / £60 / forty-five minutes / two packets / thousands of emails / last night …） | 见 `1-suread.json` 数字表 | 逐字一致，无数字漂移 |

## 六、给修复方的最小改动清单（不属审查结论，供后续处理）

1. md:20：`罗比紧跟着蒂尼·西姆` → 改为「Tiny Simm 紧跟在 Robbie 身后」；`Horatio Combe 博物馆` → `Horatio Combe Institute`。
2. md:136：删掉「拆成台上那张脸和台上的声音」，改为「指向这栋房子里的女人杰妮弗」（与 md:10 一致）。
3. md:12：删「那滩血则是这间屋子在夜里被人破门而入的结果」；「梳妆台抽屉里的奥氮平与锂」→「Mel 房间抽屉里的」；「两姐妹正各自被药物绑住」→「只有 Jennifer 服药、Mel 掌握她的药量」；「四样东西」与清单条目数对齐。
4. md:10 / md:136 / 精读层：补上倒地者 **Melissa Parkin（Mel）** 与行凶者 **Jennifer Parkin**（原文 `Her sister did this then` / `Jennifer Parkin`）。
5. md:70：把「她想停药就停」改成 Matt 的假设推演；「姐姐」改为不指定长幼的「姐妹中的另一个／Jennifer」。
6. md:11 / md:13：破门归给持 enforcer 的警员；「把冒名者钉死」改回 Matt。
