# 3-diff.md · 第 54 章《A Fatal Legacy》对账（漏 / 编 / 错）

- 权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch54_54.txt`（11,624 字符）
- 被审：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch54 there is no heartbeat.md`（145 行）
- 区间记法：`ch54:[起,止]`＝源文字符区间（换行计 1 字符）；`md L<n>`＝精读 md 行号
- 素读底稿：同目录 `1-suread.json`（先素读后开 md，顺序合规）
- 机器层：同目录 `2-machine.json`（`bash scripts/chapter.sh … --json`，退出码 0）

> 校准说明：本章引语覆盖率 20.1%，**与本书中位 20.5% 持平**（54 章实测），块数 8（中位 7，范围 5–10）⇒
> **「块少／覆盖低」本身不构成漏**。下面的「漏」只针对**键控节拍**——即本章唯一的原因说明、导航自己拿去当弧线依据的两处对白。

---

## 一、漏（素读有、md 无）

### D-1 ｜阻断｜顾问对「为什么」的回答（本章唯一的原因／死因说明）整段无引语、无分析

**源文 ch54:[3089,3285]**
```
‘Why?’ Callie whispered.

The consultant slowly shook his head. ‘I don’t know. Usually there’s a genetic problem
with the foetus which makes it incompatible with life. Sometimes it just happens.’
```
**md**：全书 54 份章 md 中 grep `genetic problem` / `incompatible with life` / `Sometimes it just happens` ＝ **0 命中**；本章导航、总结、词汇表均未提「原因」。

**为什么算阻断**：这是本章**唯一**关于死因／原因的说明，且紧接诊断抛出。本章专项要求「查结局断言（死因…）」——
md 既没引、也没析，等于把末章最关键的一块医疗信息整段跳过，读者只能知道「没心跳」，不知道医生怎么回答「为什么」。
md 未写任何取舍理由。

**修法**：新增 1 块（引语 = `‘Why?’ Callie whispered.` + 顾问整句），或在原句 4 块后补一块。

---

### D-2 ｜阻断｜「要不要再试一次」与「National Trust／继承人」两处对白，导航拿去做弧线依据，精读层却零承载

**源文 ch54:[5047,5074]**
```
‘Do you want to try again?’
```
**源文 ch54:[5077,5181]**
```
‘At some point. But not right now. You need to recover, and we need to move into our dream house first.’
```
**源文 ch54:[4909,5044]**
```
‘I want to be with you whether we ever have children or not. I don’t care whether I have an heir.
The National Trust can have the lot.’
```
**md L14（导航·人物弧线）**
> 凯厄斯在候诊室里把戒指盒捏在手里…；他从「要不要再试一次」退到「以后再说」，并把「有没有继承人」这份家族执念整个让了出去；

**为什么算阻断**：导航把这两处**原文措辞**当成本章人物弧线的两根支柱（"从…退到…"），但精读 8 个块里**没有任何一块**引它们、
分析它们（`grep 'try again' / 'National Trust' / 'heir' ch54*.md` → 只在导航 L14 与词汇表例句命中，**无引语块**）。
按《创建卡》§0②「分析里出现的每个人名/动作/关系，都必须在这段引语里」——这里是反过来的：**导航做了断言，精读层没有证据块**。
「The National Trust can have the lot.」还是全章最具主题承载力的一句（把「继承／遗产」这条全书主线在末章一次性交割）。

**修法**：原句 6 之后的引语区间（[4513,5181]）补 1–2 块，或把原句 6 的引语扩到含这三处。

---

### D-3 ｜提示｜三处只被导航一笔带过、无引语承载的节拍

| 缺什么 | 源文区间 | md 现状 |
|---|---|---|
| 婴儿房主题「Woodland animals… squirrels and acorns and little foxes」＋沙发蓝／绿条纹 | [690,1836] | 仅导航 L13「婴儿房主题与沙发颜色」、L15「沙发条纹」提词；无引语块 |
| 「Ten to twenty per cent of pregnancies. Most are a one-off.」 | [4553,4765] | 仅导航 L13「统计数字」＋总结 L144「一组统计数字」；无引语块 |
| Hampton 招揽实质：「How about being the government instead.」／「Call Hunderby. There’s a safe seat for you.」／姐姐的 tragedy 与 special unit | [8066,8107]、[8470,8570]、[9503,9625] | 仅导航 L11「要他去做官」、L13「政治招揽」；L95 回顾式点到「二战后秩序、人工智能、气候与俄罗斯中国」但不在引语内 |

**为什么只算提示**：三处都有导航／总结层面的概括性提及（不是凭空编造），且本章的引语覆盖率与本书中位持平，
不构成「键控节拍被丢弃」；但读者要看到 Hampton 到底要他做什么、统计数字怎么说的，只能翻回原文。

---

### D-4 ｜提示｜「You don’t need to decide right now.」（三个处理选项尚未决定）未被提及

**源文 ch54:[3010,3047]** `‘You don’t need to decide right now.’`
**md**：grep `decide` → 仅原句 4 的引语含 `options`，无「本章未作决定」这一事实的交代。
**注**：md **没有**越权断言「处理结果如何」，所以这不是错；只是末章把「选择」悬置了这一事实没有进入视野（与 D-1 同源）。

---

## 二、编（md 有、原文无）

### C-1 ｜阻断｜「六周后」与「分部「SIX WEEKS LATER」」——本章与全书语料均无此物

**md L11（导航·一句话概括）**
> **一句话概括**：**六周后**的十二周产检里，…
**md L15（导航·叙事手法）**
> **叙事手法**：分部「**SIX WEEKS LATER**」里，先用琐事铺满候诊室…
**md L144（一句话总结）**
> **六周后**的产检里，医生宣布「这里没有胎心」…

**源文核对**
1. 本章源文 ch54:[0,11624] 全文 grep `SIX` / `weeks later` / `six weeks` ＝ **0 命中**（本章只有 `twelve-week scan`、`nine weeks`、`ten to twenty per cent`、`1997`、`two more years` 五个数字）。
2. 全书 54 个 `text/chNN_NN.txt` grep `WEEKS LATER` ＝ **0 命中**；逐文件首行清单显示 54 个提取件全是「章号 ＋ 地名式章题」（ch01 *The Horatio Combe Institute…* … ch54 *The Whittington Hospital*），**没有任何分部／分卷页**。
3. ch53 结尾即本案收束处，且末句是「We've had the date for the twelve-week scan come through.」（`text/ch53_53.txt:74`）⇒ ch53 与 ch54 **紧接**，中间无「六周」标记。
4. ch20 原文还写明「you wait for the twelve-week scan because most miscarriages happen earlier than that」（`text/ch20_20.txt:26`），全书唯一提到孕周的地方是「十二周」，**没有「六周」这个时间标记**。

**为什么算阻断**：md 以「**分部**」这一体裁术语指认一个**带英文标题的书中分部**，而该分部在权威语料中不存在——
这不是推断失准，是**指认了一个不存在的物**。且它违反本章专项第 ③ 条（末章只允许写本章写到的；分析层不得用别章／书级信息替本章下结论）：
「六周」既非本章所写，也非他章所写。
**同一断言已扩散到书级三篇（不在本次改动范围，仅记录）**：`00_概述.md:38`、`00_情感节点.md:118`、`00_金句精选.md:322`。

**给作者的一次自证机会**：若 epub 里确有被 `extract_chapters.py` 丢弃的短分部页（该脚本会丢弃 <600 字符且无 nav 条目的页），
请出示该页；届时本条改判「假红」。**在没有出示之前，按阻断处理。**

---

### C-2 ｜提示｜「第一次约会时**没去成**的那家意大利餐厅」——原文只说「tried to go to」

**源文 ch54:[47,687]**
```
He had booked dinner for later that evening at the Italian restaurant they’d tried to go to
on their first date.
```
**md L21（中文理解）**
> 他还在他们第一次约会时**没去成**的那家意大利餐厅订好了当晚的位子。
**md L25（为什么这样写）**
> 求婚、第一次约会想去却**没去成**的餐厅、婴儿房、沙发。

**为什么只算提示**：`tried to go to`（想／试着去）并未断言「最终没去成」；md 把它坐实为「没去成」。属**措辞过强**，非编造情节。

---

## 三、错（两边都有但不一致）

### E-1 ｜阻断｜「凯莉开口的第一句是道歉」——与本章原文及 md 自己的引语都矛盾（三处）

**md L11（导航·一句话概括）**
> …回程的出租车上两人一句话没说，**进了门她开口的第一句是「对不起」**…
**md L75（原句 6·为什么这样写）**
> **整章里**她说的第一句完整的话不是关于胎儿，而是道歉；
**md L144（一句话总结）**
> 医生宣布「这里没有胎心」，**凯莉开口的第一句却是道歉**；

**源文 ch54:[690,1836]**（凯莉在候诊室已多次开口）
```
‘Blue or green stripes?’ … ‘Really?’ … ‘I think I like the green more.’ …
‘Woodland animals. That room looks out over the woods …’ … ‘That’s me,’ Callie said, standing up.
```
**源文 ch54:[4055,4097]**（到家后她的第一句——**正是 md 自己引在原句 6 的那句**）
```
‘Yes, please.’ Callie sat up. ‘I’m sorry.’
```
**为什么算阻断**：三重矛盾——① 「整章里」是错的，凯莉在候诊室已说过至少 8 句；② 「进了门她开口的第一句」是错的，
到家后她先说的是 `‘Yes, please.’`，`‘I’m sorry.’` 在其后；③ md 自己在 L69 把两句并排引了出来，
L75 却说「第一句……是道歉」。**同一份文件内部自相矛盾**，且 L144 把这条错误结论升格为全章一句话总结。

**修法**：统一改成「回到家的那段对话里，她开口的第一句是道歉」或「她在家说的第一句完整的话不是关于胎儿，而是道歉」——
但「整章里」这个范围词必须删（`Callie` 在候诊室的台词是本章的实质内容，不该被断言抹掉）。

---

### E-2 ｜阻断｜「他几天前刚为孩子**买过东西**」——原文是「browsing」，且与本块中文理解自相矛盾

**源文 ch54:[3300,3983]**
```
… when his scrolling was interrupted by an ad for baby clothes. He’d been browsing online the other day.
```
**md L65（原句 5·为什么这样写）**
> 婴儿衣物广告偏偏插在校园枪击案的报道之间，是全章刺眼的一处错位：**他几天前刚为孩子买过东西**，世界却在别处继续塌陷。
**md L61（同块·中文理解）**
> …滑动屏幕却被一条婴儿衣物广告打断——**他前几天刚在网上搜过婴儿用品**。

**为什么算阻断**：原文是 `browsing online`（浏览／逛），md 升格为「**买过**东西」——一个原文没有的**行为断言**；
而且**同一块内**的中文理解写的是「搜过婴儿用品」，两处口径不一致。按「拿不准的事实，grep 一次原文」，此处应以原文为准。
**修法**：「买过」→「逛过／看过」。

---

### E-3 ｜提示｜导航「视角」对凯莉的可知性说过头，与本章原句 3 矛盾

**md L12（导航·视角）**
> 第三人称限知，主要贴着凯厄斯的动作与念头走——摸戒指盒、订位、盯着钟、**倒牛奶**、刷手机、走在街上；
> **凯莉的状态只能从她自己的话和身体反应里读出来**：点头、把手放在肚子上又缩回、先道歉。
**源文 ch54:[2432,2593]**（原句 3，本章唯一一段贴着凯莉内心的文字）
```
Callie nodded. She wanted to cry but there was nothing. The void where a tiny possibility
had been a moment before had hollowed her out.
```
**问题**：「**只能**从她自己的话和身体反应里读出来」被本章唯一一段**凯莉内视角**（`She wanted to cry but there was nothing`）证伪；
另「倒牛奶」属原句 6 引语之外的动作（见 `4-correspondence.md` 第 6 块）。「主要贴着凯厄斯」这句本身成立（有限定词），
不必动；「只能」需改。

---

### E-4 ｜提示｜原句 2「医生只说了两句」与该块引语自相矛盾，且「没有铺垫」与本章描写相抵

**md L31（原句 2·中文理解）**
> 医生**只说了两句**：非常抱歉，福斯特小姐，这里没有胎心。
**md L35（原句 2·为什么这样写）**
> 坏消息被压成**两句**公事…作者**没有让医生先铺垫检查过程**、先做心理准备，直接把结论摆到读者眼前；
**md 自己引的原文 ch54:[2377,2429]**
```
‘I’m very sorry, Miss Foster. There’s no heartbeat.’
```
**问题**：① 该块引语是**一句**（逗号连接），md 自己的引语不支持「两句」；② 宣告之前本章确有场景铺垫——
涂耦合剂、房间安静、「the consultant’s sharp intake of breath」、「The consultant tried a different angle. Another breath.」（ch54:[1839,2374]），
「没有铺垫检查过程」只在**医生没有口头铺垫**这一层成立，md 的写法覆盖了场景层。
**修法**：「两句」→「一句」（或改成「两段」）；「没有让医生先铺垫」限定为「医生没有口头铺垫／没有先安慰」。

---

## 四、本章专项四问的结论

| 专项 | 结论 |
|---|---|
| ① 结局断言（死因／关系／数字）是否逐字一致 | **数字一致**（十二周、九周、十到二十个百分点 均逐字）；**关系一致**；**死因说明整段缺失**（D-1）——md 没有编造死因，但也没写 |
| ② 人物结局有无超出本章原文 | **无**。md 未断言任何人的死因、结局或去向超出本章；Callie 的稽留流产、Caius 拒 Hampton、Bridget 丧子史均与本章原文相合 |
| ③ 导航／总结对全书结局的概括是否越权 | **越权 1 处**（C-1「六周后／SIX WEEKS LATER」）；另「凯莉第一句是道歉」是把**别的**对白当本章结论（E-1） |
| ④ 引语是否截短或跨段拼接 | **跨段拼接 0 处**（8 条引语均为单一连续段，无省略号，`verify_fragments_indep` 全书 840 片段 0 MISS）；**截短 1 处**（原句 6，见 `4-correspondence.md`） |

---

## 五、三张单子汇总

| 单子 | 阻断 | 提示 | 合计 |
|---|---|---|---|
| 漏 | 2（D-1, D-2） | 2（D-3, D-4） | 4 |
| 编 | 1（C-1） | 1（C-2） | 2 |
| 错 | 2（E-1, E-2） | 2（E-3, E-4） | 4 |

**阻断型合计 5 条（C-1、D-1、D-2、E-1、E-2）**，另加对应组阻断 1 条（原句 6 截短，见 `4-verdict.md`）＝ **全章阻断型 6 条**。
