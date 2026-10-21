# 第 16 章 R5 判定（人工审查）

## §0 覆盖声明

- **本轮人工审查只覆盖第 16 章**（`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch16 chapter 16.md`）。
- 抽样理由：本章是全书「商场终局」章——Alba 的线收束于此，且本章**全章只有 1 行对白**（`text/ch16:66`），叙事几乎全靠画面推进；它同时是第 15 章（三人关系）与第 17 章（收束）的接口，最适合做引语逐字、身份归属与跨章事实的人工抽验。
- **其余各章（ch00–ch15、ch17）本轮只有机器层，没有人工层，不写成「通过」**（依据 `docs/rules/审查表.md:31`：「抽样章号与理由写进 `4-verdict.md` 的覆盖声明；没跑的章要写「只有机器层」，不许写成「通过」」）。第 15 章的人工层由同一子代理另出 `review/ch15/4-verdict.md`；本结论不外推到第 15 章。
- 唯一真值：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch16_chapter_16.txt`（66 行 / 20160 字符）。
- 成品 md：`ch16 chapter 16.md`（161 行；引语块 8 个；`## 本章词汇` 29 条；`## 一句话总结` 1 条）。
- 流程合规：先整章素读原文并落 `review/ch16/1-suread.json`（R1），再打开成品 md 对照（R3–R4），最后出本判定（R5）；顺序符合 `docs/rules/审查表.md:37`。
- 机器层：`review/ch16/2-machine.json`（已存在、未改动）——`verdict: ok`，8 块全 `ok=true`，`issues` 仅 `keyword_long` 5 条（块 2/4/5/6/7），非阻断。
- 签名：DSH-Mac

---

## §1 四组数（只报这四组）

| 组 | 数 | 依据 |
|---|---|---|
| **逐字** | 8/8 引语块逐字一致（100%）；`## 本章词汇` 29 条例句逐字一致（29/29，`not_verbatim=0`） | `bash scripts/chapter.sh "…/ch16 chapter 16.md" --json` → 退出码 0、`verdict: ok`、8 块 `ok=true`、`empty_quote=0`、`segment_miss=0`；块 1 在 `text/ch16:6`、块 2 在 `:9`、块 3 在 `:15`、块 4 在 `:18`、块 5 在 `:24`、块 6 在 `:36`、块 7 在 `:42`、块 8 在 `:66`，逐句比对首尾词一致。词表逐字用 `/tmp/check_vocab_ch1516.py` 核过（跳过表格分隔行）。 |
| **对应** | 8 块 × 固定三问，全部能在原文指出出处（8/8 通过） | ①动词主语：块 1「It was made of / Inside were」＝树（`:6`）；块 2「she caught sight of / She didn't know」＝Alba（`:9`）；块 3「her head seemed too big / leaving her colorless」＝那个 Diana（`:15`）；块 4「she stretched out… pinched her thigh」＝树里的 Diana（`:18`）；块 5「The lights everywhere went out / Splau became」＝叙述（`:24`）；块 6「They did it out of a deep affection」＝那些陪同者（`:36`）；块 7「she could see some of the women's uncovered bellies」＝Alba（`:42`）；块 8「I just wanted」＝Alba（`:66`）。②受事/宾语：块 3「all the fat / the muscle mass and the energy」（`:15`）；块 4「her thigh」「both women's mouths」（`:18`）；块 6「a deep affection she hadn't recognized」（`:36`）；块 7「tiny stumps: small, fleshy appendages」（`:42`）；块 8「the controllers」（`:66`）。③归属方向：块 3「to hug this emaciated version of her sister」＝Alba→Diana（`:15`）；块 5「her own face, twice duplicated」＝叙述者向 Alba 的脸回指（`:24`）；块 6「she hadn't recognized」＝Alba 未认出（`:36`）；块 7「That's why they scream, she thought」＝Alba 的想法（`:42`）。 |
| **形态** | 4 项子项（中文理解 / 关键词 / 为什么这样写 / 读者视角提示）× 8 块 = 32 个子项行，**缺 0**；引语行形态 `> **原句 N:** "…"` 8/8 合规；块数 8 ∈ [3,10]（profile novels）；导航 5 项齐全（md:11–15）；`## 本章词汇` 三档齐全（⭐⭐⭐ 10 / ⭐⭐ 12 / ⭐ 基础 7）；`## 一句话总结` 有正文（md:161）；H1 `# 16. Chapter 16` 符合本书 `N.` 形态 | `2-machine.json`：`h1_shape_ok`、`nav_count=5`、`subitems_modal`＝4 项、`blocks=8`、`profile=novels`；`struct_bad=0`、`hole=0`、`block_count` 空。**形态偏离说明**：本章块间有 `---` 分隔（9 行），与 ch00–ch11、ch17 一致（ch12–ch15 没有），两种体例在本书内并存，**不计入缺陷**，此处只记此行理由。 |
| **断言** | 15 条关键断言逐条回原文取证（15/15 有据；1 条残留推断＝提示档，父代理已修的四条按「已修复」记，不重复计缺陷） | 见 §2 判定表 A1–A15；A9 判「提示」，A10–A12 判「已修复·通过」，其余通过。 |

---

## §2 判定表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | md:21「圣诞老人会在树里接待客人，问他们乖不乖、想要什么礼物」 | ch16:`text:6`（`[7,1188)`）「The days leading up to Christmas, at peak hours, Santa Claus would welcome visitors there, asking if they'd been good and what gifts they wanted.」＋同段「customers could enter the tree freely」 | 成立（`there`＝树内） | 通过 |
| A2 | md:27「那并不是门，只是一个门框，人从外面就能看见里面」 | ch16:`text:6`「It wasn't really a door; it was just the frame.」＋「You could see the heart of the tree from the outside, since its structure was hollow.」 | 成立 | 通过 |
| A3 | md:39「这些挪动的污渍……原文没有点破」 | ch16:`text:9`（`[1191,1722)`）「She didn't know who they were, but she didn't intend to look and find out.」 | 成立（父代理已修，旧版「其实是别的女人——本章后面才说破」属编造） | 通过 |
| A4 | md:45「树里的第三个人……是被抽干之后的戴安娜」 | ch16:`text:15`（`[1811,3951)`）「And the one sitting next to her was Diana, or a gloomy version of Diana.」＋「colorless, soulless」 | 「被抽干之后的戴安娜」成立；**但「第三个人」的定位措辞易被读成「三个里的第三个」**，与原文「坐在她旁边」冲突 | 提示 |
| A5 | md:49「作者还特意让阿尔巴『想抱这个版本的姐姐，脚却不听指挥』」 | ch16:`text:15`「Alba wanted to hug this emaciated version of her sister, but her feet wouldn't respond to her command.」 | 成立 | 通过 |
| A6 | md:51「原文紧接着让阿尔巴想起姐姐大学第二年绝食的事」 | ch16:`text:15` 句序：`She thought back to when Diana quit eating her second year of university…` 在**前**，`Alba wanted to hug this emaciated version of her sister…` 在**后** | 事实成立，**时序被写反**（原文是先回忆后拥抱） | 提示 |
| A7 | md:57「树里那个被抽干的戴安娜忽然伸出手，拇指和食指掐住身旁那个女人的腿」 | ch16:`text:18`（`[3953,5035)`）「Then, all of a sudden, she stretched out her thumb and index finger and pinched her thigh」；被掐者＝`the woman beside her` | 成立 | 通过 |
| A8 | md:69「斯普劳变成一张狼嘴」 | ch16:`text:24`（`[5299,6505)`）「Splau became the mouth of a wolf」 | 成立（中文名「斯普劳」是全书通译，见 §4-5） | 通过 |
| A9 | md:97「触手在这里从超自然之物变成术后痕迹，因果关系被一下子摆平」 | ch16:`text:42`（`[12716,14164)`）只写 `scars` / `tiny stumps` / `appendages that had been cut and hadn't yet healed`，**无施动者、无手段**；`That's why they scream, she thought` 是 Alba 的猜想；`some of the women's uncovered bellies` 限定了范围 | 「术后」「被处理过」是原文没有的手术推断（全书无任何手术描写）；「因果关系被一下子摆平」把猜想说成定论；「满地都是」与 `some` 冲突 | 提示 |
| A10 | md:21（原「坐在树里」） | ch16:`text:6` | **父代理已修复**为「会在树里接待客人」，与原文一致 | 通过 |
| A11 | md:27（原「只留一扇门」） | ch16:`text:6`「It wasn't really a door; it was just the frame.」 | **父代理已修复** | 通过 |
| A12 | md:99（原「一直有人在替这些女人做手术」） | 全书 grep `surg|scalpel|operat|incision` 仅命中 `ch02:177` 的 `surgical tape`，**无任何手术描写** | **父代理已修复**为「原文没有交代是谁、又用什么手段处理的」，与原文一致 | 通过 |
| A13 | md:11「几百个和她一样的女人从各个店铺涌出来合声尖叫」 | ch16:`text:48`「Hundreds and hundreds streaming out of stores, restaurants, and cafés」；`:18`「The cries grew louder, multiplied, surged through the mall」 | 人数与来源成立；**「合声／同步」写错了对象**——同步的是 `:24` 的掌声（`clapped in perfect synchrony`） | 提示 |
| A14 | md:87「『她总在我身边』正是你以为的证据」 | ch16:`text:36`（`[10563,11705)`）「They did it out of a deep affection she hadn't recognized, and since she hadn't recognized it, she had taken it for granted.」 | 「深情」成立；措辞「你以为的证据」易读成「陪伴是幻觉」，与原文冲突 | 提示 |
| A15 | md:105「我想要的不过是那两只手柄」 | ch16:`text:66`（`[20128,20157)`）「I just wanted the controllers.」（五词）；两只手柄的依据在 **ch11:99**「one red and the other blue」 | 成立 | 通过 |

---

## §3 收口复核（外层预审疑点的独立结论）

| 疑点 | 独立结论 | 依据 |
|---|---|---|
| ① 全章最后一句是谁说的？ | **Alba**。全章唯一一句引号台词，且是她的内心直白（`:66`）；md:105／md:109／md:161 归属正确。 | `text/ch16:66`；前文 `:60`「Mission accomplished.」同属 Alba。 |
| ② 树里三个人是谁？ | Alba 自己（**坐在对面**、流鼻血的复制体）、**坐在她旁边**的 gloomy version of Diana、以及独坐另一条长椅、眼周皮肤红肿的那个。md:11「两个和她一模一样的人」与 `:24`「her own face, twice duplicated」吻合；**md:45 的「第三个人」措辞需改**（见 A4/W5）。 | `text/ch16:15`、`:24`。 |
| ③ 「谁坐在旁边／谁坐在对面」有没有搞反？ | 没有搞反，但**章末块 3 之前的 md 措辞**容易引起误读：`the one sitting next to her was Diana`（旁边＝Diana）、`The woman across from her, who was identical`（对面＝Alba 的复制体）。 | `text/ch16:15`。 |
| ④ :42 的「被切掉、还没长好」是不是指手术？ | **不是**。原文只给痕迹，不给施动者、不给手段，也不给时间。全书无手术描写 ⇒ md:97 残留的「术后痕迹／被处理过」判提示；md:99 已由父代理修好。 | `text/ch16:42`；全书 grep。 |
| ⑤ :9 的「dark stains」是不是别的女人？ | 原文**没有点破**（她「不知道是谁，也不打算去看」）。md:39 已由父代理改为「原文没有点破」，成立。 | `text/ch16:9`。 |
| ⑥ :24「没有一个女人看上去超过四十岁」的主语是谁？ | **那群女人**，不是 Alba。md 未写成阿尔巴，成立。 | `text/ch16:24`。 |
| ⑦ 女人们回家过节是客观事实还是 Alba 的投射？ | **Alba 的投射**（`She was projecting her desire to leave on the women`＋`She had no doubt`）。md 完全没写这层 ⇒ 记漏（L2，提示档）。 | `text/ch16:48`。 |
| ⑧ 章末灯是怎么亮的？ | **Alba 自己拍手**（模仿孩子为唤醒洗手间感应器自创的 choreography），不是别人点亮、也不是自动亮。md 全文无「拍手」二字 ⇒ 记漏（L4，提示档）。 | `text/ch16:57`；呼应 `:39`「No one clapped to turn the lights back on」。 |
| ⑨ 陪同者最后怎么了？ | **全部消失**（`:51`「Their companions were gone. They were alone.」），几百个女人堆在门口却转身盯着 Alba、不打算放她走。md 未写 ⇒ 记漏（L3，提示档）。 | `text/ch16:51`。 |
| ⑩ 本章有没有「母亲线」？ | 有，且是本章唯一一次母亲出场：`:33` 卡门几个月前的那个深夜（三更半座机、独自过 Ronda 交通环岛、Juan 不能陪）。md 全文未出现「卡门」⇒ 记漏（L5，提示档）。 | `text/ch16:33`。 |
| ⑪ 陪同者也是受害者吗？ | 是：连孩子和婴儿都骨瘦如柴，成年人不超过九十磅。md 只做了解读、未给事实 ⇒ 记漏（L6，提示档）。 | `text/ch16:36`。 |
| ⑫ 「商场变成投影机」是投在墙上还是商场本身？ | **商场本身变成投影机**（`Splau, an open-top mall, had become a giant projector of pink and purple stars`）。md:11「商场变成一台映出粉紫色星光的巨大投影机」成立。 | `text/ch16:42`。 |
| ⑬ 章末 Alba 死了吗？ | 没有：`:63` 她起身、穿过人群，触手重新发光；`:66` 只是最后一句实话。md:11／md:161 写「肚皮被触手撕开」＋「最后只剩五个词」，未写死，成立。 | `text/ch16:60`–`:66`。 |
| ⑭ 词表 29 条例句是否逐字取自本章？ | 是，`not_verbatim=0`（`/tmp/check_vocab_ch1516.py`，不入库）。 | 校验脚本输出。 |
| ⑮ 这声闷哼在第 17 章有回扣吗？ | **没有**：全书 `moan/moaning` 只命中 ch16:18、ch16:39；ch17 只有 `sound`/`howling`/`crying`。md:63「本章之后它还会再出现」无据 ⇒ 提示档（W3）。 | 全书 grep；`text/ch17:24/63/318/321/348`。 |

---

## §4 已核实为正确（防误修清单）

以下条目**看似有误但回原文核对后成立**，后续修复时**不得改动**：

1. **md:21「圣诞老人会在树里接待客人，问他们乖不乖、想要什么礼物」——成立（父代理已修，改后正确）。** `text/ch16:6`「Santa Claus would welcome visitors there, asking if they'd been good and what gifts they wanted」，`there` 指树内（同段「customers could enter the tree freely」）。
2. **md:27「那并不是门，只是一个门框，人从外面就能看见里面」——成立（父代理已修，改后正确）。** `text/ch16:6`「It wasn't really a door; it was just the frame.」＋「You could see the heart of the tree from the outside」。
3. **md:39「原文没有点破」——成立（父代理已修，改后正确）。** `text/ch16:9`「She didn't know who they were, but she didn't intend to look and find out.」
4. **md:99「原文没有交代是谁、又用什么手段处理的」——成立（父代理已修，改后正确）。** `text/ch16:42` 只给痕迹不给施动者；全书无手术描写。
5. **md:45「被抽干之后的戴安娜」——成立，只有「第三个人」这个措辞要改。** `text/ch16:15`「Diana, or a gloomy version of Diana… leaving her colorless, soulless」＋`:18`「Diana, or what was left of her」。
6. **md:49「想抱这个版本的姐姐，脚却不听指挥」——成立。** `text/ch16:15`「Alba wanted to hug this emaciated version of her sister, but her feet wouldn't respond to her command.」
7. **md:51「姐姐大学第二年绝食」——事实成立**（`text/ch16:15`），**只有与 md:49 的先后顺序要调**。
8. **md:57「拇指和食指掐住身旁那个女人的腿」——成立。** `text/ch16:18`「she stretched out her thumb and index finger and pinched her thigh」，被掐者是 `the woman beside her`。
9. **md:69「斯普劳变成一张狼嘴」——成立，不要改回英文。** `text/ch16:24`「Splau became the mouth of a wolf」；中文层全书统一用「斯普劳」（`00_概述.md`、`00_金句精选.md`、`00_情感节点.md`、ch16、ch17），正文英文引文保持 `Splau`。
10. **md:93「一截被切掉、还没长好的肉芽」——成立。** `text/ch16:42`「tiny stumps: small, fleshy appendages that had been cut and hadn't yet healed.」
11. **md:105「我想要的不过是那两只手柄」——成立（含「两只」）。** `text/ch16:66`「I just wanted the controllers.」（五个词）；「两只」的依据是 **ch11:99**「one red and the other blue」，**ch16 原文只写复数 controllers、未写两只** ⇒ 「两只」在本书有据，保留。
12. **md:109「那只装着手柄的盒子」——成立。** `text/ch16:60`「the box would remain intact」＋「She pulled it from her pocket.」
13. **md:15「商场保洁」——成立。** `text/ch16:60`「When the cleaning staff found her, she'd be unrecognizable」。
14. **md:11「两个和她一模一样的人」——成立。** `text/ch16:24`「her own face, twice duplicated, broken in two different ways」；树里的 Alba 复制体是「对面那个」（`:15`），与 `:24` 的「twice duplicated」一致。
15. **md:81／md:85「出于惯性…当成理所当然」——成立。** `text/ch16:36`「Out of inertia, or because they had to. Because doing otherwise had never crossed their minds. They did it out of a deep affection she hadn't recognized, and since she hadn't recognized it, she had taken it for granted.」
16. **md:13「尖叫也反转成几百人同步的掌声」——成立，且是本章的关键反转，不要在改 W1 时一起删掉。** `text/ch16:24`「It wasn't really applause. All the women had raised their arms in the air at once, and they clapped in perfect synchrony.」
17. **md:11「商场变成一台映出粉紫色星光的巨大投影机」——成立。** `text/ch16:42`「Splau, an open-top mall, had become a giant projector of pink and purple stars」。
18. **md 块 8 只有五个词——成立。** `text/ch16:66` 全句＝`I just wanted the controllers.`（5 词），机器层 `quote_long=0`。
19. **本章块间有 `---` 分隔——不是缺陷。** 全书 ch00–ch11、ch16、ch17 有，ch12–ch15 没有；两种体例并存，只作记录（§1 形态行已记理由）。
20. **md 词汇表 29 条三档齐全且逐字命中——成立，不要顺手改写例句。** `not_verbatim=0`；机器层 `keyword_bad=0`，`keyword_long` 5 条只是「关键词字段偏长」的提示，与逐字性无关。

---

本判定只覆盖第 16 章；其余各章只有机器层，不写成「通过」。本轮未改动任何 md 文件，git 未执行任何操作（未 add / 未 commit / 未 push）。
