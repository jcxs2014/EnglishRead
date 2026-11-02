# 3-diff.md · 《Victorious》第 55 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch55_chapter_iv.txt`
- 受审 md：`ch55 sydney meets the dead man.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（质问她 Victor 在哪里）
- **原文**：原文 L75：“But first, I want you to tell me…” Eli leaned in, so close their heads were nearly touching. “Where is Victor?”
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L75：原文 L75 的事实「质问她 Victor 在哪里」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 1（阻断 0 / 提示 1） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（51 词 3 句）：The hairs rose on the back of her neck, and her fingers darted toward her backpack strap, before remembering it wasn’t there. She’d left the bag—and the gun—up by the edge of the pool. Syd swore under her breath and crouched to free the knife from its sheath on her calf.
- 中文理解：她后颈的汗毛竖了起来，手指先朝背包带伸过去，随即想起背包不在身上。她把背包和枪都留在泳池边了。西德妮低声骂了一句，蹲下去把小腿刀鞘里的小刀抽出来。
- 关键词：her backpack strap · under her breath
- 为什么这样写：手指先动、记忆后到，慌张因此落在动作上而不是念头里。第二句把失手的账摊开：包和枪都在泳池那头，能用的只剩小腿上那把。第三句不解释情绪，只写她低声骂了一句、蹲下去抽刀，一个具体动作把怕接住了。三句连起来，读者拿到的是她此刻手里的全部家当。
- 读者视角提示：读者跟着她先摸了个空，再想起武器被自己留在了身后。等到那把刀真的捅出去，读者已经知道它是她身上唯一剩下的东西。
- **原文**：原文 L21-L21
- **结论**：引语 3 句 51 词（原文 L21）：中文理解逐句对得上，主语=西德妮、受事=枪，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（65 词 2 句）：Syd scrambled up the last rungs on the ladder and lunged for her backpack, expecting to be intercepted right before she reached it, to feel hands darting out of darkness, out of nowhere—but she made it. She swung the bag onto her shoulder, and started for the chain-link fence that ran around the pool, and that was when she looked up and saw Eli Ever.
- 中文理解：西德妮爬完最后几级梯子，扑向自己的背包，一路上都在等着有人在最后一刻截住她，等着黑暗里突然伸出几只手——可她拿到了。她把包甩上肩，朝围住泳池的铁网走，抬头的那一刻看见了伊莱·埃弗。
- 关键词：lunged for her backpack · chain-link fence
- 为什么这样写：句子先把她预想的坏结果整段铺开：会被截住、会有手从黑暗里伸出来，然后一句「可她拿到了」把这个预想撤回。撤回让读者的警觉松了一格，紧接着的下半句才把伊莱放进画面，落点是「看见」而不是「被发现」。
- 读者视角提示：读者刚被放进「这一关过了」的错觉里，抬头这一下才算真正交付威胁。来的人比脚步声难对付得多。
- **原文**：原文 L33-L33
- **结论**：引语 2 句 65 词（原文 L33）：中文理解逐句对得上，主语=西德妮、受事=网，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L28）
- **档**：相符

### 原句 3
- **md**：引语（37 词 3 句）：Because she’d killed him. Seen the blood soak through his shirt and the life leave his eyes. Except he couldn’t be a ghost because his boots were thudding softly on the pavement as he walked toward her.
- 中文理解：因为是她杀了他；她亲眼看着血浸透他的衬衫，看着那点活气从他眼里退走。可他也不可能是鬼，因为他朝她走过来时，靴子踩在路面上有轻轻的闷响。
- 关键词：couldn’t be a ghost · killed him
- 为什么这样写：先给「鬼」这个结论的凭据：人死了，血和眼神她都看过。紧接着用一句「可他不可能是鬼」把结论翻掉，依据只有一样东西——脚步声。推翻得这么轻，恐怖感反而更实，读者因此被迫接受更难受的那个答案：走过来的不是鬼。
- 读者视角提示：读者和她一起把两种解释都推到尽头，最后落在一个听觉细节上。她先承认自己杀过人，这个承认一落地，眼前这个人的分量就变了。
- **原文**：原文 L36-L36
- **结论**：引语 3 句 37 词（原文 L36）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=血，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L38）
- **档**：相符

### 原句 4
- **md**：引语（38 词 2 句）：Eli fired, and Syd felt the force slam into her back, enough to make her stumble—but she hadn’t been hit. Her backpack had absorbed the blow, not a bullet, but a small red dart lodging in the fabric.
- 中文理解：伊莱开了枪，西德妮感到一股力道撞在背上，撞得她踉跄了一下——可她并没有中弹。挡住那一下的是她的背包，扎进布里的不是子弹，是一支小小的红镖。
- 关键词：not a bullet · red dart
- 为什么这样写：先写冲击，再否定中弹，最后才交代打中的是什么：一支小红镖。惊吓被往后推了两拍才落地，落地时性质已经变了。枪声本该配上要命的弹，这里却给了一支扎在布上的小东西，凶险与分寸并排放着，谁都不去解释。
- 读者视角提示：读者要在这里改一改「他开枪就是要她死」这个预判：打中的是一支镖，力道仍然把她撞得踉跄，性质却已经不同。
- **原文**：原文 L45-L45
- **结论**：引语 2 句 38 词（原文 L45）：中文理解逐句对得上，主语=西德妮、受事=枪，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L48）
- **档**：相符

### 原句 5
- **md**：引语（32 词 4 句）：He continued forward and she continued back, until something stopped her. The railing of the motel stairs. The ones that led up to the second floor. To Dol, and Mitch, and help.
- 中文理解：他往前一步，她退一步，直到有什么东西挡住了她：旅馆楼梯的栏杆。那道楼梯通到二楼，通向 Dol，通向米奇，通向援手。
- 关键词：motel stairs · To Dol, and Mitch
- 为什么这样写：全段是一组对照：他 forward，她 back，两个动词一推一收，中间用 until 挂住。真正挡住她的是一道栏杆——具体的、可以用手抓住的东西。接着三个短句把栏杆背后的内容一层层摊开：二楼、Dol、米奇、援手。援手是最后一项，也是最远的一项；句子停在 help 上，前面几个词就已经让读者知道这道楼梯意味着什么。
- 读者视角提示：读者跟着她数这道楼梯还有几级——四级。上面有狗、有人、有救兵，可她只上了四级就被抓下来。这一段把「差一步」的量算给读者看。
- **原文**：原文 L51-L51
- **结论**：引语 4 句 32 词（原文 L51）：中文理解逐句对得上，主语=米奇、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L58）
- **档**：相符

### 原句 6
- **md**：引语（52 词 3 句）：As Eli’s hand closed around her throat, she drove the blade into his forearm. It went straight through, buried to the hilt on one side, the bloody tip protruding from the other. Anyone else would have cried out, but Eli simply glared, through gritted teeth, as his blood dripped onto her coat.
- 中文理解：伊莱的手一合上她的喉咙，她就把刀送进了他的前臂。刀整个穿过去，一侧没到刀柄，带血的刀尖从另一侧探出来。换了别人早该叫出声，伊莱只是咬着牙瞪她，血一滴一滴滴在她的外套上。
- 关键词：drove the blade · gritted teeth
- 为什么这样写：掐喉和捅刀写在同一个句子里，两个动作互相咬着，谁也不占上风。第二句把伤口写到具体位置：这一侧没到刀柄，那一侧露出刀尖，让读者相信这一下真的造成了伤害。第三句用「换了别人」作比，把伊莱从人的反应里划出去——不喊、不退，只瞪。
- 读者视角提示：读者刚以为她扳回一手，这一句又把胜负压平：他受了伤，手却没松。血滴在她的外套上，伤口的代价因此落到她身上，而不只是他的手臂。
- **原文**：原文 L63-L63
- **结论**：引语 3 句 52 词（原文 L63）：中文理解逐句对得上，主语=伊莱、受事=血，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L68）
- **档**：相符

### 原句 7
- **md**：引语（20 词 2 句）：“I remember. Vividly,” he said, one knee pressing into her cracked ribs. “Don’t worry,” he added, “I’ll return the favor.”
- 中文理解：「我记得。记得很清楚，」他说，一条膝盖压进她裂开的肋骨里。「别担心，」他又说，「我会还你这份人情。」
- 关键词：one knee pressing · I’ll return the favor
- 为什么这样写：回应落在两个字上：I remember——读者刚在上一块看见她承认自己杀过他，这里是他承认记得。这两句台词都短，却各自压着一个动作：说第一句时膝盖压进裂肋，说第二句时是 added，追加的、不看她的。cracked ribs 用被动式的过去分词，像是之前就裂了，现在只是被压住的那个位置。
- 读者视角提示：读者在这里听见两个人把同一件事说成两笔账：她记得杀他，他记得被她杀。这一句把两笔账并排放着，谁也没输。
- **原文**：原文 L69-L69
- **结论**：引语 2 句 20 词（原文 L69）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L78）
- **档**：相符
