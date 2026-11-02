# 3-diff.md · 《Victorious》第 77 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch77_chapter_vii.txt`
- 受审 md：`ch77 mitch watches from the roller coaster.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L1 · R1 事实未进 md（told Victor to take the path to the place it splits and go r）
- **原文**：原文 L54：He swallowed. “Not yet,” he said, panning from Victor’s position to a facade near the center of the park. A massive sign built into the front read MADMAN’S MANSION, the letters jagged, painted red. “But I can see the ride. You’re heading in the right direction. Just take the path to the place it spl
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L54：原文 L54 的事实「told Victor to take the path to the place it s」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L2 · R1 事实未进 md（found Victor no longer heading for the ride but sitting on a）
- **原文**：原文 L69：There. Mitch found him, no longer heading for the ride, but sitting on a bench in an open square, exposed.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L69：原文 L69 的事实「found Victor no longer heading for the ride bu」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 2（阻断 0 / 提示 2） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（48 词 2 句）：Victor might have taken away the pain in his side, but his palms were still sweating as he scaled the outside of the roller coaster. He reached the top and braced himself against the rail, clutching the metal for dear life as he turned to survey the park.
- 中文理解：维克多也许把他肋侧的疼痛拿走了，可他攀着过山车外侧往上爬的时候，掌心还在出汗。爬到顶上，他抵住栏杆，为了保命似的抓着那根金属，才转过身去看园子。
- 关键词：taken away the pain · braced himself
- 为什么这样写：这一段先把身体交出来：出汗的掌心、抓着金属的手，然后才给一个转身，园子到这一下才出现。前半句还塞进另一件事——疼痛可以被人拿走，怕高拿不走。句子里两个 his 挨得很近，爬上去的是谁，要靠 palms 与 braced 这两个动作才分得清。
- 读者视角提示：读者拿到的第一个信息是位置：他在高处，而且是爬上来的。为什么非上去不可，这一段没写；只写了他到顶之后先抓稳，才敢看。
- **原文**：原文 L21-L21
- **结论**：引语 2 句 48 词（原文 L21）：中文理解逐句对得上，主语=维克多、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（50 词 2 句）：He’d never really had a temper—he couldn’t afford one, looking the way he did—but he did have an aunt who told him once that some people came out of the tap already bubbling, while others had to boil. But given time, all of them could get hot enough to burn.
- 中文理解：他说自己其实从来没有脾气——以他这副样子，也养不起脾气——但他有一位姨母，曾告诉他，有些人生来就像水龙头一开就滚，有些人得慢慢烧；可只要给够时间，所有的人都能热到烫伤人。
- 关键词：had a temper · get hot enough
- 为什么这样写：整段自述被塞进破折号里：先否认有脾气，再解释为什么养不起（looking the way he did），然后才把姨母的话端出来。水龙头和炉子都是家常的东西，烧到最后却一样烫；句子用两个 But 把话往同一个方向推，先否认，再补一句更狠的。
- 读者视角提示：读者在这里听到的是一个人的自我说明，而不是他的行为。最后那句里的 them 指谁，句子没有点名；只留下一个「给够时间都会烧起来」的说法，和一处没有说出口的对象。
- **原文**：原文 L48-L48
- **结论**：引语 2 句 50 词（原文 L48）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L25）
- **档**：相符

### 原句 3
- **md**：引语（61 词 3 句）：Mitch’s gaze slid back to the house. He couldn’t tell if it was built to look like it was falling down, or simply was. There were no windows, but he still searched, desperate for some sign of the kid, some proof she was alive, and safe, though every passing second as the cold air cleared his head, it filled with questions.
- 中文理解：米奇的视线又滑回那座房子。他分不清它是照着倒塌的样子盖的，还是本来就快塌了。房子没有窗，他还是在找，急着要看见那孩子的一点迹象，要一点她活着、也还安全的凭据；可冷空气把脑子吹清一分，塞进来的问题就多一分。
- 关键词：no windows · filled with questions
- 为什么这样写：房子先被写得半真半假——照着塌的样子盖，还是本来就在塌——接着窗子被抽掉。没有窗，视线就没有落点，句子却仍旧让他 search；desperate 和 some proof 把这股劲顶住，最后用一个 though 把整段翻过来：越清醒，问题越多。
- 读者视角提示：读者被按在一扇并不存在的窗前。原文没让他看见任何东西，只把「没有窗」和「他还在找」并排放在一起。
- **原文**：原文 L57-L57
- **结论**：引语 3 句 61 词（原文 L57）：中文理解逐句对得上，主语=米奇、受事=线，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L32）
- **档**：相符

### 原句 4
- **md**：引语（30 词 3 句）：A third black van. Mitch spun toward it, boot slipping on the metal grid. He gasped, grasping for balance, heart jackhammering inside his chest as he stopped himself from falling.
- 中文理解：又一辆黑的厢车，这是第三辆。米奇朝它转过去，靴底在金属格栅上打滑。他吸了口气，伸手去抓平衡，心在胸口里像风钻一样砸，才把自己从摔下去那一下收住。
- 关键词：third black van · grasping for balance
- 为什么这样写：三十个词里重心换了三次：先给车，再给他的靴子，最后给心跳。A third black van 单独成句，长度被压到最短；打滑与抓住两个动作都不带解释，末尾才用心跳把刚才那一下补上。
- 读者视角提示：读者拿到的是一个差点脱手的瞬间，以及「第三辆」这个数。车从哪里来、里面坐着谁，这一段没有写；他抓回来那一下，也没有别人看见。
- **原文**：原文 L84-L84
- **结论**：引语 3 句 30 词（原文 L84）：中文理解逐句对得上，主语=米奇、受事=手，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L39）
- **档**：相符

### 原句 5
- **md**：引语（45 词 2 句）：Mitch swung his attention back toward Victor in time to see him stand, and start to walk again, cutting toward a roller coaster on the far side of the park. “You’re going the wrong way,” said Mitch as the agents poured through the second gate.
- 中文理解：米奇把注意力转回维克多身上，正好看见他站起来，又开始走，斜插向园子另一头的一座过山车。「你走错方向了，」米奇说，那些探员正从第二道门涌进来。
- 关键词：the wrong way · poured through
- 为什么这样写：一句里有两个方向：维克多往一边走，探员从另一道门往这边来，米奇的判断夹在中间。对白很短，只有 the wrong way 几个词，说的时候人已经在动；后半句用 as 把两件事按在同一秒上，谁也没等谁。
- 读者视角提示：读者和米奇站在同一个位置上：看见人往错的方向走，同时看见另一批人进门。维克多为什么改道，这一段没给理由；米奇那句话有没有传到他耳里，也没有写。
- **原文**：原文 L93-L93
- **结论**：引语 2 句 45 词（原文 L93）：中文理解逐句对得上，主语=维克多、受事=门，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L46）
- **档**：相符

### 原句 6
- **md**：引语（30 词 3 句）：The way the axe rang through his palms. The smell of chimney smoke. Sydney curled on the sofa while he made dinner, Dol beside her, head resting on her feet.
- 中文理解：斧头震过掌心的那一下，烟囱的味道，还有西德妮蜷在沙发上，他在灶前做饭，Dol 挨着她，头搁在她脚上。
- 关键词：the axe rang · chimney smoke
- 为什么这样写：三句都没有主语，也没有「他想起」这样的提示，斧、烟、沙发一样一样摆出来，最后落在狗把头搁在她脚上这个细节。句子短到接近清单，声音、气味和一只手的重量都留在里面。
- 读者视角提示：西德妮在这一章里只有这一处具体的模样，而且是在别人的记忆里。原文没有写她此刻在哪里，也没有写这段是多长时间以前的事。
- **原文**：原文 L105-L105
- **结论**：引语 3 句 30 词（原文 L105）：中文理解逐句对得上，主语=西德妮、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L53）
- **档**：相符
