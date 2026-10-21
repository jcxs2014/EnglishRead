# 3-diff.md · ch25《The Police Station》对账（漏 / 编 / 错）

> 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch25 scott brown goes missing.md`
> 权威源：`text/ch25_25.txt`（245 行 / 10177 字符）；md 快照 sha256 `743f937f9495db3dbaf4afc6905c41477265d5af291ac71d46d6e18303e911ce`（HEAD `a363a8883`）
> 顺序遵守：R1 素读（只读 text/）→ 落盘 `1-suread.json` → 才开 md。

---

## 一、漏（素读有、md 无）

### 漏 1【阻断】Scott「先失踪，警方才上门」这一前提层整层缺失

原文（逐字）：

- `text/ch25_25.txt:108` `‘I knew it when Scott didn’t come to work yesterday and again today. I hoped he was sick maybe and forgot to call.’`
- `text/ch25_25.txt:114` `‘Yeah, very. He’s never been late before. He’s very conscientious. Is he in trouble?’`
- `text/ch25_25.txt:120` `‘Yeah,’ Jodie said, opening her laptop and retrieving the details. She wrote them down and handed them to Caius.`

md 侧：全文检索「迟到」0、「失踪」0、「地址」0；「上班」1 次且在块 5 分析里作推断（`md:51` `……每天上班路过`），不是 Jodie 说的缺勤。
md 的叙述链是「面包店问出他叫斯科特·布朗 → **随即**在恩菲尔德…见到他的尸体」（`md:11`、`md:120`），中间缺「他昨天与今天都没来上班、他从不迟到 → 警方意识到不对 → 拿到住址上门」这一环。
影响：章题即「goes missing」，md 全文没有出现「失踪」；读者拿不到「警方为何去他公寓」的因果，也拿不到 Jodie 这个唯一提供「他从不迟到、非常尽职」这一反常基准的人。

### 漏 2【阻断】死因与 Barry 的法医判断，分析层零覆盖

原文（逐字）：

- `text/ch25_25.txt:194` `‘Stabbed in the gut. I’d say they nicked his liver. Not a nice way to go. He would’ve gone into shock quite quickly though,’ Barry said, looking down at the body in front of him. ‘One stab wound. The killer thought they’d done enough.’`
- `text/ch25_25.txt:197` `‘Professional kill?’`
- `text/ch25_25.txt:200` `‘Oh no, I should say not,’ Barry said, standing back as the body bag was being zipped up. ‘They were lucky. A professional would’ve gone straight for an artery like the carotid. No one would survive that.’`

md 侧：检索「法医」0、「巴里」0、「肝」0、「休克」0、「职业」0；「刺」1 次，出现在 `md:103` 词汇表 `carotid | 颈动脉 | A professional would’ve gone straight for an artery like the carotid.`（仅为无释义的例句）。
即：Scott 怎么死的（腹部一刀、刺到肝、快速休克、只有一处刺伤）在 md 里**一句没有**；「不是职业杀手」这个结论只以两条孤立词汇例句（`body bag` / `carotid`）出现，中文理解／为什么这样写都未引用。
影响：本章后半的推理（模式识别 → 「她专挑孤独男人下手」）建立在 Barry 的「非职业」判断上，md 把结论（孤独的男人）留住了，把证据层丢了。

### 漏 3【提示】Caius 的核心因果假设——Scott 因「送信到 P.O. Box 知道太多」而被灭口

原文 `text/ch25_25.txt:224`：
`‘He’s just gone through a break-up,’ Caius said to Amy as she re-entered the room. ‘His ex moved out and took half the furniture with them. There’s no dining room table but the marks where one had rested on the carpet are there. I’m worried, Amy. They either killed Digby for some yet unknown, awful but logical reason and then killed Scott because he knows too much about them from delivering the letters to the PO Box or …’`

md 侧：检索「信箱」0、「P.O. Box」0、「知道太多」0。这是本章唯一把「两桩命案」串成一条因果链的句子（也是「送 P.O. Box 信件」这条线的唯一落点）。

### 漏 4【提示】章末的推问链（Priory Square 猎场 / Is she spiralling? / 「I'd like to be her friend」）

原文逐字：
- `text/ch25_25.txt:239` `‘And she has a hunting ground around Priory Square.’`
- `text/ch25_25.txt:242` `Caius stared down at the indent the old dining room table had made in the carpet. ‘Is she spiralling?’`
- `text/ch25_25.txt:245` `‘She sounds cool. I’d like to be her friend,’ Amy said.`

md 侧：「失控」0、「spiralling」0、「I'd like to be her friend」0、「Priory Square」0；只有 `md:15` 一句 `结尾把推测停在「她有猎场」这样的轻句子上，疑问越轻，落差越大`——**概括了「猎场」，但没有「Is she spiralling?」这一具体追问，也没有 Amy 那句把凶手当朋友的冷收尾**（那才是本章真正的落差点）。

### 漏 5【提示】Amy 的投毒焦虑与「菠菜是不是我以为的那个」

原文 `text/ch25_25.txt:185`：
`‘Starving, but the point still stands.’ She hadn’t eaten much of her baguette. She’d kept thinking about poisonings, and wondered if the spinach in hers was what she thought it was.`

md 侧：检索「投毒」0、「毒」0。`md:14` 只写「艾米在面包之间保持清醒」，没有落到原文这条具体动作（面包没吃几口 / 怀疑菠菜）。
另 `text/ch25_25.txt:179` `‘Regulate your own emotions and behaviour, bitch.’` 也未进 md。

### 漏 6【提示】Jodie 的身份：md 写「女店主」，原文是共同所有人（co-owner）

原文 `text/ch25_25.txt:90`：`She introduced herself as Jodie, the co-owner of the bakery.`
md `md:11`：`他们找到面包店女店主朱迪`。
「店主」是中文压缩，严格身份是「共同所有人／合伙人」；另 `md:11` 漏掉 Jodie 交地址这一动作。

---

## 二、编（md 有、原文无）

### 编 1【提示】块 7 读者视角提示：「艾米的依据是**香味**和罂粟籽」——原文无「香味」

md `md:66`：`注意那句迟疑：艾米的依据是香味和罂粟籽，不是记忆；同一段里还有"始终没人动过"的那只面包卷。`
原文 `text/ch25_25.txt:135`：`She looked down at her honey-roasted goat’s cheese, sundried tomato, spinach and tapenade baguette uncertainly.` —— 艾米是**低头看**自己那份法棍，原文没有「闻／香味」。
取证（本章唯一一处 smell 是尸臭）：
`/usr/bin/grep -nE "smell|scent|aroma" text/ch25_25.txt` → 仅 `161:Caius waited to the side as the front door to Scott’s flat was broken down. They smelled him before they saw him.`（退出码 0，1 命中）
`/usr/bin/grep -niE "poppy" text/ch25_25.txt` → 仅 135 行 1 命中（退出码 0）

### 编 2【提示】块 5 为什么这样写：「他就住在附近、每天上班路过」——原文只给到「本地人」与「他是店员」

md `md:51`：`……他之所以天天顺路进邮局，是因为他就住在附近、每天上班路过。`
原文只有 `text/ch25_25.txt:59` `‘So he’s local.’` 与 `text/ch25_25.txt:62`（他穿店员 T 恤＝他在店里上班）。
「住在附近」「上班路过（顺路进邮局）」是推断，被写成陈述句；「递次走进邮局」这类因果在原文未成立。

### 编 3【提示】块 4 读者视角提示：「它能接上的店名在本区只有一个」——原文无唯一性断言

md `md:45`：`把这三个字母记牢：它能接上的店名在本区只有一个，而那个店名会牵出一整间工作场所。`
原文 `text/ch25_25.txt:56` 只是艾米认出 Purple Toad Bakery，未断言该区只有一家以 “ery” 结尾的店。

### 编 4【提示】块 2 读者视角提示：「为什么不能寄给收信人本人」——引语外的前提

md `md:31`：`这封信是整个监控戏的支点：谁寄、寄给谁、为什么不能寄给收信人本人。`
原文在本章未断言信寄不到本人；与之相关的只有 `text/ch25_25.txt:224` 里 Caius 的**推测**（信被送到 P.O. Box）与 `:167` Amy 的问句（Scott 怎么知道真正的 Isolde）。
（写成读者追问尚可，但「不能」是陈述式预设。）

### 编 5【提示】「整条樱草山／整条街」与原文人口口径不合

md `md:13` `整条樱草山都在用这种装法棍的袋子`、`md:49` `她说整条樱草山的人都在拿这种袋子装法棍`、`md:51` `作者借艾米"认得整条街"的口吻`、`md:52` `覆盖范围（整条街）`。
原文 `text/ch25_25.txt:56`：`Everyone in Primrose Hill was shuffling their baguettes around in them.` —— 是「樱草山的所有人」（区域人口），不是「一条街」。中文把区域压成街道，四处重复。

### 编 6【提示】「被搬空的家具」比原文重

md `md:13`：`再落到生活现场层（被搬空的家具、空相框、没动过的 Chablis、两只杯子、一枚乐观的安全套）`
原文 `text/ch25_25.txt:224`：`His ex moved out and took half the furniture with them.` —— 是搬走**一半**家具；原文紧接着还特意说 `There’s no dining room table but the marks where one had rested on the carpet are there`（餐桌没了、压痕还在）。「搬空」过头。

### 编 7【已修·本轮观察期内的自造措辞】分部名「A WEDNESDAY IN MAY」

- 本审查开始时（14:35 前）`md:11` 写作 `在分部「A WEDNESDAY IN MAY」里`；`/usr/bin/grep -rn "WEDNESDAY" text/` → 退出码 1、0 命中（text/ 提取件不保留分部标题，故零命中**不能**直接当伪证）。
- 该措辞已被同一书目录的另一实例判为自造并于 `a363a8883`（2026-10-21 14:35:04，commit message 明确写「19 章分部名改回书内真实标题（A X IN MAY 是自造措辞）」）改回 `在分部「WEDNESDAY」里`。
- 现状：md 已是 `md:11` `在分部「WEDNESDAY」里` ⇒ **本条无需再改**，仅留档。

---

## 三、错（两边都有但不一致）

### 错 1【提示】块 1 中文理解与本章导航对「两个女人」频次口径自相矛盾

- md `md:11`（导航）：`两个女人各来两天`
- md `md:21`（块 1 中文理解）：`两个女人只在三天里的两天出现过`
- 原文 `text/ch25_25.txt:26`：`‘Two women both came in on two of the three days and one man came in on all three.’`

原文本身有歧义（「各来两天」／「同在两天出现」两读皆通）；md 内部两处各取一读，且导航取的是较贴合原文的读法、块 1 取的是另一读法。块 1 读者视角提示（`md:24`「两个女人只是偶尔露面」）两读都容得下，故未造成事实错误，但 md 内部口径不统一。

### 错 2【提示】块 8 中文理解把「might've too」译成「难以幸免」

- md `md:70`：`……可怜的斯科特带着他那枚乐观的安全套，看上去恐怕也难以幸免。`
- 原文 `text/ch25_25.txt:230`：`poor Scott with his hopeful condom looks like he might've too` —— `too` 承接前文 `Digby had a sexual interest in “fake Isolde”`，意思是「他恐怕**也对假伊索尔德有兴趣**」。
- 中文把「也有性兴趣」换成了「逃不掉／难以幸免」（死亡语义）。语义漂移方向与原文相反：原文说的是**欲望**，md 说的是**被害**。

### 错 3【提示】导航「艾米在面包之间保持清醒」在 md 内无对应引语／分析支撑

- md `md:14`：`艾米在面包之间保持清醒，她记得迪吉约会前买的那只撒着罂粟籽、始终没动过的面包卷`
- 原文里「保持清醒」的具体内容是 `:185`（面包没吃几口 / 一直想着投毒 / 怀疑菠菜）与 `:179`（`‘Regulate your own emotions and behaviour, bitch.’`），这两处 md 都没进（见漏 5）。块 7（`md:61`）引的是 `:135`，只覆盖「罂粟籽／没动过的面包卷」这一半。

---

## 四、对账小结

| 单子 | 条数 | 阻断 | 提示 | 已修 |
|---|---|---|---|---|
| 漏 | 6 | 2（漏 1、漏 2） | 4 | 0 |
| 编 | 7 | 0 | 6 | 1 |
| 错 | 3 | 0 | 3 | 0 |
| 合计 | 16 | **2** | 13 | 1 |

（另有形态组 0 偏离、逐字组 0 缺陷，详见 `4-verdict.md`。）
