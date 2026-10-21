# 第 8 章 R5 判定（人工审查）

**覆盖声明**：本次人工审查抽样了**第 7、8、10 章**（外层预审指定的三章），三章的 R0–R5 全流程均已跑完（`1-suread.json` → `2-machine.json` → `3-diff.md` → 本文件）。**第 1–6、9、11–17 章只有机器层，没有人工层，不写成「通过」**（`docs/rules/审查表.md:31`）。机器层唯一真值＝`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch08_chapter_8.txt`（282 行，11,817 字符，94 个自然段）；成品＝`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch08 chapter 8.md`（126 行，6 个引语块，18 条词汇）。审查人：DSH-Mac。

---

## 一、四组数（只报这四组）

| 组 | 数 | 依据 |
|---|---|---|
| 逐字 | **6 / 6** | 6 个引语块逐字命中原文（`2-machine.json`：`segments 6`、`segment_miss 0`、`quote_long 0`、`empty_quote 0`；自写脚本 `check_md_quotes.py`（ch08）：引语 MISS = 0、词汇例句 MISS = 0；引文起始字符位 6 / 90 / 93 / 138 / 222 / 282 对应 `text/ch08` 行 6 / 90 / 93 / 138 / 222 / 282）。另：`本章词汇` 18 条例句全部是原文子串（hysteristic:6、accidentally:48、communicate:66、high-pitched:138、unbuttoned:222、suspiciously:252、neighbor:48、earrings:63、nauseous:129、silently:150、crouched:108、unbuckled:186、abdomen:231、blender:252、coats:90、box:252、calm:120、phone rang:96）。 |
| 对应 | **6 / 6 块（18 问）** | R4 逐块对应走完 6 个块；每块固定三问（①每个动词的主语是谁 ②受事／宾语是谁 ③归属方向回原文看 by/to/from/of）＝18 问，全部有原文出处。导航 5 条、词汇 18 条、一句话总结 1 条另行逐句对账。 |
| 形态 | **0 偏离 ／ 1 假红** | `2-machine.json` `counts`：`struct_bad 0`、`keyword_bad 0`、`cjk_low 0`、`empty_quote 0`、`quote_long 0`；`form`：`h1_shape_ok true`、`nav_count 5`、`nav_count_ok true`、`blocks 6`、`subitems_modal`＝中文理解／关键词／为什么这样写／读者视角提示（与 `profile: novels` 一致）、`baseline: book`、`issues` 四组全空。机器层仅「关键词」子项 CJK=0 一项非零，与兄弟章同体例（关键词本就是英文短语）⇒ **假红**，非本章偏离。 |
| 断言 | **21** | 判定表 21 行：通过 11 ／ **阻断 1** ／ 提示 8 ／ 假红 1 ／ 跳过 0。 |

---

## 二、判定表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 6 个引语块与原文逐字一致 | `2-machine.json` `quotes[].segments[].ok=true`（6/6）；自写脚本引语 MISS = 0 | 通过 | — |
| 2 | `本章词汇` 18 条例句均为原文子串 | 自写脚本 `check_md_quotes.py`（ch08）：词汇例句 MISS = 0（逐条行号见「四组数」行） | 通过 | — |
| 3 | 块 1（`md:19-27`）对应「每年平安夜都一样／出门总是超时／硝化甘油瓶」 | `text/ch08:6`「Every Christmas Eve, it was the same. They planned to leave home early enough to catch the train before it got too crowded, but they always ran out of time. In the end, they were forced to decide—shouting at the top of their lungs—between the stress of public transit on a holiday and the angst of car travel with Brisa, who was like a bottle of nitroglycerin ready to explode.」 | 通过 | — |
| 4 | 块 1 说「a bottle of nitroglycerin」比喻的是**Brisa**（孩子） | `text/ch08:6`「car travel with Brisa, who was like a bottle of nitroglycerin ready to explode」——`who`＝Brisa | 通过 | — |
| 5 | 块 2（`md:31-39`）说《泯灭天使》那句是 **Diana** 说的 | `text/ch08:90`「"What more do you need to do? … What is this, The Exterminating Angel? Come on, get your coats."」（该行无行内标注；判定链见「收口复核」第 2 条） | 通过 | — |
| 6 | 块 3（`md:43-51`）对应「他帮孩子穿外套／她反复确认暖气、直发夹、炉灶、烤箱」 | `text/ch08:93`「Carlos helped the kids with their jackets, since they were especially nervous tonight—Santa was coming, after all. Diana, meanwhile, looked around to make sure they weren’t forgetting anything. Several times, she confirmed that the heat wasn’t on, the straightener was safely cooling, and both the stovetop and the oven were off…」 | 通过 | — |
| 7 | 块 4（`md:55-63`）说「女儿想吐」这句是 **Diana** 编的、司机配合在 Diagonal 边停车 | `text/ch08:129`「"Well, stop as soon as you can. Stop up here. My daughter is feeling nauseous."」；`:138`「"If she throws up, she throws up… But pull over when you can, she's feeling sick, and she needs some air," Diana answered. Her voice was high-pitched, cracking.」；`:126`「"I can’t stop in the middle of Diagonal," the driver said」；`:153`「"I can pull over here, in that grassy spot."」 | 通过 | — |
| 8 | 块 5（`md:67-75`）说「不疼」「解扣子」「又热又湿」「以为是汗」出自 **Diana** | `text/ch08:222`「"No. But I’m bleeding. It doesn’t hurt, but I’m bleeding. I unbuttoned my pants because they were too tight and it was starting to get uncomfortable, and I noticed my stomach was warm and wet. I thought it was sweat, but no."」 | 通过 | — |
| 9 | 块 6（`md:79-87`）对应「四指宽、像纸浆和血做的腰带、裤腰衬衫下摆染了、并未大量出血」 | `text/ch08:282`「Running her fingertips over the injury, Diana realized that it was an open wound, about four fingers wide and wrapping around her waist like a belt made of pulp and blood. The top of her pants and the bottom of her shirt were stained, but the wound wasn’t actively bleeding.」 | 通过 | — |
| 10 | `md:14`「Brisa 把手机扔到地上」「用怀疑的目光盯着父母」归属正确 | `text/ch08:105`「A third call came in, and Brisa flung the phone to the floor.」；`:252`「Brisa, on the other hand, kept glancing suspiciously at her parents.」 | 通过 | — |
| 11 | `md:126` 一句话总结与原文事实一致 | `text/ch08:6`–`:282`；「不疼」见 `:222`「It doesn’t hurt」 | 通过 | — |
| 12 | `md:39`「前面她一直在数锁」——本章原文没有「锁」 | `/usr/bin/grep -nwiE 'lock\|locked\|unlock\|bolt\|chain\|key' text/ch08_chapter_8.txt` → 无输出，退出码 1；「数锁」的真实出处是 `text/ch04_chapter_4.txt:9`「She recognized the sound of the dead bolt, the second lock, and the third one…」（另有 `text/ch01_chapter_1.txt:15`「…or the lock unlocked.」） | 与原文不符 | **阻断** |
| 13 | `md:49`「暖气、直发夹、炉灶、烤箱，四项」与同句「三个短语」自相矛盾 | `text/ch08:93`「the heat… the straightener… and both the stovetop and the oven」＝三项并列；`md:51`「清单里的第四项——电与火」同源 | 数字不符 | 提示 |
| 14 | `md:15`「伴侣的话多以转述形式出现……看不清他的脸」与原文呈现方式不符 | `text/ch08:12/72/87/99/114/147/189/240/246/258/276` 均为直接引语；`:231`「who was undone」、`:246`「Carlos was horrified, pale」、`:225`「his knees buckled」三处都给了他的面貌与身体 | 表述不符 | 提示 |
| 15 | `md:14`「Carlos 从嫌她**老**想跳车」——原文是当场的突发抱怨 | `text/ch08:189`「"What happened? All of a sudden you’re obsessed with jumping out of trains and cars."」 | 措辞过头 | 提示 |
| 16 | `md:11`「捡起一只**成对的**银圈耳环」与原文的「又一只」不合 | `text/ch08:27`「Diana had a silver hoop earring in her palm.」（单数一只）；`:33`「"Another earring."」；`:36`「"Like the one from the other day?"」 | 措辞失真 | 提示 |
| 17 | 母亲连打五个电话、Diana 四次挂断这一整段未进 md | `text/ch08:102`「"My mom. Who knows what she wants now."」；`:111`「Carmen called four more times, and all four times, Diana silenced the call.」；`:114`「"Call her back. It’s not normal for her to call this many times," Carlos said.」 | 漏（覆盖缺口） | 提示 |
| 18 | 司机的两次拒绝（Diagonal 中间不能停、今晚最后一单不等人）未进 md | `text/ch08:126`、`:135`、`:171`、`:180` | 漏（覆盖缺口） | 提示 |
| 19 | Carlos 在车里的追问链（安全带？之前就有伤？是不是你自己弄的？）未进 md | `text/ch08:219`、`:258`、`:264`；Diana 否认 `:261`「I swear, there’s been nothing. Absolutely nothing.」 | 漏（覆盖缺口） | 提示 |
| 20 | 孩子手里的玩具「搅拌机」这一层反讽未进正文分析 | `text/ch08:252`「It was a blender, but they didn’t understand that yet.」 | 漏（覆盖缺口） | 提示 |
| 21 | 「关键词」子项 CJK=0 是否形态偏离 | `2-machine.json` `blocks[].cjk.关键词 = 0`；同体例见 `ch03 chapter 3.md:23`、`ch04 chapter 4.md:23` | 与兄弟章同体例，非偏离 | 假红 |

---

## 三、收口复核

1. **施事／归属三问（逐块走完 6 块）**
   - 块 1（`md:19`）：`text:6`「car travel with **Brisa**, who was like a bottle of nitroglycerin ready to explode」——`who`＝Brisa，被比作硝化甘油瓶的是**孩子**，不是母亲；md:21「那孩子像一只随时要炸的硝化甘油瓶」归属正确。
   - 块 2（`md:31`）：`text:90` 说话人＝Diana（判定链见下条）。
   - 块 3（`md:43`）：`text:93`「**Carlos** helped the kids with their jackets… **Diana**, meanwhile, looked around… **she** confirmed that the heat wasn’t on…」——穿外套＝Carlos，检查清单＝Diana；md:45 归属正确。
   - 块 4（`md:55`）：`text:138`「**Diana** answered. Her voice was high-pitched, cracking.」——「我带了袋子」「靠边停一下」的说话人是 Diana；md:57 归属正确。
   - 块 5（`md:67`）：`text:222`「"No. But I’m bleeding…" **Diana** reached out her hand—there was blood all over her fingers.」——血是她自己的；md:69「她解开扣子，然后发现小腹又热又湿」归属正确。
   - 块 6（`md:79`）：`text:282`「**Diana** realized that it was an open wound… wrapping around **her** waist」——伤口在**她自己的**腰上；md:81 归属正确。
   - ⇒ **六块均无施事反转**；本章的归属风险集中在 `md:14`／`md:15`／`md:39` 三处表述（见判定表 #12、#14、#15）。
2. **`:90` 的说话人判定（本章唯一无行内标注的引语）**：判定链＝① 紧邻的 `:87` 是 Carlos 刚说完 "Five minutes? Why didn’t you tell us before you requested it?"；② 下一段 `:93` 紧接写「Carlos helped the kids with their jackets… Diana, meanwhile, looked around…」，分工上是「催孩子穿外套」由 Diana 说、「帮孩子穿外套」由 Carlos 做；③ "get your coats" 正是要求对方去拿外套，与 `:93` 的动作分工一致 ⇒ **说话人是 Diana**，md:37「最后半句「穿上外套」又把她拉回一个正常管家的位置」归属正确，**不需要改动**。
3. **「谁的／谁的·谁欠谁·谁问的」**：`text:78`「"Who would break into the house just to leave an earring here?"」——问的是 Carlos（接 Diana 的 "Either it’s a ghost, or someone broke into our house."）；`text:114`「"Call her back… Look, she called me twice as well."」——「她」＝Carmen，「我」＝Carlos；md 全章未对这两句作断言，无误。
4. **人数／计数断言**：本章原文的数字只有 `text:6` 的 "two options" 与 `:90` 的 "two hours"，md 的「两个钟头」（`md:33`）与原文一致；md:49 的「四项」与原文的三项并列不符（判定表 #13）。本章无「三个孩子」类计数断言。
5. **跨章指认**：md 全文唯一疑似跨章点是 `md:39` 的「数锁」（判定表 #12，阻断）——`text/ch08` 内无 lock 类词，「数锁」的原文出处是 `text/ch04_chapter_4.txt:9` 与 `text/ch01_chapter_1.txt:15`。其余 md 内容均限于本章。

---

## 已核实为正确

以下写法在审查中看似有误，回原文逐字核对后**成立**，任何后续改稿都不得改动（`docs/rules/审查表.md` R5.5）：

1. **`md:37`「最后半句「穿上外套」又把她拉回一个正常管家的位置——她还在管，只是管的方向已经错了」成立**。依据：`text/ch08:90`「What is this, The Exterminating Angel? Come on, get your coats.」——说话人是 Diana（判定链见「收口复核」第 2 条）。
2. **`md:21`「那孩子像一只随时要炸的硝化甘油瓶」归属正确**（比的是 Brisa，不是母亲）。依据：`text/ch08:6`「car travel with Brisa, who was like a bottle of nitroglycerin ready to explode」。
3. **`md:45`「他帮两个孩子穿外套，因为今晚他们格外紧张——毕竟圣诞老人要来」成立**。依据：`text/ch08:93`「Carlos helped the kids with their jackets, since they were especially nervous tonight—Santa was coming, after all.」
4. **`md:45`「直发夹正在安全地冷却」译法成立**（原文 `the straightener was safely cooling`）。依据：`text/ch08:93`。
5. **`md:61`「这一段是本章第一次出现表演，理由是她临时造的——「女儿想吐」这个说法从头到尾没有依据」成立**。依据：`text/ch08:129`「My daughter is feeling nauseous.」＋`:132`「Carlos leaned forward and saw that the girl was perfectly fine. He looked at Diana, confused.」——原文明写孩子完全没问题。
6. **`md:63`「她要下车的真正理由，就在她自己的裤子上」成立**。依据：`text/ch08:192`「"I didn’t want to get the car dirty."」＋`:210`「"Blood," Diana said, lowering her voice.」
7. **`md:75`「她会把「我以为那是汗」说出口——那才是她第一次把不正常的东西叫出名字」成立**。依据：`text/ch08:222`「I thought it was sweat, but no.」
8. **`md:85`「作者到这一段才给出尺寸——四指宽」「并没有在大量出血」把恐怖又压低一档」成立**。依据：`text/ch08:282`「about four fingers wide」「the wound wasn’t actively bleeding.」
9. **`md:87`「那道裂口像是自己在吃自己」成立**。依据：`text/ch08:282`「The gash just below Diana’s abdomen seemed to be feeding on itself.」
10. **`md:11`「在 Diagonal 路边下车」成立**。依据：`text/ch08:126`「"I can’t stop in the middle of Diagonal," the driver said」；`:153`「"I can pull over here, in that grassy spot."」；下车点离 Alba 家约七分钟（`:123`「They were just a few meters from the Ronda de Dalt, about seven minutes from Alba’s house.」）——本章没有写「Ronda de Dalt 附近下车」，md 未越界。
11. **`md:14`「Brisa 用怀疑的目光盯着父母」归属正确**。依据：`text/ch08:252`「Brisa, on the other hand, kept glancing suspiciously at her parents.」
12. **机器层「关键词」子项 CJK=0 不是本章缺陷**。依据：`ch03 chapter 3.md:23`、`ch04 chapter 4.md:23` 的「关键词」子项同样全为英文短语 ⇒ 全书体例，非形态偏离。
