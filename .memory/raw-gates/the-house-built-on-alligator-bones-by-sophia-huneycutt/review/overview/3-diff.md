# 总览三篇全篇人判（概述＋金句精选＋情感节点）

机器层：`overview.py quotes`／`overview.py full` 退出码 0——A 整串命中 125｜拼接 0｜省略号图式 0｜查无 0；B 标签对 125｜不符 0；C 跨章多重命中 6（提示）；E H1 错配 0。⑭ 63/63（情感节点 25/25、概述 8/8、金句 30/30）。引语层无缺陷，以下全部在**中文断言层**（本项目已知：总览层中文事件断言没有任何门禁覆盖）。

| # | 型 | 位置 | 现象 | 原文依据（逐字） |
|---|---|---|---|---|
| G1 | 阻断·张冠李戴 | 00_概述.md:18「三、学徒、继承人与一屋子试探」 | 把破坏清单写成「**被切成两半的皮**」；原文两半的是**动物尸体**（鱼、鸭、天鹅、水獭），皮是被切成半英寸宽的条 | text/ch21_chapter_twenty.txt:12 `cutting all twenty into half-inch-wide strips that dangled from the ceiling like party fringe`；:276 `All of them halved.`／:279 `More accurately, ripped in half. Like an animal had torn into them.`（主语＝:273 `Animal carcasses…Fish, mostly, but also ducks and swans and an otter or two`） |
| G2 | 阻断·地点（同一错落两文件） | 00_金句精选.md:65（⑥ 上下文）＋00_情感节点.md:74（节点七 叙事概括） | 都写成「在 **Henri 家门口**把 Leon 那一夜和盘托出」；原文供述发生在 **Henri 屋内**（壁炉边），Henri 起身去泡澡后才开始 | text/ch41_chapter_forty.txt:18 `Inside Henri’s house, Aunt Virginia placed my umbrella in the mudroom`；:21 `In the living room, a gas fire whirred gently…Henri reclined on a leather couch`；:45 `Henri rose from the sofa…I’ve been hankering for a nice bubble bath. You two go on and sit by the fire.`；:285 `Then I opened Henri’s door and stepped outside`（离开时才到门口） |
| G3 | 阻断·计数断言＋过度具体 | 00_情感节点.md:86（节点八） | ①「**数十条**鳄鱼张着嘴逼近」——原文无此数：先两条，后作「数不清的黄眼睛」「它们当中一半」；②「**门上挂着** Gazzie 的锁」——原文只写「Gazzie 把我锁在了里面」，无挂锁形象 | text/ch44_chapter_forty_three.txt:105 `Countless yellow eyes shone at me`；:147 `Half of them stood out of the water by that point`；:63 `Gazzie had locked me inside.`（另 :60 只写 `the barbed wire lining the ten-foot fence`） |
| G4 | 提示·归属 | 00_概述.md:56（Virginia 段） | 「在自家后院办烤猪会」——烤猪会是 Henri 家的后院、Henri 的客人、Henri 宣布猪好了；主体被安到 Virginia 身上 | text/ch24_chapter_twenty_three.txt:129 `When the sky turned pink, Henri waved her guests outside. Her backyard overlooked a sand dune…Over a fire, a whole hog…rotated on an iron spit`；:213 `When Henri declared the hog ready`；另 text/ch11_chapter_ten.txt:78（年度烤猪会在 Greer House 一带办，也非 Virginia 后院） |
| G5 | 提示·口径 | 00_概述.md:56 | 「自认曾毁灭证据、**作过伪证**」——原文是 `given a false alibi`（提供虚假不在场证明），与「伪证」不同格 | text/ch41_chapter_forty.txt:243 `When I’d helped destroy evidence, given a false alibi?` |
| G6 | 提示·重复 | 00_情感节点.md:110（节点十 叙事概括） | 同一句「画像仍躺在原地、斧头还插在胸口、霉斑爬满那张脸」在同一段内出现两次（前一次带分号、后一次带逗号），形态缺陷非事实缺陷 | 原文一次：text/ch49_epilogue.txt（画像＋斧＋霉斑） |
| G7 | 提示·唯一性 | 00_情感节点.md:64（节点六）＋00_金句精选.md:221（⑳ 上下文） | 「**全书唯一一次** Ida 有形现身」——按「有形／被看见」计，ch05 另有窗内掠过的人形；建议改「最完整的一次」（若保留「唯一」须限定「以裙、靴、湿脚步成形的全身显形」） | text/ch05_chapter_four.txt:27 `Quick as a thought, a figure passed behind the farthest second-floor window`；text/ch31_chapter_thirty.txt:21–39（唯一成体系的全身显形＋其后的「just the curtain」） |

## 总览层已核实为正确（抽样回源全部命中，勿改）

- $30,000 撕成两半的支票（text/ch02:24）；「Mama had lied to me for thirty-two years」（text/ch02:56）。
- 十五英尺皮、头有三个人头合起来大、挂在楼梯旁（text/ch05:126／:117–120）；Ida 六十五岁生 Gazzie（text/ch10:192）。
- 骨堆在地基之下＋新骨尽量靠过去＋Caroline 起的外号（text/ch30「We place them close as we can to the original bones…」）。
- 发酸的茉莉在全书的第一次到场确在 ch07（`/usr/bin/grep -rn jasmine text/ch0[1-7]*.txt` → 仅 text/ch07_chapter_six.txt:93）——节点四「第一次飘过来」成立。
- 锁箱内容：消防报告（accelerants／multiple points of origin／set with intent）＋两本同日不同额账簿＋市长信＋George R. 两张字条（text/ch40:21）——概述 §七 逐格对得上。
- 墙龛罐子＝发、牙、血；螺钿＝牙、稀漆＝血（text/ch46:42–45）。
- 身体这条线：Hashimoto’s（Virginia 与 Gazzie 同有）、祖母 POTS、盐片（text/ch04:73–81）；Mama 的 lupus 与肾移植（text/ch19:102）；心梗（text/ch42:195、ch41:222）；150 磅（text/ch38:9）。
- 「Ironheart’s death was our beginning」为祈请、Mama 墙上是判词（text/ch30:252–264）——概述 §五 的改判关系正确。
- 「I’m not like them!」→「I’ll fix it.」→「One by one, the alligators turned toward the pond and began their slow retreat」（text/ch44:138／:150／:162）——节点八喊话内容与逐条退回成立。
- 锁孔黑眼（text/ch45:66）在「毁掉这栋房子」的计划（:108）**之前**——节点八末句顺序正确；先怀疑 Ida、再自我说服是 Gazzie（:69 `No, I reassured myself. Gazzie.`）成立。
- 医院「out a side entrance」＋`The Uber driver`（text/ch47:117／:123）、`hundreds of white sticks…decades of alligator bones freed by Flora’s floodwaters`（:120）——节点九／十成立。
- 金句 ⑮ 的「Michelle 之死地点书内两处写法不同，本条只按本章原文呈现，不作裁定」**必须保留**（text/ch04:168 岸边发现 vs text/ch18:321／ch29:177 操场）——不得被任何整改合并。
- 多版本 Leon 之死、Mama 之死、超自然是否发生、她是否怀孕：总览三篇一律不裁决，且 ⑳/㉑/㉒ 的「留退路」「问号」「三个没有」判定准确——护栏条目。
