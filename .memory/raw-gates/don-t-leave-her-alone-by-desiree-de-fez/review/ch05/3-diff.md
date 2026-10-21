# 第 5 章 R3–R4 差异单（人工审查）

- 审查对象：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch05 chapter 5.md`（成品，156 行，8 个引语块）
- 唯一真值：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch05_chapter_5.txt`（原文，729 行，48,238 字符）
- 机器层：`bash scripts/chapter.sh "…/ch05 chapter 5.md" --json` → **退出码 0**，`verdict: ok`，`issues` 四组全空（详见 `2-machine.json`）
- 流程：R1 素读（`1-suread.json`，先读原文后开 md）→ R2 机器层 → R3 三张单子 → R4 逐块＋固定三问
- 行号约定：`text:NNN` = 原文行号；`md:NNN` = 成品 md 行号

---

## 一、漏（L）

### L1｜父亲已故（两年多前的 3 月）——全篇未交代｜档：提示（漏）

**原文侧**（`text/ch05_chapter_5.txt:636`）：

> "I don't know, I feel bad for my mom. If my dad hadn't died, maybe she'd be home with him now, instead of at urgent care with my sister."

**原文侧**（`text/ch05_chapter_5.txt:642`）：

> "Maybe you're right. I can't believe in March it'll be two years since he died."

**md 侧**（`ch05 chapter 5.md:11`）：

> …一边想起父亲留在浴室里的烟味。

**md 侧**（`ch05 chapter 5.md:103-111`，块 8）：只译了烟味句本身（`md:105`），`md:109`「作者把父亲压缩成一种气味：没有脸，没有声音……和一次她反复索要的确认」保留了原文的不确定感，但**通篇没有任何一处交代这个父亲已经去世两年**。

**影响**：读者会把「父亲留在浴室里的烟味」读成父亲在场的实证（甚至幽灵式在场），而原文里这是一个**死者**的气味，且叙述者还要「反复索要确认」；`md:11` 的压缩正是被这个缺口带偏的。

**修法**：`md:11` 改为「一边想起（两年前就去世的）父亲留在浴室里的烟味」；块 8 `md:109` 或 `md:111` 补一句「父亲已于两年前的 3 月去世（:636、:642）」。

### L2｜Juan 生日当天缺席＋硬币来源（祖父给每个孩子两欧元）——未进 md｜档：提示（漏）

**原文侧**（`text/ch05_chapter_5.txt:159`）：

> "Yesterday Juan's dad gave each of them two euros so they could buy something."

**原文侧**（`text/ch05_chapter_5.txt:282-285`）：

> "Call him and ask." / "I called, but he didn't pick up. He's probably out biking or something."

**md 侧**（`ch05 chapter 5.md:13`）：

> …孩子早在一只矮柜上找出三枚硬币，另一个孩子也在换尿布台底下摸到了那枚硬币……

**影响**：`md:13` 只交代了硬币的**位置**，没有交代硬币的**来路**（祖父给的钱），也没有交代生日主人丈夫当天失联——这两点是「婴儿吞硬币」这场乌龙的前提。

**修法**：在块 4 或 `md:13` 补一句「前一天祖父给每个孩子两欧元（:159），孩子父亲当天电话打不通（:285）」。

### L3｜母亲是当年陪 Alba 睡在客厅地板上的人——未进 md｜档：提示（漏）

**原文侧**（`text/ch05_chapter_5.txt:546`）：

> "For their entire adolescence, Alba slept on the living room floor. And Carmen…spent Alba's teenage years flopped down on the couch right next to her, holding her hand…Carmen left her husband in the bedroom and went to the living room to sleep next to her daughter."

**md 侧**（`ch05 chapter 5.md:99`）：

> 接下来本章递上来的是证据（童年那张床垫），不是答案。

**影响**：md 只把床垫当作「证据」列出，没有点出陪睡者是**母亲**——而这正是母亲这一角色在本章的全部来处（她的「陪伴式纵容」），也是理解「这一家人为什么总在」的钥匙。

**修法**：`md:99` 补「陪她睡在客厅地板上的是母亲（:546）」。

---

## 二、编（C）

**无。** 已逐条核对 md 全部 5 条导航（`md:11-15`）、8 个引语块的四个子项（`md:19-111`）、词汇表 24 条（`md:113-152`）、一句话总结（`md:156`）中的**事实性断言**（人名、数字、时间、亲属关系、事件），未发现「md 有、原文无」的杜撰事实。命中的 13 处存疑写法全部属于「错」（方向／时序／措辞过头）或「漏」，已分别落在下面两张单子里。

---

## 三、错（W）

### W1｜`md:14`「你姐姐从不独处」——亲属方向反了｜档：阻断

**原文侧**（`text/ch05_chapter_5.txt:513`，Carlos 对 Diana 说）：

> "No, I mean literally. Your sister is never alone. If she's not with your mom or the kids, she's with your cousin or someone else, but she's never alone. I don't think I've ever seen her alone."

**原文侧**（`text/ch05_chapter_5.txt:549`，字符区间 [36285, 37234)）：

> Not once did Diana hear her father complain about the arrangement. If he did, it wasn't in front of the girls. She, on the other hand—who was six years older than Alba—did sometimes express her bewilderment.

**原文侧**（`text/ch02_chapter_2.txt:129`，Alba 视角，独立佐证）：

> Only her older sister, Diana, insisted she go to a specialist and sent her a dermatologist's number several times.

**md 侧**（`ch05 chapter 5.md:14`）：

> Carlos 从「躲进手机里的丈夫」变成唯一敢下判断的人，一句「你姐姐从不独处」把全章的暗线挑明

**影响**：Carlos 说的 "your sister" 指 **Alba**，而 Alba 比 Diana **小六岁**（:549；ch02:129 "her older sister, Diana"；ch17:96 "even with six years between them"）。中文只能译「妹妹」——**同一份 md 的 `md:11` 与 `md:81` 写的正是「你妹妹从不独处」**，本章文件自相矛盾；全书体例也是「姐姐＝Diana、妹妹＝Alba」（ch15:63「阿尔巴温柔地看着姐姐」、ch16:51「姐姐大学第二年绝食」）。「你姐姐」把这条全章暗线的归属方向整个倒过来。

**修法**：`md:14` 改为「一句『你妹妹从不独处』把全章的暗线挑明」。**同源错误请一并扫**：`00_金句精选.md:114`「第五章，丈夫试图解释姐姐为什么永远有人陪」——同一处应为「妹妹」。

### W2｜`md:27`「姐姐不能一个人去」——亲属方向反了｜档：阻断

**原文侧**（`text/ch05_chapter_5.txt:402`、`:408`，Carmen 对 Diana 说，主语是 Alba）：

> "She won't go alone." / "How could she go by herself?"

**原文侧**（`text/ch05_chapter_5.txt:417`，Diana 当场反击）：

> "Do you come with me when I take my kids to the doctor? Never. I go alone. Or Carlos goes. The few times I asked, when they were tiny and I couldn't handle it, you couldn't come because you was with Alba."

**md 侧**（`ch05 chapter 5.md:27`）：

> 记住这扇没有过渡的门。接下来留意每一次「不得不跟谁一起」：这家人几乎从不分开行动，而每一次都有一条具体的理由——孩子不肯留下、姐姐不能一个人去、连去趟急诊也要有人陪着。

**影响**：不能一个人去的人是 **Alba（妹妹）**，且 Diana 当面声明「I go alone」（:417）。这一条若读作 Diana（「姐姐」＝长姐），与 :417 直接冲突；若读作 Alba，则是长幼颠倒。三条理由里的另外两条（孩子不肯留下 :510、去急诊有人陪 :402/:408）都对，唯独这条把主语与亲属称谓一起拧了。

**修法**：`md:27` 改为「……孩子不肯留下、**妹妹**不能一个人去、连去趟急诊也要有人陪着」。

### W3｜`md:15`、`md:156`「饭后」——与原文冲突（全章没有人吃饭）｜档：阻断

**原文侧**（`text/ch05_chapter_5.txt:135`）：

> "It's three something already. I'm starving. The kids ate at school, but we haven't eaten a thing since seven this morning."

**原文侧**（`text/ch05_chapter_5.txt:432`、`:480`）：

> "You all go ahead and eat, we'll call when they take us back," Carmen said to Diana. / "If you don't eat here, take the rice in a Tupperware, it'll go bad," Carmen said before closing the door.

**原文侧**（`text/ch05_chapter_5.txt:567`）：

> "Sometimes. I mean, why did we come today if we have to come back tomorrow? What are we doing here alone? It's past four o'clock and we still haven't eaten lunch."

**md 侧**（`ch05 chapter 5.md:15`）：

> …最后在**饭后**那张沙发上（孩子们已经在丈夫腿上睡熟），把叙事从「一场聚会」切换成「一份档案」

**md 侧**（`ch05 chapter 5.md:156`）：

> 一场生日聚会把三样东西同时摆上桌：摆得过满的下酒菜、一次早已找到硬币却仍然要去急诊的迷信行动，以及**饭后**两个人翻出来的旧账……

**影响**：原文四次明说没人吃饭（只有 Carmen 让他们「go ahead and eat」，随即以 Tupperware 米饭收场；四点了还在说「we still haven't eaten lunch」）。md 自己在 `md:11` 写的是「一桌准备过头的**下酒菜**」——一场 aperitivo，不是正餐；写「饭后」等于凭空加了一场没发生的饭。

**修法**：`md:15` 改为「最后在**饭局散场后**那张沙发上……」；`md:156` 改为「以及**饭局散场后**两个人翻出来的旧账」。

### W4｜`md:15` 把三件回忆材料压进同一张沙发——地点／时序错位｜档：提示

**原文侧**（`text/ch05_chapter_5.txt:477`、`:489`，孩子趴在 Carlos 腿上＝**在 Alba 家**）：

> "Diana sat down and watched, fuming and powerless, as the five of them paraded out the door." / "The kids, having reached their limit, were cuddled up next to him. They were lying across the cushions, both using his lap as a pillow."

**原文侧**（`text/ch05_chapter_5.txt:546`，「童年的床垫」＝**当场在 Alba 家回想**）：

> Alba had been thirteen then…Alba dragged her mattress into the living room, and she announced she was going to sleep there, on the floor.

**原文侧**（`text/ch05_chapter_5.txt:552`，**回家**；`:606` 商场的旧忆、`:615` 父亲的烟味都在家）：

> "All right, let's go, I want to get home," Diana said to Carlos. / Diana agreed with Carlos—something was off with all three of them…The Corte Inglés had been her Disneyland, and her sister's, too.

**md 侧**（`ch05 chapter 5.md:15`）：

> 最后在饭后那张沙发上（孩子们已经在丈夫腿上睡熟），把叙事从「一场聚会」切换成「一份档案」：童年的床垫、商场的旧忆、父亲留在浴室里的烟味，一件件翻出来。

**影响**：三件材料分处两地两段：床垫与「孩子睡在 Carlos 腿上」在 Alba 家；商场的旧忆与父亲的烟味在**回自己家之后**。md 把它们并成同一张沙发上的「一份档案」，读者会以为三件事是连着回忆出来的。

**修法**：`md:15` 拆成两句：「在场边那张沙发上（孩子们已经在丈夫腿上睡熟），她先把童年那张床垫翻出来；回到自己家，商场旧忆和父亲留下的烟味才接着上来。」

### W5｜`md:13`「全家的迷信行动」「唯一能解释这团混乱的力量」——两头过头｜档：提示

**原文侧**（`text/ch05_chapter_5.txt:387`，Diana 当场否定邪眼）：

> this whole thing with the coin has nothing to do with the evil eye…you're not going to urgent care

**原文侧**（`text/ch05_chapter_5.txt:528`，Carlos 归为巧合）：

> "It must be a coincidence."

**原文侧**（`text/ch05_chapter_5.txt:237`，只有 Alba 认邪眼）：

> "It was the evil eye. I knew it. Those damn old women."

**md 侧**（`ch05 chapter 5.md:13`）：

> 「宝宝吞了硬币」的家庭乌龙被反用成一场**全家的迷信行动**……「邪眼」这种民间说法没有被作者嘲笑掉，反而被写成**唯一能解释这团混乱的力量**。

**影响**：「全家的」把 Diana（明确反对）与 Carlos（归为巧合）也算进了迷信阵营；「唯一能解释这团混乱」也把邪眼的解释力抬到全章唯一——原文里它只解释 Alba 一个人的恐惧，其余的混乱（硬币、急诊）恰恰**不是**邪眼能解释的。

**修法**：`md:13` 改为「……被反用成一场只有当事人认账的迷信行动……「邪眼」没有被作者嘲笑掉，反而成了唯一能解释**她**那团混乱的说法」。

### W6｜`md:63`「这一整天里没有一个人去核对它」——过头｜档：提示

**原文侧**（`text/ch05_chapter_5.txt:333`，Diana 当场问过母亲）：

> "Mom, what was Alba talking about with the evil eye? Did something happen?"

**原文侧**（`text/ch05_chapter_5.txt:336`，Carmen 答了）：

> "Nothing. Ignore her. It was just that some old women went up to her yesterday at Finestrelles, and she said one of them put an evil eye on her."

**md 侧**（`ch05 chapter 5.md:63`）：

> 留意这句「我早知道」指向的是前一天发生的另一件事，而这一整天里没有一个人去核对它。

**影响**：原文里「核对」动作是**发生过的**（Diana 问、Carmen 答），只是没有人去实地核实。md 写成「没有一个人去核对」，把「没去现场核实」扩大成「没人问过」。

**修法**：`md:63` 改为「……而这一整天里没有一个人去现场核实它」。

### W7｜`md:85`「一个整天埋在手机里的丈夫」——无出处｜档：提示

**原文侧**（`text/ch05_chapter_5.txt:78`，Carlos 只有这一处）：

> Carlos…took refuge in his phone

**原文侧**（`text/ch05_chapter_5.txt:18`，「埋进手机」的是母亲）：

> Carmen…remained absorbed in her phone

**md 侧**（`ch05 chapter 5.md:85`）：

> 作者让最不像会管闲事的人（一个**整天**埋在手机里的、有「盲区」的纪录片导演）来说破……

**影响**：Carlos 的「躲进手机」是 Alba 家客厅里的一个瞬间，之后他正是全章最清醒、追问最狠的人（:501、:513、:519、:528、:690-714）；「整天」既无出处，也和后半章的形象相反。而真正「整天埋进手机」的角色是 Carmen（:18）。

**修法**：`md:85` 改为「（一个刚才还躲进手机里的、有「盲区」的纪录片导演）」。

### W8｜`md:12`「病症第一次被说出口」——易读成「对家人说破」｜档：提示

**原文侧**（`text/ch05_chapter_5.txt:540`）：

> Diana knew Alba was never alone. She had never told anyone it weighed on her…she had never talked about this feature of Alba's life with anyone, neither with Carlos nor Carmen, nor with Alba herself.

**原文侧**（`text/ch05_chapter_5.txt:543`，autophobia 是 Diana 的内心检索）：

> She thought the obsession must be related to fear, and she scoured the internet for similar phobias. She found one: autophobia, the irrational fear of being alone.

**md 侧**（`ch05 chapter 5.md:12`）：

> 本章是全书弧线里「病症第一次被**说出口**」的那一格——「妹妹从不独处」这个判断，叙述者交代自己六年前就察觉了（她当年上网查过一种怕独处的病症），却在母亲、丈夫、妹妹面前谁都没讲……

**影响**：原文里这个病名与这个判断**从未对任何人说破**，只是 Diana 的内心活动与上网检索；「第一次被说出口」会让人以为本章有人把话说开了。成立的读法是「第一次被点名／第一次被读者看见」。

**修法**：`md:12` 改为「「病症第一次被**命名**」的那一格」或「第一次被读者看见的那一格」。

### W9｜`md:11`「平安夜前两天」——比原文日期早一天｜档：提示

**原文侧**（`text/ch05_chapter_5.txt:315`，母亲给出的日期）：

> "You're going to be at urgent care for no reason, two days before Christmas, when there's hardly anyone working."

**原文侧**（`text/ch05_chapter_5.txt:567`，当天＝Dec 23，明晚还有一场）：

> "Sometimes. I mean, why did we come today if we have to come back tomorrow? What are we doing here alone?"

**原文侧**（`text/ch04_chapter_4.txt:52-54`，时间轴锚点）：

> "Why doesn't she celebrate it tomorrow, so we don't have to go twice?" / "Because tomorrow is Christmas Eve, and celebrating two things at once is bad luck."

**md 侧**（`ch05 chapter 5.md:11`）：

> **平安夜前两天**的妹妹生日聚会……

**影响**：「two days before Christmas」＝**圣诞节（12/25）前两天＝12/23**；12/23 正是**平安夜（12/24）的前一天**（ch04:54「tomorrow is Christmas Eve」＋ch05:567「明天还得再来一趟」）。中文「平安夜前两天」指 12/22，与原文差一天。全书体例里「平安夜」一律指 Christmas Eve（ch08:126、ch10:154、ch13:132、ch17:153 都是平安夜当晚）。

**修法**：`md:11` 改为「**圣诞节前两天（平安夜前一天）**的妹妹生日聚会」。**同源表述请一并扫**：`00_概述.md:22`「平安夜前两天的生日饭」。

### W10｜`md:25`「根子其实就种在这种没有角落的布局里」——作者意图推断，非原文事实｜档：提示

**原文侧**（`text/ch05_chapter_5.txt:540-549`，原文把 Alba 的状况归因于恐惧与执念，不提户型）：

> She thought the obsession must be related to fear…she focused on gathering enough evidence to prove that Alba had been afflicted at least since she was a teenager.

**md 侧**（`ch05 chapter 5.md:25`）：

> 本章后半场关于「从不独处」的那记闷棍，根子其实就种在这种没有角落的布局里。

**影响**：这是作者意图层面的因果推断，且与原文给出的归因（恐惧／执念／母亲长期的陪伴式纵容）不同。作为「为什么这样写」的解读可以保留，但不应与事实性断言混同。

**修法**：加限定词（"作者像是把……"），或把归因交给原文给的线索（恐惧、母亲陪着睡地板）。

---

## 四、交叉说明

1. **称呼链（决定 W1／W2 的档位）**
   - `text/ch05_chapter_5.txt:549`：`She, on the other hand—who was six years older than Alba—did sometimes express her bewilderment.` ⇒ Diana 大六岁＝长姐。
   - `text/ch02_chapter_2.txt:129`：`Only her older sister, Diana, insisted she go to a specialist…` ⇒ Alba 视角里 Diana 是「姐姐」。
   - `text/ch17_chapter_17.txt:96`：`even with six years between them` ⇒ 两人相差六岁。
   - 全书 md 体例：`ch15 chapter 15.md:63`「阿尔巴温柔地看着**姐姐**」、`ch16 chapter 16.md:51`「想起**姐姐**大学第二年绝食」⇒ 姐姐＝Diana、妹妹＝Alba。
   - 结论：Carlos 的 "your sister"＝Alba ⇒ 中文只能是「**妹妹**」；本 md `md:11`／`md:81` 写对了，`md:14`／`md:27` 写反了；同源错误在 `00_金句精选.md:114`。
2. **时间轴链（决定 W9）**：ch04:54「tomorrow is Christmas Eve」⇒ ch04 当天＝12/23；ch05:315「two days before Christmas」⇒ ch05 当天＝12/23；ch05:567「明天还得再来」⇒ 12/24＝平安夜。因此本章＝**圣诞节前两天＝平安夜前一天**，不是「平安夜前两天」。
3. **「从不独处」是本章首次出现**：`/usr/bin/grep -c "alone" text/*.txt` → ch03:0 ch04:0 **ch05:12** ch10:12；前四章无相关表述 ⇒ `md:12`「病症第一次被说出口」在**读者层**成立（对家人层不成立，见 W8）。
4. **autophobia 全书唯一**：`/usr/bin/grep -n "autophobia" text/*.txt` → 仅 `text/ch05_chapter_5.txt:543`，exit=0 ⇒ `md:93` 的病名归属成立。
5. **原文自身的不自洽（非 md 错）**：`text:159` 说钱是「Juan's dad」昨天给的，但 `text:147`／`text:642` 显示 Juan 的岳父（Carmen 亡夫）已去世两年。md 未引用这一条，不作 md 缺陷记录，仅备注。

---

## 五、修后复核（改稿后按此复核）

1. 改 `md:14`、`md:27` 的「姐姐」→「妹妹」；同步扫 `00_金句精选.md:114`。
2. 改 `md:15`、`md:156` 的「饭后」→「饭局散场后」；`md:15` 拆句区分 Alba 家／自己家。
3. 改 `md:11` 的「平安夜前两天」→「圣诞节前两天（平安夜前一天）」；同步扫 `00_概述.md:22`。
4. 补 L1（父亲已故）、L2（硬币来源与 Juan 缺席）、L3（母亲陪睡）三处。
5. 复核命令：
   - `/usr/bin/grep -n "姐姐" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch05 chapter 5.md"` → 期望 exit=1（无输出）。
   - `/usr/bin/grep -n "饭后" "…/ch05 chapter 5.md"` → 期望 exit=1。
   - `/usr/bin/grep -n "平安夜前两天" "…/ch05 chapter 5.md" "…/00_概述.md"` → 期望 exit=1。
   - `bash scripts/chapter.sh "…/ch05 chapter 5.md" --json` → 期望退出码 0、`issues` 仍全空。
6. 本单只出指令，未改动任何 md 文件；`git` 未执行任何操作。
