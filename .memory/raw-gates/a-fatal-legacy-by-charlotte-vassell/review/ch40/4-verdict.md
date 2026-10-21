# 4-verdict.md · ch40 独立审查判定（Charlotte Vassell《A Fatal Legacy》第 40 章）

审查员：独立审查员（第二轮，接替卡死的前任）｜日期 2026-10-21
书目录：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell`
被审 md：`ch40 caius takes his family to frithsden`（小标题 H1 `# 40. Frithsden Old Hall`）
语料：`text/ch40_40.txt`（8828 字符 / 209 行 / 全部 15 处对话可核）
落盘：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch40/`（1-suread.json、2-machine.json、3-diff.md、4-correspondence.md、4-verdict.md —— **五份全部覆盖写**）

---

## 0. 审查过程与自证

| 步 | 动作 | 产物 |
|---|---|---|
| R0 | 读 `docs/rules/审查表.md` R0–R5 与 `docs/rules/生产-审查对照.md`（未读 `docs/实测档案/`） | — |
| R1 | **通读 `text/ch40_40.txt` 全文**（209 行），逐事件记人物关系与逐字数字 | `1-suread.json`（本审查员**重写**，覆盖前任版本） |
| R2 | `bash scripts/chapter.sh "<书目录>/ch40 caius takes his family to frithsden" --json`（退出码 **0**） | `2-machine.json`（重跑，覆盖前任版本）+ `2-machine.err`（空） |
| R3/R4 | 开 md，逐块三问核，**每两块追加**一次 `3-diff.md` | `3-diff.md`（块 1–2 / 3–4 / 5–6 / 7 + 形态附记） |
| R4 | 逐块一行对应表 | `4-correspondence.md` |
| R5 | 本文件 | `4-verdict.md` |

**⚠️ R1 顺序瑕疵（如实披露）**：本人先通读了 `text/ch40_40.txt` 全文（未见 md），但在目录清点时的一条命令里**先打印出了本章 md 的前 40 行**（导航 5 项 + 原句 1–3 的中文理解/关键词/为什么这样写），**随后**才落盘 `1-suread.json`。补救与自证：① `1-suread.json` 的 16 条事件全部按**原文动作粒度**独立记录，与 md 前 40 行所见内容（人物、数值、场景）逐条比对无冲突、无一方信息渗入（如 md 前 40 行未提 Marcus 的板球队、Turner 展、Dotty 的怀孕、`£10` 导览、"我不是六岁"，这些是我素读时独立记下的）；② `3-diff.md`／`4-correspondence.md` 的每一条结论都重新回原文取逐字证据，不引用 md 前 40 行；③ 结论不依赖那段预览。**本轮结论的有效性未受该瑕疵影响，但顺序瑕疵本身在此登记在案。**

**⚠️ 机器层"全绿"不等于无缺陷**：本章 `2-machine.json` 退出码 0、`segment_miss=0`、`struct_bad=0`、`empty_quote=0`、`keyword_bad=0`、`cjk_low=0`、7/7 引语逐字命中、29 条词汇例句我另行独立 flat 比对亦 29/29 命中 —— **但本轮 4 条阻断型缺陷，四道机器探针全部看不见**（时序倒置 / 方位反转 / 场景写错 / 摘要层归属错置），正是 S3 第 ⑥ 类"施事·受事·归属写反"与 S5 断言层的典型盲区。

---

## 1. 断言表（断言 | 证据（章:区间）| 结论 | 档位）

| # | 断言 | 证据（章:区间，逐字） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | 原句 1「为什么这样写」："作者**先给**一个外部理由（书太枯燥），**再抖出**真正的内部原因（案子压着人）" | `text/ch40_40.txt:41`（字符 1429–1695）：`He was still working through the Digby Combe-Watson case at the back of his head… finding it hard to concentrate on the book.`（内部原因，**先**）`The fault might lie with the author’s dry prose rather than Caius’s agitated mind.`（外部借口，**后**） | 原文顺序与 md 相反：先内部原因、后外部借口。md 同块「中文理解」自己按"案子→干涩文笔"叙述，块内亦自相矛盾 | **阻断** |
| A2 | 原句 1「中文理解」："**作者**顺手把责任推给**作者**的干涩文笔" | `text:41`：`rather than Caius’s agitated mind` —— 自我辩解的**主体是凯厄斯**（第三人称自称＝自由间接引语）；被推责者也是凯厄斯本人，推责对象是那本历史书的作者 | 主体含混（两个"作者"一为小说作者、一为历史书作者），且与同块「为什么这样写」的"**自我辩解**"口径打架。应写"他自己拿历史书作者的干涩文笔替自己开脱" | 提示 |
| A3 | 原句 2 的期限"还有六个星期" | `text:56`：`‘Well, not for another six weeks anyway.’` | 与后文可对照：ch40 属 FRIDAY 分部，此后 SATURDAY(41–47)→MONDAY(48–51)→TUESDAY(52–53)→SIX WEEKS LATER(54)，即约六周后 ch54 的**十二周扫描**（`text/ch54_54.txt:20` `Their appointment for their twelve-week scan…`）——md 的读者提示"拿它对照后面的倒数式时间表"经得起对照 | **已核实为正确** |
| A4 | 原句 2「中文理解」："父母两人**一左一右**""身体却**先软**了下来" | `text:56`：`but then relented easily at his parents’ united, imperious gaze` | 原文只给"两人的目光合一"与"轻易让步"，未给站位与身体动作；属扩写，不与原文冲突 | 提示 |
| A5 | 原句 3「中文理解」："人已经**跑去厨房**找手机了" | `text:104`（字符 4297–4326）：`Bridget left the kitchen in search of her phone. She’d put it down somewhere…` | **方向相反**：原文是**离开**厨房去找先前放在别处的手机，md 写成**跑进**厨房找手机。同句"母亲扑在婴儿衣服上"（`desperate to have a look at baby clothes online`）✓ | **阻断** |
| A6 | 原句 3「中文理解」后半（手机、婴儿衣服）是否在讲这句引语 | 引语止于 `text:104` 的 `but his parents weren’t really listening`（字符 4151–4296），手机句在其后 | 分析越出引语跨度（S2 截短）。缺口仅一个相邻句，非 Such-a-Fun-Age 式长距离；按 `生产-审查对照` S2 严格口径可判阻断 | 提示 |
| A7 | 原句 4 施事归属：父亲 Marcus 提历史学家邮件、神父洞、"建筑师的眼睛" | `text:131` `I had a historian email the family office asking questions the other day.`；`text:137` `‘About the priest holes… My builder’s brain thinks there’s some negative space that’s not accounted for.’` | 三项全对；Marcus=父亲（`text:110` 凯厄斯称其 `Dad`）✓ | **已核实为正确** |
| A8 | 原句 4「为什么这样写」："**饭桌上**随口一提" | `text:47` `Marcus was waiting for them both in the kitchen.`；`text:101` `putting the kettle on`；`text:158` `went back out to the terrace` | 全章场景为露台／厨房／门厅（`text:209` `waiting in the hall`），无餐桌；"饭桌上"可读作"吃喝时"故不判与原文相反 | 提示 |
| A9 | 原句 5 主体与三处文物 | `text:152`：`‘Nothing. What if we’ve got sculptures from Benin, or a bit of Greek temple? Something from the Forbidden City that we shouldn’t have? You know? I have no idea what’s in this building.’` | 主体=凯厄斯 ✓；贝宁／希腊神庙／故宫三处逐字对应 ✓ | **已核实为正确** |
| A10 | 原句 5「中文理解」："**父亲追问"什么开始了"**" | `text:146` `‘And so it begins.’`（**凯厄斯**）；`text:149` `‘What does?’`（Marcus 问的是"什么？"） | md 把凯厄斯的 `And so it begins` 挂到父亲的追问名下（中文引号读作父亲原话）；且 `What does?` 原文没有"什么开始了"这一说法 | 提示 |
| A11 | 原句 5「为什么这样写」："脑子却开始替这栋楼**编出**一批来路可疑的收藏" | `text:152` `What if we’ve got…?`（假设式提问） | 原文是猜测可能存在，md 的"编出"读作凭空捏造；同块下一句又自称"**猜测**"，块内口径不一 | 提示 |
| A12 | 原句 6「史实比虚构更让人难受」的方向与说话人 | `text:176`：`He didn’t read much history. He preferred fiction. It was less upsetting.` | ①方向：虚构 less upsetting ⇒ 史实更难受 ✓（`00_情感节点.md:94` 的"史实比虚构更让人难受"亦 ✓）。②说话人：这是叙述句（自由间接引语，主语 `He`=Caius），**原文无人把这句说出口**；md 全程按"凯厄斯的状态/心理"处理，未安到任何角色头上 ✓。③ md 原句 1 读者提示"他随后拿'虚构没那么难受'来替自己开脱"亦正确 | **已核实为正确** |
| A13 | 原句 6「中文理解」："却**发现自己读不进去历史**"；「读者视角提示」："是**不敢**再碰真的东西" | `text:176` `He didn’t read much history.`（一般性偏好）；`It was less upsetting.`（比较级） | "发现"把一般性习惯写成当场发现；"不敢"把比较级升为心理障碍。均属措辞过强 | 提示 |
| A14 | 原句 7 人物绑定：`someone else`／`their parents`／`She` | `text:182` `‘I’m not six, Mum,’… ‘It’s not a playdate.’`；`text:188` `It was odd to watch someone else turn into a teenager around their parents. She had thought that was just her…` | `someone else`=凯厄斯 ✓；`their parents`=凯厄斯的父母（Marcus 与 Bridget）✓；`She`=Callie ✓。md"凯厄斯在**自己**父母面前"——"自己"先行词绑定到凯厄斯，正确 ✓（老宅一场人物称呼与关系**无绑错**） | **已核实为正确** |
| A15 | 原句 7「为什么这样写」："凯厄斯在**客厅里**那套'我不是六岁'" | `text:158` `went back out to the terrace`；`text:161` `Callie looked up from her magazine`；`text:179` `Bridget appeared… with a tray`；`text:182` `‘I’m not six, Mum,’ Caius said, getting up from his seat.`；`text:209` `Dotty and Georgie were waiting in the hall` | 该场在**露台**；全章场景仅露台／厨房／门厅，**无客厅**（`text:209` 说的是 `great hall`）。md 把一句具体台词搬到了原文没有的房间 | **阻断** |
| A16 | 导航「视角」"第三人称限知，**紧贴凯厄斯**"；「叙事手法」"一场下午茶到**晚餐**的连续家庭场景" | `text:20` `She wished she’d brought a sketchbook with her.`（开篇落在**卡莉**内心）；`text:188` `She had thought that was just her…`（收尾落在**卡莉**内心）；全章无晚餐场景（`text:23` 下午茶：`a Victoria sponge`；`text:179` 傍晚客人到访；`text:209` 父母去车站） | 主体确为凯厄斯，但"紧贴"不涵盖首尾两段卡莉内心（md 自己原句 7 已写"观察者换成 Callie"，导航与块内不一致）；"到晚餐"原文无据。属概括不精确／措辞外扩，非与原文相反 | 提示 |
| A17 | 一句话总结："而他自己脑子里**真正停住的那一句**，是'虚构没那么难受'" | `text:41` `He was still working through the Digby Combe-Watson case at the back of his head… finding it hard to concentrate on the book.`（停在脑后的是**案子**）；`text:176`（less upsetting 是一般性阅读偏好陈述） | 归属错置 + **md 内部自相矛盾**：同文件导航行已写"他停不住的那句话始终是**案子的那句**"，总结却改成"虚构没那么难受"。原文支持导航那一版 | **阻断** |
| A18 | 分部名（硬事实一） | epub `library/A Fatal Legacy (Charlotte Vassell) (z-library.sk, 1lib.sk, z-lib.sk).epub` → `OPS/TOC.xhtml`：`s050-Part-008.xhtml` = `FRIDAY`，其后 s051–s055 = Chapter 036–040；`s056-Part-009.xhtml` = `SATURDAY`（自 ch041 起）。十二分部真名：A FRIDAY IN MAY / SATURDAY / SUNDAY / MONDAY / TUESDAY / WEDNESDAY / THURSDAY / **FRIDAY** / SATURDAY / MONDAY / TUESDAY / SIX WEEKS LATER | **ch40 属 FRIDAY ✓**。全库 54 章 md 中出现的 18 处分部名（分布于 17 章）逐章与 TOC 比对：**0 处误标**，"A FRIDAY IN MAY" 全库 md **0 次**误用。ch40 md 本身未写分部名（本书仅 17/54 章在导航里标分部）⇒ **无错可改** | **已核实为正确** |
| A19 | PCQV 与唱片公司（硬事实三） | 本章原文与本章 md 均未出现 PCQV／唱片公司（`grep -c` = 0） | 本章无归属问题。全书口径另核：`00_概述.md` 与 `ch36` 均写"法国奢侈集团 PCQV"与"欧拉莉亚自己的唱片公司是另一方，被 PCQV 的商业合同逼着就范"，两者未混同 ✓ | **已核实为正确**（本章不适用） |

**断言组小结**：核 19 条 → **阻断 4**（A1 / A5 / A15 / A17）／提示 8（A2 / A4 / A6 / A8 / A10 / A11 / A13 / A16）／已核实为正确 6（A3 / A7 / A9 / A12 / A14 / A18）+ A19 不适用／跳过 0。

---

## 2. 四组数

| 组 | 分母 | 分子（通过） | 缺陷明细 |
|---|---|---|---|
| **逐字** | 引语 7 块 + 词汇例句 29 条 = **36** | **36** | 0。引语 7/7 在 `text/ch40_40.txt` 命中（我独立 flat 比对；机器亦 `ok:true`×7、`segment_miss=0`、**无 `…` 缝合、无省略号**）；29 条例句逐字取自本章且各命中 1 次 |
| **对应** | **7** 块 | 主题对应 **7/7** | 逐块最重档：**阻断 3 块**（块 1 时序倒置／块 3 方位反转／块 7 场景写错）、**提示 4 块**（块 2、4、5、6）、纯通过 0 块（"这段中文在讲这句引语"这一问 7/7 成立；问题出在施事/方位/场景/时序与引语跨度） |
| **形态** | 5 个维度 | **4/5 完全符合** | 偏离 1 项（见 §3）——引语**词数下界**：块 2=24 词、块 3=21 词、块 4=25 词、块 6=12 词，低于创建卡 §3 的 30 词下界。**理由**：本书 395 块中位 37 词、142 块（36%）<30 词，`chapter.sh`/`gate.sh` 皆不查长度，属本书普遍形态而非本章独创；与 A6 同源（引语截短） |
| **断言** | **19** 条 | **6 条已核实为正确 + 1 条不适用** | **阻断 4**（A1、A5、A15、A17）／提示 8（A2、A4、A6、A8、A10、A11、A13、A16）／跳过 0 |

**阻断型条数：4**（全部落在"施事·受事·归属·方位·时序·场景写反"与"摘要层断言写反"，四道机器探针全看不见）。
**最要紧的一条：A1（块 1「为什么这样写」时序倒置）** —— 它出现在全章第一块、且是全章中心句的解释；md 把原文"先内部原因、后外部借口"讲成了"先外部理由、后内部原因"，方向相反，并连带把"自我辩解"的主体（凯厄斯）写成"作者"。同块「中文理解」按正确顺序叙述，说明这是「为什么这样写」单点的顺序误判，改一处即可自洽。**排第二的是 A5（块 3"跑去厨房找手机" ↔ 原文 `left the kitchen in search of her phone`）**——最干净的单点方位反转，一句话可改。

---

## 3. 形态组（逐项）

| 维度 | 本章实况 | 本书众数 / profile | 结论 |
|---|---|---|---|
| H1 | `# 40. Frithsden Old Hall` | 与原文小标题 `Frithsden Old Hall` **逐字一致**；本书形态 `# NN. 小标题`（如 `# 39. The Police Station`） | ✓ 符合 |
| 导航项名与项数 | 5 项：`一句话概括` / `视角` / `线索结构` / `人物弧线` / `叙事手法` | 全书 **54/54 章**导航项名与项数完全相同；`nav_count_ok=true` | ✓ 符合 |
| 子项集 | `中文理解` / `关键词` / `为什么这样写` / `读者视角提示` | profile `mystery-thriller` 四项（`句子结构` 为 optional，未加，合规）；本书众数同 | ✓ 符合 |
| 块数 | 7 | 本书中位 **7**（range 5–10） | ✓ 符合 |
| 偏离项 | 引语词数 4 块 <30 词 | 创建卡 §3 建议 30–70 词 | **偏离 1 项，理由**：本书 36% 的块 <30 词、中位 37 词，`chapter.sh`/`gate.sh` 不查长度；属本书普遍形态，非本章独创（详见 §2 形态组） |

---

## 4. 本章四个待核问题的结论

| 待核问题 | 结论 |
|---|---|
| ① 老宅一场每个人的称呼与关系 | **无绑错 ✓**。Marcus=父（`Dad`）、Bridget=母（`Mum`）、Georgie=今晚来客的画家兼雕塑家、Dotty+Georgie=`Your little friends`、布里奇特口中"你那位朋友她怀孕了"指 Dotty（`text:185`；Dotty 怀孕由 `text/ch42:57` `I’ve still got three months to go` 佐证）。md 原句 7 的 `someone else`=凯厄斯、`their parents`=其父母、`She`=Callie 全部绑定正确（A14） |
| ② 谁在问婚事／谁在提婚礼场地／谁在谈房子 | **原文**：问婚事=马库斯问戒指（`text:74` `Have you got a ring yet? We’ve got family ones.`）+ 布里奇特"未婚先孕"（`text:68` `Out of wedlock?`）；提婚礼场地=**马库斯**主动提"可以在这儿办"（`text:59` `You can have the wedding here,`）+ 布里奇特补八月/餐饮/篷房/花（`text:62`）；谈房子=马库斯"More bedrooms"（`text:50`）+ 凯厄斯与卡莉谈**农舍与厨房**（`text:164/170`）。**md 未把任何一句安到错误的人身上**；但导航把父母对婚礼场地说成"**盘问**"，原文是父母**主动张罗**（马库斯提场地、布里奇特列清单）⇒ A16 提示级 |
| ③ 「史实比虚构更让人难受」的说话人 | **原文无人把这句说出口**：这是叙述句（`text:176` `He didn’t read much history. He preferred fiction. It was less upsetting.`），主语是凯厄斯；md 全程按"凯厄斯的状态"处理，**没有误安说话人 ✓**。方向也正确（虚构 less upsetting ⇒ 史实更难受），`00_情感节点.md:94` 同向无误 ⇒ **已核实为正确（A12）**。唯一相关缺陷在摘要层：md 一句话总结把这句认作"真正停住的那一句"（A17 阻断） |
| ④ 导航与总结对"两条生活之间的分心"的概括是否与原文一致 | **主线一致 ✓**：家庭场景作表层、案子压在后脑作底噪，与 `text:41`（`at the back of his head… finding it hard to concentrate on the book`）完全对得上。**三处细部不合**：① 一句话总结与本章导航就"停住的那一句"互相矛盾（A17 阻断，原文支持导航那一版）；② 导航「视角」"紧贴凯厄斯"不涵盖首尾两段卡莉内心（`text:20`、`text:188`），且与 md 自己原句 7 的"观察者换成 Callie"冲突（A16 提示）；③ 导航「叙事手法」"下午茶到晚餐"——原文无晚餐场景（A16 提示） |

---

## 5. 已核实为正确（防误修护栏 · R5.5）

以下写法"看着像错"，回原文核对后**成立**，后续任何人不得以"读着不对"为由改动，除非能给出反证：

1. **原句 6 的"虚构没那么让人难受"方向**（`text:176` `It was less upsetting.`）——虚构 less upsetting ⇒ 史实更难受，**方向不可反**；`00_情感节点.md` 的"史实比虚构更让人难受"同向正确。
2. **原句 6 是叙述句、不是谁说的话**——主语 `He`=Caius，原文无人说出口；md 未安错说话人。**"史实比虚构更让人难受"的说话人＝无人（叙述句），主语是凯厄斯**。
3. **原句 7 的"自己父母"绑定到凯厄斯**（`their parents`=马库斯与布里奇特），**不是**卡莉的父母；`She had thought that was just her` 的 `She`=Callie。
4. **原句 3 的 Georgie**＝今晚来做客的画家兼雕塑家（`text:104`），md ✓；**布里奇特找手机**方向以原文为准：她**离开**厨房去找先前放在别处的手机。
5. **"六个星期"**可与 ch54 的十二周扫描对照（本部 FRIDAY → SATURDAY → MONDAY → TUESDAY → SIX WEEKS LATER），md 的读者提示成立。
6. **原句 4 的施事**（Marcus=父亲、`I had a historian email the family office`、神父洞、`My builder’s brain`）全对。
7. **原句 5 的三处文物**（贝宁雕塑／希腊神庙／故宫）与主体（凯厄斯）全对。
8. **分部名**：ch40 属 **FRIDAY**；全库 md 分部名与 epub TOC 逐章零误标，"A FRIDAY IN MAY" 全库零误用。
9. **词汇表 29 条例句**全部逐字取自本章且各命中 1 次；`check_vocab.py` 对本章无告警。

---

## 6. 覆盖声明与建议处置

- **本章（ch40）**：R1–R5 全跑完，逐块 7/7 核过，断言 19 条逐条核过；结论如上。
- **全书其余 53 章**：本次**未做**人判，只有机器层（`gate.sh`／`chapter.sh` 的历史绿灯），**不得称"通过"**。按 `审查表` §0.5 的成因类预筛思路，本轮已定位本章的成因类是：**①时序/顺序讲反、②方位与场景写反、③摘要层与导航层互相矛盾**——这三类应作为其余章的预筛方向（尤其：凡"为什么这样写"里出现"先…再…"的顺序断言，凡分析中出现具体房间/方位词，凡导航与总结对同一处作不同归属）。
- **建议处置（4 条阻断，均可局部改，不需重写）**：A1 改「为什么这样写」的顺序并把"自我辩解"主体改回凯厄斯；A5 把"跑去厨房找手机"改为"离开厨房去找手机"（并把该句并入引语或删去出引语的分析）；A15 把"在客厅里"改为"在露台上"；A17 让一句话总结与导航一致（用"案子的那句"）。改完须重跑 `bash scripts/chapter.sh "<书目录>/ch40 caius takes his family to frithsden"` 并跑 `scripts/corruption_scan.py`。
- **本审查未改动书目录任何 md，未执行任何 git 操作**（无 add / commit / push）；只写 `.memory/raw-gates/…/review/ch40/` 下五个文件。
