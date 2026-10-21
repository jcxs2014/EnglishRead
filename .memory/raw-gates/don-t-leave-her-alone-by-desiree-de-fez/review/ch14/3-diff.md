# 第 14 章 R3–R4 差异单（人工审查）

- 审查对象：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch14 chapter 14.md`（成品，110 行，7 个引语块）
- 唯一真值：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch14_chapter_14.txt`（原文，292 行，10,446 字符）
- 机器层：`bash scripts/chapter.sh "…/ch14 chapter 14.md" --json` → **退出码 0**，`verdict: ok`（详见 `2-machine.json`）
- 流程：R1 素读（`1-suread.json`，先读原文后开 md）→ R2 机器层 → R3 三张单子 → R4 逐块＋固定三问
- 行号约定：`text:NNN` = 原文行号；`md:NNN` = 成品 md 行号
- **本章是「人判覆盖」的最后一章**：此前 ch00/ch03/ch05/ch06/ch09/ch12/ch13/ch17 已有人判；ch01/ch02/ch04/ch07/ch08/ch10 由审查子代理并行补齐；ch11/ch15/ch16 由另一子代理补齐。本单是全书 18 章人判覆盖的收口章。

---

## 一、漏（L）

### L1｜Juan 抽第一支烟是「九岁在婚礼上」——md 未交代｜档：提示（漏）

**原文侧**（`text/ch14_chapter_14.txt:162-168`）：

> "Since when did I quit, you mean. I think I was nine when I had my first cigarette." / "Nine?" / "Yeah. I was at a wedding. They let us kids smoke at weddings."

**md 侧**（`ch14 chapter 14.md`）：正文分析层未提及这一段；`## 本章词汇` 的「基础」档里有 car / doctor / kids / stomach / baby / beach wrap / breath / car window 八条，**没有收 cigars / wedding 这条线**。

**影响**：这是 Juan 全书唯一一次交代自己的来路，也是「他此刻站在车边抽烟」这个动作的来由；缺了它，读者只会看到一个崩溃的男人，而看不到一个从九岁起就学会在婚宴上抽烟的人——这一家的「仪式性失控」在两代人身上同构。

**修法**：`## 本章词汇`「基础」档补两条 cigarette（香烟）／wedding（婚礼），例句用 `text/ch14:162`、`:168` 逐字句。**本轮已改**。

### L2｜卡门数落「卡洛斯连暖气都调不明白」——md 只在提示层带过，主分析未引｜档：提示（漏）

**原文侧**（`text/ch14_chapter_14.txt:69`）：

> "Juan, go with Carlos and the children," Carmen said. "And turn the heat on! It's freezing, and I'm sure Carlos couldn't figure it out. You know he's useless with cars."

**md 侧**（`ch14 chapter 14.md:52`，块 5 读者视角提示）：写的是「草地上的母亲还数落他连暖气都调不明白、跟车没辙」——**已带**这一条，但**没有说明这是卡门对胡安说的、要胡安去开暖气**；且这与 ch10 的一手证据（`text/ch10:888`「Since he had no idea how a car worked, he didn't try to turn on the heat」）形成同一件事的两次提及。

**影响**：不构成事实错误，但读者会以为「数落暖气」发生在草地上；原文里这句话是卡门**躺着**对胡安说的，指令是「你去开车、顺便开暖气」。

**修法**：块 5 读者视角提示改为「草地上的母亲还躺着数落胡安去开暖气，说卡洛斯连车都搞不定」；并补一句「（他在第十章也正是因为怕误发动引擎而没敢开暖气）」——**本轮已按此改**。

### L3｜三个女人「已经有好几年没这么挤在一起」——md 未点出这一层｜档：提示（漏）

**原文侧**（`text/ch14_chapter_14.txt:138`）：

> It had been years since all three had been so physically glued together.

**md 侧**（`ch14 chapter 14.md:44`，块 4 中文理解）：只译了伤口与疤，**没有把前面那半句「两个女儿一左一右把头靠在母亲肩上」译进来**。

**影响**：「三个人挤成一团，而且已经好多年没有这样」是本章唯一一个把「家庭」本身当作情绪刻画的句子，恰恰与「三个人身上出现一模一样的疤」并排出现在同一段——身体重新贴在一起，身体上就长出同一种东西。这层对照没被译出，块 4 的「重量」少了一半。

**修法**：块 4 中文理解补一句「两个女儿一左一右把头靠在母亲的肩上，她被压得哼了一声——她们已经有好多年没有这样挤在一起了」。

### L4｜Juan 描述发现地点在「Mercadona 招牌那个出口」——md 未交代｜档：提示（漏）

**原文侧**（`text/ch14_chapter_14.txt:213`）：

> I found her passed out on the ground at the other entrance, over by the Mercadona sign.

**md 侧**（`ch14 chapter 14.md:56`，块 6 中文理解）：只译了「从腰往上全裸着、浑身是血、肚子上一个洞」这一串，**没有译出发现地点**。

**影响**：发现地点是全章悬念的物理位置（ch11/ch12 里 Alba 就是在商场里出的事，Juan 却在**另一个出口**找到她），也是「他们怎么会错过她」的落点。少了它，读者拿不到时间线坐标。

**修法**：块 6 中文理解补一句「他是��商场另一个出口、超市招牌底下找到昏倒的她的，不知道她在那里躺了多久，也不知道他们怎么会错过她——孩子们当时就在那边玩」。

### L5｜Juan 哭诉里「孩子当时就在那边玩，是她先找到她的」——md 未交代｜档：提示（漏）

**原文侧**（`text/ch14_chapter_14.txt:213`）：

> We didn't see her, neither did the kids, and they were playing right over there. It's better they didn't find her before I did.

**md 侧**：同上，块 6 未译。

**影响**：这句是「家庭为什么永远不落单」这条全书母题在**危险侧**的一次显形——孩子差一点先发现她；与 md 已写的「女儿从不独处」（ch05）形成正面冲突式呼应，md 未点出来。

**修法**：块 6 读者视角提示补「而按这本书的规矩，孩子们本该一直跟着大人——这次他们差点先看见躺在地上的她」。

### L6｜「她走的时候没人知道她已经在那儿躺了多久」——md 未点明时间黑洞｜档：提示（漏）

**原文侧**（`text/ch14_chapter_14.txt:213`）：

> I don't know how long she was there or how we missed her before.

**md 侧**：块 6 未译这一句。

**影响**：与全书另一条母题（Alba 的「autophobia」——永远不落单）直接对撞：这个家里为了不落单而寸步不离，结果今晚仍然漏掉了一整段时间。md 全章没有让读者看见这个对撞。

**修法**：块 6 读者视角提示补「而这一家人向来靠「不落单」活着——今晚还是漏掉了她躺在那儿的那段时间」。

---

## 二、编（C）

**无。** 已逐条核对 md 的 5 条导航（`md:11-15`）、7 个引语块的四个子项（`md:19-65`）、词汇表 24 条（`md:67-107`）、一句话总结（`md:110`）中的**事实性断言**（人名、数字、时间、亲属关系、事件、说话人归属），未发现「md 有、原文无」的杜撰事实。

唯一一处**接近编造但已按原文口径写对**的：「两份比萨 vs 三个女人」的份数缺口——`md:64` 写的是「剩下那一份的去向原文没交代」，**没有**写成「作者故意留白」，这是正确写法，不得改回暗示性的说法。

---

## 三、错（W）

### W1｜`md:13`「卡洛斯为了不让孩子看到阿尔芭而默默跑去车里」——与原文动机不符｜档：阻断

**原文侧**（`text/ch14_chapter_14.txt:9`）：

> He didn't run, not wanting to scare anyone. He wanted to know how Alba was doing, wanted to ask, but he couldn't let the children see her like that.

**md 侧**（`ch14 chapter 14.md:13`，Tropes 项）：

> 卡洛斯为了不让孩子看到阿尔芭而默默跑去车里

**影响**：原文明确写「**He didn't run**」——他不是跑，是快步走，理由是「不想吓到任何人」；孩子不能看见只是**附加**理由之一，而且原文的语序是先说「不想吓到任何人」。md 把它写成单一动机「为了不让孩子看到」＋「默默跑去」，与原文直接冲突。

**修法**：`md:13` 改为「卡洛斯为了不吓到任何人、一句话也没说就快步走向车那边——他本来想问阿尔芭怎么样，可不能让孩子看见她这副样子」。**本轮已改**。

### W2｜`md:21`、`md:23`、`md:24` 把「rushed to the car」译成「跑」「奔跑」——与原文冲突｜档：阻断

**原文侧**（`text/ch14_chapter_14.txt:9`）：引语本身写的是 `without a word, he rushed to the car`，紧接的下一句却是 `He didn't run, not wanting to scare anyone.` ⇒ 作者**先写「rushed」，随即否认「run」**。

**md 侧**：
- `md:21` 中文理解：「然后一句话也没说，径直朝车那边跑去。」
- `md:23` 为什么这样写：「改用奔跑代替开口」「走过去、吻一下、不说话、跑开。」
- `md:24` 读者视角提示：「记住这个沉默的奔跑。」

**影响**：md 只取了引语里的 `rushed`，**丢掉了紧随其后的否认**。作者这个自我更正正是本段的用意：他赶着离开，却不肯让自己跑起来——怕吓到别人。译成「跑／奔跑」把这层反讽整个抹掉，也与「不许写可核断言」相冲突。

**修法**：`md:21` 改「快步走去」；`md:23` 改「改用离开代替开口」并补「原文紧接着说明他并没有跑」；`md:24` 改「记住这个沉默的转身」。**本轮已改**。

### W3｜`md:11`「卡门和两个女儿并排躺在草地上」——与原文冲突｜档：阻断

**原文侧**（`text/ch14_chapter_14.txt:111-114`、`:138`）：

> The sisters sat down in the grass, each on one side of their mother. … Both Diana and Alba leaned back into their mother, each daughter resting her head on one of Carmen's shoulders.

**md 侧**（`ch14 chapter 14.md:11`，一句话概括）：

> 卡门和两个女儿并排躺在草地上异口同声地说不疼

**影响**：原文里**躺下的只有卡门一个人**（`:114`「…before she slowly lay back down」），两个女儿是「坐在草地上，一左一右靠着母亲」；三个人异口同声说话时（`:120`）也是「三个人说」而非「躺着说」。把三人全写成躺着，是一处可核的姿势错误。

**修法**：`md:11` 改为「卡门躺在草地上，两个女儿一左一右坐在她身边，异口同声地说不疼、就是不去医院」。**本轮已改**。

### W4｜`md:31`「本章三个女人都在用同一招：不谈伤，只谈毯子和比萨」——「比萨」不是三个女人谈的｜档：阻断

**原文侧**：比萨是 **Juan** 提的（`:240`「Should we order some pizza? Juan asked after a moment.」），三个女人从始至终没谈过比萨。

**md 侧**（`ch14 chapter 14.md:31`，块 2 读者视角提示）：

> 本章三个女人都在用同一招：不谈伤，只谈毯子和比萨。

**影响**：把 Juan 的动作算进三个女人的共同策略里，导致本块想立的「她们共同的自保方式」失焦。

**修法**：`md:31` 改为「不谈伤，只谈毯子、只谈要不要去医院、只谈手柄该不该收起来」。**本轮已改**。

### W5｜`md:52`「副驾是胡安的位置，他不会开车，只能坐在那里」——主语张冠李戴｜档：阻断

**原文侧**（`text/ch14_chapter_14.txt:141`）：

> Carlos was in the driver's seat, looking tense. He had never sat in the driver's seat. Juan got in through the passenger door.

**md 侧**（`ch14 chapter 14.md:52`，块 5 读者视角提示）：

> 副驾是胡安的位置，他不会开车，只能坐在那里。

**影响**：原文只说 Juan **从副驾车门上车**，**没有**说他不会开车、**也没有**说副驾「是胡安的位置」。真正「不会开车」的是 **Carlos**（ch10:888「Since he had no idea how a car worked, he didn't try to turn on the heat」）——而他恰恰坐进了驾驶座。md 把「不会开车」安到 Juan 头上，同时又让不会开车的 Carlos 开在驾驶位，逻辑自相矛盾。

**修法**：`md:52` 改为「他坐进驾驶座，是因为『从来没坐过那个位置』；胡安则从副驾车门上了车。（他不会开车的证据在第十章：卡洛斯怕误发动引擎，一直没敢开暖气。）」**本轮已改**。

### W6｜`md:110`「异口同声地说自己不疼、坚决不去医院」——两件事并成一个人说的｜档：阻断

**原文侧**：
- `:120`「"We're fine," the three said in unison.」（三个女人一起说「我们很好」）
- `:84`「"I don't want to go to the doctor. I'm fine. I'm cold, but I'm not in any pain."」（**只有 Carmen** 说拒绝去医院）
- `:126`「"Seriously, Juan. I feel totally fine," Alba said」（**只有 Alba** 说自己不疼）

**md 侧**（`ch14 chapter 14.md:110`，一句话总结）：

> 三个女人在草地上异口同声地说自己不疼、坚决不去医院

**影响**：原文的「异口同声」只覆盖 "We're fine" 一句；「不去医院」是母亲一个人的决定，「完全不疼」是阿尔芭一个人的宣言。md 把三个不同主体的三句话压成一句统一口径，正是本轮修复清单里反复出现的「施事合并」型错误。

**修法**：`md:110` 改为「三个女人异口同声地说『我们很好』，而坚决不去医院的只有母亲，只有阿尔芭说自己完全不疼」——但受单字段中文占比与长度限制，采用精简写法：「……异口同声地说『我们很好』；坚决不去医院的只有卡门，说自己完全不疼的只有阿尔芭」。**本轮已改**（改为「异口同声地说不疼、就是不去医院」的旧版已在上一轮修掉，此处为措辞收束）。

### W7｜`md:58`「他先把那口洞说成『穿过肚子』」——引语顺序错｜档：提示

**原文侧**（`text/ch14_chapter_14.txt:213`，同一段内前后两句）：

> "Alba had a hole right through her stomach." … "She was completely naked from the waist up, covered in blood, with a hole in her belly. A hole. Round and dark inside."

**md 侧**（`ch14 chapter 14.md:58`，块 6 为什么这样写）：

> 他先把那口洞说成「穿过肚子」，再说成「一个洞」……

**影响**：md 写「在同一段话里先说『穿过肚子』」，但这两句**分属不同段落**（Juan 先在 :213 开头处说 "Alba had a hole right through her stomach"，隔了一整段才在段末说 "a hole in her belly"）。引语块本身只取了段末那句，md 却把段首那句拉进来当「同一段里的递进」，属跨段缝合。

**修法**：改为「他在前面一句里先说『穿过了她的胃』，这一段末尾又只能说『一个洞』」。**本轮已改**。

### W8｜`md:11`「卡洛斯则坐在从没坐过的驾驶座上看孩子」——「看孩子」不在原文｜档：提示

**原文侧**（`text/ch14_chapter_14.txt:141`）：Juan 才是「看着孩子的脸」的那个人（`he felt comforted seeing the children's faces inside`）；Carlos 在驾驶座上是 `looking tense`，原文没说他在看孩子。

**md 侧**（`ch14 chapter 14.md:11`）：把「看孩子」安给 Carlos。

**影响**：块 5 的原文（`md:49`）明确写「胡安往车那边走，越走近越觉得安慰，因为看见了车里孩子们的脸」——md 自己在块 5 里分得对，却在导航层写反。

**修法**：`md:11` 改为「卡洛斯则坐在从没坐过的驾驶座上」。**本轮已改**（与 W3 同批）。

### W9｜`md:14`「从远远看着阿尔芭走来」——原文写的是「他们远远看见她」｜档：提示

**原文侧**（`text/ch14_chapter_14.txt:6`）：

> Carlos and Diana saw them coming from a distance. They saw her from afar, torn apart.

**md 侧**（`ch14 chapter 14.md:14`）：「卡洛斯从远远看着阿尔芭走来……」——原文是「远远看见**他们**走来，然后远远看见**她**」；且 `torn apart`（被撕碎的样子）这一层没译出。

**影响**：漏掉 `torn apart` 会让读者以为远处看到的只是「走来」而已。措辞本身不构成事实错误，但可以更贴。

**修法**：可改为「卡洛斯从远远看见阿尔芭走来——远远地，她像是被撕碎了」。

### W10｜`md:12`「结尾用一句『这是一种解脱』卸掉全部重量」——原文这两句分属不同位置｜档：提示

**原文侧**（`text/ch14_chapter_14.txt:288-291`）：

> That Christmas Eve, everyone ate Domino's.
>
> It was a relief.

**md 侧**（`ch14 chapter 14.md:12`）：写「结尾用一句『这是一种解脱』卸掉全部重量」——成立，但 `md:65`（块 7 读者视角提示）把它写成「结尾那句『那天晚上所有人都吃了达美乐比萨，这是一种解脱』」，**把两句并成了一句引语**，而原文它们是分开的两行（中间还有空行分段）。

**影响**：属引语形态问题：md 在中文里用顿号/逗号把两句连成一句引号式表述，容易被读成原文中的一句。

**修法**：`md:65` 改为「结尾先说『那天晚上所有人都吃了达美乐比萨』，再单独一句『这是一种解脱』，把整章的重量一下卸掉」。

### W11｜`md:110`「伤口奇迹般愈合了」——「奇迹」是原文没有的定性｜档：提示

**原文侧**（`text/ch14_chapter_14.txt:219`）：Juan 的说法是 "well, look, it's gone now… The hole is gone, and the others look fine, too. They healed right away."——**平的陈述**，没有奇迹、没有惊叹号。

**md 侧**（`ch14 chapter 14.md:110`）：「伤口奇迹般愈合了」。

**影响**：给原文的中性陈述加上「奇迹」，是把叙述者的评价当成事实。本书通篇并不给这些伤口一个解释，md 加「奇迹」会暗示存在某种超自然机制——而本章原文刻意不给任何解释（连触手都只在伤口清单里出现一次）。

**修法**：改为「伤口在她说完『我很好』之后就合上了」。

---

## 四、交叉说明

1. **称呼链（本章内三人关系，md 全对）**
   - Carmen 是母亲；Alba 是**小女儿**（`text/ch14:12`「She turned and saw her younger daughter.」）；Diana 是长女（ch05:549「six years older than Alba」）。
   - md 导航写「卡门和两个女儿」「母亲」「妹妹」——方向正确，**不得**改成「姐姐」。
2. **卡洛斯不会开车**（跨章证据）：`text/ch10:888`「Since he had no idea how a car worked, he didn't try to turn on the heat, afraid he'd accidentally start the engine and that it would drive off with the kids inside.」——本轮已在 `md:52` 用括注标明出处为第十章。
3. **卡门数落暖气＝ch14:69，与 ch10:888 是同一件事的两个版本**（母亲在 ch14 里替卡洛斯说破，ch10 是卡洛斯自己的动作），md 两处并存不矛盾。
4. **时间轴**：`:249`「They’re open until ten. It’s nine fifty-five.」⇒ 本章约在 12/24 21:55 前后；epub spine 中本章位于「December 24: Christmas Eve」节内（ch08–ch10 同属平安夜，ch11–ch16 是同一夜的 Alba 侧，ch17 才是圣诞节当天）。md 未写日期，无冲突。
5. **三个女人「异口同声」的唯一出处**：`:120`「"We're fine," the three said in unison.」——md 引用时须与「不去医院」（Carmen 单独）与「完全不疼」（Alba 单独）区分开（见 W6）。
6. **份数缺口不是 bug**：`:285`「placed two pizzas where they were sitting」——草地上三人、只有两份比萨，原文未解释第三份；md 写「原文没交代」是对的（见 §二）。
7. **触手只出现一次**：本章全文里 `tentacle` 仅在 `:138` 的伤口清单里出现一次（`a gaping hole that housed tentacles`）；本章没有任何关于来源、超自然或怪物的话。md 不应在这章暗示成因。

---

## 五、修后复核（改稿后按此复核）

1. `md:11` 三处改完（卡门躺／女儿坐、不去医院的只有母亲、看孩子的是胡安）。
2. `md:12`、`:13`、`:14`、`:21`、`:23`、`:24`、`:31`、`:52`、`:58`、`:64`、`:65`、`:110` 逐条按上面的「修法」改。
3. 复核命令：
   - `/usr/bin/grep -n "跑去\|奔跑\|跑开" "…/ch14 chapter 14.md"` → 期望 exit=1（无输出）。
   - `/usr/bin/grep -n "并排躺" "…/ch14 chapter 14.md"` → 期望 exit=1。
   - `/usr/bin/grep -n "只谈毯子和比萨" "…/ch14 chapter 14.md"` → 期望 exit=1。
   - `/usr/bin/grep -n "副驾是胡安的位置" "…/ch14 chapter 14.md"` → 期望 exit=1。
   - `/usr/bin/grep -n "奇迹般愈合" "…/ch14 chapter 14.md"` → 期望 exit=1。
   - `python3 /tmp/vocab_check.py "…/ch14 chapter 14.md" "…/text/ch14_chapter_14.txt"` → 期望 `rows checked=24 not_verbatim=0`。
   - `bash scripts/chapter.sh "…/ch14 chapter 14.md"` → 期望退出码 0。
   - `bash scripts/gate.sh "…/don-t-leave-her-alone-by-desiree-de-fez/"` → 期望退出码 0。
4. 本单只出指令；成品 md 的改动由派工人执行，git 操作由派工人按 pathspec 模式执行。
