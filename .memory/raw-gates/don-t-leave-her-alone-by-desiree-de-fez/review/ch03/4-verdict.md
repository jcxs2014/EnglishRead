# 第 3 章 R5 判定（人工审查）

**覆盖声明**：本次人工审查覆盖**第 3 章**（R1–R5 全流程：`1-suread.json` → `2-machine.json` → `3-diff.md` → 本文件）。**其余 17 章只有机器层或预筛，本轮不能称「已审查」**（`docs/rules/审查表.md:31`）。机器层唯一真值＝`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch03_chapter_3.txt`（原文，246 行，4,249 字符，全章 82 段皆为电话对白、无叙述者转述段）；成品＝`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch03 chapter 3.md`（131 行，6 个引语块）。审查人：DSH-Mac。

---

## 一、四组数（只报这四组）

| 组 | 数 | 依据 |
|---|---|---|
| 逐字 | **6 / 6 块** | 6 个引语块逐字命中原文（`2-machine.json`：`segments 6`、`segment_miss 0`、`quote_long 0`、`empty_quote 0`）。另：`本章词汇` 22 条例句全部是原文子串（自写脚本 `rows checked=22 not_verbatim=0`）。 |
| 对应 | **6 / 6 块（18 问）** | R4 逐块对应走完 6 个块；每块固定三问（①每个动词的主语是谁 ②受事／宾语是谁 ③归属方向回原文看 by/to/from/of）＝18 问，全部有原文出处。导航 5 条、词汇 22 条、一句话总结 1 条另行逐句对账。 |
| 形态 | **0 偏离** | `2-machine.json` `counts`：`struct_bad 0`、`keyword_bad 0`、`cjk_low 0`、`empty_quote 0`、`quote_long 0`、`hole 0`；`form`：`h1_shape_ok true`、`nav_count 5 ok`、`blocks 6`（本书中位 7、范围 5–8）、`subitems_modal`＝中文理解／关键词／为什么这样写／读者视角提示（与 `profile: novels` 一致）、`baseline: book`、`issues` 四组全空。 |
| 断言 | **20** | 判定表 20 行：通过 14 ／ **阻断 1**（已修） ／ 提示 5（已修 4） ／ 跳过 1。 |

---

## 二、判定表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 6 个引语块与原文逐字一致 | `2-machine.json` `segments 6 / segment_miss 0 / empty_quote 0` | 通过 | — |
| 2 | `本章词汇` 22 条例句均为原文子串 | 自写脚本 `rows checked=22 not_verbatim=0` | 通过 | — |
| 3 | 块 1（`md:19-27`）对应「先报地名→被追问→再解释」 | `text/ch03:9`「Oh, I’m just at Finestrelles.」→ `:12`「Again? Didn’t you guys go earlier?…」→ `:15`「Yeah, but there were so many people I couldn’t exchange the controllers.」 | 通过 | — |
| 4 | 块 1 关键词三段均落在本块引语内 | `text/ch03:9`、`:12`、`:15` | 通过 | — |
| 5 | 块 2（`md:31-39`）Alba 反问「真的在平安夜？你真是没救了」 | `text/ch03:51`「On actual Christmas Eve? You’re hopeless.」（Alba 方＝奇数段） | 通过 | — |
| 6 | 块 3（`md:43-51`）「演出很糟」出自 **Diana** | `text/ch03:57`「How was Brisa’s play?」（Alba 问）→ `:60`「It was bad.」（Diana 答） | 通过 | — |
| 7 | 块 3（`md:43-51`）「她没去」出自 **Alba**、「怎么会…」出自 **Diana** | `text/ch03:69`「She didn’t go.」（Alba）→ `:72`「How come? She wouldn’t shut up about it all week.」（Diana） | 通过 | — |
| 8 | 块 4（`md:55-63`）「你母亲昨天才刚做了美甲」 | `text/ch03:153`（Alba 转述母亲「她说不介意、说自己累了」）→ `:156`（Diana）「You know she cares! She got her nails done yesterday!」 | 通过 | — |
| 9 | 块 5（`md:67-75`）「给块饼干不就完了」出自 Diana | `text/ch03:174`（Diana「practically a teenager」）→ `:177`（Alba「he throws a fit」）→ `:180`（Diana「you give him a cookie and that’s that.」） | 通过 | — |
| 10 | 块 6（`md:79-87`）迷信三句的说话人＝Alba→Diana→Alba | `text/ch03:237`（Alba「I already told the kids you were coming for lunch.」）→ `:240`（Diana「But we’re coming on Christmas Eve…」）→ `:243`（Alba「You can’t celebrate two things at once.」） | 通过 | — |
| 11 | 导航「全章没有叙述者插手，只靠引号区分两个女人」 | 原文 82 段全为对白，无转述段（`text:6` 之后直到 `:246`） | 通过 | — |
| 12 | 导航「Alba 看得见人流、婴儿和店门」 | `text:15`（人流）、`:171`「In case he got hungry.」、`:39`（店门与营业时间）、`:213`「We just got to MediaMarkt.」 | 通过 | — |
| 13 | 导航「全章最松弛的一章」 | 全章无危机事件，结尾停在「I’ve got to go. We’ll talk later.」(`text:246`) | 通过（章内可数） |
| 14 | 块 5 读者视角提示「阿尔巴说自己带宝宝坐不了公交」 | `text:159`「Yeah, but I can’t take the bus by myself.」（Alba）→ `:162`「Why not?」（Diana） | 通过 | — |
| 15 | 块 3 三句的说话人整组对调 | `text:66`「I’ll tell you later… let me call you back…」＝**Diana**；`text:69`「She didn’t go.」＝**Alba**；`text:72`「How come?…」＝**Diana**；md 原写 Alba／Diana／Alba | 与原文不符 | **阻断（已修）** |
| 16 | 块 4「她昨天才刚做了美甲」主语歧义 | `text:156` 中「she」＝母亲（Alba 转述对象）；md 原写「她」，紧跟 Diana 的句子易读成 Diana 自己 | 歧义 | 提示（已修） |
| 17 | 块 5「她连怎么哄孩子都不知道」引了不存在的台词 | 原文只有 `:180`「you give him a cookie and that’s that.」；md 原写「你连一个人坐公交都不行」（原文是 Diana 的「Why not?」） | 措辞过头 | 提示（已修） |
| 18 | 块 2 读者视角提示「往后你会看到」跨章预言 | 属可接受的前向提示，但「所有人」范围过大 | 提示 | 提示（已修） |
| 19 | 导航「读者却只听见她说自己被吵到听不清电话」 | `text:225`「I have to go, I can barely hear you.」＝Alba 说「我快听不清**你**」 | 措辞不准 | 提示（已修） |
| 20 | 「母亲留下来照看的是 Alba 的孩子」未进 md | `text:75`「She stayed with the kids.」→ `:78`「With what kids?」→ `:81`「Well, with mine.」（Alba 自己的三个孩子；Juan 陪着 Alba，最小的宝宝在 Alba 手里，`:135`「No, the baby’s with me.」） | 漏（覆盖缺口） | 提示 |

---

## 三、收口复核（三疑点独立结论）

1. **说话人交替链（本章唯一的硬骨头）——md 原稿整组对调，已修。**
   - 交替链铁证：`text:6`「"What are you doing?" **Diana asked**.」明示 Diana 是发问方；其后奇数段＝Alba、偶数段＝Diana，**41／40 句无一破例**。
   - 语义交叉验证：`text:81`「Well, with mine.」（Alba 自己的孩子）紧跟 `text:83`「You're kidding.」（Diana 的反应），两句自洽；`text:174`「he's practically a teenager! He's almost a year old, **Alba**!」为 Diana 直呼其名。
   - 结论：块 3 的「I'll tell you later…」「She didn't go.」「How come?…」三句归属必须为 Diana／Alba／Diana，md 原稿为 Alba／Diana／Alba ⇒ **阻断**，已逐处改回（`md:45`、`:49`、`:51`）。
2. **块 5 读者视角提示所引台词不存在**——「你连一个人坐公交都不行」在原文里没有对应句；原文是 Alba 说「我一个人坐不了公交」（`:159`），Diana 回「为什么」（`:162`）。已改写为「给块饼干不就完了」＋「为什么」，逐字可核。
3. **导航层的「听不清」方向**——`text:225`「I can barely hear you.」是 Alba 说自己快听不清对方，md 原写「被吵到听不清电话」（方向相反、原因错误），已改。

---

## 四、已核实为正确（防误修清单）

以下写法在审查中看似可疑，回原文逐字核对后**成立**，任何后续改稿都不得改动（`docs/rules/审查表.md` R5.5）：

1. **块 1「先报地名、再被追问、最后解释」的分析成立**（`text:9`/`:12`/`:15`）。
2. **块 6 迷信句「你不能一件事同时庆祝两件，不吉利」逐字对应原文**（`text:243`）。
3. **块 6 三句的说话人顺序 Alba→Diana→Alba 成立**（`text:237`/`:240`/`:243`）。
4. **块 2「Alba 反问『真的在平安夜？你真是没救了』」归属成立**（`text:51`，Alba 方）。
5. **块 5「他几乎是个青少年」出自 Diana、「他一饿就大发作」出自 Alba**（`text:174`/`:177`），三句顺序成立。
6. **导航「两个女人一边嫌弃一边互相兜底」成立**：`text:120`（Diana 主动提出替 Alba 换货）、`text:198`（Diana 建议改坐有轨电车）两处兜底均在原文。
7. **导航「Alba 拿『他一饿就大发作』当挡箭牌」成立**（`text:177`；另 `text:183` 补了母亲照看时孩子哭到吐的旧事）。
8. **块 4「美甲这个细节当场推翻『她说不介意』」成立**（`text:153` vs `:156`）。
9. **导航「商场的人潮、电话里的杂音和一个不肯撒手的孩子」三项均在本章有据**（`text:15`/`:213` 人潮；`:225` 杂音；`:171`/`:177` 孩子）。
10. **块 8／本章末「两场血发生在完全同一时刻」成立**（`text/ch02_chapter_2.txt` 末段「at the exact same time」，本章末块承接该线）。
11. **`本章词汇` 22 条例句全部逐字命中原文**（自写脚本 `rows checked=22 not_verbatim=0`）。
12. **各块引语均为单一自然段内的连续子串**，无跨段缝合（`text` 中每段对白各自独立成段）。

---

## 五、本轮未做

- **五步审查未做**（待用户发起）。
- **其余 17 章未人判**（本章只覆盖第 3 章）。
- **未 push**；**协作板未发**。
