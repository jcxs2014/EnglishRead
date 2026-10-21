# 4-verdict.md — ch05 独立审查裁定（R3）

审查员：R3（第三次审查；独立重读原文后落盘）
原文：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch05_5.txt`（5,461 字符）
精读：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch05 the poisoned salad is investigated.md`
机器层：`2-machine.json`（`bash scripts/chapter.sh … --json`，退出码 0，verdict=ok，四道探针 issues 全空）

---

## 一、四组数

| 组 | 条数 | 说明 |
|---|---|---|
| **逐字** | **2** | 6/6 引语块（`> **原句 N:**`）逐字命中原文，无一处改字；2 条缺陷全部在「本章词汇」表的例句列（见断言 A6/A7） |
| **对应** | **7** | 3 条落在引语块（施事/受事/归属/时序级），4 条落在导航层（归属与职级） |
| **形态** | **2** | H1、导航项数、子项集、块数均合规；2 条为导航项名变体与术语不一致 |
| **断言** | **5** | 2 条阻断、3 条提示 |
| **合计** | **16** | 其中 **阻断型 2 条**、提示 13 条、跳过 1 条 |

## 二、形态组（细项）

- **H1**：`# 5. The Police Station` — 合规。与本书既有形态一致（其余章同为 `# NN. 书内标题`），且与 epub `OPS/s014-Chapter-005.xhtml` 的书内章题 `The Police Station` 逐字相同。
- **所属分部**：书内真名 **SATURDAY**（epub `OPS/s010-Part-002.xhtml` 首行正文 `SATURDAY`，含 Chapter-002..006，本章为 Chapter-005）。md 全文**未出现任何分部名或星期名**（grep `MONDAY|FRIDAY|SATURDAY|SUNDAY|TUESDAY|WEDNESDAY|THURSDAY|分部` 零命中），因此不存在"分部名写错"；记为**跳过**。
- **导航项名与项数**：5 项 —— `一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法`，项数 = profile（mystery-thriller nav.count=5）✓。项名「视角」对应 profile 规范名「情感弧线位置」，profile 只声明「线索结构↔Tropes 兑现/反转」一个 alternates；**但全书 54 章一律用「视角」**（ch01/02/03/…/ch51 同形），属书级统一写法，非本章引入 ⇒ 提示（书级）。
- **子项集**：`中文理解 / 关键词 / 为什么这样写 / 读者视角提示` 4 项，与 profile `subitems` 完全一致 ✓。
- **块数**：本章 **6 块**，本书众数 **7**（块数中位 7.0），偏离 **−1**；profile 允许区间 3–10，6 在区间内。理由：本章可作引语的长句共 6 段（原文 39/142/439/1061/3824/4088 起），md 一段一块、逐块对位，块数随可引原句数浮动，非为凑数而增删。

## 三、断言表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | 导航「一句话概括」与「一句话总结」称「**监管机构与供应商确认那袋沙拉被污染**、启动紧急召回」 | ch05:142–436「It’s **possible** that the bag had some hemlock leaves in it.」；旁证 ch13:95「They’ve investigated the farm … there was **no trace of hemlock** … **It was murder.**」 | 原文只有「可能」，无人「确认」；FSA 这条线在本书后文（ch13）的结论恰恰是**没有毒芹、是谋杀**。md 把情态词升级为断定且方向相反，两处（导航＋总结）同错。 | **阻断** |
| A2 | 原句6「为什么这样写」：「调查在这里**从物证转到笔迹**，他们开始拆写信人给自己搭的身份」 | ch05:4088–4404 全引语只谈化名取自 Wagner 歌剧、交友广告上的 "culture vulture" mark 与 "I come from a petit bourgeois family." | 原文**没有任何笔迹调查**，也无"物证"这条线；该线是**化名＋广告自我描述**。后半句"从那句出身自述反推对方挑选化名的方式"才对。凭空添加调查内容＝虚构。 | **阻断** |
| A3 | 原句4「为什么这样写」：「也活在**机构的默认态度**里——**案子没人接手时**，省事的结论就是**不必再深究**」；「读者视角提示」：「'这只是一场意外'就很容易被**允许留在案卷里**」 | ch05:1061–1584 只写专案组被解散及政治原因；同章 2363–2562、2565–2680、4501–5372 显示三人同时在查（warrant request／外交部／搜查＋摄像头） | 把条件句写成事实前提：原文没有"案子没人接手"，也没有"结论进案卷"的文本。较 A1/A2 轻（前半句"机构默认态度"有 Chief Superintendent 的玩笑与预算说作支撑），但仍是原文之外的结论。 | 提示 |
| A4 | 导航「一句话概括／视角」与原句5「读者视角提示」把第二场地点写成「**警局厨房**」「场景在警局办公室与警局厨房之间切换」 | ch05:1954–2680 只给 kettle、mugs、窗外、街上的邮筒，无地点命名 | 场景地点为推断（英文自然但不逐字）；读者会被当成文本事实。 | 提示 |
| A5 | 导航「视角」把电话那头的搜查写成「在**迪吉故居**的搜查汇报」；「线索结构」写「**故居搜查**的空白（邻居布尔恩太太、门铃摄像头）」 | ch05:135「downstairs rooms and half of the upstairs」、141 Mrs Bourne、144「It doesn’t show **the Institute**」；旁证 ch02:155「‘**Digby didn’t live here.**’ Caius grimaced.」、ch02:444「Do you live on the square?」（Mrs Bourne 住在广场上）、ch04:17–20 Digby 自己的住处是 Dollis Hill 的 studio（一层，无楼上） | 搜查的是**霍拉西奥·康布研究所（Priory Square）**，不是"迪吉故居"——原文 ch02 明言 Digby 没住在研究所，研究所也无"楼上"以外对应他 studio 的结构；"故居"指称错。 | 提示 |
| A6 | 词汇表 `disbanded` 例句：`'You must be pretty disappointed that your special unit has been disbanded. A bit of a shock when that happened so suddenly.'` | ch05:1061–1584 同句在原文**到 "so suddenly." 之后并未结束**，md 自行补了原无的收尾引号 `’` | 逐字组：截断引语并**伪造收尾引号**（原文该处无 `’`）。 | 提示 |
| A7 | 词汇表 `flats` 例句：`'No one on the square saw anything,' Matt said, … 'Half of the flats are empty. Investment properties.` | ch05:5051–5372 | 逐字组：截断引语且**无收尾引号**，引号不成对。 | 提示 |
| A8 | 原句2「中文理解」：「**对方**已经启动紧急召回」 | ch05:142–436「They’ve done an emergency recall」 | 对应组：英文 They 二义（话题 the FSA / 最近名词短语 the supplier），md 紧接「局方正在与…供应商接洽」，读者会把"对方"默认读成供应商，而召回的行政主体通常是 FSA。英文本身歧义 ⇒ 提示，非确定性写反。 | 提示 |
| A9 | 原句2「那袋菜里有可能**混进了**毒芹的叶子」 | ch05:142–436「the bag **had** some hemlock leaves in it」 | 对应组：had＝袋里曾有/含有，"混进"添了"混入"的动作意味。（情态 "It's possible" 已正确保留为"有可能" ✓） | 提示 |
| A10 | 原句1「中文理解」：「警务总监**听完**先是摇头」 | ch05:39–139（本句是全章第一句发言） | 对应组（时序）：原文没有"听完"这一前序。 | 提示 |
| A11 | 原句3「中文理解」：「警务总监**自嘲**一句」 | ch05:439–540「The Chief Superintendent chortled at **his own joke**」 | 对应组：原文是"为自己的笑话发笑"，"自嘲"（挖苦自己）语用色彩偏移。 | 提示 |
| A12 | 原句6「中文理解」：「写信人是**不折不扣的贵族**」「照着'文化蛀虫'**那一档**自我标榜挑的」 | ch05:4088–4404「they're **super posh**」「based on their "culture vulture" **mark**」 | 对应组：posh→"贵族"偏向 aristocratic（原文更近"有钱有势/上流"）；mark 是标签，"那一档"读成分级。 | 提示 |
| A13 | 导航「叙事手法」：「**上司的**玩笑与政治寒暄不断给案情'降调'」 | ch05:60–69（PMQs、stilton 出口 South Korea、"I'm going to live in a cave"＝**Matt 与 Caius** 之间）；ch05:44（Arthur Hampton／Home Secretary／budget cuts 才是上司的政治内容） | 对应组（归属）：中文里"上司的"同时辖"玩笑"与"政治寒暄"，最自然读法把 PMQs 寒暄也归给上司，而那段是 Matt 与 Caius 的。另一读法（上司谈预算削减）亦通 ⇒ 提示。 | 提示 |
| A14 | 导航「视角」：「紧贴**顾问警员**凯厄斯」 | epub 人物页 `DI Caius Beauchamp and family`；ch02:417「Yes. **DI Caius Beauchamp.**」 | 形态/对应：他是 DI（_detective inspector_），非"顾问"。但"顾问警员"为**全书 8 章通用的既成写法**（ch09/ch12/ch13/ch16/ch17/ch44/ch51 同），非本章引入 ⇒ 提示（书级）。 | 提示 |
| A15 | 全章把 Chief Superintendent 译作「**警务总监**」 | 本书 ch37 词汇表已定：`Superintendent \| （英国警衔）**总警监** \| The Chief Superintendent stood in front of Matt and Amy with DI Robbie Eastley.` | 形态/术语：与全书自有词表冲突；全书仅 ch05 用"警务总监"，其余用"总警监"（ch37）。 | 提示 |
| A16 | 导航「线索结构」把「寄到邮政信箱的**求爱信**」列为既定线索 | ch05:102「'It’s an affair.'」、108「'Maybe they didn’t feel safe giving away their address.'」、117「'A scam, maybe?'」 | 断言：本章这三句全是**假设**（Caius 的猜测，还自我反驳了"骗局"一说）；本章原文没有断定寄的是求爱信。 | 提示 |
| A17 | 导航／总结是否与原文一致（Q4 总览） | ch05:39–5460 全章 | 三条警方工作线（FSA／召回·PO Box warrant＋外交部·搜查＋门口摄像头）与 md 导航的概括**大体一致**；不一致集中在 A1（A1 处把"可能"写成"确认"）、A5（搜查地点写错为"故居"）、A16（假设写成事实）、A4（地点推断）。 | 提示 |

## 四、四个待核问题的结论

1. **警方如何把"意外"讲成自洽剧本，每次推断是谁说的**：本章的"官方化"分两层——Chief Superintendent 用 `'Poisoned salad, eh?' … 'You couldn't make that up.'`（39–139）与 `'And they say eating your greens is good for you.'`（439–540）把投毒案降格为笑话，他本人对解散 special unit 也失望（1765–1939）；真正把"意外"写成剧本的是 **Caius 本人**：FSA→供应商→紧急召回→"袋里**可能**有毒芹叶"（142–436），以及 `'Well, no, because he ate an accidentally poisoned salad. The date panics, flees and calls off the burglary…'`（3824–4037）。**本章唯一一次反驳是 Matt 的 `'But Digby wasn't burgled.'`（3794–3821），随即被 Caius 转成剧本的一环**。补充事实：这套"意外污染"论最早由 **Matt 在 ch04:68 提出**（"What if the hemlock leaves made it into the bagged salad … by mistake"），ch05 是 Caius 把它程序化。另注：**Chief Superintendent 在本章从未下过"排除投毒/认定为意外"的结论**，md 导航把他写成"确认"的一方属于 A1 的越界。

2. **沙拉与面包归属、吃没吃**：**本章原文没有一句涉及沙拉/面包归属或吃没吃**；本章与食物有关的唯一句子是 Caius 的 `he ate an accidentally poisoned salad`（3824–4037）。归属两句在 ch02：`:131`「'The same salad on both plates.'」（说话人 Caius）、`:134`「there was a roll on Digby's side plate and just crumbs on his guest's」（说话人 Amy）。md 在本章**未声称**沙拉/面包归属，故无对应缺陷（假红风险项：若他章或别处把这两句挂到 ch05，即为越章引用）。

3. **食品标准局与供应商这条线在原文里被说成了什么结论**：原文只有 Caius 一段（142–436）——已联系 FSA；FSA 正与**那家供应商**接洽，该供应商供货给他们**确信** Digby 买沙拉的那家 greengrocer's；`They've done an emergency recall`；`It's possible that the bag had some hemlock leaves in it`。**没有**任何"已排除投毒/已认定为意外"的结论。后续结论在 ch13:95（Caius 转述 FSA 调查农场 "there was no trace of hemlock … It was murder."），不在本章。md 的"确认那袋沙拉被污染"（A1）与原文相反。

4. **md 导航与总结对本调查线的概括是否与原文一致**：大体一致（三条线都对得上），但有四处失真：A1（"可能"→"确认"，且方向与 ch13 相反）、A5（搜查地点"迪吉故居"→应为研究所/Priory Square）、A16（求爱信：假设→事实）、A4（"警局厨房"为推断）。

## 五、机器层与人工层的关系

`2-machine.json`：verdict=ok，退出码 0；quotes 6/6 命中、struct/empty_quote/keyword/cjk/quote_long 五类 issues 全空；form：h1_shape_ok=true、nav_count=5、nav_missing=[]、subitems_modal 四项、blocks=6、profile=mystery-thriller。**四道探针全绿，但上表 2 条阻断型（A1、A2）机器不可见**——A1 是模态词升级（探针只查引语与子项/中文字符比），A2 是分析句虚构调查内容（探针不校验分析的内容边界）。这与"四道机器探针全绿 ≠ 没缺陷"一致。

## 六、纪律声明

- 本次只写 `.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch05/` 下 1-suread.json / 2-machine.json / 3-diff.md / 4-correspondence.md / 4-verdict.md 五份；
- **未改动书目录任何 md**，未 `git add`、未 `git commit`、未推送；
- 所有引语与数字均逐字抄自 `text/ch05_5.txt`（区间为本文件 0-based 半开区间，行号即 `text/ch05_5.txt` 行号）。
