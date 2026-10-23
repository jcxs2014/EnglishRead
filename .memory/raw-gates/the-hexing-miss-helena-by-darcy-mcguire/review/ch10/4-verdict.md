# 4-verdict.md · 《The Hexing Miss Helena》第 10 章 审查判定

审查员：主会话自审（**同会话盲区见文末**）｜章型：**cliffhanger 章（章末问句在下一章开头作答）＋ 对话密集章**
抽样理由：快审 `ceil(N/8)` = 4 章（首末必含、等距 1·10·18·27）；本章按「对话跨章落点」类型加权入选，**且是本轮唯一此前未读过 `text/` 的抽样章**。
底稿：`1-suread.json`（R1 先素读，22 条事实／6 组关系／6 处数字／2 处原文自相矛盾）→ `2-machine.json`（R2）→ `3-diff.md`（R3）
源：`text/ch10_chapter_10.txt`（273 行）｜受审：`ch10 the mirrored office.md`（9 块 / 23 条词表）
**R2 退出码 0，verdict `ok`，9/9 引语逐字命中，字符位 14→257→4135→4637→7315→8701→13166→13852→16436 单调递增，无 `…`、无拼接。**

---

## 一、四组计数

| 组 | 计数 | 明细 |
|---|---|---|
| **逐字** | **引语 9 / 9 相符，0 错** | `2-machine.json` 全部 `ok:true`；词表 **23 / 23** 例句逐字回源命中（行号见 `3-diff.md` C12） |
| **对应** | **9 块：9 对应，0 不对应，0 密度不足** | 逐块 R4 三问全部一致：原句 1–2 主体＝辛西娅／辛西娅；原句 3–4 说话人＝**海伦娜**（原句 4 的引语出自海伦娜，md 的中文理解写「她说」并明确指海伦娜 ✓）；原句 5–6 主体＝辛西娅；原句 7 说话人＝**辛克莱**；原句 8 说话人＝辛西娅；原句 9 说话人＝辛西娅。**引语未截短**：原句 7 只取 `:227` 的末段（`:227` 前半是 `'I shall 'eed your warning…'`，md 未引）——被引部分自足 |
| **形态** | **4 / 4 符合，0 偏离** | H1 `# 10. Chapter Ten` ✓｜导航 **5 项** = profile ✓｜子项 **中文理解／关键词／为什么这样写／读者视角提示** 9 块一致 ✓｜块数 **9** ∈ profile 目标 [5,9] ✓，亦 ∈ 本书众数区间 [6,13] ⇒ **无偏离，不需写理由**（`structure.py audit` 对本章无提示） |
| **断言** | **共核 22 条：相符 16 ／ 提示 6 ／ 阻断 0 ／ 跳过 2** | 提示 6 条＝未取用的关键场景（L1–L6，见 `3-diff.md`），非缺陷；跳过 2 条＝原文自相矛盾（不裁决） |

**阻断型条数 = 0。**

---

## 二、判定表（断言 | 证据 | 结论 | 档位）

| # | 断言 | 证据（`text/ch10_chapter_10.txt:行`） | 结论 | 档位 |
|---|---|---|---|---|
| V1 | 本章未取用：醉汉被海伦娜逼退（`:104-110`） | `:104` `Helena moved like mist, stepping in front of her.`；`:104` `A crimson curl had broken free of her twist` | 全章最具动作性的一处戏未进引语与分析；取舍未写理由 | **提示**（只记不改） |
| V2 | 本章未取用：辛西娅以「毒蛇 venom」替海伦娜抬轿并反问辛克莱才智（`:176-182`） | `:176` `Trust me when I tell you, Miss Blair is far more deadly than that venom.`；`:182` `Have I been misled? Are you a fool?` | 本章唯一一次她主动出招，未取用 | **提示**（只记不改） |
| V3 | 本章未取用：她自知「是在拿命钓一个凶手」（`:188`） | `:188` `She was playing a dangerous game, baiting a killer.` | 行动自觉未进分析层 | **提示**（只记不改） |
| V4 | 本章未取用：拒绝落座「这不是一次社交拜访」（`:230`） | `:230` `‘We prefer to stand. This is no social call.’` | 姿态戏未取用 | **提示**（只记不改） |
| V5 | 本章未取用：她自问对女性身体的亲密是否正当（`:260-263`） | `:260` `the intimacy she longed to explore with Helena had nothing to do with platonic friendship`；`:263` `her blood ran rather cold` | 性别自觉整段未取用 | **提示**（只记不改） |
| V6 | 导航「叙事手法」：`胃里的翻涌` | `:35` `going to cast up her accounts`（要吐的前兆）、`:110` `something strange stirred in her belly`（情动） | 两个来源合并成一句概括，「翻涌」兼指二者；不算错但指代含混 | **提示**（措辞） |
| V7 | 原文自相矛盾一：`text/ch10_chapter_10.txt:98` 海伦娜对辛西娅说 `When your uncle is the Superintendent of Scotland Yard, you learn many things` | 全书交叉：`text/ch16_chapter_16.txt:209` `my brother, your uncle, and now you are dictating…`；`text/ch22_chapter_22.txt:156` `your uncle and my brother need no help from me`；`text/ch11_chapter_11.txt:44` `There’s a superintendent at Scotland Yard ’as nieces with the name of Blair. Lachlan MacDougal.` | 「your uncle」在原文里指向不明：按全书其余证据 MacDougal 是**海伦娜与 Clio 的舅舅**（辛西娅的舅舅从未出现），故 `:98` 疑为原书笔误。**md 未引用该句、未据此断言，本审查不裁决原文，只记「书内不一致」** | **跳过**（不裁决） |
| V8 | 原文自相矛盾二：`text/ch10_chapter_10.txt:203` 辛克莱接辛西娅 `:182` 的话却称她 `Miss Blair` | 同一段他另有三处对辛西娅称 `Lady Burrows`／`you`（`:215`、`:227`、`:239` `a pair of women as formidable as you and Miss Blair.`），且 `:167` 他称海伦娜 `Miss Blair` | 疑为原书笔误。**md 只在词表例句逐字引用该句（`acumen` 行），未据此断言** | **跳过**（不裁决） |

### 与原文相符的 16 条断言（避免「只报问题」的不完整交代）

- 十五岁 debutante 见女王：`:35` `presented to the Queen as a debutante at fifteen` ✓
- 首次（很可能也是最后一次）进这种场所、想留下看赌局：`:41` ✓
- 三个男人与一名女子：`:50` ✓；Lady Bucklethorne 领 Society of Genteel Ladies：`:53` ✓
- 辛克莱的保密规矩、管家转身即走＝「这就是答案」：`:59`、`:68`、`:71` ✓
- 赌戏 Bacarat／Macao／hazard、天花板至少两层楼：`:74`、`:77` ✓
- 海伦娜灰眼睛只看辛西娅、扶住她肘部、佛手柑与柠檬皂：`:80` ✓
- 镜子在西墙高处、只反吊灯光、要三十英尺高才看得见倒影：`:89` ✓
- 「不是镜子，是单向观察窗」：`:92` ✓
- 办公室：深色木墙、整面窗、桃花心木书桌、深绿地毯、煤气灯：`:134` ✓
- 「我是肯特米尔侯爵夫人，我不惧怕危险」：`:140` ✓
- 辛克莱全名 Damien Sinclair：`:146` ✓
- 她对辛克莱毫无吸引、直到回头撞上海伦娜的目光：`:149-152` ✓
- 辛克莱「我就死本身」：`:227` ✓
- 债务可转到活着的亲属身上：`:236` ✓
- 章末问句落在下一章开头作答：`:272` → `text/ch11_chapter_11.txt:35` `Sinclair shifted a glass of water on his desk…` ✓

### 机器层

- `chapter.sh --json`：退出码 0，verdict `ok`，`segment_miss=0`、`cjk_low=0`、`keyword_bad=0`、`struct_bad=0`、`quote_long=0`、`template=0`、`hole=0`、`block_count=0`。
- 全书级：`check_vocab` 报 `ch10 the mirrored office.md [基础] 基础档疑含超纲词「threshold」`——`check_vocab.py` 的「≥9 字且不在 BASIC_WORDS/COMMON 表」启发式（脚本 docstring 自述该判据历史假阳率 6/10）。`threshold`（门槛）是本章原词 `:137`，属**假红型**，不修 md。**是否要把 `threshold` 从 ⭐ 基础 提到 ⭐⭐ 进阶，属档位口味，不列缺陷。**

---

## 三、已核实为正确（防误修，下一轮不得以「读着不对」为由改动）

1. **「海伦娜…凭叔叔是苏格兰场警司的见识，在关键时刻把观察窗的秘密交给她」**（导航 人物弧线）——依据 `text/ch10_chapter_10.txt:92`（海伦娜点破观察窗）与 `:98`；虽然 `:98` 原文写的是 `When your uncle is the Superintendent of Scotland Yard`，但全书交叉证据显示 MacDougal 是**海伦娜与 Clio 的舅舅**（`text/ch16_chapter_16.txt:209` `my brother, your uncle`、`:22` … `text/ch22_chapter_22.txt:156` `your uncle and my brother`、`text/ch11_chapter_11.txt:44` `’as nieces with the name of Blair. Lachlan MacDougal.`），故 `:98` 的 "your" 属原书笔误。**md 按全书正确读法写「海伦娜的叔叔」＝成立，不得改成「辛西娅的叔叔」。**
2. **原句 4 的说话人是海伦娜，中文理解写「她说」**（`ch10 the mirrored office.md:50`）——依据 `:89-92`：`Helena` 说完「We’re being watched」后接 `‘They aren’t mirrors…’`，归属明确。**成立。**
3. **原句 7 的说话人是辛克莱**（`:80`）——依据 `:227` `‘I shall ’eed your warning, Lady Burrows, and give your protector ’er dues.’ He nodded at Helena. ‘But know this, your friend might be dangerous, but I am death incarnate…’`。**成立（勿与海伦娜混）。**
4. **原句 9 指向「债有没有起作用」而非「你是不是杀了他」**（`:104` 为什么这样写）——依据 `:272` `Did my husband’s debt to you play a role in his untimely death?`。**成立。**
5. **词表 `acumen` 行逐字引用了 `Miss Blair`**（`:116`）——该处是**原书原文**（`:203`），逐字引用不构成 md 缺陷；不得为了"统一称呼"而改写例句（改例句＝破坏逐字性）。

---

## 四、覆盖声明与已知盲区

- **本章覆盖**：R1 → R2 → R3 → R4（9/9 块）→ R5，**全流程走完**。
- **全书覆盖**：机器层 27/27 章；人判 **ch01 / ch10 / ch18 / ch27 = 4 / 27 章**；其余 23 章**仅机器层**；总览三篇全篇人判。
- **同会话盲区（如实标注）**：本书由本会话在写作期产出；**ch10 的 `text/` 在写作期未被读过**（写作期只回读过 ch01/ch05/ch09/ch12/ch16/ch17/ch18/ch22/ch25/ch26/ch27），故本章的独立性最高；ch01/ch18/ch27 的 `text/` 在写作期读过，本轮仍按「先素读后开 md」执行，但不能视为完全盲态。
- **未做**：深审 R0–R5 全章**未执行**；快审升级条件（§0 四条）未命中（阻断 0 / 写作期用了 `bookform.py --contract` 与 `suread.py` / 机器层无异常信号 / 用户未点名），**未提请升级**。
