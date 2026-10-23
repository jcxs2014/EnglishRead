# ch07（书内 Chapter Six）深审 R3/R4 三张单子

素读基线：`review/ch07/1-suread.json`（36 条事实／0 MISS，只读 `text/ch07_chapter_six.txt`，写完才开 md）
机器层：`review/ch07/2-machine.json` → verdict `ok`（blocks 3 ∈ 短篇档 target [2,3]；segments 3／MISS 0；words 1015；无报警）
直撇号探针：`/tmp/apos.txt` 未列 ch07 ⇒ 0 站

## 🟥 阻断（7）

### C-07-1 与本章首句冲突：「本章她不画画」
- md:12：**「本章她不画画，改翻找：抽屉、床底、壁橱顶层，最后蹲下去读墙。」**
- 原文逐字：`text/ch07_chapter_six.txt:9` — `After dinner, I drew at Mama’s desk for an hour or so, mind roiling with resentment. Once I’d outlined a flattened possum I’d passed on the highway, I closed my sketchbook and wandered to a window, trying not to hate myself for the foul image I’d created.`
- 判定：本章开场就是画了一个多小时（压扁的负鼠），画完才起身；md:11 自己还写「恨自己画出的压扁负鼠」⇒ 导航内部互抵。改法：「本章她先画完一只压扁的负鼠才起身翻找」。

### C-07-2 外貌凭空：把 brunette 写成「短发」
- md:12：**「大笑的短发少女，和把自己活成『hall monitor、prison guard』的控制者」**
- 原文逐字：`text/ch07_chapter_six.txt:21` — `A brunette girl in short shorts ran barefoot down a beach.`
- 判定：brunette 只指发色（深褐），全章无一处写发长；`short shorts` 的 short 属短裤。此处把「short」从裤子迁移到头发，属凭空外貌。改法：「大笑的棕发少女（穿短短裤、赤脚跑下沙滩）」。

### C-07-3 道具归属：鳄鱼头骨在把手上，md 挂到了钥匙上
- md:10：**「夜里却用那把藏着鳄鱼头骨的钥匙把自己反锁」**（md:12「反锁门」、md:13「被反锁的门」同批）
- 原文逐字：`text/ch07_chapter_six.txt:84` — `Tiptoeing to the door, I turned the skeleton key in the lock, noting the subtle shape of an alligator skull hidden in the intricate handle.`
- 判定：`hidden in the intricate handle` 的落点是把手（她锁门时顺势看到的门把手雕花），钥匙在原文没有任何形状描述；且本章前接 `text/ch05_chapter_four.txt:201` — `If you want extra privacy, there’s a key in your lock.`——钥匙是现成装在锁里的，形状从未描写。

### C-07-4 裁决了本章的悬置项：「不是有什么进来」
- md:13：**「『不速之客』也被反锁的门调转方向：不是有什么进来，是她把自己关进去。」**
- 原文逐字：
  - `text/ch07_chapter_six.txt:93` — `I hadn’t noticed it around Gazzie or Aunt Virginia, but who else would it belong to? Or was it just the wilting jasmine I’d seen covering the side-yard fence?`
  - `text/ch07_chapter_six.txt:96` — `“Hello?” I whispered.`
  - `text/ch07_chapter_six.txt:99` — `Then came the sound of a sigh so soft I still think I could have imagined it.`
- 判定：门外是否有者、气味属谁、叹息是否幻听——本章把三件事全部留在未决（本项目对本章的裁决红线＝超自然是否发生不裁决）；「不是有什么进来」把它关掉了，并与 md:46 自己的「记在未决清单上，别急着划掉」直接矛盾。改法：只写「方向调转：先写她把自己关进去，门外留下没有解释的声响与气味」。

### C-07-5 归属：电气借口配给了 whir，原文配的是 creaking
- md:14：**「收尾的恐惧落在嗅觉：先给 whir 声配了电气这个借口，再给茉莉香——什么借口都没给。」**
- 原文逐字：`text/ch07_chapter_six.txt:90` — `A faint whir filled the air, and I sighed. Maybe the creaking was another of Greer House’s quirks, like the noisy electrical system.`
- 判定：`the creaking`（:87 的地板吱嘎）才是借口所指；whir 在原文没有任何解释，紧接的是 :93 的气味。这句把两个声响的解释关系倒置，也正是「分析层归属」类缺陷。

### C-07-6 漏 :57 第二行墙句 `Death was our beginning`（含 :61 的反应）
- 原文逐字：`text/ch07_chapter_six.txt:53` — `Below it lay another line:` ／ `:57` — `Death was our beginning` ／ `:61` — `A chill ran up my arms.`
- 判定：本章共四条墙句，md 引到三条（:43 书名句／:68 `The devil’s inside`（md:14）／:71 `She’s in us`（md:36）），独缺最短、最先起寒的第二条；`/usr/bin/grep -c "Death was our beginning" "ch07 mothers handwriting on the closet wall.md"` → 输出 `0`，退出码 `1`；词表亦无。它同时是本章「字迹一遍比一遍潦草」之前唯一的第二级台阶。

### C-07-7 漏 :27 Mama 的直接引语 `What don’t you understand? No one is safe around you.`
- 原文逐字：`text/ch07_chapter_six.txt:27` — `And the childhood she’d given me—my mind flashed to her locking my bedroom door as I begged to join a teen art club at the library. What don’t you understand? No one is safe around you.`
- 判定：本章除临终话之外 Mama 唯一的一句直接引语，是「锁门＝保护」这条自辩的原文凭据，也是 md:12「控制者」与 md:24「为什么要离开」两处论断的依据；md 全篇 0 次命中（`/usr/bin/grep -c "No one is safe" "ch07 mothers handwriting on the closet wall.md"` → 输出 `0`，退出码 `1`）。

## 🟨 提示（7）

- P-07-1 md:10「鞋盒里几十张宝丽来全是少女时代大笑的 Mama」——同一盒里还有那个男孩（:21 `A dull-eyed boy in a tan suit, two or three years younger than Mama, stood beside them.`）；「全是」过头（「每张她都在笑」本身 ✓）。
- P-07-2 md:11「相册里的笑」——原文是鞋盒里的散片（:18 `a shoe box`、:21 `Inside lay dozens of Polaroids`），无相册／无本子。
- P-07-3 md:13「死者蹲在壁橱墙下写的警告」＋md:83 同句——:33 是明喻（`like someone had scribbled them crouched on the ground`），:36 认出的是笔迹（`Mama’s handwriting. Less elegant than what I’d grown up with, but she had been younger here, less practiced.`），姿势并非被证实的事实；建议保留「像是蹲在地上写的」。
- P-07-4 md:24「这一行没有第一人称、没有出处、没有时态让步」——同段下一句即「写下它的手被认出来了」，「没有出处」与自己的下半段互抵（可改为「这一行不写自己、也不写谁让它存在」）。
- P-07-5 md:26「这就是本书书名的出处」——属书外断言（文本只给这一行字）；建议「本章第一次给出与书名同形的一行字」。
- P-07-6 漏三处小单元：:90 `Initially, I wasn’t afraid. Gazzie’s and Aunt Virginia’s rooms were on the second floor; they were probably going to bed.`（她给的第一解释）；:30 `I spied the hint of braces behind her lips. I bet they’d been the bane of her preteen years, like they’d been for me.`（母女共用的一处少年烦恼）；:75 `A breeze blew against my neck—a window, I thought, must be open—and I shivered.`（本章第二次风，与 :12 `billowed in the warm breeze` 成对）。
- P-07-7 词表 12 行未收本章四个承重词：`skeleton key`（:84）、`Polaroid`（:21）、`hall monitor`（:27）、`croaked`（:75，已在精读关键词里出现但无档位释义）。

## ⬜ 假红／不报

- md:36「读回墙上那句 She’s in us」——:71 逐字 ✓；「只差一个代词」的对照与 :75（`She’s in you, too.`）一致，✓。
- md:34「句尾的 too 把『她在你身上』从一个人扩展到多人」——:75 两句相邻 ✓。
- md:14「月光充当照明器，逐段点亮鞋盒、字墙与那行书名级短句」——:21／:39 `I let moonlight illuminate the first phrase`／:64 `the moonlight fell on two similar phrases side by side` ✓ 三级递进成立。
- md:20 中文理解对 :43 的直译 ✓；「Greer 家把他们的财富建在鳄鱼骨头上」与原文逐项对应。
- md:83「今晚已经先给自己反锁了门」的动作次序 ✓：:81 决定 → :84 锁门 → :87 吱嘎（与 md:12「身体后退、意志前进」不冲突）。
- 短篇档 3 块＝target [2,3] 合规，不以块数报漏（漏项见 C-07-6／C-07-7／P-07-6）。
