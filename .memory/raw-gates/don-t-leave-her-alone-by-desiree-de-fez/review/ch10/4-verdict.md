# 第 10 章 R5 判定（人工审查）

**覆盖声明**：本次人工审查抽样了**第 7、8、10 章**（外层预审指定的三章），三章的 R0–R5 全流程均已跑完（`1-suread.json` → `2-machine.json` → `3-diff.md` → 本文件）。**第 1–6、9、11–17 章只有机器层，没有人工层，不写成「通过」**（`docs/rules/审查表.md:31`）。机器层唯一真值＝`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch10_chapter_10.txt`（原文，924 行，46,518 字符）；成品＝`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch10 chapter 10.md`（154 行，8 个引语块，22 条词汇）。审查人：DSH-Mac。

---

## 一、四组数（只报这四组）

| 组 | 数 | 依据 |
|---|---|---|
| 逐字 | **8 / 8** | 8 个引语块逐字命中原文（`2-machine.json`：`segments 8`、`segment_miss 0`、`quote_long 0`、`empty_quote 0`；自写脚本 `check_md_quotes.py`（ch10）：引语 MISS = 0、词汇例句 MISS = 0；引文起始字符位 986 / 12962 / 24251 / 30017 / 38509 / 43613 / 78274 / 80823，对应 `text/ch10` 行 6 / 156 / 204 / 210 / 384 / 438 / 786 / 810）。另：`本章词汇` 22 条例句全部是原文子串（phosphorescent:9、predetermined:9、autonomous:6、conflicted:6、conjecture:204、unmistakable:147、blood-streaked:147、half-deserted:6、trickled:6、haphazard:6、vignette:39、agitated:39、silhouettes:45、controllers:93、insisting:12、story:681、clinic:732、blanket:138、eyes:681、bingo woman:774、gift bag:216、kids:399）。 |
| 对应 | **8 / 8 块（24 问）** | R4 逐块对应走完 8 个块；每块固定三问（①每个动词的主语是谁 ②受事／宾语是谁 ③归属方向回原文看 by/to/from/of）＝24 问，全部有原文出处。导航 5 条、词汇 22 条、一句话总结 1 条另行逐句对账。 |
| 形态 | **0 偏离 ／ 1 假红** | `2-machine.json` `counts`：`struct_bad 0`、`keyword_bad 0`、`cjk_low 0`、`empty_quote 0`、`quote_long 0`；`form`：`h1_shape_ok true`、`h1 "10. Chapter 10"`、`nav_count 5`、`nav_count_ok true`、`blocks 8`、`block_median 7.0`、`block_range [5, 8]`、`subitems_modal`＝中文理解／关键词／为什么这样写／读者视角提示（与 `profile: novels` 一致）、`baseline: book`，`issues` 四组全空。机器层仅「关键词」子项 CJK=0 一项非零，与兄弟章同体例（关键词本就是英文短语）⇒ **假红**，非本章偏离。 |
| 断言 | **25** | 判定表 25 行：通过 11 ／ **阻断 1** ／ 提示 12 ／ 假红 1 ／ 跳过 0。 |

---

## 二、判定表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 8 个引语块与原文逐字一致 | `2-machine.json` `quotes[].segments[].ok=true`（8/8，segments 8 / segment_miss 0） | 通过 | — |
| 2 | `本章词汇` 22 条例句均为原文子串 | 自写脚本 `check_md_quotes.py`（ch10）：词汇例句 MISS = 0（逐条行号见「四组数」行） | 通过 | — |
| 3 | 块 1（`md:19-27`）对应「点数、五个不是六个」 | `text/ch10:6`「She took out her glasses and put them on, and pointed to every family member, counting. There were five of them, not six. Alba was missing.」 | 通过 | — |
| 4 | 块 2（`md:31-39`）说「突然平静」出自 **Juan 的转述**，平静的是母亲 | `text/ch10:156`「Then, I don’t know why, she suddenly got very calm. One second to the next. I almost lost it. It was so weird, like she’d been injected with morphine or something.」；`:138`「Carmen, meanwhile, was stretched out on the grass several meters away.」 | 通过 | — |
| 5 | 块 3（`md:43-51`）是 **Carlos** 的判断，且「这三个人」指 Diana／Carmen／Alba | `text/ch10:204`「Carlos couldn’t make sense of it… They did know was conjecture or intuition, not the result of something shared.」；`:204`「Each day the three would trade summaries…」 | 通过 | — |
| 6 | 块 4（`md:55-63`）说「母亲把梦想押在 **Diana** 身上」 | `text/ch10:210`「Up until Tomás was born, Carmen had a bit of a weakness for Diana. She’d projected her dreams onto her.」；同段点名 "After her first child, Diana turned into a pumpkin." | 通过 | — |
| 7 | 块 5（`md:67-75`）说这句断言是 **Diana 对母亲**说的，被断言者是 Alba | `text/ch10:384`「"Mom! Don’t change the subject… How is it possible that she still thinks Camp La Tortuga Ligera is the most amazing place on earth?… I think she’s still there."」 | 通过 | — |
| 8 | 块 6（`md:79-87`）的广告牌异变发生在 **Alba 的露台** | `text/ch10:438`「Days before Splau had swallowed her up, Alba went out to the patio… The yellow M on its red background liquefied… She went inside and shut the curtains.」 | 通过 | — |
| 9 | 块 7（`md:91-99`）说「蜡烛摆成圆圈、全场唱起古怪的歌」出自 **Diana 的目击** | `text/ch10:786`「Then the bingo woman put the candles in a circle and lit them, and everyone started chanting a very strange song, even the woman who had been crying. It seemed like they were praying.」；`:690`「They were out there sitting at that stone table on their lot…」 | 通过 | — |
| 10 | 块 8（`md:103-111`）「三十年」是 Diana 自己的口径；母亲的反应是夸她会写 | `text/ch10:330`「"Fifteen? More like thirty."」（Diana）；`:327`「"Oh, come on—that was fifteen years ago, at least."」（Carmen）；`:810`「"I just told you, thirty years later, and still you don’t believe me."」；`:801`「"Boy, you are a writer, aren’t you."」 | 通过 | — |
| 11 | md 无凭空造出的情节／关系／数字 | 5 条导航、8 块×4 子项、22 条词汇、一句话总结逐条回原文核对，全部能落到本章原文 | 通过 | — |
| 12 | `md:14`「戴上手镜点数」——原文是眼镜（glasses），且与 `md:21` 自相矛盾 | `text/ch10:6`「She took out her glasses and put them on」；`/usr/bin/grep -nw 'mirror' text/ch10_chapter_10.txt` → 无输出，退出码 1；`/usr/bin/grep -nw 'glasses' …` → `:6`，退出码 0 | 与原文不符 | **阻断** |
| 13 | `md:14`「用双手做成取景框」——原文是手搭的挡光板 | `text/ch10:9`「Diana made blinders with her own hands—still bloodstained—so she could concentrate on that image…」 | 表述不符 | 提示 |
| 14 | `md:14`「Carlos 是把这家族病症说破的那个人」——原文是他心里想通，没有人听见 | `text/ch10:204`（叙述层认知）；`:162`「Juan turned to Carlos, perplexed. "I tell her all that, and what, nothing? Not a single question?"」 | 表述不符 | 提示 |
| 15 | `md:57`「可她一有了孩子」——两个「她」夹两个「母亲」，易被读成母亲生了孩子 | `text/ch10:210`「After her first child, Diana turned into a pumpkin.」⇒ 有了孩子的是 Diana | 表述歧义 | 提示 |
| 16 | `md:154`「讲完了，母亲还是不信」——Carmen 没有表示不信 | `text/ch10:801`「"Boy, you are a writer, aren’t you."」；`:807`「"But you were always so scared. Why didn’t you say anything?"」；`:810`「still you don’t believe me」（Diana 自己的话） | 表述不符 | 提示 |
| 17 | `md:75`「对方人回来了」易被读成字面回营地 | `text/ch10:384`「I think she’s still there.」（there 指那年的夏天） | 表述歧义 | 提示 |
| 18 | 同章 Juan 的中文名与西文名混用 | `md:12`「胡安」；`md:15`、词汇表 `:137`／`:138` 用「Juan」；同书 `ch14 chapter 14.md:12`、`ch17 chapter 17.md:6`、`00_情感节点.md:1` 用「胡安」 | 体例不齐 | 提示 |
| 19 | 车身上的血手印与车底那块血布未进 md | `text/ch10:147`「A handprint, the fingers spread wide, made a broken path from one side door to the trunk.」；`:168`「I tried to apply pressure with a blanket we had in the back. That's what you see underneath the car.」；`/usr/bin/grep -cE '手印\|车底\|后备箱\|血布' "ch10 chapter 10.md"` → 0，退出码 1 | 漏（覆盖缺口） | 提示 |
| 20 | Juan 讲的走散经过（商场走散、手机在他手里、MediaMarkt 手柄）只以词汇例句出现 | `text/ch10:87`「She doesn’t have her phone. It happened so fast. We got separated inside.」；`:93`「I’m convinced she went back to MediaMarkt to ask about the Switch controllers.」；`:111`「"Because I have it."」；md 中 `MediaMarkt` 仅出现在 `md:137` 词汇例句 | 漏（覆盖缺口） | 提示 |
| 21 | 仪式里的「光柱、深粉近紫、震动」未进 md | `text/ch10:792`「there was light shooting up from the table, over the trees and into the sky. A deep pink, almost purple. And everything started to vibrate.」；`/usr/bin/grep -cE '光柱\|震动\|粉\|紫' "ch10 chapter 10.md"` → 0，退出码 1 | 漏（覆盖缺口） | 提示 |
| 22 | Alba 的露台是营地的复制品这一层未进 md | `text/ch10:414`「her patio is basically a replica of the campsite」；`:435`「As Diana said, it was a miniature of La Tortuga… Alba’s patio looked out over the B-20 beltway.」；`/usr/bin/grep -cE '复制\|露台' "ch10 chapter 10.md"` → 0，退出码 1 | 漏（覆盖缺口） | 提示 |
| 23 | 父亲夜访 Diana 家（烟味）未进 md | `text/ch10:558`「"By the way, he was at my house the other night."」；`:576`「The bathroom smelled like it did after he’d been in there—like cigarettes.」；`:588`「At four in the morning? No way… It was Dad.」；`/usr/bin/grep -cE '父亲\|爸爸\|卫生间\|烟味' "ch10 chapter 10.md"` → 0，退出码 1 | 漏（覆盖缺口） | 提示 |
| 24 | Carmen 主动断言「她已经很多年没有单独待过了」未进 md | `text/ch10:276`「"She hasn’t been alone in years," Carmen said after a long pause.」；`:288`「"That Alba is never alone."」；`/usr/bin/grep -cE '独处\|从不\|单独' "ch10 chapter 10.md"` → 0，退出码 1 | 漏（覆盖缺口） | 提示 |
| 25 | 「关键词」子项 CJK=0 是否形态偏离 | `2-machine.json` `blocks[].cjk.关键词 = 0`；同体例见 `ch03 chapter 3.md:23`、`ch04 chapter 4.md:23` | 与兄弟章同体例，非偏离 | 假红 |

---

## 三、收口复核

1. **施事／归属三问（逐块走完 8 块）**
   - 块 1（`md:19`）：`text:6`「She took out her glasses… pointed to every family member, counting.」——点数的人是 **Diana**，被点的人里缺席的是 **Alba**；md:21「少掉的那位是妹妹」归属正确。
   - 块 2（`md:31`）：`text:156` 这段话是 **Juan** 在讲（"I tell her all that…"），被描述为「突然平静」的是 **Carmen**；md:33「他转述母亲的变化」归属正确。
   - 块 3（`md:43`）：`text:204`「**Carlos** couldn’t make sense of it」——判断者是 Carlos，「这三个人」＝Diana／Carmen／Alba（`:204`「Each day the three would trade summaries」）；md:45「他完全想不通」正确。
   - 块 4（`md:55`）：`text:210`「**Carmen** had a bit of a weakness for **Diana**. She’d projected her dreams onto her.」——做梦的是母亲，承受的是 Diana；md:57 主干正确（代词歧义见判定表 #15）。
   - 块 5（`md:67`）：`text:384` 说话人是 **Diana**（称母亲 "Mom!"），被断言「还在那里」的是 **Alba**；md:69「她断言，对方其实还留在那里」归属正确。
   - 块 6（`md:79`）：`text:438` 主语是 **Alba**（「Alba closed her eyes for a moment… She went inside and shut the curtains.」）；这是 Alba 视角的转述层，md 未误算成 Diana 的动作，正确。
   - 块 7（`md:91`）：`text:786` 说话人 **Diana**（对母亲说），动作主体是 **bingo 女人**（摆蜡烛）＋全场（唱）；md:93「那个和宾果牌局绑在一起的女人把蜡烛摆成一个圆圈点燃，所有人跟着唱」归属正确。
   - 块 8（`md:103`）：`text:810` 说话人 **Diana**；`:801` 的「你真会写」是 **Carmen**；md:105／`md:111` 归属正确。
   - ⇒ **八块均无施事反转**；本章的归属风险集中在导航句 `md:14` 与 `md:154`（判定表 #12、#16）。
2. **人数／计数断言**：本章 md 的数字只有「五个，不是六个」（`md:21`／`md:25`，对应 `text:6`）、「三十年前」（`md:105`／`md:109`，对应 `text:330`／`:810`）、「九点过后」（`md:11`，对应 `text:6`「It was after nine」），逐条回原文均对得上；**md 未出现「三个孩子」类会出错的计数断言**。
3. **跨章指认**：md 正文无指向其他章的事件描述；跨书事实只有 Juan 的中文名「胡安」（判定表 #18）。亲属方向复核：`text/ch05_chapter_5.txt:549`「who was six years older than Alba」、`text/ch02_chapter_2.txt:129`「Only her older sister, Diana…」、`text/ch17_chapter_17.txt:96`「even with six years between them」⇒ **Diana 是姐姐、Alba 是妹妹**，md 全章方向正确；`text/ch14_chapter_14.txt:9` 的 "younger daughter" 指 Alba。
4. **草地上两个女人的身份**：`text:60`（一行内）「**Carmen**, meanwhile, was stretched out on the grass several meters away.」＋ `:201`「Carlos looked for Diana and saw she was stretched out next to her mom, in the same position.」⇒ 是 **Carmen 与 Diana**，Alba 不在场；md `md:12`「两个被剖开肚子的女人躺在草地上」正确（Alba 的缺席由 `md:11`「妹妹 Alba 不在」承担）。
5. **未写出的报警**：`text:168`、`:219`、`:759`、`:843`、`:849`、`:861` 都在谈 call the police / one-one-two，本章未写警报已发出；md `md:154` 未称已报警，正确。

---

## 已核实为正确

以下写法在审查中看似有误，回原文逐字核对后**成立**，任何后续改稿都不得改动（`docs/rules/审查表.md` R5.5）：

1. **`md:21`「少掉的那位是妹妹」方向正确**。依据：`text/ch10:6`「Alba was missing.」＋ `text/ch05_chapter_5.txt:549`「who was six years older than Alba」。
2. **`md:12`「两个被剖开肚子的女人躺在草地上，一个玩消除游戏，一个讲三十年前的旧事」正确**。依据：`text/ch10:138`「She was stretched out with her legs crossed… With her free hand, she was playing Candy Crush.」＋ `:201`「she was stretched out next to her mom, in the same position.」；讲旧事的是 Diana（`:603`「I’ll tell you the camper story」）。
3. **`md:33`「他转述母亲的变化」归属正确**。依据：`text/ch10:156`（Juan 的转述，被描述者是 Carmen）＋ `:138`（Carmen 躺在草地上）。
4. **`md:39`「被形容为平静的，是那个此刻正躺在草地上、肚皮上全是血块的人」正确**。依据：`text/ch10:156`「Her stomach is destroyed. It’s all bits of skin and blood clots.」（Juan 描述 Carmen 的腹部）＋ `:138`（Carmen 躺在草地上玩 Candy Crush）。
5. **`md:45`「这三个人天天说话，却其实什么也没说」正确**。依据：`text/ch10:204`「Each day the three would trade summaries… Yet they never discussed anything important.」
6. **`md:57`「母亲曾花了多年催她长大、催她走出去闯荡」正确**。依据：`text/ch10:210`「Carmen had spent years encouraging her to grow, to get out」。
7. **`md:69`「她断言，对方其实还留在那里」正确**。依据：`text/ch10:384`「I think she’s still there.」（说话人 Diana，被断言者 Alba）。
8. **`md:81`「那块麦当劳广告牌上的黄色标志化开了……上面画着一只奔跑的海龟——那是露营地的广告牌」正确**。依据：`text/ch10:438`「The yellow M on its red background liquefied, trickling downward and leaving behind just a white billboard with red text and a running turtle—the billboard for La Tortuga Ligera.」
9. **`md:87`「这里她看见就回避：窗帘一拉上，回忆立刻倒回三十年前」正确**。依据：`text/ch10:438`「She went inside and shut the curtains.」＋ `:633`「that would be their last year at Camp La Tortuga Ligera」。
10. **`md:93`「那个和宾果牌局绑在一起的女人把蜡烛摆成一个圆圈点燃，所有人跟着唱起一支古怪的歌」正确**。依据：`text/ch10:786`「the bingo woman put the candles in a circle and lit them, and everyone started chanting a very strange song」＋ `:534`「She would host bingo at her camper on Fridays. Do you remember? Women’s bingo.」
11. **`md:99`「仪式本身她从头到尾没看清，这就是她讲不清楚的根源」正确**。依据：`text/ch10:792`「because the bingo woman had her back to me, and I couldn’t really see」＋ `:798`「"Only you saw it?"… "Yeah, that’s the weird part…"」。
12. **`md:111`「母亲听到这一段的反应不是害怕，而是先夸了一句她真会写，接着才问她当年为什么不说——从头到尾没有追问一句这到底是不是真的」正确**。依据：`text/ch10:801`「"Boy, you are a writer, aren’t you."」＋ `:807`「"But you were always so scared. Why didn’t you say anything?"」。
13. **`md:11`「Splau 商场已经关门」与「九点过后」正确**。依据：`text/ch10:6`「It was after nine, and the area around Splau, which was now closed, was practically empty.」
14. **机器层「关键词」子项 CJK=0 不是本章缺陷**。依据：`ch03 chapter 3.md:23`、`ch04 chapter 4.md:23` 的「关键词」子项同样全为英文短语 ⇒ 全书体例，非形态偏离。
