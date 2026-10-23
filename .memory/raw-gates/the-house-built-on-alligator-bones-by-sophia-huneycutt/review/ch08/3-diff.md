# ch08（书内 Chapter Seven）深审 R3/R4 三张单子

素读基线：`review/ch08/1-suread.json`（64 条事实／0 MISS，只读 `text/ch08_chapter_seven.txt`，写完才开 md）
机器层：`review/ch08/2-machine.json` → verdict `ok`（blocks 8 ∈ target [5,9]；segments 8／MISS 0；words 2765）
直撇号探针：`/tmp/apos.txt` 未列 ch08 ⇒ 0 站

## 🟥 阻断（9）

### C-08-1 计数断言错：「七个词」实为五词
- md:24：**「首个明喻只用七个词就把「怎么开车」和「怎么说话」焊在一起」**
- 原文逐字：`text/ch08_chapter_seven.txt:9` — `Gazzie drove like she spoke.`（Gazzie／drove／like／she／spoke＝5）
- 判据同 ch06 C-06-3（同卷内多数计数正确，个别数错）。改法：「五个词」。

### C-08-2 想象图景的数量被改写：「一排」红顶谷仓
- md:10：**「Dart 原以为会见到一排红顶猪棚式谷仓」**
- 原文逐字：`text/ch08_chapter_seven.txt:12` — `I’d resorted to my imagination, picturing Greer Fine Alligators as a single, long, red-roofed barn, like a commercial pigsty.`
- 判定：原文明写 a single（一座长条红顶棚，像商用猪圈）；「一排」把它复数化，恰好抹掉「一座 vs 一座建筑群」的量级落差——而这个落差正是 md:14 与 md:36 自己要用的「想象—现实」判据。

### C-08-3 全称断言有反例：「数字全部经对话交付」
- md:14：**「数字全部经对话交付（三十五分钟／二十到三十美元／十英尺／三场二万五／此场一万五／年杀一万四）」**
- 原文逐字：`text/ch08_chapter_seven.txt:12` — `It was only thirty-five minutes away, but I drifted off, waking to the crunch of gravel.`（叙述层，非对话）
- 旁证：`text/ch08_chapter_seven.txt:96` — `the entire pond was surrounded by a fence about ten feet high`（十英尺先以叙述给出，:123 才由 Dart 在对话里复述 `“It’s ten feet tall,” I said, alarmed.`）
- 判定：括号清单第一项即出自叙述层；「全部」需改为「规模类数字（偷卖价／两万五／一万五／一万四）经对话交付，路程与围栏尺寸由叙述层给出」。

### C-08-4 台词归属：Harrison 在本章零台词
- md:13：**「Nova 与 Harrison 只给外貌、几句原话（Harrison 已清理了「一部分」、正在等 Gazzie），原文未写他们与谁是什么关系」**
- 原文逐字：
  - `text/ch08_chapter_seven.txt:42` — `“—out back.” The woman continued her monotone conversation without a glance in my direction. “Harrison’s already cleaned up some of it, but he’s waiting for you.”`（说话人＝Nova，不是 Harrison）
  - `text/ch08_chapter_seven.txt:174` — `We passed two rectangular barns…` 前一行 `Zipping toward the silver-roofed barns, we overtook another worker carrying a bucket. Harrison. Gazzie bobbed her head in his direction. He lifted his hand to her, then, presumably seeing me, frowned.`（他在全章只有一个抬手与一个皱眉）
- 判定：Harrison 本章没有任何直接引语；「几句原话」若指两人共有则无据。另需注意 :156 `On the far side of the breeding pond, a man in a neon-green shirt reached into a plastic bucket.` 与 :174 的 Harrison 是原文的两次出现，未标明同一人——「只给外貌」若挂在 neon-green 衫上即合并两人。改法：「Nova 只有外貌与两句原话；Harrison 本章不出声，只被转述（:42）与一次抬手、一次皱眉（:174）」。

### C-08-5 施事混淆：把她的动作算进鳄鱼的动作链
- md:84：**「幻想的动词按鳄鱼的动作链逐级升高（push → watch → nip → rip off）」**
- 原文逐字：`text/ch08_chapter_seven.txt:288` — `I could push her into the algae-infested pen, watch the alligators nip at her, rip off the delicate flesh of her fingertips.`
- 判定：push／watch 的施事是叙述者（她推、她看），nip／rip off 才是鳄鱼；「鳄鱼的动作链」把两个施事并成一个。改法：「动词按她→鳄鱼的移交升高：她推、她看，鳄鱼咬、撕」。

### C-08-6 分析层语法／词类误称（两处）
- md:64：**「『brimmed』的宾语本该是水，这里装的内容物却是鳄鱼」**
  - 原文逐字：`text/ch08_chapter_seven.txt:114` — `The water brimmed with alligators.`
  - 判定：The water 是主语，brim 此处不及物、后面是 with 短语；不存在「本该是水」的宾语位置。可改：「主语本该只是被盛满的东西，这里盛出来的却是鳄鱼」。
- md:74：**「『do-gooder』这个前缀在听科学家论点之前，先把她归档成多管闲事的好人」**
  - 原文逐字：`text/ch08_chapter_seven.txt:219` — `A do-gooder scientist tried to tell me light’s better for them`
  - 判定：do-gooder 是名词用作定语，不是「前缀」。判据效果（未听论点先归档）✓，只需换掉词类名。

### C-08-7 否定式断言与紧邻原文相悖＋漏本章末句
- md:96：**「本章结尾的两处「不想回」（农场、Greer House）都还没有配上一个「想回哪」。」**
- 原文逐字：`text/ch08_chapter_seven.txt:303` — `I didn’t want to return to the farm, and I was beginning to dread returning to Greer House, too. A life alone in Savannah might be worth the distance from my grandmother.`
- 判定：被引用的 block 之后同一行就是「想回哪」的替代项（一个人在 Savannah 过日子，换开这位祖母的距离）；md:88 的引语恰好在 too 处截断，于是结论建立在自己裁掉的半句上。md:10 概括同样止于「害怕回 Greer House」。
- 取证：`/usr/bin/grep -c "Savannah" "ch08 dart tours greer alligator farm.md"` → 输出 `0`，退出码 `1`。

### C-08-8 漏 :45＋:57：本章唯一的「继承人候选」线索与被提出的处置级别
- 原文逐字：
  - `text/ch08_chapter_seven.txt:45` — `I didn’t like the way she said his name, like he was someone important. I remembered what Gazzie had said about already knowing who would inherit the farm. Listen, missy, I’ve chosen who’s next, and it’s not you. It couldn’t be an employee, could it?`
  - `text/ch08_chapter_seven.txt:57` — `“I don’t know, Ms. Greer. I’ve been at my desk. Should I call the police? Or—”`
- 判定：本章第一次把 Harrison 与继承人名单并置（并直接回引 ch06:285 那句宣告），是读者对「下一个是谁」的第一个候选；Nova 提出报警则标出「出了什么事」的严重级别。md 只写「原文未写他们与谁是什么关系」（此句本身 ✓），但两条线索内容均未登记；`/usr/bin/grep -c "police" "ch08 dart tours greer alligator farm.md"` → 输出 `0`，退出码 `1`。

### C-08-9 漏 :234：嘶声只朝 Gazzie 起，与她给自己找的解释
- 原文逐字：`text/ch08_chapter_seven.txt:225` — `As Gazzie strode down the barn, a chorus of hisses erupted.` ／ `:228` — `It was chilling, that sound. Unnatural, almost like a coordinated protest.` ／ `:234` — `I walked tentatively forward, waiting for the hisses to follow me as well, but they didn’t. They only hissed at Gazzie, like they knew she was responsible for their imprisonment. I reasoned they must always hiss at the first person in the barn, that they were probably surprised.`
- 判定：本章最强的一处「动物替这个家说话」，并与 md:94 用到的「像小青蛙」同一段落；叙述者随即自我合理化（第一个人／受惊），正是本卷反复使用的「直觉先落地、解释后排队」形态。md 全篇无一声响描写命中：`/usr/bin/grep -c "hiss" …md` → `0`，退出码 `1`；`/usr/bin/grep -c "嘶" …md` → `0`，退出码 `1`。

## 🟨 提示（8）

- P-08-1 md:10「她抓住藻类事故打断前的最后一个空当」／md:13「挑藻类事故的空当」——成因错置：:267 `A golf cart whirred in the distance. This was probably my last chance to ask about Mama before we were interrupted.` 打断源是远处驶来的球车；藻类事故（:252-:258）已经由对讲机处理完。
- P-08-2 md:11「惊惧（会爬出围栏的鳄鱼与四位数）」——本章规模数字皆五位（25,000／15,000／14,000，:132/:138）；建议「五位数的规模」。
- P-08-3 md:84「与满章的粗粝（泥浆、锈味、通电围栏）成对照」——锈味无出处：本章气味只有 :36 `like shredded paper and hand sanitizer`、:90 `smelled vaguely of rotten eggs`、:198 `the earthy scents of mud and stagnant water`（`/usr/bin/grep -c "rust" text/ch08_chapter_seven.txt` → `0`，退出码 `1`）。
- P-08-4 块 6 引语（md:68）止于 `and they grow just fine.`，裁掉同一 :219 句内的 `Breeders get to live an extra year or so in the ponds.` 与叙述者判词 `She said it matter-of-factly, like their living conditions were out of her control.`——后者正是 md:74「顺手塞进」论断的证据位置，建议把这两句并入引语或写进分析。
- P-08-5 跨章术语不统一：closet 在 ch07 md 作「壁橱」、本章 md:11 作「衣橱」，前章另有「衣柜」写法；closet wall／Polaroid 盒这类承重道具建议全书一档。
- P-08-6 漏 :111 `“About seven inches. Unfortunately,” she added, looking anything but regretful, “Ginny tells me you’ll be gone by hatchling season.”`——Virginia 向外传递了叙述者的停留期限；词表 md:106 的例句带出「her comment」却未说明那句 comment 是什么。
- P-08-7 漏 :294 `Sure, she’d be upset—she was so sensitive about her niece—but I could probably convince her to tell me what I wanted to know.`——`her niece` 是又一处关系凭据（与 ch06:165 `her sister` 同一谱系）；也是她「换路径」时的成本估算。
- P-08-8 漏三处小的产业信息：:99 `“And not wholly efficient, but I like tradition.”`；:105 `In August, tourists pay to help take hatchlings out of their eggs… You should get a whiff of a hatchling barn in full summer heat.`；:264 `“Let nature get out of control,” Gazzie replied, “and it’ll swallow you whole.”`（本章 Gazzie 最短的一句自我陈述）。

## ⬜ 假红／不报（本轮已核）

- md:13「原文未写他们与谁是什么关系」✓——Nova 无姓、无关系；Harrison 本章无关系说明（正确登记）。
- md:10「这一幅里她的眼睛像烧尽的煤」✓ :81 `her eyes were hollow—less like burning coal and more like coal, burned`。
- md:10「数清了规模…此分支约一万五千」✓ :132 `This branch has about fifteen.`（一万五为中文补量，与「twenty-five thousand total」同段）。
- md:10「水温决定性别」✓ :207 `temperature determined the gators’ sex… so they kept most of the water warmer`。
- md:12「Gazzie 用背熟的口吻」✓ :144 `In a rehearsed tone`。
- md:84「『Yet again』承认这不是第一次」✓ :288；且与 ch06:31 `I was not the kind of woman who snaps at people` 呼应，非凭空。
- md:84「Hateful woman. 只有两个词」✓（计数正确，与 C-08-1 形成对照，勿一并改掉）。
- md:54「another 一词就说明等身画像不止这一幅」✓；md:56「本段之后的下一段她还看了一眼那双眼」✓ :81。
- 引语逐字：8 块／8 分片全命中（机器层），本章无「…」拼接块，无需 verify_fragments_indep。
