# 第 4 章 R5 判定（人工审查）

## §0 覆盖声明

- **本轮人工审查只覆盖第 4 章**（`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch04 chapter 4.md`）。
- 抽样理由：本章是 Diana 视角的第一章，也是全书「妹妹／姐姐」亲属方向的第一次落地处（md:13 原写「控制型长姐」，方向反了），且本章同时承担三处高风险动作——**归属方向**（`her sister` / `sister-in-law` / `mother-in-law` 混用）、**说话人**（`:192` 那句「It means a lot to her」）、**主角心理的反向断言**（「没做任何确认」）。适合做人工逐字＋四问法抽验。
- **其余各章本轮只有机器层，没有人工层，不写成「通过」**（依据 `docs/rules/审查表.md:31`：「抽样章号与理由写进 `4-verdict.md` 的覆盖声明；没跑的章要写「只有机器层」，不许写成「通过」」）。第 10 章已另有独立人工判定 `review/ch10/4-verdict.md`，其结论不外推到本章；**第 0–3、5–9、11–17 章一律只有机器层**。
- 唯一真值：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch04_chapter_4.txt`（373 行 / 24436 字符）。
- 成品 md：`ch04 chapter 4.md`（156 行；引语块 8 个；`## 本章词汇` 24 条；`## 一句话总结` 1 条）。
- 流程合规：先整章素读原文并落 `review/ch04/1-suread.json`（R1，16 条事件），再打开成品 md 对照（R3–R4），最后出本判定（R5）；顺序符合 `docs/rules/审查表.md:35`（「打开任何一章 md 之前，**必须先完成 R1**。违反这条，本次审查结论作废」）。
- 机器层：`review/ch04/2-machine.json`（已存在、未改动）——`verdict: ok`，8 块全 `ok=true`，`issues` 四组全空；本轮重跑 `bash scripts/chapter.sh "…/ch04 chapter 4.md" --json` 退出码 **0**（输出落 `/tmp/ch04_machine_recheck.json`，未覆盖仓库文件）。
- 签名：DSH-Mac

---

## §1 四组数（只报这四组）

| 组 | 数 | 依据 |
|---|---|---|
| **逐字** | 8/8 引语块逐字一致（100%）；`## 本章词汇` 24 条例句逐字一致（24/24，`not_verbatim=0`） | 8 条引语用 `/usr/bin/grep -F -c` 逐条核，全部 `count=1`：块 1↔`text:6`、块 2↔`:9`、块 3↔`:21`、块 4↔`:36`、块 5↔`:96`、块 6↔`:195`、块 7↔`:207`、块 8↔`:216`（与 `2-machine.json` 的 `pos=155/2229/3826/5097/6783/9858/14325/18695` 一致）。词表 24 条例句用 python3 逐条 `text.count(ex)` 核，`not_verbatim=0`（md:119–126／132–139／145–152）。 |
| **对应** | 8 块 × 固定三问，全部能在原文指出出处（8/8 通过） | ①动词主语：块 1「Diana had dreamed」＝Diana（`:6`）；块 2「She heard the door」＝Diana（`:9`）；块 3「she would say to herself」＝Diana（`:21`）；块 4「We’re meeting up」＝Diana（`:36`）；块 5「I watched them both go in」＝Diana（`:96`）；块 6「The conversation never changed」＝Carlos 的叙述层（`:195`）；块 7「She liked thinking about them」＝Diana（`:207`）；块 8「Diana stood up」＝Diana（`:216`）。②受事/宾语：块 4「Alba’s birthday」（`:36`）；块 6「her sister’s demands」（`:195`，`her sister`＝Alba）；块 7「the same criteria to reality as she did to fiction」（`:207`）；块 8「they had to get off the train」（`:216`）。③归属方向：块 2「which they’d put on first thing after moving in」＝共同安装（`:9`）；块 6「He backed her up and validated her feelings」＝Carlos → Diana（`:195`）；块 7「for the first time in two decades spent as a film critic and journalist」＝自述（`:207`）；块 8「between her and Carlos and the kids」＝空间方向（`:216`）。 |
| **形态** | 4 项子项（中文理解 / 关键词 / 为什么这样写 / 读者视角提示）× 8 块 = 32 个子项行，**缺 0**；引语行形态 `> **原句 N:** "…"` 8/8 合规；块数 8 ∈ [3,10]（profile novels）；导航 5 项齐全（md:11–15）；`## 本章词汇` 三档齐全（⭐⭐⭐ 8 / ⭐⭐ 8 / ⭐ 基础 8 = 24 条）；`## 一句话总结` 有正文（md:156）；H1 `# 04. Chapter 4` 符合本书 `N.` 形态 | `2-machine.json`：`h1_shape_ok=true`、`nav_count=5`、`nav_count_ok=true`、`subitems_modal`＝4 项、`blocks=8`、`block_median=7.0`、`block_range=[5,8]`、`profile=novels`、`profile_optional=[句子结构]`、`baseline book`；`struct_bad=0`、`hole=0`、`block_count` 空、`keyword_bad=0`、`cjk_low=0`、`empty_quote=0`、`segment_miss=0`。**形态偏离说明**：本章块间**有** `---` 分隔行（md:29/41/53/65/77/89/101），与全书多数章一致（ch12–ch15 无分隔行），不计入缺陷。 |
| **断言** | 24 条关键断言逐条回原文取证（24/24 有据，**0 条编造**，3 条措辞偏移＝提示档、1 条归属反转＝阻断档） | 见 §2 判定表 A1–A24；其中 A11（归属反转，md:27「对女儿演出的过高要求」）判「阻断」，A15／A16／A19 判「提示」，其余通过。 |

---

## §2 判定表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | md:11「吃妹妹 Alba 的生日饭」 | ch04:`text:36`（`[5166,5382)`）「We’re meeting up for Alba’s birthday. She invited me yesterday and I tried to get out of it…」 | 成立（`her sister`／`Alba` 的指向正确，见 §3⑤） | 通过 |
| A2 | md:11「戴上那副近视眼镜」 | ch04:`text:213`「She squinted, and it seemed that what the young man juggled was a knife.」＋`:216`「Once she found her glasses and put them on…」＋`:234`「"I put my glasses on."」 | 成立 | 通过 |
| A3 | md:11「认定有人在玩刀」 | ch04:`text:216`「But no, it wasn’t a trick of the eye. It was a knife.」 | 成立 | 通过 |
| A4 | md:11「站起来挤过人墙喊全家马上下车」 | ch04:`text:216`「Diana stood up. Without thinking twice, she pushed through the wall of bodies between her and Carlos and the kids. She yelled that they had to get off the train, now.」 | 成立 | 通过 |
| A5 | md:11「自己却卡在车门中间」 | ch04:`text:216`「Diana, behind them, was trapped inside, stuck halfway in the car until two other passengers managed to pry the metal doors apart.」 | 成立 | 通过 |
| A6 | md:12「把检查的循环从家里的门锁推到拥挤的车厢」 | ch04:`text:9`「She recognized the sound of the dead bolt, the second lock, and the third one…」＋`:96`「I was about to call the school and have them check that she was there, but I restrained myself」 | 成立 | 通过 |
| A7 | md:12「最低点是她在女儿学校门口那种明明记得却仍然不信的自我折磨」 | ch04:`text:96`（`[6602,7377)`）「I watched them both go in, I remember both moments. The images in my head are clear as could be. And still, I swear… Brisa hadn’t made it inside.」 | 成立 | 通过 |
| A8 | md:12／md:111／md:156「没做任何确认／没有先去确认／不再反复确认就行动」 | ch04:`text:216`「Once she found her glasses and put them on, she looked at him again, in case she’d been mistaken. But no, it wasn’t a trick of the eye.」——她先眯眼（`:213`）、再戴眼镜复看（`:216`） | 原文确有**两层自证**，「没做任何确认」与原文不符，且与 md:11「认定」自相矛盾（见 `3-diff.md` L1） | 提示 |
| A9 | md:13「控制型妹妹的套路在本章兑现——Alba 的要求从不商量」 | ch04:`text:195`「Alba’s decisions, which were always made unilaterally and without consideration of their effects on others or the effort they required.」＋「She complained about her sister’s demands」 | 成立；`her sister`＝Alba，方向正确 | 通过 |
| A10 | md:13「Carlos 看得一清二楚却插不上话」 | ch04:`text:195`「He could see very clearly Alba was holding Carmen hostage and intimidating the rest of them. But when he tried to convey that to Diana, it always played out the same way… Carlos became the bad guy for a bit.」 | 「看得一清二楚」成立；「插不上话」把原文「说了→被反推→成了坏人」的机制改写成性格（见 `3-diff.md` W3） | 提示 |
| A11 | md:27「后面对**女儿演出的过高要求**……都顺着这条线延伸」 | ch04:`text:195` 整段里所有「要求」的主语都是 Alba（`Alba's demands`／`Alba's decisions`／`Alba's impositions`）；Diana 对女儿**只有自责**（`:141`「I feel awful.」、`:150`「Fucking straightener.」），原文无任何「Diana 对女儿提要求」 | **归属方向反转**：要求的方向应是 Alba → 全家，不是 Diana → Brisa；等于凭空造出亲子压迫关系（见 `3-diff.md` W1） | 阻断 |
| A12 | md:13「母亲的话没人当真这一套也部分兑现」 | ch04:`text:21`（`[3284,4786)`）「When she tried to explain this to her mother, it made her feel crazy—Carmen would barely react, as if she couldn’t hear her, then change the subject.」 | 被无视的是 **Diana 的话**，不是母亲的话；方向调个个儿（见 `3-diff.md` L8） | 提示 |
| A13 | md:13「Carlos 追问的是她的视力，不是她的判断」 | ch04:`text:231`「"How is that possible? Are you sure it wasn’t something else?" He helped Diana roll up her sleeve. "You know how your vision is."」 | 成立 | 通过 |
| A14 | md:14「Carlos 劝她对 Alba 说不出不，到发现争不赢而认命上车」 | ch04:`text:189`「"You're already tired. I don't understand why you never tell her no."」＋`:195`「He knew it was better not to insist. And he also knew that, insist as he might, he would end up on the blue line headed toward Sant Ildefons.」 | 成立 | 通过 |
| A15 | md:14「末了还能拿她那张试衣间自拍开玩笑」 | ch04:`text:321`（`[23534,23598)`）「"Well, that and the selfie you sent her from the dressing room."」 | 成立；同行还有另一件糗事（`:300`「it's a sweater I bought for myself」＝买给自己的红毛衣），md 未提（见 `3-diff.md` L7） | 通过 |
| A16 | md:14「Brisa 与 Tomás 的天真落在抢圣诞节手工作品和追问匕首是什么上」 | ch04:`text:276`「The girl had torn the Christmas craft out of her brother’s folder.」＋`:279`「"Stop, Tomás, you're going to hurt your sister, and me as well."」＋`:354`「"What's a dagger?" asked Brisa.」 | 成立 | 通过 |
| A17 | md:15「第三人称限知在 Diana 与 Carlos 之间整段切换」 | ch04:`text:195`「Carlos went out to the dining room. He knew it was better not to insist.」 | 成立 | 通过 |
| A18 | md:15「车厢段落用穿了几层、拎了几袋的清单式排布制造窒息感」 | ch04:`text:204`「She was carrying her bag, the kids’ backpacks, their sketchbooks with their crafts in them, their end-of-semester projects.」＋`:231`「How much clothing do you have on? You must be sweating to death.」 | 成立 | 通过 |
| A19 | md:15「结尾把刀的高危收进一家人的插科打诨和一句站名纠正里」 | ch04:`text:363`「"People going around with knives in Cornellà. Maybe your mom is right—maybe you do think you're above this neighborhood."」＋`:372`「"Anyway, this isn't the Cornellà stop. It's L'Hospitalet."」 | 成立 | 通过 |
| A20 | md:99「她对女儿是否进门的反复怀疑……用的都是同一套标准」 | ch04:`text:96`＋`:207`（块 7 引文）「applying the same criteria to reality as she did to fiction」 | 「反复怀疑」成立（是**自己不信**女儿进没进去，不是对女儿提要求）；与 A11 同源，须一并改措辞 | 提示 |
| A21 | md:99「她顺口说出的那句「这对她意义重大」」 | ch04:`text:192`（`[9500,9560)`）「"It means a lot to her. And it's her birthday. It's normal."」——说话人是 **Diana**（承 `:186`/`:189` 的对话），`her`＝Alba | 归属方向：这是 Diana 替妹妹找的理由，与 md 的「她＝Diana 说出自己标准」读法冲突（见 `3-diff.md` W2） | 提示 |
| A22 | md:21「每次搬家都会去家具店比价，再去打听专业搬家的报价」 | ch04:`text:6`（`[6,1500)`）「Each time she moved, she’d check prices at furniture stores. Then she’d consult rates for professional movers who would pack up all her books with love.」 | 成立（块 1 引文逐字） | 通过 |
| A23 | md:27「书架是她给自己定的第一条标准线」 | ch04:`text:6`「Diana had dreamed for years of buying expensive shelving, real wood, solid and custom-made.」＋同段「Diana’s apartment was obsessively organized.」 | 成立 | 通过 |
| A24 | md:156「她又被妹妹的生日饭拖出门，在地铁上凭一副近视眼镜认定有人在玩刀」 | ch04:`text:36`＋`:213`＋`:216`（同 A1–A4 各条） | 成立 | 通过 |

---

## §3 收口复核（外层预审疑点的独立结论）

| 疑点 | 独立结论 | 依据 |
|---|---|---|
| ① md:13 的「控制型长姐」方向是否反了？ | **是反了，已修复**：Diana 是姐姐、Alba 是妹妹，父代理已把 md:13 改为「控制型妹妹」。本章另两处亲属表述（md:81「她抱怨妹妹的要求」、md:156「妹妹的生日饭」）方向均正确，**本章没有第二处亲属方向错误**。 | `ch02:129`「Only her older sister, Diana, insisted she go to a specialist…」；`ch05:549`「who was six years older than Alba」；`ch04:195` 的 `her sister`／`her sister's demands`／`his sister-in-law` 全指 Alba。 |
| ② 本章是否还有别的亲属方向错误？ | **没有**。逐处核过 `text/ch04:195` 内全部 sister 表述（`her sister` ×2、`her sister's demands`、`his sister-in-law`、`his mother-in-law`、`both of their daughters` 语境）以及 `:204`「her sister’s gift」、`:279`「your sister」（＝Brisa）、`:291`「Mom」（孩子口中的 Mom＝Diana，非 Carmen）。md 未把它们安到 Diana 身上。 | 同上；`/usr/bin/grep -n "sister\|mother-in-law\|Mom" text/ch04_chapter_4.txt` 全部命中行均在 `:195`/`:204`/`:279`/`:291`/`:300`/`:321`。 |
| ③ md:12／md:111／md:156「没做任何确认」是否成立？ | **不成立（提示）**：原文写她先眯眼（`:213`）、再戴眼镜复看（`:216`「looked at him again, in case she’d been mistaken」），确认后才站起。md 自己的 md:11「认定有人在玩刀」也说明她作过判断。 | `text/ch04:216` 逐字见 §2 A8。 |
| ④ md:99「她顺口说出的那句「这对她意义重大」」是谁说的？ | **Diana** 说的，句中的 `her`＝Alba；这是她替妹妹找的理由，不是她自己的标准。 | `text/ch04:192`；前两行 `:186`「"I don't have the energy to argue with her. I get so tired."」（Diana）、`:189`（Carlos「never tell her no」）。 |
| ⑤ md:13「母亲的话没人当真」方向对不对？ | **反了**：被无视的是 Diana 的话（`she tried to explain this to her mother`），母亲「几乎没有反应、像没听见、然后换话题」。 | `text/ch04:21` 逐字见 §2 A12。 |
| ⑥ md:27「对女儿演出的过高要求」是 Diana 对 Brisa 提的吗？ | **不是**。原文所有「要求」的主语都是 Alba（`Alba's demands`／`Alba's decisions`／`Alba's impositions`）；Diana 对女儿只有自责与「I feel awful」。这是本章唯一判**阻断**的项。 | `text/ch04:195` 逐字见 §2 A11；`/usr/bin/grep -nE "demand|insist|told Brisa|told Tom|told her daughter|asked Brisa" text/ch04_chapter_4.txt` 只命中 `:195` 与 `:354`。 |
| ⑦ 本章日期是平安夜当天吗？ | **不是**：本章是平安夜**前一天**（Alba 的生日），依 `:54`「Because tomorrow is Christmas Eve」；故 Alba 生日＝12 月 23 日。跨章：ch05＝这场生日聚会，ch10/ch15＝平安夜当晚。md 未写日期关系（漏，提示档）。 | `text/ch04:36`/`:54`/`:72`；`ch05:315`「two days before Christmas」、`ch05:567`「It's past four o'clock and we still haven't eaten lunch.」；`ch10:6`「There were five of them, not six.」 |
| ⑧ Carmen 在本章出场了吗？ | **没有**：本章 Carmen 只在 `:21`（Diana 的转述）与 `:195`（Carlos 的叙述层）里被提到，没有一句台词。md 全文 `Carmen` 命中 0 次，与原文一致，**不必**改。 | `/usr/bin/grep -nE "Carmen" text/ch04_chapter_4.txt` → 只命中 `:21`、`:195`；`/usr/bin/grep -c "Carmen" "ch04 chapter 4.md"` → 输出 `0`，退出码 1。 |
| ⑨ md 的「五个不是六个／戴眼镜点数」类情节是否串章了？ | **没有**：本章原文不含点数情节（那是 ch10 的 `:6`）；本章的 `glasses` 只出现在 `:213`/`:216`/`:234`/`:240` 四处，语义是近视眼镜，md 用法正确。 | `/usr/bin/grep -n "five of them\|pointed to every family member\|counting" text/ch04_chapter_4.txt` → 无输出、退出码 1；`/usr/bin/grep -nw glasses text/ch04_chapter_4.txt` → `:213`/`:216`/`:234`/`:240`。 |
| ⑩ md:13 的「控制型妹妹」是否与全书 trope 体例一致？ | **一致**：全书各章该行均为「 trope 名（带引号）＋本章兑现方式」的写法（ch05:13「「宝宝吞了硬币」的家庭乌龙被反用……」、ch10:13、ch15:13、ch17:13），ch04 本行不带引号属体例参差，记为提示级体例项，不单列缺陷条目。 | ch05:13、ch10:13、ch15:13、ch17:13 逐条比对。 |
| ⑪ 本章是否遗漏了重要原文事实？ | **是，8 处（漏，全部提示档）**：Alba 挟持母亲（`:195`）、Carlos 独生子/妻妹身份（`:195`）、拿刀者特征（`:216`）、Diana 被车门夹伤（`:222`/`:240`）、平安夜前一天的时点与「不能只买蛋糕」（`:54`/`:72`）、礼物是自己买给自己的红毛衣（`:300`/`:321`）、母亲对 Diana 的话无反应（`:21`）。已在 `3-diff.md` L1–L9 逐条给修法。 | 各条逐字与行号见 `3-diff.md` 一、漏（L）。 |
| ⑫ 词汇表 24 条例句是否逐字？ | **是**，24/24 逐字命中，`not_verbatim=0`；补写 L1–L9 不涉及词表，若顺手改词表须重跑。 | python3 逐条 `text.count(ex)` 核，输出 `vocab rows: 24 / not_verbatim: 0`。 |

---

## §4 已核实为正确（防误修清单）

以下 12 项已逐条回原文取证确认正确，**不得以「读着不对」为由改动**：

1. **md:11／md:81／md:156 的三处「妹妹」全部指 Alba**，方向正确 —— `text/ch04:36`「We’re meeting up for Alba’s birthday」、`:195`「her sister’s demands」；跨章 `ch02:129`「Only her older sister, Diana」。
2. **md:13「控制型妹妹」已经修好**（本轮口径：已修复，不重复报错）—— `ch02:129`＋`ch05:549`＋`ch04:195`「Alba's decisions, which were always made unilaterally」。
3. **md:12「明明记得却仍然不信」准确** —— `text/ch04:96`「I remember both moments. The images in my head are clear as could be. And still, I swear…」。
4. **md:13「Carlos 追问的是她的视力，不是她的判断」准确** —— `text/ch04:231`「Are you sure it wasn’t something else? … "You know how your vision is."」。
5. **md:14「Brisa 与 Tomás 的天真」两处细节准确** —— `text/ch04:276`（撕 Christmas craft）、`:354`（"What's a dagger?" asked Brisa）。
6. **md:15「第三人称限知整段切到 Carlos」准确** —— `text/ch04:195`「Carlos went out to the dining room.」。
7. **md:15「拎了几袋 / 穿了几层」准确** —— `text/ch04:204`「She was carrying her bag, the kids’ backpacks, their sketchbooks… their end-of-semester projects.」；`:231`「How much clothing do you have on?」。
8. **md:15「结尾一句站名纠正」准确** —— `text/ch04:372`「"Anyway, this isn't the Cornellà stop. It's L'Hospitalet."」；地名写法与全书一致。
9. **md:21／块 1 的中文理解与「查价—打听搬家—带着爱意搬走」三动作对应准确** —— `text/ch04:6` 逐字。
10. **md:27「书架是她给自己定的第一条标准线」准确** —— `text/ch04:6`「Diana had dreamed for years of buying expensive shelving…」。
11. **md:99「评判虚构的那套标准」这一说法本身准确** —— `text/ch04:207`「applying the same criteria to reality as she did to fiction」（块 7 引文逐字）。
12. **md 全章未出现任何本书没有的情节或数字** —— 8 条引语与 24 条例句全部逐字命中原文；md 全文阿拉伯数字仅见于 frontmatter、H1 与引语/例句内部，无自造数字（`/usr/bin/grep -nE "[0-9]" "ch04 chapter 4.md"` 命中行 md:3/4/7/19/31/43/55/67/79/91/103/149，全部可溯）。

---

**本判定只覆盖第 4 章；其余各章只有机器层，不写成「通过」。本轮未改动任何成品 md 文件，git 未执行任何操作（未 add / 未 commit / 未 push）。**
