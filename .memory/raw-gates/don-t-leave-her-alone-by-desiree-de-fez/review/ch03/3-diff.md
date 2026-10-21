# 第 3 章 R3–R4 差异单（人工审查）

- 审查对象：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch03 chapter 3.md`（成品，130 行，6 个引语块）
- 唯一真值：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch03_chapter_3.txt`（原文，246 行，4,249 字符；全章 82 段皆为电话对白，无叙述者转述段）
- 机器层：`bash scripts/chapter.sh "…/ch03 chapter 3.md" --json` → **退出码 0**，`verdict: ok`（详见 `2-machine.json`）
- 流程：R1 素读（`1-suread.json`，先读原文后开 md）→ R2 机器层 → R3 本单 → R4 逐块＋固定三问
- 行号约定：`text:NNN` = 原文行号；`md:NNN` = 成品 md 行号

---

## 一、漏（L）

### L1｜「她把生日和圣诞拆成两天」这一层未进 md｜档：提示（漏）

**原文侧**（`text/ch03_chapter_3.txt:231`）：

> "You know perfectly well it’s my birthday."

**原文侧**（`text/ch03_chapter_3.txt:243`）：

> "You can’t celebrate two things at once. It’s bad luck. And you know it."

**md 侧**（`ch03 chapter 3.md:81-87`，块 6）：已写到「你不能一件事同时庆祝两件，不吉利」，并在导航 `md:11` 写了「最后卡在一句迷信上：生日和平安夜不能一起过」。

**影响**：本条**不算漏**——md 覆盖到位。留此条作为「已核实」的对照项（详见 `4-verdict.md` 的「已核实为正确」段）。

### L2｜妈妈没去酒会，是因为留下来看阿尔巴的三个孩子（Alba 在场说辞）｜档：提示（漏）

**原文侧**（`text/ch03_chapter_3.txt:75`）：

> "She stayed with the kids."

**原文侧**（`text/ch03_chapter_3.txt:81`）：

> "Well, with mine."

**md 侧**（`ch03 chapter 3.md:45-51`，块 3）：只写到 Diana 反问「怎么会？」，未写「妈妈留下来看的是阿尔巴的孩子」这一层。

**影响**：`md:12` 情感弧线位置写「母亲临时不去了的酒会」，读者可能默认母亲是照看 Diana 家的孩子；原文里她照看的是 Alba 那边的人（Alba 自己带着最小的宝宝，Juan 陪着她，所以家里留下的正是 Alba 的另外两个孩子）。

**修法**：块 3 中文理解补一句「她留下来看的是阿尔巴的孩子」。

---

## 二、错（E）

### E1｜块 3 的说话人整组对调｜档：阻断

**原文侧**（`text/ch03_chapter_3.txt:66`，Alba 开口）：

> "I’ll tell you later. Look, let me call you back, I need to call Mom before dinner. Oh, never mind, she has her Christmas drinks tonight."

**原文侧**（`text/ch03_chapter_3.txt:72`，Alba）：

> "She didn’t go."

**原文侧**（`text/ch03_chapter_3.txt:76`，Diana 反问）：

> "How come? She wouldn’t shut up about it all week. She was driving me nuts."

**md 侧**（`ch03 chapter 3.md:45`）：

> **中文理解**：Alba 先把话头推开：Brisa 的演出「很糟」，等会儿再说；她得先给母亲打电话——算了，母亲今晚有她的圣诞酒会。Diana 一句「她没去」把这层挡板掀了，随即追问：怎么会？……

**证据链**（`1-suread.json` `speaker_map`，严格交替）：
- 开篇 `text:6`「"What are you doing?" **Diana asked**.」明示 Diana 是发问方；
- `text:15` Alba 答「there were so many people I couldn't exchange the controllers」；
- `text:57`「"How was Brisa's play?"」（问的人＝Alba，因为 Brisa 属 Diana 家）、`text:60`「"It was bad."」（答的人＝Diana）；
- `text:81`「"Well, with mine."」是 Alba 自己的孩子，`text:83`「"You're kidding."」是 Diana 的反应 ⇒ 交替链自洽，全链 41 句无一破例。

⇒ 「I'll tell you later…let me call you back」是 **Diana**（她要给自己母亲打电话）；「She didn't go.」是 **Alba**；「How come? She wouldn't shut up about it all week」是 **Diana**。md 三处全反。

**影响**：把「演出很糟」的主人（Diana 自己的女儿）安到 Alba 头上，把「她没去」这个关键反转安到 Diana 头上，块 3 的「转折」论述随之整段站不住。

**修法**（**已改**）：块 3 中文理解、为什么这样写、读者视角提示三处改为 Diana / Alba / Diana 的正确归属；导航 `md:15` 的「读者却只听见她说自己被吵到听不清电话」改为「她快听不清对方的声音」（依据 `text:225`「I have to go, I can barely hear you.」）。

### E2｜块 4「她昨天才刚做了美甲」的主语是母亲，不是 Diana｜档：提示

**原文侧**（`text/ch03_chapter_3.txt:79`，Alba 转述）：

> "She told me she didn’t care, she said she was tired."

**原文侧**（`text/ch03_chapter_3.txt:83`，Diana）：

> "You know she cares! She got her nails done yesterday!"

**md 侧**（`ch03 chapter 3.md:57`）：

> Diana 不买账：你知道她有多想去！她昨天才刚做了美甲。

**影响**：中文省略主语时「她」在上一句语境里指的是母亲（Alba 转述的母亲），md 的「她」读起来像 Diana 自己 ⇒ 歧义。

**修法**（**已改**）：改为「母亲昨天才刚做了美甲」。

---

## 三、措辞（U）

### U1｜块 5 读者视角提示把「她连怎么哄孩子都不知道」说得过满｜档：提示

**原文侧**（`text/ch03_chapter_3.txt:180`，Diana）：

> "Well, you give him a cookie and that’s that."

**md 侧**（`ch03 chapter 3.md:75`）：

> **读者视角提示**：留意 Diana 此刻的无能感。她连怎么哄孩子都不知道，这份无知正是她后来能拿「你连一个人坐公交都不行」去激她的底气。

**影响**：后半句引的那句在原文里并不存在（原文是 Diana 问「Why not?」），属把手法层写成了台词层。

**修法**（**已改**）：改为「她连怎么哄婴儿都只会说『给块饼干不就完了』；同一通电话的后半段，阿尔巴说自己带宝宝坐不了公交，她只回了一句『为什么』」。

### U2｜块 2 读者视角提示的「往后你会看到」是跨章预言｜档：提示

**md 侧**（`ch03 chapter 3.md:39`）：

> 记住「周五」和「平安夜」这两个时间点。往后你会看到，这通电话里所有人都在围绕同一个晚上讨价还价。

**影响**：半句预言（可接受），但「所有人」范围过大——本通电话里只有 Diana、Alba 与被转述的母亲三方。

**修法**（**已改**）：改为「这通电话里所有的推来推去，最后都落在这同一个晚上」。

---

## 四、已核实为正确（防误修清单）

以下写法在审查中看似可疑，回原文逐字核对后**成立**，后续改稿不得改动：

1. **块 1 开头三句的顺序与地名用法**（`md:19-27`）：`text:9`「Oh, I'm just at Finestrelles.」→ `text:12`「Again? Didn't you guys go earlier? When I talked to Mom, she said you were still there.」→ `text:15`「Yeah, but there were so many people I couldn't exchange the controllers.」——「先报地名、再被追问、最后解释」的分析成立。
2. **块 6 的迷信**（`md:79-87`）：`text:243`「You can't celebrate two things at once. It's bad luck. And you know it.」——「你不能一件事同时庆祝两件」逐字对得上。
3. **块 6 中文理解里「Alba 催人 / Diana 接话 / Alba 挡回」**（`md:81`）：`text:237`「Come on. I already told the kids you were coming for lunch.」（Alba）→ `text:240`「But we're coming on Christmas Eve, we can really celebrate then.」（Diana）→ `text:243`（Alba）——归属正确。
4. **块 2「Alba 反问：真的在平安夜？你真是没救了」**（`md:33`）：`text:51`「On actual Christmas Eve? You're hopeless.」——Alba 是问的一方，成立。
5. **块 5 的三句顺序**（`md:67`）：`text:174`（Diana「practically a teenager」）→ `text:177`（Alba「he throws a fit」）→ `text:180`（Diana「you give him a cookie」）——成立。
6. **导航「两个女人在电话里一边嫌弃一边互相兜底」**（`md:12`）：全章 82 段皆为对白，无叙述者插话；「兜底」体现在 `text:120`（Diana 主动提出替 Alba 换货）、`text:198`（Diana 建议改坐有轨电车）——成立。
7. **`本章词汇` 24 条例句**：全部为原文逐字子串（机器层 `2-machine.json` `vocab` 组；`check_vocab` 全部 ✅）。
8. **块 1 关键词「there were so many people I couldn't exchange the controllers」**：逐字落在本块引语内（`text:15`）——成立。
