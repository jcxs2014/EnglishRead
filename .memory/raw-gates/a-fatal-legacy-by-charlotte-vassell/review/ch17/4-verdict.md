# R5 判定表 · A Fatal Legacy ch17《The National Portrait Gallery》

> 唯一权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch17_17.txt`（6,133 字符）
> 被审 md：`.../ch17 callie sketches elizabeth at the gallery.md`
> 档位：**阻断**（与原文不符/缺失）｜**提示**（措辞正当）｜**假红**（工具判错）｜**跳过**（没查）
> 逐条「阻断」均附 `text/<file>:<行>` 与该处原文逐字（R5 硬约束）。
>
> ⚠️ **本表含两轮**：§一/§二 = **修前**（md5 `fadeb9e09fe3739186233ba0a29e121b`，commit `233f92c4e`）；
> §一bis/§二bis = **修后**（md5 `4364edbe500942c9b1cf36d189f589fd`，commit `aa3fbb714`）。
> 审查期间另一实例读了本目录的落盘件并据以整改（`fc89f7d9a` + `aa3fbb714`），md 被重写；
> 按 §3「报告要给修前→修后」，两轮都留档。**最终结论以 §一bis/§二bis 为准。**

---

## 一、四组数（只报这四组）｜**修前**

| 组 | 数 | 说明 |
|---|---|---|
| **逐字** | **6/6 通过**（引语）＋ **30/30 通过**（词汇例句） | 6 块引语全部是原文的**连续**子串（Python `str.find` 独立复算，与 `chapter.sh --json` 的 6/6 一致），无 `…` 缝合、无跨话轮拼接；30 条词汇例句 30/30 命中本章原文 |
| **对应** | **5/6 通过**，**1 阻断** | 6 块逐块人判：原句 4 因施事反转 + 自相矛盾判阻断；原句 2、3 各带提示（引语选短 / 措辞无据） |
| **形态** | **通过，0 偏离** | H1 `17. The National Portrait Gallery`（合原文标题、合本书 `# NN. 标题`）；导航 5 项 = 全书 54 章同名同序（`一句话概括/视角/线索结构/人物弧线/叙事手法`）；子项集 = profile 要求的 `中文理解/关键词/为什么这样写/读者视角提示`（未用 optional `句子结构`）；块数 6 = 全书出现最多的块数（19/54），落在众数区间 [5,10] 内，中位 7 → **无偏离，不需写理由** |
| **断言** | **阻断 5 条 ＋ 提示 8 条** | 详见下表 |

**修前阻断型条数：5**（W1 临摹、W2 两次退下、W3 排队施事反转、C1 反酸、原句 4 对应阻断＝与 W3 同一处，不重复计）

---

## 一bis、四组数（只报这四组）｜**修后（最终结论）**

| 组 | 数 | 说明 |
|---|---|---|
| **逐字** | **6/6 通过**（引语）＋ **30/30 通过**（词汇例句） | 整改后重测：6 块引语仍全部为原文连续子串；30 条词汇例句仍 30/30 命中本章原文（整改未动引语与词表例句） |
| **对应** | **6/6 通过**，**0 阻断**，**4 提示** | 原句 4 的施事反转已修（见 §二bis #3），逐块层面不再有阻断；残留提示：原句 2 引语选短、原句 3 措辞无据、原句 4 `Judging by` 方向、原句 6 摘要冲突已消 |
| **形态** | **通过，0 偏离** | 整改后重跑 `chapter.sh --json`：`h1_shape_ok=true`、`nav_count=5`、`blocks=6`、`block_median=7`、`block_range=[5,10]`、`profile=mystery-thriller` —— 与修前完全一致，未因整改产生形态偏离 |
| **断言** | **阻断 2 条（本章 md）＋ 1 条（跨文件）＋ 提示 8 条** | 详见 §二bis |

**修后阻断型条数：本章 md 2 条 ＋ 跨文件 1 条 ＝ 3**（残留 R1 排队施事反转、R2 半钟头情境与时序倒置；跨文件 R3 `00_金句精选.md:96,98` 反酸断言）

---

## 二、判定表

| # | 断言 | 证据（章:区间） | 结论 | 档 |
|---|---|---|---|---|
| 1 | md:11 `卡莉在国家肖像馆临摹伊丽莎白一世的画像`；md:110 `卡莉在国家肖像馆临摹伊丽莎白一世` | `text/ch17_17.txt:20`：`She had her sketchbook out. She wasn’t copying the image of the golden-age queen, she was just picking out the details that she liked.` | 原文明确否定「临摹」（`wasn’t copying`），且同份 md 的 `md:21`／`md:23` 读法相反 → 摘要层把作者明写的否定翻了 | **阻断** |
| 2 | md:13 `身体线（恶心两次袭来又两次退下）`；md:110 `她的身体两次反胃、两次退下` | `text/ch17_17.txt:29`：`The wave of nausea seemed to abate and she stood up.`（唯一一次退下）＋ `The nausea had returned and she didn’t want to puke…` ＋ `the shade of chartreuse she’d turned`；`text/ch17_17.txt:83`：`Pausing the recording periodically, unsure as to whether she was going to have to run to the loo to puke or not.` | 原文是「一次退下＋一次卷土重来＋章末仍未退」，md 写成「两次退下」，抹平了章末的开放状态；`md:56` 自己译的「不确定」与之冲突 | **阻断** |
| 3 | md:14 `到洗手间外排着队…的卡莉`；md:44 `她…是在占一个位置、排在队里`；md:45 `这个展厅里除了她还有别人在排队` | `text/ch17_17.txt:29`：`Callie stared at the white porcelain bowl… The wave of nausea seemed to abate and she stood up. Judging by the tutting, quite a queue was forming outside. She performatively flushed the empty toilet and went to wash her hands.` | 此刻卡莉**在洗手间里**，`a queue was forming outside` 是**别人在门外排**；md 把「她占了洗手间」写成「她在排队」，且同文件三处口径互斥（她排／门外一排人／展厅里的人）。四道机器探针全绿，只有施事追问能抓 | **阻断** |
| 4 | md:11 `她的胃却先开始反酸` | `text/ch17_17.txt:26` `She’d suddenly started to feel a bit sick.`；`:29` `The wave of nausea seemed to abate…`／`The nausea had returned…`；`:68` `she just felt rough`；`:83` `unsure as to whether she was going to have to run to the loo to puke or not.`；检索 `/usr/bin/grep -n -iE "acid\|reflux\|heartburn\|burn" text/ch17_17.txt` → 无输出、退出码 1 | `反酸`（胃酸反流）原文没有；原文只给 `nausea/sick/puke`。同 md 的 `md:110` 又写「反胃」、词汇表把 `sick` 释为「想吐；恶心」，三处口径不一。**联动**：`00_金句精选.md:96,98` 已把「反酸」写成 ch06→ch17→ch29→ch54 的既有身体线，只改 ch17 会留悬空断言 | **阻断** |
| 5 | md:11 `等消息的半个钟头里坐不住`；md:110 `等消息的半个钟头里从从容容地挑细节走到坐立不安`；md:11 `合同的回音刚到，她的胃却先开始反酸` | `text/ch17_17.txt:20`：`Callie had been sitting in front of a portrait of Elizabeth I for the last half an hour. She had her sketchbook out.`；`:23`：`But Callie had had enough of drawing for now. She checked her phone and saw that Mel had replied…`；`:26`：`She’d suddenly started to feel a bit sick.` | 三处对不上：①那半小时是**坐着画**（`had been sitting… She had her sketchbook out`），非「坐不住」，且 `md:110` 自称「从从容容」与 `md:11` 自相矛盾；②原文顺序是**先**查手机见回信、**后**在展厅犯恶心，`胃却先` 把先后倒置；③「刚到」原文无据（`md:28` 自己译成「已经回复了」） | **阻断**（时序 + 自相矛盾） |
| 6 | md:11 `中途躲进洗手间` | `text/ch17_17.txt:26`：`Callie flicked her hair in her direction when she turned abruptly to find the loos.`；`:29`：`Callie stared at the white porcelain bowl… She performatively flushed the empty toilet and went to wash her hands.` | 「进洗手间」有据；「躲」为文学化用词，可接受 | 提示 |
| 7 | md:110 `她只能一遍遍伸手去够那只点开邮箱却始终空着的 iPad` | `text/ch17_17.txt:50`：`Callie reached for the iPad and opened her emails.`；`:56`：`Callie refreshed her email – still nothing.`；`:83`：`She checked her email for the ‘thing’ that Eulalia had seen but nothing came through.` | 邮箱里**并非始终空着**——梅尔的回信、合同与 NDA 都在里面（`:23`），空的是**欧拉莉亚那封「我看到的东西」的邮件**。摘要层把两件事混成一件 | 提示 |
| 8 | md:44 `把等待换算成了身体在走廊里的具体位置` | `text/ch17_17.txt:29` 全文只给 `the white porcelain bowl` 与 `outside` 两处空间 | 原文无「走廊」 | 提示 |
| 9 | md:37 `甩头发既是挑衅也是掩饰` | `text/ch17_17.txt:26`：`…gave her a dirty look and was ready to pounce and tell her that the flash would damage the pigments in the paintings, but she was disappointed. Callie flicked her hair in her direction when she turned abruptly to find the loos.` | 原文是轻蔑地一甩，无「掩饰」义 | 提示 |
| 10 | md:15 `把庄严的展厅布景与失控的生理反应并置` | `text/ch17_17.txt:26,29,83`：她主动找洗手间（`turned abruptly to find the loos`）、自己缓过来（`seemed to abate`）、当众把戏做圆（`performatively flushed`） | 全程在管理身体，非「失控」 | 提示 |
| 11 | md:11 / md:13 / md:110 三处均未出现「马桶是空的、她其实没吐」 | `text/ch17_17.txt:29`：`She performatively flushed the empty toilet and went to wash her hands.` | 覆盖缺口：读者易把「躲进洗手间」读成吐了；原文恰恰相反 | 提示（漏） |
| 12 | md:13 线索结构只列 工作线/等待线/身体线，未列人物层 | `text/ch17_17.txt:83`：`Callie didn’t expect the world’s most mysterious pop girlie… to be lonely, let alone to see her as a source of comfort.` ＋ `Callie remembered reading on some blog somewhere that Eulalia had studied at the Royal College of Music.` | 覆盖缺口：欧拉莉亚「孤独、把卡莉当安慰来源」这层解释了等待线为何一直打滑，md 未收 | 提示（漏） |
| 13 | md:13/110 身体线完全按「等消息引起的焦虑」解释 | `text/ch17_17.txt:23`：`Or rather than a beach holiday she should use some of the money on a good pram. Something they could use for all their children… She needed to work out how she’d tell her mother, but that was a problem for another day.` | 覆盖缺口：怀孕/瞒着家人这层缺席（`pram` 只在词汇表 `md:103` 出现） | 提示（漏） |
| 14 | md:44 `Judging by the tutting` 的方向 | `text/ch17_17.txt:29`：`Judging by the tutting, quite a queue was forming outside.` | 主语是卡莉据咂嘴声**推断**；md 中文理解写成「从外面传出的咂嘴声判断」＝方向调换（可读，但非原文结构） | 提示 |
| 15 | md:30 `作者把商业措辞（相称的费用、期限、范围）原样搬进叙述` | `text/ch17_17.txt:23`：`the fee was commensurate with the short deadline and wide scope of the project` | 成立（引语内） | 通过 |
| 16 | md:52 `那封邮件在本章里始终没到——欧拉莉亚说“我可以发给你”，随后发来的是餐厅地址和几张表情包` | `text/ch17_17.txt:47`：`‘I can email it to you.’`；`:83`：`She checked her email for the ‘thing’ that Eulalia had seen but nothing came through.`；`:5615`：`Her phone pinged with the address of a restaurant… Then came a meme. And another. And another.` | 全部成立（说话人、先后、内容均对） | 通过 |
| 17 | md:24 `本章里展厅的画不是布景，它和卡莉正在扮演的那个人是同一件事的两种说法` | `text/ch17_17.txt:20`：`Feminine or rather feminised armour.`；`:23`：`‘Amelia’s’ email` | 成立：`Amelia` 即卡莉的化名（`text/ch06_6.txt:224` `Calliope Foster Millinary, Amelia speaking.`；`text/ch48_48.txt:120` `Yours, Amelia`） | 通过 |
| 18 | md:58 `两个女王隔空并置` | `text/ch17_17.txt:83`：`the show about Eleanor of Aquitaine` ＋ `:20`：`a portrait of Elizabeth I` | 成立 | 通过 |
| 19 | md:12 `第三人称限知，全程贴着卡莉的注意力与身体` | 全章 `text/ch17_17.txt:20-83` 无第三人称切换、无他人视角 | 成立 | 通过 |
| 20 | md:13 `等待线（欧拉莉亚说“我看到点东西”，却一直没发过来）` | `text/ch17_17.txt:41`：`‘I saw something interesting.’`；`:83`：`nothing came through.` | 成立 | 通过 |

---

## 二bis、修后判定表（最终结论；md5 `4364edbe500942c9b1cf36d189f589fd`）

> 整改来源：本审查 §一/§二 的落盘件被另一实例读取并据以整改（`fc89f7d9a` 修 ch17 md，`aa3fbb714` 再修总结行「临摹」）。
> 下列逐条复核**在整改后的 md 上重做**，不是照抄修前结论。

| # | 断言 | 证据（章:区间） | 结论 | 档 |
|---|---|---|---|---|
| 1 | md:11 `卡莉在国家肖像馆对着伊丽莎白一世的画像挑细节`；md:110 同；md:58 `展厅里被她拆着挑的那位是伊丽莎白一世` | `text/ch17_17.txt:20`：`She wasn’t copying the image of the golden-age queen, she was just picking out the details that she liked.` | **已修**（原「临摹」→「挑细节」）。注意 md:21／md:23 仍保留「临摹」二字，但那是**否定式**用法（`她并没有在临摹…`／`作者不让她老老实实临摹，而是让她“挑选”`），与原文一致，**属已核实为正确，勿再动** | 通过 |
| 2 | md:13 `身体线（恶心两次袭来：一次退下、一次卷土重来，章末悬而未决）`；md:110 `她的身体两次反胃：一次退下、一次卷土重来，章末还没个了断` | `text/ch17_17.txt:29`：`The wave of nausea seemed to abate and she stood up.`（唯一一次退下）／`The nausea had returned…`；`text/ch17_17.txt:83`：`unsure as to whether she was going to have to run to the loo to puke or not.` | **已修**，与原文的一次退下＋一次卷土重来＋章末未决完全对上 | 通过 |
| 3 | md:14 `到洗手间外排着队、只能对着空邮箱一遍遍伸手的卡莉` | `text/ch17_17.txt:29`：`Callie stared at the white porcelain bowl for a moment… The wave of nausea seemed to abate and she stood up. Judging by the tutting, quite a queue was forming outside. She performatively flushed the empty toilet and went to wash her hands.` | **残留**：md:44／md:45 已改对（`门外那队人照旧排着`／`那扇洗手间的门外还排着人`），**但 md:14 的「人物弧线」仍是「排着队的卡莉」** —— 她在洗手间**里面**，队是**别人**在门外排。原句 4 的三处口径现已互斥（md:14 队是她／md:15 `门外那队人`／md:44 `她把自己关在里面`）。修法：md:14 改为「到被排队等在洗手间外的卡莉」之类，与 md:44 口径对齐 | **阻断** |
| 4 | md:11 `等消息的半个钟头里坐不住：合同的回音刚到，她的胃却先开始发闷想吐`；md:110 `等消息的半个钟头里从从容容地挑细节走到坐立不安` | `text/ch17_17.txt:20`：`Callie had been sitting in front of a portrait of Elizabeth I for the last half an hour. She had her sketchbook out.`；`:23`：`But Callie had had enough of drawing for now. She checked her phone and saw that Mel had replied…`；`:26`：`She’d suddenly started to feel a bit sick.` | **残留（两处）**：(a) 那半小时原文写的是**坐着画**（`had been sitting… She had her sketchbook out.`），不是「坐不住」；且 md:110 又自称那半小时「从从容容地挑细节」——同文件自相矛盾。(b) 原文顺序是**先**查手机见回信（`:23`）、**后**在展厅犯恶心（`:26`），md:11 的「胃却先开始」把先后倒置。修法：md:11 与 md:110 的「等消息的半个钟头里」改为「画了半个钟头、查手机看到回信之后」，删「胃却先」 | **阻断** |
| 5 | `00_金句精选.md:96` `这条身体线（紧张、反酸、恶心、想吐）从 ch06 一路铺到 ch29 的抽血和 ch54 那句「这里没有胎心」`；`:98` `与 ch17 里她在国家肖像馆等消息时胃里反酸、躲进洗手间那段同源` | `text/ch17_17.txt` 全文检索 `acid\|reflux\|heartburn\|burn` → 无输出、退出码 1（本章原文无「反酸」）；ch17 md 已于 `fc89f7d9a` 把「反酸」改为「发闷想吐」，但**总览两处仍留「反酸」，且第 96 行把「反酸」挂到 ch06 起点上**（ch06 引文为 `Callie was tense. Her shoulders were braced, waiting for something terrible to happen.`，无反酸）；`text/ch17_17.txt:26`：`She’d suddenly started to feel a bit sick.` | **残留（跨文件）**：ch17 md 本身已修，但总览三篇中的 `00_金句精选.md` 两处仍把「反酸」写成贯穿 ch06→ch17→ch29→ch54 的既有身体线。**本书 54 章 md 中「反酸」现已归零**（修后实测：`反酸=0`、`反胃=2`、`恶心=10`、`想吐=4`），这两处成了全书唯一的「反酸」，正与「全书只用这四个症状词」的惯例冲突 | **阻断**（跨文件，需另派修 `00_金句精选.md`） |
| 6 | md:44 `把等待换算成了身体在一扇关着的门里的具体位置：门外那队人照旧排着、照旧咂嘴，她把自己关在里面` | `text/ch17_17.txt:29` 逐字 | **已修**：施事与位置全部对上（她在门内，队与咂嘴在门外），且「一扇关着的门」不再凭空造「走廊」 | 通过 |
| 7 | md:15 `洗手、门外那队人`；md:45 `那扇洗手间的门外还排着人` | 同上 `:29` | **已修**：不再把「排队」记在卡莉身上 | 通过 |
| 8 | md:15 `把庄严的展厅布景与失控的生理反应并置` | `text/ch17_17.txt:26,29,83`（她主动找洗手间、`seemed to abate`、`performatively flushed`） | **残留（提示级）**：原文里她全程在管理身体，「失控」不确 | 提示 |
| 9 | md:37 `甩头发既是挑衅也是掩饰` | `text/ch17_17.txt:26`：`…gave her a dirty look…and she was disappointed. Callie flicked her hair in her direction…` | **残留（提示级）**：「掩饰」无据，原文是轻蔑地一甩 | 提示 |
| 10 | md:110 `她只能一遍遍伸手去够那只点开邮箱却始终空着的 iPad` | `text/ch17_17.txt:23`（梅尔的回信、合同、NDA 都在她邮箱里）；`:50`／`:56`／`:83`（她反复点开邮箱找的是**欧拉莉亚那封**） | **残留（提示级）**：邮箱并非「始终空着」，空的是**那封没到的邮件**。md:52 已写对（`那封邮件在本章里始终没到`），此处口径不一 | 提示 |
| 11 | md:42 `从外面传出的咂嘴声判断，队伍已经排得挺长` | `text/ch17_17.txt:29`：`Judging by the tutting, quite a queue was forming outside.` | **残留（提示级）**：`Judging by` 的主语是卡莉（据咂嘴声**推断**出队），md 写成咂嘴声**从外面传出** | 提示 |
| 12 | md:30 `钱给得体面，她才好意思答应`（依据 `Mel had offered a handsome fee…`） | `text/ch17_17.txt:23`：`She checked her phone… as long as the fee was commensurate with the short deadline and wide scope of the project.`（本块引语止于 `[647,871]`）；`[872,959]`：`Mel had offered a handsome fee that Callie’s impostor syndrome was too proud to reject.` | **残留（提示级）**：分析依据的 `handsome fee` 一句在引语之外 → 引语选短 | 提示 |
| 13 | md:35 `顺手把头发朝那位女士的方向甩了过去` | `text/ch17_17.txt:26`：`A very serious-looking woman…gave her a dirty look…Callie flicked her hair in her direction…` | 该女士在引语**之前**的句子里（`[2050,2346]`），本块引语起点为 `[2346]` → 指代对象在引语外 | 提示 |
| 14 | 漏：原文 `She performatively flushed the empty toilet`（＝她其实没吐）未进 md | `text/ch17_17.txt:29` | **残留（提示级·漏）** | 提示 |
| 15 | 漏：欧拉莉亚的孤独／皇家音乐学院一层未进 md 分析 | `text/ch17_17.txt:83`：`Callie didn’t expect the world’s most mysterious pop girlie…to be lonely, let alone to see her as a source of comfort.` | **残留（提示级·漏）** | 提示 |
| 16 | 漏：怀孕／瞒着家人一层未进导航与总结 | `text/ch17_17.txt:23`：`Or rather than a beach holiday she should use some of the money on a good pram…how she’d tell her mother…` | **残留（提示级·漏）** | 提示 |
| 17 | md:11 `中途躲进洗手间`；md:56 `不确定自己会不会又要冲去洗手间去吐` | `text/ch17_17.txt:26`：`turned abruptly to find the loos`；`:29`：`the empty toilet`；`:83`：`unsure as to whether she was going to have to run to the loo to puke or not.` | **成立**（「又要」有据：她本章已进过一次洗手间） | 通过 |
| 18 | md:52 `那封邮件在本章里始终没到——欧拉莉亚说“我可以发给你”，随后发来的是餐厅地址和几张表情包` | `text/ch17_17.txt:47`：`‘I can email it to you.’`；`:83`：`She checked her email for the ‘thing’ that Eulalia had seen but nothing came through.`／`Her phone pinged with the address of a restaurant…Then came a meme. And another. And another.` | **成立**（说话人、先后、内容均对） | 通过 |
| 19 | md:13 等待线／工作线分列；md:24 `被女性化的盔甲`；md:58 `两个女王隔空并置`；md:12 `第三人称限知` | `:41` `‘I saw something interesting.’`；`:20` `Feminine or rather feminised armour.`；`:83` `the show about Eleanor of Aquitaine` | **成立** | 通过 |

### 修后机器层复跑

```
bash scripts/chapter.sh "notes/.../ch17 callie sketches elizabeth at the gallery" --json
  → 退出码 0；verdict "ok"；quotes 6/6 ok；counts: segment_miss 0 / struct_bad 0 / empty_quote 0 / keyword_bad 0 / cjk_low 0
  → form: h1 "17. The National Portrait Gallery"（h1_shape_ok=true）/ nav_count 5 / blocks 6 / block_median 7.0 / block_range [5,10] / profile mystery-thriller
```
**修后 R2 仍全绿，但残留阻断 2 条在 ch17 md 内 ＋ 1 条跨文件** —— 这正是「机器全绿不等于无缺陷」的实例：三处残留全是**语义层**（施事归属、时序、跨文件断言），四道机器探针结构上查不到。

---

## 三、本章专属判据的落点（任务书点名要核的三件事）

### 修前判定

| 判据项 | 原文依据 | md 写法（修前） | 判定 |
|---|---|---|---|
| 她等待与紧张时的动作 | `:26` `She’d suddenly started to feel a bit sick.`／`:29` `The wave of nausea seemed to abate and she stood up.`／`The nausea had returned…`／`:83` `unsure as to whether she was going to have to run to the loo to puke or not.` | `md:11`「胃却先开始**反酸**」；`md:13`/`md:110`「两次退下」；`md:11`「等消息的半个钟头里坐不住」 | **不通过**（反酸＝原文无；两次退下＝原文只有一次；坐不住＝原文写的是坐着画半小时） |
| 是否躲进洗手间 | `:26` `turned abruptly to find the loos`；`:29` `stared at the white porcelain bowl`／`performatively flushed the empty toilet` | `md:11`「中途躲进洗手间」；`md:35`「她猛地转身去找洗手间」 | **通过**（动作有据；「躲」属文学化用词，不判错） |
| 是否差点吐 | `:29` `not sure if she was going to be sick or not`／`didn’t want to puke`／`She’d rather have the taxi pull over and throw up on the side of the road`；`:83` `unsure as to whether she was going to have to run to the loo to puke or not.` | `md:56`「不确定自己会不会又要冲去洗手间去吐」；`md:110`「两次退下」 | 「差点吐」**通过**；「两次退下」**不通过**（章末那一次没退） |
| **「她等的那条消息」是什么、有没有写清楚** | 工作线 `:23` `Mel had replied…`（回信已到，合同＋NDA 已发来）；等待线 `:41` `‘I saw something interesting.’` → `:83` `nothing came through`（始终没到）；另 `:5615` 到的是餐厅地址＋三张表情图 | `md:13` 把工作线／等待线分开写；`md:52`「那封邮件在本章里始终没到——欧拉莉亚说“我可以发给你”，随后发来的是餐厅地址和几张表情包」 | **通过**（两条线未混淆，是本章最清楚的一处） |

### 修后判定（最终）

| 判据项 | md 修后写法 | 判定 |
|---|---|---|
| 她等待与紧张时的动作 | `md:11`「她的胃却先开始**发闷想吐**」（用词已对）；`md:13`/`md:110`「一次退下、一次卷土重来，章末悬而未决」（已对） | **部分通过**——症状词与消退次数已改对；但「等消息的半个钟头里坐不住」与「胃却先开始」的**时序与情境**仍在（§二bis #4，阻断） |
| 是否躲进洗手间 | `md:11`「中途躲进洗手间」；`md:35`「她猛地转身去找洗手间」 | **通过**（未动，成立） |
| 是否差点吐 | `md:56`「不确定自己会不会又要冲去洗手间去吐」；`md:110`「章末还没个了断」 | **通过**（修后成立；且不再出现「两次退下」） |
| **「她等的那条消息」是什么、有没有写清楚** | `md:13` 工作线／等待线分列；`md:52`「那封邮件在本章里始终没到」 | **通过**（未动，是本章最清楚的一处） |
| 附带 | 排队的人是谁（`md:14` 仍写「排着队的卡莉」） | **不通过**（§二bis #3，阻断） |

---

## 四、已核实为正确（防误修，勿据「读着不对」改动）

> 本节在**修后** md 上复核过：下列各条**修后仍然成立**，整改者未动，后续任何人不得改动。

1. **`md:21`／`md:23` 的「她并没有在临摹…只是挑选」** — 依据 `text/ch17_17.txt:20` `She wasn’t copying the image of the golden-age queen, she was just picking out the details that she liked.`：**成立**。注意这是**否定式**用法，与「摘要层把作者明写的否定翻过来」是相反方向——修摘要层时**不要**把这���处也一起改掉。
2. **`md:52` 关于餐厅地址与表情包的写法** — 依据 `text/ch17_17.txt:83` `Her phone pinged with the address of a restaurant that had a bit of a buzz to it. Then came a meme. And another. And another.`：**成立**，勿改。
3. **`md:13` 把工作线与等待线分开** — 依据 `text/ch17_17.txt:23`（梅尔回信已到）与 `:83`（`nothing came through`）：**成立**，勿合并。
4. **`md:56`「不确定自己会不会又要冲去洗手间去吐」的「又要」** — 她本章已进过一次洗手间（`:26` `find the loos`、`:29` `the empty toilet`），故「又要」有据，勿删。
5. **`md:58` 关于广播与画像两个女王的并置** — 依据 `:83` + `:20`：**成立**，勿删。
6. **`md:44`／`md:45` 修后写法** — `门外那队人照旧排着、照旧咂嘴，她把自己关在里面`／`那扇洗手间的门外还排着人`：与 `text/ch17_17.txt:29` 完全对上（她在门内、队与咂嘴在门外），**成立**，勿再动。
7. **本块引用 `‘OK then.’` 归给欧拉莉亚**（`md:51`「电话那头一句『好吧』」）— 依据 `text/ch17_17.txt:53`：`‘OK then.’` 确为欧拉莉亚所说，**归属正确**，勿改。
8. **修后 `md:13`／`md:110` 的「一次退下、一次卷土重来，章末未决」** — 依据 `text/ch17_17.txt:29`＋`:83`：**成立**，勿再动。

---

## 五、覆盖声明与取证记录

- **覆盖**：本章（ch17）全量人判（R1 素读 + R2 机器 + R3 三张单子 + R4 逐块 + R5 判定）。**全书其余 53 章只走了机器层**（`scripts/chapter.sh` 逐章，退出码 0/1/2 逐章记录），未做人判；总览三篇（`00_概述.md`/`00_情感节点.md`/`00_金句精选.md`）未做独立审查，仅在发现 ch17 断言外溢时核查了 `00_金句精选.md:96,98` 两行。**「只查了本章」不等于「全书通过」。**
- **R2 机器层命令与退出码**：
  ```
  python3 scripts/verify_corpus.py "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell"
    → P0-0 语料验收: PASS（FAIL 0 / WARN 3）；退出码 0
  bash scripts/chapter.sh "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch17 callie sketches elizabeth at the gallery" --json
    → 退出码 0；verdict "ok"；quotes 6/6 ok；counts: segment_miss 0 / struct_bad 0 / empty_quote 0 / keyword_bad 0 / cjk_low 0
  ```
  机器层全绿 **不等于** 无缺陷：`chapter.sh` 只管引语逐字、块清单、形态、中文密度，**管不了**施事归属、摘要层断言与「反酸」这类症状用词。
- **零命取证**（R5-补 要求贴命令与退出码）：
  ```
  /usr/bin/grep -n -iE "acid|reflux|heartburn|burn" text/ch17_17.txt
    → 无输出；退出码 1（本章原文确无「反酸」类词）
  /usr/bin/grep -n -i "corridor" text/ch17_17.txt
    → 无输出；退出码 1（原文无「走廊」）
  ```
  ⚠️ **本机 `/usr/bin/grep -o -E` 的多字节交替不可靠**（实测：`printf '反酸\n恶心\n' | grep -o -E "反酸|反胃|恶心"` 把两行都吐成「反酸」×2，把「恶心」行错标）。**故症状词计数一律用「逐词 `grep -o`（不加 -E）」+ Python 复算**，两条路径数字一致方采信：
  ```
  for w in 反酸 反胃 恶心 想吐; do echo "$w = $(/usr/bin/grep -o "$w" ch*.md | wc -l)"; done
    → 反酸 = 0   反胃 = 2   恶心 = 10   想吐 = 4        # 修后（ch17 md 已改「发闷想吐」）
  python3 逐文件 count 交叉复算（ch*.md）
    → {'反酸': 0, '反胃': 2, '恶心': 10, '想吐': 4}      # 与上完全一致
  ```
  修前同一口径为 `反酸 = 1`（仅 ch17 md:11）＋ `反胃 = 2`＋`恶心 = 10`＋`想吐 = 4`；`00_金句精选.md` 另有「反酸」×2（不在 `ch*.md` 内）。
- **本次未改动书目录任何 md，未 `git add`／`git commit`**；落盘仅限 `.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch17/`。
  （ch17 md 的整改由另一实例以 `fc89f7d9a`／`aa3fbb714` 完成，非本次审查所为；本审查的两轮判定均已如实留档。）


---

## §一ter / §二ter · 收口复核（2026-10-21，主会话接手后）

> 上面的 §一bis/§二bis 判的是 md5 `4364edbe…`（commit `aa3fbb714`）那个版本。**该版残留的 3 条阻断已在
> commit `0f9e866a8`（15:55）整改并入库**，故本节以**现版** md5 `1829fc1b8e7f08153f6197c6d742ef49` 为准。

### 残留三条的现状（逐条回当前 md 与原文核）

| 原残留 | 现 md | 原文依据 | 结论 |
|---|---|---|---|
| R1 md:14「到洗手间外**排着队**、只能对着空邮箱一遍遍伸手的卡莉」（施事/位置反转） | 改为「从展厅里从容挑细节、还能对路人甩一下头发的卡莉，到**关在洗手间里**、只能对着空邮箱一遍遍伸手的卡莉」 | `text/ch17_17.txt:29` `Judging by the tutting, quite a queue was forming outside.`——**队在外面排、人在里面** | ✅ 已修（与 md:44/45 口径一致） |
| R2 md:11「等消息的半个钟头里**坐不住**：合同的回音刚到，她的胃**却先**开始发闷想吐」（情境与时序倒置） | 改为「等消息的那半个钟头里**一直坐着画**：合同的回音刚到，她的胃**才**开始发闷想吐」 | `:20` `Callie had been sitting in front of a portrait of Elizabeth I for the last half an hour. She had her sketchbook out.`；`:23` 她先查手机见回信，`:26` 才犯恶心 | ✅ 已修（坐着画 ✓、回信在前恶心在后 ✓） |
| R3 跨文件：`00_金句精选.md:96,98` 的「反酸」断言 | 两处均改为「发闷／胃里发闷」 | 全书检索「反酸」＝**0 处**（`grep -rn "反酸" **/*.md` 无输出） | ✅ 已修（并已随金句精选入 git） |

### 顺带独立复核了被改写的那句身体线（结论：改得对）

现 md 写「恶心两次袭来：**一次退下、一次卷土重来，章末悬而未决**」。回原文逐处核：
`She'd suddenly started to feel a bit sick.`（起初犯恶心）→ `The wave of nausea seemed to abate and she stood up.`（**一次退下**）→
出租车上 `The nausea had returned`（**一次卷土重来**）→ 全章末句 `unsure as to whether she was going to have to run to the loo to puke or not`（**章末悬而未决**）。
⇒ **四拍全部对得上原文**，「一次退下、一次卷土重来、章末悬而未决」是准确写法（原「两次退下」才是错的）。

### 本章收口四组数（对现版 md5 `1829fc1b…`）

| 组 | 结果 |
|---|---|
| 逐字 | 6/6 引语逐字命中；30/30 词汇例句逐字命中；机器层 exit 0 |
| 对应 | **6/6 块成立**，阻断 0；提示 4（原句 2 引语选短、原句 3 措辞无据、原句 4 `Judging by` 方向、摘要层提示） |
| 形态 | H1 `17. The National Portrait Gallery`、导航 5 项、子项 4 项、块数 6 ∈ 5–10 ⇒ 0 偏离 |
| 断言 | 核 34 条：**阻断 5 → 0**（含上述 3 条残留）；提示 8 条只记不改（见 §二bis #8–#16） |

- **假红 0 · 跳过 0**。§二bis 第 8–16 行所列的 8 条提示型残留仍在 md 里，属措辞与可选覆盖，按规则只记不改。
