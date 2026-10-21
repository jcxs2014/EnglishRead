# R5 判定表 · ch35《A Fatal Legacy》

- 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch35 peter simpson calls on callie.md`
- 唯一权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch35_35.txt`（14455 字符）
- 机器层：`2-machine.json`（`bash scripts/chapter.sh "<md>" --json`，退出码 **0**，verdict=ok，无报警）
- 铁律执行：R1 素读先于开 md（`1-suread.json` 已先行落盘），本表写于其后。
- 证据一律 `text/<file>:<行>` + 该处原文逐字。

## 0. 覆盖声明

- 本次只审 **ch35**（分派范围）。本书共 54 章 md，**其余 53 章只有机器层，本报告不写「通过」**。
- 本章 md 的 9 条引语**全部落在 ch35 语料内**（自建逐字核对：9/9 在 `text/ch35_35.txt` 中连续命中），无跨章搬句 ⇒ 跨章归属（`check_crossref`）本章不适用。
- 未查：总览三篇（`00_*.md`）、其他章 md 的摘要层断言（超出分派范围）；本章 md 内未出现跨章引用。
- 机器层零报警 ⇒ 本次**无假红候选**；另见 §4「机器口径提示」一条（JSON 显示截断，非引语缺陷）。

## 1. 本章专属判据的核对结果

| 判据 | 结论 | 证据 |
|---|---|---|
| 来访者身份＝Peter Simpson | **成立**（md 的「彼得·辛普森」正确，原文本章只给名，姓氏由本书语料人物表给出） | `text/xx_characters.txt`：「the disgraced MP and fast-fashion tycoon Peter Simpson」；`text/ch08_08.txt:20`：「Peter, her biological father, had made his fortune exploiting female garment workers in developing countries」 |
| 他与 Callie 的关系（原文一句直接说明） | 原文＝`text/ch35_35.txt:104-110`：「‘What? You’re my only daughter, aren’t you?’ / ‘Am I?’ / ‘Biologically speaking.’」＋`:20`「Callie opened the front door to her father.」＋`:212`「‘Bye, Dad,’ Callie called after him」。**md 的父女框架方向正确、未写反**（导航`:11`、`:14`、一句话总结`:130` 均作「父亲／爸」）；但这条直接说明与 Callie 的反问「Am I?」**整段未被 md 引用或分析** ⇒ 判「漏」＝阻断（见 A3） | `text/ch35_35.txt:104-110` |
| 两个「Peter」之间的不适（她一叫名字对方的神色） | 原文＝`text/ch35_35.txt:23`「She went to call him Peter but he got funny when he did, despite that being the name she’d called him for 97 per cent of her life」。**md 原句 1 处理正确**（`:21`、`:23`）。注意：Peter 是她**一生 97% 都在用的名字**（习惯／本能），别扭来自**对方的反应**——md 原句 6 却把同一个称呼称作「生分的名字」，与原句 1 自相矛盾 ⇒ 提示（A12/W3） | `text/ch35_35.txt:23` |
| 客人在屋里留下的痕迹 | 原文可核的痕迹＝① 放在 coffee table 上的 file（`text/ch35_35.txt:38`）② 一口没碰的茶（`:215`，后由凯厄斯倒掉 `:245`）③ 卡莉交给他的那页 notes（`:194`，**他带走了一件东西**）。md 总结列了①②✔，遗漏③，且原句 7 写「他留下的**唯一**实物」与总结里的「茶几上的文件」自相矛盾 ⇒ 提示（A14/W8） | `text/ch35_35.txt:38`、`:194`、`:215`、`:245` |

## 2. 四组数

| 组 | 口径 | 结果 | 缺陷 |
|---|---|---|---|
| **逐字** | md 内全部引语（9）+ 全部词条例句（31） | **40 / 40** 逐字命中；引语均为**单一连续片段**，无省略号缝合、无跨段拼接（自建独立核对：9 条在源文件中连续命中，跨度 38–328 字符）；词条例句 31/31 命中且**仅命中 1 次** | **0** |
| **对应** | 逐块「这段中文是不是在讲这句引语」 | **9 / 9 对应**；不对应 0；密度不足 0；**引语选短 1**（原句 9，提示级） | 对应层 0 阻断；另在原句 8 查出 **2 处人物/施事错**（计入断言组） |
| **形态** | H1 / 导航项名与项数 / 子项集 / 块数 vs 本书众数与 profile | H1 `# 35. Caius and Callie’s Flat`＝`N.` 写法（本书 54/54）；导航 5 项，项名 `一句话概括/视角/线索结构/人物弧线/叙事手法` 与众数逐字同；子项 4 项 `中文理解/关键词/为什么这样写/读者视角提示` 与众数及 profile（mystery-thriller）同（optional「句子结构」未用，不计偏离）；块数 **9**，中位 7.0、范围 5–10，**在范围内** | **0 偏离**（无偏离 ⇒ 无需写理由） |
| **断言** | 本报告共判定 **18** 条 | 阻断 **3** · 提示 **15** · 假红 **0** · 跳过 **0** | — |

## 3. 判定表（断言 | 证据 | 结论 | 档位）

| # | 断言 | 证据（章:区间／逐字） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | 原句 8 的「反正都是我们的」是**卡莉**说的 | md `:72`：「卡莉那句“反正都是我们的”是句自嘲」；原文 `text/ch35_35.txt:227-234`：「‘I’ve been taken off the case I was working on.’ / ‘What happened?’ / ‘The series of crimes happened on a square that my dad partially owns, something about leaseholds. I don’t know. It’s ours anyway.’」——该句说话人是**凯厄斯**（`:227` 他报被撤案→`:230` 卡莉问→`:233` 凯厄斯答）；md 自己在同块中文理解 `:70` 也写「凯厄斯说」 | 说话人错配，且块内自相矛盾 | **阻断** |
| A2 | 那个部分持有广场的人＝**彼得** | md `:73`：「彼得在这宗案子里不是无关的人」；原文 `text/ch35_35.txt:233`：「my dad partially owns」（说话人=凯厄斯 ⇒ **凯厄斯的父亲**）；同章 `text/ch35_35.txt:182`：「‘We were just talking about your dad’s wool problem.’」（「your dad」＝凯厄斯之父）；`text/xx_characters.txt`：「He is the son of pragmatic Jamaican-British builder MARCUS BEAUCHAMP」；`text/ch08_08.txt:20`：「Peter, her biological father, had made his fortune exploiting female garment workers…」 | 施事/归属反转（产权人张冠李戴）；原文从未把该广场与彼得挂钩 | **阻断** |
| A3 | 父女关系的那段直接说明（「你是我的女儿／我是吗／从生物学上说」）及其反问，md 已覆盖 | md 全文无此内容（引语只到 `:40` 的「Not this again」起；`:45` 只提到 `:98`「你不是辛普森吧」）；原文 `text/ch35_35.txt:104-110`：「‘What? You’re my only daughter, aren’t you?’ / ‘Am I?’ / ‘Biologically speaking.’」；`text/ch35_35.txt:119-122`：「‘There’s no point in me changing my name.’ She regretted saying that as soon as it flew out of her mouth. / ‘Oh really?’ Peter caught the subtext.」；`:20`「Callie opened the front door to her father.」 | **漏**：关键节拍（父亲带限定词地认领＋女儿当场质疑自己是不是＋说漏嘴的拒改姓）未出现，md 把该场写成「他索姓／她一句『又来了』挡回去」的单向结构 | **阻断** |
| A4 | 原句 3 里彼得忌惮凯厄斯的成因，原文只给了「势利」一条 | `text/ch35_35.txt:41`：「This was partially due to how they had first met, but mostly due to Peter’s snobbery.」；md `:37` 只讲「怕对方那套用不着他会的东西」 | 漏一半成因（部分成因未提） | 提示 |
| A5 | 本章末尾「不能叫 Caius『Daddy』了」这一句应进入分析 | `text/ch35_35.txt:362-365`：「‘I don’t think I can call you Daddy any more. Not like that anyway.’ / ‘I suppose not.’…」；md 导航 `:14`、总结 `:130` 只处理「Peter／Dad」 | 漏本章落点（称呼线索被搬向下一代） | 提示 |
| A6 | 导航「要他亲自去**自己的**血汗工厂查账」 | `text/ch35_35.txt:137`：「all the places where **your brands had factories** working for them」——工厂是彼得的；md `:14`「自己的」主语为卡莉 | 主客易混 | 提示 |
| A7 | 原句 6：「关上门、人走远之后才是那声『爸』」／导航「人已经走远、门已经关上」 | `text/ch35_35.txt:209-212`：「He turned around and waved goodbye from the bottom of the path. / ‘Bye, Dad,’ Callie called after him, shutting the door.」——喊与关门**同时**，且是对着已转身的彼得喊 | 时序错一步 | 提示 |
| A8 | 原句 6：「她要等没有人的时候才叫得出来」 | 原文 `text/ch35_35.txt:212` 出声喊「Bye, Dad」；凯厄斯全程在屋（`:215`「‘He didn’t touch his tea,’ Caius said.」）；彼得在小径尽头（`:209`） | 与在场事实不符 | 提示 |
| A9 | 原句 6：「门口是**生分的**名字」 | `text/ch35_35.txt:23`：「the name she’d called him for 97 per cent of her life」——Peter 是她一生常用的名字；md 原句 1 `:21` 同时称其「本能地叫出」 | 块内互相矛盾（生分 ↔ 本能）；原文支持后者 | 提示 |
| A10 | 原句 4：「理由是他们那段关系刚上过头版小报」 | `text/ch35_35.txt:101`：「Peter had tried the other month to get Callie to change her surname to his **now that** their relationship had briefly been a tabloid headline」——`now that` 是时间状语，不是动机 | 时间状语被改写成因果动机 | 提示 |
| A11 | 原句 4：「他在确认她到底认**哪一半的血缘**」 | 本章原文只给「Simpson／Simpson Foundation／你不是辛普森吧」一线，未出现任何第二支血脉 | 自行加戏（原文无据） | 提示 |
| A12 | 原句 9／导航：asphodel ＝「水仙」；三条花语「每一种都绕不开死」 | `text/ch35_35.txt:320`：「Asphodel, carnations and bay leaves aren’t normally put together.」；`:326`：「‘Asphodel means “My regrets follow you to the grave”.’ … ‘Bay leaves mean “I change but in death”, and red carnations mean “Alas for my poor heart!”.’」 | ① asphodel ≠ 水仙（narcissus），建议括注英文以免与黄水仙混；② 红康乃馨花语原文是「唉我这可怜的心」的哀叹，未涉死 ⇒ 「都绕不开死」过强 | 提示 |
| A13 | 导航「视角：第三人称限知，紧贴卡莉」 | `text/ch35_35.txt:140`：「Peter could picture it now: …」；`:152`：「He had been missing his ex-wife in this respect and had been considering replacing her with a kinder, gentler, younger model…」；`:299`：「He just wasn’t sure that he was totally ready to leave London yet. He wasn’t a transplant. He’d grown up here.」 | 存在 Peter／Caius 内视角，非单贴卡莉（第三人称、限知成立） | 提示 |
| A14 | 原句 7：「他留下的**唯一**实物」；总结漏掉「他带走的东西」 | `text/ch35_35.txt:38`（file 留在 coffee table）与 `:245`（凯厄斯倒掉那杯茶）并存 ⇒ 实物不止一件；`:194`「She handed him the notes she’d just scrawled.」⇒ 他带走了那页 notes | 块内/总结层自相矛盾＋遗漏 | 提示 |
| A15 | 原句 3：「她又好笑又**刺人**」「**大概**上过谈吐训练课」 | `text/ch35_35.txt:41`：「She found it rather amusing; she was **certain** Peter had had elocution lessons…」 | 原文是「确定」非「大概」；「刺人」为原文所无 | 提示 |
| A16 | 导航「案子线（**父亲**部分持有的广场把凯厄斯的案子牵连进来，他因此被撤下）」 | `text/ch35_35.txt:182`、`:233`（是凯厄斯的父亲）；导航通篇讲彼得，此处「父亲」会被读成彼得 | 摘要层同 A2 的病灶，表述需明确 | 提示 |
| A17 | 一句话总结：「他留在客厅里的东西——茶几上的文件、一口没碰的茶、**门口那个让他神色不对的名字**」；导航「一桩旧账」 | `text/ch35_35.txt:23`（名字是他说出的一词，不是留下的物）、`:131`/`:137`（旧账＝孟加拉工厂剥削女性工人，原文未用「旧账」一词） | 比喻与措辞失准／指代不明 | 提示 |
| A18 | 原句 9 的分析覆盖了引语之外的原文（祖母的花语书、三条花语） | 引语止于 `text/ch35_35.txt:320`；分析延伸到 `:326` | 引语选短（可延引语或收窄分析），非事实错误 | 提示 |

## 4. 机器口径提示（非缺陷）

- `2-machine.json` 中 `quotes[].segments[].text` 显示为**截断**（最长约 102 字符，如「…the name she’d called him for 」）。这是 JSON 的展示截断，**不是引语被截短**——本次用独立脚本复核：9 条引语在 `text/ch35_35.txt` 中均为**单一连续子串**（跨度 38–328 字符，无 `…`、无跨段拼接）。若据该 JSON 判「引语截短」，属**假红**，特此记录以免后续误修。
- `chapter.sh` 退出码 **0**、verdict=ok、`counts` 全 0 缺陷（blocks 9 / segments 9 / segment_miss 0 / struct_bad 0 / empty_quote 0 / keyword_bad 0 / cjk_low 0）——机器层与本次人判**无冲突**；本章无假红型报警。

## 5. 已核实为正确（防误修，固定一节）

以下写法**看着像错、回原文核对后成立**，后续任何人不得以「读着不对」为由改动（除非能给出反证）：

1. **「彼得·辛普森」这个名字成立** —— 本章原文只给名 `Peter`（`text/ch35_35.txt:23` 起），姓氏来自本书语料人物表 `text/xx_characters.txt`：「the disgraced MP and fast-fashion tycoon Peter Simpson」；`text/ch08_08.txt:20`：「Peter, her biological father」。⇒ md 的「父亲彼得·辛普森」**正确**，不要因「本章没写姓」而改名。（A12 里的 asphodel/水仙是另一回事。）
2. **原句 1 的「神色不对」正确** —— `text/ch35_35.txt:23`「he got funny when she did」；且 **Peter 是她 97% 人生都在用的名字**。任何把 Peter 说成「她不常用的名字」「外号」的改法都是错的（要改的是 md 原句 6 的「生分」，不是原句 1）。
3. **原句 8 的引语内容本身正确** —— `text/ch35_35.txt:233` 逐字；说话人是凯厄斯；「**他父亲**部分持有的广场」这一内容没错，错在 md 把产权人写成彼得、把句子安给卡莉（A1/A2）。**修时只改归属，不要改引语**。
4. **「茶几上的文件」与「一口没碰的茶」两处痕迹真实存在** —— `text/ch35_35.txt:38`、`:215`（`:245` 凯厄斯把那杯茶倒掉）。原句 7 里「凯厄斯后来把茶端到水槽边倒掉」**正确**；错的只是「唯一实物」这个限定（A14）。
5. **三条花语的英文逐字正确**（`text/ch35_35.txt:326`），中文释义亦对；A12 只针对 asphodel 的中译与「都绕不开死」的概括，**不要去改花语原文**。
6. **导航「97% 的称呼」成立**（`text/ch35_35.txt:23`）；原句 1 的中文理解与「为什么这样写」无事实错误。
7. **词汇表 31 条例句全部是本章原句**（`text/ch35_35.txt` 内各命中且仅命中 1 次），分档无注水 ⇒ S4 层无需改动。
8. **H1 `# 35. Caius and Callie’s Flat` 与源文本节题逐字一致**（`text/ch35_35.txt:17`），写法与本书 54/54 一致 ⇒ 勿改。
9. **「父亲彼得·辛普森」与 Callie 的父女方向** —— `text/ch35_35.txt:20`「Callie opened the front door to her father.」、`:104`「You’re my only daughter, aren’t you?」、`:212`「‘Bye, Dad,’ Callie called after him」⇒ md **没有把关系写反**，不得反向修改（A3 是要**补上**「Am I?／Biologically speaking」这一层，不是要改关系方向）。
