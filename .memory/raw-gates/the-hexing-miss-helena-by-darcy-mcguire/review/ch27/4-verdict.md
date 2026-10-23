# 4-verdict.md · 《The Hexing Miss Helena》第 27 章 审查判定

审查员：主会话自审（**同会话盲区见文末**）｜章型：**末章（全书收束）＋ 三段视角切换章**
抽样理由：快审 `ceil(N/8)` = 4 章（首末必含、等距 1·10·18·27）；本章按「末章必含」入选，且是全书唯一一次三段视角＋十五行空白切换的收束章。
底稿：`1-suread.json`（40 条事件 / 10 组关系 / 4 处数字 / 3 处书内不一致 / 5 项悬置）→ `2-machine.json`（R2）→ `3-diff.md`（R3）
源：`text/ch27_chapter_27.txt`（395 行）｜受审：`ch27 a new oath and a red dress.md`（13 块 / 24 条词表）
**R2 退出码 0，verdict `ok`，13 条引语逐字命中（14 段独立取证），字符位 157→1103→1412→1559→4391→6124→7240→8321→9480→10086→12867→17934→18255 单调递增，无 `…`、无拼接。**

---

## 一、四组计数

| 组 | 计数 | 明细 |
|---|---|---|
| **逐字** | **引语 13 / 13 相符，0 错；词表 24 / 24 例句逐字回源命中** | `2-machine.json` 全部 `ok:true`；词表三档（9＋9＋6＝24 行）逐行取自本章 `text/`，脚本复核 24/24 命中（含 `sanctuary`/`unbreakable`/`quavered`… `terrace`） |
| **对应** | **13 块：13 对应，0 不对应，0 密度不足** | 逐块 R4 三问全部一致：原句 1–2 主体＝海伦娜；原句 3 说话人＝海伦娜（`ch27:53` 誓词）；原句 4 说话人＝辛西娅（`:56` 回应）；原句 5 说话人＝海伦娜（`:113`）；原句 6 说话人＝辛西娅（`:137`）；原句 7 主体＝海伦娜；原句 8 说话人＝辛西娅（`:198`）；原句 9 说话人＝辛西娅（`:225`）；原句 10 说话人＝辛西娅（`:237`）；原句 11 主体＝辛西娅（`:301`）；原句 12 说话人＝海伦娜（`:358`）；原句 13 主体＝两人＋哈姆雷特（`:364`）。**引语未截短** |
| **形态** | **4 / 4 符合，0 偏离** | H1 `# 27. Chapter Twenty-Seven` ✓｜导航 **5 项** = profile ✓｜子项 **中文理解／关键词／为什么这样写／读者视角提示** 13 块一致 ✓｜块数 **13** 超 `block_target [6,10]`（本章 3244 词）——但生产期已由用户拍板「末段章节沿用现状 12–13 块」，**有既定决策背书，不判偏离、不需写理由** |
| **断言** | **共核 73 条：相符 56 ／ 提示 9 ／ 阻断 6 ／ 跳过 2** | 提示 9 条＝措辞/计数级（详见判定表 W1–W9）；阻断 6 条＝时序写反 1 条＋相对章号指向错 5 条（同一簇）；跳过 2 条＝书内不一致，不裁决 |

**阻断型条数 = 6。**

---

## 二、判定表（断言 | 证据 | 结论 | 档位）

| # | 断言 | 证据（`text/<文件>:行`） | 结论 | 档位 |
|---|---|---|---|---|
| V1 | `:73` 「"再飞一次"**回指其后第三自然段**两人离床三尺悬着又落回床垫的画面」 | `:125` `…realised they were hovering at least three feet above the bed.`；`:128` `In a weightless rush, they both fell back onto the mattress in a tangle of limbs, Helena’s breasts crushed against Cynthia’s in delicious pressure.`；引语本体在 `:137` | 悬空/落回在引语**之前**；引语是本段末句，其后为十五行空白＋视角切换，不存在「其后第三自然段」 | **阻断**（时序写反） |
| V2 | `:23` 「最后一句"最大的傻子"回接**上一章**她把救援当成临终幻觉的误判」 | `text/ch25_chapter_25.txt:135` `She wasn’t dead yet. She was hallucinating. Why else would Cynthia be rushing across the fiendish room, mahogany hair streaming behind her like a cape…` | 幻觉误判在 **Chapter 25**（两章前），非上一章（Chapter 26）；`/usr/bin/grep -nE 'hallucin\|dream\|vision' text/ch26_chapter_26.txt` → 命中 `:62` `:89` `:435`（他人视角），无此内容 | **阻断**（相对章号指向错） |
| V3 | `:63` 「这与**上一章**海伦娜心里那句嘀咕——正经的布尔洛斯夫人绝不会这样说话」 | `text/ch25_chapter_25.txt:141` `Yes. Definitely hallucinating. A proper lady like Cynthia Burrows would never use such coarse language.`；`/usr/bin/grep -nE 'Lady Burrows' text/ch26_chapter_26.txt` → **rc=1（零命中）** | 该句在 Chapter 25；Chapter 26 无 `Lady Burrows` | **阻断**（相对章号指向错＋无据） |
| V4 | `:73` 「佛手柑**在上一章**是辛西娅靠风辨出爱人就在附近的信号」 | `text/ch25_chapter_25.txt:41` `The wind breathed over her, carrying with it the scent of bergamot. Helena was close.`；`/usr/bin/grep -nE 'bergamot\|lemon balm' text/ch26_chapter_26.txt` → **rc=1（零命中）** | 佛手柑＋风辨位在 Chapter 25 | **阻断**（相对章号指向错） |
| V5 | `:143` 「"心跳同步"回收**上一章**辛西娅**隔着一栋楼**要找的那个节拍」 | `text/ch25_chapter_25.txt:41` `Her heart thumped painfully, straining for the rhythm of its mate.`；`:33` `Cynthia stopped the carriage several streets away from 5 Bell Street.`；`text/ch26_chapter_26.txt:417` `Glancing at Helena, Cynthia’s heart beat hard in her chest.` | 找节拍在 Chapter 25（且是「几条街外」而非「隔着一栋楼」）；Chapter 26 只有同处时的 `:417` | **阻断**（相对章号指向错＋无据细节） |
| V6 | `:43` 「读者能逐句背诵，这也是**下一章**她能逐句回应的前提」 | `:56` `…'Helena, I will love you with my body. Seek you with my mind. Honour you with my spirit. And provide your heart sanctuary. Always.'` | 回应在同一章的下一段（md 自己的原句 4）；本章是全书末章，其后无下一章 | **阻断**（相对章号指向错） |
| V7 | `:23` 「**四句话**里三句是失去的恐惧、一句是自我羞辱」 | `:38` 含 6 句言说（见 `3-diff.md` W1 全文） | 计数错误（6 句）；「爱的宣言最短」成立 | **提示**（计数） |
| V8 | `:43` 「节奏**完全平行**……短、**无连接词**、无修饰」 | `:53` `And provide your heart sanctuary for the rest of my days.` | 第四句以 `And` 起句且长于前三句 | **提示**（措辞） |
| V9 | `:73`/`:10` 「离床三尺」 | `:125` `hovering **at least** three feet above the bed.` | 漏 `at least` | **提示**（措辞） |
| V10 | `:83` 「本章里**两位女主都能以意念动物**」 | `:177` `the vase next to her began to swirl.`（归属悬置）；`:271` `she flicked her fingers at Lady Strathmore’s goblet of wine.` | 本章内海伦娜无独立的以意念动物例证 | **提示**（超出本章证据） |
| V11 | `:123` 「**最后两句都是**名词短语开头、无主语无动词」 | `:301` `But she refused to disappear. Because she possessed something far more valuable than their approval. Determination to live an authentic life, consequences be damned.` | 只有最后一句符合 | **提示**（计数） |
| V12 | `:10` 「辛西娅**抱出**沉重的礼服」 | `:174` `Cynthia swept into her dressing room and emerged a moment later, struggling under the weight of her gown.` | 她是穿着走出更衣室 | **提示**（措辞） |
| V13 | `:14` 「誓词…逐字重复、**只改末词**」 | `:53` → `:56` 第四分句整句替换（`for the rest of my days` → `Always`） | 改的不是末词；md 自己的原句 4 分析已写对 | **提示**（措辞／自相矛盾） |
| V14 | `:11` 「**门厅**里白得吓人的脸」 | `:162` `Will you have her meet us in the marchioness’ suite?`；`:196` `The poor woman’s face had gone frighteningly pale.` | 白脸在套房／更衣室 | **提示**（场景名） |
| V15 | `:13` 「这是她**全书第一次**克制自己的能力」 | `:171` `Once more, she wished she could read Cynthia’s thoughts. She understood it might give her an unfair advantage…` | 最高级无据 | **提示**（无据最高级） |
| V16 | 书级：`ch10:11`、`00_概述.md:44` 作「肯特米尔」，`ch02:10`、`ch11:20`、`ch27:10` 作「肯特莫尔」 | `ch27:231` `My last act as Marchioness of Kentmore is to offer you a generous pension` | 同一头衔两种译名 | **提示**（术语统一，跨文件） |
| V17 | 书内不一致一：`ch27:183` `I'm dressing at Blair House.` 与 `:235` `carried her ballgown across the threshold of Kentmore House` | 同左 | 原书自身张力，md 未断言 | **跳过**（不裁决） |
| V18 | 书内不一致二：`ch27:177` 花瓶旋转的施事归属 | 同左 | 原书刻意悬置，md 已如实标注 | **跳过**（不裁决） |

### 与原文相符的 56 条断言（避免「只报问题」的不完整交代）

**A. 第一段 · 誓约**
1. 海伦娜把辛西娅带进自己房间、听见门锁响（`:35` `She heard the click of the lock`）✓
2. 「我看见你倒在那些浴室的地上，到处都是血」（`:38`）✓
3. 手臂在她腰上收紧（`:38` `her arms tightened around her waist`）✓
4. 灰眼里的银一直渗满整双眼睛（`:41` `she watched silver bleed into grey until her love’s eyes were glowing`）✓
5. 覆手在心口＋发抖的手指描过新的月牙＋「这样可以吗」（`:47`）✓
6. 辛西娅屏住呼吸、一顿一顿地点头（`:49` `She nodded in jerky movements.`）✓
7. 誓词四句、动词 爱／寻／敬／庇护（`:53`）✓
8. 想不起当年婚誓＝「尽职顺从中重复的空话」（`:56` `Empty words repeated in dutiful obedience.`）✓
9. 把结尾改成「永远」、称对方为「未来每一项事业上的伙伴」（`:56`）✓
10. 这些词把两颗灵捆成不可解的结合（`:59` `binding their spirits into an unbreakable union`）✓
11. 低吼「你是我的夫人，此刻与永远」（`:113`）✓
12. 高潮后两人离床悬空、落回床垫（`:125`/`:128`）✓
13. 佛手柑与香蜂草＝「如今于她已是家的气味」（`:137`）✓
14. 香蜂草曾用于混着迷迭香的咒烛（`text/ch20_chapter_20.txt:168`）✓
15. 「看看我能不能让我们再飞一次」（`:137`）✓

**B. 第二段 · 希金斯太太**
16. 两人已站在辛西娅宅门前台阶（`:153` `on the front steps of Cynthia’s home`）✓
17. 「我要同希金斯太太谈」（`:156`）✓
18. 管家开门时眼睛睁大（`:161` `his eyes widening at the sight of both women`）✓
19. 海伦娜希望自己能读辛西娅的心思、又明白那是不公平的优势（`:171`）✓
20. 「我等不及要离开这栋房子，和你开始新生活」（`:174`）✓
21. 海伦娜口干、花瓶旋转、「爱不断用它的美把她惊到」（`:177`）✓
22. 希金斯太太双手紧扣在身前（`:185` `her hands clasped tightly in front of her`）✓
23. 「她知道」直接映进海伦娜脑中（`:189` `Mrs Higgins’ terrified thoughts echoed in Helena’s head`）✓
24. 老太太僵在屋子中间、要自首苏格兰场、不让别的女孩再受害（`:192`）✓
25. 「我请你来不是为了对质，而是为了道谢——为了做了我做不到的那件事」（`:198`）✓
26. 「爱的另一面」（`:200-201` `This was the other side of love.`）✓
27. 告诉警司休伯特是自杀、辛克莱不会出卖（`:207`；谎在 `text/ch26_chapter_26.txt:249` `‘Hubert killed himself.’`）✓
28. 撞见休伯特对波莉动手、拿走拆信刀、尖叫他不停（`:210`；掐住见 `text/ch26_chapter_26.txt:311` `She caught him strangling one of the poor girls…`）✓
29. 「我将为我的罪在地狱里燃烧」（`:213`）✓
30. 「保护无辜者不是罪」（`:216`）✓
31. 哈姆雷特把身体贴上老太太的腿（`:220`）✓
32. 「你结果休伯特性命时也把我放了，现在轮到我为你做同一件事」（`:225`）✓
33. 以侯爵夫人身份给退休金、海边小屋（`:231`）✓
34. 事务律师安排退休面谈（`:239`）✓
35. 「我不再是布尔洛斯夫人……我们都是自由的」（`:237`）✓
36. 抬裙过门槛、「最后一次走出这道门」（`:235`）✓

**C. 第三段 · 舞厅**
37. 三句闲话独立成段（`:262-268`）✓
38. 弹指让红酒泼上前襟（`:271`）✓
39. 哈姆雷特心里说「他们注意到了我……不敢招惹她的怒气」（`:283`）✓
40. 公爵夫人买裙请她制造丑闻（`:289`）✓
41. 红裙是守寡第一个月最不该穿的衣服（`:292`）✓
42. 一周前她只想让上流社会滚蛋（`:295`）✓
43. 海蓝礼服如水流过皮肤（`:298` `flowed over her skin like water`）✓
44. 预备一种新的女士／顺从祭坛／拒绝消失（`:301`）✓
45. 芒特罗街联排宅改作避难所（`:304`）✓
46. 托马斯为流言动怒（`:309-310`）✓
47. 公爵夫人「只有蠢货才……」（`:338`）✓
48. 火女巫送来一阵热风（`:343`）✓
49. 露台独白＋「我爱海伦娜·布莱尔到余生尽头」（`:355`）✓
50. 以月光为证、夜莺为乐邀舞（`:358`）✓
51. 哈姆雷特像哨兵、心跳同步、只奏给两人的旋律（`:364`）✓
52. 出版社他书推广页已剔除不引（`:384-395`）✓

**D. 跨章与场景**
53. 第一段发生在布莱尔宅卧房（`text/ch26_chapter_26.txt:276` `they all departed for Blair House.` ＋ `ch27:35` `Helena led Cynthia into her room.`）✓
54. 月牙伤痕出自上一章（`text/ch26_chapter_26.txt:185` `save a crescent moon in hawthorn-berry red`）✓
55. 希金斯太太在上一章只被提及、未登场（`text/ch26_chapter_26.txt:237`、`:309`）✓
56. `Marchioness of Kentmore`＝肯特莫尔侯爵夫人（`:231`）✓

### 机器层

- `chapter.sh --json`：退出码 0，verdict `ok`，`segment_miss=0`、`cjk_low=0`、`keyword_bad=0`、`struct_bad=0`、`quote_long=0`、`template=0`、`hole=0`、`block_count=0`。
- 本章词表 24 行例句逐行回源命中（脚本自建复核，见 `3-diff.md` 之外的临时脚本 `/tmp/hex_vocab_ch27.py`，未入库）。
- 全书级 `check_vocab` 的 11 条 WARN 中，本章无一条（`threshold` 在本章列为 ⭐⭐ 进阶，合规）。

---

## 三、已核实为正确（防误修，下一轮不得以「读着不对」为由改动）

1. **导航「老太太哭说到她撞见休伯特掐住波莉」——成立，不要改成「撞见休伯特和波莉在一起」。** 依据：`ch27:210` `when I saw him with Polly… I screamed for him to stop, and he wouldn’t.` ＋ `text/ch26_chapter_26.txt:311` `She caught him strangling one of the poor girls…`（辛西娅对克莱奥转述）。「掐住」来自 Chapter 26 的动词，「波莉」来自 Chapter 27 的点名，md 的跨章合成**有据**，不得改弱。
2. **导航「第一段在布莱尔宅的卧房里」——成立。** 依据：`text/ch26_chapter_26.txt:276` `…they all departed for Blair House.` ＋ `ch27:35` `Helena led Cynthia into her room.`（上一章结尾正是在布莱尔宅上楼休息）。
3. **叙事手法「三段以十五行空白切换视角」——成立。** 依据：`ch27:138-152` 与 `:244-258` 两处各 15 行空白，切换点分别是 `:137`（"让我们再飞一次"）与 `:235`（抬裙过门槛），**交接点确实落在动作之后、说明之前**。
4. **叙事手法「裸行心声独立成段、不加引号」——成立。** 依据：`:189` `Dear God. She knows.`、`:213` `I shall burn in hell for my crimes.`、`:283` `They’ve noticed me. They just don’t dare court my wrath.` 三处均无引号、独立成段。
5. **「上一章她在众人面前那句谎」三处（`:93`/`:103`/`:113`）——成立，章号正确。** 依据：`text/ch26_chapter_26.txt:249` `‘Hubert killed himself.’` —— 谎确实是在上一章（Chapter 26）对警司说的；不要与 V2–V5 一起改。
6. **「上一章那道伤口」（`:33`）——成立。** 依据：`text/ch26_chapter_26.txt:185` `save a crescent moon in hawthorn-berry red`。
7. **原句 9「接的是上一段『你救了那个女孩的命』」——成立。** 依据：`ch27:218` `‘You said yourself, he wouldn’t stop. You saved Polly’s life.’`。
8. **人物弧线「希金斯太太从上一章一句被提及的名字」——成立。** 依据：`text/ch26_chapter_26.txt:237`、`:309` 两处均为**提及**，她本人全章未登场；md 的说法（「被提及的名字」而非「在场的人物」）与原文一致。

---

## 四、覆盖声明与已知盲区

- **本章覆盖**：R1（先素读 `text/ch27_chapter_27.txt` 全 395 行，写完 `1-suread.json`）→ R2 → R3 → R4（13/13 块）→ R5，**全流程走完**。
- **全书覆盖**：机器层 27/27 章；人判 **ch01 / ch10 / ch18 / ch27 = 4 / 27 章**；其余 23 章**仅机器层**；总览三篇全篇另行人判。
- **同会话盲区（如实标注）**：本书由本会话在写作期产出；**ch27 的 `text/` 在写作期读过**（写作期回读过 ch01/ch05/ch09/ch12/ch16/ch17/ch18/ch22/ch25/ch26/ch27），故本章**非完全盲态**；本章结论以「先素读后开 md」的顺序纪律执行，独立性低于未读过的 ch10。
- **取证纪律**：所有「查无」均用 `/usr/bin/grep` 显式路径并记录退出码；未使用 `git grep`（`text/` 被 `.gitignore` 排除，其退出码 1 与「真查无」不可区分）。
- **未做**：深审 R0–R5 全章未执行；**快审升级条件（§0 第 1 条「≥3 条阻断」）已命中**（ch18 3 条 + ch27 6 条），须提请用户确认是否升级，**本会话不自行升级**。
