# ch08 · R3 对账（三张单子）

> 依据：`1-suread.json`（先素读，314 行全读，43 事件 / 11 关系 / 7 数字 / 7 未决 / 10 陷阱）与 `2-machine.json`（rc=0 / verdict ok / blocks=8 / words=2696 / block_target=[5,8]）。
> 机器层：`segment_miss=0`（引语逐字）、`quote_long=0`、`keyword_bad=0`、`struct_bad=0`、`cjk_low=0`、`block_count=0`、`template=0`、`keyword_long=0`、`hole=0`。
> 补验（机器盲区）：R0 全书级 `verify_fragments_indep.py` 312 片段 / 0 MISS（本章 8 条引语均无 `…`，逐条 `segment_miss=0`）；本章 22 行词表例句 **22/22 逐字回源命中**（`/tmp/vocab_check_hx.py`）、**22/22 词头落在例句内**（`/tmp/vocab_head_hx.py`）。

---

## 一、漏（素读有、md 无）

| # | 素读事实（text 行号 + 逐字） | md 状态 | 判定 |
|---|---|---|---|
| L1 | `:77` `Cynthia’s relationship with the Marquess of Kentmore was something else entirely.`；`:200` `But she was a debutante whose father had arranged a marriage with a powerful marquess.`；`:257` `Not the marchioness.` —— 辛西娅＝肯特摩尔侯爵夫人（她自己婚姻的封号出处） | md **全篇未出现「肯特摩尔」「侯爵夫人」「marchioness」**；原句 4·中文理解只写「对上流社会的任何一位体面太太」 | **不构成阻断**（覆盖取舍；md 谈的是婚姻关系本身，不涉封号）。**建议**：导航·人物弧线或原句 8 补半句「侯爵夫人／marchioness」，否则原句 8「不是侯爵夫人，是她自己」这句反转在 md 里没有落点 |
| L2 | `:62` `‘A very dangerous man. He’s killed more people than the plague. What was Hubert thinking?’` —— 警司对辛克莱的**定性**（杀人比瘟疫多） | md 原句 3 的引语止于 `half the women as well.`，**警司紧接着的这句定性未进 md**；原句 3·为什么这样写「读者听到的是怒气与名声，而不是证据」里的「名声」二字其实指向的就是它 | **不构成阻断**（引语选段取舍）。**建议**：原句 3·读者视角提示补一句「警司随后补『杀的人比瘟疫还多』，那仍是名声不是证据」 |
| L3 | `:209` `‘Yer brother will have a fit when he finds out abou’ this. If Lord Burrows’ weren’t already dead, Thomas would kill ’im for exposing you to such danger.’`；`:212` `‘I would prefer he didn’t know all the details.’` —— **哥哥托马斯这条线**（警司会告诉哥哥／哥哥会杀人／她只求哥哥别知道细节） | md **分析层完全未提托马斯**；仅词表 `appalled` 一行的例句里出现过 `Thomas`（`:77`）；导航·Tropes 只写「她最怕被人怜悯」 | **不构成阻断**（覆盖取舍）。**建议**：原句 8 前的「她最不想被看轻的人」可与「哥哥」这一层并置，是本章「体面」的另一半压力源 |
| L4 | `:44` `The Devil of Seven Dials. DOSD.` —— DOSD 这个字母组合首次在本章出现（ch07 已铺） | md 全篇未提 DOSD | **不构成阻断**（跨章术语，ch07 已按「反复出现的字母组合」处理，**本章不得改**） |
| L5 | `:103`／`:107` `‘He spent more time at his club than here. There are weeks strung together where I didn’t see him at all.’` —— 她对丈夫行踪的交代（俱乐部、几周不见） | md 未提 | **不构成阻断**（覆盖取舍） |
| L6 | `:47` `‘Devil. That’s what the intruder thought before he jumped out of the window.’` —— 海伦娜明确说「魔鬼」是闯入者**跳窗前**心里想的 | md 原句 2·中文理解写「他逃走之前想的是，『魔鬼』一定会因为他失手而杀了他」——**已覆盖**；原句 2·为什么这样写说「交代了『魔鬼』这个名字的来源」：**成立** | 已覆盖，不计漏 |

## 二、编（md 有、原文无）

**0 条。** 逐块核过导航 5 项、原句 1–8 的中文理解／关键词／为什么这样写／读者视角提示、词表 22 行、一句话总结，未发现凭空出现的情节、关系、数字或人物。

已重点排查并**排除**的三处疑点：

- **「辛克莱」是否另有其人、是否确为凶手**：`:41` `‘The Devil of Seven Dials. Damien Sinclair.’ He spat the words like poison.`、`:56` `‘The bastard. It has to be Sinclair. He has every man in the Seven Dials working for him, and half the women as well.’` ⇒ md 把「魔鬼」落到辛克莱身上：**成立**。
- **「海伦娜读不到辛西娅」是叙述事实还是辛西娅的判断**：`:311` `Helena might be here to detect Cynthia’s hidden thoughts, but she was the witch with a secret. Perhaps she could read other people’s minds, but she couldn’t detect a thing going on in Cynthia’s head.` —— 该段与 `:314` `Damnation. The fox is right.` 同为**无引号的辛西娅内心独白**（非叙述者陈述）。md 原句 8·为什么这样写「叙述用的是辛西娅的判断语气，读起来像她自己在心里下的结论，而不是叙述者给出的真相」：**成立**（md 未把它当成叙述者认证的客观事实）。
- **「肯特摩尔侯爵」是否与休伯特是两人**：`:77` `Cynthia’s relationship with the Marquess of Kentmore was something else entirely.` —— 该句主语为 Cynthia 的婚姻对象，即**休伯特本人**（ch02:44 `the marquess… Lord Hubert Burrows` 互证）⇒ **不是**另一人，md 未提及亦无冲突。

## 三、错（两边都有但不一致）

| # | md 位置 | md 写法 | 原文（text 行号 + 逐字） | 判定 |
|---|---|---|---|---|
| E1 | 原句 2·读者视角提示 | 「读者得到一条规则：情绪越强，念头越容易被听见。**读心因此要看对方情绪，情绪越强越容易**；这条规则也让『魔鬼』从一个称呼变成一个人人害怕的名字。」 | `:53` `‘He was frightened. Strong emotions can make it easier. “The Devil’s going to kill me for sure if I fail.” That’s what he thought before he escaped.’` —— 前后两个分句**说的是同一件事**（后半句是前半句的换词重述），构成同义反复 | **提示**（措辞级：读者视角提示里同一命题连说两遍，信息量折半） |
| E2 | 导航·一句话概括 | 「认定七晷区**的人都替他办事**」 | `:56` `‘It has to be Sinclair. He has every man in the Seven Dials working for him, and half the women as well.’` —— **每个男人**替他办事，**一半的女人**才替他办事 | **提示**（措辞级：「都」把「一半女人」也括进去，属概括过头；md 同章原句 3·中文理解写的是「每个男人都替他做事，连一半女人也听他差遣」，比导航准确 ⇒ md 内部不一致） |

## 四、R4 逐块对应（三问）

| 原句 | 中文理解对应 | ①动词主语 | ②受事/宾语 | ③归属方向 | 结论 |
|---|---|---|---|---|---|
| 1 | 压短距离、夺信、扫纸、神情变凶 | 他（麦克杜格尔）压短距离、夺信、扫视 | 那封信、纸面 | 「和气、忠诚的人」变「凶猛可怖」的是**他** | 对应成立 |
| 2 | 耸肩、目光滑开；转述闯入者的临逃念头 | 海伦娜耸肩答话 | 闯入者逃走前想的「魔鬼会杀我」 | 「他逃走之前想的是」＝**闯入者**的念头，非海伦娜的判断 | 对应成立 |
| 3 | 揉头发、骂混蛋、点辛克莱 | 麦克杜格尔揉头发、骂人、断言 | 七晷区的人 | 「他认定」＝警司的判断（非物证） | 对应成立 |
| 4 | 差事＝漂亮／顺从／能生育；末项未达标即被休 | 休伯特定下三项义务 | 辛西娅 | 「被休」＝休伯特的行为；「比死还难受」落在**上流社会太太**身上 | 对应成立 |
| 5 | 先谢、再否认、再承认、再自我否定 | 辛西娅（对狐狸）道谢又改口 | 狐狸的话、「怜悯」 | 「我不是在向一只狐狸道谢」＝**她**对狐狸说 | 对应成立 |
| 6 | 先摆对自己有利的、再补不利的、最后落到证据 | 辛西娅对警司陈述 | 自己的动机、信、「魔鬼」 | 「不能给这个『魔鬼』定罪」＝**她**的主张 | 对应成立 |
| 7 | 抓人 vs 定罪被拆开；押注在「他知道是谁」 | 麦克杜格尔说抓人、关押、审问 | 辛克莱这个人 | 「他也许没杀你丈夫，但……他知道是谁下的手」＝**警司的赌注** | 对应成立 |
| 8 | 位置对调：查秘密的人自己才是有秘密的人 | 辛西娅在心里判断 | 海伦娜的能力 | 「读不到辛西娅脑子里」＝**辛西娅的判断**，非叙述者结论 | 对应成立 |

**R4 无阻断。** 未发现「分析讲的是引语之外的上下文」「讲全书主旨」「只复述字面」三类失配。

## 五、形态

`H1 = 08. Chapter Eight`（形状合规）；导航 5 项；子项 4 项（中文理解／关键词／为什么这样写／读者视角提示）＝本书众数；块数 **8**，落在本书区间 [6,13] 与本章 `block_target=[5,8]` 内（**已触上限**：若因修复增块，会触发 `block_count`）。

## 六、语料层观察（非 md 缺陷，不计入三张单子）

`:170` `Still in the reading mood?` 与 `:173` `You can find more novels waiting at Lokepub.` —— **站点宣传行混入提取件**，落点在狐狸对话中间（`:164` `Cynthia shook her head.` 与 `:179` `Of course he’s silent. …` 之间）。两行为**插入**而非顶替：紧邻的正文段落完整，且本章 8 条引语无一跨过这两行（`segment_miss=0`），**md 不受影响、不需改稿**。

同类注入另见 **ch03:188 / ch13:185 / ch19:197 / ch25:214**，合计 **5 章 6 行**（本章占 2 行，其余各 1 行）。登记备查（提词方／出版方在 epub 里塞的引流文案，非 McGuire 正文），进汇总节。
