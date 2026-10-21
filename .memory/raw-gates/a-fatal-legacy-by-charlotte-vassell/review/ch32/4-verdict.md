# 4-verdict.md · ch32《A Fatal Legacy》审查判定表

- 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch32 eulalia watches from her window.md`
- 权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch32_32.txt`（8569 字符 / 178 行，章节小标题 `Priory Square`，场景分隔符 `* * *` 在 line 166）
- 读取顺序：先只读 `text/ch32_32.txt` → 落盘 `1-suread.json`（22 条事件 / 12 条人物关系 / 12 条数字逐字）→ 才开 md（铁律未破）
- 落盘：本目录（`1-suread.json` / `2-machine.json` / `3-diff.md` / `4-correspondence.md` / `4-verdict.md`）。**未改书目录任何 md，未 git add/commit。**
- 机器层：`bash scripts/chapter.sh "…/ch32 eulalia watches from her window" --json > 2-machine.json` → **退出码 0**，`verdict: ok`，`counts: blocks 7 / segments 7 / segment_miss 0 / struct_bad 0 / empty_quote 0 / keyword_bad 0 / cjk_low 0`，`issues` 四项皆空。

---

## 一、四组数（只报这四组）

| 组 | 数 | 依据 |
|---|---|---|
| **逐字** | **7/7 引语块逐字命中** | `2-machine.json` 7 段 `ok:true`；审查方另以独立脚本 `quote in src` 逐条复核 7/7（4-correspondence.md 末表）。7 块**均为单段引语、无省略号缝合**（每块 `segments` 长度=1），故「省略号第二三段伪造」这一类不适用。 |
| **对应** | **7/7 对应** | 逐块人判（4-correspondence.md）：引语选短 0 块；讲全书主旨/作者生平 0 块；只复述字面（密度不足）0 块。7 块均有「为什么这样写」实写内容，`cjk_ratio` 最低 0.75、最高 0.94。 |
| **形态** | **0 偏离** | H1 `# 32. Priory Square`；导航 5 项（**视角 / 一句话概括 / 线索结构 / 人物弧线 / 叙事手法**，按本书众数）；子项集 = 中文理解 / 关键词 / 为什么这样写 / 读者视角提示（4 项＝众数＝profile，可选「句子结构」未用）；块数 7＝本书中位 7（54 章实测区间 5–10）。**偏离项：无。** 另记一条非机器轴的一致性提示：同分部 THURSDAY 的 ch27/28/29/30/31/33/34 都在「一句话概括」里写了"分部「THURSDAY」"，**ch32 未写**（ch35 亦未写）→ 提示。 |
| **断言** | **核查 31 条；不符 2 条（均阻断）；提示 4 条（漏 1 · 时序 2 · 解读 1）；余 25 条成立** | 明细见下表 §二。**阻断型条数 = 2**（均在导航「视角」「为什么这样写」层，不触及任何引语与词条）。 |

---

## 二、断言逐条（断言 | 证据（章:区间） | 结论 | 档位）

> 证据格式：`text/ch32_32.txt:<行>`（+ 字符区间）。**每条阻断均附原文逐字**（R5 硬约束）。
> 无逐字证据者一律不判阻断。

### 2.1 本章专属判据（任务点名核对项）

| # | 断言（md 位置） | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | 她在**二楼**窗前（md:11「自家二楼窗前」、md:21「自家二楼卧室的窗前」） | `text/ch32_32.txt:20`（chars 36–243）："standing at her bedroom window **on the second floor**" | 一致 | 跳过（已核实为正确） |
| A2 | 她看了**一小时**（md:11「看了一小时」、md:21「看了一个钟头」） | `text/ch32_32.txt:20`："She’d been watching the scene unfold for **the last hour**." | 一致 | 跳过（已核实为正确） |
| A3 | 原文是「**不愿去练瑜伽**」这句；md 是否写反 | `text/ch32_32.txt:20`（chars 428–774）："**Eulalia didn’t want to do yoga. Not today anyway.**" | md **未写反，但也未写**——原句 2 引语止于 "…left nothing to the imagination."，全篇无此句 | **提示**（漏，见 3-diff 漏 1） |
| A4 | 「同时」的写法＝命案与琐事叠在同一视野 | `text/ch32_32.txt:20` 同一段内："watching the police carry **another body** out the front of one of the neighbouring houses" → "The corpse being carried away was the end of the scene. The curtains fell closed. She stepped away and put on the workout clothes…" → "running her hand down her **concave stomach**" | md:11「挤在同一个视野里」、md:30「用『窗帘落下』的动作把命案关在窗外」、md:111「平起平坐」——与原文机制一致 | 跳过（成立） |
| A5 | 她后来确实上了那节瑜伽课（用于判断 A3 只能写成"不想"而非"拒绝"） | `text/ch32_32.txt:77`："‘Amala’s downstairs for our session.’"；`:171`："Eulalia stepped out of her **post-yoga shower**." | 成立 | 跳过（成立） |

### 2.2 事实断言（导航 / 摘要层）

| # | 断言（md 位置） | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| A6 | 「视角：第三人称限知，**全程贴着欧拉莉亚**」（md:12） | `text/ch32_32.txt:35`："She just thought that the pile of shredable adoration went some way to placate her sister’s ego…"；`:83`："**She was annoyed at her sister’s morbidity.** It sold records but the Guardian-reading masses should try to live with it."；`:149`："**Mel was concerned.** Had her sister done or said something? Thank God for the NDA."；`:155`："**Mel felt mean**, but her sister had to learn." | **与原文相反**：本章至少 4 处进入梅尔内心（其中 `:83` 处**就在 md 自己的原句 4 引语内**，并被 md:42 译成梅尔的心思）。md 内部亦自相矛盾 | **阻断** |
| A7 | 「控制线（药片、母亲的卡、那个**被人用假身份买下的邮箱框**、'我在替你投资'）」（md:13） | 本章 `text/ch32_32.txt:95`："someone bought a **dodgy** fucking PO Box on Mum’s card."；全书 `text/ch09_9.txt:89`："‘**Bogus name**,’ … ‘The PO Box.’"；`text/ch45_45.txt:51`："purchased using **Beverley’s credit card**"；`:54`："someone who was calculating enough to **steal someone’s identity**" | 概括与全书事实一致（假名登记＋盗卡），**不判编** | 假红风险（已核实为正确，勿改） |
| A8 | 「命案线（窗外又抬出一具尸体、警灯、"another body"里的"又一具"、那个"又在车引擎盖上指挥下属"的人）」（md:13） | `:20`："another body"、"perched on the car bonnet, dashing as he commanded his subordinate about"；`:86`："There were **loads of flashing lights**." | 一致（"他"未被擅自点名 ✓） | 跳过（成立） |
| A9 | 「渴望线（卡莉第二天要做的演示、烛光晚餐、城堡里打雉鸡喝波特酒）」（md:13） | `:155`："Calliope is going to present to me, umm, you and the cosmetics people **tomorrow**"；"cosy candlelit suppers"；"her boyfriend’s castle shooting pheasants and quaffing port" | 一致（"tomorrow"＝第二天 ✓；城堡属"她男朋友"✓） | 跳过（成立） |
| A10 | 「人物弧线」次序：从"我觉得卡莉不喜欢我""我这个人太多了"**到**藏药 | `:86` 藏药 → `:140` "I don’t think Callie likes me." → `:146` "I’m too much." | md 的时序句式与原文相反（原文先藏药后自怜）；作性格轨迹读可通 | **提示** |
| A11 | 「叙事手法」：先用**一个不间断的长段**把"看见尸体"和"换上运动服"接在一起，**中间不加任何评论**（md:15） | `:20` 整段（chars 36–774）含窗外尸体→换运动服→愧疚开关→镜子与敲门，段内无叙述者评论 | 成立 ✓ | 跳过（成立） |
| A12 | 同上：「**随后**交给密集的引号对话推进（梅尔的"愧疚开关"、她对卡莉的刻薄）」（md:15） | 愧疚开关五句在 `:20` 长段**之内**，早于 `:23` 起的正式对话；"对卡莉的刻薄"在 `:155` | "愧疚开关"位置错标（属长段而非"随后"） | **提示** |
| A13 | 「一句话概括」：换瑜伽服、藏药、跟姐姐争钱和卡莉（md:11） | `:20` workout clothes；`:86` "put the tablets in her bra"；`:95`–`:125` 钱与卡之争；`:140` Callie | 一致 | 跳过（成立） |
| A14 | 「一句话总结」：最后赤身裸体坐在地上把自己写成一颗等着被掰开的熟无花果（md:111） | `:174`："Eulalia sat on her floor naked. She opened her laptop up and started writing."；`:177`："She was going to skip lunch and instead parade her flat stomach around the house all afternoon"；`:171`："She smelled like a ripe fig…" | 一致 | 跳过（成立） |
| A15 | 原句 4「为什么这样写」：「**姐姐在隔壁房间**说"人一直都在死"」（md:44） | `:29`："Mel opened the door but **didn’t step into the room**."；`:35`："Mel **dumped a pile of letters** … on **her sister’s dressing table**."；被引台词 `:83`："‘Where?’ **Mel asked.**" | **与原文不符**：梅尔先不入房、随后进到**同一房间**，从未在"隔壁房间" | **阻断**（轻微，一处措辞） |
| A16 | 原句 4「为什么这样写」：命案被降格成产品卖点、"读者视角提示"引述"这能卖唱片"（md:44–45） | `:83`："She was annoyed at her sister’s morbidity. **It sold records** but the Guardian-reading masses should try to live with it." | 一致 | 跳过（成立） |
| A17 | 原句 7「为什么这样写」：「**这不是谁施加的暴力，是她自己摆好的姿势**」（md:65） | 引语本身是被动、外部施事："She **could be smashed** into mere pulp any minute by **a firm, grasping hand**." | 解读比原文绝对；文本并未说无人施加（场景依据为 `:174`–`:177`，方向可通） | **提示** |
| A18 | 原句 5「读者视角提示」：藏药"这周"＝常态而非一次性发作（md:52） | `:86`："not for the first time that week" | 一致 | 跳过（成立） |
| A19 | 原句 6「为什么这样写」：列举本身就是伤害、逐条宣布妹妹与那些无缘（md:58） | `:155`："You’ll never get invited round for cosy candlelit suppers… You’re not going to spend the weekend at her boyfriend’s castle…" | 一致 | 跳过（成立） |
| A20 | 原句 3「为什么这样写」：拿族裔当讨好妹妹的谈资 + 施恩与指责焊在一起（md:37） | `:20`："‘she’s actually fucking Indian’; ‘I go above and beyond for you over and over again and you don’t give a shit.’" | 一致 | 跳过（成立） |
| A21 | 原句 1「为什么这样写」：叙述者一句评论也不给（md:23） | `:20` 引语区间内无叙述者评语 | 一致 | 跳过（成立） |
| A22 | 原句 2「为什么这样写」：重大事件与琐事之间没有过渡句（md:30） | `:20` "The curtains fell closed. She stepped away and put on the workout clothes…" 无过渡句 | 一致 | 跳过（成立） |
| A23 | 原句 1「读者视角提示」：记住这个窗口和这条视线（md:24） | 读者提示类，不涉事实断言 | 成立 | 跳过 |
| A24 | 原句 2「读者视角提示」：决定权其实握在楼下的人手里（md:31） | 解读性提示，未与原文冲突 | 成立 | 跳过 |
| A25 | 原句 5「为什么这样写」："这份自由具体指什么，文本没有说破"（md:51） | `:86` "looming freedom" 全文未指明所指 | 一致（未编造） | 跳过（成立） |

### 2.3 引语内的事实（逐块回原文复核）

| # | 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|---|
| A26 | 妹妹与姐姐的身份方向（md 全篇"姐姐"指梅尔、"妹妹"指欧拉莉亚） | `:35` "her sister’s dressing table"；`:44` "Mel cut **Eulalia** off"；`:56` "Mel handed **her sister** the glass of water"；`:150` "her sister had to learn" | 一致，未写反 | 跳过（成立） |
| A27 | 原句 3 五句引语均为梅尔所说 | `:20` 引号内 5 句均接在 "Mel had turned on the guilt tap though, flooding her bedroom with" 之后 | 说话人归属正确 ✓ | 跳过（成立） |
| A28 | 原句 4 的提问者是梅尔（md:42「"哪儿？"梅尔问」） | `:83`："‘Where?’ **Mel asked.**" | 一致（本章"说话人"专项通过） | 跳过（成立） |
| A29 | 原句 6 的展示者是卡莉奥佩、对象含梅尔本人 | `:155`："**Calliope** is going to present **to me**, umm, you and the cosmetics people tomorrow" | 一致；md 用第一人称"向我"转述梅尔的话，自洽 ✓ | 跳过（成立） |
| A30 | 原句 7 的被动施事是"一只用力抓握的手"（外部），md 中文未把它安到别人头上 | `:171`："by a firm, grasping hand" | 一致 ✓ | 跳过（成立） |
| A31 | 词汇表 26 条例句 | 审查方脚本逐条 `例句 in text/ch32_32.txt` | **26/26 命中本章原文**，无跨章搬例、无手写编造、词形与原文一致 ✓ | 跳过（成立） |

---

## 三、档位统计

| 档位 | 条数 | 明细 |
|---|---|---|
| **阻断** | **2** | ① A6 导航「视角」断言"全程贴着欧拉莉亚"与原文相反（且与 md 自己的原句 4 自相矛盾）；② A15 原句 4「为什么这样写」"姐姐在隔壁房间"位置与原文相反 |
| 提示 | 5 | A3（漏·「不愿做瑜伽」未写）、A10（人物弧线时序倒置）、A12（"愧疚开关"位置错标）、A17（"不是谁施加的暴力"解读过强）、形态组「分部 THURSDAY 未标注」 |
| 假红 | 0 | 机器层无报警（退出码 0，issues 全空）；本审查方亦未产生工具类误报 |
| 跳过 | 25 | 未发现问题的断言（见 §二 A1/A2/A4/A5/A7/A8/A9/A11/A13/A14/A16/A18–A31 及成立项） |

**最要紧的一条**：**A6（导航「视角」）**。理由：它是全章唯一被"叙述方式"支撑、却与原文直接相反的断言——本章至少 4 处进入梅尔内心（`text/ch32_32.txt:35`、`:83`、`:149`、`:155`），其中 `:83` 正是 md 自己在原句 4 里逐字引用、并译成"她对妹妹这份阴郁有点不耐烦"的那一句；导航说"全程贴着欧拉莉亚"，等于把本章实为**双视角交替**（欧拉莉亚的病态 × 梅尔的功利）写成了单线限知，直接影响读者对"梅尔是否也在算计"的理解。

---

## 四、覆盖声明（哪些查了、哪些没查）

- **本章（ch32）**：R1 素读（22 事件）→ R2 机器层（`chapter.sh --json`，退出码 0）→ R3 三张单子 → R4 逐块对应（7/7）→ R5 断言 31 条，**本章为完整人判，非抽样**。
- **词表层（S4）**：26 条例句逐条回原文校验，**全量**（非抽样）。
- **未查**：本书其他 53 章**只有机器层**，未做人判；总览三篇（`00_概述.md` 等）本次**未查**；跨章断言只在与本章直接相关处（PO Box 身份、`posho hat girl`、Callie/Calliope 拼写）做了取证核对，取证命令与输出见 3-diff.md §四。
- **本章未跑**：`verify_corpus.py`（非本章职责，语料层由生产方在动笔前跑）；`corruption_scan.py`（本次未改任何 md）。

## 五、R5-补 · "零命中"类断言的取证（三件套）

本报告未使用任何"全书查无/零命中"型断言。文中出现的跨章取证命令与输出：

```
/usr/bin/grep -rn "PO Box" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ | head -20
  → 命中 27 行（ch04:83 / ch05:72,99,114 / ch07:152 / ch09:89 / ch16:259 / ch19:20 / ch21:32 / ch25:224 / ch31:74,101 / ch32:95,113,116 / ch37:44 / ch45:51,54 / ch52:389）；退出码 0
/usr/bin/grep -rn "dodgy" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ | head
  → 命中 8 行（ch02:393 / ch13:165 / ch16:181 / ch31:101 / ch32:95 / ch33:319 / ch44:74 / ch47:59）；退出码 0
/usr/bin/grep -rn "posho hat" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ | head
  → 命中 1 行（text/ch32_32.txt:35）；退出码 0
```
（用显式路径 + `/usr/bin/grep`，未用 `git grep`；`text/` 被 `.gitignore` 排除，默认忽略规则的 rg/git grep 在此目录永远"查无"。）

---

## 六、已核实为正确（防误修，固定一节；**后续任何人不得以"读着不对"为由改动**）

> 本节与 3-diff.md §四 同源，此处按 R5.5 固定格式重列。每条给 `text/<文件>:<行>` 与原文。

1. **"被人用假身份买下的邮箱框"（md:13）不是编造** — 本章 `text/ch32_32.txt:95`："someone bought a **dodgy** fucking PO Box on Mum’s card."；全书佐证 `text/ch09_9.txt:89`："‘**Bogus name**,’ Caius said, adding it to the board. ‘The PO Box.’"、`text/ch45_45.txt:51`："purchased using **Beverley’s credit card**"、`:54`："steal someone’s identity"。**勿改成"可疑的邮箱框"。**
2. **"二楼"成立** — `text/ch32_32.txt:20`："on the second floor"。
3. **"看了一个小时/一个钟头"成立** — `text/ch32_32.txt:20`："She’d been watching the scene unfold for the last hour."
4. **"灌水不吞药""这周不是第一次"成立** — `text/ch32_32.txt:86`："Eulalia put the tablets in her bra – not for the first time that week – and swallowed a huge gulp of water that made her cough. … She didn’t need the pills any more."
5. **梅尔是姐姐、欧拉莉亚是妹妹，未写反** — `text/ch32_32.txt:56`："Mel handed **her sister** the glass of water."；`:44`："Mel cut Eulalia off"。
6. **"卡莉"与"卡莉奥佩"是同一人的两种英文写法，不是两个人** — `text/ch32_32.txt:140`："I don’t think **Callie** likes me." 与 `:155`："**Calliope** is going to present to me…"。
7. **原句 4 的提问者是梅尔（"‘Where?’ Mel asked."），不是欧拉莉亚** — `text/ch32_32.txt:83`。
8. **词汇表 26 条例句全部逐字出自本章**（审查方独立脚本复核 26/26 命中）。
9. **"命名/众数"项：导航第 2 项用"视角"是本书众数，不是偏离** — 同书 ch01/ch06/ch31/ch33/ch42 的导航第 2 项均为"**视角**"（genre profile 里的"情感弧线位置"是本书未采用的备选项）。

---

## 七、修复建议（若执行方要改，只改这三处 + 可选补写）

1. **必改 1（阻断）** md:12 导航·视角 → 改为"以欧拉莉亚为主视角，梅尔的内心有四处插入（`text/ch32_32.txt:35 / :83 / :149 / :155`），本章实为双视角交替"。
2. **必改 2（阻断）** md:44 "姐姐在隔壁房间" → 改为"姐姐就在她房间里"（依 `:29`"didn’t step into the room"→`:35` 已在妹妹房内）。
3. **宜改（提示）** md:14 人物弧线次序与原文时序对齐（藏药 `:86` → 卡莉 `:140`/`:146` → 裸坐写故事 `:174`）；md:15 "愧疚开关"从"随后"移到"长段之内"。
4. **宜补（提示）** 原句 2 引语可延到 "Eulalia didn’t want to do yoga. Not today anyway."，把"她不想做"这半块"同时"补上；导航「一句话概括」可加"分部「THURSDAY」"以与同分部 ch27/28/29/30/31/33/34 一致。
