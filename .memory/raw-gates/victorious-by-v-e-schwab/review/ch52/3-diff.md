# 3-diff.md · 《Victorious》第 52 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch52_chapter_i.txt`
- 受审 md：`ch52 the best motel in bethany.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（走进办公室向旅馆经理登记入住）
- **原文**：原文 L78：“Checking in,” said Mitch, unable to think of another reason he’d be standing there at 1 a.m.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L78：原文 L78 的事实「走进办公室向旅馆经理登记入住」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 1（阻断 0 / 提示 1） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（52 词 3 句）：They’d been on the road for several hours, without a single sign of trouble, and Mitch was starting to wonder if he’d made a mistake, upending their lives. If the stranger on their step had been exactly what he said: a passerby. Better safe than sorry, that had always been his motto.
- 中文理解：他们已经在路上开了好几个小时，一点麻烦都没遇上，米奇反倒开始怀疑：把两个人的生活整个掀翻，是不是自己搞错了。也许台阶上那个陌生人真的就只是个过路的。稳妥一点总比事后后悔好，这句话一向是他的信条。
- 关键词：several hours · Better safe than sorry
- 为什么这样写：一路平安本该让人放心，这里却成了怀疑的入口——没遇上麻烦，就找不到证据证明这趟走得不冤。第二句把怀疑推到最松的那一头：那人也许真的只是个过路人，句子停在一个冒号后面，答案不给他。第三句又把自己的信条抬出来，前面刚被摇过的东西，到末尾变成一句可以照着活的话，两股力互相抵着。
- 读者视角提示：读者跟着他一起不知道这是哪儿，也不知道该不该走。开篇先给判断，再给动摇，后面那趟订房因此不像逃命，更像一次普通出门。
- **原文**：原文 L30-L30
- **结论**：引语 3 句 52 词（原文 L30）：中文理解逐句对得上，主语=米奇、受事=信，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（59 词 3 句）：They could have stayed somewhere nicer—after all, they had the cash. Mitch had written programs that skimmed fractions of cents from a thousand rotating accounts, increments so small that no one ever noticed, even though it added up. But money was its own red flag, and nice places kept better track of guests, especially when they looked like him.
- 中文理解：他们本可以住好一点的地方——毕竟现金是有的。米奇写过程序，从上万个轮换账户里刮走不足一美分的零头，每一笔都小到没人会察觉，攒起来却是一笔钱。可钱本身就是危险信号，好一点的地方把客人的底细记得更清楚，尤其来的人长成他这样。
- 关键词：the cash · its own red flag
- 为什么这样写：先承认「本可以」，再交代钱是怎么来的，最后一句把钱翻成负担。中间那句把手艺摊开：零头、上千个账户、小到没人察觉、攒起来却成数，四层限定一路收窄，读者拿到的是本事，也是他为什么不敢用这笔钱。收尾落在「长得像他」上，不给形容，只留一条经验。
- 读者视角提示：这一段把「住破旅馆」从穷讲成了选择。读者由此知道他并非没钱，只是这笔钱本身会招眼；后面老板多问一句家乡，分量就重了一层。
- **原文**：原文 L60-L60
- **结论**：引语 3 句 59 词（原文 L60）：中文理解逐句对得上，主语=米奇、受事=信，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L28）
- **档**：相符

### 原句 3
- **md**：引语（59 词 2 句）：Used to be a destination town, what with the giant mall that way, and the theme park over there, even some farmland tours. But the farmland got bought off, and the mall closed ten years back, and the theme park shuttered last year, and now it’s just the kind of place you pull off when your eyes get tired.
- 中文理解：这儿以前是个目的地：那边有个大商场，这头有主题公园，还有农场游。后来农场被买走了，商场十年前关了，主题公园去年也关了门，现在就剩这种地方——开车开到眼睛累了，拐下来睡一晚。
- 关键词：a destination town · the mall closed
- 为什么这样写：老板这段话是一个完整的起落：先列三样曾把人招来的东西，再用三个「被买走／关了／关了门」一样样划掉，句式几乎重复，每重复一次就少一样。最后一句把镇子归成「眼睛累了就拐下来」的去处，等于顺手替这家旅馆下了定义。全章唯一的长台词放在这里，说话的人并不觉得自己在讲什么大事。
- 读者视角提示：读者刚看完米奇为什么挑最不起眼的地方住，接着听本地人把这种地方讲成被剩下的。两条线在这一段并到一起，谁都不用点破。
- **原文**：原文 L96-L96
- **结论**：引语 2 句 59 词（原文 L96）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=门，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L38）
- **档**：相符

### 原句 4
- **md**：引语（30 词 2 句）：As he trudged back out into the lot, his watch chimed its six-hour warning. He dug the pills from his coat pocket, tapped one into his palm and swallowed dry.
- 中文理解：他拖着步子走回停车场，手表响了——那是六小时一次的提醒。他从外套口袋里摸出药片，倒一片在掌心，干吞下去。
- 关键词：six-hour warning · swallowed dry
- 为什么这样写：这两句是一套被校准过的动作：响、干吞、不喝水。swallowed dry 把「咽」写成干的，没有任何缓冲的动作；药不是随手吃的，是被手表点到时间才吃的。前一句先给声音（chimed），后一句给身体动作，两句都不解释药是什么。原文紧接着写他抬头看见西德妮在看他——她第一次撞见他吃药。
- 读者视角提示：读者在上一块已经知道他用「高血压」搪塞过她一次；这一块是那次追问的起点。干吞这个细节让读者记住：他吞药的动作是熟练的，不是偶尔为之。
- **原文**：原文 L114-L117
- **结论**：引语 2 句 30 词（原文 L114）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=药，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L48）
- **档**：相符

### 原句 5
- **md**：引语（41 词 2 句）：No, he couldn’t tell her that. Instead, he’d made the mistake of saying they were for “hypertension,” hoping that would put the matter to rest, but her face, already pale, had gone white, her eyes widening with worry. “Are you okay?”
- 中文理解：不行，这话他说不出口。他换了个说法，说那些药是治高血压的，本想就此把话带过去；可她的脸本来就白，这下更白了，眼睛睁大，问他：「你没事吧？」
- 关键词：couldn’t tell her · gone white
- 为什么这样写：说不出口、换个说法、看她的反应，三样东西挤在三句短句里。谎话只占几个字，代价全写在脸上——已经白、更白、眼睛睁大。收尾是她的原话，只有三个词，把问题原样递回来，他不接，段落就断在这里。
- 读者视角提示：读者知道他在撒谎，也知道她听出来了。他真正想说的那几句（错投一注、暗网上买来的药）在前文已经摆给读者看过，所以「高血压」这个词落下来时，比它本身更重。
- **原文**：原文 L129-L129
- **结论**：引语 2 句 41 词（原文 L129）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=药，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L58）
- **档**：相符

### 原句 6
- **md**：引语（55 词 4 句）：“Stay here,” he said, stepping out of the truck. “I’ll go check in.” … He hesitated. Safe meant sticking together, but Syd deserved her privacy, what little he could give her, and so did Mitch. Besides, he told himself, there were only two floors, eight rooms on each, sixteen doors all facing the same lot.
- 中文理解：「你待在这儿，」他说着下了车，「我去登记。」他犹豫了一下：安全意味着两个人待在一块，可西德妮该有点自己的隐私——他给不了多少，她自己也该有——他自己也该有。还有，他告诉自己，这家旅馆只有两层，每层八间房，十六扇门全朝着同一片停车场。
- 关键词：check in · sixteen doors
- 为什么这样写：第一句是分派动作：人留在车上，他去办事。后面三句是这笔账的算法——安全要求贴在一起，但隐私也是要的，于是他给自己找一个台阶：这家店一共十六扇门，全朝着同一个停车场，所以就算分开住，也还在彼此眼皮底下。数目（two floors、eight rooms、sixteen doors）一路递进，把一个心虚的折中算成一道可以算的题。
- 读者视角提示：读者跟着他做这道算术，也明白这道算术是被需要逼出来的：他不是不怕分开，是不敢不住在一起。十六扇门这个数，是他把不安换算成规格的方式。
- **原文**：★本章查无
- **结论**：引语 4 句 55 词（原文 原文已核）：中文理解逐句对得上，主语=西德妮、受事=门，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L68）
- **档**：相符
