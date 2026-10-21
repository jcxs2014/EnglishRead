# 第 11 章 R3–R4 差异单（人工审查）

- 审查对象：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch11 chapter 11.md`（成品，154 行，8 个引语块）
- 唯一真值：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch11_chapter_11.txt`（原文，156 行，27,504 字符）
- 机器层：`review/ch11/2-machine.json` → `verdict: ok`（8/8 引语 `ok=true`；`counts` 全 0；`form`：`h1_shape_ok true`、`nav_count 5 ok`、`blocks 8`、`subitems_modal` 四件与 `profile: novels` 一致）
- 流程：R1 素读（`1-suread.json`，**先读原文、后开 md**）→ R2 机器层 → R3 三张单子 → R4 逐块＋固定三问
- 行号约定：`text/chNN:行号` = 原文行号；`md:行号` = 成品 md 行号
- **本单只出审查结论，不改成品 md**（本轮硬性要求：只写审查产物）⇒ 各条「修法」均为**建议稿**，标注「建议改」，未落笔到 md。
- 计数：**漏 L＝7（L1–L7）／编 C＝0／错 W＝10（W1–W10）**。其中 W 档位：阻断 3（W1–W3）、提示 7（W4–W10）。

---

## 一、漏（L）

### L1｜「取回手柄的念头压过了再次见到女孩的恐惧」与「想活着离开 Splau」——md 未写｜档：提示（漏）

**原文侧**（`text/ch11_chapter_11.txt:99`）：

> Then she remembered the Switch controllers that had been sitting atop the red swimsuit and walked toward the bathroom exit. The need to retrieve them overpowered her fear of seeing the girl again, and she imagined she hadn't gone far. Alba also wanted to leave Splau. She wanted to leave Splau alive.

**md 侧**：`ch11 chapter 11.md` 全文未出现「取回手柄压过恐惧」「想活着离开」这一层。md:87 只写了「她盯着看了整整五分钟」，md:14 写了「第一件惦记的却是把手柄」，但**没有把「手柄战胜恐惧」写成她起身离开隔间的动因**。

**影响**：这是 Alba 走出隔间的**唯一直接动机**，也是全章最锋利的一处反讽——一个被剖开肚子的人，最想做的事是拿回两个手柄。md 把它降级成「执拗」的性格描写，读者拿不到「恐惧被一件小事压过去」这个交换。

**修法（建议改）**：在块 6（`md:87` 读者视角提示）补一句：「她盯着看了整整五分钟；然后是手柄战胜了恐惧——想起手柄还压在红泳衣上，她起身朝出口走，因为想拿回手柄的念头压过了再见那个女孩的恐惧。她还想活着离开 Splau。」

### L2｜童年捉迷藏「捂住眼睛就等于消失」与 Diana 掐她一下——md 未写｜档：提示（漏）

**原文侧**（`text/ch11_chapter_11.txt:84`）：

> It wasn't unlike what she did as a child when she and her sister played hide-and-seek. … She thought she had disappeared—until Diana pinched her leg. … There in the Splau bathroom, before she fainted from the pain, Alba longed for Diana to sit down and give her a pinch.

**md 侧**：md 全文未出现这段。这是 **Diana 在本章唯一一次出现**（`text/ch11:12` 的共用手机是另一次），md 一处也没提。

**影响**：这条同时是本章「家庭联结」的唯一实据，也是纠正 W2 的关键：原文里 Alba 与 Diana 的联结是**童年的把戏与那一下掐**，跟手柄毫无关系。md 把它漏掉，才会在 `md:14` 上把「手柄执拗」错挂到 Diana 名下（见 W2）。

**修法（建议改）**：在块 5（`md:75` 读者视角提示）后或块 6 读者视角提示里补：「本章 Diana 只出现两次：一次是她们共用手机的旧账，一次是童年捉迷藏——Alba 一直以为捂住眼睛就能消失，直到姐姐 Diana 掐她一下；这一次她痛到快晕过去前，盼的正是 Diana 来掐她一下。」

### L3｜四个关键数字：触手约每五分钟绞一次、她熬过三次分娩的痛、她为手柄着迷了两个星期、她数到三十｜档：提示（漏）

**原文侧**（`text/ch11_chapter_11.txt:99`）：

> She counted to thirty in her head, held her breath … She made it through a third attack and calculated the tentacles were wringing her out about every five minutes. The sequence was causing the worst physical pain she had experienced in her life. Worse than the pain her body had used to prepare itself for each of her three childbirths. … That had been true for the past two weeks, although no one had understood why.

**md 侧**：`md:87` 只取用了「五分钟」（盯了整整五分钟），**另外三层数字全缺**：每五分钟的绞痛周期、比三次分娩更痛、两个星期的着迷期。

**影响**：这四个数字是本章唯一把「Alba 当母亲」和「Alba 当身体」两条线焊在一起的地方（`each of her three childbirths` 是全书唯一一次写明她生过三个孩子）；`past two weeks` 又是 ch12 回忆营地时的锚点。md 只留一个孤立的「五分钟」，读者拿不到时间的量级。

**修法（建议改）**：在块 6（`md:79-87`）中文理解或读者视角提示里补齐：「她数到三十才熬过一阵；算出来触手大约每五分钟绞她一次，这一轮疼过她这辈子最疼的比分娩三次还要狠；只有手柄那点疯劲持续了两个星期，没人说得清为什么。」

### L4｜Claire's 是「她和女儿最爱的店」，Brigitte 还没发现美甲片——md 未写｜档：提示（漏）

**原文侧**（`text/ch11_chapter_11.txt:126`、`:129`）：

> The store with the lights on was, in fact, Claire's, where they sold cheap costume jewelry, trinkets, and accessories, mostly for kids and teenagers. … She felt exhausted at the sight of an empty Claire's—the very store she delighted in with her daughter, where they could easily spend an hour and often bought armfuls of jewelry whose value plummeted the moment they got home. … it was the press-on nails display. … Brigitte had yet to discover them.

**md 侧**：md:103 的引语里出现过 "Claire's"（逐字，属引语部分），但 `md:105` 中文理解只写「那面友好的饰品店橱窗」，**没有交代这是母女最爱的店，也没有 Brigitte／美甲片**。

**影响**：原文用「母女的快乐之地」来铺这家店，再让血泼在它的橱窗上——反差全靠这层日常性。md 少了这层，「友好的 Claire's」只剩一个专有名词；Brigitte 又是本章唯一出现的 Alba 子女（`:129`），漏掉她等于少了一个家庭线锚点。

**修法（建议改）**：在块 8（`md:105` 中文理解）补一句：「亮灯的店是 Claire's，卖便宜时装首饰的——她和她女儿最爱的那家，母女俩常常一逛一小时；连压纹美甲片那一排，她女儿 Brigitte 都还没发现过。」

### L5｜Bijou Brigitte 招牌没亮＝不祥；Caga Tió 的王冠要带给 Brigitte 和 Brisa——md 未写｜档：提示（漏）

**原文侧**（`text/ch11_chapter_11.txt:105`）：

> She got up and saw she was next to a jewelry store: Bijou Brigitte. She thought it was a bad omen that the sign with her daughter's name on it wasn't lit. … The same one where, just shortly before, she'd been searching for crowns for their Caga Tió, to bring to Brigitte and Brisa.

**md 侧**：md 全文**没有出现** "Bijou"、"Caga"、Brisa、Brigitte 任何一个名字。

**影响**：这是全章唯一的**家庭内部坐标**：Bijou Brigitte ＝ Alba 母亲（原文自己的店，招牌＝ 女儿的名字）、Caga Tió ＝ 家庭传统、王冠要带给 Brigitte（Alba 的女儿）和 Brisa（Diana 的女儿）。漏掉它，读者既不知道 Alba 是母亲也不知道 Diana 那边有一个 Brisa，等于把本章的「一家人各自在圣诞夜」这层网抽掉了——也正因如此，`md:12` 才容易把「母亲」写混（见 W1）。

**修法（建议改）**：在块 6 之后的读者视角提示里补：「她走过挂着自己女儿名字的 Bijou Brigitte 珠宝店，招牌没亮，她觉得不祥；不久前她还在这条通道上替一家的 Caga Tió 找王冠，要带去给 Brigitte 和 Brisa——Alba 的女儿与 Diana 的女儿各一个。」

### L6｜商场是 Splau；平安夜商场没照常收尾，清洁工圣诞节后一早才来——md 未写｜档：提示（漏）

**原文侧**（`text/ch11_chapter_11.txt:87`）：

> Since it was Christmas Eve, the mall had closed without the usual routines. Everything was left precisely as it was—the cleaning staff would come in first thing after Christmas.

**md 侧**：`md:11` 只写了「平安夜的商场」，**没有点出 Splau**；商场「一切原样保留、清洁工节后才来」这层未写。

**影响**：Splau 是 ch09–ch13 的同一地点（ch10:6「the area around Splau, which was now closed」），md 不点地名，读者无法把这一章钉在平安夜的 Splau 时间轴上；「商场没有照常收尾」则是这一夜一切异常的**公共条件**（扶梯还在转、灯还亮着、店还开着），是 `:102`–`:129` 那段的因。

**修法（建议改）**：在 `md:11` 一句话概括里把「商场」写成「Splau 商场」，并在块 6 读者视角提示补：「因为是平安夜，商场没照常收尾，一切原样摆着，清洁工要圣诞节后一早才来——所以灯还亮着、扶梯还在转。」

### L7｜镜中显老、哭又笑、要找皮肤科并向 Diana 要医生电话——md 未写｜档：提示（漏）

**原文侧**（`text/ch11_chapter_11.txt:90`、`:93`）：

> She looked like a large, Alba-sized stain. … She saw her eyelids were raw and thought she could no longer put off the dermatologist. She'd have to text Diana for her doctor's number. … She started to sob, brought her hands to her eyes, and pressed firmly down.

**md 侧**：md 未出现「显老」「哭」「皮肤科」「问 Diana 要医生电话」。

**影响**：这一段是 Alba 身上**母性**的最后一处具体动作：被切开的肚子上她还在想「得去看皮肤科」，而且是**向 Diana 要医生电话**（姐姐是演员，ch02:129 由 Diana 介绍过皮肤科医生）。它同时把「Diana 姐妹」这条线第二次落到实物上（补 L2 的缺口），也把「哭又笑」的荒诞补全。

**修法（建议改）**：在块 6 读者视角提示补：「她照镜子只看到一团自己的大小的污渍，哭了一场又笑了一场；她想自己这副眼睛大概拖不得了——还得发消息给 Diana 要皮肤科医生的号码。」

---

## 二、编（C）

**无。** 已逐条核对 md 的 5 条导航（`md:11-15`）、8 个引语块的四个子项（`md:19-111`）、词汇表 22 条（`md:113-151`）、一句话总结（`md:154`）中的**事实性断言**（人名、数字、时间、亲属关系、事件、说话人归属、店名、地名），未发现「md 有、原文无」的杜撰事实。

- 尤其确认三条最易编的点都写对了：红泳衣女孩**没有被写成女儿**（md 全篇只称「女孩／孩子」，与全书铁证「女孩＝ Alba 十二岁时的自己」不冲突）；`md:11`、`md:154` 的「把银耳环钉进耳朵」指向的是**女孩对 Alba 的行为**（方向正确，部位泛化见 W5）；`md:61`「泳衣和晒痕把她留在夏天」有原文支撑（`:60` 晒成古铜色、金发被日光和氯水漂白）。

---

## 三、错（W）

### W1｜`md:12`「前面都是母亲在怀疑、在害怕」——把 Diana 的视角安到母亲身上｜档：阻断

**原文侧**（`text/ch11_chapter_11.txt:12`，本章唯一一次提 Diana）：

> She thought about her sister, who'd never understood why they shared phones. "Phones are personal!" she would say.

（对照人物关系：`text/ch11:12` 的 "her sister" ＝ Diana；`text/ch05:549`「She, on the other hand—who was six years older than Alba—…」＝ Diana 是**姐姐**；`text/ch10:60`、`:138`、`:213` 里站在草地上的母亲是 **Carmen**。）

**md 侧**（`ch11 chapter 11.md:12`，情感弧线位置）：

> 全书最冷的一章，也是恐惧第一次由别人施加：前面都是**母亲**在怀疑、在害怕……

**影响**：ch05–ch10 的「怀疑与害怕」的主体是 **Diana（姐姐）**——ch06:6「Diana lived in terror of the possibility that something would happen to her children.」、ch09:6「One of Diana's back pockets started to vibrate.」、ch10 整章是 Diana 在 Splau 门口数人头、给母亲看伤口。**Carmen 在这一段是坐在草地上的旁观者，不是怀疑者**（ch10:138 Diana 明确说「her mother」）。md 把「前面」的主体换成了母亲，是一处可核的**归属错误**，而且它正落在导航层——全书读者据此会把 ch05–ch10 的恐惧线归错人。

**修法（建议改）**：`md:12` 改为「全书最冷的一章，也是恐惧第一次由别人施加：前面几章都是**姐姐 Diana**在怀疑、在害怕（Carmen 只是被她叫到草地上旁观），这一章里那个女孩把银耳环徒手钉进她的耳朵，而主角还在盯着自己肚子里那场舞蹈出神。」

### W2｜`md:14`「她身上最像 Diana 的地方也在这里露了头——……把手柄从地上捡起来、塞到门外」——归属方向错｜档：阻断

**原文侧**：
- Alba 与 Diana 的联结只有两条：`text/ch11:12`「She thought about her **sister**, who'd never understood why they shared phones.」（共用手机的妹妹）；`text/ch11:84`「She thought she had disappeared—until **Diana** pinched her leg.」（童年捉迷藏被姐姐掐一下）。
- 手柄那一段里**Diana 一次也没出现**（`text/ch11:9`）：「Instinctively, she grabbed the box and slid it under the stall door … she wanted to try to keep them from getting dirtier.」

**md 侧**（`ch11 chapter 11.md:14`，人物弧线）：

> Alba 从照顾别人的母亲变成被安排的人；她身上最像 **Diana** 的地方也在这里露了头——伤口还在流血，她第一件惦记的却是把手柄从地上捡起来、塞到门外……

**影响**：md 断言「手柄执拗＝像 Diana 的地方」，但原文里 Diana 与 Alba 的对应物是**共用手机**和**那一下掐**，跟手柄毫无关系；把手柄执拗挂到 Diana 名下，是本章归属方向错得最深的一处（读者会以为 Alba 之所以抓着手柄不放，是因为像姐姐——原文没有这层）。这处错也把 L2 的漏项坐实了：md 手里没有那条真正的童年联结，才会去另找替代品。

**修法（建议改）**：`md:14` 删掉「她身上最像 Diana 的地方也在这里露了头」，改为「她身上**属于母亲**的那部分也在这里露了头——伤口还在流血，她第一件惦记的却是把手柄塞到门外，因为她自己也知道那盒东西最重要」；Diana 的相似点另起一句，落到本章实证上：「本章她与 Diana 的联结只有两处：共用手机的旧账，和童年捉迷藏时姐姐掐她一下的那一下。」

### W3｜`md:99`「序章里那对多出来的银耳环」——数量错（序章是九只，不是一对）｜档：阻断

**原文侧**（`text/ch00_prologue.txt:21`，序章；`text/ch12_chapter_12.txt:6` 同源）：

> Her ears were covered in new piercings, full of earrings she'd never seen before. She counted **nine hoops**, all different sizes, **five in one ear and four in the other**.

（本章 `text/ch11:141` 女孩挑耳环时取的是「several of the larger ones」，逐个钉进 **Alba 的右耳** ⇒ 本章语境里也是「多只、尺寸各异」，不是「一对」。）

**md 侧**（`ch11 chapter 11.md:99`，块 7 读者视角提示）：

> 耳环在这里不是装饰而是记号；序章里那对多出来的银耳环，到这里才有了可能的来路。

**影响**：序章的「多出来的耳环」是**九只**（五只一耳、四只另一耳），且与本章「把好几种尺寸的素银圈一只只钉进右耳」正好互证。md 写成「**一对**」，把一只可核的数字说错了；这条数字还是序章→ch11→ch12 三章之间的**贯穿物**，错了会一路错下去。

**修法（建议改）**：`md:99` 改为「序章里多出来的那**几只**银耳环——她当时数出九只，五只一耳、四只另一耳——到这里才有了可能的来路。」

### W4｜`md:109`「圣洁与暴烈在同一间店里互相覆盖」「女孩想守住的橱窗」——原文没有的定性｜档：提示（措辞过头）

**原文侧**（`text/ch11_chapter_11.txt:153`）：

> She reflexively jumped, and Alba's head hit the floor. Her back against the display with the plastic nails, the girl watched as Alba started shaking again, and the tentacles sprang out, reaching for her a second time. … flinging ribbons of Alba's blood in every direction. … ruthlessly painting the friendly Claire's window displays.

**md 侧**（`ch11 chapter 11.md:109`，块 8 为什么这样写）：

> 接着她的身体把血甩到女孩想守住的橱窗上；**圣洁**与暴烈在同一间店里互相覆盖……

**影响**：两处都是原文没有的定性：①「圣洁」——原文形容橱窗的词是 "friendly"（友好），没有「圣洁」；②「女孩想守住的橱窗」——女孩没有「想守住」任何东西，她只是站在塑料美甲片陈列架旁**看着**（"Her back against the display with the plastic nails, the girl watched as…"），血泼在「友好的 Claire's 橱窗」上，是触手干的，不是女孩守护又失守的。

**修法（建议改）**：`md:109` 改为「先是女孩把血按进她的耳朵，接着她的身体把血甩到那面**友好的** Claire's 橱窗上；友好与暴烈在同一间店里互相覆盖，直到最后触手优雅地折回肚子里，像什么都没发生过。」

### W5｜`md:11`、`md:12`、`md:154`「把银耳环钉进她的耳朵」——部位泛化（原文是**右耳耳垂**）｜档：提示

**原文侧**（`text/ch11_chapter_11.txt:141`；`text/ch11:138`）：

> After piling them into a small mountain to her right, she took several of the larger ones and began to pierce **Alba's right ear**, pressing the earrings all the way through.

> She didn't use a piercing gun, or numb her up with an ice cube.

**md 侧**：`md:11`「还亲手把银耳环钉进了她的耳朵」；`md:12`「那个女孩把银耳环徒手钉进她的耳朵」；`md:154`「那个把银耳环钉进她耳朵的孩子」。

**影响**：方向对（女孩对 Alba）、手段对（徒手、无枪无冰），但**部位**被抹平：原文钉的是**右耳的耳垂／软骨**（"the other side of the lobe or the cartilage"），而且是**好几只**不是一只。md 三处都说成单数泛指「耳朵」。

**修法（建议改）**：三处统一改为「把银耳环徒手钉进她的**右耳耳垂**」。

### W6｜`md:11`「门外**躺着**一个穿红泳衣的小女孩，**用身体挡着门**」——两个状态并列，与原文时序冲突｜档：提示

**原文侧**（`text/ch11_chapter_11.txt:60`、`:63`、`:45`）：

> Under the door, she now saw more than just two feet. The girl was stretched out on the ground, looking up at the ceiling. …（`:60` 女孩躺在地上）
> … it couldn't have been the girl, because she wouldn't have had time to jump up from the floor. …（`:63` 门被顶着时，女孩**已经跳起来**了）
> Whoever it was seemed to be leaning against the door, barricading her inside.（`:45` 挡住门的是**靠着门**的人）

**md 侧**（`ch11 chapter 11.md:11`）：

> 门外躺着一个穿红泳衣的小女孩，用身体挡着门，还亲手把银耳环钉进了她的耳朵。

**影响**：「躺着」和「挡着门」在原文里是**先后**两态（`:45` 靠门挡 → `:60` 她躺在地上 → `:63` 她又跳起来挡门），md 把它们并成同时发生的两个动作；而且 `:45` 的措辞是「**靠着**门」不是「用身体挡」。另注：`:60` 时她躺在地上、手柄盒在她肚子上，此时尚未钉耳环——「还亲手把银耳环钉进」的时间点被压缩到同一瞬间。

**修法（建议改）**：`md:11` 改为「门外那个穿红泳衣的小女孩先躺在地上，手柄盒压在她肚子上；她跳起来抵住门，不放 Alba 出去，最后徒手把银耳环钉进了她的右耳。」

### W7｜`md:73`「『找了多年却在此地重逢』的荒诞」——原文是「多年记不清的脸」，不是「找了多年」｜档：提示（措辞过头）

**原文侧**（`text/ch11_chapter_11.txt:63`）：

> For years, the image she'd retained of this girl had been **blurry and imprecise**, and she didn't recognize that vacant stare, but she was sure she knew exactly who it was. She'd long **dreamed of crossing paths** with her, but she'd never imagined finding her here, lying on the floor of a mall bathroom.

**md 侧**（`ch11 chapter 11.md:73`，块 5 为什么这样写）：

> 而「**找了多年却在此地重逢**」的荒诞，又让这场重逢带上了一层说不清的罪责感。

**影响**：原文是「**一直记不清**她的脸」＋「**早就梦想过**与她相遇」；md 写成「找了多年」，把「模糊的残影」升格成了「持续主动搜寻」。同时 `md:69` 写「她认得这张脸」也对不上原文——原文明说 `she didn't recognize that vacant stare, but she was sure she knew exactly who it was`（**没认出**那个眼神，只是确信知道是谁）。

**修法（建议改）**：`md:69`「她认得这张脸」改为「她**没认出**那双眼睛，却确信自己知道那是谁」；`md:73`「找了多年却在此地重逢」改为「**多年没看清过的脸**，却在商场卫生间的地上重逢」。

### W8｜`md:25`「读者立刻知道这是平安夜」——引语本身不含此信息，属解读当事实｜档：提示

**原文侧**：`text/ch11:6`（块 1 引语）只有一只 MediaMarkt 纸袋与模糊视线；**平安夜是后来才交代的**——`text/ch11:87`「Since it was **Christmas Eve**, the mall had closed without the usual routines.」（另见 `text/ch11:9`「she, like so many mothers that **Christmas**, had made up her mind about what Santa Claus would deliver.」）。

**md 侧**（`ch11 chapter 11.md:25`，块 1 为什么这样写）：

> 读者立刻知道这是平安夜、是商场、是出门办事的半路……

**影响**：块 1 的引语只给了「纸袋＋模糊」，并不能让读者「立刻知道这是平安夜」；这是作者手法的解读，被写成了引语可交付的事实。属解读当事实（不阻断，但需收）。

**修法（建议改）**：`md:25` 改为「读者立刻知道这是商场、是出门办事的半路（至于平安夜，要等到后文商场没照常收尾时才点明）……」。

### W9｜`md:14`「Alba 从照顾别人的母亲变成被安排的人」——原文里她是**自己做主**｜档：提示（措辞过头）

**原文侧**（`text/ch11_chapter_11.txt:9`）：

> Instinctively, she grabbed the box and slid it under the stall door … She fervently hoped they'd be safe on the other side of the door. **Such missions needed to be carried out even if the world was in flames—she, like so many mothers that Christmas, had made up her mind about what Santa Claus would deliver.**

**md 侧**（`ch11 chapter 11.md:14`）：

> Alba 从照顾别人的母亲变成被安排的人……

**影响**：原文写的是「她**自己拿定了主意**」，动机是「就算世界着火，这种事也得做」；「被安排的人」与之相反（她随后确实被女孩反安排，但那是后面的事）。这半句把 Alba 提前写成了被动者，削弱了本章「非做不可的执拗」这条力。

**修法（建议改）**：`md:14` 改为「Alba 从照顾别人的母亲，变成**自己拿定主意**的人——她把最后一样东西主动送出门，然后被安排到别人的位置上」。

### W10｜`md:14`「正是这份非做不可的执拗，让她把最后一样东西交了出去」——「交出去」方向基本成立，但需保住「主动」｜档：提示（措辞收束）

**原文侧**（`text/ch11_chapter_11.txt:9`、`:66`）：

> Instinctively, she grabbed the box and slid it under the stall door … She made sure to set the box right next to the door so she wouldn't lose sight of it. …

> "What's your problem?" the girl asked scornfully while she **petted the box she had taken**.

**md 侧**（`ch11 chapter 11.md:14`）：「……正是这份非做不可的执拗，让她把最后一样东西**交了出去**。」

**影响**：结论不算错（她确实把盒子送出、女孩确实拿走了），但「交了出去」在中文里偏「被迫交出/让渡」，而原文是**主动送出**并「希望它们在门那边安全」（"She fervently hoped they'd be safe on the other side of the door"）。与 W9 叠在一起，读者会得到「Alba 被迫交出手柄」的印象，与原文相反。

**修法（建议改）**：`md:14` 末句改为「正是这份非做不可的执拗，让她**主动把最后一样东西推出门外**——她甚至盼着它在门那边是安全的。」

---

## 四、交叉说明

1. **W2 与 L2 是同一件事的两面。** 原文里 Diana 与 Alba 的对应物只有两条（`text/ch11:12` 共用手机、`text/ch11:84` 掐她一下），md 一条都没写（L2 漏），却把「手柄执拗」挂到 Diana 名下（W2 错）。⇒ 修法不是给 `md:14` 换个说法，而是**先把 L2 补进来**，W2 才能自然消解。
2. **W1 与 L5 是同一件事的两面。** md 全文没有 Brigitte / Brisa / Bijou Brigitte（L5 漏），也就无从知道「前面几章在怀疑害怕的是姐姐 Diana、母亲 Carmen 只是在场」（W1 错）。⇒ 补 L5 能同时给 W1 提供可核依据。
3. **W3 与 L2 共同指向「跨章数字/联结」的核对。** 序章的九只耳环（`text/ch00:21`）在本章被逐只复现（`text/ch11:141`「several of the larger ones … Alba's **right ear**」），md 写成「一对」，属跨章铁证被压缩。
4. **W4 与 W5 都在 `md` 顶部导航与底部总结里重复出现同一处偏差**（`md:11`/`md:12`/`md:154` 三次说「钉进耳朵」；`md:109` 说「女孩想守住的橱窗」），改时须三处同改，否则导航与总结会互相打架。
5. **C＝0 的含义**：md 唯一的「可能像编造」处——红泳衣女孩的身份——**没有写错**。md 全篇只称「女孩／孩子」，没有说她是 Alba 的女儿，与全书铁证（`text/ch12:162`「including **Alba, age twelve**」、`:168`「Twelve-year-old Alba, with her red swimsuit and sun-bleached hair」、`:213`「The red swimsuit and the worn-out Victoria sneakers…」）相容。**不得**在后续改稿中把女孩的身份「说明确」——本章原文没有交代。
6. **逐字与形态不在本单范围**：`2-machine.json` `verdict: ok`，8/8 引语 `ok=true`，`counts` 各项为 0，`h1_shape_ok true`、`nav_count 5 ok`、`blocks 8`、四件子项齐备；`本章词汇` 22 条例句经脚本核对 `rows=22 not_verbatim=0`。唯一异常是「关键词」子项 CJK=0，与 `ch03 chapter 3.md:23`、`ch04 chapter 4.md:23` 同体例 ⇒ **假红**（见 `4-verdict.md` 判定表）。

---

## 五、修后复核命令

> 本轮**未改成品 md**（硬性要求），以下命令用于将来改稿落地后的复核。

```bash
cd /Users/jcxs2014/Documents/Works/EnglishRead

# 1) 机器层门禁（改稿后必须重跑，退出码 0＝无阻断）
bash scripts/chapter.sh "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch11 chapter 11.md"

# 2) 原文行号取证（text/ 被 gitignore，必须用 /usr/bin/grep，不能用 git grep）
TXT="notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch11_chapter_11.txt"
/usr/bin/grep -n "her sister\|Diana pinched\|Christmas Eve\|Bijou Brigitte\|Claire's\|nine hoops\|right ear\|piercing gun" "$TXT"

# 3) 跨章铁证复核
/usr/bin/grep -n "Alba, age twelve\|Twelve-year-old Alba" \
  "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch12_chapter_12.txt"
/usr/bin/grep -n "nine hoops" \
  "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch00_prologue.txt"

# 4) 成品侧核对被改行
MD="notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch11 chapter 11.md"
/usr/bin/grep -n "母亲\|Diana\|交了出去\|银耳环\|圣洁\|想守住\|找了多少\|对" "$MD"

# 5) 词汇表逐字自检（应输出 rows 22 not_verbatim 0）
python3 - <<'PY'
t=open("notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch11_chapter_11.txt").read()
bad=n=0
for l in open("notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch11 chapter 11.md"):
    c=[x.strip() for x in l.rstrip("\n").split("|")]
    if l.startswith("|") and len(c)==5 and c[1]!="词/短语" and "---" not in l:
        n+=1; bad+= c[4] not in t
print("rows",n,"not_verbatim",bad)
PY
```

**审查人**：DSH-Mac。**未执行任何 `git add` / `commit` / `push`；未修改任何成品 md。**
