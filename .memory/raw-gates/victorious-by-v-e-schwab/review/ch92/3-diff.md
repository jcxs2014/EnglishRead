# 3-diff.md · 《Victorious》第 92 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch92_chapter_xxii.txt`
- 受审 md：`ch92 the empty cartridge.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L2 · R1 事实未进 md（scanned the crowd and counted twenty, maybe thirty people in）
- **原文**：原文 L42：Victor scanned the crowd. Twenty, maybe thirty in total.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L42：原文 L42 的事实「scanned the crowd and counted twenty, maybe th」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 1（阻断 0 / 提示 1） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（64 词 3 句）：Victor let the hum wash over him, his senses stretching out until they brushed the nearby study group, the trio of faculty on their phones, the young couple shoulder to shoulder. As he studied the people ranged around the steps, Dani studied him. Beneath his shirt and coat, the monitor pressed between his ribs, its sensor feeding vitals to the tablet in real time.
- 中文理解：维克多任那股嗡鸣漫过来，感官往外铺，先碰到近处的自习小组，再是三个打电话的教员，还有肩挨肩的一对年轻人。他看台阶上这些人，丹妮在看他。衬衫和外套底下，监测器压在他肋骨之间，传感器把生命体征实时送进平板。
- 关键词：wash over him · Dani studied him
- 为什么这样写：这一段先把他的感知铺开成一张网：自习小组、三个教员、一对年轻人，由近及远地排过去，读者的视线跟着他往外走；随后一句把镜头折回来——他看别人，丹妮看他。最后才落到肋骨间那块监测器上：他身上发生的事，同时正被读成屏幕上的数字。
- 读者视角提示：读者跟着他的感官在人群里走了一圈，又在同一段里被提醒这些感知有仪器在记。他往人群里伸得越远，这一段的分量就越往「被测量」那一侧偏。
- **原文**：原文 L30-L30
- **结论**：引语 3 句 64 词（原文 L30）：中文理解逐句对得上，主语=维克多、受事=肩，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（52 词 3 句）：He could have leveled all of them at once, through sheer brute force, but that wasn’t the point. Victor had always preferred to use his power like a scalpel, not a hammer, but now, it was imperative. If there was a limit to what his body could endure, then efficiency was everything.
- 中文理解：他本可以靠蛮力一次把在场所有人放倒，可那不是他要的。他一向更愿意把能力当手术刀用，而不是当锤子；到了现在，这一点成了必须。身体能承受的东西既然有上限，效率就成了全部。
- 关键词：like a scalpel · efficiency was everything
- 为什么这样写：三句话都在给同一件事让路：先否掉最省事的做法（蛮力），再给出他一贯的偏好（手术刀而不是锤子），最后把偏好升级成必须——"now, it was imperative"。理由是身体有上限，于是「效率」被放到句尾，成为这一段的落点。
- 读者视角提示：读者在这里拿到的是一条自我约束：他能做的比他要做的多得多。约束的理由写得很直白——身体有上限，所以只做小动作、只碰一两个人。
- **原文**：原文 L45-L45
- **结论**：引语 3 句 52 词（原文 L45）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=手术刀，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L24）
- **档**：相符

### 原句 3
- **md**：引语（51 词 3 句）：One by one, they each stopped running, dragged to a stop by the unseen force of Victor’s will. Distantly, he felt the tightness forming in his chest, but he didn’t let go. Unlike the bodies on the Slope, the players struggled, each locked in their own sudden war against his hold.
- 中文理解：草坪上那些踢球的人一个接一个停下，被他的意志拖住。他远远地觉出胸口在收紧，却没有松手。跟台阶上那些人不一样，这些球员在挣——每个人都被锁进一场突然打起来的仗里，对手是那只按住他们的手。
- 关键词：the unseen force · didn’t let go
- 为什么这样写：句子把「停」写成一串动作：一个接一个、被拖住。第二句把镜头挪进他身体里——胸口在收紧——随即用「但他没松手」把这层感觉压回去。第三句才交代差别：跟台阶上那些身体不同，球场上这些人在挣；"sudden war" 把这场不动手的按压写成对抗。
- 读者视角提示：读者同时拿到两个进度：外面被按住的人越来越多，里面胸口越来越紧。他没有松手，这个动作把外面和里面两条进度并到了一起。
- **原文**：原文 L66-L66
- **结论**：引语 3 句 51 词（原文 L66）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L30）
- **档**：相符

### 原句 4
- **md**：引语（44 词 2 句）：What happened was he’d gone searching for his limits in a crowded concert, and he’d found them. Which was how he’d also found that controlling bodies took more strength than simply dropping them. But what he said was simply, “I took a second dose.”
- 中文理解：事情是他跑到一场拥挤的音乐会上去找自己的上限，并且找到了。也是在那里，他发现操控身体比单纯把人放倒更费力气。可他嘴上只说了一句：「我吸了第二剂。」
- 关键词：a crowded concert · a second dose
- 为什么这样写：这一段先在心里把经过讲全：去哪、找什么、找到什么、顺带学到什么；然后一句「但他说的只是」把前面全部收掉，只留一句承认。前两句是给读者的，第三句是给丹妮的，两者的落差就是这一段的分量。
- 读者视角提示：读者知道的比丹妮多：上限是在音乐会上试出来的，操控比放倒更费力。她只听到「第二剂」四个字，所以后面她讲药理时，读者已经先一步明白事情到了哪一步。
- **原文**：原文 L120-L120
- **结论**：引语 2 句 44 词（原文 L120）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L36）
- **档**：相符

### 原句 5
- **md**：引语（68 词 3 句）：“It worked, because this,” she said, holding up the empty vial, “is a suppressant and a stimulant, which means you’re walking a chemical tightrope. That’s why I can’t increase the dosage, and why you can’t take more than one. It’s a fine fucking balance between risk and reward, and if you take too much, you’ll do more damage to your heart, and it won’t keep you from dying.
- 中文理解：丹妮举着空药管说：它管用，是因为这东西既是抑制剂又是兴奋剂，等于在化学钢丝上走。所以她不能加剂量，他也不能多吸一次。风险与回报之间是一道极细的平衡；吸多了只会更伤心脏，而且拦不住死亡。
- 关键词：a chemical tightrope · risk and reward
- 为什么这样写：她的反驳从「它管用」开始——先承认他的观察，再把「管用」拆成两种相反的作用，于是「加量」这个请求在药理上就不成立。后面两句是代价清单：更伤心脏、拦不住死。句子越往后越硬，最后落在 "dying" 这个词上。
- 读者视角提示：读者刚跟着维克多把剂量看成解决办法，这一段把同一个东西翻过来：它压住的是感觉，不是病情。她举着空药管说话，那支空管本身就是证据。
- **原文**：原文 L132-L132
- **结论**：引语 3 句 68 词（原文 L132）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=药，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L42）
- **档**：相符

### 原句 6
- **md**：引语（36 词 2 句）：The body was a machine, and he had been so focused for so long on keeping one part from breaking down, he had neglected the others. He had been to hell and back a hundred times.
- 中文理解：身体是一台机器；他太久只顾着不让其中一个部件坏掉，把其余的都撂在一边。他已经在生死之间来回过一百次。
- 关键词：a machine · to hell and back
- 为什么这样写：前一句把身体说成机器，随即给出账目：盯着一个部件，漏掉其余。后一句不再解释，只报次数——一百次。两句话之间没有转折词，机器的比喻和「来回一百次」并排放着，分量落在后一句。
- 读者视角提示：读者听到的是一句自我结算：一百次来回，换来的是「只顾一个部件」这个结论。他自己把话说得这么平，反而比抱怨更重。
- **原文**：原文 L153-L153
- **结论**：引语 2 句 36 词（原文 L153）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L48）
- **档**：相符
