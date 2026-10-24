# ch62 The Empty Orchestra — R3 差异 / R4 逐块

- md：`notes/books/novels/life-out-of-order-by-audrey-niffenegger/ch62 the empty orchestra.md`
- text：`notes/books/novels/life-out-of-order-by-audrey-niffenegger/text/ch62_the_empty_orchestra.txt`（335 行，三段拼贴）
- 素读底稿：`review/ch62/1-suread.json`；机器层：`review/ch62/2-machine.json`（rc=0, 8 块）
- 三个时点（逐字）：`:18`「Wednesday, January 30, 2069 (Oliver is 40, Madeline is 89)」／`:109`「Tuesday, October 15, 2041 (Oliver is 40, Zach is 40, Clare is 70, Beck is 65)」／`:290`「Tuesday, December 27, 2022 (Alba is 21, Zach is 22, Oliver is 40)」——md `:15` 写「三个日期倒着跳：二〇六九、二〇四一、二〇二二」，相符
- POV 标签（`/usr/bin/grep -nE "^(Oliver|Zach|Alba|Clare|Beck|Madeline):"`）：`:23 Oliver`／`:114 Oliver`／`:122 Zach`／`:218 Oliver`／`:235 Zach`／`:270 Oliver`／`:295 Oliver` —— md `:15`「靠 Oliver: 与 Zach: 的标签分界」成立

## R3-1 漏（素读有、md 无）

| # | 素读事实 | 原文（逐字 + 位置） | md 侧 | 判定 |
|---|---|---|---|---|
| L1 | 1980s 那场阁楼音乐会的**年龄错位**：他当时是「十几岁」，阿尔芭「五十多岁」，他觉得她令人发怵 | `:70`「Her cough reminds me of a concert Alba and I attended together a very long time ago, when I was a teenager. Alba was in her fifties, and I found her intimidating. It was winter in the 1980s, and the concert was in someone’s loft, a dreary, draughty, ramshackle place.」 | md 原句 4 的引语从「The piece they played was so extraordinary」起，把「他十几岁／她五十多岁」全跳过；总结 `:132` 只写「一场听不清的旧音乐会」 | **提示**（这是全书「时间旅行」最直观的一次亮相：同一个阿尔芭比他大三十多岁。缺这层，原句 4 的「她衣服空在座位上」就只是一个悬疑画面，读者不知道他当时面对的是哪个阿尔芭） |
| L2 | 黄房子床板下的笔记本：阿尔芭最后记的日期是 2041 年 10 月 14 日，她写自己从 9 月 7 日起就住在这里，没给理由；奥利弗读后想「她离开他了」 | `:228`「I remove the floorboard in Alba’s bedroom and consult our notebook. The last date Alba gives is October 14, 2041. She writes that she’s been living here in her present for weeks, since September 7, but she doesn’t give any reason, and I sit here on the floor with the notebook in my hands and think, she’s left him, and I am deeply sorry.」 | md 全章未提笔记本；`:228` 的「she’s left him」是奥利弗那句「我明白我对你做了什么」的**前因**，缺它，原句 7 的认罪显得无来由 | **提示**（它是本章唯一交代「阿尔芭什么时候走的、奥利弗怎么知道的」的段落，属情节信息而非细节；但不构成转折遗漏，故不阻断） |
| L3 | 冰箱里那瓶没开封的曼萨尼亚：阿尔芭爱喝的酒，看见它他就知道了 | `:246`「There’s an unopened bottle of Manzanilla in the fridge; Manzanilla is one of Alba’s favorite wines, and when I see it I know」 | md 未提 | 提示（氛围物件，可略） |
| L4 | 扎克「五天没跟任何人说话」 | `:122`「Zach: I’ve been sleeping badly again. I haven’t spoken to anyone in five days, and I wonder if I will lose my mind from loneliness.」 | md `:14` 只写「从被丢下的人变成闯入者」 | 不成立（人物弧线已概括，非事件） |

> 结论：本章**无阻断级漏**。三个时点的转折都在：玛德琳要「Something—new」（`:54`）→ 她死（`:87`–`:101`）→ 奥利弗落到 2041 黄房子（`:114`）→ 扎克偷通讯录找上门（`:192`/`:211`/`:235`）→ 卧室里「Why?」（`:277`）→ 2022 雪夜割腕（`:295`–`:325`）。md 一句话总结逐条覆盖。

## R3-2 编（md 有、原文无）

| # | md 断言（逐字） | 原文核对 | 判定 |
|---|---|---|---|
| B1 | `:11`「扎克靠偷来的通讯录找上门」／`:132`「扎克偷走克莱尔的通讯录」 | `:192`「Clare always leaves her bag on one of the dining room chairs. I open it, find her address book…」位于 `:122` 起的 **Zach** 段内；`:211`「I recognize Henry’s handwriting.」同段 | 不成立（归属正确：偷的人是扎克，不是奥利弗——这一点极易看错，已核） |
| B2 | `:132`「循着亨利笔迹的地址找上门」 | `:211`「is a strip of yellow legal paper with an address in Ravenswood jotted on it in blue ballpoint pen. **I recognize Henry’s handwriting.**」 | 不成立 |
| B3 | `:132`「在卧室里问一句『为什么』」 | `:270`「The bedroom door opens… I sit up and say, “Zach.”」→`:277`「“Oliver.” He looks distraught. “Why?”」 | 不成立（地点、问句都对） |
| B4 | `:13`「到他嘴里成了没人可填的空」 | `:320`「Alba said, it’s meant for us to add our voices, but to me it’s just emptiness without potential.」 | 不成立 |
| B5 | `:132`「母亲唱过的摇篮曲」 | `:60`「lullabies my mother once sang to me」 | 不成立 |

> 结论：本章**无编造级条目**；6 条抽查全部有原文。

## R3-3 错（两边都有但不一致）

| # | md 侧（逐字） | 原文（逐字 + 位置） | 不一致点 | 判定 |
|---|---|---|---|---|
| E1 | `:132`「把一场**听不清**的旧音乐会…拼成新的音乐」 | `:76`「The music I heard that evening has always hovered at the edge of my memory’s reach, like a dream badly described at breakfast. I didn’t have the vocabulary to capture it then, and I barely remember it now」 | 原文是**记不清**（barely remember），不是当时听不清；那首曲子当场好得让他像被催眠（`:70`「so extraordinary」），「听不清」与引语自相矛盾 | 提示（用词偏移；改「记不真切的旧音乐会」即可） |
| E2 | `:11`「玛德琳在红沙发上咳得直不起身」 | `:23`「Madeline is lying propped up on the red sofa, coughing… She struggles to sit up and I help her.」 | 「咳得直不起身」把「躺着、想坐起来很费劲」写成「直不起身」，方向近似 | 假红（可读作同义改写） |
| E3 | `:12`「只有两段下坠」 | 三段时间线各自下坠（临终—对峙—自杀），md 的「两段」指「前半临终的慢／后半骤然转凉」 | 读法而非事实 | 已核（非错） |

## R4 逐块对应

| 块 | 引语位置与首句 | 这段中文是不是在讲这句引语 | 判断 |
|---|---|---|---|
| 原句1 | `:30` "Her breath rages through her—…" | 是。空楼/骚灵/瘦/减法四层全在引语内 | 对应成立（`为什么这样写` 里的「痰音」取自引语**前**一句 `:30` 开头「her cough is a horrible sound, a deep barking retch」→ 引语选短·提示） |
| 原句2 | `:35` "The smoke from the painted wood is sweet and probably toxic…" | 是。烟的甜与毒、没别的选择、只问过一次，均出自引语 | 对应成立（`为什么这样写` 说「先交代柴的来处」，而柴的来处 `:35`「the wood that used to be the shed in the back garden」在引语**之前**、被切掉了 → 引语选短·提示） |
| 原句3 | `:58` "I sit at the piano and wonder…" | 是。「新＝她没听过」而非「世上没有」，md 的读者提示把这层点明，未越界 | 对应成立 |
| 原句4 | `:70` "The piece they played was so extraordinary…" | 是。但引语跳过了同段前文的「我十几岁／她五十多岁」（见 L1） | 对应成立（提示） |
| 原句5 | `:87` "The fire is very low, and I can see my breath…" | 是。两次呼吸＋指背＋凉＋怕，主语与受事全对 | 对应成立 |
| 原句6 | `:192` "Clare always leaves her bag on one of the dining room chairs…" | 是。叙述者是扎克（`:122` 段内），md 写「他打开包」未误挂成奥利弗 | 对应成立 |
| 原句7 | `:283` "I expect him to yell at me…" | 是。叙述者奥利弗、受事扎克；「what Alba and I have done」指他与阿尔芭的共同责任，md 译「自己和阿尔芭对他做了什么」方向正确 | 对应成立 |
| 原句8 | `:320` "The Japanese word karaoke means “empty orchestra.”…" | 是。词源→阿尔芭的说法→他的反驳，三层对照完整 | 对应成立 |

## 形态

- 8 块四子项齐全；块数 8 ∈ 本书该章 `block_target [7,12]`；`cjk_ratio` 最低 0.66（>0.6）；词汇 14 条例句逐条比对 text，miss=0。
- 三段拼贴的块序与原文时间顺序一致（2069 → 2041 → 2022），无跨段倒置。
