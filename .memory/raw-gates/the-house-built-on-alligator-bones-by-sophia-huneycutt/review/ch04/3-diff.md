# ch04 对账（R3/R4）

text = `text/ch04_chapter_three.txt`（310 行）｜md = `ch04 aunt virginia darts dinner and the island invitation.md`｜块数 9｜素读事实 29 条

## 阻断

- **[C-04-1] 凭空道具／事实**｜md:10「Virginia 姨妈**带着讣告、盐药片与一顿晚饭**出现在叙述者的公寓门口」
  :48 讣告＝`I read the obituary online.`（她读过，没带）；:72 盐药片是**叙述者自己说**「Just need a salt tablet.」，全章没有任何一方递出盐丸的动作；晚饭＝开车去餐馆（:87「Dinner it is. My treat.」），也不是「带着」。三个道具里两个凭空、一个错介质。
- **[C-04-2] 归属／施事**｜md:10「**当面告诉她**：回信的那位 Ginny 不是助手，而是又一个家里人」
  :9 全句是叙述者**内心**的纠正（`wasn’t an assistant; she was another family member`），本章对话里 Virginia 从未说过「我不是助手」；md:24 自己把它处理成「一条被自己贴错标签的亲属关系」——正确，与概括冲突。
- **[C-04-3] 实体混淆**｜md:12「富有的姨妈**用支票解决问题**」
  本章 Virginia 只提出付房租（:273 `Your grandmother and I will pay your rent.`）；全书唯一的支票＝ch02 那张被撕成两半的三万美元（:231 叙述者回想 `Then I remembered the thirty-thousand-dollar check`），**不是姨妈用来解决问题的工具**。
- **[C-04-4] 章内范围断言不成立**｜md:66「这一章里这个动作还会再来。」
  「先去安慰对方」这个动作在本章只出现一次（:120–:123）；此后 Virginia 再次哽咽（:246）时叙述者没有第二次安慰。要写「反复出现」须改成跨章口径（ch03 水池边、ch05 之后都有），不能锁在本章。
- **[C-04-5] 漏（跨章伏笔级单元）**｜:102＋:105
  `she seemed genuinely curious about my life, from my job to my sketchbook, which I’d placed in the back seat with my leather pen roll, a lucky thrift store find` ＋ `I’d learn to use oil paints if I ever did her portrait, I decided. No ethereal watercolors for Virginia Greer.`
  速写本／笔卷（二手店幸运物）与「要为她画肖像、为此去学**油画**」两条全篇缺席（导航、九块、词汇层均无）。油画在本书记载里有专门归属（ch16 Leon＝传统派用油画、自画 Ida），本章是叙述者第一次说要学油画——总览与 ch16 审查都要用这条，漏在这里最贵。
- **[C-04-6] 漏（第一个 Gazzie 剖面）**｜:303
  `“Gazzie’s big on tradition. And she enjoys it, for God knows what reason. Sometimes I think she’s part alligator herself.” Then, more to herself than me: “Though, that can’t be true. No one hates them more than she does.”`
  Virginia 先说 Gazzie「有时像部分就是鳄鱼」，随即**自己推翻**「那不可能是真的，没人比她更恨它们」——这是全书第一次给出 Gazzie 的内在矛盾，也是 ch37/ch43 供词线的种子；md 全篇未提（:300 那句「既然你们已经过得舒服，为什么还经营农场」的问话也未提）。
- **[C-04-7] 逐字（直撇号）**｜分析层引语用 ASCII `'`，语料为弯撇号 `’`，六处：
  md:12 `I'm ironing out a few details`（原文 :264 `I’m ironing…`）、md:13 `It's nothing`（:72 `It’s nothing.`）、md:24 `wasn't an assistant`（:9 `wasn’t`）、md:54 `Though, of course, she'd claimed she'd come from a Florida foster home`（:123 两处 `she’d`）、md:64 `I couldn't repress the urge to reassure her`（:58 `couldn’t`）、md:84 `luxury brands can't get enough of them`（:216 `can’t`）。
  ⇒ `analysis.py inline` 因撇号归一化一律放行（已知坑第 27 条），**只有人判/自建尺子能查**；全库同类共 44 处，见深审指令文件「全局逐字类」。

## 提示

- **[C-04-P1]**｜md:84「though 在第一句末尾把话折回来」——`though` 在引语的**第二句**末（`We prioritize the skins, though—`）。
- **[C-04-P2]**｜:189 叙述者自己这几天搜过鳄鱼场照片、最怪的一张是背心人字拖的男人拎着鳄鱼尾巴甩、并说自己不穿护甲连靠近都不敢——md 未提（与 :193–:204「鳄鱼跳出水面五英尺／员工挂整鸡」同单元，全由 Virginia 之口，md 只取了产品那两句）。
- **[C-04-P3]**｜:252 Virginia 那段长铺垫（母亲葬礼后整月连两条西裤都选不定）md 未提；它既是人物对照（同为丧亲者），也是「my mother」指代的一次显形。
- **[C-04-P4]**｜md:50「一身晒不掉的**黑色**」——原文 `a permanent tan`＝永久的晒痕／晒黑，「黑色」偏重；md:52 关键词列 `permanent tan` 正确。
- **[C-04-P5]**｜md:20／:40「这一大家子人个个都在哪儿病着」✓，但 md:46 已经正确地给「我祖母」留了不连线——保持；`Hashimoto's`（md:40／:42）属词头式提及，按既定口径**算假红、不必改**。

## 已核实为正确

- 九个引语块逐字（2-machine.json）；H1 `04. Chapter Three`＝文件号比文内章号大 1 ✓。
- md:26「记下『背叛 Mama』这个罪名是她自己判的，不是在场任何一个人说的」✓——本章无人说过此话，护栏正确。
- md:46「『我祖母』指谁、和叙述者口中那位写信的祖母是不是同一个人，本章此处没有交代清楚」✓——:81 Virginia 的原话确实不点名，**这是全书级的不连线护栏，勿删勿改成「＝Gazzie」**。
- md:34「首句用过去完成时把结论摆在最前」✓（`Mama hadn’t been affectionate`）。
- md:74「清单收的全是节律与偏好……没有一条涉及她与 Mama 之间发生过什么」✓（:147 三项：dawn／三杯黑咖啡／收古董）。
- 岛与镇的地理（:138 Amelia Island／Fernandina Beach 是岛上最大的镇）、农场在内陆而房子在岛侧（:177）、只有一个农场对游客全开（:192）三处均与原文一致。
- 「曾曾祖母 1800 年代末投资铁路」＝Virginia 之口（:279），而**叙述者对「Ida 是否即这位曾曾祖母」只写成一句自问**（:282 `Was Ida my great-great-grandmother?`）——md 未把它坐实（:66 之外无一处连线），保持。
- ⚠️ 新护栏（深审补记）：本章 `my mother` **有两个所指**——:144／:186／:252 是 Virginia 说**她自己的**母亲，:174 是叙述者问**Caroline** 是否在农场长大。md 未混淆，任何后续改动不得把三处合并成同一人（Gazzie 的女儿＝Caroline 的证据在 ch38/ch43，不在本章）。
