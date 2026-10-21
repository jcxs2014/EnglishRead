# ch17 判定表（R5）

- 审查对象：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch17 chapter 17.md`（153 行）
- 唯一真值：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch17_chapter_17.txt`（3,232 词 / 18,353 字符 / 19,155 字节 / 378 行）
- 底稿：`review/ch17/1-suread.json`（R1 素读）、`review/ch17/2-machine.json`（R2 机器层）、`review/ch17/3-diff.md`（R3 三单 + R4 逐块）
- 章型：末章 → 重 S5（总结层 / 总览层）；审查员 DSH-Mac（**本轮只出指令不改稿**）
- 判定表列：`断言 | 证据（章:区间） | 结论 | 档位`；四档＝**阻断 / 提示 / 假红 / 跳过**；「通过」行的档位记作 `—`
- 机器层：`bash scripts/chapter.sh … --json` 退出码 **0**（0 无阻断 / 1 阻断 / 2 无法判定；2 才不是通过），verdict `ok`，8 块引语 `ok:true`，`segment_miss=0`、`struct_bad=0`、`keyword_bad=0`、`cjk_low=0`
- ⚠ 机器全绿不等于本章合格：下面 5 条阻断全部落在 **S5 总结层 / R4 对应层**，机器探针查不到

---

## A. 逐字（引语逐字 / 例句逐字 / 措辞逐字）

| 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|
| A1 8 个原句引语均为原文逐字，无改写、无吞词 | `text/ch17_chapter_17.txt:6,33,39,48,96,201,279,366`；`2-machine.json`（8/8 `ok:true`、`segment_miss=0`） | ✅ 成立 | — |
| A2 词汇表 21 条例句全部在原文出现且逐字一致 | Python 脚本（NFKC＋引号归一＋空白归一）核 `text/ch17_chapter_17.txt`：`vocab rows checked=21 verbatim_ok=21 miss=0` | ✅ 成立 | — |
| A3 `md:87`「还有两个女儿**同一分钟流鼻血**」——"同一分钟"与原文的 "at the same time" 不等，且原文是"约一个月前" | `text/ch02_chapter_2.txt:468` `About a month ago, the girls’ noses had both bled dramatically, in different places and situations but at the same time.`（另 `:462` `Alba and Diana often got nosebleeds, and that was just one of the alerts their bodies would send them.`） | 事件有据，措辞走样（"同一分钟"过窄，且跨章未注） | 提示 |

## B. 对应（这段中文是不是在讲这句引语）

| 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|
| B1 `md:111` 把章节"结尾"钉在副歌歌词「结尾那句"你在忘记我"…它会变成一句指控」；**原文末句是母亲一句关于空气炸锅的家常话，成品里零出现**，且 `md:11`／`md:153` 两处总结都收在"谜团正中间"的悬置上 | `text/ch17_chapter_17.txt:366`（副歌）→ `:372` `“Diana!” Carmen yelled.` → `:375` `“What?”` → `:378` `“Why don’t you get an air fryer like the one your sister has?”`；md 侧 `/usr/bin/grep -inE 'fryer|空气炸锅|炸锅' "ch17 chapter 17.md"` → 命中 0、退出码 1 | 末章收束位置判错：把刻意的轻描淡写读成"指控/悬疑"，且末句整句漏 | **阻断** |
| B2 原句1 引语止于 "…flushed and very tired."，`md:21` 却讲到引语外的"深夜再折回商场接那三个女人" | `text/ch17_chapter_17.txt:6` 全句（含 `Then, sometime after midnight, Juan went back to Splau for the women…`） | 引语选短（中文超出了引语覆盖范围） | 提示 |
| B3 原句2 引语止于球鞋句，`md:33` 却讲到引语外的"三个女人都得换，因为孩子们不能看见她们这副样子" | `text/ch17_chapter_17.txt:33` 后半 `“All three of you should. The kids can’t see you like this. You can put all your clothes in the washer. …”` | 同上 | 提示 |
| B4 `md:21`「胡安先把卡洛斯和孩子们**送回家**」 | `text/ch17_chapter_17.txt:6` `they went to Alba’s apartment in two shifts. First Juan took Carlos and the kids.` | 目的地是 Alba 家的公寓，非卡洛斯家 | 提示 |
| B5 `md:57`「她住的公寓正好夹在中间，**离两个出口都不远**」 | `text/ch17_chapter_17.txt:48` `Her apartment was right in the middle, two exits away from each shopping center.` | `two exits` 是距离（离两个商场**各**两个出口），被读成"两个出口都不远" | 提示 |
| B6 `md:39`「**真正的决定权始终握在三个女人手里**」 | `text/ch17_chapter_17.txt:33` `“All three of you should. The kids can’t see you like this. You can put all your clothes in the washer. …”`；`:57` `Juan made them promise they’d come back out only when they had cleaned up.`；唯一一次顶回是 `:36` `“I’m not exhausted,” Alba said.` | 越界解读（Juan 才是发号施令的一方） | 提示 |
| B7 `md:75`「卡洛斯是本章**唯一**觉得"不对"的成年人」 | `text/ch17_chapter_17.txt:183` `He thought it odd that Alba, who was still breastfeeding, wanted champagne.`；`:186` `they were trying—unsuccessfully—to process what had happened that night.` | 越界解读（Juan 同样在察觉与消化） | 提示 |
| B8 `md:109`「歌词里"**她已不在你身边**"」被当引语引用 | `text/ch17_chapter_17.txt:366` 引语四句为 `“ ‘I dream of you—what have you given me? Without your love, I would never have believed. I dream of you—what have you given me? I long for you, you’re forgetting me.’ ”` | 释义当引文 | 提示 |
| B9 固定三问 8/8 块施事方向正确（无"施事/归属反转"型错误） | 例：`:39`（Juan 捧脸检查 → Alba 抓手腕制止）对应 `md:45`；`:96`（Carlos 察觉 → Alba 散开发遮耳朵）对应 `md:69`；`:201`（Alba 提问 → Diana 领悟）对应 `md:81`；`:279`（me＝母亲 Carmen）对应 `md:93`；`:366`（they＝母女三人）对应 `md:105` | ✅ 成立 | — |

## C. 形态（H1 / 导航 / 子项 / 块数）

| 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|
| C1 H1 形态合规 | `2-machine.json`：`h1="17. Chapter 17"`、`h1_shape_ok=true` | ✅ 成立 | — |
| C2 本章导航 5 项齐全；每块四子项（中文理解/关键词/为什么这样写/读者视角提示）齐全 | `2-machine.json`：`nav_count=5 ok`、`subitems_modal=[中文理解, 关键词, 为什么这样写, 读者视角提示]`、`struct_bad=0`、`cjk_low=0` | ✅ 成立 | — |
| C3 块数 8 落在本书区间内 | `2-machine.json`：`blocks=8`、`block_median=7.0`、`block_range=[5,8]`（baseline=book） | ✅ 成立（但见 C4） | — |
| C4 修 B1（补末句）时**不得新增第 9 个原句块** | `2-machine.json`：`block_range=[5,8]`，本章已 8 块（上限） | 修复约束：末句应并入原句8 的读者视角提示与两处总结 | 提示 |

## D. 断言（总结层 / 总览层的人物、情节、时序、跨章指向）

| 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|
| D1 `md:11`「**三个浑身是血的女人分两趟回到阿尔巴家**」——主语错绑 | `text/ch17_chapter_17.txt:6` `they went to Alba’s apartment in two shifts. First Juan took Carlos and the kids. … Then, sometime after midnight, Juan went back to Splau for the women` | 分两趟的是**全体**；三个女人只在第二趟（`md:21` 块内反而写对了） | 提示 |
| D2 `md:11`「…**姐妹俩才明白这不是错觉**…」与 `md:153`「…**姐妹俩才明白那些东西是真的**…」——原文写的是相反的人物状态 | `text/ch17_chapter_17.txt:201` `She still didn’t understand, but it didn’t really matter.`；`:228` `Now it was Alba who was confused, but instead of asking questions, she tried to steer the topic back in her favor.` | 两个女儿都"明白了"与原文直接冲突（Diana "still didn't understand"、Alba "was confused"） | **阻断** |
| D3 `md:153`「而戴安娜**也在同一刻发现**，自己一直站在谜团正中间」——把两个节拍并成"同一刻"，并压平了顺序 | `text/ch17_chapter_17.txt:201`（Alba 提问 → Diana 领悟）早于 `:279`（母亲讲那一夏的营地口述）；`:366`（副歌）更在其后 | 时序并置错误 | **阻断** |
| D4 `md:51`「阿尔巴在商场里说手柄"只是有点脏"」——原文无此台词、无此场景 | 全书查无：`/usr/bin/grep -inE 'dirty' text/*.txt` → 仅 `text/ch02_chapter_2.txt:312`、`text/ch08_chapter_8.txt:192`、`text/ch08_chapter_8.txt:207`（退出码 0，全与手柄无关）；原文 `text/ch17_chapter_17.txt:48` `She slid the Switch controllers out of her pocket, wiped them off with a towel lying nearby, and put them in the giant trash bag…`（自家阳台、默默、无台词） | 编（凭空台词＋场景错位） | **阻断** |
| D5 `md:75`「…那是**下一章**两个男人在车里抽烟时要说的话」——本书没有下一章 | `ls text/` → 只有 `ch00_prologue.txt`…`ch17_chapter_17.txt`（18 个），md 侧同为 `ch00`…`ch17`；该场景实际在 `text/ch14_chapter_14.txt:156` `They left the car, and Juan lit a cigarette. Carlos asked for one.` | 编（指向不存在的下一章） | **阻断** |
| D6 `md:13`「完美靠谎话维持——藏血衣、藏耳朵、**藏疤、藏触手**」 | `text/ch17_chapter_17.txt:48`（手柄藏进垃圾袋）、`:33`（血衣进洗衣机）有据；但本章触手是**被说出口**的：`:282` `“It was a tentacle, Mom,” said Alba. “I had two.”` | "藏触手"只对 Juan / Carlos 成立，导航句未点明，易被读成"三人互相隐瞒" | 提示 |
| D7 母亲"营地阿姨"线（bingo lady／让它们出来的人／那一夏至少还有三人）零命中 | `text/ch17_chapter_17.txt:216` `“The bingo lady and her friends. The women who played bingo at her camper.”`；`:234` `“But they helped. Not just me—a lot of the women there. At least three others that summer alone.”`；`:255` `“They thought it was best to let them out, but they’d listen to your reasons… they’d tell you how to contain them—or if they were already partway out, how to get rid of them.”`；md 侧 `/usr/bin/grep -cE 'bingo|Tortuga|营地|阿姨' "ch17 chapter 17.md"` → 0/0/0/0，退出码 1 | 漏（本章最大的世界观翻面未收；母亲口述只取了"小尾巴/触手"半边） | 提示 |
| D8 Alba 吃止痛药 / 纱布胶布 / 次日必须去 urgent care 零命中 | `text/ch17_chapter_17.txt:96` `…patching them up with gauze and tape, and she had even taken a painkiller—rare for her, since she avoided medication at all costs. But it hurt. She knew she’d have to go to urgent care tomorrow—Christmas…`；md 侧 `/usr/bin/grep -cE '止痛|胶布|紧急门诊' "ch17 chapter 17.md"` → 0/0/0，退出码 1 | 漏（三个女人的身体状况只收了一半） | 提示 |
| D9 「65 寸电视 / 其实更像 75 寸」零命中 | `text/ch17_chapter_17.txt:75` `Carlos again looked away from the sixty-five-inch screen, thinking that number seemed too small, that it had to be more like seventy-five.`；`:186` `…watching a televised Christmas gala on the sixty-five-inch TV.`；md 侧 `/usr/bin/grep -cE '电视|英寸' "ch17 chapter 17.md"` → 0/0，退出码 1 | 漏（末章两个数字） | 提示 |
| D10 Juan 的 Santa 说辞 / 孩子反复出来问 Santa 零命中 | `text/ch17_chapter_17.txt:57` `He explained that Santa might pass them by if he saw them playing in their bedroom so late.`；`:186` `…they came out every few minutes for snacks, or to ask when Santa would show up.`；md 侧 `grep -cE 'Santa|圣诞老人'` → 0/0，退出码 1 | 漏（给孩子的圣诞夜掩护这条日常线） | 提示 |

## E. 未核（跳过档，不作阻断依据）

| 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|
| E1 词汇表档位（⭐⭐⭐/⭐⭐/⭐）是否存在"基础词进高档"的注水 | 未系统核（按 S5 加权非本章重点；机器层 `keyword_bad=0` 只保证例句逐字） | 未核 | 跳过 |
| E2 歌词 "I Dream of You" 所指的女孩究竟是谁、与 ch13/ch16 的跨章考据 | 未核（跨章考据，不影响本章判定） | 未核 | 跳过 |

---

## 报数（只报四组）

| 组 | 行数 | 阻断 | 提示 | 假红 | 跳过 | 通过 |
|---|---|---|---|---|---|---|
| **逐字** | 3 | 0 | 1 | 0 | 0 | 2 |
| **对应** | 9 | **1** | 7 | 0 | 0 | 1 |
| **形态** | 4 | 0 | 1 | 0 | 0 | 3 |
| **断言** | 10 | **4** | 6 | 0 | 0 | 0 |
| **判定表合计** | **28** | **5** | **15** | **0** | **2** | **6** |
| 附：未核（跳过档，单列不计入四组） | 2 | — | — | — | 2 | — |

- 四档合计校验：阻断 5 ＋ 提示 15 ＋ 假红 0 ＋ 跳过 2 ＋ 通过 6 ＝ 28 行 ✔
- 机器层假红：0（chapter.sh 退出码 0，verdict `ok`，8/8 块 `ok:true`；工具未误报任何一条）
- 人工判定与机器判定差：**机器 0 阻断 vs 人工 5 阻断**，5 条全部在 S5 总结层 / R4 对应层 / 跨章断言层，机器探针覆盖不到

---

## R5-补 · 取证命令（显式路径 / -E / 命令＋输出＋退出码）

工作目录：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/`（`text/` 被 .gitignore，**全程 `/usr/bin/grep`，未用 git grep**）

```
$ /usr/bin/grep -inE 'fryer' text/*.txt
text/ch17_chapter_17.txt:378:“Why don’t you get an air fryer like the one your sister has?”
→ 命中 1；退出码 0
$ /usr/bin/grep -inE 'fryer|空气炸锅|炸锅' "ch17 chapter 17.md"
（无输出）→ 命中 0；退出码 1

$ /usr/bin/grep -inE 'dirty' text/*.txt
text/ch02_chapter_2.txt:312:…so I wouldn’t get my butt dirty.
text/ch08_chapter_8.txt:192:…I didn’t want to get the car dirty.
text/ch08_chapter_8.txt:207:Dirty with what?
→ 命中 3，均与"手柄"无关；退出码 0

$ ls text/
ch00_prologue.txt … ch17_chapter_17.txt（共 18 个，无 ch18）→ 无"下一章"可对照

$ /usr/bin/grep -inE 'cigarette|smoking' text/*.txt
text/ch14_chapter_14.txt:156:They left the car, and Juan lit a cigarette. Carlos asked for one.
→ 命中（含 ch10:192）；退出码 0

$ /usr/bin/grep -inE 'bingo|La Tortuga|let them out|At least three' text/ch17_chapter_17.txt
text/ch17_chapter_17.txt:210 / :216 / :234 / :255 → 命中 4；退出码 0
$ /usr/bin/grep -cE 'bingo|Tortuga|营地|阿姨' "ch17 chapter 17.md"
0 / 0 / 0 / 0 → 退出码 1

$ /usr/bin/grep -inE 'painkiller|urgent care|gauze' text/ch17_chapter_17.txt
text/ch17_chapter_17.txt:96 → 命中 1；退出码 0
$ /usr/bin/grep -cE '止痛|胶布|紧急门诊' "ch17 chapter 17.md" → 0/0/0；退出码 1

$ /usr/bin/grep -inE 'sixty-five-inch|seventy-five' text/ch17_chapter_17.txt
text/ch17_chapter_17.txt:75 / :186 → 命中 2；退出码 0
$ /usr/bin/grep -cE '电视|英寸' "ch17 chapter 17.md" → 0/0；退出码 1

$ /usr/bin/grep -inE 'Santa' text/ch17_chapter_17.txt
text/ch17_chapter_17.txt:57 / :186 → 命中 2；退出码 0
$ /usr/bin/grep -cE 'Santa|圣诞老人' "ch17 chapter 17.md" → 0/0；退出码 1

$ /usr/bin/grep -inE 'nose' text/*.txt
text/ch02_chapter_2.txt:357 / :462 / :468 → 命中 3；退出码 0

# 词汇 21 条例句逐字（Python，NFKC＋引号归一＋空白归一）
vocab rows checked=21 verbatim_ok=21 miss=0
```

---

## 已核实为正确

以下写法"看起来像错"，回原文核对后成立，不作缺陷记录（每条给出 text/<文件>:<行> 与原文）：

| # | 成品写法 | 原文（逐字） | 核对结论 |
|---|---|---|---|
| V1 | `md:11`／`md:57`「两个商场广告牌夹住她家」「一块是芬斯特雷列斯商场，一块是斯普劳」 | `text/ch17_chapter_17.txt:48` `they’d changed the billboards. One was for the Finestrelles mall and the other for Splau. Her apartment was right in the middle, two exits away from each shopping center.` | ✅ 空间细节与原文一致（唯一瑕疵是 B5 的"两个出口"措辞） |
| V2 | `md:63`「它和序章那家童趣店、第十二章她醒来的那间店是同一个商圈」 | `text/ch00_prologue.txt:12` `She came to in the dark… soon the whole store was lit up.`、`:18` `…The sight of it, in her daughter’s favorite store, where Brigitte mistook cheap jewelry for the real thing…`；`text/ch11_chapter_11.txt:6`（Splau 商场）、`:126` `The store with the lights on was, in fact, Claire’s, where they sold cheap costume jewelry, trinkets, and accessories, mostly for kids and teenagers.`；`text/ch12_chapter_12.txt:174` `What kind of person cries at Claire’s?`、`:240`（Alba 跟到店门口） | ✅ 成立：序章与第十二章是同一家 Claire's（位于 Splau 商场内）＝与两块广告牌同一个商圈 |
| V3 | `md:61`「家就卡在**夺走手柄的商场**和出事的那栋楼之间」 | `text/ch02_chapter_2.txt:126` `That day’s mission was to exchange a couple of Switch controllers for her eldest… The excursion to Finestrelles was supposed to be the happy ending to seven days of phone calls…` | ✅ 成立：手柄是 Finestrelles 那天丢的（＝广告牌里的 Finestrelles mall） |
| V4 | `md:99`「这段是"口述版"，而**第十一章、十二章是阿尔巴自己看见的版本**」 | `text/ch11_chapter_11.txt:99` `…silvery tentacles coiled around her intestines.`、`:153`（`The girl hadn’t yet finished with Alba…`）、`:156` `…the tentacles returned to their resting state…`；`text/ch12_chapter_12.txt:261` `The tentacles shot from her belly… They unfurled and stretched toward the girl’s body…` | ✅ 成立：ch11／ch12 正是 Alba 亲历的版本，与本章母亲的"口述版"成对照 |
| V5 | `md:109`「作者把一家人搂在一起的手臂，和那个**缠住女孩的触手**放在同一段里」 | `text/ch12_chapter_12.txt:261` `They unfurled and stretched toward the girl’s body… They embraced her, stroked her hair, petted her, and then dragged her back over to Alba, who unknowingly devoured the girl as she slept.` | ✅ 成立：触手确实缠住（embraced/stroked）那个女孩 |
| V6 | `md:87`「两个女儿同一分钟流鼻血」中的**事件本身** | `text/ch02_chapter_2.txt:462` `Alba and Diana often got nosebleeds, and that was just one of the alerts their bodies would send them.`、`:468` `About a month ago, the girls’ noses had both bled dramatically, in different places and situations but at the same time.` | ✅ 事件有据（措辞问题另计 A3） |
| V7 | `md:45` 原句3 的施事：Juan 捧脸细看、Alba 抓手腕拦下 | `text/ch17_chapter_17.txt:39` `Juan held his wife’s face in his hands and very carefully examined her flayed ears. … When he started to feel her head for cuts or swelling, Alba stopped him, gently grabbing his wrist.` | ✅ 主语/受事/归属方向均正确 |
| V8 | `md:69` 原句5 的施事：Carlos 察觉到 → 是 Alba 散开头发 | `text/ch17_chapter_17.txt:96` `…he realized she’d undone her ponytail… Tonight, Alba had left her hair loose so the kids wouldn’t see her ears.` | ✅ 方向正确（"她"＝Alba，不是 Diana） |
| V9 | `md:81` 原句6 的施事：Alba 提问 → Diana 领悟自己也身在事中 | `text/ch17_chapter_17.txt:201` `Then Alba asked: “Mom, how did you keep the octopus from getting out?” … She knew she was a part of it, part of the mystery, because she had the same scar on her belly…` | ✅ 方向正确（"She"＝Diana） |
| V10 | `md:93` 原句7 的口述者＝母亲 Carmen（"me""my belly button"） | `text/ch17_chapter_17.txt:279` `“All that summer, something strange was happening with my stomach… There was a tail coming out from inside me…”` | ✅ 口述人正确，未把母亲的经历安到 Diana 身上 |
| V11 | `md:21`「深夜再折回商场接那三个女人」 | `text/ch17_chapter_17.txt:6` `Then, sometime after midnight, Juan went back to Splau for the women, who were still lying down, chatting away. Alba and Diana got up easily enough, and the three of them helped Carmen stand.` | ✅ "深夜"＝sometime after midnight、"三个女人"＝Alba＋Diana＋Carmen 全对 |
| V12 | `md:33`「三个女人都得换，因为孩子们不能看见她们这副样子」 | `text/ch17_chapter_17.txt:33` `“All three of you should. The kids can’t see you like this. You can put all your clothes in the washer. …”` | ✅ 人数与动机均对 |
| V13 | `md:15`「耳朵上贴纱布」 | `text/ch17_chapter_17.txt:96` `…she had done her best to treat them by patching them up with gauze and tape…` | ✅ 成立 |
| V14 | 词汇表 21 条例句逐字 | 脚本核 `text/ch17_chapter_17.txt`：`vocab rows checked=21 verbatim_ok=21 miss=0` | ✅ 21/21 全部逐字成立 |
