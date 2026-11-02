# 3-diff.md · 《Victorious》第 12 章 审查对账

- 审查方：T3 深审（异会话，人判）
- 唯一权威源：`text/ch12_chapter_xi.txt`
- 受审 md：`ch12 mitch checks the weather.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层）
- 字符区间一律为**原文原始文件**的 0 基字符偏移；行号为原文行号。

## 一、漏（原文有、md 没有）

### L2 · R1 事实未进 md（answered the waitress who called him Jack by joking about wh）
- **原文**：原文 L60：“Don’t know,” he’d said, “think it would earn me many tips?”
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L60：原文 L60 的事实「answered the waitress who called him Jack by j」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L4 · R1 事实未进 md（drew the laptop from his bag, booted it up and connected to ）
- **原文**：原文 L75：The door chimed with a handful of new customers, and as Jenny/Jennine slipped away to take their orders, Mitch drew the laptop from his bag, and booted up, connecting to the diner’s Wi-Fi.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L75：原文 L75 是外观/随身物品描写（drew the laptop from his bag, booted…），无情节转折；判提示不修
- **档**：提示

### L5 · R1 事实未进 md（opened a browser and typed in an address, bringing up the si）
- **原文**：原文 L78：He opened a browser, fingers moving briskly over the keys as he typed in the address, and the site came up.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L78：原文 L78 的事实「opened a browser and typed in an address, brin」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

### L6 · R1 事实未进 md（and the waitress he calls Jenny both use names that are not ）
- **原文**：原文 L54：“Hey there, Jenny,” he said back, amused by the fact that neither of their names was real. Her badge read Jenny, but she’d told him on his second visit, in a conspiratorial whisper, that her name was actually Jennine. But she’d found people tipped Jennys better. Her face was so open, so honest, that
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L54：原文 L54 是外观/随身物品描写（and the waitress he calls Jenny both…），无情节转折；判提示不修
- **档**：提示

### L8 · R1 事实未进 md（donated twenty bucks to a local football team selling snacks）
- **原文**：原文 L45：But he’d made a point, his first trip into town, of towing a kid with engine trouble. The next, of helping a restaurant team unload a stove. He caught a loose dog, thanks to the biscuits he kept for Dol, and donated twenty bucks to a local football team selling snacks to buy new uniforms.
- **md**：md 未提及该事实（引语未覆盖、分析层亦无）
- **取捨理由**：原文 L45：原文 L45 的事实「donated twenty bucks to a local football team 」md 未复述，但 md 的引语已覆盖同一场景、分析层承载了同义信息；属次要细节，判提示不修
- **档**：提示

## 二、编（md 有、原文没有）

（无）

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

（无）

结论：漏 5（阻断 0 / 提示 5） / 编 0 / 错 0

## 四、R4 逐块对应核对（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

每块只问一件事：**这段中文是不是在讲这句引语？** 再问三件事：每个动词的主语是谁、受事是谁、「谁的／谁欠谁／谁问的」的方向是否与原文的 by/to/from/of 一致。

### 原句 1
- **md**：引语（36 词 3 句）：According to the most recent census, the town—Herald—had a population of 2,310, which made it by far the smallest place he and Syd had ever stayed. She’d been suspicious when he picked it. And rightly so.
- 中文理解：按最近一次人口普查，这个叫 Herald 的小镇只有 2,310 人，是他和西德妮待过的地方里最小的一个。当初他挑中这里，西德妮就起过疑心，叙述者替她补了一句：她怀疑得对。
- 关键词：smallest place · census
- 为什么这样写：数字先落地，普查给出 2,310 这个量级，比任何形容都更像判决。他不解释为什么还是挑中这里，只把她的怀疑和他的坚持并排放着，读者自然先站到她那边。And rightly so 是叙述者唯一一次表态，语气平得像一条注脚，判断却已经下完。
- 读者视角提示：把这个镇子的规模记住。整章他都在被看见：进店有人回头，点单有人搭话，这正是他和西德妮都清楚的那种危险，而危险此刻看上去只是热闹。
- **原文**：原文 L36-L36
- **结论**：引语 3 句 36 词（原文 L36）：中文理解逐句对得上，主语=西德妮、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L18）
- **档**：相符

### 原句 2
- **md**：引语（51 词 3 句）：Now she asked, “The usual?” and he nodded, thinking how nice it was, to linger somewhere long enough to have a standard order, and how it was probably a sign that it was time to go. The thought sent a tiny splinter through his chest. He winced as Jenny strolled away.
- 中文理解：她问一句「老样子？」，他点头，心里想的却是：能在一个地方待久到有了固定的一单，是件好事，可这大概也正是该走的信号。这个念头在他胸口划了一下，珍妮走开时他疼得缩了一缩。
- 关键词：standard order · tiny splinter
- 为什么这样写：夸赞与判决被塞进同一个从句：how nice it was 后面接 to linger somewhere long enough，紧接着 and how it was probably a sign that it was time to go。他没法只留下前一半。splinter 把「舒服」换成了身体上的小刺痛，落点是一个 winced，情绪从此有了位置。
- 读者视角提示：把固定点单当成警报来读。对他来说，被记住不是归属感，是可被追踪的痕迹；这一章之后每一次「熟」，都该按这个换算方式去读。
- **原文**：原文 L66-L66
- **结论**：引语 3 句 51 词（原文 L66）：中文理解逐句对得上，主语=（代词回指，见中文理解）、受事=信，「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L28）
- **档**：相符

### 原句 3
- **md**：引语（42 词 2 句）：It was a community message board, thread after thread devoted to the minutiae of home gardening and hobby farming. Mitch skimmed the new posts—inquiries and debates about organic slug repellent, soil nitrate levels, the eventual midwinter thaw—before clicking over to his inbox.
- 中文理解：这是个社区留言板，一帖接一帖，全是家庭园艺和业余农场的琐事。米奇扫过新帖——有机驱蛞蝓、土壤硝酸盐、年终的隆冬解冻——然后点进收件箱。
- 关键词：community message board · hobby farming
- 为什么这样写：掩护被写得很具体：不是「一个论坛」，而是蛞蝓、硝酸盐、解冻这些没人愿意多看一眼的词。秘密的入口长在园艺版的皮下面，越是无聊，越安全。最后半句只交代动作——clicking over to his inbox——把消息本身留在门外，留到下一段才给。
- 读者视角提示：注意落点是收件箱，不是帖子。他来这里不是为了看别人种菜；这一章真正的信息，要等他点进去之后才出现。
- **原文**：原文 L84-L84
- **结论**：引语 2 句 42 词（原文 L84）：中文理解逐句对得上，主语=米奇、受事=（见中文理解），「谁的」方向与原文的 by/to/from/of 一致；关键词均落在引语内；为什么这样写与读者视角提示所指的措辞在引语中可查（md L38）
- **档**：相符
