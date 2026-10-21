# 3-diff · ch30《The Police Station》对账（漏 / 编 / 错）

- 权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch30_30.txt`
- 被审 md：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch30 scott left a trail of coffee cups.md`
- 区间记法：`text/ch30_30.txt:行号` 与字符区间（整文件 4735 字符，见 1-suread.json）
- 落盘顺序：R1 素读 → 落盘 1-suread.json → R2 机器层 → 才开 md

---

## D1【错 · 说话人】导航「人物弧线」把凯厄斯的「Seconded（附议）」记到马特名下 —— **阻断**

- md 逐字（`ch30 scott left a trail of coffee cups.md:14`）：
  > - **人物弧线**：艾米一句「回应少得可怜」给整场搜寻定性；**马特**往冷笑话罐里投一枚硬币，**一句「附议」接住「凯厄斯的午餐是不是很色」**，同时又往坏处想，追问对面是不是专门猎捕脆弱男人的连环杀手；……
- 原文逐字（`text/ch30_30.txt:74` 与 `:77`，字符区间 4123–4317 与 4320–4646）：
  > ‘Put a quid in the tin,’ Matt said, gesturing to the ‘bad joke jar’ on his desk. Caius had implemented it after one too many low-quality puns. They were going to spend it on a meal at Christmas.
  >
  > ‘Seconded. A new round of “Is Caius’s Lunch Wanky?” resumes on Monday too.’ **Caius’s desk phone rang. He nodded along.** ‘Absolutely. Send the details over to my DS who will get in touch with the person who reported it. I’ll be along in twenty minutes.’ **He put the phone down and looked at Matt.** ‘Saddle up. There’s another one.’
- 判定依据：
  1. 原文该段说话人 = 接电话的人 = 凯厄斯：紧接引语后的叙述句是「Caius’s desk phone rang. He nodded along.」，答话「Send the details over to **my DS**」用的是第一人称所有格 my DS（凯厄斯的 DS），挂断后「**He** put the phone down and looked at **Matt**」——即说话人在听 Matt 说话；随后 `:80`（字符 4649–4712）才是 Matt 开口：「‘Another break-in on Priory Square?’ Matt got up from his seat.」
  2. 「Seconded（附议）」附议的是上一句马特的「Put a quid in the tin」；马特不可能附议自己刚投的那枚硬币。
  3. 「Is Caius’s Lunch Wanky?」这一轮被宣布「周一重开」，与 md 的写法「附议接住『凯厄斯的午餐是不是很色』」也接不上：接在后面的不是回应，而是另一件事（新一轮）。
- 判据：R3「错」中的「主语 / 说话人」；R4 固定追问「每个动词的主语是谁」。
- 另附：md 把「马特桌上那罐坏笑话」写在 `md:15` 是**对的**（原文 `text/ch30_30.txt:74`「the ‘bad joke jar’ **on his desk**」，his = Matt），请勿连坐修改。

---

## D2【漏 · 数量】「每班正好三十个杯子」未进 md —— 提示

- 原文逐字（`text/ch30_30.txt:41`，字符区间 1413–1496）：
  > ‘Yep, he was giving out **exactly thirty cups per shift** and recording the responses.’
- md 全篇检索结果（`/usr/bin/grep -n -oE "十三|十六|三十|thirteen|sixteen|thirty" "ch30 scott left a trail of coffee cups.md"`）：
  > 11:十三　19:thirteen　19:sixteen　21:十三　21:十六　23:thirteen　25:十三　25:十六　115:sixteen　116:thirteen　116:十三　116:thirteen
  > → **无「三十 / thirty」**（退出码 1）
- 说明：md 已写对「十三袋垃圾」「十六次尝试」，但第三章专属判据要求核的**杯子数量**（三十杯/班）缺失。原文的数字是三个（thirteen bin bags / sixteen attempts / thirty cups per shift），md 只承载了两个。
- 档位说明：此条不是**写错数量**，是**非关键细节的遗漏**，不触发 R3「关键事件/转折未出现」的阻断条款，故记为**提示**；但它同时是 D3 的成因（见下）。

---

## D3【漏 / 引语选短】原句 3 的分析用到了引语之外的句子 —— 提示

- md 逐字（`md:45`）：
  > **为什么这样写**：把求爱写成「实验」、把回应写成数据，这是斯科特自己的框架；……
- 引语逐字（`md:39`，机器定位 pos 1436，`text/ch30_30.txt:44`，字符 1499–1623）：
  > ‘Which were few and far between?’ Amy said. She didn’t need to see Scott’s write-up of his ‘experiment’ to know the outcome.
- 句外依托（`text/ch30_30.txt:41` 与 `:47`）：
  > ‘Yep, he was giving out exactly thirty cups per shift and **recording the responses**.’
  > ‘He’s used **PowerPoint to create graphs of his findings**,’ Caius said.
- 判定：「把回应写成数据」的**字面锚点**（recording the responses / graphs of his findings）在**引语之外**；引语本身只有「write-up of his ‘experiment’」与「the outcome」。属 S2「截短」— 引语选短了（分析覆盖的原文比引语长）。
- 档位：提示（方向未错、数据未错；只是分析超出引语范围）。若与 D2 合并修，可一并把 `:41` 那句纳入引语或补写进中文理解。

---

## D4【编 · 场景细节】读者视角提示里的「物证袋」原文无 —— 提示

- md 逐字（`md:57`）：
  > **读者视角提示**：……杯子正躺在警局的物证袋里，帖子正摊在凯厄斯的屏幕上。
- 原文逐字（`text/ch30_30.txt:20`，字符 41–511）：警方是在警局里翻检「the crumpled napkins and soggy paper cups」，**未出现**「物证袋 / evidence bag」字样。
- 说明：「物证袋」是合理的场景想象，非情节/关系/数字凭空出现，故不判阻断；同句「帖子正摊在凯厄斯的屏幕上」有据（`text/ch30_30.txt:62`「closing the lid on Scott’s **laptop**」＝帖子在笔记本上）。

---

## D5【核过 · 不算缺陷】md:14 之外的「视角」归属 —— 跳过

- md 逐字（`md:12`）：「艾米翻杯子与记录，凯厄斯翻手机与论坛帖子，马特在旁追问或调侃」。
- 原文（`text/ch30_30.txt:20`）：翻检杯/餐巾纸的主语是复数「**They** were now poring over」；艾米的具体动作是派 uniform、说过「they’d counted sixteen attempts」。
- 判定：md 把警局团队的共同动作记在艾米名下，属概略归属；艾米另有派警与计数两处具体动作，不构成与原文冲突，不判缺陷。**记为跳过（已核，不改）**。

---

## D6【无法从语料判定】导航里的「分部 A THURSDAY IN MAY」 —— 跳过

- md 逐字（`md:11`）：「在分部「A THURSDAY IN MAY」里……」
- 取证命令与输出：
  ```
  /usr/bin/grep -ril "thursday in may" text/
  → （无输出）
  退出码 1
  ```
  全书 text/ 内**无任何分部标题行**（`/usr/bin/grep -rhoE "^[A-Z][A-Z ]{6,}$" text/` → 无输出），说明分部名在提取件里根本不存在，md 的该说法来自原书结构而非本章语料。
- 判定：语料内不可核 ⇒ 只能记「未核」，不判阻断。

---

## D7【核过 · 数量写对】三处已写出的数字与原文逐字一致 —— 已核实为正确

| md | md 逐字 | 原文逐字 | 位置 |
|---|---|---|---|
| `md:21` | 一名倒霉的法证技术员带回**十三袋垃圾**，光第一袋就数出**十六次尝试** | a poor forensics technician returned with **thirteen bin bags** full of rubbish. So far they’d counted **sixteen attempts** in the first bag alone. | `text/ch30_30.txt:20`（字符 41–511） |
| `md:25` | 把示爱的规模量化成可以清点的数目：**十三袋垃圾、十六次尝试** | 同上 | `text/ch30_30.txt:20` |
| `md:23` | 关键词 `thirteen bin bags` | thirteen bin bags full of rubbish | `text/ch30_30.txt:20` |

⇒ **md 没有写错任何数量**；问题只在 D2（漏了「三十杯/班」）。

---

## 三张单子小结

| 单子 | 条数 | 阻断 | 提示 | 跳过 |
|---|---|---|---|---|
| 漏 | 2（D2 三十杯/班、D3 引语选短） | 0 | 2 | — |
| 编 | 1（D4 物证袋） | 0 | 1 | — |
| 错 | 1（D1 说话人）＋2（D5 视角概略归属、D6 分部名） | **1** | 0 | 2 |
