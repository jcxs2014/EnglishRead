# 3-diff.md — ch05 逐块三问（R3 独立审查）

依据：`text/ch05_5.txt`（5,461 字符）与 `ch05 the poisoned salad is investigated.md`。
区间为原文 0-based 半开区间 [start,end)。每块三问：(a) 这段中文是不是在讲这句引语？(b) 这句是谁说的——施事/受事/归属有没有写反？(c) 分析有没有讲到引语之外的内容？

---

## 原句 1

- **引语首 20 字**：`‘Poisoned salad, eh?’ asked the ` （原文 39–139）
- **(a)(b)(c)**：(a) 是——中文理解「警务总监听完先是摇头，说"毒沙拉"这种说法你根本编不出来」正是这句。(b) 施事**未写反**：说话人是 Chief Superintendent，md 记为「警务总监」；受事是「毒沙拉」这一说法本身。(c) 分析未越界：「先给上级反应、暂不给案情本身」「'看上去像意外'的第一层」均可由本句与原句3 支撑。**唯一疑点**：「听完」二字——本句是全章第一句发言（原文此句之前无任何人物说话），Chief Superintendent 并未先听完任何汇报，「听完」是原文没有的先后关系。
- **两侧片段**：原文 39–139 `‘Poisoned salad, eh?’ asked the Chief Superintendent, shaking his head. ‘You couldn’t make that up.’`｜md 25 `警务总监听完先是摇头，说"毒沙拉"这种说法你根本编不出来。`

## 原句 2

- **引语首 20 字**：`‘We’ve contacted the Food Standards A` （原文 142–436）
- **(a)(b)(c)**：(a) 是——中文理解复述的正是 FSA 报告这段。(b) 施事对：报告人是 Caius（「凯厄斯报告」）；层级对：FSA 正在与供应商接洽、供应商供货给他们确信迪吉买沙拉的那家 greengrocer’s（原文 "the supplier that distributes to the greengrocer’s we’re certain Digby Combe-Watson bought it from"）→「局方正在与给那家蔬果店供货的供应商接洽——那家店可以确定就是迪吉·康姆-沃森买沙拉的地方」忠实。**归属存疑**：「They’ve done an emergency recall」的 They 在英文里有两个候选（句子话题 the FSA / 最近的名词短语 the supplier），md 作「对方已经启动紧急召回」，紧接上句「局方正在与…供应商接洽」，读者会把「对方」默认读成供应商；而紧急召回的行政主体通常是 FSA——英文本身歧义，中文取了供应链一端，属指代未锁定（提示级）。另一处轻微用词偏差：「那袋菜里有可能混进了毒芹的叶子」——原文 "the bag had some hemlock leaves in it"，had＝袋里曾有/含有，「混进」添了「混入」的动作意味。(c) 分析未越界，且**正确保留了情态**：「It's possible」→「有可能」未被写成断定；「它把毒芹降级成供应链上的一次疏漏」有原文支撑。
- **两侧片段**：原文 142–436 `…Caius said, adjusting his posture. ‘They’ve done an emergency recall. It’s possible that the bag had some hemlock leaves in it.’`｜md 35 `…局方正在与给那家蔬果店供货的供应商接洽…对方已经启动紧急召回，那袋菜里有可能混进了毒芹的叶子。`

## 原句 3

- **引语首 20 字**：`‘And they say eating your greens is` （原文 439–540）
- **(a)(b)(c)**：(a) 是——中文理解「警务总监自嘲一句：听说多吃青菜对身体好」讲的正是这句。(b) 施事**未写反**：仍是 Chief Superintendent，且原文明写 "The Chief Superintendent chortled at his own joke"，md 记「警务总监…说」正确。用词轻微偏移：原文是「为自己的笑话发笑」(chortled at his own joke)，md 作「自嘲」（自嘲＝挖苦自己），语用色彩略有出入（提示级）。(c) 分析未越界：「把毒芹说成'青菜'」「危险被说成营养」「说这话的还是主管本人」均可由原句1–3 串联支撑。
- **两侧片段**：原文 439–540 `‘And they say eating your greens is good for you.’ The Chief Superintendent chortled at his own joke.`｜md 45 `警务总监自嘲一句：听说多吃青菜对身体好。`

## 原句 4

- **引语首 20 字**：`‘How are you doing?’ The Chief Super` （原文 1061–1584）
- **(a)(b)(c)**：(a) 是——中文理解复述的正是这段。(b) 施事/受事/归属**均未写反**：问话者是 Chief Superintendent（md「警务总监先问他还好吗，然后压低声音说」＝ "leaned in and spoke quietly" ✓）；「它的靠山阿瑟·汉普顿」＝ "your champion Arthur Hampton" ✓；「新来一位热衷于继续削减预算的内政大臣」＝ "the appointment of a new Home Secretary keen on further budget cuts" ✓；「短时间内确实破过几个冷案和那桩双重列车谋杀案，成绩相当漂亮」＝ "Your team had had some real success in a short space of time… Those cold cases and the double train murder, all within a year. It was very impressive." ✓（"double train murder" 译作「双重列车谋杀案」直译但未误作两起）。(c) **分析越界（阻断级）**：「为什么这样写」写「于是'意外'这一层不只活在当事人的想象里，也活在**机构的默认态度**里——**案子没人接手时**，省事的结论就是**不必再深究**」。原文只说专案组被解散及其政治原因，从未说这桩案子「没人接手」；本章恰恰是三人同时在查（原文 2363–2562 Matt 的 warrant request、2565–2680 Caius 告知外交部、4501–5372 Amy 的搜查与 Matt 的摄像头）。「读者视角提示」进一步写「'这只是一场意外'就很容易被允许留在案卷里」，同样把原文没有的机构性结论（结论被采纳进案卷）写成了文本内事实。
- **两侧片段**：原文 1061–1584 `…what with your champion Arthur Hampton leaving the Cabinet and the appointment of a new Home Secretary keen on further budget cuts, its closure was inevitable really…`｜md 59 `…于是"意外"这一层不只活在当事人的想象里，也活在机构的默认态度里——案子没人接手时，省事的结论就是不必再深究。`

## 原句 5

- **引语首 20 字**：`‘Well, no, because he ate an accid` （原文 3824–4037，紧接 Matt 的 `‘But Digby wasn’t burgled.’` 3794–3821）
- **(a)(b)(c)**：(a) 是。(b) **施事/受事/归属全部正确**：Matt 先说「But Digby wasn’t burgled.」→ md「马特指出迪吉家并没有失窃」✓；Caius 接「Well, no, because he ate an accidentally poisoned salad.」→ md「凯厄斯解释说：那是因为他吃了一份被意外污染的沙拉」✓（受事 Digby，未写反）；「约会的对象慌了神，逃走，就把入室盗窃取消了」＝ "The date panics, flees and calls off the burglary" ✓；「对方知道警方会查他们，如果以前也干过，就更不想让人看出规律」＝ "They’d know we’d be looking for them and they don’t want us to see a pattern if they’ve done it before" ✓。(c) 分析未越界：「一套能自圆其说的剧本」「作者又留了一处后门」与原文相称。**唯一附带疑点**：「读者视角提示」称这是「两个警员在**厨房**里随口说出的一段话」、导航称「在**警局厨房**里边泡茶边」——原文第二场只写了 kettle、mugs、窗外、街上的邮筒，从未指明地点是「厨房」（更未指明是「警局厨房」），此为推断（提示级）。
- **两侧片段**：原文 3794–4037 `‘But Digby wasn’t burgled.’ / ‘Well, no, because he ate an accidentally poisoned salad. The date panics, flees and calls off the burglary…’`｜md 65 `马特指出迪吉家并没有失窃；凯厄斯解释说：那是因为他吃了一份被意外污染的沙拉——约会的对象慌了神，逃走，就把入室盗窃取消了…`

## 原句 6

- **引语首 20 字**：`‘It’s either fake or they’re super posh` （原文 4088–4404）
- **(a)(b)(c)**：(a) 是。(b) 施事**未写反**：仍是 Caius（md「凯厄斯说」✓）；原文 "they're super posh" 的 they＝写信人，md「写信人」✓；「它出自瓦格纳的一部歌剧」＝ "It's from an opera by Wagner"（it＝化名 Isolde）✓；「他不肯承认这个事实五分钟前他还不知道」＝ "Caius wasn’t going to admit that this fact had been new to him five minutes ago" ✓；「上面还写着'我出身小资产阶级家庭'」＝ "It says, 'I come from a petit bourgeois family.'" ✓。用词轻微偏移：「super posh」译「不折不扣的贵族」偏 aristocratic（原文更接近「极有钱有势/上流」）；"culture vulture" mark 译「'文化蛀虫'那一档」把 mark（标签）读成「档位/分级」（提示级）。(c) **分析越界（阻断级）**：「为什么这样写」写「调查在这里**从物证转到笔迹**，他们开始拆写信人给自己搭的身份」——原文**没有任何笔迹调查**，本章这条线是**化名**（Isolde 取自 Wagner 的 Tristan and Isolde）与交友广告上的**自我描述**（"culture vulture" mark / "I come from a petit bourgeois family."）；md 后半句「再从那句出身自述反推对方挑选化名的方式」才是对的，「从物证转到笔迹」是凭空添加的调查内容。
- **两侧片段**：原文 4088–4404 `‘It’s either fake or they’re super posh. It’s from an opera by Wagner.’… ‘They’ve handpicked it based on their “culture vulture” mark. It says, “I come from a petit bourgeois family.”’`｜md 79 `调查在这里从物证转到笔迹，他们开始拆写信人给自己搭的身份：先怀疑名字是编的，再从那句出身自述反推对方挑选化名的方式。`



---

## 书级例句全串核验（2026-10-21，主会话收口补记）

- 本章词表有 **1 条**例句未通过「全串逐字」核验（`check_vocab` 只取前 60 字符指纹，故判绿）：
  - `disbanded`：md 补了原文没有的收尾引号（原文该句对白仍在延续）
- 处置：去掉收尾引号，按原文留到句末
- 详见 `.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/vocab-full-string-audit.md`（书级审计记录与探针说明）。
