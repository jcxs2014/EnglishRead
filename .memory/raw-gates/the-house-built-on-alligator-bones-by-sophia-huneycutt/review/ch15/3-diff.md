# ch15（书内 Chapter Fourteen）深审 R3/R4 三张单子

素读基线：`review/ch15/1-suread.json`（57 条事实／**0 MISS**，只读 `text/ch15_chapter_fourteen.txt`，写完才开 md）
机器层：`review/ch15/2-machine.json` → verdict `ok`（blocks 4 ∈ target [2,4]；segments 5／MISS 0；words 1143；struct_bad 0）
词表：13 行例句展平逐字 **0 MISS**；直撇号 **0 站**
跨章取证：ch09:30／ch09:36（浴房茉莉味与水中陌生女人）、ch06:12（男人的笑声）、ch05:189（Lena 已被点名）、ch11:12（downtown 散步计划）、ch12:27/:42（天花板裂缝与屋顶工）

> ⚠️ 本轮一条**审查方自查**：素读稿初稿把 :90 记成 `I shook her head.`（第一人称配 her 的「书内 person 滑移」），逐字 anchor 立刻 MISS，实为 `I shook my head.` ⇒ **凡拟写进「书内不一致／不许裁决」的原文，必须先过 anchor 逐字**，本文件与判定表均未采用该说法。

## 🟥 阻断（8）

### C-15-1 抹平原文刻意保留的时点：「天亮前」
- md:10：**「天亮前楼梯上真有脚步、墙里有嗡鸣」**
- 原文逐字：`:21` — `The light drifting in from the window was so weak I wasn’t sure whether it came from the sun or moon.`；`:45` — `In the barely there morning light streaming through the front doors—I could tell it was morning by then—her white hair glimmered.`
- 判定：文本在 :21 明确让她**分不清日月**，到 :45 才用破折号补一句「那时已能判断是清晨」（`by then`＝中间某个时点转成清晨，未定位）。md 把脚步声（:27）钉在「天亮前」，正是原文撤掉的那根刻度；且 :27 在 :21 之后、:45 之前，落在刻意悬空的那段里。
- 改法：「醒来后不久楼梯上真有脚步、墙里有嗡鸣——她那时还分不清窗光属于太阳还是月亮（:21），直到 Virginia 赶到才确认已是清晨（:45）」。

### C-15-2 认知对冲升格：「松鼠睡裤坐实了他在这个家的名分」
- md:90：**「而 Harrison 的松鼠睡裤坐实了他在这个家的名分」**
- 原文逐字：`:63` — `“I stay in the spare room sometimes,” he said casually, managing to look slightly triumphant. “After late nights.”`；`:72` — `Harrison probably stayed in Greer House all the time. He and Gazzie had much more than a boss-employee relationship. He was practically family.`；`:75` — `A surrogate grandson.`
- 判定：可见的证据只有「**有时**住空房」（他自己说的）＋睡裤；「常年住」「名分」全部挂在 `probably`／`practically` 上，是 Dart 的心证——md:13 写「露出留宿 Greer House 的事实」、md:40／md:44 也都保住了 `probably`，唯独收口句把它升成「坐实」。同句里 md:90 又说「她**第一次**应下屋外的邀请」（见 C-15-3），两句都是总结层的强化措辞。
- 改法：「而 Harrison 那条印满松鼠的睡裤，让她把『他有时住空房』听成了『他大概就是这家里的人』——名分是她自己下的，原文只给了 `sometimes` 与 `practically`」。

### C-15-3 跨章「第一次」断言无出处，且与同书 ch11 记录相抵
- md:90：**「她第一次应下屋外的邀请，急着离开 Greer House」**
- 本章原文逐字：`:114` — `I agreed quickly, eager to leave Greer House and whatever peculiarities lurked within.`（只写「立刻答应」，无任何「第一次」）
- 反证逐字：`text/ch11_chapter_ten.txt:12` — `…I absently admired a red bromeliad as I sipped iced tea and listened to Aunt Virginia detail the stroll we’d take downtown that afternoon.`（`we’d take` 已含她同行）；**同书 `ch11 aunt virginia confesses letter forgery.md:11` 已把这一笔登记为「散步计划」**。
- 判定：「第一次」是跨章全称计数，必须先枚举前文所有屋外邀约；本章与前文至少有一次 Virginia 排定的 downtown 散步。属既有缺陷簇「计数断言／『第一次』类」。**改法**：删「第一次」，或限定成「她第一次这样**立刻**应下屋外的邀请」（`agreed quickly` 有据）。

### C-15-4 全称断言被自己的引语反证＋「降级」方向自相矛盾
- md:40：**「三句都出自她一人的心口揣摩，句句带着『大概』『几乎』这类留有余地的词」**
- md:44：**「三句全是她的心证，用词却一路降级——从推测 "probably"，到比较 "much more than"，到最后一锤 "practically family"」**
- 原文逐字（即本块引语）：`:72` — `Harrison **probably** stayed in Greer House all the time. He and Gazzie had **much more than** a boss-employee relationship. He was **practically** family.`
- 判定：中间一句 `He and Gazzie had much more than a boss-employee relationship` **不带任何缓冲词**——它是三句里唯一的直陈判断，恰是「几乎就是家人」得以落地的承重点。所以「句句带着留有余地的词」为假（同块内即有反例）；md:44 又称这条链「一路降级」，紧接却写「最后一锤」，方向自相矛盾。
- 改法：md:40 删末句「句句带着…」，改为「三句里有两句留了余地（`probably`／`practically`），中间那句却用 `much more than` 直接判定」；md:44 改「从推测，到不带缓冲的比较，再到只差一个名分的 `practically family`」。

### C-15-5 承重信息缺失：她先假设是 Gazzie、再由本能否定（instinctually 句）
- 原文逐字：`:30` — `I assumed it was Gazzie, up early again. Maybe I’d get her to tell me another family story, and she’d like me again.`；`:33` — `I knew, instinctually, that something was wrong, that this figure wasn’t Gazzie or Aunt Virginia.`
- md 现状：这两句只以**词表 `instinctually` 行的例句**形式存在（导航、4 个块均无「不是 Gazzie 也不是 Virginia」这层排除；:30 的「以为又是早起的 Gazzie／也许就能再喜欢她」整句更未提）。
- 判定：本章的鬼影之所以成立，全靠「先按熟人解释、再被本能推翻」这一转——排除法（既不是 Gazzie 也不是 Virginia）是它唯一的形式证据；md:56 讨论「闯入者／非人之物两套候选」，却不写这两套是**由这次排除逼出来的**。md:11 弧线也从「梦里惊恐」直接跳到「尖叫求救」，跳过 :30–:33 的假设→否定→嗅到→看见→喊叫五步。**按「进了词表≠已登记」既有规则判阻断。**
- 改法：块2 的「为什么这样写」末补「而这份不对劲是被**排除**出来的：她先认定是又早起的 Gazzie（:30，还盼着再听一个家族故事），随后本能地否掉——那影子既不是她也不是 Virginia（:33）」。

### C-15-6 承重信息缺失：茉莉味是 ch09 那次出现的前兆，本章同一标记复现
- 原文逐字（本章）：`:33` — `The smell came next: jasmine, slightly off. A concentrated perfume rather than the light scent of fresh flowers.`
- 反证／同源逐字：`text/ch09_chapter_eight.txt:30` — `Suddenly, the jasmine scent washed over me in a wave, like someone had poured a whole bottle of essential oil in the water. Had I dropped a bath bomb in by accident? It smelled sour now…`；随后 `ch09:36` — `Where my reflection should have been was a stranger.`
- 判定：md 的块4 正确地指出「这是**第二次**，第一次是那桩浴水倒影」，却没有把两次的**共同前兆**登记下来：同一股「茉莉、略微不对／闻着发酸」的浓缩香气，都在异常出现前涌到；且 :93 的规律句 `I only ever heard it before something odd happened` 只讲嗡鸣，茉莉是它的嗅觉版。md:14 已具备「音效共用」这条眼力（hiss／电嗡），却漏了气味这条同级通道。取证：`/usr/bin/grep -n "jasmine" "<ch15 md>"` → 无输出（退出码 1）。
- 改法：md:14 补「**气味也共用**：ch09 浴房里那股『茉莉、发酸』的浓缩香气同样是异常的前兆（ch09:30），本章 :33 复现——她数得出嗡鸣的规律，却还没把茉莉列进同一张清单」。

### C-15-7 承重信息缺失：「几天前那个男人的声音」是全书伏笔在本章的兑付点
- 原文逐字（本章）：`:72` — `Heart sinking, I remembered the man’s voice from a few nights before. Of course.`
- 同源逐字：`text/ch06_chapter_five.txt:12` — `Faint voices woke me. I thought I heard a man laughing, then sleepily decided I hadn’t; only women lived in Greer House.`
- 判定：块3 的引语从 `Harrison probably stayed…` 起截，正好把这一拍（**她想起那个男人的声音**）留在块外，md 全文（导航＋4 块＋词表）也无一处提及；而 :69  Harrison 话锋的最后半句 `“Actually, I guess you don’t.”` 同样未收——「心往下沉」在原文里正是接在这句抢白之后。两条合起来，本章对「Harrison 为何住在这里」给出的**唯一一条旧证据链**（ch06 夜里男人的笑声 → 当时她自我否定「只有女人才住 Greer House」→ 此刻 `Of course.` 反悔）整块缺席。
- 取证：`/usr/bin/grep -nE "男人|笑声|几天前|guess you don" "<ch15 md>"` → 无输出，退出码 1。
- 改法：块3 的「为什么这样写」补「且这三句之前还有一拍：她先想起几天前那个男人的声音（:72，接 ch06:12 那次『我以为听见男人笑，又说服自己只有女人住这儿』），一句 `Of course.` 把当年的自我否定推翻」；并在 md:44 记下 `“Actually, I guess you don’t.”`（:69）是心沉的直接触发句。

### C-15-8 句式误称：把陈述＋反讽写成「她自问」
- md:26：**「本章稍后她自问梦回应的是 Ida 猎 Ironheart 的传说」**
- md:12：**「梦中巨鳄的嘶鸣被她认作回应了 Ida 追猎 Ironheart 的传说」**
- 原文逐字：`:24` — `The dream had echoed Ida’s legendary hunt for Ironheart. So now I was facing alligators in my dreams as well as at work. Great.`
- 判定：这是**陈述句＋一句反讽**（`Great.`），全章没有对「梦是否呼应传说」发问（唯一问句是 :87 Virginia 的 `Could it have been a bad dream?` 与 :81/:66 的问）。md 把它写成「她自问」＝句式类别误判（本库连续第五章出这一类：ch11 残句／ch12 单音节／ch13 将来时／ch14 宾语前置）；md:12 另把范围从「这场梦」（`The dream`）缩成「梦中巨鳄的嘶鸣」。
- 改法：md:26 改「本章稍后她自己给出判语：这场梦呼应了 Ida 猎 Ironheart 的传说（:24），接着是一句反讽的 `Great.`」；md:12 改「这场梦（含嘶鸣）被她认作呼应……」。

## 🟡 提示（6）

- **T-15-1**（md:10）「奔过来的是 Aunt Virginia、清洁公司老板 Lena 和留宿客房的 Harrison」——三拨人被并成一拨：:42 只有 Virginia `rushing from the dining room`；:45 Lena 是「出现在她身后、越过她的肩张望」；Harrison 更晚，是 :54 Virginia「目光落在她身后某处」→:57 才现身的。建议分层，顺带保住「她身后一直有人」这条本章的的空间感。
- **T-15-2**（md:10）「**显然是**被派来盯她的」——:9 是 `Gazzie had apparently ordered them to babysit me, though she didn’t check on me once`：推断＋反证同句。建议「像是被派来盯她」。
- **T-15-3**（md:13）「Harrison 本章露出留宿 Greer House 的事实」缺 `sometimes`（:63）；与 :72 的 `probably … all the time` 分层写，才不与 C-15-2 的整改冲突。
- **T-15-4**（md:10／块2）她的复述也带折扣：:84 `“No,” I said… “She wore something dark. A long skirt, maybe.”`——「黑裙」在 :33 是叙述、在她自己口中是 `maybe`。建议块2 或导航点一句，供「可信度」讨论使用。
- **T-15-5**（md:56）「本章给了**两套**候选（闯入者／非人之物）」——原文另有第三套并已当场被否：:87 `“Could it have been a bad dream?”` ＋ :90 `I shook my head.`。改「三套（闯入者／非人之物／噩梦），最后一套她当面摇头否掉，前两套既未证实也未证伪」。
- **T-15-6**（md:13）「用去海滩的提议救场」把 :111 `Aunt Virginia’s tone edged on desperate, but I appreciated the attempt at cheerfulness.` 折成一个动作；「近乎绝望的语气＋她领情」是 Virginia 弧线的承重，建议原样并入。

## ⬜ 判为假红（8，勿改）

- **F-15-1** md:13「十五秒赶到」对 :42 `no more than fifteen seconds later` ✓（数量逐字，非约数）。
- **F-15-2** md:13「替她想『也许是噩梦』」✓：:87 虽是问句，:93 叙述层已把它称作 `Aunt Virginia’s perfectly reasonable explanation`，md 不算升格。
- **F-15-3** md:40／md:44 对 `probably`／`practically` 的处理正确；红只在「句句」与「降级」两处，**整改时不得反向删掉缓冲词的说明**。
- **F-15-4** md:24「"Another." 没有主语也没有动词」✓（:12 末的一字句）。
- **F-15-5** md:34「与上一块梦里同用的 "glided" 在此复现」✓：`glided` 在本章出现于 :12（梦里的眼睛）与 :33（影子），两处对照有据。
- **F-15-6** md:14「梦境与现实的音效共用 hiss 和电嗡」✓：:15/:21（hiss）、:27/:93（hum，且 :93 说 `The hum had quieted`）。
- **F-15-7** md:56「记账时先挂她名下」✓——与「不许裁决」一致，整改时勿把「闯入者」写实。
- **F-15-8** md:10「可 Gazzie 一次也没来看过她」✓ :9 `didn’t check on me once`，与 :102 `had finished dressing for the day instead of checking on me` 是同一件事的两处写法，**不是**前后矛盾。
- 词表 13 行例句 0 MISS；`…` 拼接块（原句2）已在书级 `verify_fragments_indep.py`（313 条／443 片段／MISS 0）中逐片段命中 ⇒ 引语条数 313 全程不变。
