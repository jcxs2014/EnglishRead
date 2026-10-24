# ch22 深审 R3 三张单子（漏 / 编 / 错）

> 章：`text/ch22_chapter_22.txt` ↔ `ch22 the dowagers refusal.md`
> 流程：R1 素读（`1-suread.json`，203 条证据片段全部为原文子串，`BAD=0`）→ R2 机器 → R3 本文件 → R4 逐块对应（§四）→ R5 判定（见 `4-verdict.md`）

---

## 〇、结构底账

| # | 事实 | 证据（`text/ch22_chapter_22.txt`） |
|---|---|---|
| 1 | 正文体范围 `:35`–`:288`（`:288` `You create a new life in the Cotswolds.` 为最后一句） | `:35` `Cynthia’s world, moments ago a spinning, glittering dream…` |
| 2 | **单一视角＝辛西娅**全章到底，换场只换地点不换 POV | 通读 `:35`–`:288`；`:129` 起场景二仍贴辛西娅 |
| 3 | 换场空白带 `:114`–`:128`（15 行空白），场一 `:35`–`:113`、场二 `:129`–`:288` | 逐行核 |
| 4 | 推广／版权残留行 0 条 | `grep -ci lokepub` → `0`（本章 §六 A） |
| 5 | 场一地点＝**辛西娅的房间**（布莱尔宅）：她在此穿衣、拿外套、出门 | `:68` `she hastily slipped on her corset` → `:98` `Snatching her bodice and outer skirt from the chair where she had so carefully placed them the night before` → `:113` `Pushing open the door, Cynthia stepped out of the room`；承接 ch21 `:80` `Cynthia was tangled in her sheets.`（海伦娜是**走进她的房**） |
| 6 | 场二地点＝**辛西娅自己的家**（她已"逃离布莱尔宅"） | `:249` `Cynthia’s yearning for Helena had only increased since she fled Blair House` |
| 7 | 守丧刻度：按礼至少两年，实际丈夫死后**才一个月** | `:207` `By rights, I should remain in mourning for at least two years, and it’s barely been a month.` |
| 8 | 婚龄十年 | `:231` `Hubert doesn’t deserve two more years of my life. He’s already had ten.` |
| 9 | 书内**未给舞会日期**（无 tomorrow / 星期 / 具体日） | §六 B：`grep -niE "tomorrow|…|sunday"` → **无命中，rc=1** |
| 10 | 魔宠心语＝**不加引号裸行**，共 5 处，且以辛西娅的答话反向锁定说话人 | `:56` `Your souls are intertwined…` → `:59` 辛西娅答 `'I can’t stay, Hamlet.'`；`:62` `She wants you…`；`:71` `If Ophelia was scared, I would stay.` → `:74` 辛西娅问 `'For how long?…'`；`:77` `As long as she needed.` → `:80` 辛西娅答 `'Then I suppose a fox and a ferret…'`；`:83` `I always make sense.` |
| 11 | 辛西娅**直接心语**＝不加引号：`:47` 三句连写；**章末 `:285`–`:288` 也是不加引号的两行问答** | `:47` `I’ve fallen in love.…I’m such a fool!`；`:285` `What happens when your soulmate rejects you?`／`:288` `You create a new life in the Cotswolds.` |
| 12 | 引号体系：台词用单弯 `'…'`；爵夫人原话用双弯 `"divine retribution"` | `:225` |
| 13 | `:240` 身份宣言的实际收尾句被 md 引语截断 | `:240` `…subject to the whims of others. Whatever choices she made moving forward would be hers alone. It was time to take control of her life, even if that meant sacrificing her heart to reclaim her soul.` |
| 14 | ch22 之后**确实有**海伦娜力量失控（md:34 的"埋线"可核） | `text/ch23:65` `Her magic had been malfunctioning since Cynthia left.` |
| 15 | 水／海意象**在 ch20 已落到辛西娅身上**（她的梦） | `text/ch20:381` `…it brought with it dreams of swirling waters, sucking her into their depths.` |
| 16 | md：13 块（`md:18/28/38/48/58/68/78/88/98/108/118/128/138`）、词表 24 行 9/9/6、导航 5 项 | `2-machine.json`：`blocks=13`、`block_target=[6,10]`、**`block_hint`＝「块数 13 偏离本章篇幅建议 6–10（本章 3043 词）」**、`segments=13`、`segment_miss=0`、`issues` 全空 |

---

## 一、漏

| # | 原文事实 | md 现状 | 判定 |
|---|---|---|---|
| L1 | `:207` 守丧刻度：`By rights, I should remain in mourning for at least two years, and it’s barely been a month.` ＋ `:231` `He’s already had ten.`（婚龄十年） | md:10／md:191 都只写「去出席舞会」，**未记「应守丧两年／丈夫死了一个月」**；md:191 只收了「十年」 | **阻断（漏）** |
| L2 | `:240` 身份宣言的收尾：`It was time to take control of her life, even if that meant sacrificing her heart to reclaim her soul.` | 引语块 11 停在 `…whims of others.`，分析层也没写这句；md:124 称「三个短句是本章身份宣言的高点」，却缺了高潮里那句代价 | 提示 |
| L3 | `:198` `Hope that she might help women like Lily.` —— 跨章回收 ch16 的 Lily | 无 | 提示 |
| L4 | `:156` `I’m sure your uncle and my brother need no help from me.` —— 「你的叔叔（＝布莱尔姐妹的舅舅拉克兰）与我哥哥（托马斯）」是本案的实际侦查组合 | 无；此句同时为「拉克兰＝母系」提供书内取证（与全书 md「叔叔」待改 12 处同源） | 提示 |
| L5 | `:213` 爵夫人的为人：`No secret was safe with the duchess, nor any man she set her sights on.` | md:191 只写「爵夫人爱看丑闻」，未记这条分寸 | 提示 |
| L6 | `:261` `Or hope Helena might be missing her just a little.` 的第三重念头 | md:10/191 只写「专注魔法成了不想海伦娜的借口」 | 提示（可与 L7 合并，不必单改） |

---

## 二、编

**本节无新增凭空事实**（md 的三处新增内容——房间、舞会日期、dowager house 产权——见 §三 E1/E2/E5，按「新增情境事实」记在错栏，不重复计数）。

**成立取证表（md 事实主张逐条回原文）**

| md 主张 | 原文 |
|---|---|
| 辛西娅追问「怕自己爱上我后会变得冷酷残忍」 | `:38` |
| 海伦娜「眼里闪银、只说'我知道'」 | `:41` |
| 她在这个当口才认清自己已经恋爱 | `:44` `It wasn’t until this moment…that Cynthia realised the truth.`＋`:47` |
| 把心碎压后、先用怒气脱身，说出「那我离开」 | `:50` |
| 哈姆雷特心语：灵魂交织／「她只是害怕」 | `:56`／`:62` |
| 海伦娜沉默＝确认 | `:65` `her silence screamed a confirmation Cynthia could not ignore` |
| 「我会非常想你」是对魔宠说的 | `:59` |
| 拒绝「做朋友」，三句「Not when」：空抱／空厅／寻不到另一半 | `:107`（海伦娜提议）＋`:110` |
| 「再见，海伦娜」＋推门走向独自面对的未来 | `:110`／`:113` |
| 克莱奥「禁止」她逃去乡里 | `:129` |
| 埃莉劝她等几周 | `:141` `Give her a few weeks. She’ll come around.` |
| 寡妇宅改成有需要的女人的家：教育、培训、庇护 | `:183` |
| 名单来自希金斯太太、是休伯特解雇的女佣 | `:177` |
| 「多半被他侵害过」为辛西娅推断 | `:177` `Women he doubtlessly abused.`（原文即推断副词）→ md 用「多半」✔ |
| 克莱奥邀她入会：「不是血脉，而是由魔法结成的姐妹」 | `:168` `Maybe not by blood but bound by magic` |
| 反问：若托马斯拒绝你，你能留下吗（克莱奥答不能） | `:171`／`:174` |
| 「神圣报复」是爵夫人的原话 | `:225` `in her words, "divine retribution"` |
| 力量：一挑眉挪花瓶；几次尝试＋一道闪电后推衣柜三寸 | `:255` |
| 克莱奥判定地巫、与土元素相连（木、陶土、石英、玻璃） | `:258` |
| 专注魔法成了不想海伦娜的借口 | `:261` |
| 想起爱情药水、随即否定（不能夺走自由意志） | `:276`／`:279` |
| 理解海伦娜的恐惧、仍确认罗温是对的 | `:282` |
| 章末两行一问一答 | `:285`／`:288` |
| 「誓」的内容与出处本章未交代 | 全章无说明（`:86` 只有 `my oath`）✔ |
| 「银光第二次出现」＝`:41` 第一次、`:86` 第二次 | `:41` `flashed silver`／`:86` `catching Cynthia in her silver glare` ✔ |
| 「为后面力量失控埋线」 | `text/ch23:65` `Her magic had been malfunctioning since Cynthia left.` ✔ |
| 原句 7 是三个短句（`And don’t twist…`／`You are rejecting me…`／`I never would have guessed…`） | `:95` 引语内恰 3 句 ✔ |
| 原句 11 是三个短句、后两句省略主语 | `:240` `She was a sapphist. A witch. And a powerful woman…` ✔ |

---

## 三、错

| # | md 位置 | md 说法 | 反证 | 判据 | 判定 |
|---|---|---|---|---|---|
| E1 | `md:10` | 「**辛西娅在海伦娜房里**听完那句…」 | 这一夜是**海伦娜走进辛西娅的房间**：ch21 `:65` `'This is ridiculous. I’m going to speak with her.'` → `:77` 推门 → `:80` `Cynthia was tangled in her sheets.`；ch22 `:68` 辛西娅在本房间穿胸衣、`:113` 走出这间房 | 场景归属写反 | **阻断（轻）** |
| E2 | `md:10`＋`md:191` | 「她答应**次日**出席德文郡爵夫人的夏日舞会」 | 全章无任何日期词（§六 B：`tomorrow/morrow/next day/星期` 全部无命中，rc=1）；原文只有 `:198` `invited me to her annual summer ball`＋`:207` 的"舞会临近" | (g) 引语外新增情境事实 | **阻断（轻）** |
| E3 | `md:24` | 「全书水与海的意象**第一次**落到辛西娅身上，而她接下来是被浪打翻的那个人」 | `text/ch20:381` `Sleep was slow in coming, and when it did arrive, it brought with it dreams of swirling waters, sucking her into their depths.`——ch20 章末（辛西娅 POV）水已把她往下吸 | (j) 跨章「第一次」必须全书取证；已证伪 | **阻断（轻）** |
| E4 | `md:30` | 「'咬唇'和'stared resolutely at the window'（**同段稍后**）都是回避动作」 | `stared resolutely at the window` 在 `:86`（**45 行之后、另一段落**：`Hamlet turned his head to Helena, who sat up. She held the sheet against her chest and stared resolutely at the window.`）；原句 2 引语只到 `:41` | 章内相对位置写错（引语内无此句） | **阻断（轻）** |
| E5 | `md:114` | 「寡妇身份（**dowager house 是亡夫留给她的财产**）改成工具」 | 全章只说 `:135` `the dowager house waiting in the Cotswold district`、`:183` `put my dowager house to good use`；**未写产权来源** | (g) 引语外新增情境事实（此处是术语释义被写成剧情事实） | 提示 |
| E6 | `md:44` | 「这是全章**唯一**一段完全不加引号的直接心语」 | 章末 `:285`–`:288` 同样是不加引号的自问自答（`What happens when your soulmate rejects you?` / `You create a new life in the Cotswolds.`） | (i) 唯一性断言有同章反证；两处以「感叹三句」与「两行问答」可区分 ⇒ 只提示 | 提示 |
| E7 | `md:106` | 「本章的转折点全压在这**十四行字**里」 | 该块在 md 占 `md:98`–`md:106` 共 9 行；对应原文 `:98`–`:113` 共 6 个自然段、16 个物理行——**"十四行"两头都对不上** | (f) 行数断言无据 | 提示 |
| E8 | `md:104` | 「作者把 **ch21 开头**海伦娜'推门进去'与这里的'推门出去'配成对称」 | ch21 的推门在 `:77`，位于 `:35`–`:371` 的前段（约 1/8 处），不是开头；ch21 开头是失眠段落（`:35`） | 跨章相对位置不严 | 提示 |
| E9 | `md:116` | 「**同段前一句**她说'这远不够'」 | `though it hardly feels like enough` 在 `:177`，是**上一段**的末句；引语块本身在 `:183` | 相对位置不严（内容归属正确） | 提示 |
| E10 | `md:11` | 「本章紧接 ch21 的拒绝，是**全书情绪最低点**与转段的枢纽」 | `text/ch26:38` `she watched the counterpart of her soul shudder from the impact of Sinclair’s bullet`、`:98` `I can draw out the bullet`、`:203` `And you got shot instead.`——中枪与取弹在情绪量级上更低 | 可核最高级（跨章），至少须 hedge | 提示 |
| E11 | `md:76` | 「ch21 里她口中的'不作恶'是布莱尔所有女巫的誓，**与这里这条不同**」 | 本章 `:86` 只给 `my oath`，未说内容；「不同」这一判断书中未明写。可支撑它的书内线索是 ch21 `:47` `'But I made a vow, Hamlet.'`（她另有私誓）与 ch20 `:65` `She had sworn never to become so vulnerable.`，md 未引 | 断言缺证（方向可信） | 提示 |
| E12 | `md:13` | 「海伦娜本章**只在台词与一滴眼泪里出现**」 | 她还有动作与外形描写：`:41` `Helena bit her lip`、`:86` `She held the sheet against her chest and stared resolutely at the window`、`:110` `her riot of red curls frothing about like sea waves…her pale arms bare` | 范围写窄（要点"内心不进入"是对的） | 提示 |
| E13 | `md:14` | 「（其中 "If Ophelia was scared, I would stay." 一行**原文没有标明说话者**）」 | 句式确无 tag ✔，但**对话链可锁死**：`:71` → `:74` 辛西娅 `'For how long? Days? Weeks? Months? Years, perhaps?'` → `:77` `As long as she needed.` → `:80` 辛西娅 `'Then I suppose a fox and a ferret make more sense…'`；同链 `:62` 已有 `She wants you.` 的狐狸心语 | 表述可误导（读者会以为无法判定） | 提示 |

---

### 问答链底账（R4 归属核对用）

`:38` 辛西娅 → `:41` 海伦娜 → `:47` 辛西娅（心声）→ `:50` 辛西娅 → `:56` 哈姆雷特 → `:59` 辛西娅 → `:62` 哈姆雷特 → `:65` 叙述 → `:71` 哈姆雷特 → `:74` 辛西娅 → `:77` 哈姆雷特 → `:80` 辛西娅 → `:83` 哈姆雷特 → `:86` 海伦娜 → `:89` 辛西娅 → `:92` 海伦娜 → `:95` 辛西娅 → `:104` 辛西娅 → `:107` 海伦娜 → `:110` 辛西娅 → `:129` 克莱奥 → `:132` 罗宾爵士（渡鸦）→ `:138` 辛西娅 → `:141` 埃莉 → `:144` 辛西娅 → `:147` 克莱奥 → `:150` 埃莉 → `:156` 辛西娅 → `:159` 埃莉 → `:162` 辛西娅 → `:165` 埃莉 → `:168` 克莱奥 → `:171` 辛西娅 → `:174` 克莱奥 → `:177` 辛西娅 → `:180` 克莱奥 → `:183` 辛西娅 → `:186` 克莱奥 → `:189` 埃莉 → `:195` 埃莉 → `:198` 辛西娅 → `:204` 埃莉 → `:207` 辛西娅 → `:210` 克莱奥 → `:219` 辛西娅 → `:222` 克莱奥 → `:225` 辛西娅 → `:228` 埃莉 → `:231` 辛西娅 → `:234` 克莱奥 → `:237` 辛西娅 → `:243` 克莱奥 → `:246` 埃莉 → `:249` 叙述／辛西娅 → `:252` 埃莉 → `:264` 埃莉 → `:267` 克莱奥 → `:276` 辛西娅 → `:285` `:288` 辛西娅（自问自答）。

⇒ md 的 13 块说话人**零错**；`md:66` 已标明「我会非常想你」对魔宠说，正确。

### 块序单调性

`35 < 41 < 47 < 50 < 58 < 86 < 95 < 110 < 113 < 183 < 240 < 255 < 276` ⇒ **13 块 0 调转**。

---

## 四、R4 逐块对应表

| 块 | md | 原文 | 动词主语 | 受事 | 归属方向 | 结论 |
|---|---|---|---|---|---|---|
| 1 | :18 | `:35` | her world（disintegrated） | 梦／现实 | 「她的」世界 ✔；md:24「第一次」⇒ **E3** | 对应 ✔ |
| 2 | :28 | `:41` | Helena（bit lip／eyes flashed）／I know it | 嘴唇／光 | 「知道」＝承认辛西娅的推论 ✔；md:30「同段稍后」⇒ **E4** | 对应 ✔ |
| 3 | :38 | `:47` | I（fallen in love／’m a fool） | 一个不肯爱回去的女人 | 心声归属辛西娅 ✔；md:44「唯一」⇒ **E6** | 对应 ✔ |
| 4 | :48 | `:50` | Anger came／she would nurse／she would use | 心碎／怒气 | 「推后」与「当下」同句 ✔ | 对应 ✔ |
| 5 | :58 | `:58` | her voice（broke）／she turned away | Hamlet | 「可对海伦娜生气、狐狸无辜」✔；md:66「对魔宠说」✔ | 对应 ✔ |
| 6 | :68 | `:86` | Helena（turned／catching）／my oath | Cynthia／誓 | 誓言主体＝海伦娜 ✔；md:76「不同」⇒ **E11** | 对应 ✔ |
| 7 | :78 | `:95` | You（twist／are rejecting／would have guessed） | me／altruism | 施事＝辛西娅的判断 ✔；3 句 ✔ | 对应 ✔ |
| 8 | :88 | `:110` | her arms（ache）／her heart（change）／her soul（seek） | Helena／另一半 | 「她受不了」＝辛西娅的预期 ✔ | 对应 ✔ |
| 9 | :98 | `:113` | Cynthia（pushed／stepped） | 门／未来 | 「独自」＝此刻判词 ✔；md:106「十四行」⇒ **E7** | 对应 ✔ |
| 10 | :108 | `:183` | I（am going to put／am turning／hope to offer） | 宅子／女人 | 「她」承诺 ✔；md:114 产权⇒ **E5** | 对应 ✔ |
| 11 | :118 | `:240` | She（was） | — | 三条身份断言主体＝辛西娅 ✔；漏收尾句⇒ **L2** | 对应 ✔ |
| 12 | :128 | `:255` | she（could transport／shift） | 花瓶／衣柜 | 施事＝辛西娅、尺度＝三寸 ✔ | 对应 ✔ |
| 13 | :138 | `:276` | I（if only…）／she（thought） | 药水 | 「她会用吗」＝她自己的疑问 ✔ | 对应 ✔ |

---

## 五、形态层

| # | 检查项 | 结果 |
|---|---|---|
| 1 | 导航 5 项齐全 | ✔ |
| 2 | 13 块格式 `> **原句 N:**` 连续、外层 `"…"` 首尾闭合 | ✔（本章外层双引号体例整齐，与 ch21 的参差不同） |
| 3 | 四子项齐全（含「读者视角提示」） | ✔ 13/13 |
| 4 | 词表标准 Markdown 表格、9/9/6＝24 行、词头全部在正文命中 | ✔（`check_vocab` rc=0、`vocab_head` rc=0） |
| 5 | 块数档位：13 vs `block_target=[6,10]` ⇒ **超限** | 提示型（rc 仍 0）⇒ **禁止增第 14 块**，补漏只进导航或现有块 |
| 6 | 引号体系：台词单弯、爵夫人原话双弯 | ✔ 与 md:14 自述一致 |
| 7 | `unforgiveable` 拼写＝书内原样（非常规 forgiving 拼法） | ✔ 词表照抄原文，**不得"纠正"** |

---

## 六、实跑取证

**A. 本章推广残留**
```
$ /usr/bin/grep -ci lokepub notes/books/novels/the-hexing-miss-helena-by-darcy-mcguire/text/ch22_chapter_22.txt
0
```

**B. 舞会日期（E2）**
```
$ /usr/bin/grep -niE "tomorrow|to-morrow|morrow|next day|following day|monday|tuesday|wednesday|thursday|friday|saturday|sunday" text/ch22_chapter_22.txt
（无输出）
rc=1
```

**C. 水意象跨章（E3）**
```
$ /usr/bin/grep -n "churning water\|dream" text/ch20_chapter_20.txt
381:Sleep was slow in coming, and when it did arrive, it brought with it dreams of swirling waters, sucking her into their depths.
```

**D. 银光与后续力量失控（md:34 成立）**
```
$ /usr/bin/grep -rn "silver" text/ch22_chapter_22.txt
41:Helena bit her lip. Her grey eyes flashed silver…
86:Hamlet turned his head to Helena, who sat up. She held the sheet against her chest…
$ /usr/bin/grep -n "malfunctioning" text/ch23_chapter_23.txt
65:Her magic had been malfunctioning since Cynthia left.
```

**E. 情绪最低点（E10）**
```
$ /usr/bin/grep -niE "bullet|shot" text/ch26_chapter_26.txt
38:…she watched the counterpart of her soul shudder from the impact of Sinclair’s bullet
98:…‘I can draw out the bullet, but s…
203:‘And you got shot instead.’…
```

**F. 逐字（R2 ＋ 两把独立尺子）**
`chapter.sh --json`：`verdict ok`、13 块全 `ok`、`segment_miss=0`、`issues` 全空；`/tmp/hx_md_frag.py` → `checked=13 BAD=0`；R1 底稿 `/tmp/hx_frag_check2.py` → `checked=203 BAD=0`。

---

## 七、悬置

| # | 悬置点 | 取证 |
|---|---|---|
| U1 | 海伦娜「my oath」的具体内容与立誓时间地点 | `:86` 只有四词；全书未在本章说明——md:76 已要求读者不要补写 ✔ |
| U2 | 舞会具体日期（md 的"次日"无据，但也无法反证是哪天） | §六 B 无命中；只能删「次日」，不能改成别的日期 |
| U3 | `dowager house` 的产权来源（亡夫遗产／她自购／他人赠予） | `:135`/`:183` 均未写；E5 的改法是退回术语释义 |
| U4 | 希金斯太太名单上的女佣具体人数 | `:177` `a rather extensive list`，未给数 |
| U5 | 爵夫人的情人传闻（`:213`）的真假 | 叙述层暗示（`nor any man she set her sights on`），无事实；不裁决 |
| U6 | 克莱奥与埃莉是否真会如约来访 | `:186`/`:243`/`:270` 均为承诺；书内后续不据此判定 |
