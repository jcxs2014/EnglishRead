# 4-verdict.md · ch28「28. The Police Station」审查判定

> 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch28 leigh cannot place scott.md`
> 唯一权威源：`text/ch28_28.txt`（252 行 / 9536 字符）
> 落盘：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch28/`
> 覆盖率声明：**本次只审 ch28**。本书其余 53 章**只有机器层**（`chapter.sh` 逐章），**不得据此推断为「通过」**；
> 未跑人判的章在全书报告中必须标「只有机器层」。ch28 已完成 R1–R5 全流程。

---

## 一、四组数（唯一汇报口径）

| 组 | 口径 | 结果 | 阻断 | 提示 | 假红 | 跳过 |
|---|---|---|---|---|---|---|
| **逐字** | 8 条引语 + 26 条例句是否原文逐字 | **8/8 引语精确命中原文**（独立 Python 子串比对，不依赖工具口径）；**26/26 词汇例句精确命中**；引语落点偏移 2867/3060/3297/3466/3853/5900/8109/9306 | **0** | 0 | 0 | 0 |
| **对应** | 每块中文是否在讲这句引语（主语/受事/归属方向） | **8/8 对应成立**；引语选短 0、不对应 0、密度不足 0（每块「为什么这样写」95–117 CJK 字，无一块只复述字面） | **0** | 4（块2/5/6/7 的措辞与归属问题） | 0 | 0 |
| **形态** | H1 / 导航 / 子项集 / 块数 vs 本书众数与 profile | H1 `# 28. The Police Station`＝全书统一形 `# N. <小节名>`（54 章全同）；导航 **5 项**（全书众数 5）；子项集＝`中文理解 / 关键词 / 为什么这样写 / 读者视角提示`，与本书 profile 及众数**完全一致**；块数 **8** vs 全书中位数 **7**、全书区间 **[5,10]** ⇒ **在区间内，无偏离**（故不需写偏离理由） | **0** | 0 | 0 | 0 |
| **断言** | 事实断言 / 归属 / 缺失项 | 已核 md 相关断言与缺失项共 **11 条**（A1–A11）：阻断 **1**、提示 **10**、假红 0、跳过 0；另机器层口径备注 1 条（A12，非 md 缺陷） | **1** | **10** | 0 | 0 |

**四组数一句话**：逐字 8/8、对应 8/8、形态 0 偏离、断言 11 条中 **1 阻断 + 10 提示**。
**阻断型条数：1**。

---

## 二、断言明细表（`断言 | 证据（章:区间）| 结论 | 档位`）

| # | 断言 | 证据（章:区间／md 行） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | 块 2/导航：「bunny boiler（兔子房）」这个词**是从警方的问法里接过去的**／「那是**审讯桌上的词**」／「她**复述别人用词**」 | 原文 `text/ch28_28.txt:105`：**"‘I don’t know.’ She looked at Caius who clicked his pen and put it down with a finality. ‘Is that all you’ve got? He was dating a bunny boiler?’"**（该词出自曼迪自己口中）；她这句话之前警方的唯一问句 `text/ch28_28.txt:108`：**"‘For now. Unless there’s anything else you think is important? A stalker, for example.’"**；md `ch28 leigh cannot place scott.md:14`、`:30`、`:31` | 全书语料中「bunny boiler」**仅此一处出处**，无人对她说过该词、警方也未用过该问法 ⇒ md 凭空给它安了一个来源（归属反转）。**最小改法**：改为「这个词是她自己嘴里蹦出来的俚语」，裂缝点改用 `text/ch28_28.txt:123`「From what you said last night he was murdered by some sort of scheming femme fatale」（此处她确实在复用警方的框架，有原文支撑） | **阻断** |
| A2 | md 导航：「在分部「**A THURSDAY IN MAY**」里」 | 书中分部题名逐字为 **"THURSDAY"**（epub `OPS/s041-Part-007.xhtml` 的 `<h1>` 与 `OPS/TOC.xhtml` "THURSDAY 28"）；含 "A … IN MAY" 的是 Part 1（`OPS/s008-Part-001.xhtml` → "A FRIDAY IN MAY"）；`text/` 语料内无任何分部标题 | 语义可解（周四是五月的某个周四），但**不是书中题名**；全书 6 章统一如此 ⇒ 体例问题，非本章独有 | 提示 |
| A3 | md 导航：「作者**不写推理独白**」 | `text/ch28_28.txt:132`：**"He was equally perplexed by this. It couldn’t have just been that Scott was willing to go to the Post Office for her, could it?"**（侦探推理）；`text/ch28_28.txt:135`："she felt like she had no choice but to cradle a little hope in her heart"（进人物内心） | 断语偏绝对：原文确有一次推理与一处内心 | 提示 |
| A4 | 漏：警务室开头整段（5K 的 PB、艾米摇戒指／马特口型「还没有」、油漆与 Letterboxd）未入「精读」 | `text/ch28_28.txt:65`、`:68`、`:53` | md 已在导航声明取舍（`md:13`、`:15`），不作阻断；补半句即可 | 提示 |
| A5 | 漏：Jodie 的证词在「精读」层无任何引语块（四位被询人只讲了三个） | `text/ch28_28.txt:212`：**"I don’t know, to be honest. It didn’t bother me but I don’t think he liked me much on a personal level. He never engaged me in small talk. I was just his boss. I was a pay cheque, that’s it."** | 导航层已含她（`md:13`「老板娘只当他是工钱」），不作阻断；但她是唯一明确回答「不知道他有没有女朋友」的人，与莉的 "I’m sorry, I really don’t know" 互为支点 | 提示 |
| A6 | 漏：Angus 认 Digby 照片这一条跨案线索全无 | `text/ch28_28.txt:187-190`：**"‘Have you ever met this man?’ Matt showed him Digby’s picture."** / **"‘He looks sort of familiar. Does he live nearby or something?’"** | md 全文无 Digby／迪吉；属线索级遗漏，非情节转折，不作阻断 | 提示 |
| A7 | 漏：蔡厄斯走出问询后的推理与「邮局」线索未入 md | `text/ch28_28.txt:132-135` | 本章专属判据（母亲**完全不提的那部分生活**）最硬的材料恰恰是「她从头到尾没提过信件／邮局」，md 未取用；不作阻断 | 提示 |
| A8 | 块 5：「钱、名声、好处，这些东西**在关于儿子的叙述里从未出现过**」 | `text/ch28_28.txt:129`：**"I loved Scott. He was everything to me but he was a normal kid. He wasn’t rich or famous. What could she have got out of him?"** | 同一块引语里就出现钱与名声（否定式），句自相矛盾；应改为「她能想到的动机只有钱和名声」 | 提示 |
| A9 | 块 5：「她连"她"是谁都没追问，**只问**"她能得什么"」 | `text/ch28_28.txt:123`：**"…From what you said last night he was murdered by some sort of scheming femme fatale. **Why was she interested in him?**"** | 她问了**两句**动机类问题，「只」字不成立 | 提示 |
| A10 | 块 6：「他却在**对方开口前**把耳机塞了进去」 | `text/ch28_28.txt:178`：**"He tried to tell me the details of how she was stringing him along but I put my headphones in before he could really start."** | 「he could really start」的 he=斯科特；md 的「对方」默认指向那个女孩，反而把本块自己的主题句（不是儿子不肯讲，是听的人没听）弄模糊 | 提示 |
| A11 | 块 7：「**他说**喜欢漂亮但自尊心低的女孩」 | `text/ch28_28.txt:234`：**"He liked pretty ones with low self-esteem."**（仍是莉的转述，原文无斯科特直接引语） | 转述被写成直接引语，易被读成斯科特亲口 | 提示 |
| A12 | 机器层口径备注（非 md 缺陷）：`2-machine.json` 的 `pos` 字段与裸文件偏移对不上 | 例：块 1 记 `pos=2720`，实际裸文件偏移 2867 | 推测按「空行已折叠」的语料计算；`ok` 判定本身正确。第三方按 `pos` 回原文会错位 ⇒ **记给工具维护者**，不改 md | 提示（工具） |

---

## 三、R5-补 · 零命中断言的自证（命令 + 输出 + 退出码）

```
/usr/bin/grep -rniE "bunny boiler" text/*.txt
→ 命中 1 行：text/ch28_28.txt:105:‘I don’t know.’ She looked at Caius who clicked his pen and put it down with a finality. ‘Is that all you’ve got? He was dating a bunny boiler?’
→ 退出码 0

/usr/bin/grep -rniE "thursday in may" text/
→ 0 命中；退出码 1（text/ 语料内无分部标题，非「查无该分部」的结论：分部题名已改从 epub 结构取证）
```
（取证用显式路径 + `/usr/bin/grep`，未用 `git grep`／rg 默认 ignore 规则；`text/` 被 `.gitignore` 排除，`git grep` 的退出码 1 与「真查无」不可区分。）

---

## 四、已核实为正确（防误修，固定一节）

以下条目**读着像错，回原文核对后成立**，后续任何人不得以「读着不对」为由改动，除非能给出反证。

1. **「Leigh」是收银员、母亲叫「Mandy」**——`text/ch28_28.txt:78`：**"‘Again, I’m so sorry for your loss,’ Caius said to Scott’s mother Mandy."**；`text/ch28_28.txt:222`：**"‘Scott was a twat,’ Leigh, the cashier at the bakery, said."**
   md `md:11`/`:120` 分得完全正确（母亲曼迪／收银员莉）。⚠ **任务书里「Scott 的母亲 Leigh」的说法与原文不符**：原文中母亲是 **Mandy**，Leigh 是面包店收银员——
   这是任务书的表述问题，**不是 md 的缺陷**。另注：md 文件名 `ch28 leigh cannot place scott` 属写作方自拟 keyplot（书中本章题名为「28」+「The Police Station」），按命名约定不算错。
2. **块 2 的引语本身逐字正确**——`text/ch28_28.txt:105` 逐字命中；**错的只是引语来源的解释**（A1），**不是引语**。修的时候不要动引语。
3. **H1 `# 28. The Police Station` 正确**——epub `OPS/s042-Chapter-028.xhtml` 的 `<h1>28</h1>` + `<h2>The Police Station</h2>`；本书 54 章 md 的 H1 统一为 `# N. <小节名>`。
4. **「她给不出工作内容、作息、同事，也说不出他下班后去了哪里」成立**——`text/ch28_28.txt:111` 全章关于母亲口中儿子生活的**全部**描述只有 "He worked in a bakery, for God’s sake." 一句。
5. **「NW1 满街都是金发」成立**——`text/ch28_28.txt:249` 问句 "Any blondes?" 紧接 `:252` **"‘It’s NW1. You can’t throw a three-day-old cronut without hitting one, natural or not.’"**，玩笑指向即金发者。
6. **「他做咖啡、她管收银台与面包」方向正确**——`text/ch28_28.txt:246`：**"‘No, he did the coffee and I did the tills and the bread. …’"**（主语 Scott=他，Leigh=她）。
7. **「是审讯桌上的词」之外的框架论有原文支撑处**——`text/ch28_28.txt:123`：**"From what you said last night he was murdered by some sort of scheming femme fatale."**（她确实在复用警方的说法）；A1 要改的是**「bunny boiler 这个词」的来源**，不是这一层意思。
8. **语料无误**——把 `text/ch28_28.txt` 逐行回查 epub `OPS/s042-Chapter-028.xhtml`，唯一一处对不上的是 `text/ch28_28.txt:135`，原因是 epub 该处夹了页码 **"178cradle a little hope"**，提取时已清页码 ⇒ 提取件正确（此条为**假红类工具现象**，非 md 缺陷）。
9. **词汇表 26 条例句全部逐字出自本章**（29 行表格含 3 行表头）。

---

## 五、结论

- **四组数**：逐字 **8/8**（另 26/26 词汇例句）｜对应 **8/8**（选短 0 / 不对应 0 / 密度不足 0）｜形态 **0 偏离**（H1 合形、导航 5 项、子项集与 profile 一致、块数 8 ∈ 全书区间 [5,10]，中位数 7）｜断言 **11 条：1 阻断 + 10 提示**（另机器层口径备注 1 条）。
- **阻断型条数：1**。
- **最要紧的一条（A1）**：md 三处（`md:14` 导航人物弧线、`md:30` 块 2「为什么这样写」、`md:31` 块 2「读者视角提示」）断言「bunny boiler（兔子房）」这个词是**曼迪从警方的问法里接过来的**、是**审讯桌上的词**、是她**复述别人用词**；
  而原文 `text/ch28_28.txt:105` 显示这个词**由她自己说出**，她之前听到的警方问句是 `text/ch28_28.txt:108` 的「A stalker, for example」，全书语料中「bunny boiler」**仅此一处出处**（`/usr/bin/grep -rniE "bunny boiler" text/*.txt` → 命中 1，退出码 0）。
  这正是「施事/归属反转」类——句子通顺、引语逐字、机器四探针全绿，错的只是「这个词是谁的」。
  建议改法：把来源改为她自己说出口的俚语，把「她用侦探的框架谈自己的儿子」这层意思挂到 `text/ch28_28.txt:123`（那里有原文支撑）。
- **次要紧**：本章专属判据只完成了「答得快」「绕开」两层，「**完全不提的那部分生活**」最硬的一条（母亲从不提邮局／信件；作者却让蔡厄斯在此想到 Post Office，`text/ch28_28.txt:132`）没被取用（A7）；另四位被询人中 Jodie 在「精读」层缺席（A5）。
