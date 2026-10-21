# 第 11 章 R5 判定（人工审查）

**覆盖声明**：本次人工审查**只覆盖第 11 章**（`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch11 chapter 11.md`，154 行，8 个引语块）。R0–R5 全流程已跑完（`1-suread.json` → `2-machine.json` → `3-diff.md` → 本文件）。**全书其余各章（ch00–ch10、ch12–ch17）只有机器层，没有人工层，不写成「通过」**（`docs/rules/审查表.md:31`：「抽样章号与理由写进 `4-verdict.md` 的覆盖声明；**没跑的章要写「只有机器层」，不许写成「通过」**」）。机器层唯一真值＝`text/ch11_chapter_11.txt`（156 行，27,504 字符）。审查人：DSH-Mac。本轮**未改任何成品 md**，未执行 git add / commit / push。

---

## 一、四组数（只报这四组）

| 组 | 数 | 依据 |
|---|---|---|
| 逐字 | **8 / 8 引语块**；**词汇 22 / 22 例句** | `2-machine.json`：`verdict: ok`，8 个引语块 `segments[].ok=true`（字符位 3 / 2045 / 6587 / 10120 / 11214 / 16602 / 24777 / 26840；词数 35/38/56/38/30/… 全部落在 30–70 词区间）；`counts`：`quote_long 0`、`segment_miss 0`、`empty_quote 0`。另：自写脚本核 `本章词汇` 表 22 条例句 → `rows 22 not_verbatim 0`（唯一 3 处未命中为表头行）。 |
| 对应 | **8 / 8 块（24 问）＋导航 5 条 ＋ 词汇 22 条 ＋ 总结 1 条** | R4 逐块走完 8 个块，每块固定三问（①每个动词的主语是谁 ②受事／宾语是谁 ③归属方向回原文看 by/to/from/of）＝24 问，全部回原文有出处或列入差异单；导航 5 条、词汇 22 条、一句话总结 1 条另行逐句对账。**结果：3 条阻断 + 7 条提示**（见 §2 判定表 #12–#21）。 |
| 形态 | **0 偏离 ／ 1 假红** | `2-machine.json` `counts`：`struct_bad 0`、`keyword_bad 0`、`cjk_low 0`、`empty_quote 0`、`quote_long 0`、`template 0`；`form`：`h1_shape_ok true`（"11. Chapter 11"）、`nav_count 5 ok`、`blocks 8`、`subitems_modal` 四件（中文理解／关键词／为什么这样写／读者视角提示）与 `profile: novels` 一致、`baseline: book`、`issues` 四组全空。唯一异常＝「关键词」子项 CJK=0，与兄弟章同体例（`ch03 chapter 3.md:23`、`ch04 chapter 4.md:23` 的关键词子项同样全为英文短语）⇒ **假红**，非本章偏离。 |
| 断言 | **27** | 判定表 27 行：通过 11 ／ **阻断 3** ／ 提示 8 ／ 假红 1 ／ 跳过 1 ／ 编造 0 复核 3。 |

---

## 二、判定表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 8 个引语块与原文逐字一致 | `2-machine.json` `quotes[].segments[].ok=true`（8/8） | 通过 | — |
| 2 | 8 个引语块词数均落在 30–70 词、1–3 句、单自然段 | `2-machine.json` `quotes[].words`；`counts.quote_long 0` | 通过 | — |
| 3 | `本章词汇` 22 条例句均为原文子串 | 自写脚本 `rows 22 not_verbatim 0` | 通过 | — |
| 4 | 块 1（`md:19-27`）对应「醒来只见一只 MediaMarkt 纸袋」 | `text/ch11:6`「Between the wall and the mall toilet, there was a small paper gift bag…a bag from MediaMarkt.」 | 通过 | — |
| 5 | 块 2（`md:31-39`）对应「灯灭挥手＝她教孩子的游戏」 | `text/ch11:9`「she had just reenacted their game」「a rave for children」 | 通过 | — |
| 6 | 块 3（`md:43-51`）对应「两条沉重带子滚下大腿、盘好塞回洞里」 | `text/ch11:12`「two heavy bands rolled down her thighs…put them back in the hole they had come out of」 | 通过 | — |
| 7 | 块 4（`md:55-63`）对应「红泳衣＋Victoria 旧白球鞋＋晒成古铜色＋十一二岁」 | `text/ch11:60`「a red swimsuit…Victoria brand, dirty and worn, no laces…She looked eleven or twelve years old.」 | 通过 | — |
| 8 | 块 5（`md:67-75`）对应「圆脸／雀斑／银圈耳环／血冷」 | `text/ch11:63`「Her face was round…a stunning explosion of freckles…silver hoop earrings. Alba's blood went cold.」 | 通过 | — |
| 9 | 块 6（`md:79-87`）对应「肚中银色触手像迪斯科球」 | `text/ch11:99`「she saw silvery tentacles coiled around her intestines…had a disco ball in her belly.」 | 通过 | — |
| 10 | 块 7（`md:91-99`）对应「不用枪不用冰块、徒手把耳环按穿耳垂」 | `text/ch11:138`「She didn't use a piercing gun, or numb her up with an ice cube」；`:141`「squeezing each earring post directly through Alba's pale earlobe」 | 通过 | — |
| 11 | 块 8（`md:103-111`）对应「触手扑向女孩、甩出血染 friendly Claire's 橱窗」 | `text/ch11:153`「Without warning, the tentacles stretched toward the girl, as if they wanted to give her a hug. Or strangle her, maybe.」「ruthlessly painting the friendly Claire's window displays.」 | 通过 | — |
| 12 | `md:12`「前面都是**母亲**在怀疑、在害怕」 | `text/ch11:12`「She thought about her **sister**」；`text/ch05:549`「who was six years older than Alba」；`text/ch10:138`「Diana looked over at **her mother**」 | 与原文不符 | **阻断** |
| 13 | `md:14`「她身上最像 **Diana** 的地方＝把手柄捡起来塞到门外」 | `text/ch11:12`（共用手机）、`text/ch11:84`（Diana pinched her leg）＝Diana 与 Alba 的两条联结；`text/ch11:9` 手柄一段中 Diana 零出现 | 归属方向错 | **阻断** |
| 14 | `md:99`「序章里**那对**多出来的银耳环」 | `text/ch00_prologue.txt:21`「She counted **nine hoops**, all different sizes, **five in one ear and four in the other**」；`text/ch12:6` 同源；`text/ch11:141`「several of the larger ones…Alba's **right ear**」 | 数字错 | **阻断** |
| 15 | `md:109`「女孩**想守住**的橱窗」「**圣洁**与暴烈互相覆盖」 | `text/ch11:153`「the girl **watched** as Alba started shaking again」「the **friendly** Claire's window displays」 | 措辞过头（原文无此定性） | 提示 |
| 16 | `md:11`／`md:12`／`md:154`「把银耳环**钉进她的耳朵**」 | `text/ch11:141`「began to pierce **Alba's right ear**」；`:138` 逐只取较大的几只 | 部位／数量泛化 | 提示 |
| 17 | `md:11`「门外**躺着**…**用身体挡着门**」并列 | `text/ch11:45`「leaning against the door, barricading her inside」；`:60` 躺地；`:63`「she wouldn't have had time to jump up from the floor」 | 时序／状态错位 | 提示 |
| 18 | `md:69`「她**认得这张脸**」、`md:73`「**找了多年**却在此地重逢」 | `text/ch11:63`「the image she'd retained…had been **blurry and imprecise**, and she **didn't recognize** that vacant stare…She'd long **dreamed of crossing paths** with her」 | 措辞过头 | 提示 |
| 19 | `md:25`「读者立刻知道这是**平安夜**」 | `text/ch11:6` 引语不含节日；`text/ch11:87`「Since it was Christmas Eve, the mall had closed without the usual routines.」 | 解读当事实 | 提示 |
| 20 | `md:14`「Alba 从照顾别人的母亲变成**被安排的人**」「让她把最后一样东西**交了出去**」 | `text/ch11:9`「she…**had made up her mind**」「she wanted to try to keep them from getting dirtier」「Such missions needed to be carried out even if the world was in flames」 | 措辞过头（主动写成被动） | 提示 |
| 21 | 覆盖缺口：Splau／平安夜未收尾、Claire's 与 Brigitte、Bijou Brigitte／Caga Tió／Brisa、手柄战胜恐惧、每五分钟绞痛与三次分娩、两个星期着迷、童年掐腿、镜中显老与问 Diana 要医生电话 | `text/ch11:87`、`:99`、`:105`、`:126`、`:129`、`:84`、`:93`、`:9` | 漏（覆盖缺口，不阻断） | 提示 |
| 22 | 「关键词」子项 CJK=0 是否形态偏离 | `ch03 chapter 3.md:23`、`ch04 chapter 4.md:23` 同体例；`2-machine.json` `blocks[].cjk.关键词 = 0` | 与兄弟章同体例，非偏离 | 假红 |
| 23 | md 是否存在「原文没有」的杜撰事实（编单） | 逐条核对 `md:11-15`、`md:19-111`、`md:113-151`、`md:154` 的事实性断言（人名／数字／时间／亲属关系／事件／说话人／店名／地名） | **无编造**（C＝0） | 通过 |
| 24 | 红泳衣女孩的身份是否被写错成女儿 | `text/ch12:162`「including **Alba, age twelve**」；`:168`「Twelve-year-old Alba, with her red swimsuit and sun-bleached hair」；`:213`「The red swimsuit and the worn-out Victoria sneakers…」；md 全篇只称「女孩／孩子」 | 未写错（但**不得**在后续改稿中把身份「说明确」——本章原文未交代） | 通过 |
| 25 | `md:93`「徒手把银耳环一根根按进她的耳垂…直到耳环从另一侧穿出来」是否准确 | `text/ch11:141`「pressing the earrings all the way through…not giving up until she saw the earring come out on the other side of the lobe or the cartilage」 | 准确 | 通过 |
| 26 | `md:87`「她盯着看了整整五分钟」是否准确 | `text/ch11:99`「She stood like that for **five minutes**, staring in fascination」 | 准确 | 通过 |
| 27 | 其余 16 章（ch00–ch10、ch12–ch17）的人工层结论 | 本次只跑第 11 章（`docs/rules/审查表.md:31` 要求写明） | 只有机器层，未核 | 跳过 |

---

## 三、收口复核（三处最需盯的地方的独立结论）

1. **「前面几章是谁在怀疑、在害怕」——md 写错了，属阻断。**
   - 原文铁证：`text/ch11:12`「She thought about her **sister**, who'd never understood why they shared phones」；`text/ch05:549`「She, on the other hand—who was **six years older than Alba**」⇒ Diana 是**姐姐**；`text/ch06:6`「**Diana** lived in terror of the possibility that something would happen to her children」；`text/ch09:6`、`text/ch10` 整章是 Diana 在 Splau 门口数人头。
   - 母亲是 **Carmen**，在 ch10 处于「躺在草地上」的位置（`text/ch10:60`、`:138`、`:159`），**不是怀疑者**。
   - ⇒ `md:12` 的「前面都是母亲在怀疑、在害怕」必须改。
2. **「手柄执拗＝像 Diana」——方向错，属阻断。**
   - Alba 与 Diana 的联结**只有两条**：`text/ch11:12`（共用手机的妹妹）与 `text/ch11:84`（童年捉迷藏「until Diana pinched her leg」）。
   - 手柄那一整段（`text/ch11:9`）**Diana 零出现**；原文对 Alba 的定性是「她**自己拿定了主意**」（"had made up her mind"、"even if the world was in flames"），不是「被安排」。
   - ⇒ `md:14` 两处都要改（详见 `3-diff.md` W2、W9、W10）。
3. **「序章里那对多出来的银耳环」——数字错，属阻断。**
   - `text/ch00_prologue.txt:21`「She counted **nine hoops**, all different sizes, **five in one ear and four in the other**」；`text/ch12:6` 同一记忆复现。
   - 本章 `text/ch11:141` 女孩取「several of the larger ones」逐只钉进 **Alba 的右耳** ⇒ 与「九只、尺寸各异」互证，绝不是「一对」。
   - ⇒ `md:99` 必须改；且**不得**在改稿中把女孩身份写成女儿（见判定表 #24）。

---

## 四、已核实为正确（防误修清单）

以下写法在审查中看似有误，回原文逐字核对后**成立**，任何后续改稿都不得改动（`docs/rules/审查表.md` R5.5）：

1. **「红泳衣女孩」的身份 md 没有写错。** md 全篇只称「女孩／孩子」，从未说她是 Alba 的女儿——与全书铁证（`text/ch12:162`、`:168`、`:213`：女孩＝**Alba 十二岁时的自己**，营地幽灵）相容。⚠️ 反向纪律：**也不许**在改稿时替本章补一句「她其实是……」——`text/ch11` 原文没有交代。
2. **`md:99`「耳环在这里不是装饰而是记号」成立。** 依据 `text/ch11:141`「not giving up until she saw the earring come out on the other side of the lobe or the cartilage」——耳环确实从「饰物」变成「记号」（与序章「她从没见过的耳环」形成闭环）。要改的只是「那对」→「那几只／九只」。
3. **`md:73`「作者把恐惧的落点放在『认出』而不是『看见』」这一手法判断成立。** 依据 `text/ch11:63`「she was sure she knew exactly who it was」——原文确实把反应写成「知道是谁」而非「看清脸」。要改的只是 md 把「多年没看清」写成了「找了多年」。
4. **`md:87`「真正被吓住的人不会这样」成立。** 依据 `text/ch11:99`「staring in fascination」「the first time in years she'd looked in a mirror for so long without thinking of anything but herself」——原文明写这是**着迷**，不是吓住。
5. **`md:105`「像要拥抱，也可能是要勒住她」成立且是逐字对译。** 依据 `text/ch11:153`「as if they wanted to give her a hug. **Or strangle her, maybe.**」——md 的「也可能」正是原文 "maybe" 的对应。
6. **`md:111`「结尾那一下『优雅地折回』最冷」成立。** 依据 `text/ch11:156`「the tentacles returned to their resting state, **gracefully folding back** into her abdomen」——"gracefully" 即「优雅」。
7. **`md:154`「她被剖开的肚子里那场银色舞蹈」成立。** 依据 `text/ch11:99`「The dancing tentacles hypnotized her」＋`:99`「she saw silvery tentacles coiled around her intestines」。
8. **`md:13`「Tropes 兑现/反转：门外挡门的那个孩子不是走散了等人来救，她是在等人想起她」成立。** 依据 `text/ch11:78`「Because you forgot about me.」（女孩给出的唯一理由）＋`text/ch11:66`「"What's your problem?" the girl asked scornfully while she petted the box she had taken.」。
9. **`md:25`/`md:61` 的「具体物品推进」这一手法判断成立**（纸袋→泳衣→耳环→橱窗的物链在原文中确实成立）；`md:61`「作者用泳衣和晒痕把她留在夏天」有出处（`text/ch11:60`「tan」「blond ponytail…bleached and limp from sun and chlorine」）。要改的只是 `md:25` 把「平安夜」提前说成引语可交付的事实。
10. **`md:12`「主角还在盯着自己肚子里那场舞蹈出神」成立。** 依据 `text/ch11:99`「staring in fascination」＋`text/ch11:99`「The dancing tentacles hypnotized her」。
11. **「关键词」子项 CJK=0 不是本章缺陷。** 依据 `ch03 chapter 3.md:23`、`ch04 chapter 4.md:23` 的「关键词」子项同样全为英文短语 ⇒ 全书体例，非形态偏离（假红）。
12. **8 个引语块的逐字性与句级形态全部成立。** 依据 `2-machine.json`（`ok=true`×8、`quote_long 0`、`empty_quote 0`）＋自写脚本 `rows 22 not_verbatim 0`。**任何改稿都不得改动引语正文**——本轮 3 条阻断与 8 条提示**全部落在导航／中文理解／为什么这样写／读者视角提示／词汇提示层**，引语原文一字未动。

---

**审查人**：DSH-Mac。**未修改任何成品 md；未执行 `git add` / `git commit` / `git push`。**
