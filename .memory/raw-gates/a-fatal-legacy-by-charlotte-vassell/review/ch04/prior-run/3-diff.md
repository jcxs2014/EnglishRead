# 3-diff.md · ch04 三张单子（漏 / 编 / 错）

- 书：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell`
- 章：`ch04 digbys studio is searched.md`
- 唯一权威源：`text/ch04_4.txt`（4178 字符 / 98 行）
- 审查方：独立审查员（只负责第 4 章）；**只写本目录，未改书目录任何 md，未 git add/commit**
- 取证口径：全部用**显式文件路径** + `/usr/bin/grep`（`-E` 交替、`-w` 单词），命令与退出码见文末「取证三件套」。

---

## 一、漏（素读有、md 无）

### L1 · 明信片整段缺席（提示）
- **原文**：`text/ch04_4.txt:56`
  > Caius wandered over to the fridge. Inspecting a postcard of a Goan beach clinging to the front of it, he took it down. ‘Darling, meant to write when in Blighty but had mad rush for visa. Let’s talk about the Institute when I get back on 27th. Mum x.’ Caius turned to a half-height bookcase near the bed. A wooden box with a rose carved into the side had caught his eye. He opened it. It contained a month’s worth of frequent correspondence.
- **md**：`ch04 digbys studio is searched.md` 全文**无**「明信片 / postcard / Blighty / Institute / 27th / Mum」任何一项（`grep -nE '明信片|postcard|Blighty|Institute|27th|Mum'` → 命中 0，仅 `## 本章词汇` 之外的词条表里有 `postcard | 明信片` 一行例句，但例句只作词汇样例，未进入分析层）。
- **判**：这是全章**唯一**带具体日期（`27th`）与机构名（`the Institute`）的物件，也是全章唯一来自「母亲」一线的信件；md 导航的「线索结构」自称列出物证清单却未含它。**提示级**（不构成情节转折缺失，故不判阻断）。

### L2 · Isolde 动机的三个选项与 Willow 一线未进分析层（提示）
- **原文**：`text/ch04_4.txt:71`（Caius 用信反驳逃走的合理性）／`:74`（`‘Isolde could be married? She doesn’t want to get caught on a date.’`）／`:77`（`‘Or maybe she’s broken her curfew? He hit on Willow the intern; she’s twenty, twenty-one. Maybe nineteen when she started.’`）／`:83`（`‘It’s a PO Box,’ Caius said.`）
- **md**：`ch04 …md:13` 只写到「关系（通信对象 Isolde、只有一个邮政信箱的地址）→ 案情假说（毒芹误入沙拉，还是约会对象事后逃走）」；**已婚 / 宵禁 / Willow 被搭讪与年龄 / 「有感情就不会跑」的反驳**均未出现。
- **判**：md 保留了假说主干（逃走的可能），但把 Caius 的**论证结构**（因为信温情、两人已通信一段时间，所以逃走不合理）压成了并列二选一。**提示级**。

### L3 · 「年代滞后」的闲谈段（memes / tutu corgi / Amy）未进分析层（跳过—已被块 3 覆盖）
- **原文**：`text/ch04_4.txt:44`（`‘There are no memes in Digby’s world.’`）、`:47`（`‘Mate, it’ll be over in a week. Someone will put a tutu on a corgi.’ Matt wasn’t sure that was true.`）、`:50`、`:53`（`‘That’s all right, Amy is.’`）
- **md**：`ch04 …md:38` 已在块 3「读者视角提示」里把「时代滞后」作为孤独底色写出，主题上覆盖。**不判缺陷**（记为已覆盖，避免重复计漏）。

---

## 二、编（md 有、原文无）

### B1 · 标本（cross-eyed taxidermy kangaroo）被断言「安置在抽屉里」——**阻断**
- **md**：`ch04 digbys studio is searched.md:30`
  > **为什么这样写**：抽屉一拉开就撞见一只标本——他把收藏的癖好带回了住处，**那只标本被安置在这间极简小屋的抽屉里**；"斜着眼"的标本配上一尘不染的房间，是用喜剧口吻写出一个把公共收藏品与私人洁癖混着过日子的怪人。
- **原文**：`text/ch04_4.txt:26`（逐字）
  > ‘Makes sense,’ Caius said, opening Digby’s sock drawer. ‘If I had to see that cross-eyed taxidermy kangaroo every day I’d want to live in an immaculate little minimalist box too. It smells like beeswax. I bet he polished the place with a toothbrush every week.’
- **判**：原文只写 Caius **打开袜子抽屉**，随即就那只标本开了一句玩笑；**原文从未交代标本放在哪里**（`grep -nE 'kangaroo|taxidermy' text/ch04_4.txt` → 仅 `:26` 一处命中）。md 却把它定位成「抽屉里的标本」并写「抽屉一拉开就撞见一只标本」。**md 有、原文无 ⇒ 编 ⇒ 阻断**（且与 B2 同源：把「抽屉」当成本章通用容器）。

### B2 · 标本被断言为「公共收藏品 / 博物馆的碎片」——**提示**
- **md**：`ch04 …md:30`（`把公共收藏品与私人洁癖混着过日子的怪人`）、`:31`（`他的私人生活里仍然装着博物馆的碎片`）
- **原文**：`text/ch04_4.txt:26` 只有 `cross-eyed taxidermy kangaroo`；全章无「博物馆藏品 / 馆藏 / 借展」字样（`grep -nE 'museum|museums' text/ch04_4.txt` → 命中 1，见 `:65` 的 `does it at the museum`，指的是**约会地点**而非标本来源）。
- **判**：把个人标本判为公共馆藏，原文无据。属推论越界，**提示级**（同一段已因 B1 判阻断，此条不重复计阻断）。

### B3 · 「不能联网的老电视」——提示
- **md**：`ch04 …md:14`
  > 抽屉上摆着一台**不能联网**的老电视
- **原文**：`text/ch04_4.txt:38`（逐字）
  > ‘Yeah. I’m wondering. There’s an old TV that wouldn’t be able to **stream** on top of the drawers and a radio in the kitchenette but no laptop.’
- **判**：原文说的是「不能串流（影音服务）」，且该句的对比落点是 **no laptop**；「不能联网」是另一个事实断言。**提示级**（措辞改写）。

### B4 · 「剪报 / 登报」把媒介从「杂志」改成报纸味——提示
- **md**：`ch04 …md:11`（`一张交友广告剪报`）、`:13`（`杂志剪报`）、`:14`（`他孤独到需要**登报**找人`）、`:49`（`**剪报**上写着`）；而 `:100` 词表又写 `magazine | 杂志`
- **原文**：`text/ch04_4.txt:89`（逐字）
  > ‘Digby’s definitely not the Hinge type.’ Caius took the other letters out of the box. **A cut-out from a magazine was at the back.** ‘“North London romantic seeks connection with fellow old soul. 37, good-ish looking, sometimes amusing, culture vulture.” He posted a lonely-hearts ad.’
- **判**：原文媒介是 **magazine（杂志）**，md 分析层三处写「剪报」、一处写「登报」（中文语境均指向报纸），与本章词表自写的「杂志」自相矛盾。
  **取证**：`/usr/bin/grep -nE '报纸|newspaper' "ch04 digbys studio is searched.md"` → 命中 0，exit=1；`/usr/bin/grep -nE '杂志|magazine|剪报|剪下' md` → 命中 5，exit=0。⇒ md **没有**写「报纸」二字，故不判「编造报纸」，判**提示级**（媒介措辞与原文及本章词表不一致）。
- **附注（本章专属判据）**：本章专属判据提到「一则登在报纸上的交友广告」——**原文并非报纸而是杂志**，md 也未写「报纸」；此项经查为 md 正确、无缺陷。

### B5 · 「搜查队」vs「两名警探」——提示
- **md**：`ch04 …md:11`（`搜查队在迪吉·康姆-沃森…书房里翻找线索`）vs `:109`（`两名警探搜查迪吉·康姆-沃森多利斯山的单间书房`）
- **原文**：全章在场者只有 Matt 与 Caius 两人（`:23`–`:98` 全部对话轮换仅此二人）。
- **判**：同一文件内层级表述不一致 + 「队」夸大人数。**提示级**。

### B6 · 「独居老学者」与章内自引的「37」相冲——提示
- **md**：`ch04 …md:11`（`把"独居老学者"的形象…`）、`:109`（`把一个独居学者的孤独…`）；而 `:49` 自己引用的是 `37 岁`
- **原文**：`text/ch04_4.txt:89`（`37, good-ish looking…`）
- **判**：37 岁称「老」与本章内引文不合；「学者」仅为「在博物馆工作」的推衍（原文 `:65` 只说约会选在 museum）。**提示级**。

### B7 · 「自己剪下来收着」——提示
- **md**：`ch04 …md:14`（`连交友广告都自己剪下来收着`）
- **原文**：`text/ch04_4.txt:89`（`A cut-out from a magazine was at the back.`）+ `:95`（`‘The poor guy had kept the ad. A memento of their romance.’`）
- **判**：原文只说盒底有一份杂志剪页、且 Digby 留了它；**谁剪的未写**。**提示级**。

---

## 三、错（两边都有但不一致）

### E1 · 信件的位置：md 写「抽屉」，原文写「刻玫瑰的木盒」——**阻断**
- **md**（三处，含导航层与总结层）：
  - `:11` `房间的陈设、**抽屉里那一叠通信**和夹在盒底的一张交友广告剪报`
  - `:13` `物证（车站旁果蔬店的收据、打字机、**抽屉里的信件**、杂志剪报）`
  - `:109` `从一尘不染的极简陈设、**抽屉里的旧信**和一则自登的交友广告里`
- **原文**：`text/ch04_4.txt:56`（逐字）
  > Caius turned to a half-height bookcase near the bed. **A wooden box with a rose carved into the side** had caught his eye. **He opened it. It contained a month’s worth of frequent correspondence.**
  > （另见 `text/ch04_4.txt:89`：`Caius took the other letters out of **the box**.`）
- **判**：信在**木盒**（rose carved wooden box，放在床边 half-height bookcase 上）；全章唯一的抽屉是 `Digby’s sock drawer`（`:26`，且开抽屉的动作与信件无关）。md 三处把木盒里的通信改写成抽屉里的通信，且两处落在**导航层与一句话总结层**（读者最先看到的层级）。主语/容器错置 ⇒ **阻断**。
- **取证**：`/usr/bin/grep -nE '抽屉|木盒|盒子' md` → 命中 `:11 :13 :14 :30 :109`（exit=0）；`/usr/bin/grep -nE 'drawer|box|bookcase' text/ch04_4.txt` → 命中 `:26 :29 :38 :56 :89`（exit=0），`:56` 明写 wooden box / `:89` 明写 out of the box。

### E2 · 块 4 把「意外污染」写成「找凶手」——提示
- **md**：`ch04 …md:44`
  > 这是全章头一次把"他出去买过东西"与"他的死"接上线的推理，而推理的依据只是一张前一天在车站旁果蔬店开出的收据；作者让嫌疑沿着一条采购链去**找凶手**，把搜查从房间推回到社会关系上。
- **原文**：`text/ch04_4.txt:68`（逐字）
  > ‘**Accidental contamination?**’ Matt asked, showing Caius the receipt he’d found. ‘What if the hemlock leaves made it into the bagged salad he bought from the greengrocer’s by mistake. It says organic on the receipt. Maybe they added a bit of the hedgerow not realising.’
- **判**：Matt 提的是**意外**（no killer）；收据指向的是**蔬果店这条供应链**，不是「社会关系」。因果方向被改写。**提示级**（属评论层措辞，非情节断言）。

### E3 · 块 6「紧接着那句把 A memento of their romance 翻成 A memento mori now」措辞倒置——提示
- **md**：`ch04 …md:58`
  > 警探先带着同情说出"可怜的家伙"，把"纪念品"落到一个温情的词上；紧接着那句把「A memento of their romance」**翻成**「A memento mori now」，一件柔情纪念品在一秒之内被改写成死亡纪念品…
- **原文**：`text/ch04_4.txt:95` 与 `:98`（逐字，两句相邻）
  > :95 `‘The poor guy had kept the ad. A memento of their romance.’`
  > :98 `‘A memento mori now.’`
- **判**：原文是**三句并列**：句 2 出现 `A memento of their romance`，句 3 才出现 `A memento mori now.`（后句在 md 的引语块之外）。md 的说法在方向上没错（memento mori 改写了 memento），但表述成「把 romance 句翻成 mori 句」，把并列两句写成了替换关系。**提示级**。

### E4 · 块 1「他只看得见其中一半」——提示
- **md**：`ch04 …md:21`
  > 如今望出去的花园已经一分为二，**他只看得见其中一半**。
- **原文**：`text/ch04_4.txt:20`（逐字）
  > It now had a view of a halved garden.
- **判**：原文说的是**花园被一分为二**（分割房屋的结果），未说他只能看见其中一半（他那一半应可尽览）。轻微越界。**提示级**。

---

## 四、本章专属判据的三项核对（房间本身如何讲述这个人）

| 判据项 | 原文 | md | 结论 |
|---|---|---|---|
| 一件旧沙发 | 全章**无** sofa/couch/沙发（`/usr/bin/grep -nE '沙发|sofa|couch' text/ch04_4.txt` → 命中 0，exit=1）；studio 陈设为 bed / table / kitchenette / shower / drawers / half-height bookcase | 全章**无**「沙发/sofa/couch」（同命令对 md → 命中 0，exit=1） | **双方均无 ⇒ 无缺陷**。记录于此以防后续被当作「应补的旧沙发」加进去——原文没有这个东西 |
| 一则登在**报纸**上的交友广告 | 媒介是 **magazine**（`A cut-out from a magazine was at the back.`）；且是**杂志剪页** | md 三处写「剪报」、一处写「登报」，**未出现「报纸」二字**；md 自己的词表写「magazine｜杂志」 | **提示级（B4）**：md 未编造报纸，但「剪报/登报」措辞与原文媒介不一致 |
| 「人物弧线」抓孤独怎么被写出来 | 孤独靠物：PO Box 地址（`:83`）、无 email 只用邮寄（`:32`）、老电视/收音机/无 laptop（`:38`）、保留广告（`:95`）、无 app（`:86`） | `:14` 人物弧线段写了「没有电子邮箱、凡事只寄信、老电视、收音机、连交友广告都自己剪下来收着」 | **成立**（主题抓得准）；仅「不能联网」「剪报」「登报」「自己剪下来」四处措辞待修（B3/B4/B7） |

---

## 五、取证三件套（命令 + 输出 + 退出码，全部显式路径，不用 git grep / 不用 rg 默认 ignore）

```
$ cd notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell
$ /usr/bin/grep -nE '沙发|sofa|couch' "ch04 digbys studio is searched.md"   → 命中 0；exit=1
$ /usr/bin/grep -nE '沙发|sofa|couch' text/ch04_4.txt                    → 命中 0；exit=1
$ /usr/bin/grep -nE '报纸|newspaper' "ch04 digbys studio is searched.md"  → 命中 0；exit=1
$ /usr/bin/grep -nE '报纸|newspaper' text/ch04_4.txt                     → 命中 0；exit=1
$ /usr/bin/grep -nE '杂志|magazine|剪报|剪下' "ch04 …md"                  → 命中 5（:11 :13 :14 :49 :100）；exit=0
$ /usr/bin/grep -nE 'magazine|newspaper|journal' text/ch04_4.txt        → 命中 1（:89）；exit=0
$ /usr/bin/grep -nE 'drawer|box|bookcase' text/ch04_4.txt                → 命中 5（:26 :29 :38 :56 :89）；exit=0
$ /usr/bin/grep -nE 'kangaroo|taxidermy' text/ch04_4.txt                 → 命中 1（:26）；exit=0
$ /usr/bin/grep -nE 'museum|museums' text/ch04_4.txt                     → 命中 1（:65，约会地点）；exit=0
$ /usr/bin/grep -noE '[0-9]+ ?[a-z]*|[a-z]+ ?[0-9]+' text/ch04_4.txt     → :1 4 / :12 4 / :32 1960s / :56 on 27 / :89 37；exit=0
$ /usr/bin/grep -nE '全书|查无|零命中|从没|从未|没有出现' "ch04 …md"     → 命中 0；exit=1
```

补充（机器层）：`bash scripts/chapter.sh "notes/…/ch04 digbys studio is searched" --json` → **退出码 0**（`2-machine.json` 落盘在本目录）；`python3 scripts/check_vocab.py "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell"` → **FAIL(0)**，ch04 无词条告警。
补充（人工复核引语/例句逐字，Python 计数）：6 条引语**各命中 1 次**；32 行词表**例句均为原文精确子串**（其中 3 行为表头，非词条）。

---

## 六、三张单子计数

| 单子 | 阻断 | 提示 | 跳过/已覆盖 |
|---|---|---|---|
| 漏 | 0 | 2（L1、L2） | 1（L3，已被块 3 覆盖） |
| 编 | **1**（B1） | 6（B2–B7） | — |
| 错 | **1**（E1） | 3（E2–E4） | — |

**阻断合计 2 条：B1（标本在抽屉里）、E1（信件在抽屉里而非刻玫瑰的木盒）**——两条同源：把「抽屉」当成本章的通用容器，误改了房间讲述人物的方式。
