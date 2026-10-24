# ch20 深审 R3–R4 三张单子（`ch20 intertwined spirits.md` vs `text/ch20_chapter_20.txt`）

> R1 素读已先行完成（`1-suread.json`，深档，逐字复核 `checked=200 BAD=0`）；R2 机器层见 `2-machine.json`。
> 取证口径：`text/ch20_chapter_20.txt:行号` 逐字；`/usr/bin/grep` 显式路径（`text/` 被 .gitignore 排除，`git grep` 恒空）。

## 〇 结构底账（先立尺子）

1. 正文 `:35`–`:381`；`:106`–`:119` 为**纯空白分场带**（无任何文字，含 0 条推广行）。实测：
   `python3` 扫 `:35`–`:381` 内 `Lokepub`／`Add one to your list` ⇒ **命中 0**。本章不是「水印广告章」，md 也未写广告行——**相符**。
2. 两个视角段：**场景一贴海伦娜 `:35`–`:104`**（回忆十四岁前几天捡到哈姆雷特＋起居室对峙＋辛西娅掌心风暴）；**场景二贴辛西娅 `:120`–`:381`**（回信→记忆仪式→植物治愈→留宿→客厅摊牌→上楼走错门）。
3. **无引号、无说话人标记的心声/传念**共 7 处：`:41`（海伦娜 `So how the bloody hell is he Cynthia's familiar as well?`）、`:156`、`:159`、`:213`、`:216`、`:219`、`:363`（`Drat!`）——其中 **`:351` 是哈姆雷特传给辛西娅的心念**（`You can't leave her. She is frightened. She needs you.`），既无引号也无 tag，形态与人物心声相同、性质是魔宠单向对辛西娅说话。
4. 无 tag 台词 3 处：`:41`（心声）、`:101`（由 `:104` `Clio's words were followed by Sir Robin's caw.` 确认说话人＝克莱奥）、`:351`。
5. 元素与身体证据：**海伦娜＝水**（`:74` `She could feel the water gathering in her hands.`；`:327` `The vase to Cynthia's right started to vibrate as the water within swirled.`；跨章印证 `text/ch09_chapter_9.txt:98` `Helena was cool and calm by nature, much like her element that flowed over obstacles…`）；**辛西娅＝掌心微型风暴**（`:92` `Clouds roiled and spun in the cup of her open hand. Miniature bolts of lightning cracked…`）；窗外雷雨在两人对撞时落下（`:77`）；章末辛西娅梦见 `swirling waters, sucking her into their depths`（`:381`）。
6. 关系口径（本章内可证）：`:180` `she thought it might work on his sister` ⇒ **辛西娅是托马斯的姐妹**；`:273` `her sister-in-law's frank gaze` ⇒ **克莱奥＝托马斯之妻＝辛西娅的嫂子**；`:62` `She and Thomas discovered their connection when they were investigating Lord Beachley's murder` ⇒ **克莱奥与托马斯才是已成的 spirit match**。
7. 能力分工：`:180` 克莱奥通常只见**死者**的过去；`:183` `Ellie… her gifts being limited to the future` 且罗温说 `I don't suppose Ellie can help`（**埃莉并未实际尝试**）；`:68` 海伦娜的天赋是读心；`:204` `Humans can't steal our elemental power.`（「偷力量」第三次被正面否定——md 任何 hedge 不得反向写成断言）。
8. 自封线双对象：`:120` `Ellie, you joked once that **Helena** had hexed herself, and that's why her powers were blocked. You were closer to the truth than you thought.`（回指 `text/ch06_chapter_6.txt:155` 埃莉原话 `Has a witch ever hexed herself, Aunt Rowan?… Have you considered you might be the problem, Hel?`）；`:132` 才转向 `a witch had indeed hexed herself` 的 1629 旧案（来源：`my dear friend, Magnolia Marchbank` 的回信）。⇒ **这条线先套海伦娜，再转辛西娅（`:135` 辛西娅 `Or hexing myself, for that matter?`）**。
9. `:53` `It's possible Hamlet chose both you and Cynthia because your spirits are intertwined…` ＋ `:41` `as well?` ＝ ch19 章末揭示（`text/ch19_chapter_19.txt:396`）的机制所在；**机制在 ch20，不在 ch19**（ch19 判定表已锁此条）。
10. 块数：**12**（`block_target [7,12]` 上限，`block_hint` 空）⇒ **禁增第 13 块**；补漏只进导航或现有块分析层。

## 一 漏（R3-1）

| # | 原文证据（逐字） | 内容 | md 现状 | 档位 |
|---|---|---|---|---|
| L1 | `:120` "Ellie, you joked once that Helena had hexed herself, and that's why her powers were blocked. You were closer to the truth than you thought." | 罗温**正面肯定**埃莉旧玩笑：海伦娜的力量是被她自己封住的（回指 `ch06:155`） | md 全篇把「血魔法自封」只挂在辛西娅身上（导航 md:10、总结 md:181、原句5 md:64）；`:120` 一句在 12 个引语块与导航中无踪 | **阻断** |
| L2 | `:351` "You can't leave her. She is frightened. She needs you."（承 `:348` "Halfway up the stairs, she realised Hamlet had followed her."） | 哈姆雷特**主动向辛西娅传念**（无引号无 tag）＝魔宠与她双向沟通 | 原句9 md:106 写"她只是让哈姆雷特去选海伦娜。后面哈姆雷特照样跟着她上楼"——只到"跟着上楼"，漏掉紧随其后的传念 | **阻断** |
| L3 | `:210` "Her own brother had fallen victim to vicious gossip." ／ `:213` "If Helena is with me, it's worth the effort. Even if we fail." ／ `:216` "Cynthia would need to forge her own path forward. Alone." | 辛西娅在客厅摊牌**之前**已自行算过风险并决定接受；她的"丑闻"参照系是她哥哥 | md:11 写"从被审视的外人，到被确认的女巫与地巫，再到被海伦娜的'不能交织'推开"；md:13 写"她对海伦娜的期待在客厅被拒，转成愤怒和自持"——全章她的主动性被写成纯被动 | **阻断** |
| L4 | `:74` "She could feel the water gathering in her hands." ／ `:327` "The vase to Cynthia's right started to vibrate as the water within swirled." | 海伦娜情绪一失控，水就自行外泄（她的元素）；与辛西娅掌心风暴 `:92` 构成**并置** | md:14 只写"雷声和闪电在两人对峙时落下，章末又以翻涌的水收尾"——元素暗线被降格成天气 | **阻断** |
| L5 | `:35` "Both Clio and Ellie had found their animal companions when they were in their seventh year and first manifested their elemental powers. Helena was coming into her second milestone of magic…" | 魔宠/元素力的**年龄刻度**（七岁初显、第二个里程碑≈十四岁） | 仅作为词表 `manifested`／`milestone` 的例句出现（md:144、md:159），分析层与导航无 | 提示 |
| L6 | `:41`／`:156`／`:159`／`:213`／`:216`／`:219`／`:363`／`:351` | 两段的共同视角手法＝无引号无 tag 的心声（含魔宠传念） | md:14 只说"两段都贴人物限知" | 提示 |
| L7 | `:62` "She and Thomas discovered their connection when they were investigating Lord Beachley's murder." | 克莱奥与托马斯才是已成的 spirit match——本书对"命定之伴"的既有尺度 | 原句4 md:50 只把 spirit matches 译作"灵魂伴侣"，未注明书中已有实例 | 提示 |
| L8 | `:177` "A memory teased at the edges of Cynthia's mind but stayed annoyingly out of reach. A whisper none of them could quite hear." | 合唱时记忆"够不着"的意象 | 原句6 只讲克莱奥的失败；总结写"仪式只留下头痛和一只烧焦的枕头" | 提示 |
| L9 | `:228` "Aunt Rowan reached out and embraced Cynthia in a warm, hard hug. When she released her, Clio and Ellie followed suit. Ellie wiped tears from her eyes. And then Cynthia stood in front of Helena." 承 `:231` "Instead of embracing her, Helena reached down to pet Hamlet…" | 三人依次拥抱→辛西娅站到海伦娜面前→海伦娜却伸手去摸狐狸 | 原句8/原句9 均未提这组对照 | 提示 |
| L10 | `:300` "Apparently, all the Blair women were prone to blushing, except Aunt Rowan." | 叙述者对布莱尔家的一句玩笑式概括 | md:13 只写"埃莉…缓冲" | 提示 |
| L11 | `:360` "With her newfound power, Cynthia gave the fox a nudge, then continued to the second floor." | 辛西娅第一次**主动使用**新力量（对魔宠施力） | 总结只写"辛西娅让哈姆雷特选海伦娜"（指 `:243` 口头），漏 `:360` 的实际施力 | 提示 |
| L12 | `:330` "not sure if she wanted to shake Helena until she saw reason or wrap her up and hold her until she felt steady once more" | 辛西娅的两难（摇醒 vs 抱住） | 原句11 未提；md:13 的"愤怒和自持"缺这一层 | 提示 |
| L13 | `:372` "Once the ribbons had been untied, she took in a lungful of air and exhaled in relief." | 解束腰＝解放的身体隐喻（与 `:174` `voluminous skirts`、`:369` 无人房间呼应） | 词表 `corset` 例句只作词汇用途 | 提示 |

## 二 编（R3-2：md 里原文没有的东西）

对 12 个引语块＋5 项导航＋总结做逐片段回源：**引语层 0 凭空**（`hx_md_frag.py` ⇒ `checked=13 BAD=0`；机器层 `segments=13 segment_miss=0`）。

分析层与导航层逐条核（原文可证＝成立）：

| md 断言 | 证据 | 结论 |
|---|---|---|
| md:24 "惩罚的念头和树篱下的相遇贴在一起" | `:38` 同段内先 `The goddess was punishing Helena…` 后 `an orange ball of fluff scampered from beneath the hedge` | 成立 |
| md:24 "哈姆雷特出场，用动作而不是神谕回答" | `:38` `He looked at her with his golden eyes, yipped, and Helena knew.` | 成立 |
| md:34 "作者让海伦娜自己承认这举动愚蠢小气" | `:44` `Helena could have sat next to her, but she didn’t. It was stupid and petty.` | 成立 |
| md:34 "最后一句短，像结论" | `:44` 末句 `She had stolen Hamlet.`（4 词） | 成立 |
| md:44 "她用的是'有可能'，不是'一定'" | `:53` `It’s possible Hamlet chose both you and Cynthia…` | 成立 |
| md:44 "魔宠的选择……跟着两人的灵魂走" | `:53` `he can’t devote himself to one without also committing to the other` | 成立 |
| md:54 "罗温先否掉前一个猜测" | `:123` 埃莉问 `Is that why Helena can’t hear Cynthia’s thoughts?` → `:126` `‘No. I think there is another reason for that.'` | 成立 |
| md:54 "这里的'如果'很要紧" | `:126` `If they are spirit matches…` | 成立 |
| md:64 "一封回信、一位朋友，再给时间、处境和手段：一六二九年、屠杀、火刑柱、血魔法" | `:132` 顺序为 case→`witch massacres in 1629`→`burned at the stake`→`blood magic` | 成立 |
| md:66 "罗温没有说辛西娅就是那个女巫" | `:132` 只讲 `The poor woman`；`:183` 罗温 `I don’t know why your magic was bound` | 成立 |
| md:74 "克莱奥的特殊经验来自托马斯" | `:180` `given her ability to see Thomas’ memories` | 成立 |
| md:74/76 "只是一点头痛和一只烧焦的枕头" | `:180` `a slight headache for Cynthia and a singed pillow` | 成立 |
| md:84 "作者让答案从辛西娅嘴里出来，而不是让罗温宣布" | `:183` 罗温 `something has loosened the spell’s hold` → `:186` 辛西娅 `‘Hubert’s death.' Cynthia didn’t realise the truth until she spoke it.` | 成立 |
| md:94 "叶脉、茎干、根系、盘根结" | `:225` `through the veins, along its stem, and into the root system… unfurl a rootbound knot` | 成立 |
| md:94 "罗温随后喊出'又有一个地巫'（earthwitch）" | `:228` `‘Well, I think we have another earthwitch among us!'` | 成立 |
| md:96 "罗温的确认也让'偷海伦娜的魔法'这个指控更难成立" | `:204` `Humans can’t steal our elemental power.` | 成立 |
| md:104 "辛西娅先道歉，再否认偷窃，最后把选择交给魔宠" | `:243` `‘I’m sorry about Hamlet… I wasn’t stealing your magic, and I promise now I won’t steal your familiar.’ She turned to Hamlet. ‘You must choose Helena.'` | 成立 |
| md:106 "后面哈姆雷特照样跟着她上楼" | `:348` | 成立（但见 L2：不止"跟着"） |
| md:114 "她用的不是'我不愿意'，而是'不可能'" | `:336` `But our souls cannot be intertwined. It’s impossible.` | 成立 |
| md:114 "她怕的不是辛西娅，而是自己会陷进去" | `:65` `She had sworn never to become so vulnerable.`；`:56` `Alarm tightened fingers around her throat.` | 成立 |
| md:120 "今晚让她累的不是这场折腾，而是海伦娜" | `:345` `This evening did not exhaust me, but you have.` | 成立 |
| md:124 "'害怕'是这里面最准的一刀" | `:321`/`:324` 辛西娅已点破她在回避；`:65` 誓言 | 成立 |
| md:134 "'几乎'两个字很关键——她动摇了，但没有进去" | `:366` `nearly washing away her resolve` → `:369` `Shutting the door with a loud click, she turned and entered the opposite room.` | 成立 |
| md:136 "她闻到的是海伦娜的房间" | `:366` 佛手柑与柠檬＋紧随 `What she wouldn’t give to hold Helena.`；跨章 `ch10:80` `Bergamot and lemon soap.`（海伦娜身上）、`ch18:380`、`ch27:137` | 成立 |
| md:136 "合上门、进对面房间的动作在下一段" | `:369` 逐字 | 成立（精确） |
| md:11 "最后在辛西娅掌中风暴前忘记愤怒与誓言" | `:98` `Helena forgot everything. Her anger. Her fear. Her promise to never fall in love.` | 成立 |
| md:181 "克莱奥当场断定她确实是女巫" | `:101`＋`:104` `Clio’s words were followed by Sir Robin’s caw.` | 成立（说话人确认无误） |
| md:181 "最终进了对面房间，睡下后梦见翻涌的水" | `:369`／`:381` | 成立 |

**凭空判定：0 条。**（md:24 "她的安心里就始终混着一点不敢确认" 与同段末 `Helena knew.` 相反，计入「错」E9，不重复计凭空。）

## 三 错（R3-3）

| # | md 位置与原文 | 错在哪 | 证据 | 档位 |
|---|---|---|---|---|
| E1 | md:13 "她的嫉妒先替她定了罪，**随后又被罗温的解释逼回自己身上**。" | 时序＋触发者写反：自我拆穿发生在罗温解释**之前**（`:44` `It was stupid and petty`、`:47` `Shame warred with fear`）；罗温解释（`:53`）之后她是**更怕＋向外追问**（`:56` Alarm→`:68` 追问→`:74` nearly shouted），直到辛西娅掌心风暴才忘怒（`:98`）。且与自家 md:11 的顺叙（`承认小气→更恐慌→风暴前忘记`）自相矛盾 | `:44`/`:47`/`:53`/`:56`/`:68`/`:74`/`:98` | **阻断** |
| E2 | md:10 "罗温用**林利思戈巫团的回信**讲出一六二九年血魔法自封的前例"；md:181 同 | 来源归属：`:120` 林利思戈回信对应的是"海伦娜自封"那句玩笑；1629 旧案出自 `:132` "my dear friend, Magnolia Marchbank" 的回信。两处是否同一封信原文未写 ⇒ 不得合并为"林利思戈讲 1629" | `:120`/`:132` | 提示 |
| E3 | md:70 "她以为这招对**妹妹**也能用" | `:180` 只写 `his sister`（托马斯的姐妹），未分长幼；"妹妹"新增序位 | `:180` | 提示 |
| E4 | md:12 "留宿与'**只隔一条走廊**'" | `:300` 埃莉原话 `Helena is just across from you`；`:360` 楼梯平台左右两扇门 ⇒ 是"对面"，不是"隔一条走廊"（罗温与埃莉才 `all the way down the hall`） | `:300`/`:360` | 提示 |
| E5 | md:14 "两段都贴人物限知，**对话占大半**" | 量化证伪：正文 `:35`–`:381` 共 112 个自然段，**45 段以引号起句（40%）、66 段含引语（59%）**；按词数引语仅 **566／3854 ≈ 14.7%**。"占大半"若指篇幅必错，若指段数也只到"过半含引语" | 实跑脚本（见 §六） | **阻断** |
| E6 | md:11 "后半是辛西娅的视角：**从被审视的外人**" | `:255`/`:258`/`:228` 她被挽留、被拥抱、被称为 `another earthwitch among us`；本章内她是被接纳者，"外人"与原文相反（对照 `ch19:312` `You welcomed me into your family`） | `:228`/`:255`/`:258` | 提示 |
| E7 | md:10 "罗温解释说**这是因为**两人的灵魂交织" | 把 `:53` `It’s possible…` 的推测升级为定论；与自家 md:44/md:46 的 hedge 冲突 | `:53` | 提示 |
| E8 | md:181 "克莱奥只能看死者的过去，**埃莉只能看未来**"（并列入"众人试着唤回"） | `:183` 罗温说 `I don’t suppose Ellie can help with her gifts being limited to the future` ⇒ 埃莉**未被尝试**，不是"试了但只能看未来" | `:183` | 提示 |
| E9 | md:24 "她的安心里就**始终混着一点不敢确认**" | 引语止于 `right over to Helena`，同一自然段结尾是 `Helena knew. She had found her spirit companion.`——毫不迟疑；"不敢确认"只属于 `:38` 前半的惩罚之忧 | `:38` | 提示 |
| E10 | md:24 "'做错了事'**始终**没有说明是什么事' | 全章级否定断言未限定范围；实测 `:38` 的 `what she had done` 在全书 `text/` 中仅此一次命中（见 §六），本章内成立，但"始终"读起来像全书 | `:38`＋grep | 提示 |
| E11 | md:126 "这个背影就是本章两人关系的落点" | 本章在它之后还有 `:348`–`:381` 三拍（狐狸传念、走错门、对面房间与梦）；"落点"若被读成情节终点即失真——与 md:14"章末又以翻涌的水收尾"并列时，措辞需限定为"情感的落点" | `:348`–`:381` | 提示 |

**问—答链底账**（`:68`→`:71`→`:74`→`:77`→`:80`→`:83`→`:86`→`:89`→`:92`；场景二 `:120`→`:123`→`:126`→`:129`→`:132`→`:135`→`:138`→`:141`→`:144`→`:147`→`:150`→`:153`→`:156`→`:159`→`:162`→`:165`）：
每问必查"谁问的／谁答的／答的是不是同一个问题"。三处关键：
- `:68` 海伦娜问"为什么我听不见哈姆雷特，而她能听见哈姆雷特"——**同一场景内**无人回答，答案要到场景二 `:126`（罗温对埃莉 `:123` 的追问才答"平衡"）。md 原句4 把它当作对 `:123` 的回答 ✓ 正确，未踩"跨场景合并"的坑。
- `:123` 埃莉问的是"是不是因为海伦娜自封 ⇒ 所以海伦娜听不见辛西娅"；`:126` 罗温答"No"，但 `:120` 刚说埃莉"更接近真相"——**先肯定自封、再否定它解释这一现象**。md 原句4/原句5 均未写出这一"同一段落内先 Yes 后 No"的层次（并入 L1 修）。
- `:234` 海伦娜问 `What have you done to him?` → `:237` 辛西娅 `What have I done? Truly?` → `:240` 海伦娜 `He’s never acted this way before.` → `:243` 辛西娅三段式回应。md 原句9 从 `:243` 起引 ✓ 未打乱序；但总结把 `:234` 写成"海伦娜问她对它做了什么"✓ 方向对。

**时序专查**（章内）：`:35`（回忆，14 岁前）→`:44`→`:53`→`:92`→`:101` 顺序单调 ✓；`:120`→`:132`→`:165`→`:180`→`:186`→`:225`→`:243`→`:249`→`:270`→`:306`→`:336`→`:345`→`:366`→`:381` 顺序单调 ✓；md 引语块 1–12 落点 `:38/:44/:53/:126/:132/:180/:186/:225/:243/:336/:345/:366` **全部单调递增，零调转**。唯一时序缺陷＝E1（把 `:44`/`:47` 的自我拆穿排到 `:53` 之后）。

## 四 R4 逐块对应（12/12）

| 块 | md 行 | 引语落点 | 动词主语／受事 | 归属方向（谁的·谁欠谁·谁问的） | 判定 |
|---|---|---|---|---|---|
| 原句1 | 18 | `:38` | 主句主语＝海伦娜（she/Helena）；毛球＝哈姆雷特；`right over to Helena` 受事＝海伦娜 | 女神→海伦娜（她单方面解读）；md:26 明示"是海伦娜自己的解释，不是叙述者的判决" ✓ | 对应 |
| 原句2 | 28 | `:44` | `she didn’t` 主语＝海伦娜；`she dismissed the idea` 主语＝海伦娜；`She had stolen Hamlet` 主语＝辛西娅（海伦娜的判词） | 谁在定罪：海伦娜给辛西娅；md:36 已标"不是书里发生的事" ✓ | 对应 |
| 原句3 | 38 | `:53` | `Those witches are bound`；`It’s possible Hamlet chose both you and Cynthia`；`he can’t devote himself` 主语＝哈姆雷特 | 说话人＝罗温（`:50` 已 establish）✓；md:40 写"罗温说" ✓ | 对应 |
| 原句4 | 48 | `:126` | `hearing Cynthia’s thoughts would be an unfair advantage`；`The goddess believes in balance` | 说话人＝罗温（`:126` `Aunt Rowan watched Helena carefully.`）✓；回答对象＝`:123` 埃莉之问 ✓ | 对应 |
| 原句5 | 58 | `:132` | `I sent my letter to… Magnolia Marchbank, she told me of a case`；`she used blood magic to block her own powers` | 双重转述：罗温←玛格诺莉亚←旧案女巫；md:60 "对方告诉她" ✓ 方向对 | 对应 |
| 原句6 | 68 | `:180` | `Clio tried next`；`she thought it might work on his sister`（`his`＝Thomas） | 施事＝克莱奥；受事＝辛西娅；`his sister`＝托马斯的姐妹 ⇒ md:70 用"妹妹"新增序位（E3） | 对应（序位待订） |
| 原句7 | 78 | `:186` | `Cynthia didn’t realise the truth until she spoke it`；`A widow is beholden to no one but herself` | 领悟者＝说者＝辛西娅；md:84/86 强调"不是罗温宣布""没人替因果作证" ✓ | 对应 |
| 原句8 | 88 | `:225`（两段拼接，`…` 省略 `At first, she wasn’t sure what to do, but`） | `Cynthia was able to regenerate three plants`；`she funnelled her energy`；受事＝植物根系 | 力量来源＝辛西娅自己，作用于植物自身通路；md:96 "她动的不是别人的力量" ✓ | 对应 |
| 原句9 | 98 | `:243` | `I wasn’t stealing your magic`；`You must choose Helena`（对哈姆雷特说）；`Something ached in Cynthia at cutting the bond` | 说话人＝辛西娅，命令对象＝狐狸，让渡对象＝海伦娜；md:104/106 方向 ✓（漏 L2） | 对应 |
| 原句10 | 108 | `:336` | `I cannot be your spirit match`；`our souls cannot be intertwined` | 说话人＝海伦娜（`:327`/`:330` 之间），对象＝辛西娅；md:110 "海伦娜说" ✓ | 对应 |
| 原句11 | 118 | `:345` | `You are impossible, Helena Blair`；`This evening did not exhaust me, but you have` | 说话人＝辛西娅，指向＝海伦娜（全名）；md:120 ✓ | 对应 |
| 原句12 | 128 | `:366` | `she cracked open the door to her right`；`a wave of bergamot and lemon poured forth`；`Her core melted` | 施事＝辛西娅；房间归属＝海伦娜（跨章气味印证）；md:136 方向 ✓ | 对应 |

调转 **0**；主客／让渡／传念方向错 **0**（唯一方向问题是 E2 的"信源归属"与 E1 的"谁触发自省"）。

## 五 形态（8 项判据）

| 项 | 实测 | 判定 |
|---|---|---|
| H1 | `# 20. Chapter Twenty`（书内既有形态） | ✓ |
| 导航子项数 | 5（`nav_count_ok` true，`nav_missing` []） | ✓ |
| 引语块数 | 12（`block_target [7,12]`，`block_hint` 空）⇒ **触顶，禁增第 13 块** | ✓（受限） |
| 四子项 | 中文理解／关键词／为什么这样写／读者视角提示 全 12 块齐 | ✓ |
| 关键词长度 | `keyword_bad=0 keyword_long=0`；12 组均为引语内子串 | ✓ |
| 中文占比 | `cjk_low=0`（各块 0.84–0.92） | ✓ |
| 词表 | `## 本章词汇` 24 行＝高级 9／进阶 9／基础 6；`vocab_check_hx.py 20` rows=24 missing=0；`vocab_head_hx.py 20` rc=0；表体为标准 Markdown 四列 | ✓（两处微瑕见下） |
| 引语片段 | `segments=13 segment_miss=0`；独立尺子 `hx_md_frag.py` `checked=13 BAD=0` | ✓ |

形态层两条提示（不判阻断）：
- F1 md:172 `familiar | 魔宠，使魔`——与全书统一译名台账（Hamlet 一律"魔宠"，魔宠 53／使魔 13／灵兽 2 待统一）冲突，释义里并列"使魔"会再制造一个口径。建议删"，使魔"或改为"魔宠（书中译名统一作'魔宠'）"。
- F2 md:152 `intertwined` 例句末尾残留右单引号 `…committing to the other.’`——同表其余 23 行例句均无引号残留；建议去掉行首行尾的引号字符。

## 六 实跑取证（命令＋输出＋退出码）

```
$ bash scripts/chapter.sh "…/ch20 intertwined spirits.md" --json
rc=0  verdict=ok  md/corpus 字段路径均已核存在（避免 ch19 那种空壳假绿）
blocks=12  words=3779  block_target=[7,12]  block_hint=""（触顶不增）
segments=13  segment_miss=0  struct_bad=0  empty_quote=0  keyword_bad=0  cjk_low=0  template=0  hole=0  block_count=0
form: h1="20. Chapter Twenty" nav_count=5 profile=novels

$ python3 /tmp/vocab_check_hx.py 20   → ch20: rows=24 missing=0   rc=0
$ python3 /tmp/vocab_head_hx.py 20    → （无输出）                 rc=0
$ python3 /tmp/hx_md_frag.py <md> <text/ch20_chapter_20.txt>       → checked=13 BAD=0
$ python3 /tmp/hx_frag_check2.py text/ch20_chapter_20.txt review/ch20/1-suread.json → checked=200 BAD=0

$ python3（正文 :35–:381 量化）
paras=112  start-with-quote=45  contain-quote=66  quoted_words=566  total_words=3854  ratio=0.147
scene1 :35-:104 dlg/tot = 116/870 = 0.133 ; scene2 :120-:381 = 450/2984 = 0.151
Lokepub/「Add one to your list」命中 0（⇒ :106–:119 为纯空白分场带）

$ /usr/bin/grep -n "hexed" text/ch*.txt
ch03:261 ch06:155 ch16:35 ch20:120 ch20:132   （rc=0）
$ /usr/bin/grep -rn "closer to the truth" text/ch*.txt → ch10:161 ch20:120
$ /usr/bin/grep -rn "what she had done" text/ch*.txt → 仅 ch20:38
$ /usr/bin/grep -n "water" text/ch20_chapter_20.txt → :74 :186 :327 :369 :381
$ /usr/bin/grep -rn "her element" text/ch*.txt → ch09:98 ch16:275
```

## 七 悬置与不裁决（U）

- U1 罗温给海伦娜与辛西娅的是**同一件雪莉酒容器吗**：`:44` 辛西娅 `a glass of sherry`、`:120` 罗温 `her crystal glass of sherry`——两处并存，不裁决是否同一壶／是否有人换过杯。
- U2 1629 旧案与辛西娅是否为同一人：`:132` 只说 `a witch`，原文未点名 ⇒ 不得写成"就是辛西娅"（md 已守住，见 §二）。
- U3 林利思戈巫团的回信与玛格诺莉亚的回信是否同一封：原文未写 ⇒ 只订正归属口径（E2），不裁决"两封信"。
- U4 埃莉玩笑（`ch06:155`）被 `:120` 肯定到什么程度：`closer to the truth than you thought` 之后紧接 `:126` 的 `No`——**罗温对"海伦娜自封"是肯定、对"自封解释了听不见"是否定**；两读皆有文本支持 ⇒ 只补写层次，不裁决成"海伦娜确实自封了"。
- U5 海伦娜「做错了事」是什么：本章未写（`:38` 全书唯一命中）⇒ 不得补写。
- U6 `:366` 右边门＝海伦娜的房间：由气味（`ch10:80`）与 `:300` "Helena is just across from you" 推出，原文未有一句"this was Helena's room" ⇒ 保留推断口径，不写成原文陈述。
- U7 `:381` 的梦是否预示后文水相关危机：本章无 ⇒ 不作预言。
- U8 `:327` 花瓶的水是海伦娜施的还是自行震动：原文 `The vase to Cynthia's right started to vibrate as the water within swirled.` 未写施事 ⇒ 只能说"随她情绪外泄"，不写"她失控施法"。
