# 第 8 章 R3–R4 差异单（人工审查）

- 审查对象：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch08 chapter 8.md`（成品，126 行，6 个引语块）
- 唯一真值：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch08_chapter_8.txt`（原文，282 行 / 281 个非空行，11,817 字符，94 个自然段，对话密集）
- 机器层：`bash scripts/chapter.sh "…/ch08 chapter 8.md" --json` → 退出码 0，`verdict: ok`（详见 `2-machine.json`）
- 流程：R1 素读（`1-suread.json`，先读原文后开 md）→ R2 机器层 → R3 本单 → R4 逐块＋固定三问
- 行号约定：`text:NNN` = 原文行号；`md:NNN` = 成品 md 行号

---

## 一、漏（L）

### L1｜母亲连打五个电话、Diana 四次挂断这一整段未进 md｜档：提示（漏）

**原文侧**（`text/ch08_chapter_8.txt:102`）：

> "My mom. Who knows what she wants now."

**原文侧**（`text/ch08_chapter_8.txt:111`）：

> One second later, the phone rang again. Carmen called four more times, and all four times, Diana silenced the call.

**原文侧**（`text/ch08_chapter_8.txt:114`，Carlos 开口）：

> "Call her back. It’s not normal for her to call this many times," Carlos said. "Look, she called me twice as well."

**原文侧**（`text/ch08_chapter_8.txt:117`，Diana 拒接）：

> "But she’s annoying. They’re both so annoying. It’s most likely something stupid. They can wait, we’re in the car already."

**md 侧**：`ch08 chapter 8.md` 全文没有一处写母亲打电话，也没有一处写 Diana 挂断。`md:14` 只写「Brisa 把手机扔到地上，又用怀疑的目光盯着父母」。

取证命令：
```
/usr/bin/grep -nE 'silenced the call|called me twice|so annoying|something stupid' text/ch08_chapter_8.txt
→ text/ch08_chapter_8.txt:111、:114、:117（+ :117）；退出码 0
/usr/bin/grep -cE '母亲.*电话|挂断|不接' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch08 chapter 8.md"
→ 0；退出码 1
```

**影响**：这一段是全章的暗线发动机——正是母亲的连环电话与 Diana 的四次挂断，才让 Carlos 在 `:114` 说出「给她回个电话，这不正常」，也才让 `:150` 的 Brisa「looking between her mother and father」有可解的背景。md 只写了 Brisa 摔手机（L1 已写）与 Brisa 怀疑地看着父母（`md:14`），没有写「是谁在打、谁不接」，读者看到 Brisa 的怀疑却没有来源。

**修法**：`md:14` 或块 3（`md:43-51`）的「读者视角提示」补一句：车里母亲连打五个电话，Diana 一次没接，Carlos 让她回。

### L2｜「打翻了电梯/差点吐」的表演与司机的两次拒绝未进 md｜档：提示（漏）

**原文侧**（`text/ch08_chapter_8.txt:126`，司机）：

> "I can’t stop in the middle of Diagonal," the driver said, his voice sour.

**原文侧**（`text/ch08_chapter_8.txt:135`，司机）：

> "She’s going to throw up? Great, that’s great," the driver yelled.

**原文侧**（`text/ch08_chapter_8.txt:171`，司机）：

> "It’s not early. It’s almost eight."

**原文侧**（`text/ch08_chapter_8.txt:180`，司机）：

> "No, no, I can’t wait for you. This is my last ride of the night," he rushed to say.

**md 侧**：`md:11`、`md:61`、`md:73` 写了「女儿想吐」是临时编的、司机配合在 Diagonal 路边停下（`md:11`「坐上车后，她忽然要在 Diagonal 路边下车」），但**没有写司机的两次拒绝与不情愿**（不能在 Diagonal 中间停车、这是他今晚最后一单不等人）。

取证命令：
```
/usr/bin/grep -nE "middle of Diagonal|going to throw up\?|It.s not early|last ride of the night" text/ch08_chapter_8.txt
→ text/ch08_chapter_8.txt:126、:135、:171、:180；退出码 0
```

**影响**：原文里司机的抵抗是这场戏的外部压力源，也让 Diana 的「我带了袋子、一滴都不会弄到车上」那段台词有了对手（`md:57` 只写了她的话，没写她要说服的是一个正在生气的人）。缺了司机这层，「编造」这件事的成本显得太轻。

**修法**：块 4（`md:55-63`）「为什么这样写」补一句：司机先是拒绝在 Diagonal 中间停车，又抱怨这是今晚最后一单不等人，她的表演是冲着这个不耐烦去的。

### L3｜Carlos 在车里问的那串问题（「你把自己弄伤的？」「是安全带吗？」）未进 md｜档：提示（漏）

**原文侧**（`text/ch08_chapter_8.txt:219`）：

> "Did you hurt yourself? Was there something in the taxi? The seat belt, or something else?" he asked.

**原文侧**（`text/ch08_chapter_8.txt:258`）：

> "Did something happen before? The last few days—did you see anything? A cut, a rash…This kind of thing doesn’t just happen,"

**原文侧**（`text/ch08_chapter_8.txt:264`）：

> "Did you do it to yourself?"

**md 侧**：`md:14` 写 Carlos「看见血后腿软、掩面痛哭，最后被她的手按住」，没有写他在车里的追问。

取证命令：
```
/usr/bin/grep -nE 'Did you hurt yourself|seat belt, or something else|did you do it to yourself|doesn.t just happen' text/ch08_chapter_8.txt
→ text/ch08_chapter_8.txt:219、:258、:264；退出码 0
```

**影响**：原文里 Carlos 的第一反应是**找原因**（安全带？之前就有伤？是不是你自己弄的？），Diana 的第一反应是**否认**（`:261`「I swear, there’s been nothing. Absolutely nothing.」）。这条问答链是「她自己信了」这层判断的实据——md:61 只给了结论，没有给出问答过程。

**修法**：块 5（`md:67-75`）「读者视角提示」可补：Carlos 连问三句「是不是你自己弄的」，她一口咬定没有。

### L4｜「It was a blender」这个道具与 Diana 提到的「刀/浸泡式搅拌机」式比喻未进 md｜档：提示（漏）

**原文侧**（`text/ch08_chapter_8.txt:252`）：

> Diana took off her sweater and looked over at the kids, who had opened a gift with no name on it without asking. It was a blender, but they didn’t understand that yet. Tomás wasn’t taking his eyes off the box. Brisa, on the other hand, kept glancing suspiciously at her parents. Diana, who could easily read every one of her children’s emotions, winked to put her at ease.

**原文侧**（`text/ch08_chapter_8.txt:105`）：

> A third call came in, and Brisa flung the phone to the floor.

**原文侧**（`text/ch08_chapter_8.txt:150`）：

> But Brisa was looking between her mother and father, silently trying to decode the situation.

**md 侧**：`ch08 chapter 8.md` 的「blender」只出现在词汇表例句（`md:118`），正文分析没有写它是孩子手里的玩具、父母此刻还读不懂它。

**影响**：原文用孩子的玩具「搅拌机」写下这一家人的误读——大人看着那道伤口，看见的却是孩子手里的玩具，所以「他们还不明白」。md 把它留在词汇表里，正文分析少了一层反讽；顺带说明：`md:14` 写的「用怀疑的目光盯着父母」**归属正确**（"Brisa…kept glancing suspiciously at her parents"），此处不需要改动。

**修法**：块 6（`md:79-87`）「读者视角提示」补一句：孩子手里正拿着一个搅拌机玩具，大人看着那道伤口却还读不懂它指的是什么。

取证命令：
```
/usr/bin/grep -n 'blender' text/ch08_chapter_8.txt
→ text/ch08_chapter_8.txt:252；退出码 0
/usr/bin/grep -c '搅拌机' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch08 chapter 8.md"
→ 1（仅 md:118 词汇例句行）；退出码 0
```

---

## 二、编（fabricated）

### F1｜`md:39`「前面她一直在数锁」——本章原文没有「锁」｜档：阻断

**原文侧**：`text/ch08_chapter_8.txt` 全文**不含** lock / locked / unlock / bolt / chain / key 任何一词。

取证命令：
```
/usr/bin/grep -nwiE 'lock|locked|unlock|bolt|chain|key' text/ch08_chapter_8.txt
→ 无输出；退出码 1
```

**md 侧**（`ch08 chapter 8.md:39`）：

> 留意她张口就是电影。这个细节不是闲笔：前面她一直在数锁、数电器、数出租车，现在她只能用一部电影来描述自己家里的僵局。

**影响**：「数锁」这一项在本章没有出处。本章她检查的是**电器**（`:93` 暖气、直发夹、炉灶、烤箱），**没有数锁**。原文里「数锁」出现在别处：`text/ch04_chapter_4.txt:9`「She recognized the sound of the dead bolt, the second lock, and the third one, which they’d put on first thing after moving in. Diana, who knew the order and speed with which Carlos unlocked the locks…」（那是 ch04 的场景——她在黑暗中辨认丈夫开门的三道锁）；另有 `text/ch01_chapter_1.txt:15`「that she hadn’t left the straightener on, or the door open, or the lock unlocked.」（ch01 出门后回想）。md 把 ch04/ch01 的记忆挪到了 ch08 的「前面」，且放在「数电器、数出租车」并列的位置，读起来像同一条出门清单上的第四项。

**修法**：`md:39` 改为「前面她一直在数电器、数出租车，现在她只能用一部电影来描述自己家里的僵局」；若要保留「锁」，必须改写为跨章指认并注明出处在 ch04。

---

## 三、错（E）

### E1｜`md:49`「暖气、直发夹、炉灶、烤箱，四项」与「三个短语的句式完全平行」自相矛盾｜档：提示

**原文侧**（`text/ch08_chapter_8.txt:93`）：

> Several times, she confirmed that the heat wasn’t on, the straightener was safely cooling, and both the stovetop and the oven were off, before her phone dinged to let them know the driver was arriving.

**md 侧**（`ch08 chapter 8.md:49`）：

> 这一段把她的检查欲写成清单：暖气、直发夹、炉灶、烤箱，四项，一项一项排过来，还明写着「反复确认」。三个短语的句式完全平行，像一份出门前的安全表……

**影响**：原文这句里的并列单位是 **three**（`the heat` / `the straightener` / `both the stovetop and the oven`），md 在同一句里先说「四项」再说「三个短语」，两个数字打架。而且 md:51「注意清单里的第四项——电与火」把第四项说成「电与火」，可原文第三项（炉灶＋烤箱）才是火与电，第一项暖气也属电。

**修法**：`md:49` 统一为「三项：暖气、直发夹、炉灶和烤箱」；`md:51` 改为「注意清单里的第三项——炉灶和烤箱，这是火」。

### E2｜`md:15`「伴侣的话多以转述形式出现，读者听得到他话里的慌张却看不清他的脸」与本章的呈现方式不符｜档：提示

**原文侧**（`text/ch08_chapter_8.txt`，Carlos 的直接引语共 11 处）：`:12`「"What now?" Carlos asked quietly, almost to himself.」、`:72`、`:87`、`:99`、`:114`、`:147`、`:189`、`:240`、`:246`、`:258`、`:276`——全部以直接引号呈现，句句可闻。

**原文侧**（`text/ch08_chapter_8.txt:231`）：

> For a few seconds, she examined her abdomen, completely serene, then she looked back up at Carlos, who was undone.

**原文侧**（`text/ch08_chapter_8.txt:246`）：

> "How is that possible? Look at yourself." Carlos was horrified, pale. All that kept him from fainting was the sound of their kids' voices and movements in the background.

**原文侧**（`text/ch08_chapter_8.txt:225`）：

> As he helped her out of her sweater, his knees buckled. He leaned against the car to avoid collapsing.

**md 侧**（`ch08 chapter 8.md:15`）：

> 伴侣的话多以转述形式出现，读者听得到他话里的慌张却看不清他的脸；

**影响**：两处对不上。① 原文里 Carlos 的话**全是直接引语**，不是转述；② 原文还给了他三次清晰的面部／身体描写（`who was undone`、`horrified, pale`、`his knees buckled`），「看不清他的脸」没有依据。

**修法**：`md:15` 改为「伴侣的话则一句一句直接给出，慌张全在句子里」；若要保留「看不清脸」的写法，须删去原文里那三处面部描写才成立。

### E3｜`md:14`「Carlos 从嫌她老想跳车」把 Carlos 的抱怨说成事先就有的习惯｜档：提示

**原文侧**（`text/ch08_chapter_8.txt:189`）：

> "What an asshole," Carlos said angrily. "What happened? All of a sudden you’re obsessed with jumping out of trains and cars. Diana, this is too much."

**md 侧**（`ch08 chapter 8.md:14`）：

> Carlos 从嫌她老想跳车，到看见血后腿软、掩面痛哭，最后被她的手按住；

**影响**：原文里的 "All of a sudden" 明确表示这是**当场的、突发的一句抱怨**（先问 "What happened?"，再说"All of a sudden"），不是「老」习惯。「老」字是无出处的时间性夸大。

**修法**：`md:14` 改为「Carlos 从当场抱怨她突然要跳车，到看见血后腿软、掩面痛哭，最后被她的手按住」。

### E4｜`md:11`「母亲在洗衣篮边捡起一只成对的银圈耳环」——「成对」与原文的「又一只」不合｜档：提示

**原文侧**（`text/ch08_chapter_8.txt:27`）：

> "My hand, look!" Diana had a silver hoop earring in her palm.

**原文侧**（`text/ch08_chapter_8.txt:33`）：

> "Another earring."

**原文侧**（`text/ch08_chapter_8.txt:36`）：

> "Like the one from the other day?"

**md 侧**（`ch08 chapter 8.md:11`）：

> 母亲在洗衣篮边捡起一只成对的银圈耳环，坚持说那不是自己的；

**影响**：原文里她捡到的是**又一只**（"Another earring."），与「前几天那只」一样（"Like the one from the other day?" / "Identical."）。她捡到的是**孤零零一只**，「成对」反而暗示她手里握着一对完整耳环——与原文相反。「成对」这个词来自 Diana 后面那句 "Another earring" ＋ "Identical" 的口头比对，不是她手里的东西。

**修法**：`md:11` 改为「母亲在洗衣篮边捡起一只银圈耳环——和前几天那只一模一样，她坚持说那不是自己的」。

---

## 四、交叉说明（支撑链）

1. **耳环来源链**：本章四提耳环（`:27` 捡到一只 / `:33` "Another earring." / `:63` "These aren't my earrings." / `:78` "Who would break into the house just to leave an earring here?"）。本章**没有**交代这只耳环的来处，也没有交代「前几天那只」的来处。`/usr/bin/grep -rn "earring" text/` → exit=0，按文件计数 `ch00_prologue.txt` 1、`ch08` 4、`ch11` 4、`ch12` 4；后续在 `text/ch11_chapter_11.txt:63/126/138`（饰品店、女孩给 Alba 打耳洞）与 `text/ch12_chapter_12.txt:120/132/138/156`（「The earrings. Camp La Tortuga Ligera. Me.」、女孩把耳环从 Alba 耳上扯下来）才有下文 ⇒ md 在本章不写耳环来历，是对的（不可把后续当本章事实）。
2. **说话人交替链（ch08 对话密集段）**：以行号奇偶＋语义交叉验证，`text/ch08_chapter_8.txt` 的直接引语归属为：`:12` Carlos、`:15/18/21/24/27/33/39/42/45/51/54/57/60/63/69/75` Diana（洗衣房段）、`:72` Carlos、`:78` Carlos、`:84` Diana、`:87` Carlos、`:90` Diana、`:99` Carlos、`:102` Diana、`:114` Carlos、`:117` Diana、`:126/135/153/171/180` 司机、`:129` Diana、`:138` Diana、`:141` Brisa、`:144` Diana、`:147` Carlos、`:156` Diana、`:159/165/189/195/234/240/246/258/264/276` Carlos、`:168` Diana、`:177` Diana、`:183` Diana、`:192/198/204/207/210` Diana、`:201/213` Carlos、`:216/222` Diana、`:228` Carlos、`:231`（叙述）、`:243/249/255/261/267/273/279` Diana、`:282`（叙述）。
   - **`:90`「What more do you need to do? … The Exterminating Angel? Come on, get your coats.」的说话人判定**：该行没有行内说话人标注。判定链＝① 紧邻的 `:87` 是 Carlos 刚说完 "Five minutes? Why didn't you tell us before you requested it?"；② 下一段 `:93` 紧接着写「Carlos helped the kids with their jackets… Diana, meanwhile, looked around…」，即分工上「催孩子穿外套」由 Diana 说、「帮孩子穿外套」由 Carlos 做；③ 「get your coats」是要求对方去拿外套，与 `:93` 的动作分工一致 ⇒ **说话人是 Diana**。md 块 2（`md:31-39`）把它写成「她张口就是电影」，归属正确（此处不需要改动）。
3. **跨章指认核对**：md 全文无指向其他章的事件描述；唯一疑似跨章的是 `md:39` 的「数锁」（已列 F1，阻断）。原文里「数锁」的真实出处是 `text/ch04_chapter_4.txt:9`。
4. **数字／计数核对**：本章原文的数字只有 `text/ch08_chapter_8.txt:6` 的「two options」（两个选项）与 `:90` 的 "two hours"（两个钟头），md 的「两个钟头」（`md:33`）与原文一致；md 的「四项」与原文的 three 并列结构不符（见 E1）。

---

## 五、修后复核

本单只出指令，**未改动任何 md 文件；git 未执行任何操作**。

| 项 | 期望 |
|---|---|
| F1 数锁 | `md:39` 删去「数锁」，或改写为带跨章出处的表述（`text/ch04_chapter_4.txt:9`） |
| E1 四项/三个短语 | `md:49`、`md:51` 统一为三项 |
| E2 转述形式 | `md:15` 改为「直接引语」 |
| E3 老想跳车 | `md:14` 删「老」 |
| E4 成对的耳环 | `md:11` 改为「又一只、和前几天那只一模一样」 |
| L1–L4 四条漏 | 在 `md:14`、`md:43-51`、块 4/5/6 的「读者视角提示」里补齐对应事实 |

复核命令（修完后应全部 exit=1）：
```
/usr/bin/grep -cE '数锁' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch08 chapter 8.md"
/usr/bin/grep -cE '母亲.*打电话|挂断' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch08 chapter 8.md"
/usr/bin/grep -c '四项' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch08 chapter 8.md"
/usr/bin/grep -c '成对的银圈耳环' "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch08 chapter 8.md"
```

机器层期望：`bash scripts/chapter.sh "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch08 chapter 8.md" --json` 退出码 **0**，`counts.struct_bad 0`、`empty_quote 0`、`keyword_bad 0`、`cjk_low 0`、`quote_long 0`、`segment_miss 0`；`form.h1_shape_ok true`、`nav_count 5`、`blocks 6`。

---

## 六、复核轮次二（2026-10-21 23:35，md 已按本单修过后复核）

- 受审 md 版本：`ch08 chapter 8.md` = 12821 字节 / 126 行 / md5 `15589bfba50f9ffc0d0ac60d5ba53ee5`，对应 commit `9ae597b3f`（21:55:59，「ch08 复核修复（凭空「数锁」/清单项数/耳环成对/Carlos 抱怨时点/伴侣话为直引）」）。
- 机器层复跑：`bash scripts/chapter.sh "…/ch08 chapter 8.md" --json` → 退出码 **0**，`verdict: ok`；`counts`：`struct_bad 0`、`empty_quote 0`、`keyword_bad 0`、`cjk_low 0`、`quote_long 0`、`template 0`、`hole 0`、`block_count 0`、`segments 6`、`segment_miss 0`；`form`：`h1_shape_ok true`、`nav_count 5`、`nav_count_ok true`、`blocks 6`、`block_median 7.5`、`block_range [5,8]`、`profile novels`、`baseline book`；引语字符位 [40, 2534, 2711, 5131, 8042, 10968] 与存档 `2-machine.json` 一致（复跑输出写临时文件，未覆盖存档）。
- 逐字复跑：自写脚本 `check_md_quotes.py`（ch08）→ 原句块 6 条全部命中，词汇例句 MISS 数 = 0。

### 本轮已销账（6 项）

| 原编号 | 状态 | 复核证据 |
|---|---|---|
| F1（阻断） | **已修** | `md:39` 现文：「前面她一直在数电器、数出租车，现在她只能用一部电影来描述自己家里的僵局」——「数锁」已删；`/usr/bin/grep -c "数锁" "…/ch08 chapter 8.md"` → 0，退出码 1。 |
| E1 | **已修** | `md:49` 现文「暖气、直发夹、炉灶和烤箱，三项，一项一项排过来……三个短语的句式完全平行」；`md:51` 现文「注意清单里的第三项——炉灶和烤箱，火就在这里」——与 `text/ch08:93`「the heat wasn’t on, the straightener was safely cooling, and both the stovetop and the oven were off」的三项并列一致。 |
| E2 | **已修** | `md:15` 现文「伴侣的话则全部以直接引语出现，读者听得到他一句接一句的慌张」——与 `text/ch08` 中 Carlos 的 11 处直接引语（`:12/72/87/99/114/147/189/240/246/258/276`）一致。 |
| E3 | **已修** | `md:14` 现文「Carlos 从当场抱怨她突然要跳车」——与 `text/ch08:189`「All of a sudden you’re obsessed with jumping out of trains and cars」一致。 |
| E4 | **已修** | `md:11` 现文「母亲在洗衣篮边捡起一只银圈耳环——和前几天那只一模一样，她坚持说那不是自己的」——与 `text/ch08:27`「a silver hoop earring in her palm」＋`:33`「"Another earring."」＋`:36`「"Like the one from the other day?"」一致。 |
| L4 | **已修** | `md:87` 现文末句「而孩子手里正抱着一个还没拆封的搅拌机玩具，大人盯着那道伤口，却还读不懂它指的是什么」——与 `text/ch08:252`「It was a blender, but they didn’t understand that yet」一致。 |

### 本轮仍未修（3 项，全部为「md 未覆盖原文事实」的漏；提示档）

#### L1｜母亲连打五个电话、Diana 四次挂断仍未进 md｜档：提示（漏）

**原文侧**（`text/ch08_chapter_8.txt:96`，事起）：

> Brisa got upset when she saw the phone ringing. To appease her, and maintain that rare moment of peace, Diana reached out with one finger to decline; the video played on. The phone rang once more and Diana declined it again.

**原文侧**（`text/ch08_chapter_8.txt:111`）：

> One second later, the phone rang again. Carmen called four more times, and all four times, Diana silenced the call.

**原文侧**（`text/ch08_chapter_8.txt:114`，Carlos 开口）：

> "Call her back. It's not normal for her to call this many times," Carlos said. "Look, she called me twice as well."

**原文侧**（`text/ch08_chapter_8.txt:117`，Diana 拒接）：

> "But she's annoying. They're both so annoying. It's most likely something stupid. They can wait, we're in the car already."

**md 侧**：`/usr/bin/grep -cE "司机|挂断|不接|连打" "…/ch08 chapter 8.md"` → **0；退出码 1**。

**影响**：这是全章的暗线发动机——母亲的连环电话与 Diana 的四次挂断，才让 Carlos 说出「给她回个电话，这不正常」（`:114`），也让 Brisa「looking between her mother and father, silently trying to decode the situation」（`:150`）有可解背景。md 写了 Brisa 摔手机（`md:14`）与 Brisa 怀疑地盯着父母（`md:14`），却没写「是谁在打、谁不接」。

**修法**：块 3（`md:43-51`）「读者视角提示」补一句：车里手机响个不停——母亲连打五次，Diana 一次没接（还把手机扔到地上让 Brisa 捡），Carlos 让她回个电话。

#### L2｜司机的两次拒绝仍未进 md｜档：提示（漏）

**原文侧**（`text/ch08_chapter_8.txt:126`，司机）：

> "I can't stop in the middle of Diagonal," the driver said, his voice sour.

**原文侧**（`text/ch08_chapter_8.txt:171`，司机）：

> "It's not early. It's almost eight. And there's barely anything around here—we're in the middle of nowhere. The kids are going to catch cold."

**原文侧**（`text/ch08_chapter_8.txt:180`，司机）：

> "No, no, I can't wait for you. This is my last ride of the night," he rushed to say. His tone had become nasty.

**md 侧**：`md:11` 只写「坐上车后，她忽然要在 Diagonal 路边下车」；md 全文没有「司机」二字（`/usr/bin/grep -c "司机" "…/ch08 chapter 8.md"` → 0，退出码 1）。

**影响**：司机的抵抗是这场戏的外部压力源，也让 `md:57` 那句「我带了袋子、一滴都不会弄到车上」有了对手。缺了司机这层，「编造」这件事的成本显得太轻。

**修法**：块 4（`md:55-63`）「为什么这样写」补一句：司机先是拒绝在 Diagonal 中间停车，又说这是今晚最后一单、不会等他们，她的表演是冲着这个不耐烦去的。

#### L3｜Carlos 在车里的追问链仍未进 md｜档：提示（漏）

**原文侧**（`text/ch08_chapter_8.txt:219`）：

> "Did you hurt yourself? Was there something in the taxi? The seat belt, or something else?" he asked.

**原文侧**（`text/ch08_chapter_8.txt:258`）：

> "Did something happen before? The last few days—did you see anything? A cut, a rash…This kind of thing doesn't just happen,"

**原文侧**（`text/ch08_chapter_8.txt:264`）：

> "Did you do it to yourself?"

**原文侧**（`text/ch08_chapter_8.txt:261`，Diana 否认）：

> "I swear, there's been nothing. Absolutely nothing."

**md 侧**：`/usr/bin/grep -cE "Did you hurt yourself|seat belt|自己弄|割伤|安全带" "…/ch08 chapter 8.md"` → **1**（仅 `md:111` 词汇例句 unbuckled 一行）；正文分析里没有这串问答。

**影响**：Carlos 的第一反应是**找原因**（安全带？之前就有伤？是不是你自己弄的？），Diana 的第一反应是**否认**。这条问答链是「她自己信了」这层判断的实据，`md:61` 只给了结论没给过程。

**修法**：块 5（`md:67-75`）「读者视角提示」补一句：Carlos 连问三句——是不是安全带弄的、之前有没有受伤、是不是你自己弄的；她一口咬定什么都没有。

### 本轮复核命令（原样）

```
/usr/bin/grep -c "数锁" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch08 chapter 8.md"
→ 0；退出码 1（F1 已修）
/usr/bin/grep -cE "四项|第四项" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch08 chapter 8.md"
→ 0；退出码 1（E1 已修）
/usr/bin/grep -c "转述" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch08 chapter 8.md"
→ 0；退出码 1（E2 已修）
/usr/bin/grep -c "老想跳车" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch08 chapter 8.md"
→ 0；退出码 1（E3 已修）
/usr/bin/grep -c "成对" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch08 chapter 8.md"
→ 0；退出码 1（E4 已修）
/usr/bin/grep -cE "母亲.*打电话|挂断|不接|连打" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch08 chapter 8.md"
→ 0；退出码 1（L1 未修）
/usr/bin/grep -c "司机" "notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch08 chapter 8.md"
→ 0；退出码 1（L2 未修）
```

### 本轮结论

- **本章无阻断**：上一轮的 F1 阻断已由 `9ae597b3f` 修掉，复核通过。
- 本轮剩余 3 项（L1、L2、L3）全部是「md 未覆盖原文事实」的**漏**（提示档），**没有一条与原文逐字冲突**。
- 三条漏项的共同后果：md 把「母女连打五个电话」「司机两次拒绝」「Carlos 三句追问」这三段现实阻力全略去了，读者看到的是一场只有两个人在互相对峙的戏。
