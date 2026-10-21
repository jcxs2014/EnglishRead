# 第 5 章 R5 判定（人工审查）

**覆盖声明**：本次人工审查只抽样了**第 5 章**（外层预审指定的三处疑点全部落在本章），R0–R5 全流程已跑完（`1-suread.json` → `2-machine.json` → `3-diff.md` → 本文件）。**第 1–4、6–17 章只有机器层，没有人工层，不写成「通过」**（`docs/rules/审查表.md:31`）。机器层唯一真值＝`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch05_chapter_5.txt`（729 行，48,238 字符）；成品＝`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch05 chapter 5.md`（156 行，8 个引语块）。审查人：DSH-Mac。

---

## 一、四组数（只报这四组）

| 组 | 数 | 依据 |
|---|---|---|
| 逐字 | **8 / 8** | 8 个引语块逐字命中原文（`2-machine.json`：`segments 8`、`segment_miss 0`、`quote_long 0`、`empty_quote 0`；引文起始字符位 2 / 1810 / 5626 / 19327 / 27748 / 30786 / 33259 / 43117）。另：`本章词汇` 24 条例句全部是原文子串（自写脚本 `rows checked=24 not_verbatim=0`）。 |
| 对应 | **8 / 8 块（24 问）** | R4 逐块对应走完 8 个块；每块固定三问（①每个动词的主语是谁 ②受事／宾语是谁 ③归属方向回原文看 by/to/from/of）＝24 问，全部有原文出处。导航 5 条、词汇 24 条、一句话总结 1 条另行逐句对账。 |
| 形态 | **0 偏离 ／ 1 假红** | `2-machine.json` `counts`：`struct_bad 0`、`keyword_bad 0`、`cjk_low 0`、`empty_quote 0`、`quote_long 0`；`form`：`h1_shape_ok true`、`nav_count 5 ok`、`blocks 8`、`subitems_modal`＝中文理解／关键词／为什么这样写／读者视角提示（与 `profile: novels` 一致）、`baseline: book`、`issues` 四组全空。唯一「异常」＝「关键词」子项 CJK=0，与兄弟章同体例（`ch03 chapter 3.md:23`、`ch04 chapter 4.md:23` 的关键词子项同样全是英文短语）⇒ **假红**，非本章偏离。 |
| 断言 | **26** | 判定表 26 行：通过 11 ／ **阻断 3** ／ 提示 10 ／ 假红 1 ／ 跳过 1。 |

---

## 二、判定表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 8 个引语块与原文逐字一致 | `2-machine.json` `quotes[].segments[].ok=true`（8/8）；字符位 2/1810/5626/19327/27748/30786/33259/43117 | 通过 | — |
| 2 | `本章词汇` 24 条例句均为原文子串 | 自写脚本 `vocab rows checked=24 not_verbatim=0`（正文 text 全文） | 通过 | — |
| 3 | 块 1（`md:19-27`）对应「门一开就是开放式公寓」 | `text/ch05:6`「…the door to the apartment led straight into the open-plan kitchen, dining, and living area.」 | 通过 | — |
| 4 | 块 2（`md:31-39`）对应「母亲赠三星＋Diana 惧新式电视」 | `text/ch05:9`「Carmen had given Diana the Samsung more than fifteen years earlier, when she moved in with her previous boyfriend. And Diana hadn't wanted to replace it because she had a phobia of modern TVs.」 | 通过 | — |
| 5 | 块 3（`md:43-51`）对应「三个人都不在场」 | `text/ch05:15`「To varying degrees, all three of them shared the tendency to not be present…」；`text/ch05:606`「something was off with all three of them」 | 通过 | — |
| 6 | 块 4（`md:55-63`）说「这是邪眼」的人是**妹妹 Alba** | `text/ch05:237`「She started crying harder. "It was the evil eye. I knew it. Those damn old women."」（上一句 :234 是 Diana 的 "But why?"） | 通过 | — |
| 7 | 块 5（`md:67-75`）对应「按眼窝→视野发花→看见怪物」 | `text/ch05:441`「Diana pressed her fingers to her eyes…Alba looked like a creature from another dimension.」 | 通过 | — |
| 8 | 块 6（`md:79-87`）"Your sister is never alone" 指 Alba＝**妹妹** | `text/ch05:513`（字符 [30786, …)）；`text/ch05:549`（[36285, 37234)）「who was six years older than Alba」 | 通过 | — |
| 9 | 块 7（`md:91-99`）autophobia＝叙述者 Diana 的内心检索、起于六年前 | `text/ch05:543`（[33581, 34700)）「Six years prior, the revelation had hit her…she scoured the internet for similar phobias. She found one: autophobia…」 | 通过 | — |
| 10 | 块 8（`md:103-111`）烟味＝**Diana 自己家**浴室、六个月前那个凌晨四点的记忆 | `text/ch05:615`（字符 43117 起）「about six months prior…The bathroom smelled strongly of cigarettes…She knew that cigarette smell was her father」；`text/ch05:618`「four in the morning on a Tuesday」「Damn it, Dad.」 | 通过 | — |
| 11 | `md:14`「你姐姐从不独处」把 Carlos 说的 "your sister" 译反了 | `text/ch05:513`（Alba）；`text/ch05:549`（Diana 大六岁）；`text/ch02:129`「Only her older sister, Diana…」；`text/ch17:96`「even with six years between them」 | 与原文不符 | **阻断** |
| 12 | `md:27`「姐姐不能一个人去」主语／称谓拧了 | `text/ch05:402`「She won't go alone.」、`:408`「How could she go by herself?」（指 Alba）、`:417`「Do you come with me when I take my kids to the doctor? Never. I go alone.」 | 与原文不符 | **阻断** |
| 13 | `md:15`、`md:156` 的「饭后」与原文冲突（全章无人吃饭） | `text/ch05:135`、`:432`、`:480`、`:567`（"we still haven't eaten lunch"） | 与原文不符 | **阻断** |
| 14 | `md:15` 把三件回忆材料压进同一张沙发 | `text/ch05:477`、`:489`（孩子在 Carlos 腿上＝Alba 家）、`:546`（床垫＝当场回想）、`:552`（回家）、`:606`（商场旧忆）、`:615`（烟味） | 地点／时序错位 | 提示 |
| 15 | `md:13`「全家的迷信行动」「唯一能解释这团混乱的力量」过头 | `text/ch05:387`（Diana 否定邪眼）、`:528`（Carlos「It must be a coincidence.」）、`:237`（只有 Alba 认） | 措辞过头 | 提示 |
| 16 | `md:63`「这一整天里没有一个人去核对它」过头 | `text/ch05:333`（Diana 问过）、`:336`（Carmen 答了） | 措辞过头 | 提示 |
| 17 | `md:85`「一个整天埋在手机里的丈夫」无出处 | `text/ch05:78`（Carlos 只有一处「took refuge in his phone」）、`:18`（「埋进手机」的是 Carmen） | 措辞过头 | 提示 |
| 18 | `md:12`「病症第一次被说出口」易读成「对家人说破」 | `text/ch05:540`「she had never talked about this feature of Alba's life with anyone, neither with Carlos nor Carmen, nor with Alba herself.」 | 措辞过头 | 提示 |
| 19 | `md:25`「根子其实就种在这种没有角落的布局里」属作者意图推断 | `text/ch05:540-549`（原文把 Alba 的状况归因于恐惧／执念，不提户型） | 解读非事实 | 提示 |
| 20 | `md:11`「平安夜前两天」比原文日期早一天 | `text/ch05:315`「two days before Christmas」＝12/23；`text/ch05:567`（明晚还有一场）＝12/24 平安夜；`text/ch04:54`「Because tomorrow is Christmas Eve」 | 日期偏移一天 | 提示 |
| 21 | 父亲已故（两年前的 3 月）未进 md | `text/ch05:636`「If my dad hadn't died…」、`:642`「in March it'll be two years since he died」 | 漏（覆盖缺口） | 提示 |
| 22 | 硬币来源（祖父给每个孩子两欧元）与 Juan 生日当天缺席未进 md | `text/ch05:159`、`:183`、`:285` | 漏（覆盖缺口） | 提示 |
| 23 | 母亲是当年陪 Alba 睡客厅地板的人未进 md | `text/ch05:546`「Carmen…flopped down on the couch right next to her, holding her hand…went to the living room to sleep next to her daughter.」 | 漏（覆盖缺口） | 提示 |
| 24 | 「关键词」子项 CJK=0 是否形态偏离 | `ch03 chapter 3.md:23`、`ch04 chapter 4.md:23` 同体例；`2-machine.json` `blocks[].cjk.关键词 = 0` | 与兄弟章同体例，非偏离 | 假红 |
| 25 | md 是否存在「原文无」的杜撰事实（编单） | 逐条核对 `md:11-15`、`md:19-111`、`md:113-152`、`md:156` 的事实性断言 | 无编造 | — |
| 26 | 其余 16 章（ch01–04、ch06–17）的人工层结论 | 抽样只跑第 5 章（`docs/rules/审查表.md:31` 要求写明） | 只有机器层，未核 | 跳过 |

---

## 三、收口复核（外层预审三处疑点的独立结论）

1. **人物关系方向（疑点 1）——确认 md 内部方向反了，且反在两处**
   - 原文铁证：`text/ch05:549`「She, on the other hand—who was six years older than Alba—…」（Diana 大六岁＝长姐）；`text/ch02:129`「Only her older sister, Diana…」；`text/ch17:96`「even with six years between them」。
   - Carlos 的 "Your sister is never alone."（`text/ch05:513`）＝**Alba**，即**妹妹**。md 写对了的是 `md:11` 与 `md:81`（「你妹妹从不独处」）；写反的是 `md:14`（「你姐姐从不独处」）与 `md:27`（「姐姐不能一个人去」）。
   - 读者视角提示里「不能一个人去」的是 **Alba**：Carmen「She won't go alone.」（:402）「How could she go by herself?」（:408）；Diana 当面说「I go alone.」（:417）。⇒ 两条**阻断**。
   - 附带发现：同源错误在 `00_金句精选.md:114`「第五章，丈夫试图解释姐姐为什么永远有人陪」；全书 md 体例是「姐姐＝Diana、妹妹＝Alba」（`ch15:63`、`ch16:51`），`00_概述.md:22` 用的是「妹妹」。改稿时建议一并扫。
2. **「六年前」（疑点 2）——md 写对了**
   - `text/ch05:543`「Six years prior, the revelation had hit her, right around the time of her own personal downturn, when Tomás was born…she scoured the internet for similar phobias. She found one: autophobia…」——「六年前察觉＋上网查病名」在同一段，`md:12` 的「叙述者交代自己六年前就察觉了（她当年上网查过一种怕独处的病症）」与 `md:97` 的「宁可花六年收集证据」都成立。
3. **说话人与归属（疑点 3）——三条归属 md 全对，一处措辞需收**
   - 块 4「这是邪眼」＝**Alba 本人**（`text/ch05:237`「She started crying harder. "It was the evil eye. I knew it."」，`md:57` 归属正确）。
   - 块 8 的烟味＝**Diana 自己的记忆**，发生在**她自己家**的浴室、六个月前那个凌晨四点（`text/ch05:615`、`:618`）；父亲＝Diana 与 Alba 的父亲／Carmen 的亡夫，**两年前的 3 月去世**（`text/ch05:636`、`:642`）——md 未交代死亡（漏，提示档）。
   - 「你妹妹从不独处」＝**Carlos 当面对 Diana 说的原话**，不是叙述者转述（`text/ch05:513`，`md:81` 归属正确）；叙述者只在 `:540`–`:549` 的内心独白里自己确认这件事。

---

## 已核实为正确

以下写法在审查中看似有误，回原文逐字核对后**成立**，任何后续改稿都不得改动（`docs/rules/审查表.md` R5.5）：

1. **`md:11`、`md:81` 的「你妹妹从不独处」方向正确**（不得改成「姐姐」）。依据：`text/ch05:513`「Your sister is never alone.」说的是 Alba；`text/ch05:549`「She, on the other hand—who was six years older than Alba—did sometimes express her bewilderment.」；`text/ch02:129`「Only her older sister, Diana, insisted she go to a specialist and sent her a dermatologist's number several times.」；`text/ch17:96`「even with six years between them」。
2. **`md:12` 的「六年前」有出处**。依据：`text/ch05:543`「In fact, it wasn't that long ago that Diana herself had come to realize how serious it was…Six years prior, the revelation had hit her, right around the time of her own personal downturn, when Tomás was born.」
3. **`md:97` 的「宁可花六年收集证据」成立**。依据：`text/ch05:543`「Instead, she focused on gathering enough evidence to prove that Alba had been afflicted at least since she was a teenager.」（自六年前顿悟起持续取证）。
4. **`md:57` 把「这是邪眼」归给妹妹 Alba 正确**。依据：`text/ch05:237`「"In case he did swallow it. It's too dangerous. They're full of germs, they're toxic." She started crying harder. "It was the evil eye. I knew it. Those damn old women."」；前一句 `:234` 是 Diana 的 "But why?"。
5. **`md:93` 的「她找到一个：autophobia」＝叙述者 Diana**。依据：`text/ch05:540`「Diana knew Alba was never alone.」＋`text/ch05:543`「She thought the obsession must be related to fear, and she scoured the internet for similar phobias. She found one: autophobia, the irrational fear of being alone.」
6. **`md:105` 的烟味句译法忠实，且「父亲」＝Diana 与 Alba 的父亲**。依据：`text/ch05:615`「The bathroom smelled strongly of cigarettes. It smelled exactly the way the bathroom at her parents' house did when he was in it—the man had smoked two packs a day since she was little.」（「父母家那个浴室」＝原生家庭；「浴室里烟味很重」＝Diana 与 Carlos 自己家，`text/ch05:618`「four in the morning on a Tuesday」）。
7. **`md:69` 的「妹妹看上去像个来自另一个维度的生物」指 Alba**。依据：`text/ch05:441`「Blurry like that, with an oversized puffer coat and her children's arms and legs sticking out from behind her, Alba looked like a creature from another dimension.」
8. **`md:27` 里「孩子不肯留下」成立**（同一条理由链中的第一项没问题）。依据：`text/ch05:510`「My niece and nephew are like that, too. Since Alba's never left them alone with anyone, they don't want to stay back, not even if it's with us.」
9. **`md:14`「我带孩子看病时你一次都没陪过」成立**。依据：`text/ch05:417`「Do you come with me when I take my kids to the doctor? Never. I go alone. Or Carlos goes. The few times I asked, when they were tiny and I couldn't handle it, you couldn't come because you were with Alba.」
10. **`md:33`「十五年前、母亲在她跟前男友同住时送的」成立**。依据：`text/ch05:9`「Carmen had given Diana the Samsung more than fifteen years earlier, when she moved in with her previous boyfriend.」
11. **`md:13`「三枚硬币在矮柜上、那枚硬币在换尿布台底下」成立**。依据：`text/ch05:183`「Brisa pointed to a low dresser, on top of which three euros lay in a corner.」；`text/ch05:216`「Brigitte lay flat on the floor, reached under the baby's changing table, and pulled out a toy car and a one euro coin wrapped in a gray ball of lint.」
12. **`md:156`「硬币被找到了」成立**。依据：`text/ch05:216`（硬币在换尿布台底下被找到）＋`text/ch05:222`「"We found it. He didn't swallow anything," Diana said.」
13. **`md:99`「童年那张床垫」成立**。依据：`text/ch05:546`「Alba had been thirteen then…Alba dragged her mattress into the living room, and she announced she was going to sleep there, on the floor.」
14. **`本章词汇` 24 条例句全部逐字命中原文**（自写脚本 `rows checked=24 not_verbatim=0`），无需改动。
15. **机器层「关键词」子项 CJK=0 不是本章缺陷**。依据：`ch03 chapter 3.md:23`、`ch04 chapter 4.md:23` 的「关键词」子项同样全为英文短语 ⇒ 全书体例，非形态偏离。
