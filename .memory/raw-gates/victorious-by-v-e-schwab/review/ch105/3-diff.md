# 3-diff.md · 《Victorious》第 105 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch105_chapter_xxxv.txt`
- 受审 md：`ch105 the tablet and the knife.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（the number of cameras that showed the red pickup: One）
- **原文**：原文 L57：One of the external, motion-activated cameras showed a red pickup driving through the gates. Change of plans, thought Gabriel.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L57：原文 L57 的事实「the number of cameras that showed the red pick」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 1（阻断 0 / 提示 1） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（49 词 2 句）：He wouldn’t have known that anything was different if not for the pain in his leg as he moved toward the door. With every step, the room around him flickered, revealing momentary glimpses of an altered room—a shattered glass, Helena’s blood, and ash, the furniture askew—before regaining its composure.
- 中文理解：要不是腿上的痛，他不会知道有什么不一样。他朝门口走，每走一步，四周的房间就闪一下，露出另一个房间的样子——碎掉的玻璃杯、海伦娜的血、灰烬，家具歪着——然后又恢复原状。
- 关键词：an altered room · the furniture askew
- 为什么这样写：第一句把「不一样」全部压进腿上的痛，用 if not for 把痛设成唯一的线索。第二句跟着脚步走：with every step 之后房间闪一次，破折号里排开四样东西，破折号合上又写回 composure，房间看着又完整了。
- 读者视角提示：读者跟着他一步步挪，看到房间在两个版本之间切换；破折号里的那几样只在痛的瞬间露出来。段落最后落在 composure 上，画面收得干干净净，像什么都没发生。
- **原文**：原文 L24-L24
- **结论**：引语 2 句 49 词（原文 L24）：中文理解逐句对得上，主语=海伦娜、受事=门，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（66 词 3 句）：He must have known, on some level, that he would not see his wife and son, much as he had loved them, would not find himself transported to the house upstate, or the one he’d built his practice in. The years he’d spent toiling away on cases with no novelty, no chance for innovation. Because his job was here, his purpose, here, surrounded by his work.
- 中文理解：他大概在某个层面上早就知道：他不会见到妻子和儿子，尽管他很爱他们；也不会被送到州北那栋房子，或是他挂牌行医的那一栋。那些年他埋头办没有新意、没有创新机会的案子。因为他的工作在这里，他的目的在这里，被工作围着。
- 关键词：no chance for innovation · his purpose
- 为什么这样写：第一句先让一步（much as he had loved them），再把两个「不会」并排：不会见到妻儿，不会被送到那两栋房子。第二句只写那些年办的案子，no novelty 与 no chance for innovation 把一长段年头压成一句。第三句用 Because 起头，把 job 和 purpose 各说一遍，两个 here 夹在中间，末尾落在 surrounded by his work。
- 读者视角提示：这一段是他自己算的账：妻儿、上州的房子、挂招牌行医的那栋、那些没有新意的案子，都列在「不会」那一边，最后剩下的只有办公室。两个 here 把范围收得很窄，句末的 surrounded 又把这个范围围紧。
- **原文**：原文 L33-L33
- **结论**：引语 3 句 66 词（原文 L33）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L24）
- **档**：相符

### 原句 3
- **md**：引语（43 词 3 句）：There his good mood guttered when he found Noah lying dead. He saw—and didn’t see—the body. It lay there in reality, but had been neatly excised from his dream, the body only visible in fragments, when the pain shot up his injured leg.
- 中文理解：走到走廊，他的好心情灭了——他发现诺亚躺在那儿，已经死了。他看见了，又没看见那具尸体。尸体确实躺在现实里，却从他的梦里被干净地切掉，只有痛从伤腿窜上来的时候，才看得见一些碎片。
- 关键词：lying dead · neatly excised
- 为什么这样写：第一句先写 mood guttered，再补原因，情绪在句子开头就掉下去。第二句用两个破折号把 saw 和 didn’t see 夹在一起，同一个动作既是看见又是不看见。第三句给机制：in reality 与 from his dream 各站一边，最后用 when 把痛接回来。
- 读者视角提示：读者和他在同一刻看见尸体，又在同一刻看不见它。第三句把「看得见」的条件写成痛：伤腿一疼，那具尸体才露出碎片。
- **原文**：原文 L39-L39
- **结论**：引语 3 句 43 词（原文 L39）：中文理解逐句对得上，主语=诺亚、受事=碎片，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L30）
- **档**：相符

### 原句 4
- **md**：引语（40 词 3 句）：A detail Gabriel kept close at hand as he continued down the hall. He found several agents blindly wandering, rendered useless by Serena’s fog. He tried to wrest them back, will them into doing as he said, to no effect.
- 中文理解：他把这个细节揣在身上，继续沿走廊走。他找到几个特工，他们在塞雷娜的雾里瞎转，已经派不上用场。他试着把他们拉回来，试着让他们照他说的做，没有用。
- 关键词：blindly wandering · wrest them back
- 为什么这样写：第一句把上一段得到的细节收成 a detail kept close at hand，人还在往前走。第二句写他看到的人：几个特工在雾里打转，rendered useless 是结果。第三句连用两个动作（wrest them back / will them into doing），句末 to no effect 把力气全部作废。
- 读者视角提示：这一段的重心是他发现自己指挥不动人：两次尝试都写出来了，结果只有一个词。他能带走的只有那个细节。
- **原文**：原文 L48-L48
- **结论**：引语 3 句 40 词（原文 L48）：中文理解逐句对得上，主语=塞雷娜、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L36）
- **档**：相符

### 原句 5
- **md**：引语（50 词 3 句）：He freed a tablet from an agent’s hand and ordered Control to lock the building down. Was annoyed but unsurprised when no one answered. Using the device to scan the cameras, he located Sydney and Serena, and he was about to head toward them when something flashed across the screen.
- 中文理解：他从一个特工手里抽出平板，命令 Control 封锁大楼。没人应答，他恼火，却不意外。他用这台设备扫摄像头，找到了西德妮和塞雷娜，正要朝她们去，屏幕上有什么闪了一下。
- 关键词：ordered Control · flashed across the screen
- 为什么这样写：第一句两个动作连着：拿走平板、下令封锁。第二句省掉主语，只剩 Was annoyed but unsurprised 与 when no one answered，「没人应答」摆在句末。第三句用现在分词一路推进，先给 located 的结果，再用 when 把方向掰到屏幕上的那一下。
- 读者视角提示：读者跟着他的手走：抽平板、下令、扫摄像头，一路都在找人和找路。句末的 something flashed 没有说是谁，画面停在一个还没看清的东西上。
- **原文**：原文 L54-L54
- **结论**：引语 3 句 50 词（原文 L54）：中文理解逐句对得上，主语=西德妮、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L42）
- **档**：相符
