# 3-diff.md · 《Victorious》第 25 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch25_chapter_vi.txt`
- 受审 md：`ch25 june kills three men.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（walked into the hotel lobby where Bella and Grace were waiti）
- **原文**：原文 L28：It wasn’t hard to spot them at the lobby’s edge, bare legs and high heels sticking out from cinched black coats. June sauntered over, blond bob grazing her chin with each stiletto-ed step.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L28：原文 L28 的事实「walked into the hotel lobby where Bella and Gr」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L4 · R1 事实未进 md（let Grace take the cash off the floor and warned her not to ）
- **原文**：原文 L191：She meant it. But she also meant, Do not pass go. Do not call the cops. Do not make me regret this.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L191「let Grace take the cash…don't call the cops」是支线细节
- **档**：提示

### L7 · R1 事实未进 md（was on the twenty-third floor）
- **原文**：原文 L58：The doors opened, spitting them out on the twenty-third floor, and all they had to do was follow the music and the raucous laughter, both of which were seeping through the door at the end of the hall.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L58：原文 L58 是一处静态状态描写（was on the twenty-third floor…），非情节动作；md 只摘了动作性更强的句子，本条属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 3（阻断 0 / 提示 3） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（47 词 3 句）：“Didn’t know you were working,” muttered the redhead, Grace, crossing her arms and blowing a dark curl out of her face. No love there, thought June, though she didn’t know the drama. A glancing touch was enough to borrow a whole body, but memories were trickier things.
- 中文理解：红发的格蕾丝压着嗓子说「不知道你也接活」，抱着手臂把一缕深色卷发吹开。琼看出这两人之间没有交情，却不知道是为了什么——她只借了身体，没借到记忆。轻轻一碰就够她借用整具身体，可记忆是更难搬走的东西。
- 关键词：glancing touch · memories were trickier
- 为什么这样写：三个人见面本该先认人，这一段先给的是她认不出的那部分。格蕾丝的敌意是一个没有上下文的信号（No love there），琼只能看见表情，读不到缘由；memory 的缺口用一句规则补上，后面每一次冒充都受这条规则约束。
- 读者视角提示：读者此刻只知道她借了身体，不知道借的是谁的身体；连「她长什么样」都还没人交代。能确认的只有一件事：身体的记忆不在她手上，所以她说的话、认的人，随时可能穿帮。
- **原文**：原文 L37-L37
- **结论**：引语 3 句 47 词（原文 L37）：中文理解逐句对得上，主语=琼、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L22）
- **档**：相符

### 原句 2
- **md**：引语（64 词 2 句）：Grace rapped her knuckles on the wood, and seconds later, it swung open onto a lavish suite, with sweeping skyline views, and three men in various stages of inebriation. One sat on a couch, cutting lines, one stood at the window, nursing a tumbler, and one leaned in the doorway, a cigar in one hand and an open bottle of champagne in the other.
- 中文理解：格蕾丝用指节在门上叩了两下，几秒后门开向一间豪华套房：落地窗把整条天际线收进来，三个男人醉在深浅不同的程度上。一个坐在沙发上分可卡因，一个站在窗边捧着平底杯，一个倚在门口，一手雪茄，一手开了瓶的香槟。
- 关键词：lavish suite · various stages of inebriation
- 为什么这样写：门开之后是一组排比：One sat…, one stood…, one leaned…，三个人靠姿势和手里的东西区分开，作者一个名字都不报。阔气也只写两样——收进窗里的天际线、没喝完的香槟；醉意写成 in various stages，说明这场酒早就开始了。
- 读者视角提示：到这一句为止，三个人只是三个位置：沙发、窗边、门口。记住这三个位置，后面谁先动、谁先倒下，读者都只能靠它们指认。
- **原文**：原文 L61-L61
- **结论**：引语 2 句 64 词（原文 L61）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=门，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L32）
- **档**：相符

### 原句 3
- **md**：引语（48 词 3 句）：He’d ordered a sidecar, but she didn’t know how to make one, so she was going with a whisky sour. He might have noticed, if he’d been looking at her hands instead of her tits. She rattled the cocktail shaker, the ice inside making a sound like static.
- 中文理解：他要的是边车，她不会调，就改做威士忌酸。他要是看她的手而不是她的胸，本来能发现这一点。她摇起调酒壶，里面的冰响得像静电。
- 关键词：a sidecar · a sound like static
- 为什么这样写：一段里塞进两处不匹配：酒不对，注意力也不对。前一句用 might have noticed 写出「差一点被发现」，后一句立刻把感官挪到声音上——冰撞壶壁 like static，那点白噪音成了她在这间房里唯一能独占的东西。
- 读者视角提示：她既是被看的一方，也是唯一在计算的一方。这杯错酒暂时没人追究，本身就说明这屋里没人在意她手上做什么。
- **原文**：原文 L110-L110
- **结论**：引语 3 句 48 词（原文 L110）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L42）
- **档**：相符

### 原句 4
- **md**：引语（11 词 1 句）：“Harry never saw it coming,” gloated the Man on the Couch.
- 中文理解：「哈里完全没料到，」沙发上的那个男人得意地说。
- 关键词：never saw it coming · gloated
- 为什么这样写：这句是补刀：gloated 一个词就把说话人的立场摆出来——他不是旁观，是享受对方措手不及。never saw it coming 说的是哈里，句子真正在说的是沙发上的那个人怎么看待这件事。一个 gloated 抵一整段得意。
- 读者视角提示：敌意收购这件事真正落地就在这一句：有人打算对哈里动手，而哈里不知道。读者跟着这句知道了在座谁也不干净。
- **原文**：原文 L122-L122
- **结论**：引语 1 句 11 词（原文 L122）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L52）
- **档**：相符

### 原句 5
- **md**：引语（63 词 2 句）：Bella shot up from the sofa and stumbled toward the door, half dressed, as if she was in any danger. June didn’t have a chance to reassure her because the Man on the Couch lunged for the gun on the table, and she had just enough time to trade the blonde she’d been wearing right before he fired three shots into her chest.
- 中文理解：贝拉从沙发上弹起来往门口跑，衣服只穿了一半，仿佛她真有危险似的。琼来不及安抚她——沙发上那男人扑向桌上的枪，她只够在枪响之前把身上那具金发身体换掉，于是三发子弹打进去的不是她的胸口。
- 关键词：trade the blonde · three shots
- 为什么这样写：这一句把换身写成一个时间单位：had just enough time。前半句用 as if she was in any danger 写贝拉多余的恐惧，后半句用子弹兑现真正的危险。作者把结果留到下一段（Only it wasn’t her chest.），让读者先跟着弹道走一遍。
- 读者视角提示：这是全章第一次让我们看着她换身的过程本身：不是躲开，是把弹道挪到别人身上。她赢了这一回合，也刚刚亲手把一个人变成自己的挡箭牌。
- **原文**：原文 L152-L152
- **结论**：引语 2 句 63 词（原文 L152）：中文理解逐句对得上，主语=琼、受事=枪，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L62）
- **档**：相符

### 原句 6
- **md**：引语（44 词 1 句）：She couldn’t wear a dead shell—but that was okay, she was already shifting, abandoning the body for the mustachioed concierge she’d met on her way in, the one who’d sneered when she handed him her coat, like he knew what she was there for.
- 中文理解：她穿不住一具死掉的躯壳——不过没关系，她已经在换了：丢下那具正在倒下的身体，换成进楼时见过的那个留胡子的礼宾员；那人接过她外套时还嗤了一声，像是知道她来干什么。
- 关键词：dead shell · mustachioed concierge
- 为什么这样写：规则用破折号即时补上，紧跟着一句「不过没关系」——这不算困境，是一个熟手在走流程。礼宾员那一记 sneered 是她进楼时挨的，作者把它留到现在才用掉：脸不是随手挑的，是带着账挑的。
- 读者视角提示：换身在这里第一次显出冷意——她不需要尸体，只需要一张还没用过的脸。而她挑中的那张脸，恰好是今晚唯一看不起她的人。
- **原文**：原文 L167-L167
- **结论**：引语 1 句 44 词（原文 L167）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L72）
- **档**：相符

### 原句 7
- **md**：引语（45 词 2 句）：June met her eyes—her eyes, green as the surf on a stormy day—and sipped, tasting the spirit for the first time in years. She let it sit on her tongue, smoky and sweet, let it slide through her when she swallowed, warming in its wake.
- 中文理解：琼和自己的眼睛对上——那双眼睛绿得像暴风雨天的海浪——抿了一口，这是多年来第一次尝到酒的味道。她让酒停在舌头上，烟熏味带着甜，咽下去时一路暖过来。
- 关键词：green as the surf · spirit
- 为什么这样写：镜子之后，句子里出现的才终于是她自己的眼睛，颜色交给一个带风暴的比喻（green as the surf on a stormy day），跟她此刻的安静正好反着。for the first time in years 是这一段的重量：前面整章的嗅觉、味觉都是借来的，只有这一口是她的。
- 读者视角提示：这是全章唯一不设防的一刻。她清楚自己不能久留，所以这一段写得越慢，越像在拖延。
- **原文**：原文 L248-L248
- **结论**：引语 2 句 45 词（原文 L248）：中文理解逐句对得上，主语=琼、受事=酒，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L82）
- **档**：相符
