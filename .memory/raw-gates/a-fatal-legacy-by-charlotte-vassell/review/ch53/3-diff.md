# ch53 · 三张单子（漏 / 编 / 错）

> 审查方：独立审查员（只审 ch53）。源：`text/ch53_53.txt`（唯一权威源，2786 字符 / 78 行）。
> 交叉源（仅用于核「分部」名，epub 内 `OPS/`）：`library/A Fatal Legacy (Charlotte Vassell) ….epub`。
> md：`ch53 callie is finally sick.md`（99 行）。
> 档位：**阻断 / 提示 / 假红 / 跳过**。

---

## 一、编（md 有、原文无）

### 编-1（阻断）分部名「A Tuesday in May」不存在

- **md 侧**（`ch53 callie is finally sick.md:15`）：
  > `- **叙事手法**：全章靠家常对话推进，底下的不安用生活细节垫出来——谁买了什么、谁把话岔开、碎片布属于哪个项目、扫描日期是谁先提起；分部「A Tuesday in May」把这一切处理得很轻，收尾落在 Caius 去晾衣服这种家务动作上。`
- **原文侧**：`text/ch53_53.txt` **全文没有 "Tuesday"、没有 "May"、没有任何分部标题**（本章只有一个分部标题 `Caius and Callie’s Flat`，见 :17）。md 把一个不存在的分部名用书名号引起来当事实陈述。
- **权威核对（epub）**：本章 `OPS/s071-Chapter-053.xhtml`（其 `<h2 id="h253">Caius and Callie’s Flat</h2>`，正文与 `text/ch53_53.txt` 逐字一致）所属分部是 `OPS/s069-Part-011.xhtml`，该分部标题为 **`<h1 id="h167">TUESDAY</h1>`**；全书 12 个分部的标题里唯一的 "…IN MAY" 是 `OPS/s008-Part-001.xhtml` 的 **「A FRIDAY IN MAY」**（第 1 章起的第一部，与 ch53 无关）。⇒ md 写的「A Tuesday in May」是把别处的分部名（FRIDAY IN MAY）与本分部名（TUESDAY）拼出来的，全书不存在。
- **取证命令与输出**：
  ```
  /usr/bin/grep -ril "tuesday" .     # 在书目录内（含 text/ 与全部 md）
    → 唯一命中 ./ch53 callie is finally sick.md:15 ；退出码 0
  /usr/bin/grep -n -i -E "monday|tuesday|...|sunday" text/*.txt
    → 37 行命中，全部是正文里的 "Saturday/Monday" 用词，无任何分部标题；退出码 0
  ```
- **同类章节写法（证明正确写法存在）**：`ch51:11`「在分部「MONDAY」里」、`ch18:11`「在 TUESDAY 这一分部里」、`ch22:12`「本章属「五月的星期三」这一分部」、`ch54:15`「分部「SIX WEEKS LATER」里」。
- **结论**：**阻断**（编造分部名并加书名号当事实）。正确写法应为 分部「TUESDAY」。

### 编-2（阻断）Caius 被写成 Callie 的「丈夫」

- **md 侧**（`ch53 callie is finally sick.md:44` 与 `:51`）：
  > `:44`「她的**丈夫**刚数出三样她的享乐——Pinot Grigio、开心果可颂和床上那点事」
  > `:51`「她先夸了**丈夫**一句，再拿起那封通知信，把日期说出口」
- **原文侧**：`text/ch53_53.txt` 全章**没有 husband / wife / married / 任何婚姻表述**（`:20–:77`）。二人的关系表述只有同居（`the flat`）与 `'Thanks, babe.'`（`:35`）、`'How’s my girl doing?'`（`:35`）。
- **全书证据（他们订了婚、未结婚）**：
  - `text/ch40_40.txt:59–61`：
    > `'You can have the wedding here,' Marcus said.` ／ `'If we pull our finger out you could have it in August. Caterer. Marquee. Someone to do the flowers. Callie knows people who could do her dress on a short turnaround,' Bridget said.`
    ⇒ 婚礼在未来（八月），ch53（五月）时**尚未举行**。
  - `text/ch52_52.txt:41`：`'I found out about the engagement rings, by the way.'`；`:50`：`'I don’t want Callie walking around with something too expensive.'` ⇒ 订婚戒指，不是婚戒。
  - `text/ch27_27.txt:98`：`'I take it that isn’t what it’s like with your boyfriend? He is your boyfriend, you’re not engaged, right?'`
  - `text/ch27_27.txt:101`（Callie 本人对这段关系的定义）：
    > `'I refer to him as my "paramour" and he refers to me as his "missus". It’s an equal partnership.'`
- **同书写法**：ch27 md 写「当警察的**伴侣** Caius」，ch28 md 写「凯厄斯被马特套出凯莉怀孕、自己要当爸」，全库无一处把二人写成夫妻。
- **结论**：**阻断**（关系状态凭空升级为婚姻；两处）。应作「未婚夫 / 伴侣 / 对象」。

### 编-3（提示）「三个『No』」——原文是 2 个 No + 1 个 Yes

- **md 侧**（`:30`）：
  > `**为什么这样写**：三个「No」连着一句「Yes」，是一段不像台词的台词：……`
  > （`:28`）`Callie 连着说了三句「不。对。不」。`
- **原文侧**（`text/ch53_53.txt:44`）：
  > `'No. Yes. No.' Callie reached for the fabric on the table.`
  ⇒ 三个词＝**两个 No + 一个 Yes**（中间的 Yes 才是「想听」的那个），不是「三个 No 再加一个 Yes」（那是四个词）。md 的「三个『No』」既多算一个 No，又把 Yes 的位置说成了末尾。
- **同 md 内的自相矛盾**：`:11` 导航写的是正确的「`No. Yes. No.` 的三连回答」；`:29` 关键词也写 `No. Yes. No.`。只有 `:28`/`:30` 两处走样。
- **结论**：**阻断**（对引语本身的计数错误，且正是本章专属判据③「三连回答原文是几个字」要核的那一处）。`:28` 把 Yes 译成「对」（读作「正确」而非「好／想」），建议改为「不。好。不。」并把 `:30` 改成「两个『No』夹着一个『Yes』」。

---

## 二、漏（素读有、md 无）

### 漏-1（提示）骷髅 / 「dead nun」与「earthly」一节完全没进块、也没进导航

- **原文侧**（`text/ch53_53.txt:50–66`，共 6 个话轮）：
  > `:50` `'Were there any skeletons in the end?'`
  > `:53` `'Yeah, hundreds of them. I’ve never heard the words “dead nun” spoken so many times.'`
  > `:56` `'I really would’ve been a terrible nun.'`
  > `:59` `'You’re too earthly.'`
  > `:62` `'Earthly?'`
  > `:65` `'You like pleasure too much. Pinot Grigio, pistachio croissants and getting railed.'`
- **md 侧**：`ch53 …md` 全文只在**词汇表**出现一次：`ch53 …md:76` `| terrible nun | 糟糕的修女（指不成气候的修女） | 'I really would’ve been a terrible nun.' |`；5 个引语块与 5 条导航**均未**写到「几百具骷髅 / dead nun / 新房子挖出人骨」这条线。
- **为什么仍判「提示」而非「阻断」**：本章的主动作（吐了、合约黄了、扫描日期）已被覆盖；这一节是喜剧插科，也是「骷髅＝新房子下面有修女墓」这条暗线的唯一一次露头，属可取舍范围。
- **结论**：**提示**（md 未写取舍理由；建议在导航「线索结构」里补一句，或在块 4 引语扩到 `:65` 一带）。

### 漏-2（提示）块 4 的分析依赖引语之外的前文 ⇒ 引语选短

- **md 侧**（`:44`）：
  > `她的丈夫刚数出三样她的享乐——Pinot Grigio、开心果可颂和床上那点事——……`
- **原文侧**：块 4 的引语只到 `:68` `'None of that. That's what got us into this mess.' Callie stuck her tongue out.`；md 分析里点名的三样东西在**引语之外**的 `:65`：
  > `'You like pleasure too much. Pinot Grigio, pistachio croissants and getting railed.'`
- **判断依据**：`docs/rules/生产-审查对照.md` S2 典型失误①「截短：分析覆盖的原文比引语长」——本条是「分析引用了引语外的一行」，属同一类；但该块讲的核心（否认＋承认同口气）仍在引语内，故判**提示**（建议把引语扩到 `:65` 收尾，或在分析里点明「他上一句刚数出三样」）。

### 漏-3（跳过）本章之外的汇总层对本章的引用

- **说明**：本次范围仅第 53 章；`00_概述.md` / `00_金句精选.md` / `00_情感节点.md` 对本章的引用与断言**未核**（不属本章 md，也未在委托范围内）。
- **结论**：**跳过**（如实标注「未查」，不写成「通过」）。

---

## 三、错（两边都有但不一致）

### 错-1（提示）「给人梳头」——原文是抚摸头发，不是梳

- **md 侧**（`:12`）：`- **视角**：……煮水、拿杯子、泡茶、**给人梳头**、把手机递过去；`
- **原文侧**（`text/ch53_53.txt:35`）：
  > `Callie fell into his lap and he stroked her hair.`
  ⇒ `stroked her hair`＝抚摸／顺她的头发；`梳头`＝comb hair，是另一个动作。
- **结论**：**提示**（动作不准；改作「抚她的头发」）。

### 错-2（提示）「把手机递过去」——原文是掏出手机给她看

- **md 侧**（`:12`）：`……**把手机递过去**；`
- **原文侧**（`text/ch53_53.txt:47`）：
  > `Caius took his phone out and showed Callie some of the stills from the footage of the little robot’s second journey.`
  ⇒ 他**掏出自己的手机**并把屏幕上的剧照**给她看**，手机没有交到她手上。md 的施事方向没错（主语仍是 Caius），但动作被换成「递过去」，易读成「把手机递给 Callie」。
- **结论**：**提示**（改作「掏出手机给她看剧照」更准）。

### 错-3（提示）「手上却在搓那块碎布」——动作发生在前一个场景

- **md 侧**（`:44`）：`她嘴上推掉，手上却在搓那块碎布，身体比嘴诚实。`
- **原文侧**：`text/ch53_53.txt:44` `'Callie reached for the fabric on the table. She rubbed it between her fingers.'`（在块 2 里）；到块 4 的 `:68` 她的动作是 `Callie stuck her tongue out.`，**原文没有写她此刻仍在搓布**。
- **结论**：**提示**（时序外移／推断）；原文只保证她「搓过那块布」，不保证「此刻在搓」。

### 错-4（提示）「信……不是当场拆开的」——原文未写的否定推断

- **md 侧**（`:51`）：`信是从茶几上拿起来的，不是当场拆开的，说明她早就知道内容，只是一直没告诉对面的人。`
- **原文侧**（`text/ch53_53.txt:74`）：
  > `'You smell really good.' Callie picked a letter up off the coffee table. 'We’ve had the date for the twelve-week scan come through.'`
  ⇒ 原文只写「拿起一封信」并说出日期已到位；「不是当场拆开的」是原文没写的**否定推断**（无逐字依据）。
- **结论**：**提示**（可改为「她一拿起信就报出了日期——信显然早看过」）。

### 错-5（提示）字词与格式层面的三处小瑕

- `:99` 一句话总结：`底下那点**不安全**靠生活细节垫着`——按同句语义应为「**不安**」（前一句已用「不安」）。
- `:31` 读者视角提示：`而不是**Jen** 那边的进展`——缺空格；且原文她谈的是 Venetia 带来的消息，并未谈「Jen 那边」，措辞含混。
- `:44` `床上那点事` 对 `getting railed`——语域大幅降级（原文是粗口），可接受但偏弱。
- `:21`/`:44` `碎布` 与词汇表 `:66` `swatches｜布样；色卡` 用词不一致。
- `:95` 词汇例句 `| hundreds | 数百个 | 'Yeah, hundreds of them. |`——右引号缺失。
- **结论**：**提示**（四条打包）。

---

## 四、已核实为正确（防误修）

以下几处**读着像错、回原文核对后成立**，后续任何人不得以「读着不对」为由改动：

1. **PCQV 与唱片公司未混同**（`:11`、`:28`、`:99`）：原文 `text/ch53_53.txt:44` `The deal's off with PCQV, obviously. Everyone at the record label is panicking because they're not sure how much they knew, if that makes sense.`——PCQV（法国奢侈集团，彩妆/香氛线，见 ch36 md `:11`「法国奢侈集团 PCQV」「欧拉莉亚自己的唱片公司是另一方」）与唱片公司是两个主体，md 三处都分列陈述，**正确**。
2. **扫描日期是「通知到了」，不是「已经做完」**（`:49`「说十二周扫描的日期已经通知下来了」、`:11`「日期定下来了」、`:99`「那封通知信里十二周扫描的日期」）：原文 `text/ch53_53.txt:74` `We've had the date for the twelve-week scan come through.`＝日期通知到位；md 全篇**没有**「扫描已经做完」的意思，**正确**。
3. **本章没有「电话那头」**：原文全章无任何电话对话（手机只用于展示剧照，`:47`）；md 全文也没有「电话那头」字样，**没有凭空造出电话内容**。注意：ch18 md 的「电话那头」指的是 Venetia 那通电话（`text/ch18_18.txt:44`），与本章无关。
4. **「六个开心果可颂」数字逐字一致**：原文 `:20` `bought six more pistachio croissants`；md `:11`「六个开心果可颂」、`:99`「六个可颂」——数字正确（「more」＝又买了六个，md 未强调「又」但不构成错误）。
5. **导航「Callie 吐过之后」不误**：`:26` `Callie came out of the bathroom and flopped onto the sofa. 'I was finally sick.'`——先吐后说，顺序成立。
6. **块 3「他们」指唱片公司**：`text/ch53_53.txt:47` `'They're definitely morally culpable if not legally.'` 的 `They` 承上句的 the record label，md `:35` 写「他们即便在法律上不担责」未错配到 PCQV，**正确**。
7. **词汇表例句全部命中本章**：`check_vocab.py` 全书退出码 0，ch53 无 FAIL/WARN（仅 `:95` 引号不闭合属格式）。
