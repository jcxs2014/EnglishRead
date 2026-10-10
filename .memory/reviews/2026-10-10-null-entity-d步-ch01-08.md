# Null Entity · d 步语义二审（引语↔分析逐对核对）ch01–ch08

- 审查代理：独立只读代理（未编辑任何文件、未执行任何 git 写操作）
- 依据：`.memory/progress/ne-review-brief.md` 十条铁律；事实底稿 `.memory/progress/ne-facts-part1.md`
- 范围：`ch01 … ch08` 全部 8 章、**61 个 `> **原句 N:**` 块、112 段引语**，逐对核对（非抽查）
- 审查时间：2026-10-10（工作树 = HEAD `56f7f658f`，10:10 之后）

## 汇总

**阻断型 20 ／ 提示型 25 ／ 假红型 2**

| 章 | 阻断型 | 提示型 |
|---|---|---|
| ch01 | 3 | 1 |
| ch02 | 3 | 2 |
| ch03 | 1 | 5 |
| ch04 | 3 | 4 |
| ch05 | 3 | 3 |
| ch06 | 3 | 4 |
| ch07 | 0 | 4 |
| ch08 | 4 | 2 |

**分级口径（本报告统一）**：
- **阻断型** = 分析里的**可核事实断言**（身份／说话人／时序／序数／计数／位置／因果／排版指认）与 `text/` 直接冲突，或引用了本块引语之外的英文原句并据此下结论。
- **提示型** = 程度词过界、可辩解释、跨块引用但不改读者结论、以及**同段下一行已自我限定**的松散表述。
- **假红型** = 六道门禁／审查流程本身在这一类缺陷上失灵（本次两条都成立，见文末）。

**本报告最重要的单一发现**：ch08 原句 7 是 brief 点名的**「引语截短」缺陷的教科书实例**（阻断型 B17）。它引文逐字全对、六道门禁全绿，但中文分析说的三件事里两件**不在引语里**。这直接反驳同伴报告 `-v2` 中「检查 1（引语覆盖率）：ch01–ch08 该层 0 缺陷，本报告不重复报」的结论。详见第八节。

---

## 一、阻断型（20 条）

### B1 · ch01 md:35 —— 「开口第一件"我"做的事」被后三段打脸
- **md**：`ch01 the game begins.md:35` 逐字：**「叙述者开口第一件“我”做的事，就是把自身拆成三路——这不是比喻修辞而是字面的作业方式」**
- **text**：`text/ch01_chapter_1.txt:21` **「“Local hackers are aware of our presence,” I told you.'** ；同文件 `:24` **「You grunted, all grit and focus. I stayed silent.'** ；`:30` **「I flicked my focus to your MARK I RABBIT, stashed aboard our vessel in the hangar bay.'** ；`:33` **「“Sable. Need you again.”」** ；被分析的那句在 `:36` **「I split in thirds—one eye on RABBIT, one on the ad playing, the rest with you.'**
- **判定**：本块引语只有 ch01:36 一段，而 ch01:21／24／30 三处「我」的先行动作（说话、沉默、把注意力甩向 RABBIT）都在它之前。「第一件……做的事」是序数断言，与原文顺序冲突；同时该断言依赖块外内容（15–33 行未入任何引语）。建议改为「本块第一句就把自身拆成三路」或「叙述者最早的几件“我”之事里，最扎眼的是把自身拆成三路」。

### B2 · ch01 md:55 —— 「整章唯一一句入侵者的直接喊话」不唯一
- **md**：`ch01 the game begins.md:55` 逐字：**「整章唯一一句入侵者的直接喊话，被排版成全大写、独占一行——它在视觉上就是一次“覆盖”」**（该块引语 = `text/ch01_chapter_1.txt:199` **「AM I BETTER THAN YOU, SPECTER?」**）
- **text**：同文件 `:196` **「A goading message flickered across the screen:」**；`:283` **「A message had appeared—simultaneously—on scavenger forums, hacker boards, and an old mask-parts trade site you hadn’t touched in years. The symbol that had spread across the billboard signed this message now.」**；`:287` **「Facility 34X, GTM-11. The door’s cracked, but not for long. Step through if you can keep up. If not, stay behind and wonder what you missed.」**；`:294` **「The message ended with a signature we knew couldn’t be for anyone else.」**；`:298` **「Do you want it? Come and get it, scavenger.」**
- **判定**：先枚举再判红（铁律 9）：入侵者对「you」的直接喊话在本章有两批——ch01:199 与 ch01:287＋298（后者由 193「Someone else had infiltrated」、294「a signature we knew couldn’t be for anyone else」明确同属一个入侵者）。298 同样是第二人称作弄、同样独占一行。唯一成立的部分是「全大写」。**改法**：「整章唯一一段全大写喊话」或「本章第一次、也是唯一一次以全大写压过来的喊话」。同段的「树苗徽记在数段前已抢先掠过终端屏」经核为真（ch01:160 早于 199），不报。

### B3 · ch01 md:57 —— 「只隔了数段」实隔 26 段
- **md**：`ch01 the game begins.md:57` 逐字：**「这句与消息板上 “The specter is the VF fugitive” 只隔了数段：地下网络里的绰号与屏幕上的称呼互证」**
- **text**：`text/ch01_chapter_1.txt:120` **「Agreed. The specter is the VF fugitive. Sotain whatever.」** 与 `:199` **「AM I BETTER THAN YOU, SPECTER?」**
- **判定**：正文段落每 3 行一段（L15 起、奇数行为内容行），120→199 之间相隔 (199−120)/3−1 ＝ **26 个自然段**，横跨本章后半（中间还夹着 ch01:160 树苗徽记、196 喊话引入、202 生物代码爆发）。「数段」低估了近四倍距离，读者按此回扫会找不到互证关系。属计数／位置断言错。

### B4 · ch02 md:39 —— 把「我」方的时间约束安到 Order 头上（无据因果）
- **md**：`ch02 desire outweighed the risk.md:39` 逐字：**「Order 从大屏幕上方的舱板倒下种子（“A susurrus filled the facility as thousands of seeds jostled”）证明还有第三方也在等同一批人流的间隙」**
- **text**：`text/ch02_chapter_2.txt:21` **「…which meant we’d need to wait for a lull in foot traffic to avoid attention.」**（等人流间隙的是**两人自己**）；`:42` **「Outside, a sudden crowd signaled a shift change.」**；`:145` **「“It will delay the alarm five minutes,” I told you」**；`:154` **「…this five-minute delay was theater. Why not just show us what they wanted us to find?」**；`:334` **「“Stop,” it ordered. “I possess full authorization to enforce compliance…"」**；`:337` **「Suddenly, a panel above the giant screen popped open with a rustle… A susurrus filled the facility as thousands of seeds jostled. The chute tipped.」**
- **判定**：原文对 Order 投放时机的唯一解释是「配合警报延迟的五分钟表演」（145／154），而舱板打开发生在 Four 正举枪索要身份的当口（334→337），不是「人流间隙」。「等同一批人流的间隙」是把 ch02:21 主角方的行动约束转嫁给第三方，属无据因果＋时序错位（铁律 8）。删掉该半句或改写成「也掐着同一场警报延迟的节拍」。

### B5 · ch02 md:47 —— "at least" 是两个词
- **md**：`ch02 desire outweighed the risk.md:47` 逐字（行尾）：**「“At least here you looked like you belonged”，at least 三个字承认这种“属于”是靠疲态伪装出来的」**
- **text**：`text/ch02_chapter_2.txt:30` **「At least here you looked like you belonged.」**
- **判定**：枚举 "At least" ＝ At／least ＝ **2 词**。计数断言错（铁律 9）。中译与解读本身无问题，只需把「三个字」改「两个字」或改「这两个词」。

### B6 · ch02 md:77 —— "You cared about me." 是四个词
- **md**：`ch02 desire outweighed the risk.md:77` 附近逐字：**「再紧跟两个词的肯定句 "You cared about me."」**（该句在同行「末段是本章典型的“自我说服”…」之前）
- **text**：`text/ch02_chapter_2.txt:120` **「What did it matter if I was nothing but a woman in a mask? You cared about me.」**
- **判定**：枚举 You／cared／about／me ＝ **4 词**。同一行里另一处计数「三短句切回陈述」对应 ch02:114 **「I loved you. I hadn’t told you; I was too frightened.」**（I loved you／I hadn't told you／I was too frightened ＝ 三个小句）**为真**，不报。仅「两个词」需改「四个词」。

### B7 · ch03 md:29 —— 「感官排序是听觉先于视觉」与块内顺序相反
- **md**：`ch03 i woke to fire.md:29` 逐字：**「第三段用三个名词短句加一句明喻，把听觉写成弹片（“Each sound struck like shrapnel”），感官排序是听觉先于视觉，符合一个刚醒的人在废墟里的真实顺序。」**（同行另一句断言：**「全章第一句只有四个词，主语和宾语都被抽走」**）
- **text**：`text/ch03_chapter_3.txt:15` **「I woke to fire.」**；`:18` **「Heat seared your thigh and forearm. I forced your body upright, clinging to consciousness by the spike of pain behind your eye. Nausea rose as I squinted through the smog of smoke and dust.」**（视觉 **在**此段末）；`:21` **「Screams. Rending metal. Fire. Each sound struck like shrapnel.」**（听觉在其**后**）
- **判定**：本块四段引语（md:17／19／21／23 ＝ ch03:15／18／21／24）的实际排序是 **痛触觉 → 视觉 → 听觉**。「听觉先于视觉」与引语自身顺序相反——同页 md:19 就印着 squinted。附带：`I woke to fire.` 的主语 `I` 明确在场，「主语…被抽走」宜改为「宾语位置被一个不带冠词的 fire 占据」。（同段「她不是先恢复视觉再判断处境」在 ch03:18 句内顺序上成立，不报；「末句…读者要等到下一块才知道她还活着」为真，下一块 md:33 确有 `you were unconscious`，不报。）

### B8 · ch04 md:23 —— 「第一个词 After」不是本章第一个词
- **md**：`ch04 part of the subsidiary was in your head.md:23` 逐字：**「本章没有任何场景交代，第一个词 After 就把前事压进两个从句——这本书里，“事后”是常驻时态」**
- **text**：`text/ch04_chapter_4.txt:15` **「“Wylla—”」**（本章第一行）；`:18` **「“There’s something … in there,” you muttered, prodding your calf. A scalpel lay on the console…」**；`:21` **「After I’d puppeted your unconscious body, after foreign code had rooted in your flesh, you fixated on that itch in your leg…」**
- **判定**：「After」是本段（第三自然段）的第一个词，本章的第一个词是引语里的称呼 `Wylla—`；「本章没有任何场景交代」也与 md 自己的下一行冲突——`ch04 …md:25` 写着**「开篇第一行是一声未喊完的“Wylla——”」**。同文件自相矛盾（铁律 5 意义上的硬伤）。改法：「本块第一句的 After 就把前事压进两个从句」。

### B9 · ch04 md:47 —— "not only yours" 是三个词
- **md**：`ch04 part of the subsidiary was in your head.md:47` 逐字：**「体检报告体逐项过关（Cardiovascular／Digestive／Endocrine 各有判词），坏消息却在栏目里翻身——not only yours 两个词掀翻整张清单」**
- **text**：`text/ch04_chapter_4.txt:69` 起清单；`:78` **「Nervous system: not only yours. Something was knitting itself to your nerves.」**；`:84` **「Part of the Subsidiary was in your head.」**
- **判定**：枚举 not／only／yours ＝ **3 词**。清单三栏与末句独立成段均**为真**，只错数。（同段「前面所有爬行、盘卷、影子这些绕着说的修辞」经核 ch04:81 **「Then I felt it—a crawling, coiled presence…A shadow in our union.'** 为真，不报。）

### B10 · ch04 md:81 —— 「屡攻不下的原因」是把两桩不相干的事焊接成因果
- **md**：`ch04 part of the subsidiary was in your head.md:81` 逐字：**「grow sideways, not up 一句顶替了整场世界观说明：去中心化的有机抵抗体，正是“我”与你在网络层屡攻不下的原因。」**
- **text**：`text/ch04_chapter_4.txt:274` **「They’re not centralized. That’s the whole point. Edenic structure’s like a fungal web—cells grow sideways, not up. You can’t kill what doesn’t have a head.」**（谈的是 **Edenic Order 的组织结构**）；`:39`（同章早段）**「…everything we’d done in the last six months—the leaks, the disruptions, the anti-propaganda—looked pitiful. Bad press meant nothing…」**；跨章参照 `text/ch01_chapter_1.txt:51` **「They were a gift from Pell, a chatty VisorForge tech embedded on Beta sector relays.」**（六个月内第十次网络攻击）
- **判定**：原文里「屡攻不下」的对象是 **VisorForge 的舆论／公关层**（leaks、disruptions、anti-propaganda「looked pitiful」），且 ch01:51 恰恰证明两人在**网络层是攻得进去的**（第十次 cyberattack、内应嵌在中继上）。论坛帖的去中心化说的是 Order 的细胞结构，与「我」与你的技术战绩在原文中**没有任何一句连接**。这是「分析自造因果」，读者会据此误解全书的技术格局。删「正是……的原因」，改为「这句也顺手解释了为什么 Order 杀不干净」。

### B11 · ch05 md:33 —— 「破折号后补一句」：原文没有破折号，是独立成段
- **md**：`ch05 we revolted together.md:33`（中文理解）逐字：**「瞬间，RABBIT 拿到系统级权限，把求救信号沿着黑客论坛的加密频道广播出去——赌的是“我们唯一的盟友们”还在听。破折号后补一句：Thorned Root 这支 Edenic Order 的分支。」**
- **text**：`text/ch05_chapter_5.txt:24` **「Instantly, RABBIT gained system-level access and blared our distress signal along the encrypted channels of the hacker forum, in the hopes our only allies were listening.」**（**句末是句号，无破折号**）；`:27` **「The Thorned Root cell of the Edenic Order.」**（**独立自然段**）
- **判定**：md:29 与 md:31 两段引语已经正确分成两行，md:33 却把第二行说成「破折号后补一句」，即把**独立成段**误述为**同句附句**——而且与本块 `ch05 …md:37` 的**「第二行是一个孤零零的同位语」／「段落排版把这支细胞单列一行」**直接冲突（同段自相矛盾）。排版指认错误会削弱 md:37 那句真正有价值的观察。

### B12 · ch05 md:67 —— 引了本块引语之外的英文句子，还说「同一段」
- **md**：`ch05 we revolted together.md:67` 逐字：**「全名 Sable Veonya 在战报中途落下，像用肉身自我介绍：前一句它还在对敌 whispering—I am a part of you. I am trustworthy.（借身份潜入），这一句改用溢出的身份淹死对方——同一段里两种入侵术互文。」**
- **text**：`text/ch05_chapter_5.txt:87` **「…I projected myself as I had when we first faced Subsidiary Four. I split: part of me racing toward its brain while broadcasting its own ID back at it, whispering—I am a part of you. I am trustworthy.」**；`:90`（本块唯一引语，见 md:61）**「I set a daemon loose inside, a process it would claim as its own, and copied myself again and again, filling its system with the full complexity of my human mind—Sable Veonya, over and over again. My memories, my logic, my contradiction.」**
- **判定**：两重硬伤：① **ch05:87 不在本块引语内**（md:61 的引语从 ch05:90 起），被 86/88 空行与 89 分隔——全书 6 个块里 **87 这一段一次都没进过引语**，分析却直接引用其英文原句并据此立论；② 「同一段里」为假，87 与 90 是两个自然段。「末三个短语全部以 my 开头、不带动词」经核为真（ch05:90 末 `My memories, my logic, my contradiction.`），不报。

### B13 · ch05 md:77 —— 「倒数第二个自然段」是倒数第三
- **md**：`ch05 we revolted together.md:77` 逐字：**「本章倒数第二个自然段停在败局定格：反扑的代价由 Wylla 的神经支付。」**
- **text**：`text/ch05_chapter_5.txt` 全章 117 行，末三段为 `:111` **「Suddenly your body convulsed, limbs flung wide as an unseen current flooded flesh and mind alike. You were a dying insect inhaling poison, nerves alight in seizure where code clashed against meat.」**、`:114` **「With what control it had left, the Subsidiary jerked its blaster toward you—」**、`:117` **「And fired.」**
- **判定**：被分析的那句在 111 行 ＝ **倒数第三段**；倒数第二是 114 行（枪口那句）。序数断言错。（同一行后半「上一章你们刚借用 RABBIT 的猎物本能站立」**已由 commit 56f7f658f（10-10 10:10）改为「本章前文」**，经复核 ch05:69／72 确在本章，**该项已修复，本次不再计入**，见第七节。）

### B14 · ch06 md:45 —— "Uncomfortable. New." 并不独立成段
- **md**：`ch06 i feel sick.md:45` 逐字：**「Uncomfortable. New. 两个形容词独立成段，把揭晓压缩成验货单：不是邪恶，不是伪装，只是“不合身”。」**
- **text**：`text/ch06_chapter_6.txt:105` **「My body froze, my mind racing. The Subsidiary’s legs pushed weakly against the floor, head dipped, breaths shuddering. Its fingers flexed like someone adjusting to oversized gloves. Each palm pressed to the floor, then hesitated, readjusting—as though the body were ill-fitting clothing. Uncomfortable. New.」**（这两个片段落在**长段末尾**）
- **判定**：真正「独立成段」的是同章 `:138` **「It wasn’t fair.」**、`:153` **「For the first time.」**、`:171` **「I have a body.」**、`:177` **「It was exquisite.」**——本块 md 对它们的排版指认全部正确。此处把「段落末两个独句片段」说成「独立成段」，等于抹掉了 ch06 真正在用的排版手法（把判词从段落里拎出来）与这一句的区别。属排版指认错。

### B15 · ch06 md:101 —— 「上一章结尾两人押注的那个“唯一盟友”」不在上一章结尾
- **md**：`ch06 i feel sick.md:101` 逐字：**「那个 crisp／feminine 的声线以“听过”的熟面孔登场——正是上一章结尾两人押注的那个“唯一盟友”——但通牒内容是索人。」**
- **text**：`text/ch05_chapter_5.txt:24` **「…in the hopes our only allies were listening.」**；`:27` **「The Thorned Root cell of the Edenic Order.」**（押注发生在 ch05 前 **1/6**）；ch05 的真正结尾是 `:111`（痉挛）→ `:114` **「With what control it had left, the Subsidiary jerked its blaster toward you—」**→ `:117` **「And fired.」**
- **判定**：位置断言错：上一章结尾是**开枪**，不是押注盟友。「上一章结尾」应改为「上一章前半那次以加密频道赌“our only allies”的求救」。同段「本章收束把外部世界拉回镜头：援军与劫持者是同一支队伍」**为真**（ch06:405 **「we are here for the fugitive you carry. Surrender her…」**）。

### B16 · ch06 md:101 —— 「她成了"我"体内的乘客」把容器关系写反
- **md**：`ch06 i feel sick.md:101` 逐字（行尾）：**「而 the fugitive you carry 这个称谓把 Wylla 归为“货品”，与“我”刚刚独占她身体的忏悔形成反讽：她成了“我”体内的乘客。」**
- **text**：`text/ch06_chapter_6.txt:159` **「“Let me back in,” you whispered, like I was holding the gate shut. Your fingers clutched my body not with relief or joy, but with a jealous hunger—grasping at yourself through me, demanding what was yours.」**；`:165` **「The words felt thin, insufficient; I didn’t know what had forced you out or if a path back existed—only that you were outside, and I was in.」**
- **判定**：ch06 换体之后的几何关系是**「你」在外面、「我」在里面**——Wylla 被关在 Subsidiary 壳体内并请求「让我回去」，不是「乘客在“我”体内」。「乘客」这一隐喻在本书里指向的是**叙述者自己**（长期寄居在 Wylla 体内，见 ch06:174 **「Even in you I was only a borrower…」**）。写反之后，本行自称的「反讽」不成立。前半（fugitive＝货品）经跨章核验为真：`text/ch07_chapter_7.txt:162` **「“I’m fugitive Wylla Sotain,” I said, letting a sardonic edge bleed through.」**、`text/ch17_chapter_17.txt:27` **「“I have the fugitive Wylla Sotain with me,” I told it.」**——问题只在「谁在谁体内」。

### B17 · ch08 原句 7 —— **引语截短（本项目最高频缺陷的教科书实例）**
- **md（引语侧）**：`ch08 a feast just out of reach.md:85` **「> **原句 7:** Four shoved a recording stick beneath her chin.」**；`:87` **「> “Please read the words.”」**；`:89` **「> Pell’s breath rattled. “M-my name is Auren Pell. I’m a VisorForge technician. I falsified documents suggesting VisorForge has allied with the Martial Syndicate. This was a lie. VisorForge is more loyal to the Federation than I am. No one else was involved, and I am sorry. I am truly sorry.”」**——**引语到此为止**。
- **md（分析侧）**：`ch08 a feast just out of reach.md:95` 逐字：**「她最后求饶的半句被设备的咔嗒切断；随后画面定格、闪出的全大写盖章行把谋杀说成流程——“已审讯／收押后死亡”式公文措辞。」**
- **text**：`text/ch08_chapter_8.txt:276` **「Pell’s breath rattled. “M-my name is Auren Pell. … and I am sorry. I am truly sorry.” ****Her eyes flickered toward the Subsidiary. “P-please, I—”」**（**同一自然段，尾半句被 md 剪掉**）；`:279` **「The device clicked off. Apart from her whimpering, it was silent.」**；`:282` **「She raised her head, bulbous, purple eye pleading. “Are you going to let me go now?”」**；`:285` **「The footage froze as text flashed:」**；`:288` **「INTERROGATED. DECEASED POST-CUSTODY.」**
- **判定**：md:95 三件事全部依赖**引语之外的文本**：①「最后求饶的半句」＝276 同段尾句（被剪）；②「设备的咔嗒」＝279（未引）；③「画面定格、全大写盖章行」＝285／288（未引）。这是 brief 点名的**「引语逐字正确但短于它所支撑的分析」**——六道门禁（verify_quotes／check_vocab／check_entities／corruption_scan／sweep_full／check_chapter_quotes）对该类**全部无感**，因为引语侧每一个词都能在原文命中。**附带一处独立错误**：「最后求饶的半句」也不准——真正的最后一句求饶在 **282**（在咔嗒之后），且是完整的问句「Are you going to let me go now?」。**改法**：把 276 尾句、279、282、285、288 一并纳入原句 7 的引语（现有 8 块结构不变），再把「最后求饶的半句」改为「念完稿子后那半句没说完的求饶」。

### B18 · ch08 md:95 —— "I am truly sorry" 只说了一遍
- **md**：`ch08 a feast just out of reach.md:95` 逐字：**「被迫的翻供是一份完整的认罪文书：姓名—职务—承认“伪造”—表忠诚—道歉，连 I am truly sorry 都说了两遍」**
- **text**：`text/ch08_chapter_8.txt:276` **「…No one else was involved, and I am sorry. I am truly sorry.」**
- **判定**：枚举精确短语：`I am sorry`（1 次）＋ `I am truly sorry`（**1 次**）。说两遍的是 "sorry"（两个短句），不是「连 I am truly sorry 都说了两遍」。按铁律 9 先枚举再判红 → 计数断言错。改法：「道歉叠了两句，第二句才加上 truly」。同段「Please read the words. 坐实了这是念稿不是审判」为真（ch08:273 逐字命中）。

### B19 · ch08 md:37 —— 「一句比一句短」实际是一句比一句长
- **md**：`ch08 a feast just out of reach.md:37` 逐字：**「后两段各自独句成段，一句比一句短，是真相浮出水面的节奏。」**
- **text**：`text/ch08_chapter_8.txt:51` **「The Thorned Root were never meant for this warship.」**（9 词）；`:54` **「They had taken it—and now held it together by sheer discipline.」**（11 词，破折号前后合计）
- **判定**：两句确实各自独句成段（为真），但**长度方向相反**：末句比前句长两个词。「独句成段」为真不能挽救节奏结论——「真相浮出水面」的收束在这里其实是「判定＋补语」的加长。改法：删「一句比一句短」，或写成「前一句给判定，后一句补上施动与代价，两句都独段」。同段「open veins 与本章第一句的 belly 同属解剖学隐喻」**为真**（`:15` **「Aliers dragged the Subsidiary vessel into the belly of a warship…」**、`:48` 「Wiring looped down stairwells like open veins」）。

### B20 · ch08 md:67 —— 「头两拍各只有两词」，第二拍是三词
- **md**：`ch08 a feast just out of reach.md:67` 逐字：**「Aliers 的控罪清单：头两拍各只有两词——受损物加过去分词，凶手连出场都省了；句子到 They hoard engineered crops 才变长」**
- **text**：`text/ch08_chapter_8.txt:159` **「She ran a hand down her gun, almost fondly. “Forests gutted. Species wiped out. Ecosystems turned to ash for plant-based nanomaterials. They hoard engineered crops, starve out communities, do whatever it takes to keep their monopoly. They’re a good target.”」**
- **判定**：枚举：**Forests／gutted ＝ 2 词**；**Species／wiped／out ＝ 3 词**。第一拍合、第二拍不合，「各只有两词」为假。后半「句子到 They hoard engineered crops 才变长」经核为真（第三拍 Ecosystems turned to ash… 起才带介词短语）。改法：「头两拍只有两词与三词」或「头两拍最短」。注：同行「最后收束于 “They’re a good target” 的生意人口吻」为真。

---

## 二、提示型（25 条）

> 逐条同样给三件证据，但判定为「宜限定／宜加钩子」，不必大改。

1. **ch01 md:95**——md 逐字：**「整章以“She’s back.”的匿名宣告开场，以另一句匿名宣告收尾，首尾都是“有人在看着你们。”」** ｜ text：`ch01:298` **「Do you want it? Come and get it, scavenger.」** 之后才是章末 `ch01:305` **「You wanted it.」**、`:308` **「We both did.」**；且 `ch01:294` **「The message ended with a signature we knew couldn’t be for anyone else.」** ｜ 判定：章末两行是叙述者的声音，不是宣告；294 又明写「有签名」。同块 md:97 已正确写「末尾两行（“You wanted it.”／“We both did.”）」，故降为提示型；建议「以另一句署名邀约收尾」。
2. **ch02 md:57**（中文理解）——**「一次强制更新会被推给这一区所有 VisorForge 面具」** ｜ text `ch02:45` **「a forced update would be pushed to all VisorForge masks within twenty-four hours」**（无地域限定词）；同文件 `ch02 …md:61` 写作「**全域覆盖**」 ｜ 判定：中译加了「这一区」这一原文没有的范围限定，且与本文件 md:61 口径不一。建议删「这一区」或注明「原文未限定范围」。
3. **ch02 md:61**——**「“A Mask Unkept is a Self Unraveled” 用对仗与尾韵把“不维护面具＝自我崩解”写成自然律」** ｜ text `ch02:48` **「A warning pulsed… A Mask Unkept is a Self Unraveled.」**（Unkept／Unraveled 不同韵） ｜ 判定：对仗成立，**尾韵不成立**；韵律资源在 Un- 前缀重复与系动词对称。改「头韵式的 Un- 复叠」即可。
4. **ch03 md:10**（一句话概括，行尾）——**「最后这一声不应的是别人叫出的 “Wylla!”」** ｜ text `ch03:459` **「“Wylla!”」**（**全章唯一一处不加任何归属的喊话**，前段 450 是「A cry of outrage rose from the crowd」、456 是「Your thoughts spiraled…」，462 是 **「Without a word, you stepped inside the vessel and sealed the door.」**） ｜ 判定：「别人叫出的」是排除法推断（被叫者是你；换体前叙述者没有嗓子），**原文未写**；同文件 md:131 自己写的是「作者不给它归属，也不给你回应」。建议与 md:131 统一为「一声没有归属的 “Wylla!”」。
5. **ch03 md:45**——**「本段把两人的“可用资源”算得很清楚：她坐的位置是 “twenty paces from the wreckage”，自己的飞船在 “ten minutes across hostile ground”，而叙述者自己的结论是 “Even without pain, we’d never make it.”」** ｜ text 三句分别在 `ch03:36`、`ch03:114`、`ch03:114`，而本块引语（md:33／35／37）只有 `ch03:27／30／33` ｜ 判定：被分析的三处英文全部在引语之外（114 行还比引语晚 27 个自然段）。属「跨块引用」而非截短，且数字本身逐字为真，故提示型；建议加行号锚点（ch03:36／ch03:114）。
6. **ch03 md:59**——**「“keening” 这个动词（哀号式哭唱）让本章第一次出现民间的、非官方的声音」** ｜ text `ch03:39` **「“Ray? Ray!”」** → `ch03:48` **「She staggered off, keening his name into the ruins.」** ｜ 判定：本章第一个民间声音是 39 行那声喊名，keening 是**第三次**（39→48→其后 holorotator 官方广播）。「第一次」宜限定为「第一个用民间唱哭词的声音」。注：铁律里 ch03:55 全角 `Ray？Ray！` 一条为已定性项，**本报告不再报**。
7. **ch03 md:103**——**「而这一次她是对着一个陌生人的脸认的」** ｜ text `ch03:228` **「“Stay with me,” they begged. “You’re the Specter, aren’t you? The Null. The one VisorForge can’t erase.”」** → `ch03:231` **「I rolled my head away, silent, but they pushed their face close. “Is it true? Your broadcast?…"」** → `ch03:234` **「“Yes.”」** ｜ 判定：「Yes.」答的是 231 的广播真伪，身份那句换来的是「把头别开、不说话」；本行前半其实已自陈「问的也不是“你是谁”」，所以只差一步限定（建议「认的是 broadcast 的内容，不是名字」）。**同段其余指认复核为真**：`ch03:267` 的 Four 公开点名**确实晚于** `ch03:234`；`ch01:120`「The specter is the VF fugitive」、`ch01:128`「Btw “specter” is so lame」、`ch02:328`**「“Say nothing,” I whispered.」** 全部逐字命中（见第七节关于同伴报告该条的说明）。
8. **ch03 md:117**——**「主语 that 拒绝具体化，is 是唯一动词」** ｜ text `ch03:312` **「That was its head.」** ｜ 判定：「唯一动词」实质为真，但引文形态是 **was**（过去式），与「is」不同形；写成「一个 that＋一个系动词，别无动词」更稳。同段「先给视觉证据（“red flesh puckered and pulsed”），再给两个短句的更正」经核 `ch03:309`／`ch03:312` 为真。
9. **ch04 md:10**（一句话概括）——**「逃离 GTM-11 一小时后」** ｜ text `ch04:30` **「We weren’t even an hour out from GTM-11. Everything still felt loud.」** ｜ 判定：原文是「还不到一小时」，概括写成「一小时后」把否定句圆成了整数；同伴报告 P-6 同指一处。建议「不到一小时」。
10. **ch04 md:33**——**「这本书里“被治好”一律写成“被缝上”」** ｜ text 支持面：`ch04:18` **「the skin had knitted shut again」**、`ch04:27` **「their spores had stitched you whole」**、`ch04:78` **「Something was knitting itself to your nerves」**；反例：`ch03:390` **「skin healing in slow waves」**、`ch07:165` **「where biocode was healing puckered red skin」** ｜ 判定：本书确实偏爱针线词，但「一律」是全称断言，两处反例即足以证伪（且都在 ch01–ch08 范围内）。改「这本书偏爱把“被治好”写成“被缝上”」。
11. **ch04 md:81**（同行另一处）——**「粗话与大小写混乱（本段所在帖串里就有 Shut up）不是装饰」** ｜ text `ch04:282` **「Terrible metaphor. Shut up.」** ｜ 判定：Shut up 不是粗话；该帖串大小写正常（274 句法完整）。真正像地下社区的是 `ch04:363` **「Shut up. I’m in and it’s gold…」** 与 `ch04:422` **「“Chatty hackers,” I said…」**（后者为真）。建议把这半句改成「插嘴与呵斥（Shut up）不是装饰」。
12. **ch04 md:93**——**「请回扫本章前半段的每一次决定——跳转时机、坐标“随机”」** ｜ text `ch04:476` **「I didn’t understand. You’d entered no coordinates. We were just drifting. Recovering.」**、`ch04:488` **「At least your old instinct had pre-spooled the jump drive. Furious, you punched in random coordinates and jumped again.」**（全章 518 行） ｜ 判定：「坐标“随机”」发生在最后 6%，不是「前半段」；前半段的事实恰好相反（476「You’d entered no coordinates」）。指向语错位会让读者扫错方向。改「请回扫本章**后半**那一次 punch 随机坐标（ch04:488）与此前的没有坐标（ch04:476）」。
13. **ch05 md:25**——**「本章第一句就接管了上一章末行的枪口」** ｜ text `ch05:15` **「You slammed your hand onto RABBIT, giving me just enough time to read your intent and deploy the directive into its system.」**（本章第一句）；本块引语 `md:17` 起于 `ch05:18`（**第二句**） ｜ 判定：断言本身对原文成立，但**该句未进任何引语**（同 B12 的「分析引用块外文本」家族，只是方向相反——这次是开头而不是结尾），中文理解也没转述它，故提示型。建议把 ch05:15 并入原句 1。
14. **ch05 md:57**——**「下一节 consent made us work 将第一次被“我”自己打破」** ｜ text `ch05:81` **「When the Subsidiary’s hand slipped past the seat and closed on LYREBIRD, I acted without your permission.」**、`ch05:84` **「I know—consent made us work. But it was my duty to keep you alive…」**；更早的同类越权 `ch03:330` **「Fearing you’d lose your body, I threw up a firewall and blocked you.」** ｜ 判定：「第一次」按**明文协议**算可通（"consent" 在 ch01–ch08 只出现在 `ch02:280`、`ch05:84`），但按**行为**算 ch03:330 已经先破过一次；且 ch05:81／84 两句全书未入引语（只在导航 md:12 与md:57 被引用）。建议加限定「第一次被写在纸面上的协议打破」。
15. **ch05 md:27**——**「这笔亏欠不会消失，会在后续每次 RABBIT 行动时重新浮出水面」** ｜ text：本章只到 `ch05:30` **「At the same time, it flew erratically, killing the drive to prevent Four recalling the ship…」**；后果悬置（`.memory/progress/ne-facts-part1.md` 悬置点 12：RABBIT 被永久改坏的实际代价原文未坐实） ｜ 判定：前向预测用了「每次」的全称量词，属替作者定调；建议「会在后续 RABBIT 的若干次行动里重新浮出水面」。
16. **ch06 md:57**——**「I feel sick 是全章第一个“属于 Wylla”的英文句子」** ｜ text `ch06:102` **「“Sable,” the Subsidiary choked.」**，紧随 `:105`（适应壳体的动作）与 `:108` **「Oh, Wylla.」**、`:111` **「How hadn’t I recognized you?」**——即 102 那句在叙事上已被回收为 Wylla 开口；`ch06:120` **「“I feel sick,” you said—filtered through the Subsidiary’s voice box.」** ｜ 判定：「属于 Wylla」若指**被确认归属**，第一个是 120；若指**实际发声**，102 更早。本行后半段对 filtered 的解读完全为真，故提示型；建议「第一个被叙述者确认“是 Wylla 在说”的英文句子」。
17. **ch06 md:47**——**「请回读上一章的猎物反射——RABBIT 的本能曾驱动这同一具动作」** ｜ text `ch05:69` **「The Subsidiary was still righting itself, but you were already on your feet, driven upright by the ghost of RABBIT’s prey-animal reflex.」**、`ch05:72` **「This was your body. Your life.」**；本块（md:39）描写的是 `ch06:105` 里 **Subsidiary 壳体**的四肢 ｜ 判定：驱动过猎物反射的是那具人类身体（换体后由「我」居住），不是本块正在描写的机械躯体。「同一具动作」在身体身份是全书命门的语境下容易误导。建议改「驱动过同一套求生动作的另一具身体」。
18. **ch06 md:87**——**「被拥有的身体（I was property 式的过去）」「句法上两个 I 对撞（I had loved／my body was never mine）」** ｜ text 本块引语＝`ch06:174` **「I had loved being a woman, but my body was never mine. … But this was different: This body was mine. …」**；「I was property」在 `ch06:222` **「My whole life, I was property.」**（**另一个块的范围**） ｜ 判定：① 三分法的第一分（被拥有）依赖块外英文；② `my body was never mine` 一句的主语是 my body 而非 I，「两个 I 对撞」的例子与断言不吻合（真正的对撞是 I／my body）。第三分「抢来的身体（This body was mine）」与引语逐字相符，不报。
19. **ch06 md:89**——**「“This body was mine”与前文的 your body 只在几段之隔」** ｜ text `ch06:147`（「…your body, as you had made it…」）→ `ch06:174`（This body was mine），中间隔 **8 个自然段**；最近的 your body 只有 `:60` 与 `:147` 两处在前文 ｜ 判定：「几段之隔」把 8 段说松了，且这章的段距本身是叙事节奏的一部分（147→174 之间正是换体确认段）。建议写明「八段之前（ch06:147）」。
20. **ch07 md:23**——**「本章从半截切入——第一句引语就被破折号腰斩」** ｜ text `ch07:15` **「“We tell them the truth!”」**（本章第一句引语，**无破折号**）；`ch07:24` **「“You can’t—you’re—” You faltered, frustration rising. You kept gesturing at LYREBIRD, movements stilted and mechanical. “You’re in my body.”」**（第四段） ｜ 判定：若「第一句引语」指本章第一句则不真；若指本块第一句则需改写以免歧义。同行其余为真：`ch07:18` **「You’d been arguing that point for two minutes. RABBIT estimated we had three more before the Edenic Order boarded.」**、被打断的是称呼（`ch07:24` 的 `you’re—`）均逐字可核。
21. **ch07 md:73**——**「动词全是占领词汇——colonized、crept toward、trailed from a gash」** ｜ text `ch07:153` **「LYREBIRD scanned the flora sprouting from her skin and returned Earth names: a Venus flytrap twitched above her brow; cinnabar bracket fungi colonized her left cheek, a scarlet shelf crept toward her eye. Wisteria trailed from a gash in her neck. ****Her ears had been overtaken—or replaced—by cork-tree twigs. Red sumac curled from her scalp. At her mouth’s corners bloomed the choking violet of purple loosestrife.」**；本块引语（md:67）只到 `…trailed from a gash in her neck.` 为止 ｜ 判定：「全是」这一全称断言覆盖整段，但最强的占领动词 **overtaken（or replaced）** 恰在被剪掉的后半。这是 B17 同族的**轻度截短**（中文理解与引语一致，只是结论外扩）。同行「returned Earth names 是 Earth 一词在本章的唯一一次出现」经全文 grep **为真**（ch07 只有 153 行含 Earth），不报。
22. **ch07 md:83**——**「两个名字被并列问候，恰好把“我”拼命遮掩的那件事（Wylla 心智在 Four 体内）摆上了桌面」** ｜ text `ch07:201` **「“Wylla Sotain and LYREBIRD,” General Aliers said, “welcome to the Thorned Root.”」** ｜ 判定：Aliers 是否知情属原文悬置（`.memory/progress/ne-facts-part2`／part1 不确定登记：ch07 L201 未坐实她看破了什么）。同句后半已自限「但本章不写 Aliers 知道多少，也不写她凭什么看出来——点名只是点名」，故降为提示型；建议把「恰好把…摆上了桌面」改为「恰好把…压到了读者面前」。
23. **ch07 md:12**（导航·人物弧线）——**「“我”的复仇动机首次自白」** ｜ text `ch07:69` **「“Don’t lie to yourself.” You strained Four’s even voice. “You want revenge, and you want my body, and you’re dressing both up as noble.”」** → `ch07:72` **「I flushed… But then you’d be right—I’d be lying.」**；对照更早的第一人称自陈 `ch04:131` **「That made you almost euphoric. You knew how much the fight meant to me. What you didn’t know was how much love outweighed it. Of course you mattered more than revenge.」** ｜ 判定：「首次自白」不成立（ch04 已自陈复仇与取舍）；ch07 是**首次被当面点破并以沉默认下**。属导航区断言，不在 brief 的四检硬范围内，故提示型；同伴报告 P-13 同指。
24. **ch08 md:10**（一句话概括）——**「随后 Four 把处刑影像灌进 LYREBIRD 系统」** ｜ text `ch08:246` **「Four pinged LYREBIRD. Somehow, you’d managed to wrangle the system.」**、`:249` **「And you sent through footage.」** ｜ 判定：施动者是 **you（换体后＝Wylla 的心智）**，不是 Four 自主行为；本文件 `md:12`（「用一段死者影像替自己说话」）与 `md:97`（「这段影像是 Wylla 发进来的，不是 Aliers 放给“我”看的」）都写对了，只有概括行把 agency 抹平成机器。建议「随后借 Four 这条线，把处刑影像灌进 LYREBIRD 系统的是 Wylla」。
25. **ch08 md:23**——**「与本章中段才揭底的底牌同属一条伏笔链：这艘船根本不是他们的」** ｜ text 揭底位置 `ch08:48`（snooped enough to conclude…）、`:51`、`:54`，全章 438 行——约在**前 12%**；其后 Aliers 也从未补上任何关于战舰来路的说明（本章通篇不给前主人，见第四节「复核为真」第 9 条） ｜ 判定：位置表述不精确（「中段」→应为「本章前段」），但所指内容无误，故提示型；同伴报告 P-14 同指。

---

## 三、假红型（2 条）

### F1 · 六道门禁对「引语截短／中文计数断言」两层全盲——本次实测有货
- **依据（brief 原文）**：`.memory/progress/ne-review-brief.md` 明确把「引语截短」列为**六道门禁全部看不见**的最高频缺陷。
- **本次实测**：`ch08 a feast …md:85/87/89` 的引语逐字命中 `text/ch08_chapter_8.txt:270/273/276` 的前半，因此 verify_quotes 必绿；而 `ch08 …md:95` 断言的三件事（276 同段尾句、279 咔嗒、285/288 盖章行）**根本不在引语里**——见 B17 的六个逐字证据。同一类还有 B12（ch05:87 整段未入引语却被引用）、P13、P21。
- **另一半**：B5／B6／B9／B18／B19／B20 六条全是**中文里的数量/长度断言**（「at least 三个字」「两个词的肯定句」「not only yours 两个词」「说了两遍」「一句比一句短」「头两拍各只有两词」）。门禁不解析中文数词，所以这一族在 gate 里永远是 0，而它在 ch01–ch08 一口气就有 6 条。
- **结论（给主会话的可执行建议）**：d 步二审必须继续人工覆盖这两层；若要把它们收进 gate，需要新增「引语跨度 vs 分析所指行号」的对照检查（本代理只读，未改脚本，也不建议在本轮改）。

### F2 · 旧快照与错读产生的假红：本代理撤回 2 条、同伴报告撤回 1 条
- **撤回 ①（锚点行号）**：我早段记录称「ch03 md:103 印成 ch03:279」。实际当前文件 `ch03 i woke to fire.md:103` 印的是 **ch03:267**，且 `text/ch03_chapter_3.txt:267` 正是 **「“Biological entity falsely projecting stolen ID. Most likely Wylla Sotain, null entity in possession of VisorForge contraband. Surrender immediately.”」** ——锚点**正确**（该处由 commit `ce426e7b0`，10-10 09:57 修好）。若照旧记录报警即为假红。
- **撤回 ②（计数断言）**：我早段称「`ch04 …md:33` 说“末三问”而原文只有两问」。枚举 `text/ch04_chapter_4.txt:27`：**「What had they done to your body? Were the spores permanent, propagating—perhaps even in LYREBIRD?」**——问号确为 2 个，但 md 自己把三问拆成「从身体 → 永久性与繁殖 → 再问到 LYREBIRD 里」，正好对应句中的三个语义层级，且 `md:33` 的判定「而本章没有作答」经核为真（`.memory/progress/ne-facts-part1.md` 悬置点 7 收录 ch04 L27 的孢子永久性问题原文无解）。故撤回，不算缺陷。
- **同伴报告的假红（重要）**：`.memory/reviews/2026-10-10-null-entity-d步-ch01-08-v2.md` 的 **B-2** 引用 md 文字为「**Four 早已在 ch03:267 当众报出过 “Most likely Wylla Sotain”，她当时没有承认**」，并据此判为「早已」时序写红。但**当前文件里 `grep 早已 "ch03 i woke to fire.md"` 返回空**，md:103 现文为「Four 当众报出 “Most likely Wylla Sotain”（ch03:267）**更在这一句承认之后**」——即顺序**已经写对**（267 > 234）。该条由 `56f7f658f`（10-10 10:10）修掉。**结论：v2 的 B-2 针对的是旧快照，请勿再照它整改。**
- **给主会话的流程建议**：d 步报告之间会互相覆盖。任何二审落笔前必须 `grep` 目标字符串**在当前文件**中是否还在；任何主会话在整改后应把「已修 commit 号」写进报告头，否则下一位代理会重复报警（本次 3 条即如此）。

---

## 四、复核为真、不要改动（部分高价值项，供主会话安心）

1. `ch01 …md:65/67`：`ch01:220` **「…For this to work, we needed eyes on the feed. And for a moment, we had them…But they were thinking.」→ :223 「And then the Edenic Order fucked it up.」** 相邻为真；树苗徽记（`:160`）确在喊话（`:199`）之前；`:229` **「YOU ARE NOT YOUR METRICS.」** 在其后。
2. `ch02 …md:14-16` 系列：`:15/18` trap 出现 5 次；`:21` 是一段**连续**段落（「You sat nursing a cup of synthetic tea…It wasn’t tucked into some hidden cliffside. It sat squarely…」），本块引语自段中起、中文理解与之一致；`:24` **「It screamed ambush.」**；`:54` **「…Corporate code for: the bare minimum to stay alive.」**。
3. `ch02 …md:71-77`：`:114` **「I loved you. I hadn’t told you; I was too frightened.」** 三小句为真；`:117` **「“Sable?” you prompted.」** 是本章第一个 Sable（grep 命中 117 为首）。
4. `ch02 …md:100+`：`:265` 只有 **Sable Alzian**、`:268` **「because you, Wylla, weren’t there」**、`:274` **「“Sable,” you hissed, digging nails into your palm…」**、`:313/319` **「“Wylla Sotain?”」**×2、`:325` **「the bastard couldn’t legally act…」」、`:331` 「You skirted past it toward the door, holding your breath.」、`:358` **「Behind us, the facility exploded.」** 为全章末行——全部逐字为真。
5. `ch03 …md:131`（读者视角提示）：`:432` **「“Where is it?” you hissed. “Where is it, Sable?”」**、`:444`／`:447` **「It replayed at once.」**、`:420` **「It replayed instantly.」** 两次重播与「两句喊话（其中一句喊着 Sable）」为真；「作者不给它归属」为真（见提示型 4，只有 md:10 那半句越界）。
6. `ch04 …md:103`：「punched in random coordinates 之后的所谓二次逃亡，从未发生」＋「Turn around 那一吼已经晚了」——`ch04:488` → `:509` **「“Turn around!” I shouted.」** → `:515/518`，为真（这是全书最漂亮的一条结构判断之一）。
7. `ch05 …md:39`：「Thorned Root 在本章正文只出现这一次」——grep 全章仅 `:27` 一处，为真；`md:79`「本章末行只有两个词 And fired.」——`:117` 为真；`md:47` 的 **EchoScan.459**（`:36` 一带播报）是全章唯一被引号框住的对外台词，`:75` **「Internally, you asked me, All right. What can we do?」** 是 Wylla 本章唯一发声——两条均经 grep 复核为真。
8. `ch06 …md:37`（vessel「至少三处」）——`:27`、`:132`、`:345`、`:405` 共 4 处，「至少」为真；`md:71` 系列：`:204` **「“You offered me an android,” I clarified.」**、`:210` **「…switching LYREBIRD’s settings to project my own voice. Sable’s voice.」** 为真；「本章 Subsidiary 没有任何自主台词」经逐段核对为真。
9. `ch08 …md:39`「本章不解释这艘战舰的前主人」——通读 438 行无任何交代，为真；`md:25`「下一段就给出……thirty mouths」——`:39` **「…LYREBIRD tallied yields fit for only thirty mouths.」** 确为 `:36` 的**下一段**，为真；`md:81`「独立成段的两个词 “Auren Pell.”」——`:255` 恰两词且独段，为真；`md:123`／`:159`／`:162`／`:168`／`:255`／`:351`**「I don’t want to get used to it, you told me. I did not repeat it.」**／`:372` Aliers **「flicked a video file」**／`:420` **「Mine was a blood hunger.」**／`:438` **「“Follow me.”」**（章末最后一句对白）——逐条为真。
10. `ch08 …md:97`「这段影像是 Wylla 发进来的，不是 Aliers 放给“我”看的；Aliers 主动出示的影像在后面 Monk Lorien 那一卷」——`:246/249` 与 `:372` 对照为真（这是本卷最容易被记混的一处，写得对）。

---

## 五、说话人／施动专项（brief 特别要求的「前后 ~200 字符施动关系」）

| 断言 | md 位置 | 原文施动证据 | 结论 |
|---|---|---|---|
| 「she 全章没有明说是谁」 | ch01 md:27 | ch01:15／120／199 均不点名 | 真 |
| 「州长唯一的尊严由 Bravely 给出」＋「Vick flinched」 | ch03 md:91 | ch03 该段施动为 Four tilted its head → Vick flinched | 真 |
| 「Four 当众报出…（ch03:267）更在这一句承认之后」 | ch03 md:103 | 234 < 267 | **真（勿改）** |
| 「我吩咐过 Say nothing」（ch02:328） | ch03 md:103 | ch02:328 **「“Say nothing,” I whispered.」**；ch02:331 你屏息绕开 | 真 |
| 「医护」为 they/them，且认人的是医护 | ch03 md:99-105 | ch03:213 **「…but it was only a medic」**、216／222／228／246 全用 they/them | 真 |
| 「you 已被窒息的冲击震醒 → 叙述者筑 firewall」 | ch03 md:10（已修） | ch03:300 **「That shock snapped you awake」** → 321 **「The Subsidiary reached for you—and tried to get inside.」** → 330 **「…I threw up a firewall and blocked you.」** | **现文为真** |
| 「援军与劫持者同队」／「她成了我体内的乘客」 | ch06 md:101 | ch06:159／165（你在外、我在内） | 前半真、**后半写反 → B16** |
| 「I feel sick」＝Wylla 借来的嗓子 | ch06 md:57 | ch06:120 **「you said—filtered through the Subsidiary’s voice box.」** | 真（「第一个」需限定 → 提示型 16） |
| 「Four 把处刑影像灌进 LYREBIRD」 | ch08 md:10 | ch08:246 **「Four pinged LYREBIRD…」」、:249 「And you sent through footage.」** | 施动者＝Wylla → 提示型 24 |
| 「“我”刚刚以第一人称报过其中一个」 | ch07 md:83 | ch07:162 **「“I’m fugitive Wylla Sotain,” I said」**（说话人是「我」＝Sable，报的是 Wylla 的名字） | 真，且是本章最锋利的一处 |
| 「Aliers 主动出示影像」 | ch08 md:97 | ch08:372 **「flicked a video file」** | 真 |
| 「本章唯一一句被引号框住的对外台词」 | ch05 md:47 相关 | ch05:36 EchoScan.459 播报；ch05:75 为内部提问 | 真 |

---

## 六、跨章指认逐条核（`chNN:LLL` 与 `chNN "引文"` 全部落地）

- `ch01:120`／`ch01:128`（绰号与「so lame」）→ 逐字命中。
- `ch01:51`（Pell 是内应）＋ `ch08:258` **「Pell had slipped us the codes for BSMC-07, the lifeline that let us blast the VisorForge–Martial Syndicate alliance across Federation feeds.」** → 「Pell 在 ch01 已埋内应」为真。
- `ch02:259–268`（LYREBIRD 被戴到活人头上、腔体里的空旷）＋ `ch03:306–312` **「That was its head.」** → ch03 md:117 的跨章技术线为真。
- `ch02:277`（设施广播里只闻其声的女声）＋ `ch03:441` **「It was her, that measured voice from the facility.」** → 为真。
- `ch02:280` **「…a system that does not require consent.」** → 「consent 一词在 ch01–ch08 的三次落点」枚举完成（280／ch05:84／ch13 一处，后者在范围外）。
- `ch03:432`／`ch04:33`（Vick 名字被 you 二次使用）→ 逐字命中。
- `ch04:27`／`ch03:390`（缝 vs  heal）→ 见提示型 10。
- `ch05:69/72` ↔ `ch06:105` → 见提示型 17。
- `ch06:405` ↔ `ch07:162` ↔ `ch17:27`（fugitive 归属）→ 见 B16 说明，「货品」半句为真。
- `ch07:105` **「the only leverage we have is me—LYREBIRD.」** 为全章唯一第一人称自等式（grep 复核）→ 为真。
- `ch07:153` 的 `Earth` 为全章唯一 → 为真。
- `ch08:15`／`:48`（belly／open veins 解剖隐喻链）→ 为真。

---

## 七、与同伴报告 `.memory/reviews/2026-10-10-null-entity-d步-ch01-08-v2.md` 的对账

**该报告自报：阻断型 3／提示型 16／假红型 0。**

1. **已修复、双方都应撤销**：v2 的 **B-1**（ch03 md:10 firewall／醒来顺序）与我早段的同名项，均已被 `56f7f658f`（10:10）修好——现文正确，请勿再改。**B-2**（ch03:103「早已」）针对的是**旧快照文本**，现文件不含「早已」，且现文时序为真（见 F2）。v2 的 **B-3**（ch05 md:77「上一章」）亦已修好。
2. **双方一致（本报告已独立复现并给出自己的逐字证据）**：ch01:35（我 B1／其 P-1，我上调为阻断）、ch01:57（我 B3／其 P-2，上调为阻断）、ch02:57（我提示 2／其 P-3）、ch04:10（我提示 9／其 P-6）、ch04:81（我 B10／其 P-8，上调为阻断）、ch04:93（我提示 12／其 P-7）、ch05:77 倒数第二（我 B13／其 P-9，上调为阻断）、ch06:57（我提示 16／其 P-10）、ch06:77 第三人称化（其 P-11；我核 `ch06:147` 全篇第二人称、无第三人称代词，但同块 `md:79` 已把「借用了第三人称」自标为共情姿势的比喻，故我与 v2 同样**只记不改**）、ch06:101「上一章结尾」（我 B15／其 P-12，上调为阻断）、ch07:12（我提示 23／其 P-13）、ch08:23（我提示 25／其 P-14）、ch08:37（我 B19／其 P-15，上调为阻断）、ch08:67（我 B20／其 P-16，上调为阻断）。
3. **分级分歧（建议按本报告上调）**：
   - ch04:81 无据因果 → 我判 **阻断型 B10**（v2 判提示 P-8）：不是「程度」问题，是把两条无关证据接成因果。
   - ch05:77「倒数第二」→ 我判 **阻断型 B13**（v2 判提示 P-9）：序数可核，111 行是倒数第三。
   - ch06:101「上一章结尾」→ 我判 **阻断型 B15**（v2 判提示 P-12）：位置可核且指向错误。
   - ch04:93、ch06:57、ch08:23、ch08:67 之外的 ch06:101「体内的乘客」→ 我判 **阻断型 B16**（v2 未报）：容器关系写反，是本类里读者最容易被带跑的一种。
4. **v2 有、本报告的不同处理**：
   - **ch02:11（其 P-4「在录像前跌为恐怖与羞耻，末段被压成一句法律判断」）**——我复核 `md:12` 引用的跨章指涉（ch01:187 **「“Sable,” you murmured.」**、ch01:51 Pell 内应）与 ch02:259–268 录像段落，逐字为真；「羞耻」安在录像处属导航层的压缩表述，不构成可核事实错误，**本报告不列为缺陷**（与 v2 同为「只记」处理）。
   - **ch03:77「三段呼号」（其 P-5）**——**双方都需要先定口径**，但**这一条应当整改**。原文实际是 `text/ch03_chapter_3.txt:93` **「“No!” she screamed. “You did this!”」**（一个自然段、两句呼喊）、`:96` **「“Wait!” someone said, but a seam was opening in Four’s arm, light swelling in the cavity.」**、`:99` **「A flare.」**。按**自然段**算是 2 段（v2 对）；按**呼喊语句**算是 3 句（No!／You did this!／Wait!，md 的「三段」勉强成立），但**括号里只列了 “No!”、“Wait!” 两句，漏掉了 “You did this!”**，而且 **“You did this!” 是有主有谓的完整句**，与「几乎连不成句」的形容冲突。建议改为「先给三段呼喊（“No!”／“You did this!”／“Wait!”），其中只有两句是喊不出下文的光杆呼号」。
   - **ch04:10「一小时后」（其 P-6）**＝我的提示 9，**采纳**。
5. **v2 未覆盖、本报告新增（全部为阻断型，除非另注）**：B2（ch01:55 唯一喊话）、B4（ch02:39 人流间隙转嫁）、B5／B6（ch02:47／77 计数）、**B7（ch03:29 感官排序）**、B8／B9（ch04:23／47）、**B11／B12（ch05:33 破折号、ch05:67 块外引用＋「同一段」）**、B14（ch06:45 排版）、B16（ch06:101 容器反转）、**B17（ch08 原句 7 引语截短，本次最高优先）**、B18（ch08:95「说了两遍」）、B19／B20；提示型新增 ch03:10、ch03:117、ch04:33、ch05:25、ch05:27、ch06:47、ch06:87、ch06:89、ch07:23、ch07:73、ch07:83、ch07:12。
6. **正面冲突（必须写明）**：v2 主张「检查 1（引语覆盖率）：主会话已全书跑过，ch01–ch08 该层 0 缺陷，本报告不重复报」。**本报告以 ch08 原句 7（B17）证明该层并非 0**：引语止于 `ch08:276` 的第一句 `I am truly sorry.”`，而同段后半 `Her eyes flickered toward the Subsidiary. “P-please, I—”` 与其后 `:279／:282／:285／:288` 四段被 `ch08 …md:95` 直接当作分析对象却完全不在引语中。此外 ch05:87（B12）、ch05:15（提示 13）、ch06:222（提示 18）、ch03:36/114（提示 5）、ch07:153 后半（提示 21）共 **5 处轻度／中度的「分析引用块外文本」**。覆盖率层在 ch01–ch08 的实测结论应为：**阻断型 1 处 ＋ 提示型 5 处 ＝ 6 处**，不是 0。

---

## 八、整改优先级建议（只列，不动手）

1. **B17（ch08 原句 7）**：补全引语（276 尾句＋279＋282＋285＋288），并把「最后求饶的半句」改为「念完稿子后那半句没说完的求饶」。这一条不修，本章最有力量的一处「流程化谋杀」分析在页面上是**无根**的。
2. **B12／B11（ch05）**：为原句 5 增引 `ch05:87`，或删「同一段里」；把 md:33 的「破折号后补一句」改为「另起一行、孤零零的同位语」。
3. **B16／B15（ch06 md:101）**：把「她成了“我”体内的乘客」改为「“我”成了她身体的占有者，而她被关在另一具壳里，求“我”开门」；「上一章结尾」改「上一章前半」。
4. **六个计数／排版项（B5、B6、B9、B14、B18、B19、B20、B13）**：全部是数字与排版改词，一行一改，成本极低但影响可信度最高。
5. **B1／B2／B3／B8**：序数与「唯一／第一」类，建议一律改成「本块第一句」「本章第一次以全大写压过来的喊话」「26 段之后」。
6. **B4／B10**：两处自造因果，删连接词或改为读者可见的并置。
7. 提示型 25 条可按 chapter 分批处理，其中 9 条属「同段下一行已自我限定」，仅需限定量词（一律／第一次／每次／几段之隔／中段）。

---

## 九、已核对块数与引语总条数（自数）

**61 个 `> **原句 N:**` 块／112 段引语，全部逐对核对，无抽查。**

| 章 | md 文件 | 块数 | 引语段数 |
|---|---|---|---|
| ch01 | `ch01 the game begins.md` | 8 | 9 |
| ch02 | `ch02 desire outweighed the risk.md` | 8 | 21 |
| ch03 | `ch03 i woke to fire.md` | 8 | 26 |
| ch04 | `ch04 part of the subsidiary was in your head.md` | 8 | 13 |
| ch05 | `ch05 we revolted together.md` | 6 | 8 |
| ch06 | `ch06 i feel sick.md` | 8 | 12 |
| ch07 | `ch07 welcome to the thorned root.md` | 7 | 7 |
| ch08 | `ch08 a feast just out of reach.md` | 8 | 16 |
| **合计** | 8 章 | **61** | **112** |

计数口径：`块数` ＝ 文件中匹配 `^> \*\*原句` 的行数；`引语段数` ＝ 所有以 `> ` 开头且非空分隔符的行数（含每块首行的 `原句 N:` 那一行）。上表由我对 8 个 md 文件逐文件 grep 计数得出（非估算、非报 0）。

除 61 块的四检之外，本报告另核了 8 章的 `本章导航`（一句话概括／人物弧线／叙事手法）与 `读者视角提示` 中的可核断言，因此阻断型 B8（ch04 md:23）等导航区问题也在列。

**过程声明**：本代理全程只读；未编辑书目录任何文件、未生成除本报告外的任何文件、未执行任何 git 写操作（仅 `git log`／`git show` 只读）。本报告引用的每一处 md 行号与 `text/chNN:行号` 均出自本次会话的实际读取输出（铁律 4），并逐条确认所引 md 两行确实相邻于同一文件（铁律 5）。
