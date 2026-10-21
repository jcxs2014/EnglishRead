# R3 对账 · ch52《A Fatal Legacy》

- 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch52 willow bell is arrested.md`
- 唯一权威源：`text/ch52_52.txt`（19,016 字符 / 481 行）
- 读取顺序：**先只读 text（已落盘 `1-suread.json`），之后才开 md**
- 偏移约定：`chNN:偏移` = 源文件 python 字符偏移（0 起、半开区间）；md 行号用 `md:行号`
- 档位：**阻断** / 提示 / 假红 / 跳过

---

## 摘要

| 单子 | 条数 | 其中阻断 |
|---|---|---|
| 漏（素读有、md 无） | 4 | 1 |
| 编（md 有、原文无） | 7 | 3 |
| 错（两边都有但不一致） | 8（另 1 行“错-3”是编-2 的交叉引用，不另计） | 1 |
| **合计** | **19（+1 交叉引用）** | **5** |

阻断型 5 条：**漏-1**（结局定性缺失）· **编-1**（雕像＝墓室骸骨）· **编-2**（Andy 的家族归属，2 处）· **编-3**（the label＝博物馆标签）· **错-1**（“公开场合撒谎”方向反 + 与本章总结自相矛盾）。

引语层：**10 条引语全部为源文的连续子串**（`t.find(q) >= 0`），逐字 10/10；无跨段/跨话轮缝合（详见 `4-verdict.md` 与 `4-correspondence.md`）。

---

## 一、漏（素读有、md 无）

### 漏-1【阻断】全书收网章的结局定性（指纹归属 + 罪名），分析层与总结层零覆盖

- **素读原文（ch52:18764–19016，章末最后一节）**
  > ch52:18764 `the partial fingerprints at the Institute are his`
  > ch52:18890 `she is definitely getting two accounts of murder and one of manslaughter. She won’t see daylight until she’s in her sixties.`
  > ch52:18379 `‘She did it all,’ Matt said. ‘Andy’s confessed to Scott’s death and to being there for Jimmy’s out of guilt, but none of the causes of death were accurate. He knew about the deaths though. He’s trying to take the blame for her.’`
- **md 侧**
  - md:15 导航·叙事手法只有一句概括：`结尾用三段对话（认罪／顶罪／拒谈）收束，把最终定性交给检方`
  - md:168 一句话总结**止于父子走向地铁**（`而 Caius 却在走向地铁的路上把整条作案链……讲给父亲听`），全章最后 5,000 余字符（Andy 受审 / 走廊定罪）**没有进入任何一块、也没有进入总结**
  - 结论性事实只以**未解读的词汇表例句**形式存在：md:134 `manslaughter | 过失杀人；误杀罪 | The CPS will decide… two accounts of murder and one of manslaughter.`；md:162 `fingerprints | 指纹 | Doesn’t matter really, now we’ve confirmed that the partial fingerprints at the Institute are his`
- **判定**：md 未写明取舍理由；章末是全书的**法律定性收口**（Willow 两项谋杀 + 一项误杀；研究所部分指纹转指 Andy），且本章 10 块全部落在前半章（引语区间 ch52:36–10828，只覆盖全章 57%），后 43%（含两处 `* * *` 分隔线，ch52:16499 / ch52:18201）零块。判**阻断（漏）**。

### 漏-2【提示】Margot Bourne 全章零出现

- **原文**：ch52:3986 `Call me Margot`；ch52:4153 `‘I guess that’s the end of the museum then.’`；ch52:4620 `‘The neighbour. She wanted to buy the Institute so she could extend.’`；ch52:12474 段 Caius 长推理：`Digby her boss is going to sell the Institute, possibly to his neighbour Margot Bourne – the woman who grabbed my arm.`
- **md 侧**：`grep -o "Margot\|Bourne" ch52*.md` → **0 命中**。导航、五块、总结、词汇表均无。
- **判定**：她在本章承担“买下研究所的邻居 + Caius 推理链的一环”，属**铺垫性关键人物**，但本章无转折由她完成。判**提示（漏·非阻断）**。

### 漏-3【提示】父子归家整段（ch52:11093–16200，约占全章 1/4）分析层零块覆盖

- **原文**：ch52:12143 `‘That historian, he’s seeing the girl.’` 起，至 ch52:15489 `…she posted a missing diary, a vital piece of evidence, to her disguised as a fan letter so we’d find it at her house.` 止——Caius 对父亲完整复述作案链（假 Isolde / LRB 交友广告 / 毒沙拉 / PO Box / 栽赃 Jen）。
- **md 侧**：md:12 导航·视角只写 `前半段…后半段转为警局里…`，未提这段；md:14 人物弧线与 md:168 总结各用一句话概括（「把整条作案链在父亲面前复述一遍」）。
- **判定**：总结层已覆盖事件本身，缺的是精读层的一块。判**提示（漏·非阻断）**。

### 漏-4【提示】广场闲笔（订婚戒指 / 全脸面罩，ch52:598–1710）未被任何块选取

- **原文**：ch52:598 `‘I found out about the engagement rings, by the way.’`；ch52:1456 `‘Full face masks. They can cope with everything, including asbestos. One each for you, me and Matt…’`
- **md 侧**：无对应块（md:15 导航·叙事手法提到「全脸面罩」，仅作为闲笔标签）。
- **判定**：属氛围性闲笔，选与不选均可，判**提示（不阻断）**。

---

## 二、编（md 有、原文无 / 无依据）

### 编-1【阻断】「这尊纪念碑所纪念的，正是本章挖出来的那些尸骨」——与全书语料矛盾

- **md 侧（md:25，原句 1 · 为什么这样写）**
  > `而父子俩并排坐在广场上，画面和谋杀案里那些被陈列的遗物遥遥相对，读者读到最后会发现，这尊纪念碑所纪念的，正是本章挖出来的那些尸骨。`
- **原文侧**
  - ch52:36 `Caius and Marcus were sitting in front of the feminist blob statue in memory of the mystic nun burnt at the stake.`
  - ch48:12517 `The nun who was burnt for heresy during the Reformation.` ／ ch48:12574 `The one with the blob statue in the middle of the square.` —— 雕像纪念的是 **Alice de Burge**
  - ch33:10985 `One of the priory’s most infamous inhabitants was Alice de Burge.` ／ ch33:11333 `Alice de Burge was burnt at the stake for heresy in 1532. All known copies of ‘Her Visions’ were set alight with her.`
  - ch51:2546 `it’s an old priory that the tunnel probably leads to a crypt and a load of dead nuns`；ch52:6409 `Skeletal remains were piled high on stone shelves.`
- **判定**：被烧死的 Alice de Burge（1532）与墓室石架上的埋葬遗骸**不是同一批人**（焚 vs 葬）；原文本章从未把雕像与墓室骸骨等同。md 以“读者读到最后会发现”的确定语气断言了一个源文不存在的关系。判**阻断（编）**。

### 编-2【阻断】把 Caius/Marcus 一家的 priest holes 记到 Andy 头上（2 处）

- **md 侧**
  - md:35（原句 2 · 为什么这样写）：`而后半句的“boring”其实是 Caius 的误判：这个人马上会说出关于他自己家族的那段要紧历史。`
  - md:65（原句 5 · 为什么这样写）：`Andy 的“融化”是他这个人第一次露出的真相——他不是来看热闹的，他是来看自己家族藏起来的东西的`
- **原文侧**
  - ch52:7459 `‘Your family were Recusants.’`（Andy 对 Marcus 说）
  - ch52:7602 `Your house is riddled with priest hides.`（Andy 对 Marcus 说，“Your house”＝Marcus/Caius 的宅子）
  - ch52:2382 `I’ve written six articles about the history of these hundred acres` —— Andy 是**这一百英亩的外来史学家**，与埋藏物无亲属关系
- **判定**：Andy 讲的是**对话对象（Marcus 一家）的家族史**，不是他自己家。两处都把「他自己家族」写成 Andy 的。判**阻断（错·人物归属）**（同时计入第三节「错-3」）。

### 编-3【阻断】导航把「the label」释为「博物馆标签」——实为唱片厂牌

- **md 侧（md:13，导航·线索结构）**
  > `→ 报纸上关于博物馆标签的报道与 DJ Sonikk 的访谈，把公众视线与调查推进到同一天。`
- **原文侧**
  - ch52:6002 `‘Have you seen that the label has been taking a lot of flak in the press? DJ Sonikk did another interview.’`
  - ch23:6014 `When the label had first approached him about working on Eulalia’s second album…`；ch23:355 `the label think`；ch27:161 `the label’s plan for me to perform in them`；ch46:171 `she’s probably… the label`（`Mel sent a creepy man from the label`）
- **判定**：全语料里 `the label` 一律指 **Mel/Eulalia 的唱片厂牌**（DJ Sonikk 即该厂牌的制作人），与本博物馆无关；md 释为「博物馆标签」属凭空所指。判**阻断（编）**。

### 编-4【提示】「画在墙上的伊甸园之蛇」

- md:11 导航：`机器人照出的不只是骸骨，还有画在墙上的伊甸园之蛇`
- 原文 ch52:7197 `‘What is all that?’ Amy asked, peering at a painting. ‘The worms. That drawing is, what, a snake?’`；ch52:7299 `‘It’s the snake in the Garden of Eden. That’s what Horatio meant in his journal,’ Andy said.`
- 判定：原文只说是“一幅画”（在机器人镜头画面里被看到），无“画在墙上”。判**提示**。

### 编-5【提示】「当场被铐走」

- md:14 导航·人物弧线：`Willow 从“实习生”变成当场被铐走的人`
- 原文 ch52:10205 `‘Willow Bell, I am arresting you…’`；ch52:10472 `Amy watched from the kerb as Andy and Willow were led away.`
- 判定：原文只有“被带走”，无手铐。判**提示**。

### 编-6【提示】「把公众视线与调查推进到同一天」

- md:13 导航：`…把公众视线与调查推进到同一天`
- 原文 ch52:6002 句中并无“推进调查”的因果；报道内容是唱片厂牌挨骂。
- 判定：凭空因果。判**提示**。

### 编-7【提示】「谋杀案里那些被陈列的遗物」

- md:25 `画面和谋杀案里那些被陈列的遗物遥遥相对`
- 原文 ch52:6409 `Skeletal remains were piled high on stone shelves. Body on top of body on top of body.`（石架上堆放，非陈列展品）
- 判定：措辞失真但不影响事实链。判**提示**。

---

## 三、错（两边都有但不一致）

### 错-1【阻断】原句 7「她在公开场合撒了一个谎」与本章一句话总结自相矛盾，且与源文方向相反

- **md 侧**
  - md:87（原句 7 · 读者视角提示）：`Willow 之所以露馅，是因为她在公开场合撒了一个谎，帖子替她记着账。`
  - md:168（一句话总结）：`Amy 用一条三个月前的 Instagram 帖子戳穿 Willow **临时编造的论文题目**`
- **原文侧**
  - ch52:9659 `‘What’s your dissertation on, Willow?’ Matt asked.`
  - ch52:9758 `She stood looking at him, frozen on the spot. ‘The Hundred Years War.’`（室内答案＝临时编造，她当场僵住）
  - ch52:9805 `‘Is it?’ Amy asked. ‘I thought it was a feminist history of herbal remedies used in England between 1300 and 1500? That’s what you said on an Instagram post three months ago.’`
- **判定**：源文里 **Instagram 帖才是她真实的那一份**（Amy 靠“公开版 vs 口头版”比对揭穿她），**室内的 “The Hundred Years War” 才是临时编造**。md 的读者视角提示把谎言的位置说反，且与本章自己的总结互相打架。判**阻断（错·因果/事实方向）**。

### 错-2【提示】原句 2「读者此时已经知道他自称都铎史专家」——时序

- md:35 `读者此时已经知道他自称都铎史专家，却还不知道他与 Willow 的关系`
- 原文：引语 ch52:1713–1968 结束于 `…or if he was just boring.`；Andy 自称都铎专家在 **ch52:2350** `I’ve written six articles about the history of these hundred acres`（在引语之后约 640 字符）。
- 且同块末句自相矛盾：md:37 `他后面所有的自信、所有的科普，都会在警局里变成他认罪时的开场白`（“后面才有”）。
- 判定：措辞时序错（“此时”若指阅读到该引语时）。判**提示**。

### 错-3【阻断·与编-2 同一事实的两处表述】Andy 的家族归属

见「编-2」，此处只补一句：md 的**正确写法应是**“这个人马上会说出关于**对话对象（Marcus）一家**的那段要紧历史”。判**阻断**（计入阻断总数一次，此处不重复计条）。

### 错-4【提示】原句 9「这一句之后接的分节符里」

- md:105 `而这一句之后接的分节符里，她一句话都没有说，沉默本身成了她的第一次“陈述”。`
- 原文：引语止于 ch52:10367；下一个 `* * *` 在 **ch52:16499**，中间隔着约 4,900 字符的父子归家戏；且 Willow 在 ch52:10204 之前还说过话（ch52:9758 `‘The Hundred Years War.’`、ch52:9590 `‘You called me about my brooch? Can I get it?’`）。
- 判定：两种读法（“下一个分隔符之后”“这句话之后的这一节”）下“被捕后一言不发”都成立，属**措辞歧义**；判**提示**（不判红）。

### 错-5【提示】原句 1「本身就是全书的开篇」

- md:25 `一章从一座看不懂的雕像开始，本身就是全书的开篇`
- 原文：`blob` 全语料只出现在 ch31:1767 / ch48:12574 / ch52:36，**ch01 开场是研究所里的 Digby**（ch01:71 `Digby Combe-Watson is sprawled out on the antique rug…`）——雕像不在全书开头。
- 但本书每章带**场次副标题**（ch01 `The Horatio Combe Institute, Priory Square, Camden`；ch52 `Priory Square`），若“全书的开篇”指的是**节标题「Priory Square」也是全书首章的场次名**，则属合法的分部/场次结构信息。
- 判定：两种读法一错一合法，无法从文本判定作者所指；判**提示（措辞歧义，需作者澄清）**。

### 错-6【提示】原句 8「年轻警探」

- md:95 `把追赶写成一个年轻警探凭本能做出的动作`
- 原文本章未交代 Amy 年龄（ch52 全章无年龄信息）。
- 判定：合理推断，非事实断言。判**提示（不判红）**。

### 错-7【提示】导航·视角「前半段…后半段转为警局里…」

- md:12 `前半段第三人称限知贴着 Caius（父亲 Marcus 在旁充当对照与吐槽者），后半段转为警局里 Andy、Willow、Amy、Matt、Robbie 各自的对话，视角跟着说话人来回切。`
- 原文：ch52:11093–16200（占全章约 1/4）是**父子上街回家、仍是 Caius 限知**；警局段里 Willow **全程未开口**（ch52:18212 `‘Willow’s refusing to talk,’ Amy said`）。
- 判定：视角切换点画错、且把未发言者列入“各自的对话”。判**提示**。

### 错-8【提示】原句 10 读者视角·因果

- md:117 `也就是说结论不是靠抓人现场问出来的，是靠从面包店收来的那批垃圾慢慢拼出来的`
- 原文：逮捕的**触发点**是 Amy 当场用 Instagram 帖子对质（ch52:9805）＋ Willow 转身要跑（ch52:10099）；纸杯是**事后佐证**（ch52:10593 `Forensics found the paper cup late last night…`）。
- 判定：把佐证说成“结论”，因果偏斜。判**提示**。

### 错-9【提示】原句 6「紧接着作者用‘她的时机无可挑剔’点破」——源文该句在引语**之前**

- md:75 `…紧接着作者用“她的时机无可挑剔”点破了这一点。`
- 原文 ch52:9048 `‘Hello,’ Caius said, turning around. Her timing was immaculate.` —— 该句位于引语（ch52:9077）**之前** 29 字符，不是“紧接着”（其后）。
- 判定：语序措辞小瑕，论证实质不受影响。判**提示**。

---

## 四、核对通过（不列缺陷，仅备案）

- **10 条引语逐字**：全部为源文连续子串（`t.find(q) >= 0`），偏移 36 / 1713 / 5127 / 6319 / 6894 / 9077 / 9784 / 10099 / 10204 / 10593。
- **引语 9 的尾部 `…`**：源文 ch52:10204 行尾自带 `…`，md 照录，**不是**跨段缝合；机器 `2-machine.json` 把该尾段归一化成空串（`norm()` 去引号）后 `pos=0` 恒真，属**工具口径空转**，不影响结论（已另行用精确子串法复核）。
- **词汇表 30 条**：每条例句在本章源文中 `count == 1`（逐条 grep -F 复核），无手写编造例句；档位无注水（`infoladen` / `Recusants` / `priest hides` 归 ⭐⭐⭐ 合理）。
- **数字断言**：md 引用的「三条隧道」相关表述、二十年、三个月前、1300–1500、十年、十点、一具头骨等，均与源文一致（详见 `1-suread.json` 的 numbers_and_dates）。
- **逮捕对象**：md:99 `for the murders of Digby Combe-Watson and Scott Brown` = ch52:10205，**一致**（收网章最容易错的一项，未错）。
- **指纹归属**：md:111 `杯子上有 Willow 的指纹` = ch52:10593 `It had Willow’s prints on it`，**一致**；md:162 例句里研究所部分指纹属 Andy = ch52:18764，**一致**。
