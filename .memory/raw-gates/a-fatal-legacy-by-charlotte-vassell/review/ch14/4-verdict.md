# 4-verdict.md · ch14《A Fatal Legacy》审查判定表

- 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch14 the red lion is closing down.md`（**审查当时的文件名**；C1 判该名为凭空情节，已于 2026-10-21 14:26 改名为 `ch14 the special unit is closed down.md`，软链接同步，内容为同一份）
- 唯一权威源：`text/ch14_14.txt`（3,550 字符 / 113 行）
- 落盘：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch14/`
- 档位：**阻断**（与原文不符/缺失，须改）· **提示**（措辞正当，可改可不改）· **假红**（工具判错）· **跳过**（没查）

## 四组数（只报这四组）

| 组 | 分母 | 通过 | 阻断 | 提示 | 假红 | 跳过 |
|---|---|---|---|---|---|---|
| **逐字** | 33（5 引语 + 28 词汇例句） | **33** | 0 | 0 | 0 | 0 |
| **对应** | 5 块 | **5**（含 1 块带阻断级施事错配） | **1** | 2 | 0 | 0 |
| **形态** | 4 项（H1 / 导航 / 子项集 / 块数） | **4** | 0 | 0 | 0 | 0 |
| **断言** | 20 条（事实断言 + 漏 2 条） | 成立 8 | **1** | 11 | 0 | 0 |

**阻断型条数 = 2**（C1 编：文件名 keyplot 凭空情节；E1 错：第 2 块提问者/施事对调）。
提示型 = 11，机器层无假红，**无跳过项**（本机 `chapter.sh --json` 退出码 0、verdict=ok；引语逐字与词汇例句我用独立脚本复核过，不采信机器自证）。

---

## 判定表（断言 | 证据（章:区间） | 结论 | 档）

| # | 断言 | 证据（`text/ch14_14.txt`） | 结论 | 档 |
|---|---|---|---|---|
| A1 | 文件名 keyplot「**the red lion is closing down**」＝Red Lion 酒吧面临关闭 | 全章 113 行无一句说酒吧要关闭；被关闭的是 special unit：`text/ch14_14.txt:38` `‘Nope.’ They’d been summoned to the Chief Superintendent’s office a little over three weeks ago and had been informed of its closure.`；`:53` `He hadn’t mentioned the unit closing beyond uttering ‘Well, that’s that’ in the lift afterwards.`。取证：`/usr/bin/grep -n "Red Lion" text/*.txt` → 仅 `ch14_14.txt:17:The Red Lion Public House`（退出码 0，全书 1 处＝小标题）；`/usr/bin/grep -n -i "closing\|closed" text/*.txt` → 退出码 0，ch14 的两处命中都指专案组 | **不成立（编：凭空情节，且已传播进本次审查任务书）** | **阻断** |
| A2 | 特别行动组被撤销 | `:38` `had been informed of its closure` | 成立 | — |
| A3 | 「**三周前**被宣布关闭」 | `:38` `a little over three weeks ago`（三周**多一点**） | 基本成立，md 取整（数字未逐字） | 提示 |
| A4 | 关闭由 Chief Superintendent 办公室正式告知 | `:38` `They’d been summoned to the Chief Superintendent’s office … and had been informed of its closure` | 成立（md 未点出来源，属可补的省略，不算错） | 提示 |
| A5 | 「**Caius 原本指望**借它查清姐姐下落的机会也就没了」 | `:56` `‘He’s taken the end of the special unit harder than I thought he would. **I think** he saw it as his chance to work out what happened to his sister.’` | 不成立：原文是**马特的推测**，md 导航与总结写成既定事实（同文件第 4 块却正确写成「在马特看来」） | 提示 |
| A6 | 「表面是**三个人同时**松了口气」 | `:41` 只有艾米 `‘I’m so glad it’s been closed down.’ Amy was relieved…`；马特无任何如释重负的表达，反见 `:50` `‘Something will. Hampton’s down but he’s not out.’` | 不成立（群体情绪凭空扩大） | 提示 |
| A7 | 「收尾时**三人各给一句**短答」 | 结尾三句：`:107` `‘Yeah, but he’d drive me insane,’ Caius said…`（凯厄斯的长段，非「一句短答」）、`:110` `‘One weekend perhaps,’ Matt said, being diplomatic.`、`:113` `‘Yeah,’ Amy said, sipping on her dandelion and burdock.` —— 只有马特、艾米两句短答 | 不成立（计数错，凯厄斯没有收尾一句） | 提示 |
| A8 | 「他们失去的正是那个**共同据点**」（指专案组，非酒吧） | `:38`–`:41` + `:50`；`it`/`the unit` 均指专案组 | 成立（md 未把「据点」误指酒吧） | — |
| A9 | Callie 周末要接下的那份 special commission | `:89` `‘On edge. She’s had this special commission come in on the weekend that she’s excited for but it’s stressing her out.’` | 成立 | — |
| A10 | 「凯厄斯姐姐的**失踪**」 | 本章 `:56` 只写 `what happened to his sister`；全书设定 `text/xx_characters.txt:20` `after the unsolved disappearance of his sister Lydia` | 成立（不算编） | — |
| A11 | 「全章凯厄斯一次也没主动提姐姐，是马特替他说破的」 | `his sister` 全章仅 `:56` 一处，说话人是 Matt（`:56` 引语开头 `He’s taken…`）；`:53` 记凯厄斯只说过 `‘Well, that’s that’` | 成立 | — |
| A12 | 「艾米与马特对同一件事的判断并不一致」 | `:41`（庆幸）vs `:50`（`Something will. Hampton’s down but he’s not out.`） | 成立 | — |
| A13 | 「它是这一章**唯一**一处对『事情已经结束』的反驳」 | `:41` `Although to her mind the threat of being dragged into a truly heinous conspiracy would never quite go away now.` —— 第 1 块原句本身即反驳 | 不成立（唯一性断言为假） | 提示 |
| A14 | 邀请「被**两个**客气的说法挡了回去」 | `:110` `‘One weekend perhaps,’ Matt said, being diplomatic.`（唯一的挡回）；`:113` `‘Yeah,’ Amy said, sipping on her dandelion and burdock.`（**应允**，不是挡回） | 不成立（计数错） | 提示 |
| A15 | 「凯厄斯全程用酒名和玩笑挡着」 | `:65` 酒名双关 `‘Matt, I went with a pint of “And Ale Tell You One Thing”. It’s a guest IPA.’`、`:71` `‘And a dandelion and burdock for Miss 1932, here.’`；`:95`–`:103` PMT / netball / Regina George 玩笑 | 成立 | — |
| A16 | 「我快习惯了」（`I’m getting used to it all`）说话人＝**凯厄斯** | `:107` `‘Yeah, but he’d drive me insane,’ **Caius said**, before taking a sip of his pint. ‘I’m getting used to it all. I think I’m going to get too used to it. I’d invite you guys up, but I appreciate that you might not fancy it.’`（谈的是祖宅与其父，不是酒吧） | 成立（说话人核对通过） | — |
| A17 | 第 3 块「**艾米说**，她觉得自己了解凯厄斯的一切」 | `:53` `Amy nodded. She watched Caius at the bar. He hadn’t mentioned the unit closing beyond uttering ‘Well, that’s that’ in the lift afterwards. ‘I feel like I know everything about Caius, and yet I somehow also feel like I know nothing about him either.’` —— 本句无言语动词，紧随叙述句，且前一分句用 `uttering` 明指凯厄斯说出口的话 ⇒ 本句是**心里话** | 不成立（语体：心里话被写成说出口） | 提示 |
| A18 | 第 5 块「作者让主角亲口说出对继承生活的**不安**」 | `:107` 只写 `I’m getting used to it all`（无「不安」）；「不安」是解读 | 解读非事实 | 提示 |
| A19 | **漏**：凯厄斯是否辞职这条线 | `:59` `‘Do you still think he’s going to quit?’`、`:62` `‘Yeah.’ Matt watched Caius from across the pub. ‘His family will make him or maybe even Callie.’`；md 全文无「quit/辞职」 | 漏（唯一新开的剧情问句；`text/xx_characters.txt:20` 「and is surprised he’s still there」与之相扣） | 提示 |
| A20 | **漏**：凯厄斯对 Hampton 的最新态度 | `:83` `‘I have. I left him on read.’`；md 无 | 漏（已读不回＝Hampton 线的最新状态） | 提示 |

### 阻断级两条的原文逐字（供修复方直接改）

**E1（第 2 块中文理解首句，`:28`）**
- md 现文：「**艾米问他**「什么东西会接替它」，马特既没有安慰，也没有顺着说单位没了是好事，只丢下一句断言……」
- 原文逐字（`text/ch14_14.txt:44`–`:50`）：
  > `:44` `‘I wonder what will replace it?’ Matt said off-handedly.`
  > `:47` `‘What do you mean?’`
  > `:50` `‘Something will. Hampton’s down but he’s not out.’`
- 判定：**提问者是马特，反问「What do you mean?」的是艾米**。md 把提问者安到艾米身上（§⑥ 施事/归属反转；四道机器探针全绿，只有 R4 固定三问能抓）。
- 建议改文：「马特随口问『什么会接替它』，艾米反问『你什么意思？』，马特既没有安慰，也没有顺着说单位没了是好事，只丢下一句断言……」

**C1（文件名 keyplot）**
- md 当时名：`ch14 the red lion is closing down.md`（另有同名软链接）——**已于 2026-10-21 14:26 依本条改名**，现为 `ch14 the special unit is closed down.md`（软链接 `ch14 the special unit is closed down -> ch14 the special unit is closed down.md`）
- 原文逐字（唯一与「关闭」相关的两处，均指专案组）：`text/ch14_14.txt:38` `…had been informed of its closure.`；`text/ch14_14.txt:53` `He hadn’t mentioned the unit closing…`
- 建议新名：`ch14 the special unit is closed down.md`（`ch<NN> <keyplot>.md`、单空格、无标点）；同时修软链接与 `00_情感节点.md:56` 「节点五：据点被撤掉之后（ch13-ch14）」的指向。
- **注**：改名会改 URL slug ⇒ 需确认站点链接策略（重定向/改名是否允许）后再动；本审查**未改动书目录任何文件**。

---

## 形态组（逐项，无偏离即不写理由）

| 项 | 本章 | 本书众数 / profile | 结论 |
|---|---|---|---|
| H1 | `# 14. The Red Lion Public House` | 本书 54/54 章同形态 `# NN. <场景小标题>`（ch12 `# 12. Tate Britain`、ch13 `# 13. The Police Station`、ch15 `# 15. Caius and Callie’s Flat`）；与 AGENTS.md「H1 跟随书内既有形态」一致 | 无偏离 |
| 导航项名与项数 | 5 项：一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法 | 全书 54/54 章**同名同序 5 项**（profile 列的第二项为「情感弧线位置」，本书统一用「视角」；以本书众数为准） | 无偏离 |
| 子项集 | 中文理解 / 关键词 / 为什么这样写 / 读者视角提示（4 项，每块齐全，无缺无乱序） | profile `mystery-thriller` subitems 4 项一致，可选项「句子结构」未用（允许） | 无偏离 |
| 块数 | 5 块 | 本书块数中位 **7**，范围 5–10；profile 允许 3–10；5 与 ch21/ch26/ch47/ch53 并列本书最少 | **在范围内，无偏离需理由**（本章为节奏放缓的对话章，5 块合制） |
| 小节 | 本章导航 / 精读 / 本章词汇 / 一句话总结（4 节） | profile `sections` 4 项一致 | 无偏离 |
| frontmatter | `状态: 未读`、`source_text: ch14` | 全书 54/54 章同值 | 无偏离 |

---

## 已核实为正确（防误修护栏：以下写法看着像错，回原文核对后成立，后续任何人不得以「读着不对」为由改动）

1. **「凯厄斯姐姐的失踪」成立**（导航 `:13`）——本章 `text/ch14_14.txt:56` 只写 `what happened to his sister`，但全书人物表 `text/xx_characters.txt:20` 明写 `after the unsolved disappearance of his sister Lydia` ⇒ 「失踪」有据。
2. **「我快习惯了」的说话人是凯厄斯，不是马特也不是艾米**——`text/ch14_14.txt:107` `‘Yeah, but he’d drive me insane,’ Caius said, before taking a sip of his pint. ‘I’m getting used to it all. I think I’m going to get too used to it. I’d invite you guys up, but I appreciate that you might not fancy it.’`（谈祖宅与父亲，**不是**酒吧）。
3. **第 4 块把「查姐姐」标成马特的推测是对的**——`text/ch14_14.txt:56` `I think he saw it as his chance to work out what happened to his sister`，md 写「在马特看来」如实还原了推测语气（**导航与总结层才需补「马特认为」**）。
4. **「专案组关闭」是事实而非推测**——`text/ch14_14.txt:38` `They’d been summoned to the Chief Superintendent’s office a little over three weeks ago and had been informed of its closure.`（关闭时间＝a little over three weeks ago，来源＝Chief Superintendent 办公室）。
5. **引语截到句末不违反规则**——第 4 块舍弃了同一段引语的第三句 `The whole tit-for-tat off-the-books thing meant he could’ve actually had a go but he never really got a chance.`（该句被收进词汇表 `off-the-books` 例句，仍在本章原文中），且分析未涉及该句 ⇒ 不构成「引语选短」；同类截法在 ch15/ch13/ch12 均为全书房规。
6. **「他们失去的正是那个共同据点」指专案组、未误指酒吧**——`:38`–`:50` 的 `it`/`the unit` 均指专案组。
7. **词汇表 28 条例句全部逐字命中本章原文（各 1 次）**——含 `off-the-books`、`subconsciously`、`originator` 三条不在引语块内的例句；例句取自本章即可，不必在引语块内。

---

## 覆盖声明

- **本次人判范围＝仅第 14 章**（R1 素读 → R2 机器层 → R3 三张单子 → R4 逐块 → R5 判定），其余 53 章**只有机器层**，不得据此写「通过」。
- 为判「本书众数」，我统计了全书 54 章的导航项名/项数与块数分布（只读元数据，不作内容判断）。
- 为判「引语截到句末是否房规」，比对了 ch15 / ch13 / ch12 的引语块写法（**在 R1 落盘之后**才读的其他章 md；R1 期间未开任何 md）。
- 为核「语料是否完整」，比对了 `library/*.epub` 的 `OPS/s025-Chapter-014.xhtml` 与 `text/ch14_14.txt`：**逐行一致**（差异仅 epub 页码与一处硬换行）⇒ 语料无缺段、无并章；本章所属分部为 epub 的 `OPS/s021-Part-004.xhtml` = `MONDAY`（任务书写的「A MONDAY IN MAY」是 Part-001 的标题，与本章所属分部不符——**属任务书口径，不是 md 缺陷**）。
- 全程遵守：只写 `.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch14/`；**未改书目录任何 md、未 git add/commit**。
- 未做（跳过型，注明以便下一轮）：全书跨章断言（`00_概述.md` / `00_情感节点.md` / `00_金句精选.md` 的 ch14 相关句未做人判，仅发现 `00_情感节点.md:58` 复述了「三个人同时松了口气」与同一份未加限定的「失去共同据点」说法，**未逐条核**）。

---

## 改名后复核（2026-10-21 收尾，主会话）

- **被审版本**：`ch14 the special unit is closed down.md`，sha256 `962a161977ffdd7c72dfd81f3f9a961e86c7a3cc6d94f64ea1cf77ab529f519e`（14:26:11 改名后版本）。上文「审查对象」一行的旧名是**审查当时**的文件名（按 C1 判它为凭空情节而改名）；**md 内容未被改名动作改动**，本表逐条结论对现名文件同样成立。
- **改名落地**：`ch14 the red lion is closing down.md` → `ch14 the special unit is closed down.md`，同名软链接同步重建（`ch14 the special unit is closed down -> ch14 the special unit is closed down.md`），符合命名约定（`ch<NN> <keyplot>.md`、单空格、无标点）。
- **改名后机器层复跑**：`bash scripts/chapter.sh "<书目录>/ch14 the special unit is closed down.md"` → **退出码 0**，verdict ok；块数 5 ∈ 本书区间 5–10，形态 0 偏离。
- **本表结论**：阻断型 **2 → 0**（C1 文件名编造＝改名；E1 第 2 块提问者/施事对调＝已改），提示型 11 条只记不改。
