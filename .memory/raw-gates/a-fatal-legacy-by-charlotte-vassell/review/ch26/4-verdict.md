# 4-verdict.md · ch26 独立审查判定

> 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch26 matt returns from harrogate.md`
> 唯一权威源：`text/ch26_26.txt`（2331 字符 / 78 行 / 19 段）；副证源：`library/*.epub`（= text/ 的抽取母本，用于书结构与段落结构核对）
> 审查员：独立审查（先素读 → 落盘 `1-suread.json` → 后开 md）。本次**未改动书目录任何 md，未 git add/commit**，全部产物只写在 `.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch26/`。

---

## 一、四组数（只报这四组）

| 组 | 数 | 依据 |
|---|---|---|
| **逐字** | **5/5 引语逐字命中（MISS 0）**；另有词汇表 **28/28 例句在本章 text/ 逐字命中且各命中 1 次**；块数与源段落一一对齐（源 19 段中 P1/P9/P16/P18/P19 被引为 5 块） | `bash scripts/chapter.sh "<md>" --json` → exit 0，`quotes[].segments[].ok` 全 true、`segment_miss 0`；`verify_fragments_indep.py`（全书 776 引语 / 844 片段，MISS 0、拼接未标省略号 0）；`check_vocab.py` FAIL 0；例句 `str.count` 逐行计数 = 1（28/28） |
| **对应** | **5/5 块成立**（无「引语选短」块、无「讲全书主旨/作者生平」块、无「只复述字面、无为什么这样写」的低密度块）；其中 **1 块（块 4）的「中文理解」另有否定域反转**（不属对应失败，属断言错误 → 阻断 W1） | `4-correspondence.md`（逐块人判 + 三问：动词主语/受事/归属方向） |
| **形态** | **H1 ✓ / 导航项名与项数 ✓ / 子项集 ✓ / 块数 = 5（中位 7、众数 6、全书区间 5–10，落在下限）** —— 四项里 **3 项与全书众数完全一致，块数一项低于中位数 2 块**，偏离理由见下 | `python3 scripts/bookform.py "<书目录>" --json`（整书 54 章）+ `chapter.sh` 形态段 |
| **断言** | **共 12 条**：**阻断 2 条 · 提示 10 条 · 假红 0 条 · 跳过 1 类**（另见第三节「已核实为正确」8 条） | 本文件第二节判定表 |

### 形态组细目

| 形态项 | 本章 | 本书众数（54 章） | 结论 |
|---|---|---|---|
| H1 | `# 26. The Police Station` | 54/54 章均为 `N.` 形式（`h1_forms: {"N.": 54}`） | ✓ 一致（源文本第 17 行小标题逐字为 `The Police Station`，与 H1 相符） |
| 导航项名与项数 | 5 项：`一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法` | `nav_sets`：`一句话概括/视角/线索结构/人物弧线/叙事手法` = 54/54 章，`nav_counts` 全为 5 | ✓ 完全一致（`nav_missing: []`） |
| 子项集 | `中文理解 / 关键词 / 为什么这样写 / 读者视角提示` | profile `mystery-thriller` 的 `profile_subitems` 同四项（可选 `句子结构` 未用） | ✓ 一致（`struct_bad 0`） |
| 块数 | **5** | 分布：6×19、7×10、9×8、10×7、8×5、5×5；**中位 7、众数 6、区间 5–10** | ⚠️ 低于中位 2 块、低于众数 1 块，**未越界**（另有 ch14/ch21/ch47/ch53 同为 5 块） |
| **块数偏离理由（一行）** | 本章原文仅 **2331 字符 / 19 段**，是全书第 3 短（最短 ch21 1872、ch47 1996、ch26 2331；全书中位 8083.5，最长 19843），单场景 19 段里含 5 处独立发言（寒暄段 7 段 + 案情段 12 段），块数取到 5 与本章体量相符；md 的导航「叙事手法」已写「段落极短、对话密集」，但**没有一句是「块数为什么取 5」的显式理由** ⇒ 记**提示**（按形态规则「偏离且无理由」才升阻断；此处偏离在全书区间内、且有可解释的体量依据，故不判阻断） | | |

---

## 二、断言判定表

| # | 断言 | 证据（章:区间 / md 行） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | md 导航称本章属「**五月的星期三**」分部 | md:12「本章属「五月的星期三」这一分部。」 ⟷ epub `OPS/s033-Part-006.xhtml` 正文逐字 `WEDNESDAY 129 WEDNESDAY 130`；`OPS/toc.ncx` 第 26 章（`s039-Chapter-026.xhtml`）落在 Part-006 与 Part-007 之间 ⇒ 属 Part-006，标题逐字只有 `WEDNESDAY`；「A FRIDAY IN MAY」逐字在 `OPS/s008-Part-001.xhtml`（`A FRIDAY IN MAY 3 A FRIDAY IN MAY 4`），是 Part-001（第 1–2 章） | 分部名在书中不存在，「IN MAY」系把 Part-001 的标题安到第 26 章头上（本次审查任务书给定的「分部 A WEDNESDAY IN MAY」即源自 md 这句，非书内事实） | **阻断** |
| 2 | 块 4 中文理解把 Matt 的 `I doubt it` 译作「**我怀疑他知道**」 | 源 `text/ch26_26.txt:75`（chars 1784–1906）逐字：`‘I doubt it,’ Matt said, staring at the board. ‘It was transactional. He was taking the letters to get in her good books.’`（it = 上一问 `text/ch26_26.txt:72` chars 1709–1781 `‘Why did he help? Do you think he knew he was an accomplice?’`）⟷ md:38「Matt 盯着白板说：「我怀疑他知道。」」 | 中文常规读法「我怀疑（他）知道」＝ *I suspect he knows*，与原文 *I doubt it*（*I doubt that he knew*）**极性相反**；同块「为什么这样写」又写「拿信**不是**因为知情或忠诚」＝Scott 不知道 ⇒ 块内自相矛盾。**否定域反转** | **阻断** |
| 3 | 导航把「一句荤笑话」明确归给 **Amy** | md:14「…**Amy** 一边用 Tumblr、Etsy、meme 调侃，一边用一句荤笑话把正经推测拽回地面。」 ⟷ 源 `text/ch26_26.txt:78`（chars 1909–2330）逐字：`‘Also known as her knickers.’ Caius’s desk phone rang. ‘All right. Thank you.’ He put the receiver down. ‘Uniform have collected…’` | 原文**未给该句任何说话人标注**；段落结构（Caius 的一句 → Caius 的座机 → Caius 接电话 `He put the receiver down` → Caius 派活）与全书同型范式 `text/ch38`（epub `s053-Chapter-038.xhtml`：`‘Yikes.’ Caius’s phone rang. He took the call…`）都指向 Caius；但反向读法（Amy 插话）亦讲得通，**原文不能排他定案** ⇒ md 块级写「有人」稳妥，只有导航这句缺支撑 | 提示 |
| 4 | 块 5 中文理解说「入职表**上面有**他给的母亲联系方式」 | md:44「制服同事已经从那家面包店取走了斯科特的新员工入职表，上面有他给的母亲联系方式」 ⟷ 源 `text/ch26_26.txt:78`（chars 1909–2330）逐字：`Uniform have collected his new starter forms from the bakery. We’ve got contact details for his mum that he gave to them.` | 原文分两句：表单已取回 ／ 我们有母亲联系方式；未说联系方式印在表上。md 把两句并成一条因果链（高度可能，但非原文） | 提示 |
| 5 | 块 2 把「白板是警局处理命案的固定动作…再往板上写人物与关系」写成通则 | md:28 ⟷ 源 `text/ch26_26.txt:48`（chars 877–1000）逐字：`Matt looked up at the new whiteboard that had appeared for Scott Brown’s murder.` | 本章只提供「新出现一块为该案的白板」；「固定动作」「写人物与关系」是本章外的推演（本书 ch09 即 `money or sex on the whiteboard`），宜标明是通则推演 | 提示 |
| 6 | 块 3 中文理解把 `Once we’d found him` 的触发条件写成「影像一旦找到」 | md:32「…他们能在邮局找到拍到斯科特的影像——**影像一旦找到**，斯科特就能把他们指认出来。」 ⟷ 源 `text/ch26_26.txt:69`（chars 1389–1706）逐字：`… we would find the footage of Scott at the Post Office. Once we’d found him, Scott could easily identify them.` | 原文 him 指**斯科特本人**（警方顺藤找到他），md 换成「影像」；同块「为什么这样写」方向正确，故不判阻断 | 提示 |
| 7 | 一句话总结把「警方会找到他」压成「**他会被邮局拍到的影像认出来**」 | md:96 ⟷ 源 `text/ch26_26.txt:69`（chars 1389–1706）逐字：`Scott was killed because, well because anyone with half a brain would realise that we would find the footage of Scott at the Post Office. Once we’d found him, Scott could easily identify them.` | 原文因果链＝「找到影像 → 找到斯科特 → 他能指认 ⇒ 必须灭口」；md 总结漏掉「顺藤找到他」一环，把施受关系并成「被影像认出来」。同段其余部分逐字对得上 | 提示 |
| 8 | 两个被引答语的**提问**在分析层缺席 | 源 `text/ch26_26.txt:66`（chars 1336–1386）`‘Do you think they’re a spree killer?’ Matt asked.`（只进词汇表 `spree killer` 例句）／`text/ch26_26.txt:72`（chars 1709–1781）`‘Why did he help? Do you think he knew he was an accomplice?’ Amy asked.` ⟷ md 全文 `/usr/bin/grep -c 'accomplice'` → **0**；`grep -c '同谋'` → **0** | 块 3「先答『不』」、块 4「我怀疑他知道」都以「答」开头，被答的问句却缺席，读者在 md 内无从还原答的是谁的问题（块 4 的歧义正是本表第 2 条） | 提示 |
| 9 | 「Yumi（Matt 想带谁去）」「Caius 在约克读过大学」未进分析层 | 源 `text/ch26_26.txt:29`（chars 394–551）逐字 `‘Delightful. Might take Yumi for a break in the summer…’`／`text/ch26_26.txt:32`（chars 554–690）逐字 `‘I love Yorkshire. I went to uni up there.’` ⟷ md:85、md:86 两行含 Yumi，但**都只是词表 `definitely`/`different` 的例句**；`grep -c 'went to uni'` → **0** | 两条有名有姓/有出身的事实只以例句形式存在，分析层与导航层从未点出 | 提示 |
| 10 | 「`The tea’s shit though.`」在分析与词汇表两处皆无 | 源 `text/ch26_26.txt:32` 尾句（chars 554–690 内）逐字 `‘The tea’s shit though.’` ⟷ md `grep -c "tea’s shit"` → **0** | 与 `treason against God’s own country`（进了词表 `tantamount` 例句）配对构成地域笑点主干，缺了它导航里的「互嘲地域」只剩蔡斯单边的南方笑话 | 提示 |
| 11 | 四句接话/寒暄未进入 md（P2 Amy 咬司康、P10 `‘I can see the Daily Mail headlines now,’`、P12 `‘Is that still going on?’`、P14 `‘Thank God.’`） | 源 chars 157–244 / 1003–1056 / 1256–1281 / 1321–1333，逐字见 `3-diff.md` §4 对照表 ⟷ md 中零引用 | 均属寒暄接话，不推进案情；md 导航已声明「用一整段吃司康、喝茶、互嘲地域的寒暄垫底」＝已声明取舍 | 提示 |
| 12 | 词汇档位注水 + 截断例句省收尾引号 | `check_vocab.py`（整书）WARN 中属本章 4 条：`[基础] 基础档疑含超纲词「definitely」「different」「purchased」「collected」`（全书 26 条同型，属书级习惯）；另 `uniform`/`new starter`/`collected` 三行例句为截断引语，缺原文收尾引号 `’`（原文 `…I’ll deal with that. Matt, get the staff…`） | 四词为日常高频词，列入 ⭐ 基础 档偏注水（`different`/`definitely` 尤其接近无用条目）；截断例句逐字性不受影响（28/28 命中 1 次），仅格式小瑕 | 提示 |

### 档位合计

- **阻断 2 条**（第 1、2 条）——都必须改：① 分部名「五月的星期三」应为「WEDNESDAY」；② 块 4「我怀疑他知道」应改为否定式（并建议补回 Amy 的提问）。
- **提示 10 条**（第 3–12 条；其中第 12 条含「档位注水」与「截断例句省收尾引号」两小项）——只记不改。
- **假红 0 条**：本次机器层（`chapter.sh` exit 0 / `verify_fragments_indep.py` MISS 0 / `check_vocab.py` FAIL 0 / `corruption_scan.py` FAIL 0 / `verify_corpus.py` PASS）**没有报出任何需要人工推翻的报警**，故无假红条目。
- **跳过**：本章的导航层里凡涉及**全书层面**的事实（全书节奏、双时间线、跨章人物弧线）不在本章可核范围，未核；**本书其余 53 章本次只有机器层**（书级 `bookform`/`check_vocab`/`corruption_scan`/`verify_fragments_indep`/`verify_corpus` 均已跑过全书），**不得记作「通过」**。

### 覆盖声明

- 本次人判覆盖：**ch26 全章**（R1 素读 19 段全读、R3 三张单子逐块对账、R4 五块逐块对应、R5 断言 12 条）。
- 机器层覆盖：**全书 54 章**（`bookform.py --json`、`check_vocab.py`、`corruption_scan.py`、`verify_fragments_indep.py`、`verify_corpus.py`），ch26 另跑 `chapter.sh --json`。
- 未做：ch01–ch25、ch27–ch54 的**人判**（漏/对应/说话人/施事/事实断言），以及全书总览三篇（`00_概述.md` 等）的人判——**这些章只有机器层**。
- 语料层：epub `s039-Chapter-026.xhtml` 的 19 个段落与 `text/ch26_26.txt` **逐段完全一致**，抽取边界完整、无并篇/截断。

---

## 三、已核实为正确（防误修 · R5.5）

> 以下写法「读着像错」，回原文核对后**成立**。后续任何人不得以「读着不对」为由改动，除非能给出反证。

| # | md 写法 | 回原文逐字 | 判定 |
|---|---|---|---|
| 1 | 块 3 用「**迪吉**」指 Digby | 源 `text/ch26_26.txt:69`（chars 1389–1706）`‘Digby’s murder was thoroughly planned…’`；译名「迪吉」是**全书既定译法**：`/usr/bin/grep -oh '迪吉' notes/.../a-fatal-legacy-by-charlotte-vassell/*.md \| sort \| uniq -c` → 120 处，且 ch26 与全书一致（全书无「迪格比」写法） | ✓ 正确，勿改 |
| 2 | 块 3「任何有点脑子的人都会想到」 | 源逐字 `because anyone with half a brain would realise that we would find the footage of Scott at the Post Office.` | ✓ 忠实 |
| 3 | 块 5「制服同事」= Uniform | 源逐字 `Uniform have collected his new starter forms from the bakery.` | ✓ 正确（英式 uniform＝制服警员） |
| 4 | 块 1「这盒饼是他**离开**哈罗盖特时在路上顺手买的」 | 源逐字 `he’d quickly purchased on his way out of Harrogate.` | ✓ 正确（on his way **out**＝离开时，不是「去时」；此坑常被写反） |
| 5 | 块 2「为 Scott Brown 命案**新立起来**的白板」 | 源逐字 `the new whiteboard that had appeared for Scott Brown’s murder.` | ✓ 正确 |
| 6 | 块 5 的三路分工归属 | 源逐字 `Matt, get the staff from The Purple Toad in.`／`Amy, please chase up where his electronics have got to.`／`I’ll deal with that.`（= Caius 处理母亲联系方式） | ✓ 施事/受事方向全对，未见归属反转 |
| 7 | 导航「Matt 从仰头看白板抛出猜想，到盯着白板把斯科特降级成一场交易，最后领到查 The Purple Toad 的活」 | 源逐字 `Matt looked up at the new whiteboard…` → `‘I doubt it,’ Matt said, staring at the board.` → `Matt, get the staff from The Purple Toad in.` | ✓ 三个动作与顺序均对得上 |
| 8 | 导航「Caius 一边说『不』一边犹豫」 | 源逐字 `‘No,’ Caius said, although he hesitated.` | ✓ 正确（犹豫的是 Caius，不是提问的 Matt） |
