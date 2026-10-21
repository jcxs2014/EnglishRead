# 第 7 章 R5 判定（人工审查）

**覆盖声明**：本次人工审查抽样了**第 7、8、10 章**（外层预审指定的三章），三章的 R0–R5 全流程均已跑完（`1-suread.json` → `2-machine.json` → `3-diff.md` → 本文件）。**第 1–6、9、11–17 章只有机器层，没有人工层，不写成「通过」**（`docs/rules/审查表.md:31`）。机器层唯一真值＝`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch07_chapter_7.txt`（28 行，3,300 字符，8 个正文自然段）；成品＝`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch07 chapter 7.md`（140 行，7 个引语块，20 条词汇）。审查人：DSH-Mac。

---

## 一、四组数（只报这四组）

| 组 | 数 | 依据 |
|---|---|---|
| 逐字 | **7 / 7** | 7 个引语块逐字命中原文（`2-machine.json`：`segments 7`、`segment_miss 0`、`quote_long 0`、`empty_quote 0`；引文起始字符位 139 / 418 / 742 / 1367 / 2466 / 2705 / 2999，逐块 `ok: true`）。另：`本章词汇` 20 条例句全部是原文子串（自写脚本 `check_md_quotes.py`：词汇例句 MISS 数 = 0）。 |
| 对应 | **7 / 7 块（21 问）** | R4 逐块对应走完 7 个块；每块固定三问（①每个动词的主语是谁 ②受事／宾语是谁 ③归属方向回原文看 by/to/from/of）＝21 问，全部有原文出处。导航 5 条、词汇 20 条、一句话总结 1 条另行逐句对账。 |
| 形态 | **0 偏离 ／ 1 假红** | `2-machine.json` `counts`：`struct_bad 0`、`keyword_bad 0`、`cjk_low 0`、`empty_quote 0`、`quote_long 0`；`form`：`h1_shape_ok true`、`nav_count 5`、`nav_count_ok true`、`blocks 7`、`block_range [5,8]`、`subitems_modal`＝中文理解／关键词／为什么这样写／读者视角提示（与 `profile: novels` 一致）、`baseline: book`、`issues` 四组全空。唯一「异常」＝「关键词」子项 CJK=0（机器层仅此一项非零），与兄弟章同体例（关键词本就是英文短语）⇒ **假红**，非本章偏离。 |
| 断言 | **22** | 判定表 22 行：通过 13 ／ **阻断 1** ／ 提示 7 ／ 假红 1 ／ 跳过 0。 |

---

## 二、判定表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 7 个引语块与原文逐字一致 | `2-machine.json` `quotes[].segments[].ok=true`（7/7）；字符位 139/418/742/1367/2466/2705/2999 | 通过 | — |
| 2 | `本章词汇` 20 条例句均为原文子串 | 自写脚本 `check_md_quotes.py`（ch07）：词汇例句 MISS 数 = 0；逐条行号 deactivated:12、comprehend:18、unsettled:21、flashlight:6、proceeded:27、clenched:27、trembling:27、unnatural:27、curtains:6、shoulders:12、duvet:21、rousing:27、mushroom lamp:6、window:6、ceiling:27、chest:27、nightstand:6、toes:27、mouth:27、lie back:21 | 通过 | — |
| 3 | 块 1（`md:19-27`）对应「蘑菇灯早灭＋手机手电＋女儿立于床尾面朝窗」 | `text/ch07:6`「They always left the mushroom lamp on, but she'd forgotten to charge it during the day…From the door, she could see the girl was standing at the foot of the bed, her feet on the little mat, facing the window.」 | 通过 | — |
| 4 | 块 2（`md:31-39`）对应「没装窗帘＋对面楼能看到女儿」 | `text/ch07:6`「Since they'd only moved in recently, they still hadn't put up curtains. And the mental image of her daughter from the other side of the window, seen from the apartment across the way, unsettled her as much as the sight in front of her.」 | 通过 | — |
| 5 | 块 3（`md:43-51`）说「Brisa collapsed」的是**母亲施行的动作**（把女儿转过来） | `text/ch07:12`「When she tried to turn her around by the shoulders, Brisa collapsed.」；主语＝Brisa（collapsed），动词 try 的主语＝Diana | 通过 | — |
| 6 | 块 4（`md:55-63`）对应「去厨房取水→回来看见女儿睡着→把手放在背上确认呼吸」 | `text/ch07:27`「Diana went to the kitchen for a glass of water, and when she got back, her daughter had fallen asleep. She left the glass on the dresser, sat down at the edge of the bed, and placed her hand on her daughter's back to make sure she was breathing normally.」 | 通过 | — |
| 7 | 块 5（`md:67-75`）对应「第二次触摸摸到不像背也不像胸的东西」 | `text/ch07:27`「Her stomach then clenched as soon as she realized she didn't know quite what she was touching. It had the warmth of Brisa, but it felt nothing like her back or even her chest.」 | 通过 | — |
| 8 | 块 6（`md:79-87`）对应「上半身趴着、膝盖脚尖朝天花板、跳起来开灯」 | `text/ch07:27`「Her daughter was face down from the waist up, but her knees and the tips of her toes pointed toward the ceiling. Diana jumped up and rushed to turn on the light.」 | 通过 | — |
| 9 | 块 7（`md:91-99`）对应「门口捂嘴发抖→去书房拿 AirPods 放播客→守着睡了一夜」 | `text/ch07:27`「Standing at the door to her child's bedroom, one hand covering her mouth, legs trembling, she had no idea what to do. She went to the office for her AirPods, put on a podcast, and proceeded to lie awake all night right next to Brisa, who didn't move again.」 | 通过 | — |
| 10 | `md:14`「她先是数女儿有没有呼吸」成立 | `text/ch07:27`「placed her hand on her daughter's back to make sure she was breathing normally」 | 通过 | — |
| 11 | `md:15`「先听见屋里有动静，再借手机手电看轮廓，最后靠手掌确认」成立 | `text/ch07:6`「Diana heard something in Brisa's room…phone flashlight on」；`:27` 手掌触摸 | 通过 | — |
| 12 | `md:75`「还有温度，说明还是活的」成立 | `text/ch07:27`「It had the warmth of Brisa, but it felt nothing like her back or even her chest.」 | 通过 | — |
| 13 | `md:140` 一句话总结与原文事实一致（一个夜晚／从数呼吸到摸形状／开灯说正常／戴耳机守到天亮） | `text/ch07:6`–`:27` 全段 | 通过 | — |
| 14 | `md:11`「摸到的身体既不像背也不像胸」与「一碰就软」被并成同一次触碰 | `text/ch07:12`（转身时瘫软）与 `text/ch07:27`（第二次触摸摸到形状不对）之间隔着一整段；原文两次触碰结论不同 | 与原文不符 | **阻断** |
| 15 | `md:11`、`md:87`「开灯却一切正常」压掉了原文的双重否定 | `text/ch07:27`「She was in an uncomfortable position, but not an unnatural one, **nothing like what she'd seen**.」——原文说的是「与黑暗中看到的不是同一副模样」，不是「正常」 | 措辞失真 | 提示 |
| 16 | `md:15`「全章几乎是一个长段落」与原文段落结构不符 | `text/ch07` 实测 8 个正文自然段（`:6` 655 / `:9` 95 / `:12` 218 / `:15` 65 / `:18` 105 / `:21` 227 / `:24` 14 / `:27` 1,896 字符），长的是末段 | 结构判断不符 | 提示 |
| 17 | `md:13`「梦游这一老套解释被兑现」未标明这是 Diana 的判断 | `text/ch07:27`「now she was absolutely sure Brisa had been sleepwalking」——是母亲的结论，不是叙述者事实 | 归属未标 | 提示 |
| 18 | Brisa 醒来后的「I'm thirsty.」未进 md | `text/ch07:24`「"I'm thirsty."」；`:21`「It was then that Brisa truly woke up.」 | 漏（覆盖缺口） | 提示 |
| 19 | Diana 的两句台词「Get in bed.」「Do you have to go to the bathroom?」未进 md | `text/ch07:9` | 漏（覆盖缺口） | 提示 |
| 20 | 露营睡袋与「女儿已翻身趴下」未进 md | `text/ch07:27`「She took one of the kids' camp sleeping bags from the closet…her daughter had now rolled onto her stomach.」 | 漏（覆盖缺口） | 提示 |
| 21 | 叫不醒 Carlos 与「她独自过了一夜」未进 md 正文 | `text/ch07:27`「She tried to wake Carlos up…rousing that man was basically impossible.」＋「angry, if unfairly, that Carlos was out through the whole thing」 | 漏（覆盖缺口） | 提示 |
| 22 | 「关键词」子项 CJK=0 是否形态偏离 | `2-machine.json` `blocks[].cjk.关键词 = 0`；同体例见 `ch03 chapter 3.md:23`、`ch04 chapter 4.md:23` | 与兄弟章同体例，非偏离 | 假红 |

---

## 三、收口复核

1. **施事／归属三问（逐块走完 7 块）**
   - 块 3（`md:43`）：`text:12`「When **she** tried to turn **her** around by the shoulders, **Brisa** collapsed」——`she`＝Diana（主语），`Brisa`＝collapsed 的主语（受事被施动的对象）；md:45「母亲伸手想把她转过来，女儿却一下子瘫了下去」归属正确。
   - 块 4（`md:55`）：`text:27`「Diana went to the kitchen…She left the glass on the dresser…placed **her hand on her daughter's back**」——主语全程 Diana；md:57 归属正确。
   - 块 5（`md:67`）：`text:27`「Her stomach then clenched **as soon as she realized she didn't know quite what she was touching**」——`she`＝Diana；`it`＝她摸到的那个东西；md:69「她伸手去安抚女儿，手一碰，胃就抽紧了」归属正确。
   - 块 6（`md:79`）：`text:27`「**Diana** jumped up and rushed to turn on the light」——开灯的是 Diana；md:81「母亲一下子跳起来去开灯」归属正确。
   - 块 7（`md:91`）：`text:27`「She went to the office for her AirPods」——`she`＝Diana，AirPods 归她；md:93「她去书房拿了耳机」归属正确。
   - 块 2（`md:31`）：`text:6`「the mental image of **her** daughter from the other side of the window, **seen from the apartment across the way**」——被看的人是女儿、看的人是对面楼；md:33「对面楼的人从窗外看进来会看到女儿的样子」方向正确（md:37 的「把『看』的方向掉个头」评述也成立）。
   - ⇒ **七块均无施事反转**；本章的归属风险集中在 `md:11` 把两次触摸并成一次（见判定表 #14）。
2. **「谁的」（梦游归属）**：`text:27`「now **she** was absolutely sure **Brisa** had been sleepwalking」——下判断的是 Diana，被判断的是 Brisa；md:13 未标明这一点，且 Carlos 叫不醒这件事整段缺席（判定表 #17、#21）。
3. **数字／日期**：本章原文**不含任何阿拉伯数字与日期字样**（`/usr/bin/grep -nE '[0-9]' text/ch07_chapter_7.txt` → 只命中第 1 行章号 `7`，退出码 0），md 也未给出任何数字断言 ⇒ 无计数类断言可核。
4. **跨章指认**：md 全文无指向其他章的事件描述 ⇒ 无跨章核对项。（相关背景：`text/ch06_chapter_6.txt:12` 已有 "approach Brisa like a sleepwalking explorer"，说明「梦游」是 Diana 的既有解读框架。）

---

## 已核实为正确

以下写法在审查中看似有误，回原文逐字核对后**成立**，任何后续改稿都不得改动（`docs/rules/审查表.md` R5.5）：

1. **`md:45`「像被关掉了开关一样」、`md:49`「女儿不是昏过去，是被关掉了」忠实于原文比喻**。依据：`text/ch07:12`「She collapsed as if she'd been deactivated, as if the energy that had kept her standing had suddenly been cut off.」
2. **`md:25`「作者先用一个没充上电的小夜灯交代『黑是本来就有的』」成立**。依据：`text/ch07:6`「They always left the mushroom lamp on, but she'd forgotten to charge it during the day, so that night, it had turned off a bit early.」
3. **`md:37`「作者把『看』的方向掉了个头——不是女儿看外面，是外面看进来」成立**。依据：`text/ch07:6`「the mental image of her daughter from the other side of the window, seen from the apartment across the way」——原文确实把「被看」的方向从女儿转向对面楼。
4. **`md:57`「把水杯放在柜子上」译法成立**（原文 `dresser`＝梳妆台／矮柜）。依据：`text/ch07:27`「She left the glass on the dresser」；`md:57` 用「柜子」是通顺的中译，未改变事实。
5. **`md:61`「只有焦虑到那个份上的人，才会在孩子睡着后还伸手去数她有没有在呼吸」成立**。依据：`text/ch07:27`「placed her hand on her daughter's back to make sure she was breathing normally」。
6. **`md:85`「作者用『上半身趴着、下半身倒立』这个自相矛盾的姿势制造生理不适」成立**。依据：`text/ch07:27`「face down from the waist up, but her knees and the tips of her toes pointed toward the ceiling」。
7. **`md:97`「结尾把恐怖换成了荒诞的日常」成立**。依据：`text/ch07:27`「She went to the office for her AirPods, put on a podcast, and proceeded to lie awake all night right next to Brisa」——应对方式是放播客，原文没有给出任何查证动作。
8. **`md:123` 的 rousing 例句逐字命中原文**。依据：`text/ch07:27`「but rousing that man was basically impossible」。
9. **机器层「关键词」子项 CJK=0 不是本章缺陷**。依据：`ch03 chapter 3.md:23`、`ch04 chapter 4.md:23` 的「关键词」子项同样全为英文短语 ⇒ 全书体例，非形态偏离。
10. **机器层存档与复跑一致**。依据：`bash scripts/chapter.sh "…/ch07 chapter 7.md" --json` 复跑退出码 0、`verdict: ok`、7 个引语字符位与 `2-machine.json` 相同（复跑输出写临时文件，未覆盖存档）。

---

## 六、复核轮次二判定（2026-10-21 23:35）

**受审版本**：`ch07 chapter 7.md` = 11758 字节 / 140 行 / md5 `c6d3c343fcaad849af1d24ba8e017f60`（commit `6f02ca802`，21:40:08）。
**机器层复跑**：退出码 **0**，`verdict: ok`，`issues` 五组全空；引语字符位 [139, 418, 742, 1367, 2466, 2705, 2999] 与存档 `2-machine.json` 一致。逐字自检：原句块 7/7、词汇例句 MISS = 0。

### 四组数（轮次二）

| 组 | 数 | 说明 |
|---|---|---|
| 逐字 | **7 / 7** | 8 段引语与 20 条词汇例句全部逐字命中原文（`check_md_quotes.py`） |
| 对应 | **7 / 7 块（21 问）** | 逐块重走 21 问归属，主语／受事／归属方向与轮次一相同且无变化 |
| 形态 | **0 偏离 ／ 1 假红** | `counts` 全零；「关键词」子项 CJK=0 与兄弟章同体例 |
| 断言 | **22** | 通过 13 ／ **阻断 0** ／ 提示 8 ／ 假红 1 ／ 跳过 0 |

### 轮次二判定表（增量）

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| 23 | 轮次一的阻断 E1（两次触摸并成一次）已销账 | `md:11` 现文拆成「母亲伸手想把她转过来，她却一下子瘫了下去」＋「后来母亲再伸手去安抚，手一碰，胃就抽紧了——摸到的身体既不像背也不像胸」；`text/ch07:12`「When she tried to turn her around by the shoulders, Brisa collapsed.」＋`text/ch07:27`「it felt nothing like her back or even her chest」 | 已修 | — |
| 24 | 轮次一的 E2（段落形态）已销账 | `md:15` 现文「正文段落不长却连成一条单向的下坠」；段落实测 8 段，末段 `:27` 占 57.9% | 已修 | — |
| 25 | 轮次一的 E4（开灯后的「正常」）已销账 | `md:87` 现文「开灯之后看到的东西和她以为看到的完全不一样」；`text/ch07:27`「She was in an uncomfortable position, but not an unnatural one, nothing like what she'd seen.」 | 已修 | — |
| 26 | `md:13`「母亲认定女儿是在梦游」已标明归属 | `text/ch07:27`「now she was absolutely sure Brisa had been sleepwalking」 | 通过 | — |
| 27 | 「我口渴」（`:24`）与 `:21` 真正醒来仍未进 md | `/usr/bin/grep -cE "thirsty|Get in bed|bathroom|camp sleeping|sleeping bag|rolled onto" "…/ch07 chapter 7.md"` → 0，退出码 1；`text/ch07:24`「"I'm thirsty."」 | 漏（覆盖缺口） | 提示 |
| 28 | `:9` 两句台词仍未进 md | `text/ch07:9`「"Honey, what's going on? Get in bed." … "Do you have to go to the bathroom?"」 | 漏（覆盖缺口） | 提示 |
| 29 | `:27` 露营睡袋＋翻身趴下仍未进 md | `text/ch07:27`「She took one of the kids' camp sleeping bags from the closet… her daughter had now rolled onto her stomach.」 | 漏（覆盖缺口） | 提示 |
| 30 | `:18`／`:21`「站起来却像睡着」仍未进 md | `text/ch07:18`「she didn't seem to comprehend her words」；`:21`「although her eyes were open, she was fast asleep」；`/usr/bin/grep -c "听不进" "…/ch07 chapter 7.md"` → 0，退出码 1 | 漏（覆盖缺口） | 提示 |
| 31 | `:27` 叫不醒 Carlos 仍未进正文 | `text/ch07:27`「She tried to wake Carlos up… rousing that man was basically impossible.」；`/usr/bin/grep -nE "sleepwalking\|Carlos" "…/ch07 chapter 7.md"` → 仅 `md:123` 词汇例句 | 漏（覆盖缺口） | 提示 |

### 轮次二结论

- **本章无阻断**（轮次一的 E1 阻断已修并复核通过）。
- 剩余 5 条提示项全部是「原文有、md 未覆盖」的**漏**，没有一条与原文逐字冲突，**不构成阻断**。
- 覆盖缺口集中在一处：`:18`–`:24` 这段（站起来却听不进话 → 睁眼却睡着 → 被放回床上 → 醒来要水）以及「叫不醒丈夫」，在 md 的七块（落在 `:6/6/12/27/27/27/27`）里没有任何对应分析。
