# R5 判定表 · A Fatal Legacy ch17《The National Portrait Gallery》

> 唯一权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch17_17.txt`（6,133 字符）
> 被审 md：`.../ch17 callie sketches elizabeth at the gallery.md`
> 档位：**阻断**（与原文不符/缺失）｜**提示**（措辞正当）｜**假红**（工具判错）｜**跳过**（没查）
> 逐条「阻断」均附 `text/<file>:<行>` 与该处原文逐字（R5 硬约束）。

---

## 一、四组数（只报这四组）

| 组 | 数 | 说明 |
|---|---|---|
| **逐字** | **6/6 通过**（引语）＋ **30/30 通过**（词汇例句） | 6 块引语全部是原文的**连续**子串（Python `str.find` 独立复算，与 `chapter.sh --json` 的 6/6 一致），无 `…` 缝合、无跨话轮拼接；30 条词汇例句 30/30 命中本章原文 |
| **对应** | **5/6 通过**，**1 阻断** | 6 块逐块人判：原句 4 因施事反转 + 自相矛盾判阻断；原句 2、3 各带提示（引语选短 / 措辞无据） |
| **形态** | **通过，0 偏离** | H1 `17. The National Portrait Gallery`（合原文标题、合本书 `# NN. 标题`）；导航 5 项 = 全书 54 章同名同序（`一句话概括/视角/线索结构/人物弧线/叙事手法`）；子项集 = profile 要求的 `中文理解/关键词/为什么这样写/读者视角提示`（未用 optional `句子结构`）；块数 6 = 全书出现最多的块数（19/54），落在众数区间 [5,10] 内，中位 7 → **无偏离，不需写理由** |
| **断言** | **阻断 5 条 ＋ 提示 8 条** | 详见下表 |

**阻断型条数：5**（W1 临摹、W2 两次退下、W3 排队施事反转、C1 反酸、原句 4 对应阻断＝与 W3 同一处，不重复计）

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

## 三、本章专属判据的落点（任务书点名要核的三件事）

| 判据项 | 原文依据 | md 写法 | 判定 |
|---|---|---|---|
| 她等待与紧张时的动作 | `:26` `She’d suddenly started to feel a bit sick.`／`:29` `The wave of nausea seemed to abate and she stood up.`／`The nausea had returned…`／`:83` `unsure as to whether she was going to have to run to the loo to puke or not.` | `md:11`「胃却先开始**反酸**」；`md:13`/`md:110`「两次退下」；`md:11`「等消息的半个钟头里坐不住」 | **不通过**（反酸＝原文无；两次退下＝原文只有一次；坐不住＝原文写的是坐着画半小时） |
| 是否躲进洗手间 | `:26` `turned abruptly to find the loos`；`:29` `stared at the white porcelain bowl`／`performatively flushed the empty toilet` | `md:11`「中途躲进洗手间」；`md:35`「她猛地转身去找洗手间」 | **通过**（动作有据；「躲」属文学化用词，不判错） |
| 是否差点吐 | `:29` `not sure if she was going to be sick or not`／`didn’t want to puke`／`She’d rather have the taxi pull over and throw up on the side of the road`；`:83` `unsure as to whether she was going to have to run to the loo to puke or not.` | `md:56`「不确定自己会不会又要冲去洗手间去吐」；`md:110`「两次退下」 | 「差点吐」**通过**；「两次退下」**不通过**（章末那一次没退） |
| **「她等的那条消息」是什么、有没有写清楚** | 工作线 `:23` `Mel had replied…`（回信已到，合同＋NDA 已发来）；等待线 `:41` `‘I saw something interesting.’` → `:83` `nothing came through`（始终没到）；另 `:5615` 到的是餐厅地址＋三张表情图 | `md:13` 把工作线／等待线分开写；`md:52`「那封邮件在本章里始终没到——欧拉莉亚说“我可以发给你”，随后发来的是餐厅地址和几张表情包」 | **通过**（两条线未混淆，是本章最清楚的一处） |

---

## 四、已核实为正确（防误修，勿据「读着不对」改动）

1. **`md:21`／`md:23` 的「她并没有在临摹…只是挑选」** — 依据 `text/ch17_17.txt:20` `She wasn’t copying the image of the golden-age queen, she was just picking out the details that she liked.`：这两处**是对的**，修 W1 时不要动它们。
2. **`md:52` 关于餐厅地址与表情包的写法** — 依据 `text/ch17_17.txt:83` `Her phone pinged with the address of a restaurant that had a bit of a buzz to it. Then came a meme. And another. And another.`：**成立**，勿改。
3. **`md:13` 把工作线与等待线分开** — 依据 `text/ch17_17.txt:23`（梅尔回信已到）与 `:83`（`nothing came through`）：**成立**，勿合并。
4. **`md:56`「不确定自己会不会又要冲去洗手间去吐」的「又要」** — 她本章已进过一次洗手间（`:26` `find the loos`、`:29` `the empty toilet`），故「又要」有据，勿删。
5. **`md:58` 关于广播与画像两个女王的并置** — 依据 `:83` + `:20`：**成立**，勿删。
6. **导航「一句话概括」中「合同的回音刚到」** — 方向对（Mel 回复、`fee commensurate`），只是到达时刻原文没给；改写建议只动时序词，勿整句推翻。
7. **本块引用 `‘OK then.’` 归给欧拉莉亚**（`md:51`「电话那头一句『好吧』」）— 依据 `text/ch17_17.txt:53`：`‘OK then.’` 确为欧拉莉亚所说，**归属正确**，勿改。

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
  /usr/bin/grep -h -o -E "反酸|反胃|恶心|想吐|犯恶心|胃里翻" ch*.md | sort | uniq -c
    → 16 反酸（全部在本章与 00_金句精选.md）；0 反胃；0 想吐；0 犯恶心；0 胃里翻
       —— 全书 54 章 md 的症状词表里只有「恶心」，「反酸」是本章与总览独有的用词
  /usr/bin/grep -n -i "corridor" text/ch17_17.txt → 无输出；退出码 1
  ```
- **本次未改动任何 md，未 `git add`／`git commit`**；落盘仅限 `.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch17/`。
