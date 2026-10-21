# 第 15 章 R5 判定（人工审查）

## §0 覆盖声明

- **本轮人工审查只覆盖第 15 章**（`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch15 chapter 15.md`）。
- 抽样理由：本章是全书「三人关系重排」的枢纽章（Alba / Diana / Carmen 三个女人第一次把伤口摆上桌），也是 ch16 商场终局与 ch17 收束的直接前置章，且本章两次出现**说话人易错**的对话（`text/ch15:15`、`:30`），适合做人工逐字与归属抽验。
- **其余各章（ch00–ch14、ch16、ch17）本轮只有机器层，没有人工层，不写成「通过」**（依据 `docs/rules/审查表.md:31`：「抽样章号与理由写进 `4-verdict.md` 的覆盖声明；没跑的章要写「只有机器层」，不许写成「通过」」）。第 16 章的人工层由同一子代理另出 `review/ch16/4-verdict.md`，本章结论不外推到第 16 章。
- 唯一真值：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch15_chapter_15.txt`（141 行 / 8270 字符）。
- 成品 md：`ch15 chapter 15.md`（111 行；引语块 7 个；`## 本章词汇` 24 条；`## 一句话总结` 1 条）。
- 流程合规：先整章素读原文并落 `review/ch15/1-suread.json`（R1），再打开成品 md 对照（R3–R4），最后出本判定（R5）；顺序符合 `docs/rules/审查表.md:37`。
- 机器层：`review/ch15/2-machine.json`（已存在、未改动）——`verdict: ok`，7 块全 `ok=true`，`issues` 仅 `keyword_long` 7 条（非阻断）。
- 签名：DSH-Mac

---

## §1 四组数（只报这四组）

| 组 | 数 | 依据 |
|---|---|---|
| **逐字** | 7/7 引语块逐字一致（100%）；`## 本章词汇` 24 条例句逐字一致（24/24，`not_verbatim=0`） | `bash scripts/chapter.sh "…/ch15 chapter 15.md" --json` → 退出码 0、`verdict: ok`、7 块 `ok=true`、`empty_quote=0`、`segment_miss=0`；块 1/2 在 `text/ch15:6`、块 3 在 `:15`、块 4 在 `:30`、块 5 在 `:36`、块 6 在 `:117`、块 7 在 `:141`，逐句比对首尾词一致。词表逐字用 `/tmp/check_vocab_ch1516.py` 核过（跳过表格分隔行）。 |
| **对应** | 7 块 × 固定三问，全部能在原文指出出处（7/7 通过） | ①动词主语：块 1/2「拼图/画面」＝Diana 的拼图（`:6`）；块 3「说/看/撕」＝Alba（`:15`）；块 4「started bleeding / It was telepathic」＝Diana（`:30`）；块 5「embraced / there had been a radical shift」＝Carmen（`:36`）；块 6「I had it in my stomach」＝Carmen（`:117`）；块 7「looked at her sister / didn't say」＝Alba（`:141`）。②受事/宾语：块 3「two slices」（`:15`）；块 4「the taxi to your house」（`:30`）；块 6「my stomach / that summer」（`:117`）；块 7「her sister」（`:141`）。③归属方向：块 3「looked at her mom's and sister's」＝向外→母亲与姐姐（`:15`）；块 4「like the day Brisa and Brigitte got bloody noses」＝回指旧例（`:30`）；块 6「our first summer at the campsite」＝自述（`:117`）；块 7「that Diana, without knowing it, had been with her in Splau」＝向内（`:141`）。 |
| **形态** | 4 项子项（中文理解 / 关键词 / 为什么这样写 / 读者视角提示）× 7 块 = 28 个子项行，**缺 0**；引语行形态 `> **原句 N:** "…"` 7/7 合规；块数 7 ∈ [3,10]（profile novels）；导航 5 项齐全（md:11–15）；`## 本章词汇` 三档齐全（⭐⭐⭐ 8 / ⭐⭐ 8 / ⭐ 基础 8）；`## 一句话总结` 有正文（md:111）；H1 `# 15. Chapter 15` 符合本书 `N.` 形态 | `2-machine.json`：`h1_shape_ok=true`、`nav_count=5`、`subitems_modal`＝4 项、`blocks=7`、`block_median=7.5`、`range=[5,8]`、`profile=novels`；`struct_bad=0`、`hole=0`、`block_count` 空。**形态偏离说明**：本章块间**没有** `---` 分隔行（全书只有 ch12/ch13/ch14/ch15 四章没有，与 ch12–14 同体例），不计入缺陷，仅记此行理由。 |
| **断言** | 15 条关键断言逐条回原文取证（15/15 有据，0 条编造，2 条措辞偏移＝提示档） | 见 §2 判定表 A1–A15；其中 A13、A14 判「提示」，其余通过。 |

---

## §2 判定表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | md:11「母亲的腹部伤口和戴安娜的伤口在同一刻出现」 | ch15:`text:42`（`[3621,3756)`）「The wound showed up on both of us at the same time.」——`both of us`＝Carmen+Diana | 成立 | 通过 |
| A2 | md:11「卡门最后承认自己当年肚子里也曾有过一只章鱼」 | ch15:`text:111`（`[6032,6150)`）「I had an octopus in my stomach, too.」「It was years ago.」＋`text:117` | 成立 | 通过 |
| A3 | md:13「戴安娜刚说『你不是不信这种事吗』，卡门反问『哪一种？』」 | ch15:`text:51`「But, Mom, you don't believe in that kind of thing.」→ `text:54`「What kind of thing?」（说话人＝Carmen） | 成立（顺序与问句内容均对） | 通过 |
| A4 | md:13「阿尔巴接着说『你刚才还在讲心灵感应』」 | ch15:`text:60`「Wait a second, Diana. You're the one who was just talking about telepathy," Alba said」——**说话人是 Alba，不是卡门** | 说话人写对了，但「拆掉超自然」的功劳被记到卡门头上（见 `3-diff.md` W1） | 提示 |
| A5 | md:13「卡门抱了小女儿，却几乎立刻退开」 | ch15:`text:36`「her youngest daughter」＝Alba（`[2914,3578)`）＋`text:39`「So the hug lasted only a few seconds.」（`[3581,3618)`） | 成立 | 通过 |
| A6 | md:15「一角是亮灯的厢式车，另一角是三个女人和写着 Splau 的红色招牌」 | ch15:`text:6`（`[7,1460)`）「three women sitting on the ground outside what looked like a mall, with a red sign out front that read Splau」 | 成立 | 通过 |
| A7 | md:21「十一月廿八日……都到寒假最后一天为止」 | ch15:`text:6`「November 28」[199,210)、「before Epiphany」[397,412) | 成立 | 通过 |
| A8 | md:24「多年赶不上主显节前的最后一块」 | ch15:`text:6`「Not once had she managed to set down the last piece before Epiphany, and it depressed her.」 | 成立 | 通过 |
| A9 | md:35「阿尔巴说着，看了看母亲和姐姐的手——一样脏」 | ch15:`text:15`（`[1657,1908)`）「"My hands are disgusting," she said, and she looked at her mom's and sister's, which were just as dirty」——**说话人＝Alba**，受事＝母亲与姐姐的手 | **归属正确**（本轮指定陷阱①） | 通过 |
| A10 | md:42「『妈妈也是。』戴安娜说」 | ch15:`text:30`（`[2585,2873)`）「What octopus? I started bleeding in the taxi to your house… And Mom, too. I think it happened about the same time…」——**说话人＝Diana**（承 `:27` Alba 的问句） | **归属正确**（本轮指定陷阱②） | 通过 |
| A11 | md:51「上一代的人感受得到爱，却既不习惯用身体表达，也不习惯用语言表达」 | ch15:`text:36`「they had always felt loved by Carmen, but it hadn't been easy for her to express it physically or verbally」 | 成立 | 通过 |
| A12 | md:59「两个女儿都明白：即使那只是妄想，对母亲来说也真的发生过」 | ch15:`text:120`（`[6520,6857)`）「even if it had been just a delusion, for her, it had really happened.」 | 成立 | 通过 |
| A13 | md:44「也正是后面母亲一句反问就能掀翻的东西」 | ch15:`text:72`（Carmen 转向 Diana 的追问）→`text:75` Diana「Very funny.」（**没被说服**）→`text:81` Diana「No, I agree…」（反而顺着母亲走）；真正掀翻「心灵感应」的是 `text:60` Alba 的反问 | 掀翻者被记成母亲；原文里母亲的两次质疑（`:54`、`:72`）都没能动摇 Diana | 提示 |
| A14 | md:44「戴安娜口中的『相信』其实是在没有更好说法时的应急」 | ch15:`text:63`「Yeah, but I believe. I've experienced things.」＋`text:69`「Just things.」——她是先斩后奏地宣称相信，只是对「经历过什么」含糊 | 降格为「应急」，与原文的自我确信不符 | 提示 |
| A15 | md:65 / md:111「真正握着答案的人一句话都没说」「妹妹只是温柔地看着姐姐，什么也没有说」 | ch15:`text:141`（`[8065,8269)`）「Alba looked at her sister tenderly… Nor did she say that Diana, without knowing it, had been with her in Splau that night.」 | 成立 | 通过 |

---

## §3 收口复核（外层预审疑点的独立结论）

| 疑点 | 独立结论 | 依据 |
|---|---|---|
| ① 「My hands are disgusting」是谁说的？ | **Alba**。成品 md 归属正确，无需改动。 | `text/ch15:15`（`[1657,1908)`）：说话人 Alba；她看的是 `her mom's and sister's`；md:35 写对了。 |
| ② 「And Mom, too…It was telepathic」是谁说的？ | **Diana**。成品 md 归属正确，无需改动。 | `text/ch15:30`（`[2585,2873)`）：承 `:27` Alba 的「The octopus? You guys had the same thing?」，同一行内说话人是 Diana；md:42 写对了。 |
| ③ 「Wait a second, Diana…」是谁说的？ | **Alba**（原文行内自带 `Alba said` 标签）。这是本章唯一能推翻 Diana「心灵感应」说法的反问，md 把它写成卡门的反问在前面拆、阿尔巴在后面附和 ⇒ 逻辑归属偏移（提示）。 | `text/ch15:60`（`[3939,4026)`）原文即含 `"Wait a second, Diana. You're the one who was just talking about telepathy," Alba said`。 |
| ④ 本章有没有「用身体表达爱」的代际对照？ | 有，且 md 写对了。 | `text/ch15:36`「Between one generation and the next, there had been a radical shift. Diana and Alba hugged and kissed their kids… But that's not what they had experienced growing up…」；md:51 成立。 |
| ⑤ 「Alba 被抱住」抱她的是谁？ | **Carmen**（Alba 是 Carmen 的 youngest daughter），md:13「卡门抱了小女儿」成立。 | `text/ch15:36`＋`text/ch15:39`。 |
| ⑥ 卡门「当年营地的夏天」里到底发生了什么？ | 原文只给「那年她在沙滩上晕倒」「整只章鱼在胃里待了一整个夏天」「两个女儿吓得差点死」，**没有**给更细的机制。md 未越界发挥，成立。 | `text/ch15:117`（`[6265,6517)`）。 |
| ⑦ 本章是否交代了 Alba 今晚在商场经历了什么？ | **没有**。原文只给旁证（耳朵被撕裂、与店员起过冲突、被困洗手间），md 未编造具体经过，成立。 | `text/ch15:84`、`:87`、`:78`、`:9`、`:90`。 |
| ⑧ 「同刻出血」是否发生在三个人身上？ | **只发生在 Carmen 与 Diana 两人**（`both of us`），**不含 Alba**。md:11 写「母亲的腹部伤口和戴安娜的伤口在同一刻出现」正确。 | `text/ch15:42`。 |
| ⑨ 本章有没有「卡门说服了 Diana」？ | 没有。Diana 末尾仍在自陈「Both of you are so brave」并保留「I've experienced things」。md 未写成「被说服」，成立；md:44 把它写成可被一句反问掀翻，是 md 侧的推断（见 A13/A14）。 | `text/ch15:63`、`:132`。 |
| ⑩ 本章是否给出「为什么 Alba 不说」的由头？ | 给了：`she didn't have the energy or confidence to explain what she had gone through`。md 只写结果未写由头 ⇒ 记漏（`3-diff.md` L8，提示档）。 | `text/ch15:90`（`[5055,5422)`）。 |
| ⑪ 本章是不是「圣诞夜／平安夜」？ | 是，三处互证（`text:18`「What a Christmas Eve dinner」、`:93`「It's Christmas Eve」、`:96`「There are people who work on Christmas Eve」）。md 写「圣诞夜」正确。 | 原文行 18/93/96。 |
| ⑫ 本章的地名与年龄锚点是否在 md 里？ | 不在：md 全文无 `Cornellà`（`text:102`），无「二十七岁」（全书唯一，`text:102`），无 `campsite` 专名以外的扩展。md 未编造地名 ⇒ 成立，但缺失（`3-diff.md` L4，提示档）。 | `text/ch15:102`（`[5696,5805)`）。 |
| ⑬ 词表 24 条例句是否逐字取自本章？ | 是，`not_verbatim=0`（`/tmp/check_vocab_ch1516.py`，不入库）。 | 校验脚本输出。 |
| ⑭ 子项形态是否与全书一致？ | 已一致：父代理把本章子项统一为 `**中文理解**：` 形式，全书 18 章子项前缀统计一致（每章短横形式仅导航 5 项）。**记此行理由：形态偏离在父代理修复前存在，现已消除。** | `2-machine.json` 的 `subitems_modal`；全书 md 前缀统计。 |

---

## §4 已核实为正确（防误修清单）

以下条目**看似有误但回原文核对后成立**，后续修复时**不得改动**：

1. **md:35「阿尔巴说着，看了看母亲和姐姐的手——一样脏」——归属成立。** `text/ch15:15`（`[1657,1908)`）：`"My hands are disgusting," she said, and she looked at her mom's and sister's, which were just as dirty`。说话人＝Alba，被看的人＝母亲与姐姐，md 三要素全对。
2. **md:42「『妈妈也是。』戴安娜说」——归属成立。** `text/ch15:30`（`[2585,2873)`）：这一行是 Diana 连续说话（承 `:27` Alba 的问句），「And Mom, too」与「It was telepathic」同属 Diana，md 写对了。
3. **md:11「母亲的腹部伤口和戴安娜的伤口在同一刻出现」——成立，且不要改成「三个人」。** `text/ch15:42`「The wound showed up on both of us at the same time.」说话人是 Carmen，`both of us`＝Carmen 与 Diana，**Alba 不在其列**。
4. **md:13「卡门抱了小女儿，却几乎立刻退开」——成立。** `text/ch15:36`「her youngest daughter」＝Alba（不是 Diana）；`text/ch15:39`「So the hug lasted only a few seconds.」支持「几乎立刻退开」。
5. **md:13「卡门反问『哪一种？』」——问句内容与顺序成立。** `text/ch15:51`（Diana 说「You don't believe in that kind of thing」）→ `:54`（Carmen「What kind of thing?」）顺序正确；本条**只**错在「拆掉超自然」的归属，不在问句本身。
6. **md:21「十一月廿八日……到寒假最后一天为止」——成立。** `text/ch15:6`「November 28」[199,210) 与寒假收工的描述同在一段。
7. **md:24「多年赶不上主显节前的最后一块」——成立。** `text/ch15:6`「Not once had she managed to set down the last piece before Epiphany, and it depressed her.」
8. **md:15「三个女人与写着 Splau 的红色招牌」「亮灯的厢式车」——成立。** `text/ch15:6` 同段：`three women sitting on the ground outside what looked like a mall, with a red sign out front that read Splau`；厢式车一角在同段。
9. **md:51「上一代的人感受得到爱，却不习惯用身体或语言表达」——成立。** `text/ch15:36`「they had always felt loved by Carmen, but it hadn't been easy for her to express it physically or verbally」。
10. **md:59「即使那只是妄想，对母亲来说也真的发生过」——成立。** `text/ch15:120`「even if it had been just a delusion, for her, it had really happened.」
11. **md:65 / md:111「Alba 什么也没说」——成立。** `text/ch15:141`「Nor did she say that Diana, without knowing it, had been with her in Splau that night.」——md 的「两个『没有说』」正对应原文这一句的两个否定式。
12. **md:111「卡门说出当年营地的那个夏天」「女儿笨拙地说你们真勇敢」——成立。** `text/ch15:117`（营地夏天）＋`text/ch15:132`「Both of you are so brave.」（说话人＝Diana，对象＝母亲与 Alba）。
13. **md 用「圣诞夜」而非「平安夜」——原文无冲突。** `text/ch15:18`「What a Christmas Eve dinner」、`:93`「It's Christmas Eve」；「平安夜」是同一夜的中文说法，不构成事实冲突。
14. **md 不写营地专名——成立，不要补。** `text/ch15:117` 只写 `the campsite`，专名 `Camp La Tortuga Ligera` 出现在 **ch02:249、ch10:384/414/423/435/438**，本章没有点名，md 沿用「营地」是忠实的。
15. **md 不写 Alba 的伤是怎么来的——成立，不要补。** 原文只给旁证（`text/ch15:9` 洗手间、`:78` 与店员起过冲突、`:84`/`:87` 耳朵），没有机制描写；md 未编造机制，是对的（`3-diff.md` L1/L2/L5 只要求补旁证，不是补机制）。
16. **md 七个引语块的选段长度偏长——不是缺陷。** 块 3（`:15`）45 词、块 4（`:30`）33 词、块 7（`:141`）39 词，均在创建卡「1–3 句、30–70 词、不超 4 行」的区间内；机器层 `quote_long=0`。
17. **`## 本章词汇` 的 ⭐ 基础档（8 条）体例与全书一致。** 三档齐全、条目 24 条在 `text/ch15` 内逐字命中，机器层 `keyword_bad=0`；`keyword_long` 7 条只是「关键词字段偏长」的提示，不影响逐字性。
18. **本章块间没有 `---` 分隔行——不是缺陷。** 全书 ch12/ch13/ch14/ch15 四章均无，ch15 与 ch12–14 同体例（`3-diff.md` §1 形态偏离说明已记此行理由）。

---

本判定只覆盖第 15 章；其余各章只有机器层，不写成「通过」。本轮未改动任何 md 文件，git 未执行任何操作（未 add / 未 commit / 未 push）。
