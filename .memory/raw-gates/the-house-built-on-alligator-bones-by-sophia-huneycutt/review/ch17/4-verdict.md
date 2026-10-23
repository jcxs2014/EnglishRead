# ch17 深审判定表（R5）

章：`ch17 sneaking into uncle leon room.md`（书内 Chapter Sixteen，H1 `# 17. Chapter Sixteen` ✓）
语料：`text/ch17_chapter_sixteen.txt`（126 行／9,785 B／words 1,706）
流程：R1 素读（**82 条事实／0 MISS**）→ R2 机器层（`chapter.sh` 退出码 0）→ R3/R4 → 本表

## 四组报数

| 组 | 判据 | 结果 |
|---|---|---|
| 逐字 | 引语块 5／片段 5／查无 0；`quote_long` 0（无跨段拼接块，书级 313 条／443 片段口径条数不变）；词表 16 行例句展平逐字 0 MISS；直撇号 **0 个** | 🟢 全绿 |
| 对应 | 5 块 anchor 全在素读表内；缺项：:12/:15（Virginia 外出的性质与 Henri 线）、:60 `And by everything, I mean nothing.`、:69 `He looked sick. Or scared.`、:117 `someone stepping into the room`、:99 `like I was an errant dog`、:24/:111 办公室位置、:12 三人小群 | 🔴 阻断 3（C-17-6／7／8）＋提示 4（T-17-4／5／6／7） |
| 形态 | nav 5 项 ✓／子项四项 ✓／blocks 5 ∈ 建议 [3,5] ✓／struct_bad／empty_quote／keyword_bad／cjk_low／template／hole 全 0 | 🟢 全绿 |
| 断言 | 全称断言×2（副词撑住／被事实逐一推翻）／悬置径判（血衣）／跨章「第一次」（Harrison 松动）／评价与同文件相抵（受制） | 🔴 阻断 5（C-17-1／2／3／4／5）＋提示 3（T-17-1／2／3） |

**本章合计：阻断 8 ／ 提示 7 ／ 假红-不报 8 ＋ 字形站 0**

## 缺陷形态归因

- **本章把「悬置」当卖点，md 的两处红恰恰是把悬置写实**：`Mud—or blood.`（:75）被写成「血衣」，`He looked sick. Or scared.`（:69）被收成「忧郁」。同一判据在 ch16 表现为「指代径判」，在 ch17 表现为「两可项被单边化」⇒ 建议预筛规则：**凡原文出现 `A—or B.`／`. Or B.` 型二选一句式，逐条核对 md 是否只留了一边。**
- **「每一次／逐一／全部」型全称断言再次成片**（C-17-1、C-17-2，另 T-17-2 的辖域过宽）。本库连续多章的第一名仍是全称与计数；ch15 提出的「跨章『第一次』先枚举」本章再度命中（C-17-4）。
- **同文件两处口径不一致＝自查报警信号，本章出现 3 次**：血衣（md:14 vs md:10 vs md:56）、受制（md:13 vs md:10）、`contained only` 辖域（md:24 与块内逐字引文）。这条判据成本极低（同文件 grep 同一实体两种写法），建议整改批单列一步。
- **跨章已建立人物／地点第二次未接**：ch16 的 C-16-9（Henri 被记成「出现而不解释」）与本章 C-17-6／T-17-5（Henri 与办公室双双 0 命中）——同一条线在两章里各丢一次 ⇒ 建议为本书建一张**跨章实体登记清单**（Henri、茉莉、嗡鸣、dryer sheets、Gazzie 的办公室、Ida 的原作清单），每章审时按表打勾，而不是靠临场 recall。

## 已核实为正确（下轮勿改坏）

1. `:9` 起意段全链：`Mama’s Polaroid photos hadn’t sated my curiosity about Uncle Leon, and I still hadn’t run into Gazzie.`／`After another failed attempt to ask Aunt Virginia about him, I had no choice but to snoop.`／`Mama’s room held hints of her; surely Uncle Leon’s bedroom would reveal something of him, too.`／`One of the two spare rooms across the hall must have been his.`／`Aunt Virginia appeared, like she had a sixth sense for mischief`／三连差事（`review the upcoming week’s lunch menu`／`hang new curtains in the drawing room`／`rearrange the toolshed`）✓——md:10「好奇没被宝丽来喂饱」逐字对应；`surely`／`must have been` 两处**她的推断**未被写成事实（唯一问题是「两次」计数，见 T-17-1）。
2. `:12`→`:21` 作案窗口：`as I sketched on the patio, Gazzie texted the three-person Greer House thread that she’d be back late from running errands`／`“I’ll be fine,” I assured her, shutting my sketchbook.`／`As soon as I clicked the front door shut behind her ten minutes later, the sounds of Greer House kicked off: floorboards creaking, pipes shuddering. I ignored them all and thundered up the stairs.` ✓——房子的声音在**她出门行动**时响起这一层，md:14「物件主导／感官读数」的结构判读与之一致；词表 `thundered` 行例句逐字。
3. `:24`→`:27` Harrison 的房：`The handle gave immediately`／`a navy room with a prim iron bed`／`A T-shirt lay on a bedside chair, more wrinkled clothes piled in a laundry basket by the closet`／`The bed was unmade, white covers thrown this way and that`／独立短句 `This was where Harrison stayed.` ✓（md:10「先翻了 Harrison 的客房」；无引号的判定句未被写成他的台词）。
4. `:30` 翻找与照片：`that didn’t stop me from searching for a porn stash, a block of cocaine—anything that might taint Gazzie’s view of him.`／`The nightstand contained only earplugs and an eye mask`／`The Son by Jo Nesbø`／`a photograph fell out`／`Harrison, given the golden-brown curls`／`an older man, presumably his father, holding up their respective fish`／`I stuffed the bookmark back in, refusing to be moved.` ✓——原句 1 整块逐字；**照片被当作书签**这一层 md:20 已译出；md:24／md:26 判读见 F-17-2／T-17-2。
5. `:33`→`:36` 气味与想象：`I caught a whiff of dryer sheets and something musky. Cedar, maybe.`／`I could picture him lying shirtless in bed, hair wet from a shower…`／`He probably wore that smug expression even in private, the prick.`／`Blushing like I’d just walked in on him`／`I had to leave before Gazzie saw me and got the wrong idea.` ✓——`Cedar, maybe`／`probably` 两层缓冲在素读已记；md:11「窘迫（闻到 Harrison 气味时脸红）」对应 :36 逐字；柔顺剂味与 ch13:48 同一标记（本章第二次，全书到 ch32:12 仍在用）。
6. `:39`→`:42` 冰门把与「有人在场」：`Slipping through the adjoining bathroom—a copy of mine, with two marble sinks instead of one`／`With a hiss, I drew back. The handle was freezing.`／`opened it a crack`／`In my peripheral vision, something moved.`／`the room seemed several degrees cooler`／`below the ACs’ roar, I could hear Greer House’s low hum`／`Dated electrical system, I reminded myself.`／`People loved to leave them open here, AC be damned.` ✓——词表 `peripheral`／`freezing`／`doorknob` 三行例句逐字；**嗡鸣与 ch15:27／ch14:9 同一条听觉线索在本章第三次出现**（素读 relations 已记，整改时勿与 C-17-1 的副词之争连带删掉）。
7. `:45`→`:51` 摔门与自我解释：独立段 `Behind me, the cracked door to the other room slammed shut.`／`My first thought was unfiltered, fueled by the stress of potentially getting caught: Ida doesn’t want me in there.`／`I shook my head. It was Greer House’s draft, I told myself uneasily.` ✓——原句 2 引语与「先转身、再盯、最后才承认念头」的链条判读正确；:51 的 `uneasily` 定位正确（F-17-3）。
8. `:54`→`:57` 进门：`For the briefest moment, I imagined coming face-to-face with the blurry shape I’d seen downstairs, falling into a pair of black, depthless eyes.`／`my body cringed from a tangible sense of pressure and a gust of even cooler air`／`It was ten times colder than anywhere else in Greer House, and that was saying something.`／`Gazzie could return any minute. I had to hurry.` ✓——「她想象的是**楼下那个影子**」＝对 ch15 黑裙的直接回指（素读 relations 已记，md 未误写成她再次看见）；词表 `tangible` 行例句逐字。
9. `:60`→`:63` 空房：`The room was half the size of Mama’s, with only two windows overlooking the backyard and one the side yard.`／`enough for me to see everything. And by everything, I mean nothing.`／`Rubbing my arms, I turned in a full circle, eyes darting from spot to spot, but the room had been stripped bare.`／`The iron-framed bed had no blankets on it, no pillows. The only thing hiding in the dresser was dust.`／`Despite its emptiness—or because of it—I knew it was Uncle Leon’s room. He’d been erased.`／`Neither option felt convincing.` ✓——原句 3 判读三条（`or because of it` 把逻辑拧反／被动删施动者／`mysterious` 由叙述者挂号）全部成立；词表 `stripped` 行例句逐字。**「他看着像病了。或者怕。」一句的缺失见 C-17-8，勿与本节既有判读连带改写。**
10. `:66`→`:69` 壁橱与照片：`a weak light underneath a narrow, closed door`／`a single forgotten lightbulb lit its sole occupants: three boxes stacked on the floor`／`The top one, a shoebox, held dozens more Polaroid photos`／`Mama skinny-legged and grinning, her hair in a 1980s fluff, complete with high-waisted mom jeans`／`Her arm was slung around a boy about two years younger, dressed in all black`／`His eyes were bulbous.` ✓——md:10「三只箱子」「Mama 与黑衣男孩的合影」数目与主体均对（**搂臂的是 Mama**，素读已订正：原文 `Her arm`）；词表 `occupants` 行的释义「容纳之物；居住者」把双关写全，判优。
11. `:72`→`:75` 茉莉／太阳穴痛／血衣疑物：`The faint scent of jasmine wafted toward me, and a sound drifted in from the hallway—a muttering, like someone talking to themselves.`／`pain sliced through my temples. As soon as I stepped out of the closet, it disappeared.`／`pressing my ear to it, but the hall was silent`／`I might as well snoop as much as possible before she did.`／`a busted portable cassette player and a shirt torn in half, a dark substance crusting the bottom. Mud—or blood.`／`Had they saved the clothes Uncle Leon died in?` ✓——**茉莉第四次在场**（ch09:30→ch15:33→本章 :72），且同样紧贴异常（太阳穴痛＋私语），md 未登记这条线（与 ch15 C-15-6 同族，整改时一并处理）；md:56 对那件衬衫的**中性**表述是正确的（问题只在 md:14，见 C-17-3）。
12. `:78`→`:84` 脚步与锁箱：`tight as a rope around my middle`／`louder, angrier, though still muffled, like someone speaking through a curtain, and off, somehow`／`They thudded softly, almost—wetly, and slightly out of sync.`／`Gazzie must have been outside in the mud at the farm, must have stubbed a toe.`／`This was it. She would burst in, grab me by the shoulders, haul me out.`／`My heart pounded in time with her footfalls.`／`made from some sort of metal. The top jiggled promisingly but didn’t open; it was locked.` ✓——「湿的、不同步的脚步」是本章最硬的异常读数之一，md:12 的「鬼始终不现身，靠……完成『在场感』」成立；词表 `promisingly` 行例句逐字。
13. `:87` 三问：`From whom—Gazzie? Aunt Virginia? Mama?` ✓——原文把「Leon 在防谁」列成三项且都不答；md 未记（并入 T-17 类，整改时**不得替她选一个**）。
14. `:90`→`:108` 被抓：`“What are you doing in here?” a gruff voice barked behind me.`／`Gazzie stood in the doorway, hands in fists.`／`Browning blood splattered her white button-down, and strands of hair fell from her clip.`／`She towered over me in my squat on the floor.`／`“I’m sorry— It’s just— I found out about Uncle Leon. I was wondering—”`／`“Out,” she bellowed. “Out!”`／`despite my vision darkening`／`her chest rose and fell in exaggerated huffs. I tried to apologize, but she wouldn’t have it. She raised her hand, cutting me off.`／`“Go in there again,” she growled, “and I’ll send you back to Georgia faster than you can say boo.”` ✓——原句 4 判读（镜头自下而上／`towered` 量的不是身高而是压迫／`Browning` 的时间感）全部逐字有据；md:10「撂下『再进就送你回乔治亚』」对应 :108 ✓。
15. `:114`→`:126` 回读与翻转：`If she was trying to snuff out my curiosity about Uncle Leon, she’d failed miserably.`／`heart still pounding, I pulled out the stolen Polaroids`／`a melancholy kid who’d grown into a melancholy teen`／`In photo after photo, he was at the edge of things.`／`curled up in a chair, scribbling in a sketchbook`／`My anger began to fade, replaced by determination.`／`he’d have annotated his sketchbooks, left thoughts here and there. Maybe that’s where I’d find a hint about Mama.`／`sneak back into his closet, open the lockbox where he’d likely hidden at least a few of his sketchbooks`／`it had been soft, feminine.`／`Nothing like Gazzie’s voice at all.` ✓——原句 5 的「先果后因／回读全章／归因作废」三判均与 :123/:126 相符；词表 `melancholy`／`disposition` 两行例句逐字。

## 不许裁决（本章内）

- **廊下嘟囔的女声是谁**：:123/:126 只给「轻柔、女声、不像 Gazzie」；候选（Ida／黑裙影子／Virginia／其他）原文一律未指认。**不得与 ch15 的黑裙影子、ch09 浴房的 stranger 合并成同一主体。**
- **门把为何冰冷、门为何自行摔上、房间为何冷十倍**：:39/:45/:57 均未归因；她自己的两种解释（穿堂风 :51、老旧电路 :42）本章既未证实也未证伪。
- **Leon 的死因与那桩「事故」**：:63 `his mysterious accident`、:87 `Maybe it had to do with his accident`、:228（ch16）`terrible accident` 三处只给标签；本书已把 Leon／Mama／Michelle 三种死法列为**一律不裁决**项。
- **那件撕半衬衫上的深色物质是泥还是血**：:75 原文即两可；**不得**与 :93 Gazzie 衬衫上明写的血合并成同一来源（见 C-17-3）。
- **锁箱里是什么**：:84 只到 `it was locked`；:120 的「里面大概是他的速写本」是她带 `likely`／`at least a few` 的推测，不得当作本章已揭内容。
- **Leon 在藏什么、藏给谁**：:87 的三项问句（Gazzie／Virginia／Mama）原文未选。
- **照片里那个「正要进门的人」是谁**（:117）：出自 `like his attention had been caught by…` 的明喻，是她的读法，不得写实。
- **Leon 的眼神是病还是怕**（:69）：`He looked sick. Or scared.` 两可，不得择一（见 C-17-8）。
- **照片里的年长男人是否 Harrison 的父亲**：:30 自带 `presumably`。
- **Virginia 是否在 Henri 处过夜**：:15 是 `may not be back until tomorrow morning` ＋ `with a blush` 的条件句，未成事实。
- **「Greer House 三人小群」的第三人**：:12 只写 `three-person`，成员未点名。
- **她去的 Leon 旧屋在楼上何处、与 ch16 的「餐厅／书房／农场前办公室」如何拼合**：:24/:111 只给「客房离 Gazzie 的办公室最近」「她砰上自己办公室的门」，平面关系原文未画全。
