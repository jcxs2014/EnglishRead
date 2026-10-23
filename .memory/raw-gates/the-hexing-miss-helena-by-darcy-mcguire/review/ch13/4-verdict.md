# ch13 · R5 判定表（深审）

> 章：`ch13 the carriage confession.md`｜原文：`text/ch13_chapter_13.txt`（326 行）｜档位：**深审 R0–R5**（批 5／27，第 1 章）
> 取证纪律：R1 先素读（96 事件 / 10 关系 / 10 数字 / 5 未决 / 16 陷阱，全部逐字回源自检 0 BAD），写完才打开 md。

---

## 一、四组计数

### 组 1 · 逐字

| 项 | 结果 | 取证 |
|---|---|---|
| 引语块逐字 | **8/8**（8 片段，`segment_miss=0`） | `2-machine.json` → `quotes[*].segments[*].ok=true` |
| 含 `…` 的引语 | **0 条** | 本章 8 条引语无省略号；R0 全书级 `verify_fragments_indep.py` 312 片段 / 0 MISS 已覆盖 |
| 词表例句逐字 | **22/22** | `/tmp/vocab_check_hx.py 13` ⇒ `ch13: rows=22 missing=0` |
| 词表词头落在例句内 | **22/22** | `/tmp/vocab_head_hx.py` ⇒ 无输出（零失配），rc=0 |
| 素读底稿自身逐字 | **96/96** | `/tmp` 自检脚本：`events 96 … BAD 0`（含 U+FFFD 0、行号越界 0、关系/数字片段全部命中） |

### 组 2 · 对应

**8/8 块的中文理解与引语对应成立**（R4 三问逐块见 `3-diff.md` §四）。
失配仅出现在**分析层越界**两处：原句 5「那个雨天」（E2，阻断）、原句 3「一副说完就不管的样子」（E7，提示）。
无「分析讲全书主旨」型失配，无「只复述字面」型失配。

### 组 3 · 形态

| 项 | 结果 |
|---|---|
| H1 | `13. Chapter Thirteen` — `h1_shape_ok=true` |
| 导航项数 | **5**（`nav_count_ok=true`，`nav_missing=[]`） |
| 子项 | 4 项＝本书众数（`subitems_modal` 与 `profile_subitems` 一致） |
| 块数 | **8** ∈ 本书 [6,13] ∩ 本章 `block_target=[5,8]` ⇒ **已触上限，不得增第 9 块** |
| 引号配对 | 本章 **0 偏离**（`/tmp/pair4_hx.py` 全书 TOTAL 1，唯一一处在 ch09 原句 7） |
| CJK 密度 | `cjk_low=0`（四子项比率 0.84–0.94） |

### 组 4 · 断言

**共核 52 条** ＝ 相符 **45** ／ 提示 **5** ／ 阻断 **2**。

---

## 二、判定表（只列非「相符」项）

| # | 断言（md 位置 + 原文） | 证据（text 行号 + 逐字） | 结论 | 档位 |
|---|---|---|---|---|
| **E1** | 原句 1·读者视角提示：「读者读完这句会知道，**这一章要交代的不是案情**，而是她怎么重新看自己」 | `:305` `He said there were others who had reason to murder Hubert, but what he didn’t tell us was the name that came into his mind.`；`:311` `‘Not intentionally. But when you asked who killed your husband, he thought it clear as church bells on Sunday. **George Lippert.**’`；`:317` `‘No idea. But Uncle Lachlan might know. And if he doesn’t, he’ll find out.’` | 章级内容断言**与原文相反**：本章章末正是案情推进（多出一个陌生嫌疑人）。**并与同一 md 的原句 7·读者视角提示「这一句把追查的方向整个换了」自相矛盾** | **阻断** |
| **E2** | 原句 5·为什么这样写（末句）：「气味写得比动作更牢，**那个雨天**就这样被一句话钉住」 | 原句 5 引语起于 `:158` 的 `Clara and I hid together in a linen cupboard.`，**不含**雨天；雨天在引语之外：`:158` `It was a rainy day, and we were playing hide-and-seek. Ellie was seeking us.` | 分析覆盖的原文比引语长（引语截短型越界）。所述事实本身为真，故修法是**换词**而非撤回 | **阻断（轻）** |
| E3 | 原句 8·为什么这样写：「四句都短，**句子之间没有连接词**」 | 引语自身 `:326`：`**But** she saw Helena’s lips press together. She shouldn’t have asked. It was impossible **at any rate**. She wasn’t a witch, **no matter what** the fox said.`；md 自己的中文理解把 `at any rate` 译作「**反正**」 | 四个句子**之间**按字面确无连接词（`But` 在首句句首、`at any rate` 在第三句句内），但读者眼前的引语里两处连接成分都在 ⇒ 措辞与原文语感不符。**与 ch12 E1（阻断）的区分**：ch12 那句「两句之间没有转折词」被 `But` 正好夹在所描述的两句中间当场证伪；本章的「句子之间」仍可字面成立 | **提示** |
| E4 | 一句话总结：「女教师告她跟动物低语、召来天气，**母亲却只盼魔法绕过女儿**」 | `:218` `‘…Whatever is wrong, **train it out of her**.’`；`:227` `‘…**I will double your wages** to keep what you have seen a secret.’`；`:230` `‘**Triple.**’`；`:233` `‘Fine. But if you breathe a word of this, **I will decimate you**. When I’m through, you won’t be fit to train field mice.’` | 「只」字把母亲的三项**行动**（吩咐训练掉／出钱买沉默／威胁毁人）压成一句心愿；与 L6（该段交易未进分析层）同源 | **提示** |
| E5 | 导航·叙事手法：「中段插入一段**没有过渡的**童年闪回」 | `:212` `**A memory flashed, fast and vivid.**`（明示过渡句）；`:209` 末句 `she couldn’t remember what if felt like to just be Cyn.`（软引子） | 技法描述与原文相反。（同句后半「靠马车一顿把人拽回现在」对应 `:263`/`:266`，**说对了**） | **提示** |
| E6 | 导航·人物弧线：「那份沉默既让她**挫败**，也让她**着迷**」 | `:89` `‘It’s **frustrating**. I’m used to the constant noise, but the silence is impossible.’`（挫败 ✓）；`:200` `You **bewilder** me.`；`:131` `**Infuriatingly** so.` | 「挫败」有直接对应；「着迷」在原文无对应词，最接近的是 `bewilder`（＝摸不着头脑／困惑） | **提示** |
| E7 | 原句 3·为什么这样写：「舔嘴、搁鼻子，**一副说完就不管的样子**」 | 引语（`:98`）只有 `He licked his chops and placed his sharp nose between delicate paws.`；「说完」在引语之外的 `:95`（狐狸的心声 `I have a few questions I’d like answered. Like why you two smell of each other.`） | 「说完」依赖引语外的一句；但 md 导航已写「狐狸哈姆雷特在心里插话」⇒ 全篇内部可自证 | **提示（轻）** |

### 漏 / 编（详见 `3-diff.md` §一、§二）

- **漏 7 条（L1–L7），全部不构成阻断**：L1 `:209` 辛西娅的「跳下去」宣言与吻手指；L2 `:269`「那栋她很快就要搬离的房子」；L3 `:176`「什么也没发生／克拉拉爱的是马厩管事之子」；L4 `:83`「和你在一起，是安静的」原句未收；L5 `:71` 眼睛变银的机制；L6 `:227`–`:233` 封口费 double→triple 与「decimate」威胁；L7 `:317` 拉克兰叔叔这条下章钩子。
  ⚠️ 其中 **L3 与导航的「初次心动」表述互为依存**——正因为原文 `:176` 明写 `Nothing happened`，「初次心动」才不至于被读成一段旧情；建议补四字。
- **编 0 条**（十一处疑点逐条排除，见 `3-diff.md` §二）。

---

## 三、修复指令（改前一行 → 改后一行）

> **默认只出指令不改稿**；以下 7 条交执行方。E1 为第一优先，E5 为第二优先。

| # | 档位 | 位置 | 改前 | 改后 |
|---|---|---|---|---|
| E1 | 阻断 | 原句 1·读者视角提示 | `读者读完这句会知道，这一章要交代的不是案情，而是她怎么重新看自己；她说“看清了”，可看清的究竟是什么，还要等车厢里的对话一点点交出来。` | `读者读完这句会知道，开场要交代的不是案情，而是她怎么重新看自己；她说“看清了”，可看清的究竟是什么，还要等车厢里的对话一点点交出来——案情要到章末才以一个陌生的名字回到桌上。` |
| E2 | 阻断 | 原句 5·为什么这样写 | `气味写得比动作更牢，那个雨天就这样被一句话钉住。` | `气味写得比动作更牢，那段回忆就这样被一句话钉住。` |
| E3 | 提示 | 原句 8·为什么这样写 | `四句都短，句子之间没有连接词，读起来像一句接一句地给自己找理由。` | `四句都短，句首一个“ But ”、句中一个“反正”，把否认一句句往前推，读起来像她在给自己找理由。` |
| E4 | 提示 | 一句话总结（`:139`） | `一段童年闪回里，女教师告她跟动物低语、召来天气，母亲却只盼魔法绕过女儿；` | `一段童年闪回里，女教师告她跟动物低语、召来天气，母亲一边出钱买沉默、一边盼魔法绕过女儿；` |
| E5 | 提示 | 导航·叙事手法 | `中段插入一段没有过渡的童年闪回，靠马车一顿把人拽回现在；` | `中段只用一句“记忆闪过”带入童年闪回，再靠马车一顿把人拽回现在；` |
| E6 | 提示 | 导航·人物弧线 | `那份沉默既让她挫败，也让她着迷。` | `那份沉默既让她挫败，也让她摸不着头脑。` |
| E7 | 提示 | 原句 3·为什么这样写 | `先写她猛一转头，再写狐狸的闲适：舔嘴、搁鼻子，一副说完就不管的样子。` | `先写她猛一转头，再写狐狸的闲适：舔嘴、搁鼻子，一副丢下那句话就不管的样子。` |

> ⚠️ **E2 若选择「扩引语」而非「换词」**：可把 `It was a rainy day, and we were playing hide-and-seek. Ellie was seeking us.` 并入原句 5 引语之首（源文 `:158` 同段，逐字可回源），**不增块**、不触 `block_target` 上限；两种改法择一即可，**不得同时做**（否则「雨天」既在引语内又在分析里重复）。

---

## 四、已核实为正确（45 条，本轮逐条回源）

**导航·一句话概括（8 条）**
1. 「海伦娜再试读心」——`:50` `‘Try again, now. I’ll think something simple, and you try to read me.’` ✓
2. 「眼睛在暗处转成银色」——`:59` `In the dark carriage… they lightened, glowed, and turned to flashing silver.` ✓
3. 「狐狸哈姆雷特在心里插话，辛西娅发现自己听得见它」——`:95` ＋ `:98` `some magic must be at play to let her hear Helena’s familiar` ✓
4. 「她承认拍照时想的是海伦娜的头发、想尝她」——`:110` `‘I was thinking that your hair is like a blazing sunset… And I wanted to taste you.’` ✓
5. 「九、十岁那年在亚麻橱里对克拉拉·博蒙特初次心动」——`:158` `I was near to nine or ten… Clara and I hid together in a linen cupboard… It was then I knew.` ＋ `:149` `‘Clara Beaumont.’` ✓（「初次心动」为 `:158` `everything in me came alive` 的合理对应；⚠️ 依赖 `:176` `Nothing happened` 才不致误读，见 L3）
6. 「心里第二次冒出『她是我的』」——`:164` `She is mine.` ＋ `:167` `For the second time` ✓（第一次在 ch11 `:89`）
7. 「海伦娜说出辛克莱脑中闪过的名字乔治·利珀特」——`:305` `the name that came into his mind` ＋ `:311` `George Lippert.` ✓
8. 「辛西娅问过能否听见动物，最后仍说自己不是女巫」——`:320` ＋ `:326` `She wasn’t a witch, no matter what the fox said.` ✓

**导航·情感弧线位置（4 条）**
9. 「紧接俱乐部那晚的拍照与对峙，两人同车回梅费尔」——`:35` `as they bumped along the gas-lit streets towards Mayfair`（跨章衔接 ch12 ✓）
10. 「从被人试探的窘迫 → 主动坦白欲望 → 听见另一个女人的名字时生出嫉妒」——`:101` → `:110` → `:152` `An overwhelming hatred for Clara Beaumont washed through Cynthia, though she didn’t know a thing about her.` ✓ **时序正确**
11. 「一段童年闪回把她压回七岁那年的恐惧」——`:245` `He was ten, only three years older than her` ＋ `:248` `her seventh birthday` ✓（10−3＝7，两处互证）
12. 「车停时她已经在道别，最后一句又把刚松动的部分按了回去」——`:263` ＋ `:281` `‘You are home, Helena.’` ＋ `:326` ✓

**导航·Tropes（4 条）**
13. 「马车告白、读心试探、初恋情敌、家族隐瞒魔法的童年闪回、侦探线上的新名字都在」——`:110`／`:50`／`:152`／`:212`–`:260`／`:311` ✓ 五项逐条落地
14. 「能读人心的海伦娜偏偏读不到辛西娅」——`:47` `no matter how I try, your thoughts remain hidden. It makes no sense.` ✓
15. 「辛西娅能听见的偏偏是狐狸」——`:98` ✓
16. 「告白之后等来的不是承诺，而是『情感纠葛应当避免』的劝告」——`:110`（告白）→ `:194` `Emotional entanglements are fraught with peril and should be avoided at all costs.` ✓ **时序成立**（劝告确在首次坦白之后）；且海伦娜全章**从未给出承诺** ✓

**导航·人物弧线（5 条）**
17. 「辛西娅从『我不是女巫』的自我否认里，把欲望说出口」——`:110` ＋ `:326` ✓
18. 「海伦娜承认自己被弄糊涂了」——`:200` `You bewilder me.` ✓
19. 「愿意把等待的时间让给她」——`:206` `I want to give you whatever time you need to be sure.` ✓
20. 「狐狸哈姆雷特用一句气味的问题，把两人之间的亲密点破」——`:95` `Like why you two smell of each other.` ✓
21. 「十岁的哥哥托马斯替她争辩，随即被女教师拉走，第二天就要去上学」——`:239` ＋ `:245` `Governess Smithers pulled him away` ＋ `:242` `You’re leaving for school on the morrow` ✓

**导航·叙事手法（3 条，另 1 条见 E5）**
22. 「全章限在马车这一封闭空间」——`:35`–`:326` 当下时间全在车厢内（闪回另计）✓
23. 「几乎全由对话推进，辛西娅的判断夹在两句台词之间」——`:41`–`:92`、`:101`–`:209`、`:299`–`:326` 皆对话与心声交替 ✓
24. 「章末不解释她为什么问动物的心思，只留一句自我否认」——`:320`→`:326`，原文未给动机 ✓

**原句 1–8 的分析层（17 条）**
25. 原句 1·中文理解「纱被揭掉…变的只有她自己心里的一切」——`:35` ✓
26. 原句 1·为什么这样写「**三句话**」——引语确为 3 句 ✓（计数断言已枚举取证）
27. 原句 2·为什么这样写「颜色先被写成『辨不出』」——`:59` `she could barely distinguish their shade` ✓
28. 原句 2·为什么这样写「『变亮、发光、转银』**三个动作**」——`lightened, glowed, and turned to flashing silver` ✓
29. 原句 2·为什么这样写「比喻取的是结冰」——`like water freezing on a pond` ✓
30. 原句 3·中文理解「她没有感到海伦娜说过的那种失重般的涌动」——`:98` `She didn’t feel the rush of weightlessness Helena described` ✓
31. 原句 3·为什么这样写「最后一句用『一定』补上解释，说明她拿不准」——`some magic **must** be at play` ✓（未升格为叙述者断言）
32. 原句 3·读者视角提示「她把这件事推给某种魔法，却没有问为什么偏偏是她听得见」——全章她只在 `:320` 问**海伦娜**能否读动物，**从未**问自己为何能听见 ✓（否定断言成立）
33. 原句 4·为什么这样写「开头先立一句『不反悔』」——`:110` 首句 `But when Cynthia made a promise, she did not renege.` ✓
34. 原句 4·为什么这样写「两个比喻都往暖色上走」——`blazing sunset`／`the glory of autumn` ✓
35. 原句 5·为什么这样写「被压成**三样东西**：藏身处、气味、贴过来的身体」——`linen cupboard`／`the smell of starch and pears`／`pressed her body against mine` ✓
36. 原句 5·为什么这样写「没有一句解释『明白了什么』，只用『就是那一刻』收住」——引语止于 `It was then I knew.` ✓（否定断言成立）
37. 原句 6·中文理解「就像当年绕过她自己，也绕过她自己的母亲」——`:260` `As it did me, and my mother.` ✓ **三代**，未写成两代
38. 原句 6·为什么这样写「整段没有一个狠字，却句句是在关门」——`:260` 全段无威胁性词汇 ✓
39. 原句 7·中文理解「他并不是有意说出来的」——`:311` `Not intentionally.` ✓
40. 原句 7·中文理解「当**她**问是谁杀了她丈夫时」——`:311` `when **you** asked`（海伦娜对辛西娅说）⇒ 归属方向正确 ✓
41. 原句 7·为什么这样写「前半句先撇清『不是有意』，后半句再让名字落地；名字落在句末」——✓
42. 原句 8·中文理解「反正那是不可能的事」——`It was impossible at any rate.` ✓（**但**见 E3：分析层否认了这里的连接成分）
43. 原句 8·读者视角提示「读者刚看见她承认欲望、追问动物的心思，转头就撞上这句否认」——`:110` → `:320` → `:326` ✓ **时序正确**

**词表与总结（2 条）**
44. 词表 **22 行**释义与例句逐条对应（`decimate` 释义与 ch11 不一致 ⇒ 进跨章术语汇总，不计本章缺陷）✓
45. 一句话总结除 E4 一处「只」字外，其余各项（读心转银／狐狸插话／坦白／克拉拉／第二次「她是我的」／乔治·利珀特／问过动物／不肯承认是女巫）与导航·一句话概括一致、与原文一致 ✓

---

## 五、覆盖声明与本章特有盲区

- **覆盖**：本章为**深审**（R0–R5 全跑），非「仅机器层」。人判覆盖：导航 5 项全部、原句 1–8 的四子项全部（32 项）、词表 22 行全部、一句话总结、H1 与形态。
- **深审进度：12/27**（ch02–ch13 已完成；ch01 为试产章、ch18/ch27 已有快审四件套待加深复核）。
- **本章特有盲区（机器层零覆盖，全靠人判）**：
  1. **章级内容断言**（E1 型）——「这一章要交代的不是 X」这类句子无任何门禁可查，且**能与同一 md 的另一块自相矛盾**；建议后续各章把「读者视角提示」里出现「这一章／本章」的句子单独列一遍。
  2. **分析层的「引语外具体细节」**（E2 型）——`segment_miss=0` 只证引语逐字，**不证分析没有伸手到引语之外**；单个名词（「那个雨天」）就能越界。
  3. **否定式技法断言**（E3／E5 型）——「没有连接词」「没有过渡」这类句子最容易被写顺手，须逐字回数。
  4. **`只／仅／从来` 一类限定副词**（E4 型）——总结层的压缩最易在此处失真。
  5. **语料层的「像广告的正文」**——`:287` 是狐狸的心声而非推广行（详见 `3-diff.md` §六）；判据是**跨章是否逐字重复**＋**上下文是否构成对话**。
- **本章未做裁决的悬置点（原文本身未答，不得代为断言）**：U1「焦糖和咸味」那个问题一周前问在何处；U2 海伦娜为何读不到辛西娅；U3 辛西娅七岁前记忆为何空白；U4 乔治·利珀特是谁；U5 辛西娅即将搬去哪里。
