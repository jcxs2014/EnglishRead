# 第 2 章 R3–R4 差异单（人工审查）

- 审查对象：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch02 chapter 2.md`（成品，156 行，8 个引语块）
- 唯一真值：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch02_chapter_2.txt`（原文，483 行，43,371 字节）
- 机器层：`bash scripts/chapter.sh "…/ch02 chapter 2.md" --json` → **退出码 0**，`verdict: ok`；`issues` 只有 `keyword_long` 8 条与块数提示，**判红项全空**（复核输出落在 `/tmp/ch02_machine_recheck.json`；仓库内 `review/ch02/2-machine.json` 未改动、未覆盖）
- 流程：R1 素读（`review/ch02/1-suread.json`，先读原文、后开 md）→ R2 机器层 → R3 三张单子 → R4 逐块＋固定三问
- 行号约定：`text:NNN` = 原文行号；`md:NNN` = 成品 md 行号；字符区间为原文 UTF-8 解码后的 `[start, end)`
- 取证口径：全部用显式路径 `/usr/bin/grep`（`text/` 被 `.gitignore` 忽略，`git grep` 对它永远查无），短词用 `-w`，交替匹配用 `-E`；词数用 Python 按空格切分实测
- **本单状态**：**全部条目已销账**——`§〇` 的 2 条、`§一` 的 L1–L7、`§三` 的 W1–W7 均已由作者按本单修完并入库（commit `1fcf5c7c6`／`2544325a9`）。本单为只出指令的记录单，**本身不改动任何成品 md 文件**；`git` 操作由作者执行。

---

## 〇、本轮已修复（记录用，不再需要动）

| # | 位置 | 原写法 | 现写法 | 原文依据 | 复核命令（期望退出码） |
|---|---|---|---|---|---|
| F1 | `md:75`（块 5 读者视角提示） | 记住「只剩领口」这个画面。**本章后面还会出现一次类似的失焦，那时她怀里抱的是孩子。** | 记住「只剩领口」这个画面；本章后面她抱着孩子追店员时，注意力再次收缩，只剩眼前那一小块布。 | `text/ch02:249`「Still, as Alba trailed the associate, MediaMarkt began to vanish around her until it completely faded away… all she could see was the shirt collar of the associate.」——**本章只有这一次收缩**，且「水母」的第二次出现是 `text/ch02:219`「Carmen turned for a second and saw a swarm of jellyfish on the screen at her back」（**电视屏幕上**的画面，不是失焦） | 原句已不可核（`/usr/bin/grep -n "类似的失焦" "…/ch02 chapter 2.md"` → 期望 exit=1） |
| F2 | `md:109`（块 8 为什么这样写） | 最后一句只有**五个词** | 最后一句只有**四个词** | `text/ch02:483`「They could find no solace.」——按空格实测**是五个词**（They / could / find / no / solace.），区间 `[41930,41956)` | — |

> ⚠️ **F1、F2 两条「已修复」都需要回看**：
> - **F2 是把对的改错**：原文「五个词」本来就是对的（Python 按空格切分＝5），改成「四个词」后与原文不符 ⇒ 记为 **W1（阻断）**，建议改回「五个词」。
> - **F1 只修掉了「水母／失焦」那一半**：新句里「本章后面」「再次收缩」仍断言存在**第二次**收缩，而本章没有第二次（失焦只有 `:249` 一处，且原句 5 引的就是它）⇒ 残余记为 **W2（阻断）**。

---

## 一、漏（L）

### L1｜本章没有任何时间锚点（星期几、几点、离圣诞几天、两个女人的年龄）——md 全文只有「圣诞前」一处｜档：提示（漏）

**原文侧**（`text/ch02_chapter_2.txt:36`，区间 `[2177,2245)`）：

> "OK. But who’s sneaking around pressing buzzers on a Wednesday at seven a.m.?"

**原文侧**（`text/ch02_chapter_2.txt:132`）：

> "Despite there being only three days until Christmas, there weren’t many people at Finestrelles."

**原文侧**（`text/ch02_chapter_2.txt:165` / `:171`）：

> "Tomorrow is my birthday." / "The next day. Christmas Eve? Are you out of your mind? Do you know how many people will be out?"

**原文侧**（`text/ch02_chapter_2.txt:48`，区间 `[4268,4309)`；`:129`，区间 `[13790,13847)`）：

> "the face of a seventy-five-year-old woman" / "the face of the thirty-seven-year-old whose eyes were raw and burning"

**md 侧**（`ch02 chapter 2.md:11`）：

> …被一整个**圣诞前**的早晨和一座冷清的商场磨得没脾气…

**影响**：读者拿不到「周三早上七点」「离平安夜三天」「Carmen 75 岁、Alba 37 岁」这三个锚点，就无法把本章与第 1 章（Brisa 的圣诞演出）放进同一条时间线上；本章恰恰是全书第一次给出星期与日期锚点的一章。

**修法**：建议在 `md:11` 或块 1／块 8 的中文理解里补一句，例如「**周三早上七点，距平安夜还有三天（Carmen 七十五岁，Alba 三十七岁）**」。

### L2｜每天四趟接送、五人「小公社」——全章日程与「祖母＝母亲延伸」的因由，md 未出现｜档：提示（漏）

**原文侧**（`text/ch02_chapter_2.txt:117`，区间 `[7356,7419)`、`[7734,7785)`、`[7972,8146)`）：

> "Every morning, Carmen went with Alba to take the kids to school. And to pick them up for lunch. And to take them back for the afternoon. And to pick them up again. And to take them to their after-school activities… It was a long and exhausting circuit, because the school was in Esplugues, half an hour from home, and part of the trip had to be done by bus. No one had suggested the infinitely more reasonable option: that Carmen stay home with the baby while Alba took the other children to class. The five of them paraded in and out every day like their own little commune: grandmother, mother, two children, seven and nine, and a baby in a stroller, less than a year old."

**md 侧**：`md:11` 只有「连同一同带娃的母亲 Carmen」；`md:45` 只有水母比喻的解读。**四趟、Esplugues、五人公社、「更合理的方案没人提」全部缺席**。

**影响**：块 3 的水母比喻（祖母＝母亲身体的延伸）缺了它的**结构来源**——正是这段日程让「三人合成一个生物」成为日常；缺了它，块 3 只剩一个漂亮比喻。

**修法**：建议在块 3 的「中文理解」或 `md:11` 补一句：「**每天四趟接送——上学、午饭、下午、放学加课外班，学校在 Esplugues，半小时路程；五个人的小公社：祖母、母亲、两个孩子（七岁、九岁）和一个不到一岁的婴儿。**」

### L3｜Alba 没有工作、自己的事一直被推后、Diana 是唯一坚持让她看病的人——md 未出现｜档：提示（漏）

**原文侧**（`text/ch02_chapter_2.txt:336`，区间 `[26640,26679)`）：

> "Oh, quiet, Mom. The one I don’t have."

**原文侧**（`text/ch02_chapter_2.txt:129`，区间 `[12644,12704)`、`[12954,13015)`）：

> "The supposed demands of motherhood always meant postponing whatever had to do with her exclusively." / "Only her older sister, Diana, insisted she go to a specialist and sent her a dermatologist’s number several times. But she hadn’t listened…"

**md 侧**：`md:11` 只写「把全年提前算好」（即提前采购、提前计划）；`md:21` 的中文理解也只讲「提前」。

**影响**：`md:12`「承第一章那种「非做不可」的焦虑」与 `md:25`「三个动作全是完成态」都把 Alba 写成**完美主义的计划者**；原文的底色是**她自己的事一直被推后**（没工作、眼皮病不治、皮肤科号码不听）。少了这一层，人物弧线（`md:14`「滑到在商场地板上缩成一团」）失去上半段的重量。

**修法**：建议在块 1（`md:21`）或块 6 补一句：「**她没有工作**（`:336`「The one I don’t have.」），**属于自己的事一直被推后**：眼皮从出生起就皱而鳞状，姐姐 Diana 几次把皮肤科电话塞给她，她都没去。**」

### L4｜父亲已故；二十三个癖好是 Diana 在父亲葬礼的守夜上数的——md 只有数字，没有前因｜档：提示（漏）

**原文侧**（`text/ch02_chapter_2.txt:132`）：

> "Diana had sensed this for a long time, and a few years ago, at her father’s funeral, she’d decided to confirm it. As an exercise in warding off the bewilderment of a sudden death, she had spent the wake observing the women on her mother’s side, from her aunts to her most distant cousins… She had counted twenty-three obvious manias."

**md 侧**（`ch02 chapter 2.md:57`）：

> 她数出二十三个显而易见的癖好。其中有一个是所有人共有的：谁只要说出「死亡」这个词，就把两只脚跟并在一起。最精巧的一个，她只在马德里的双胞胎表亲身上见过。

**影响**：md 只给了「二十三」这个数，没有交代「谁数、为什么数、在什么场合数」。读者会把这份清单当成冷幽默的家族笑话，错过它真正的来源——**一场葬礼守夜上对「突然死亡」的恐惧**。第 5 章的同类缺口（父亲已故）当时已记为 `ch05/3-diff.md` L1，本章是同一条线的第二处。

**修法**：建议在块 4 的「中文理解」补一句：「**这份清单是 Diana 在父亲葬礼的守夜上数的**——她为了抵抗「突然死亡」的困惑，盯着母系所有女人的癖好数了三天。**」

### L5｜Brigitte 体操馆那一整场（平衡木、白色滚边连体衣、两位教练、三米米色地毯、「像个小连环杀手」）——md 只借了一句 leotard｜档：提示（漏）

**原文侧**（`text/ch02_chapter_2.txt:471`，区间 `[35880,35954)`、`[36341,36373)`）：

> "The neckline of her leotard, white with silver trim, was soaked with blood. Some droplets had dotted the beam and the mat beneath it." / "a row of viscous red drops decorating the three meters of beige carpet between the balance beam and the bleachers"

**原文侧**（`text/ch02_chapter_2.txt:474`，区间 `[37203,37241)`）：

> "why she looked like a little serial killer"

**md 侧**：全章只在 `md:105` 借了 "Brigitte’s leotard" 一笔；`md:11` 只写「两个女孩在同一时刻流鼻血」。

**影响**：本章最重的一场戏（血渗进连体衣、教练更心疼地毯、抱走女儿的那位一身干净）没有进 md，读者看到的是「一句收尾」和「一块血块」，缺少从**现场**到**母亲取块**的因果台阶。

**修法**：建议在块 7 或块 8 的「中文理解」补两句：「**一个月前，Brigitte 在体操馆的平衡木上开始流血，白色滚边连体衣被血浸透，三米米色地毯上留下一排血点；两个教练一个把她抱走，另一个更心疼地毯。**」

### L6｜手机意外录下的视频（血块与塑料尺并排、自己开始播放）——md 未出现｜档：提示（漏）

**原文侧**（`text/ch02_chapter_2.txt:480`，区间 `[41062,41127)`、`[41374,41429)`、`[41492,41513)`）：

> "she didn’t realize that she had hit record and was taking a video" / "The video she had just taken started playing on its own: In it, the clot was where she had put it, unmoving alongside Tomás’s plastic ruler. In the background: her accelerated breathing."

**md 侧**（`ch02 chapter 2.md:99`）：

> 记住「翻过来也没断」这个细节——紧接着她就会找出一把尺子，量出三十厘米；而这块血块在本章末尾还会被再次提起。

**影响**：原句 7（`md:91`）只引到 "it didn’t break, didn’t explode"，量尺与视频都落在引文之外；md 用「紧接着她就会找出一把尺子」预告了尺子，却漏掉了手机掉在地毯上、视频自己播起来这一节——那是全章最冷的一笔（恐惧被录下来自己重播）。

**修法**：建议在块 7／块 8 补一句：「**她本来只想拍照发给儿科医生，却误按了录像键；手机掉在地毯上后，那段视频自己播了出来：血块与 Tomás 的塑料尺并排，背景里是她自己加速的呼吸。**」

### L7｜Alba「跨门两次」的强迫——本章最能说明她这个人的细节，md 未出现｜档：提示（漏）

**原文侧**（`text/ch02_chapter_2.txt:132`）：

> "Once there, Alba furtively crossed the threshold of MediaMarkt then came back out only to enter again, natural as could be, as if she didn’t know her mother was watching her. Carmen knew about her daughter’s compulsion to cross through a door or an archway twice."

**原文侧**（`text/ch02_chapter_2.txt:342`，区间 `[27025,27114)`）：

> "Alba had just stepped out of MediaMarkt—for the second time—"

**md 侧**：`md:13` 写了「恶眼被反用」与「祖母带娃模板被写成繁殖的病症」，`md:61` 写了「二十三个癖好」，但**没有一处写跨门两次的强迫**。

**影响**：md 侧读者能感到 Alba「有强迫」，却拿不到最具体的一次强迫（进店要跨两遍）。这处细节还与 `md:11`「躲老妇」的现场直接相关——她之所以躲不开「寡妇」，正是因为退路也是一道要跨两次的门槛。

**修法**：建议在块 5／块 6 的「中文理解」或 `md:13` 补一句：「**Alba 进店要跨两遍门槛（母亲知道这个强迫）；所以当那两个老妇迎面走来时，她退无可退。**」

---

## 二、编（C）

**无。** 已逐条核对 `md:11-15`（导航 5 项）、`md:19-111`（8 个引语块 × 四子项）、`md:113-152`（词汇 24 条）、`md:156`（一句话总结）中的事实性断言（人名／亲属方向／年龄／日期／数字／地点／次数／事件顺序），**未发现「md 有、原文无」的杜撰事实**：块 1–块 8 的引语与全部 24 条例句都是原文子串（8/8、24/24 逐字），导航与总结里的每条事实都能在原文指出出处。

本轮命中的存疑写法全部属于「**错**」（§三 W1–W7）或「**漏**」（§一 L1–L7）；其中两条「作者已改」的地方（§〇 F1/F2）经复核后发现**一处改错、一处只改了一半**，也记在 §三。

---

## 三、错（W）

### W1｜`md:109`「最后一句只有**四个词**」——原句是**五个词**，这一改把对的改错了｜档：阻断

**原文侧**（`text/ch02_chapter_2.txt:483`，区间 `[41930,41956)`）：

> "They could find no solace."

**词数实测**（Python 按空格切分）：

```
"They could find no solace." → 5  →  ['They', 'could', 'find', 'no', 'solace.']
```

**md 侧**（`ch02 chapter 2.md:109`）：

> …最后一句只有**四个词**，短到像一声叹气。

**影响**：`git log -S` 显示这行原写「**五个词**」（`cdcf14f2e` 起草即为「五个词」），被 `0661c9c0d` 改成「四个词」——**改动的方向是反的**：改前与原文一致，改后与原文不符，而「四个词」这个数在原文里根本不存在。读者一数就是五个；同书 `00_概述.md:46`「十、收尾是一句五个词」与 `00_金句精选.md:298`「全章最后一句只有五个词：我想要的不过是那两只手柄」指的是**第 16 章**结尾（`text/ch16:66`「I just wanted the controllers.」，同为五个词），**与本章不冲突**，不能用它们来改本章。

**修法**：**建议改回「最后一句只有五个词」**（并在同一处把「最后一句」的指代收紧，见 W5）。

### W2｜`md:75`（块 5 读者视角提示）「本章后面她抱着孩子追店员时，注意力**再次**收缩」——本章只有一次收缩，就在这一段里｜档：阻断

**原文侧**（`text/ch02_chapter_2.txt:246`）：

> "Holding the baby to her, increasingly worked up, she kept after the associate with the broken glasses, chasing him down aisles until he stopped to check something on a computer."

**原文侧**（`text/ch02_chapter_2.txt:249`，区间 `[21290,21582)`）：

> "Still, as Alba trailed the associate, MediaMarkt began to vanish around her until it completely faded away. Whenever she felt obsessive or anxious, the places she moved through shed all objects and life; they became thresholds that she alone crossed. In that moment, all she could see was the shirt collar of the associate. Everything else was blurry or dark, depending on the intensity of the light. For seconds, she lost herself in the details of the fabric’s edge, stretched out and frayed… until the weight of her son became intolerable: Since when did the child weigh thirty pounds?"

**md 侧**（`ch02 chapter 2.md:75`）：

> 记住「只剩领口」这个画面；本章后面她抱着孩子追店员时，注意力再次收缩，只剩眼前那一小块布。

**影响**：三重错位——
① **次数**：「再次收缩」断言有第二次；本章的收缩只有 `:249` 一处（`/usr/bin/grep -c "shed all objects and life" text/ch02_chapter_2.txt` → 1；「trances」也只出现在 `:252` 描述同一件事）；
② **时序**：「本章后面」把它推后，而原句 5 引的**就是**这一段本身，读者按提示往后找，只会扑空；
③ **与本块自相矛盾**：`md:73` 已经写明「注意力收缩之后留下的不是脸，是一小截领口的布——作者始终不肯让她看清那个**她追着的人**」，即收缩与追店员是同一个连续场景。

被本条取代的旧句「本章后面还会出现一次类似的失焦，那时她怀里抱的是孩子」是同一类错误（它把 `:219` 电视屏幕上的一群水母当成了第二次失焦）；`0661c9c0d`／`041dfc930` 改掉了「水母／失焦」那一半，却留下了「后面」「再次」两个同样指向「还有第二次」的词。

**修法**：**建议改为**「记住「只剩领口」这个画面——她怀里抱着孩子追店员，注意力收缩到只剩眼前那一小块布（就是这一段，没有第二次）。」

### W3｜`md:109`「三个解释来源（医生、教练、家人）」——原文列的是**五个**来源，同一块的中文理解已经列全｜档：提示

**原文侧**（`text/ch02_chapter_2.txt:483`）：

> "None of the explanations from pediatricians, gymnastics coaches, Carmen, Carlos, or Juan convinced them."

**md 侧**（`ch02 chapter 2.md:105`）：

> 儿科医生、体操教练、Carmen、Carlos、Juan 的话都说服不了她们；她们找不到任何安慰。

**md 侧**（`ch02 chapter 2.md:109`）：

> 三个解释来源（医生、教练、家人）被平铺成一份清单，等于宣告「所有正常解释都已被用尽」…

**影响**：同一块里 `:105` 列了五个、`:109` 说三个，读者会以为作者漏数了。五个来源里有三个是具体的人（Carmen、Carlos、Juan），「医生、教练、家人」把它压成三类，恰好抹掉了「连自家人也给不出说法」这层意思——而这层意思正是末句「They could find no solace.」的落点。

**修法**：**建议把「三个解释来源（医生、教练、家人）」改为「五类解释来源（两位儿科医生、两位体操教练，外加 Carmen、Carlos、Juan 三位家人）」**，与 `:105` 对齐。

### W4｜`md:61`（块 4 为什么这样写）「接着**他**抽出其中一条」——同块内「他」没有指代对象｜档：提示

**原文侧**（`text/ch02_chapter_2.txt:132`）：

> "She had counted twenty-three obvious manias. There was one tic that every one of them shared: They clicked their heels together whenever someone said the word death. The most sophisticated one she had only seen in their twin cousins from Madrid."

**md 侧**（`ch02 chapter 2.md:57`，经 `688db3eb2` 已改）：

> 最精巧的一个，**她**只在马德里的双胞胎表亲身上见过。

**md 侧**（`ch02 chapter 2.md:61`）：

> 作者把「疯」做成了一份可清点的清单：二十三个。…**接着他抽出其中一条**当作全族共有的本能——触发条件不是谁说了什么，而是「死亡」这个词本身…

**影响**：①上一句的主语是「作者」，「他」在中文里默认承接上句主语；而本书作者 Desirée de Fez 是女性，同书其它章的「为什么这样写」一律写「作者」不写「他」；②同块 `:57` 的「她」已被 `688db3eb2` 明确指为 **Diana**（`She had counted…` 的施事），于是同一块里「她」＝Diana、「他」＝作者，读者也可能把「他」误读成 Diana 的男性亲属；③原文里并没有「抽出」这个动作，只有叙述（"There was one tic that every one of them shared"），「抽出」是评论动作。

**修法**：**建议把「接着他抽出其中一条」改为「接着从清单里挑出其中一条」**（或「接着让 Diana 抽出其中一条」），并把「作者」补回主语。

### W5｜`md:109`「最后一句」——指的是哪一句？同一块内两个「最后一句」指向不同句子｜档：提示

**原文侧**（`text/ch02_chapter_2.txt:483`，本章真正的**末句**，区间 `[42104,42126)`）：

> "Even more disturbingly: It had happened to their daughters, not other women’s, and at the exact same time."

**md 侧**（`ch02 chapter 2.md:111`）：

> 本章还有**最后一句**压在这一段之上：出事的是她们自己的女儿，而且两场血发生在同一个时刻——记住这个「同时」。

**md 侧**（`ch02 chapter 2.md:109`）：

> …**最后一句**只有四个词，短到像一声叹气。

**影响**：`md:111` 把「本章的最后一句」判给了 "at the exact same time" 那句（成立），`md:109` 又用「最后一句」指 "They could find no solace."——那是**倒数第二句**（本章最后三句：14 词 + 5 词 + 18 词）。同一块内同一个词两个所指，读者读块 8 时会不知道作者在数哪一句。

**修法**：**建议 `md:109` 改为「引语里的最后一句只有五个词」**（或「倒数第二句只有五个词」），把「本章最后一句」留给 `:111`。

### W6｜`md:12`「恐惧线则借血**正式登场**」——与总览给出的恐惧线起点冲突｜档：提示

**总览侧**（`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/00_情感节点.md:58`）：

> ## 节点六：恐惧越过家门（ch06-ch07）

**总览侧**（`00_情感节点.md:28`）：

> ## 节点三：怪癖是可以点数的（ch02）

**md 侧**（`ch02 chapter 2.md:12`）：

> …欲望线在本章尚无迹可寻，**恐惧线则借血正式登场**。

**影响**：同书的第 1 章已经因为同一件事改过口径——`ch01 chapter 1.md:12` 原写「欲望线与恐惧线都还没**露面**」，因与「节点六：恐惧越过家门（ch06-ch07）」冲突，在 `0661c9c0d` 改成「都还没**成形**」。本章改用「正式登场」，等于宣布恐惧线在 ch02 就登场，与节点体系打架；本章在节点体系里的位置是「怪癖是可以点数的」（节点三）。

**修法**：**建议改为「欲望线在本章尚无迹可寻，恐惧线则开始渗血」**一类写法，与第 1 章的「还没成形」保持同一口径（恐惧真正跨出门在 ch06–07）。

### W7｜`md:12`「承第一章那种「**非做不可**」的焦虑」——引号里的词在第一章没有出处｜档：提示

**取证命令**（显式路径，不用 `git grep`）：

```
$ /usr/bin/grep -rn "非做不可" notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez
→ 00_金句精选.md:286
→ .overview_templates/ov_00_金句精选.md.tpl:286
→ ch16 chapter 16.md:81
→ ch02 chapter 2.md:12
退出码 0（**ch01 命中 0 处**）
```

**md 侧**（`ch02 chapter 2.md:12`）：

> 承第一章那种「非做不可」的焦虑，本章把它从一个人的内心检查放大成一个三代家庭的结构性症状…

**影响**：「非做不可」是**第 16 章**的原句用语（`text/ch16`「出于惯性，或者因为非做不可」），第 1 章没有这四个字（第 1 章的焦虑是**反复检查直发夹**）。读者按引号去第 1 章找，会以为第 1 章写了「非做不可」。语感上两句其实说的是结构相似的东西（提前准备＋停不下来），所以这是措辞出处问题，不是事实错误。

**修法**：**建议把「承第一章那种「非做不可」的焦虑」改为「承第一章那种反复检查的焦虑」**（或去掉引号，写成「承第一章那种停不下来的焦虑」）。

---

## 四、交叉说明

1. **人物与称呼链（决定 W1–W7 的归属判定）**
   - `text/ch02:129`：`Only her older sister, Diana, insisted she go to a specialist…` ⇒ Diana 是**姐姐**、Alba 是妹妹（与 `ch01`/`ch05` 的称呼链一致）。
   - `text/ch02:48`：`her youngest daughter’s apartment`＋`her son-in-law to come out and open the metal door`＋`Juan didn’t always accurately guess…` ⇒ Juan 是 **Alba 的丈夫、Carmen 的女婿**；`:48`「the face of a seventy-five-year-old woman」＝**Carmen 75 岁**。
   - `text/ch02:117`：`grandmother, mother, two children, seven and nine, and a baby in a stroller, less than a year old` ⇒ Alba 名下**三个孩子**（`md:11`「Alba 和她三个孩子」✓成立）。
   - `text/ch02:126`：`That day’s mission was to exchange a couple of Switch controllers for **her eldest**.` ⇒ 手柄是给**长子**的（`md:99` 只说尺子，未涉及手柄归属；`00_概述.md` 与 `ch16` 的「我想要的不过是那两只手柄」指同一对象）。
   - `text/ch02:477`：`That same afternoon, while **her cousin** was at gymnastics, Brisa was sleeping in her room.` ⇒ **Brigitte（Alba 的女儿）是 Brisa（Diana 的女儿）的表姐**；`:468`「the girls’ noses had both bled」指这两个女孩。
   - `text/ch02:480`：`She grabbed Tomás’s backpack, rooted around in it for a ruler`＋`Tomás’s plastic ruler` ⇒ Tomás 是 Brisa 的哥哥（Diana 的儿子）。
   - `text/ch02:342`：`Alba simply called them “the widows,”`＋`They looked to be around seventy` ⇒ 「the widows」＝商场里那对约七十岁的老妇；`:48` 的 75 岁是 **Carmen**，两人不可混。
   - `text/ch02:483`：`pediatricians, gymnastics coaches, Carmen, Carlos, or Juan` ⇒ 本章里 Carlos 是 **Diana 的伴侣**（`text/ch01:15`「She called Carlos」；`ch10 chapter 10.md:39`「Juan 又招手让 Diana 和 Carlos 走近看车」），Juan 是 Alba 的丈夫 ⇒ 五个解释来源分属两位母亲与她们的家人（见 W3）。

2. **时间轴链（决定 W6 与 §4 的两条「已核实为正确」）**
   - `text/ch02:36`「on a Wednesday at seven a.m.」＋`:132`「only three days until Christmas」＋`:165`「Tomorrow is my birthday.」＋`:171`「The next day. Christmas Eve?」⇒ 本章＝**12 月 22 日（周三）**，Alba 生日 12/23，平安夜 12/24。
   - `text/ch02:468`「About a month ago, the girls’ noses had both bled dramatically, in different places and situations but at the same time.」⇒ **两场鼻血在一个月前的同一个时刻**（原文只给 "at the same time"／"at the exact same time"，**没给分钟**；`00_情感节点.md:30` 的「同一分钟」是总览自己的措辞，不属本章 md）。
   - `text/ch02:477`「**That same afternoon**, while her cousin was at gymnastics, Brisa was sleeping in her room.」⇒ 「that same afternoon」指的是 `:468-474` 那个**一个月前**的下午（Brigitte 在平衡木上那次），**Brisa 的出血也发生在那一天** ⇒ 本章结尾整段（`:468-483`）都在回叙里。
   - 结论：`md:11`「本章最后把时间拨回一个月前——两个女孩在同一时刻流鼻血」与 `md:15`「结尾突然把时间拨回一个月前，用两个女儿的血和一句「在同一个时刻」收束」**成立**（见 §4）。

3. **「失焦」与「水母」两条线（决定 W2 与 F1）**
   - `text/ch02:249`「all she could see was the shirt collar of the associate」＝**唯一一次**收缩（`/usr/bin/grep -c "shed all objects and life" text/ch02_chapter_2.txt` → 1）；`text/ch02:252`「the trances that swallowed her for minutes on end」是母亲对同一现象的描述。
   - `text/ch02:120`「a many-tentacled jellyfish」＝叙述者对「祖母＝母亲延伸」的比喻；`text/ch02:219`「Carmen turned for a second and saw a swarm of jellyfish on the screen at her back」＝**电视屏幕上的画面**。
   - 结论：旧句「本章后面还会出现一次类似的失焦，那时她怀里抱的是孩子」把 `:219` 读成了第二次失焦 ⇒ 已改（`041dfc930`）；但新句的「后面／再次」仍断言存在第二次 ⇒ W2；而 `md:51`「记住水母这个比喻，本章后段它还会以另一种方式再出现一次」**成立**（`:219` 的水母正是「另一种方式」，见 §4）。

4. **「五个词」的两处出处（决定 W1）**
   - 本章末句 `text/ch02:483`「They could find no solace.」＝**五个词**（Python 实测，区间 `[41930,41956)`）。
   - 第 16 章末句 `text/ch16:66`「I just wanted the controllers.」＝**五个词**；`00_概述.md:46`、`00_金句精选.md:298`、`ch16 chapter 16.md:105` 的「五个词」指的是这一句。
   - 两处是两句话，**互不冲突**；本章原先的「五个词」本来正确，改成「四个词」才是错。

5. **机器层两条红线的性质（决定 §4 的两条假红）**
   - `keyword_long` 8 条（每块 1 条关键词超长，词数 14/21/16/18/19/10/23/19）：`scripts/bookform.py:443` 按空格切词计数；`:488` 的 blocked 判定**不含 keyword_long** ⇒ 只作提示。与兄弟章同体例（第 3 章 7 条、第 11 章 8 条、第 14/15 章各 7 条、第 16 章 5 条；第 1 章复核同样 8 条）⇒ **假红**。
   - `block_count` 提示「块数 8 偏离本章篇幅建议 13–15（本章 7372 词）」：本书兄弟章块数为 6–8（中位 7），8 块是众数之一；`docs/rules/genre-profiles.json` 的 novels profile 给的是 `blocks [3,10]` ⇒ **假红**。
   - 取证命令与退出码见 `review/ch02/4-verdict.md` §2 的 A11、A12。

---

## 五、修后复核（改稿后按此复核）

1. **W1**：`md:109` 的「四个词」→「五个词」。
   - `/usr/bin/grep -n "四个词" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch02 chapter 2.md"` → 期望 exit=1。
   - 复核词数（Python）：`len("They could find no solace.".split()) == 5` → 期望 True。
2. **W2**：`md:75` 去掉「本章后面」与「再次」，并把场景点明为**同一段**。
   - `/usr/bin/grep -n "再次收缩" "…/ch02 chapter 2.md"` → 期望 exit=1。
   - `/usr/bin/grep -c "shed all objects and life" "…/text/ch02_chapter_2.txt"` → 期望输出 `1`、退出码 0（本章收缩仅一次）。
3. **W3**：`md:109`「三个解释来源」→「五类解释来源（两位儿科医生、两位体操教练，外加 Carmen、Carlos、Juan）」。
   - `/usr/bin/grep -n "三个解释来源" "…/ch02 chapter 2.md"` → 期望 exit=1。
4. **W4**：`md:61`「接着他抽出其中一条」→「接着从清单里挑出其中一条」。
   - `/usr/bin/grep -n "接着他抽出" "…/ch02 chapter 2.md"` → 期望 exit=1。
5. **W5**：`md:109`「最后一句」→「引语里的最后一句」。
   - `/usr/bin/grep -n "本章还有最后一句" "…/ch02 chapter 2.md"` → 期望 exit=0（这一句属 `md:111`，**保留**）。
6. **W6**：`md:12`「恐惧线则借血正式登场」→「恐惧线则开始渗血」一类写法。
   - `/usr/bin/grep -n "正式登场" "…/ch02 chapter 2.md"` → 期望 exit=1。
7. **W7**：`md:12`「承第一章那种「非做不可」的焦虑」→「承第一章那种反复检查的焦虑」。
   - `/usr/bin/grep -n "非做不可" "…/ch02 chapter 2.md"` → 期望 exit=1。
8. **L1–L7** 建议落点：`md:11`（L1、L2、L3）、块 3 中文理解（L2）、块 1 中文理解（L3）、块 4 中文理解（L4）、块 7／块 8 中文理解（L5、L6）、块 5／块 6 中文理解（L7）。
   - 复核：`/usr/bin/grep -nE "Esplugues|小公社|皮肤科|守夜|平衡木|录像|跨两遍" "…/ch02 chapter 2.md"` → 期望 exit=0（以上七处均已出现）。
9. **机器层回归**：`bash scripts/chapter.sh "…/ch02 chapter 2.md" --json` → 期望退出码 0、`verdict: ok`；`issues.keyword_long` 与 `block_count` 两条**允许继续存在**（假红，见 §四 第 5 条），其余 `issues` 组仍须为空。
   - 复核输出请落在 `/tmp` 下，**不要覆盖仓库内 `review/ch02/2-machine.json`**。
10. 本单只出指令，**未改动任何 md 文件**；`git` 未执行任何操作（未 add / 未 commit / 未 push）。
