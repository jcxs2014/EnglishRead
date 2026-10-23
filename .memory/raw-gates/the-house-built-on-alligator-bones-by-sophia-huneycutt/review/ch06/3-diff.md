# ch06（书内 Chapter Five）深审 R3/R4 三张单子

素读基线：`review/ch06/1-suread.json`（74 条事实，0 MISS，只读 `text/ch06_chapter_five.txt`，写完才开 md）
机器层：`review/ch06/2-machine.json` → verdict `ok`（逐字全命中；引语块 10 条；无门禁报警）
直撇号探针：`/tmp/apos.txt` 未列 ch06 ⇒ 本章分析层无「非逐字(直撇号)」站点（全局 44 处不含本章）

## 🟥 阻断（10）

### C-06-1 亲属称谓凭空：把 Gazzie 写成 Virginia 的母亲
- md:10：**「Virginia 夹在母亲与客人之间两头圆场」**
- 原文逐字：
  - `text/ch06_chapter_five.txt:165` — `Aunt Virginia stepped out from behind her sister. “Now, Gazzie. Don’t scare her off when she’s just arrived. Dart, you’ll have to forgive your grandmother.`
  - 旁证 `text/ch08_chapter_seven.txt:192` — `As I slipped out of my seat, I considered the sisters’ dynamic.`
- 判定：本章唯一交代两人关系的一句是 sister（叙述者同时收到「your grandmother」这层称谓，见 C-06-2 说明）。写「母亲」在本章无出处，且与本章自己的证据相反。排行（谁年长）原文不写，只能写「姐妹」。

### C-06-2 全称断言跨章失据：「辈分关系……不是出自任何家人的介绍」
- md:64：**「辈分关系（great-great-grandmother）出自一个花园工人的嘴，而不是出自任何家人的介绍——信息的来路从此带着标记」**
- 原文逐字：
  - `text/ch04_chapter_three.txt:279` — `She held up her hand. “Your great-great-grandmother invested in railroads in the late 1800s.”`（说话人＝Virginia 姨妈，家人）
  - `text/ch04_chapter_three.txt:282` — `My mind flashed to the woman in the portrait—those hard eyes, that curling lip. Was Ida my great-great-grandmother?`
  - `text/ch05_chapter_four.txt:219` — `Ida had to be a family member, if not my great-great-grandmother herself; otherwise, why keep so many images of her around?`
  - `text/ch06_chapter_five.txt:90` — `“The resemblance between you and your great-great-grandmother.”`
- 判定：这一辈分由家人（Virginia）在 ch04 已当面说出，叙述者本人也已在 ch04:282 把它与画像挂钩、在 ch05:219 用条件式悬着。Harrison 的独创处只有两件：把「像」说出来（:90）与把 Ida↔曾曾祖母钉死（此前一直是 if not／was Ida…? 的条件式）。故「不是出自任何家人的介绍」为假。

### C-06-3 计数断言错：两处「两个词」实为三词
- md:74：**「『Not a compliment.』两个词的更正紧跟在她道谢之后」**
- md:84：**「只留下一个数字般干净的否定——it’s not you，两个词把前面所有款待的话全部作废」**
- 原文逐字：`text/ch06_chapter_five.txt:159` — `“Not a compliment.”`（Not／a／compliment＝3）；`text/ch06_chapter_five.txt:285` — `“Listen, missy, I’ve chosen who’s next, and it’s not you.”`（it’s／not／you＝3）
- 判据一致性：同卷 md:24 对 `This was the original.`（:21）写「短短四个词」＝正确。⇒ 不是口径不同，是这两处数错。

### C-06-4 凭空事件：替「Damp」填上洗澡
- md:44：**「Damp 一词顺手交代他冲过澡，却半个字不提为什么」**
- 原文逐字：`text/ch06_chapter_five.txt:36` — `He’d cleaned himself up. Damp, his hair was more brown than gold, forming loose curls that grazed his eyebrows.`
- 判定：全章无洗澡／水源／淋浴的任何字样（`/usr/bin/grep -n "shower" ch06_chapter_five.txt` 空）。原句本身只给「收拾过了＋头发潮」；句子后半 already 说「半个字不提为什么」，前半却又替它填上一个具体事件，自相矛盾且凭空。

### C-06-5 词源断言无据：「spitting image 的字面是『吐出来的影像』」
- md:76：**「『spitting image』的字面是『吐出来的影像』——与前面墙上那张『要爬出画布』的脸正好共享同一个意象方向：长相不是遗传，更像是一种外溢。」**
- 原文逐字：`text/ch06_chapter_five.txt:153` — `“You’re the spitting image of her.”`
- 判定：成语字面拆解属外部语言学断言，本库不背书（该 idiom 的 `spitting` 并非「吐出」义的可拆成分）；且后半的「不是遗传，更像外溢」整层结论靠这条词源撑。建议只保留「叙述者在同一章里两次把长相写成会自己离体移动的东西（:27 `like she was trying to crawl out`／:153 spitting image）」，不做词源声明。

### C-06-6 章内时序：把开席那一步挪到餐桌冲突末尾
- md:104：**「桌子刚刚才摆上冷虾沙拉和橙子，此刻多接住一层看不见的湿。」**
- 原文逐字：
  - `text/ch06_chapter_five.txt:198` — `“How are you settling in, honey?” Aunt Virginia asked, digging tongs into a salad piled with cold shrimp and chopped oranges.`（开席）
  - `text/ch06_chapter_five.txt:207` — `Aunt Virginia smiled but didn’t add anything as she distributed salad onto Gazzie’s plate, then mine.`
  - `text/ch06_chapter_five.txt:240` — `Gazzie spoke without looking up from her half-eaten salad. Aunt Virginia and I had barely made a dent in ours.`
  - `text/ch06_chapter_five.txt:303` — `…like my sadness was leaking onto the dining table.`（md 所指时刻）
  - `text/ch06_chapter_five.txt:306` — `Instead, she speared the last few leaves of her salad.`
- 判定：沙拉在开席时（:198/:207）就已上桌，:303 已是一顿饭将尽（Gazzie 半盘→最后几片）。md:104 的「刚刚才」把开头动作拉到结尾，正是本库缺陷簇第一名（章内时序写反）的形态。

### C-06-7 漏：餐厅三面墙上的三幅画（:192 整块）
- 原文逐字：`text/ch06_chapter_five.txt:192` — `Paintings adorned the three other walls: one realistic still life of a doll sitting at a table set for tea; a cartoon-style portrait of a woman at a leather-topped wooden desk; an impressionist work of a woman digging underneath a mansion not unlike Greer House. The two women wore similar Victorian-era dresses, but the painting styles made it difficult to tell whether they were the same person. They made me uncomfortable, like they were in on a joke I didn’t understand.`
- 判定：本章唯一一整组「画中人」单元，含一个直接压本书题面的意象（女人在类似 Greer House 的大宅下面挖掘）＋「是否同一个人无法判断」＋「被排除在笑话之外」。md 全篇（导航／10 块／词表／总结）0 次命中：`/usr/bin/grep -c "三幅\|画\|digging" "ch06 long lost granddaughter meets gazzie.md"` 无该单元。

### C-06-8 漏：Virginia 搓手腕＋原文自标的「此后久久留存」（:129）
- 原文逐字：`text/ch06_chapter_five.txt:129` — `She shot me an encouraging smile, but her right hand rubbed her left wrist. That image lingered for a long time afterward: her gingerly holding her hand to her chest, like she was protecting a bird with a broken wing. I figured she’d twisted it picking something up.`
- 判定：叙述者用 `That image lingered for a long time afterward` 亲自在场标记的未来回收点，紧跟一个折翼鸟比喻，再紧跟一个她自己给出的物理解释（扭伤）——三项一体，md 0 次。与 ch05 已登记的「护着折翼鸟＝保护」母题直接相关。

### C-06-9 漏：phosphate deal（:273）
- 原文逐字：`text/ch06_chapter_five.txt:273` — `“Farming isn’t just any old business. Alligator farming, especially.” Her eyes flicked toward Aunt Virginia. “I don’t have time to teach someone the fundamentals. We have a lot going on at the farm. Not to mention the phosphate deal. You know that, Ginny.”`
- 判定：Gazzie 拒绝教她的第二条理由里唯一的生意新线索，承接 `text/ch04_chapter_three.txt:63`（`Plus, she’s in the middle of an acquisition. You know how it is.`），并给 Virginia 那句 `You know that, Ginny` 的称呼落点；md 与词表均 0 次。

### C-06-10 漏：四年级 Savannah River 游船与 Michelle 在场（:234）
- 原文逐字：`text/ch06_chapter_five.txt:234` — `“My fourth-grade class took a boat down the Savannah River. It was my highlight of the year.” Michelle had stood at the helm, butterfly hair clips glittering in the sun as her eyes snaked back to me in my seat.`
- 判定：本章叙述者唯一一次让 Michelle 以「活着、站在舵位、回头看她」的形态出场；与 `text/ch04_chapter_three.txt:168`（`Michelle had been discovered on a nearby shore; according to a news report, one of our classmates had nearly tripped over her body.`）构成同一个人的两次在场，属「在场者漏写」类。md 0 次。

## 🟨 提示（14）

- P-06-1 md:24「尺寸的参照物是她自己的床头柜」——原文参照物是床头柜上那幅画（:24 `at least twenty times the size of the one on my bedside table`），不是柜子。
- P-06-2 md:24「她床头天天看的那幅」——「天天」＝补写频率；本章只写它摆在床头柜上。
- P-06-3 md:36「本章稍后会给出一个纯粹物理的说法」——电路说法在 ch05 已给出（`text/ch05_chapter_four.txt:156` Virginia 的解释）；本章只回指（:30 `And Aunt Virginia had already explained the house’s dated electrical system`）并补一句「也许有的房间线路好些」（:108）。
- P-06-4 md:70「被改之人（Mama）」——原文是叙述者自己的对冲（:153 `Still can’t believe she changed her last name.” Mama, presumably.`）；md 去掉 presumably 写成定称。建议作「（她想来是 Mama）」。
- P-06-5 md:84「也说不选的原因」——现写法读作「说出没选她的原因」，应为「也不说没选她的原因」。
- P-06-6 md:100「自我认识借敌人的眼睛完成」——原文无敌人定性（:303 `through Gazzie’s eyes`）；建议「借那位不肯认她的祖母的眼睛」。
- P-06-7 md:104「『孤零零』『对家人如饥似渴』是两个残缺短句」——原文 `Alone, desperate for family.`（:303）是一句里的两段；md:100 的中文理解本身也按一句带逗号处理。
- P-06-8 md:114「真实得不需要别人在场」＋md:116「恶意不需要观众」——:348-351 `My eyes flicked to Gazzie, who scowled at me… I took pleasure in Gazzie’s growing frown`，快感发生时对方在场；「不需要观众」只在章末对鳄鱼皮那一跺成立（:363-366）。
- P-06-9 md:14「自我辩白句……压在每轮情绪末尾」＝全称；本章可数三处（:54 `No, I assured myself`／:201 `I reminded myself of the person I wanted to be`／:351 `I told myself… not at all`），其余情绪段落用的是别种自我约束（:12 不想被当作病弱、:45 不是会呛人的人）。
- P-06-10 漏 :15 `nearly tripping over an orangewood cane leaning against the wall, an alligator head carved into its handle`——本章唯一的道具级怪笔触（绊她一下的鳄鱼头手杖），可并入 C-06-7 的补写或单列一句。
- P-06-11 漏 :150 `Again, I felt that someone was watching us, waiting to see how our first meeting would fare.`——注视母题在本章的第二／累计第三次落点（前两次 ch05），md 未收。
- P-06-12 漏 :102 `I couldn’t believe I’d let myself slip. The long travel day must have thrown me off. Or the nap.`——她替自己失态找的第一组外因，与 :351 的辩白同构，可支撑 md:114 的「递减排列」论。
- P-06-13 漏三处小信息单元：:210-:216 蔫掉的天堂鸟与「这里的花不持久，大概是空调」；:321 `“We need to decide on something for the solstice party, too.” A vague threat lay in those words.`（Virginia 用来把 Gazzie 支进厨房的筹码）；:249 `My class had visited in the sixth grade, pre-homeschooling, and I distinctly remembered rushing by a habitat filled with green scaly bodies that looked like Scooby-Doo monster suits.`（`pre-homeschooling` 是叙述者身世的一句）。
- P-06-14 词表：⭐常用 sweatshirt 与 sneakers 两行共用同一例句（:36）；本章 `phosphate deal`、`Gim Gam`（:144）、`hanger-on`（:303）、`solstice`（:321）未进任何档位。

## ⬜ 假红／不报（本轮已核，勿在下轮重复报警）

- 「长回来的孙女」＝译者选定的固定译法，md 全篇一致（导航 md:10、块 4 md:50、块 7 md:80、总结）；语义偏斜（long-lost＝失散多年／素未谋面）在快审已作为译法层问题登记，深审不升级为阻断。
- md:13「『那就好』三个字说得响亮」——对应 :354 `“If it’s really no trouble, that’d be great,” I said brightly.`；「三个字／响亮」自洽，不报。
- md:14「Virginia 说出『your grandmother』这层关系」——:165 逐字在，✓。
- md:26「本章之后同一件东西还会分出『两个版本』」——已核后文确有原作／复制品分裂：ch13:150 `another copy of Ida’s primary portrait`、ch16:279 `She only works on the originals, the ones Ida herself commissioned`、ch30:114 `We don’t have enough originals to hang up at the farm`、ch43:15 `the single original portrait containing only a few strands of hair` ⇒ 跨章预告成立，登记为「已核实为正确」。
- md:44「标签 unpleasant 先行，理由由谁也不负责提供」——本章内确无解释（理由在 ch05:84-96 的打量与 frown），措辞可容，不报。
- md:46「这个人的名字要到本章后段才出现」——:168→:171 ✓；:36 亦未出现姓名 ✓。
