# ch09 人工审查 · R5 判定表

- 审查对象：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch09 chapter 9.md`
- 唯一真值：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch09_chapter_9.txt`（21 行 / 474 字符 / `wc -w` = 78 / 6 自然段）
- 配套文件：`review/ch09/1-suread.json`（R1 素读）、`review/ch09/2-machine.json`（R2 机器层，EXIT=0）、`review/ch09/3-diff.md`（R3 三单＋R4 逐块）
- 审查人：DSH-Mac ｜ 本轮只出指令不改稿

## 判定表

| # | 断言 | 证据(章:区间) | 结论 | 档位 |
|---|---|---|---|---|
| B1 | 原句 3 的「为什么这样写」把 P3/P5 的发言人写成「电话那头」，并称该句「在整通电话里原样说了两遍」（md:49） | ch09 text:6 `“I have to call you back,” she said, almost to herself, sliding the iPhone into her pocket.`；text:9 与 text:15 `“They can’t find Alba.”` | 通话在 P2 末即结束（她说完把手机滑进口袋），两处同句只能是现场对话；且与 md:37「为什么**被挂断**」自相矛盾 → 归属反转 | 阻断 |
| B2 | 原句 4 的中文理解「**她**追问，这句话到底什么意思」（md:57） | ch09 text:12 `“What?” Carlos asked, still covering Diana with the coat.`；text:18 `“What do you mean they can’t find Alba?”`；文体惯例 `text/ch08_chapter_8.txt:261`↔`:263`、`:216` | 问话人应为 Carlos、被问者为 Diana（未标说话人的行按「在场另一方应答」交替）；md 把被问者当问话人 | 阻断 |
| B3 | 原句 5 的中文理解「**对方**说，妈妈刚说 Alba 不见了」（md:69） | ch09 text:18、text:21 `“Mom just said Alba is missing.”`；`text/ch08_chapter_8.txt:102` `My mom.` | P7 是对 P6 的回答：说话人＝Diana、对象＝Carlos；md 把听的人当说的人 | 阻断 |
| B4 | 导航 1/2/4 与一句话总结沿用同一归属模型，并断言「Carlos 全程只有一个「什么？」」（md:11、md:12、md:14、md:106） | ch09 text:12 与 text:18（Carlos 本章有**两**句台词）；text:6（电话已结束） | B1–B3 的下游复述；「Carlos 只有一句」与原文直接冲突的事实断言 | 阻断 |
| T1 | 「紧接着**丈夫**用一个字的疑问打断」（md:49） | ch09 text:12；全书英文称 Diana 的伴侣为 partner：`text/ch01_chapter_1.txt:12` `Her partner was going to be in Madrid all day`、`text/ch05_chapter_5.txt:540` `his partner’s family`、`text/ch10_chapter_10.txt:894` `his partner and his mother-in-law`；`grep -nw husband` 全书命中均为 Juan／Carmen 亡夫／bingo 女人们的丈夫 | 关系用词与原文用词不符；但 `text/ch10_chapter_10.txt:879` `Carlos raised his voice to his mother-in-law` 保留已婚读法 ⇒ 建议改「伴侣」，不判阻断 | 提示 |
| T2 | 「被一句**五个词**的短句拽成惊惶的追问者」（md:14） | ch09 text:9／text:15 `“They can’t find Alba.”`；`printf "They can't find Alba.\n" \| wc -w` = 4 | 标准分词为 4 词（`can’t` 拆成 can+not 才得 5）⇒ 计数口径歧义，非情节事实错，建议改「四个词」 | 提示 |
| T3 | 「全章只有六个自然段，其中**一半**是纯对白」（md:15） | ch09 text 自然段 6 ✓；纯对白段 4（P3/P5/P6/P7）、含叙述段 2（P2/P4） | 「六个自然段」✓；「一半」应作「四段／三分之二」 | 提示 |
| T4 | 「偏偏她的语气还很不耐烦」（md:25） | ch09 text:6 `unconcerned that her hand was covered in blood` | unconcerned＝漠不关心／毫不在意，非「不耐烦」；且与本块自己的中文理解 md:21「一点也不为那手上的血担心」矛盾 | 提示 |
| T5 | 「语法上是一个规整的**反问**」（md:61） | ch09 text:18 `“What do you mean they can’t find Alba?”` | 是信息询问句（要求解释），不是反问句；术语用词不准 | 提示 |
| T6 | 「恐惧**第一次**不在她身上」（md:12） | `text/ch08_chapter_8.txt:216` `“No. I don’t know what’s happening. But I think my stomach is bleeding.”` | 「第一次」缺逐字支撑：上一章 Diana 的恐惧已在自己身上；全书级断言建议弱化为「这一次」 | 提示 |
| T7 | md:37「为什么**被挂断**」与 md:49「在整通电话里…两遍」并存 | ch09 text:6 | 二者不能同真；本项仅提示「改稿时须先统一口径」，判定归 B1 | 提示 |
| F1 | 5 块引语长度 23/23/9/8/6 词，低于创建卡建议的 30–70 词 | ch09 text 全文 78 词 | **已知例外**：原文太短，不可能达到 30 词。真实判据（逐字／单段落／块序＝原文顺序／编号连续）四项全过 ⇒ 不判缺陷 | 假红 |
| F2 | 原文 text:9 与 text:15 逐字相同（`“They can’t find Alba.”`），md 引语层只引一次 | ch09 text:9／text:15；md:19–75 | 结构审计按「唯一命中」会判「不可判定」；md 有意只引一次、另一处改为分析文字复述「原样说了两遍」（md:49）⇒ **次数复述忠实原文**，非「重复块」缺陷 | 假红 |
| F3 | 机器层 `chapter.sh` EXIT=0、issues 五类全空 | `review/ch09/2-machine.json` | 本章 5 块引语**确实** 5/5 整串逐字命中（自跑比对：text[6:146]／[147:283]／[312:369]／[398:438]／[441:473]）⇒ 该绿灯为真；但机器只比 52 字符指纹、覆盖不到引语尾部，**不可用它替代逐字判定**（本轮的阻断均出自机器层之外） | 假红 |
| S1 | 「全书弧线最陡的一次下坠」「全书最低的那段路」（md:12、md:106） | — | 全书级解读断言，无逐字判据，不判 | 跳过 |
| S2 | 「报信的人平静得像在报天气」（md:13） | ch09 text:21 `“Mom just said Alba is missing.”` | 修辞性判断；「转述」这一行为本身有原文支撑，不判 | 跳过 |
| S3 | 引语长度是否落在 30–70 词建议区间 | — | 见 F1：已知例外，跳过 | 跳过 |

**判定表行数：17**（阻断 4 / 提示 7 / 假红 3 / 跳过 3）

## 四组报数

| 组 | 计数 | 明细 |
|---|---|---|
| 逐字 | **5/5 块命中，0 缺陷** | 整串 flat 比对：原句1 text[6:146]、原句2 text[147:283]、原句3 text[312:369]、原句4 text[398:438]、原句5 text[441:473]；词汇例句 11/11 逐字命中 |
| 对应 | **5 块中 2 块全对应，3 块有归属/事实不符** | 干净：原句 1、原句 2；缺陷：原句 3（为什么这样写半块）、原句 4（中文理解说话人）、原句 5（中文理解说话人） |
| 形态 | **8 项全过 ＋ 1 项已知例外** | frontmatter／H1／导航 5 项／子项 4 项／块数 5（在众数 7、range 5–8 内）／编号 1–5 连续／块序 6→147→312→398→441 与原文一致／引语单段落、无 `…` 缝合、无跨话轮拼接；例外：引语长度（见 F1） |
| 断言 | **核 9 条：5 条成立、1 条提示、4 条措辞级提示** | 成立：Alba＝家人（`text/ch10_chapter_10.txt:207` `It was the same with Diana and her sister`）、Alba 失踪（`text/ch10_chapter_10.txt:6` `Alba was missing.`）、「强迫症患者」（`text/ch10_chapter_10.txt:432` `She was pathologically obsessed with order`）、Carlos 盖外套（`text/ch08_chapter_8.txt:279` `cover me up with the coat for a minute`）、母亲＝Carmen（`text/ch08_chapter_8.txt:102` `My mom.`）；提示：丈夫＝partner（T1）、五个词（T2）、一半纯对白（T3）、不耐烦（T4）、反问（T5）、恐惧第一次（T6） |

## 「阻断」级清单（4 条）

1. **断言**：原句 3 的「为什么这样写」称 Alba 那句出自「电话那头」且「在整通电话里原样说了两遍」。
   **证据区间**：ch09 text:6 / text:9 / text:15（md:49）。
   **为什么阻断**：原文 P2 末 `sliding the iPhone into her pocket` 表明通话已结束，两处同句只能是现场对话；该归属还与 md 自身 md:37「被挂断」直接矛盾，属「句子通顺、引语逐字、中文是中文」但「谁对谁做了什么」反了——四道机器探针全绿只能靠 R4 固定三问抓出。
2. **断言**：原句 4 的中文理解「她追问」。
   **证据区间**：ch09 text:12、text:18；文体惯例 `text/ch08_chapter_8.txt:261`↔`:263`、`:216`。
   **为什么阻断**：问话人应为 Carlos、被问者为 Diana，md 把被问者当问话人（说话人错配）。
3. **断言**：原句 5 的中文理解「对方说」。
   **证据区间**：ch09 text:18、text:21；`text/ch08_chapter_8.txt:102`。
   **为什么阻断**：末句是对 P6 的回答，说话人是 Diana、对象是 Carlos，md 把听的人当说的人（说话人错配）。
4. **断言**：导航 1/2/4 与一句话总结的归属模型及「Carlos 全程只有一个「什么？」」。
   **证据区间**：ch09 text:12 与 text:18（Carlos 本章两句台词）、text:6（电话已结束）；md:11/12/14/106。
   **为什么阻断**：前三条的下游复述；且「Carlos 只有一句」是与原文直接冲突的事实断言，须同批修。

**改稿方向（仅指令，不改稿）**：以 §3-diff.md §3.1 的归属链为准——P3＝Diana、P4＝Carlos、P5＝Diana、P6＝Carlos、P7＝Diana；来电者原文始终未点名；母亲＝消息来源（转述者），既非本章说话人也非失踪者。md 的原句 3/4/5 三块与导航 1/2/4、一句话总结须按此统一改写；「丈夫」改「伴侣」；「五个词」改「四个词」；「一半是纯对白」改「四段是纯对白」；「不耐烦」改「漠然／毫不在意」；「反问」改「追问式的问句」；「恐惧第一次」改「这一次」。

## 已核实为正确

> 以下写法「读着像错」，核对后成立，后续不得以「读着不对」为由改动。

1. **5 块引语全部逐字**：整串 flat 比对 5/5 命中（text[6:146]／[147:283]／[312:369]／[398:438]／[441:473]），含 `“Hello,”` 的弯引号、`didn’t respond` 的撇号、`iPhone` 等全部细节一致。机器层 EXIT=0 在「引语逐字」这一项为真。
2. **引语长度 6–23 词低于建议区间**：原文仅 78 词，本章 5 块不可能达到 30 词，属**已知例外**，不是「选引语选得太短」的缺陷。
3. **原文两段逐字相同（text:9／text:15）而 md 只引一次**：引语层只收一次、另一处放在分析文字里复述「说了两遍」，是正确处置，不是「漏引」也不是「重复块」。
4. **原句 3 的中文理解施事/受事方向正确**：主语 Carlos、受事 Diana（`covering Diana with the coat`）、`still`＝「还在」，与 text:12 一致——错的只是同一段「为什么这样写」里的说话人归属。
5. **原句 2 的中文理解逐项对应**：「说了声你好／听了一会儿／没有回答／现在得回拨／把手机塞回口袋／像是在对自己说」六项全部落在 text:6 之内；`almost to herself` 的释义方向正确。
6. **把「电话是谁打来的」留作悬念**（md:39）：原文对来电者不点名，md 也未补成事实，符合「留白不臆造」。
7. **末句收口没读成「母亲失踪」**：md 一律把「妈妈」当转述者/消息来源，`Alba 不见了` 才是缺失项（md:69/73/75/106）；有 `text/ch10_chapter_10.txt:6` `Alba was missing.` 与 `text/ch10_chapter_10.txt:207` `It was the same with Diana and her sister` 支撑。
8. **「Alba ＝ 家人」成立**：ch10:207 明写 Diana 与 Alba 是姐妹；「危险从 Diana 身上挪到家人身上」的方向与原文一致。
9. **「强迫症患者」成立**：`text/ch10_chapter_10.txt:432` `She was pathologically obsessed with order` ＋ ch09 text:6 `She stopped examining herself` 双向支撑。
10. **「手上沾的是自己的血」成立**：`text/ch08_chapter_8.txt:222` `there was blood all over her fingers`、`:231` `she examined her abdomen`（自己的腹部伤口）。
11. **词汇表 11 条例句全部是原文逐字连续片段**，无生造词条、无跨标签拼接；`missing` 例句 `Mom just said Alba is missing.` 与 text:21 一致。
12. **形态八项全过**：frontmatter 三字段与同书 18 章一致；H1 `# 09. Chapter 9` 合众数；导航 5 项、子项 4 项（中文理解／关键词／为什么这样写／读者视角提示）齐备；编号 1–5 连续；块序与原文顺序一致；每块引语单段落、无 `…` 缝合、无跨话轮拼接。
