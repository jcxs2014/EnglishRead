# 3-diff.md · 《The Hexing Miss Helena》第 27 章 三张单子（R3）

受审：`notes/books/novels/the-hexing-miss-helena-by-darcy-mcguire/ch27 a new oath and a red dress.md`
参照：`text/ch27_chapter_27.txt`（395 行；末 12 行为出版社他书推广页，已剔除不引）
底稿：`1-suread.json`（40 条事件 / 10 组关系 / 4 处数字 / 3 处书内不一致 / 5 项悬置）｜机器层：`2-machine.json`（verdict `ok`，引语 13 / 14 段全中，块数 13）

取证方式：`/usr/bin/grep` 显式路径（`text/` 被 `.gitignore` 排除，`git grep` 与 rg 默认 ignore 恒空，退出码与「真查无」不可区分）。
**书内章号 ↔ 文件映射已逐个核过**：`text/ch25_chapter_25.txt` 首行 `Chapter 25`、`ch26_chapter_26.txt` → `Chapter 26`、`ch27_chapter_27.txt` → `Chapter 27`（与 md 的 H1 `# 25./# 26./# 27.` 一一对应，无偏移）。

---

## 一、漏（素读有、md 无）

| # | 原文事件 | 证据 | 判断 |
|---|---|---|---|
| L1 | 三人喝一杯白兰地庆祝希金斯太太获释 | `:240` `they all had a sniffer of brandy to celebrate.` | 收束小动作，未进分析层；只记 |
| L2 | 克洛伊的礼服细节：紫蕾丝紧身胸衣＋孔雀羽衬裙＋午夜发髻插真孔雀毛 | `:308-310` `The bodice comprised rich purple lace… peacock feathers.` | 与本章主线无关；只记 |
| L3 | 公爵夫人凑近辛西娅耳边说「这也给我一些以后可以跟你试试的主意」，海伦娜眼中银光一闪 | `:349-352` `She’s also given me some ideas to try with you later.’` | 收尾调情线，md 只写「背书」；只记 |
| L4 | 露台门是 French doors；两人走向门口时公爵夫人在盘问托马斯 | `:344-348` `towards the French doors opening onto the terrace` | 场景细节；只记 |

md 的导航与一句话总结已覆盖本章主线（立誓 → 赦免与退休 → 舞厅宣言 → 月下共舞），以上均为**非阻断**。

---

## 二、编（md 有、原文无 / 与原文冲突）

| # | md 原文（位置） | 原文逐字 | 判断 |
|---|---|---|---|
| E1 | `ch27 a new oath and a red dress.md:73` 为什么这样写：「"再飞一次"**回指其后第三自然段**两人离床三尺悬着又落回床垫的画面」 | `:125` `…realised they were hovering at least three feet above the bed.`；`:128` `In a weightless rush, they both fell back onto the mattress in a tangle of limbs…`；`:137` `'Silly witch.' … 'Let's see if I can make us fly again.'` | **阻断型（时序写反）**：悬空与落回在 `:125`/`:128`，**在**该引语（`:137`）**之前**；该引语是本段最后一句，其后是十五行空白与视角切换，根本不存在「其后第三自然段」。方向与段落计数两处皆错 |
| E2 | `:23` 为什么这样写：「最后一句"最大的傻子"**回接上一章**她把救援当成临终幻觉的误判」 | `text/ch25_chapter_25.txt:135` `She wasn’t dead yet. She was hallucinating. Why else would Cynthia be rushing across the fiendish room…`；`:141` `Yes. Definitely hallucinating. A proper lady like Cynthia Burrows would never use such coarse language.` | **阻断型（跨章指向错）**：幻觉/「正经夫人不会这么说话」在 **Chapter 25**，不是本章的上一章（Chapter 26）。Chapter 26 全文检索 `hallucin|dream|vision` 只命中 `:62`、`:89`、`:435`（他人视角的 vision），无海伦娜的幻觉误判 |
| E3 | `:63` 为什么这样写：「这与**上一章**海伦娜心里那句嘀咕——正经的布尔洛斯夫人绝不会这样说话——是同一次翻转的两面」 | 同上 `ch25:141`；`/usr/bin/grep -nE 'Lady Burrows' text/ch26_chapter_26.txt` → **rc=1（零命中）** | **阻断型（跨章指向错＋无据）**：Chapter 26 里 `Lady Burrows` 一次也没出现；该句在 Chapter 25 |
| E4 | `:73` 为什么这样写：「佛手柑**在上一章**是辛西娅靠风辨出爱人就在附近的信号」 | `text/ch25_chapter_25.txt:41` `The wind breathed over her, carrying with it the scent of bergamot. Helena was close.`；`/usr/bin/grep -nE 'bergamot|lemon balm' text/ch26_chapter_26.txt` → **rc=1（零命中）** | **阻断型（跨章指向错）**：风携佛手柑辨位在 **Chapter 25**；Chapter 26 无 bergamot/lemon balm |
| E5 | `:143` 为什么这样写：「"心跳同步"回收**上一章**辛西娅**隔着一栋楼**要找的那个节拍」 | `text/ch25_chapter_25.txt:41` `Her heart thumped painfully, straining for the rhythm of its mate.`（同段前句：`:33` `Cynthia stopped the carriage several streets away from 5 Bell Street.`） | **阻断型（跨章指向错＋无据细节）**：找节拍的动作在 **Chapter 25**；Chapter 26 检索 `rhythm\|mate\|beat\|heart\|pulse` 只命中 `:74`、`:315`、`:417`、`:471`，其中 `:417` 是两人同处时的 `Cynthia’s heart beat hard in her chest`，无「隔着一栋楼」 |
| E6 | `:43` 为什么这样写：「读者能逐句背诵，这也是**下一章**她能逐句回应的前提」 | `:56` `…'Helena, I will love you with my body. Seek you with my mind. Honour you with my spirit. And provide your heart sanctuary. Always.'` | **阻断型（跨章指向错）**：逐句回应发生在**同一章的下一段**（`:56`，即 md 自己的原句 4）；本章是全书末章，其后无「下一章」 |

> **簇**：E2–E5 是同一类缺陷（**相对章号指向错**：本章说「上一章」，实际在两章前的 Chapter 25），四处都指向同一段素材（`ch25:135`/`ch25:141`/`ch25:41`）；E6 是同一类缺陷的另一形态（把「下一段」写成「下一章」）。

---

## 三、错（两边都有但不一致）

| # | md 原文（位置） | 原文逐字 | 判断 |
|---|---|---|---|
| W1 | `:23` 「**四句话**里三句是失去的恐惧、一句是自我羞辱」 | `:38` 整句含 6 句言说：① `When I saw you lying on the floor of those baths…` ② `I can face death without fear, but living without you is impossible.` ③ `I love you, Cyn.` ④ `And I’m not afraid of that any more.` ⑤ `The only thing that scares me is losing you.` ⑥ `I’ve been the biggest fool.` | 计数不符（6 句，非 4 句）；「爱的宣言反而最短」成立。**提示型** |
| W2 | `:43` 「节奏**完全平行**……短、**无连接词**、无修饰」 | `:53` 第四句 `And provide your heart sanctuary for the rest of my days.` 以 `And` 起句且明显长于前三句 | 第四句有连接词、长度不齐。**提示型** |
| W3 | `:73` 「两人**离床三尺**悬着」（导航 `:10` 同款「离床三尺」） | `:125` `…hovering **at least** three feet above the bed.` | 漏 `at least`（至少）。**提示型** |
| W4 | `:83` 「本章里**两位女主都能以意念动物**」 | `:177` `Helena’s mouth went dry as the vase next to her began to swirl.`（归属刻意悬置）；本章辛西娅的施法只有 `:271` `she flicked her fingers at Lady Strathmore’s goblet of wine.` | 本章内海伦娜并无独立的「以意念动物」例证（花瓶那一处正被 md 自己说成刻意不明写）；断言超出本章证据。**提示型** |
| W5 | `:123` 「**最后两句都是**名词短语开头、无主语无动词」 | `:301` `But she refused to disappear. Because she possessed something far more valuable than their approval. Determination to live an authentic life, consequences be damned.` | 只有最后一句是无主语无动词的名词短语；倒数第二句有主语与谓语。**提示型** |
| W6 | `:10` 导航「辛西娅**抱出**沉重的礼服」 | `:174` `Cynthia swept into her dressing room and emerged a moment later, struggling under the weight of her gown.` | 她是**穿着**礼服走出更衣室，不是抱着走出。**提示型** |
| W7 | `:14` 叙事手法「誓词出现两次、逐字重复、**只改末词**」 | `:53` 第四句 `…And provide your heart sanctuary for the rest of my days.` → `:56` 第四句 `…And provide your heart sanctuary. Always.` | 改的不是「末词」，第四分句整句被替换（`for the rest of my days` → `Always`）；md 自己的原句 4 分析已如实写出这一改法。**提示型** |
| W8 | `:11` 情感弧线「三段的情绪颜色依次是热、痛、亮：卧室的暖光、**门厅**里白得吓人的脸、舞厅的煤气灯与钻石」 | `:162` `Will you have her meet us in the marchioness’ suite?`；`:174` `swept into her dressing room`；`:196` `The poor woman’s face had gone frighteningly pale.` | 白脸出现在**侯爵夫人套房／更衣室**，不是门厅（门厅只有管家开门）。**提示型** |
| W9 | `:13` 人物弧线「这是她**全书第一次**克制自己的能力」 | `:171` `Once more, she wished she could read Cynthia’s thoughts. She understood it might give her an unfair advantage, and balance was important…` | 最高级断言无据（全书是否首次克制，文本未建立）；可核的只是本章这一例。**提示型** |

---

## 四、书级形态（跨文件，非本章）

| # | 位置 | 事实 | 判断 |
|---|---|---|---|
| P1 | `ch10 the mirrored office.md:11` `00_概述.md:44` 用 **肯特米尔**；`ch02 the dead marquess.md:10` `ch11 the devils price.md:20` `ch27 …:10` 用 **肯特莫尔** | 原文同一头衔 `Marchioness of Kentmore`（`ch27:231`） | 同一专名两种译法（2 文件 vs 3 文件）。**提示型（术语统一）**，不判阻断 |
| P2 | `Strathmore` 只在 `text/ch27_chapter_27.txt` 出现 2 次 | `/usr/bin/grep -c 'Strathmore' text/ch*.txt` → 仅 ch27 为 2，其余 26 章 0 | 「斯特拉斯莫男爵夫人」是本章新出场人物，无跨章译名不一致问题。**不是缺陷** |

---

## 五、书内不一致（不裁决）

| # | 现象 | 判断 |
|---|---|---|
| S1 | `:183` `‘No. I’m dressing at Blair House.’` 与 `:235` `As Helena and Cynthia carried her ballgown across the threshold of Kentmore House together`（礼服自肯特莫尔宅抬出）之间的地点张力 | 原书自身如此，md 未就此断言，**不裁决** |
| S2 | `:177` 花瓶旋转的力量归属刻意悬置 | 原书刻意不明写，md 已在分析层如实标注，**不裁决** |
