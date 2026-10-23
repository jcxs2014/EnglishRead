# 3-diff.md · ch04《a frigid touch》对账三张单子

审查员：主会话自审（**同会话盲区见 4-verdict.md 末节**）｜章型：对话密集章（揭密场景）
基准：`text/ch04_chapter_4.txt`（336 行，1 基行号）｜底稿：`1-suread.json`（30 事件 / 10 关系 / 4 数字）
R2：`2-machine.json`（`chapter.sh --json` 退出码 0，verdict `ok`）

---

## 一、漏（素读有、md 无）

| # | 素读（原文逐字） | 行 | md | 判定 |
|---|---|---|---|---|
| L1 | `She closed her eyes, knowing they would be bright silver, but Cynthia’s thoughts remained hidden as the electric current increased…`／`During the entire encounter, Cynthia’s thoughts were still hidden from Helena.` | :41、:50 | 引语层未取；导航「却被一股电流般的力量逼得松手」＋人物弧线「走到承认自己根本读不到她」已点到 | **不构成阻断** |
| L2 | `‘We are witches. Aunt Rowan, Ellie, Helena, and I.’`／`‘I do. Because it is true. Look at the evidence in front of you, Cynthia. Clio is a witch, and I love her all the more for it.’` | :149、:155 | 引语层未取；原句 6 结尾「她们的巫术就这样露了出来」已覆盖揭晓本身 | **不构成阻断**：但**托马斯当场接受**这一步缺席，值得留意 |
| L3 | `‘At the Duchess of Devon’s house party. When we were investigating Viscount Beachley’s murder.’`／`‘I asked him to keep my secret until I could share it with you at the right time.’` | :164、:194 | 原句 7 的上下文（辛西娅追问「你为什么不早告诉我」）隐含此事，但引语层未取 | **不构成阻断**：背景补充 |
| L4 | `This time, her efforts were met with a sharp smack of power.` | :296 | 引语层未取；导航与人物弧线已覆盖「读心再次被弹开」 | **不构成阻断** |

**结论：关键转折 0 漏。**

---

## 二、编（md 有、原文无）

**本组 0 条。** 导航五项、十条引语的分析层逐句回原文核对，未发现凭空的情节、关系或数字。

---

## 三、错（两边都有但不一致）

| # | md 写的 | 原文 | 判定 |
|---|---|---|---|
| E1 | 原句 7·中文理解：「**辛西娅咽了一下，纤细的喉咙收紧，又挺直肩膀，慢慢呼出一口气，才转向哥哥托马斯。**」；原句 7·为什么这样写：「开口之前先写身体：**吞咽、喉咙收紧、挺肩、缓缓呼气**，把一场质问前的紧张全放在她身上。」 | 原句 7 的引语从 `'Thomas. I stood with you…` 起算；被分析的四个身体动作在 **引语起点之前**（引语未含 `…`，是**前端截短**）：`:188` `Cynthia swallowed, her delicate throat constricting as she squared her shoulders. She exhaled slowly before addressing her brother. ‘Thomas. I stood with you…` | **阻断**（引语截短：分析覆盖的原文比引语长；按 R4 应「引语选短了，退回创建卡 §2 ①」） |
| E2 | 原句 2·中文理解：「辛西娅先反问一句**"你说的都是些什么鬼话"**」 | `:65` `‘You don’t say? What the bloody hell is going on?’`——原句是**两句**：`You don’t say?`（讥讽的反问「得了吧／是吗？」）＋ `What the bloody hell is going on?`；中文把两句并成一句「你说的都是些什么鬼话」，既吞掉了反问句，也把第二句的语气换了 | **提示**（直接引语误判／跨句合并） |
| E3 | 原句 8·读者视角提示：「**她没有抱住谁**，只往后靠、摇了摇头，语气却已经把屋里的敌意按住」 | `:200` `The proper lady pulled Clio into a tight hug. ‘You can never lose me, Clio. …’`——**辛西娅把克莱奥紧紧搂进怀里**，就在同一行、引语起点之前三句 | md 断言的「没有抱住」被同一行原文直接推翻；引语未含拥抱动作，是**前端截短＋否定断言错** | **阻断** |

---

## 四、机器层与本轮人判的分工

- `2-machine.json`：`segment_miss=0`、`quote_long=0`、`keyword_bad=0`、`struct_bad=0`、`cjk_low=0`、`hole=0`、`block_count=0`（ch04 10 块 / 3,056 词，`block_target:[6,10]`）。
- 独立复核（探针在 `/tmp`，不入库）：
  - 引语逐字：10/10 首尾与整串均可在原文定位；其中 **原句 4、6、8、9、10 共 5 条含 `…`**，逐段取证：**每一片段各自是原文中的连续串**（片段数 15，`segment_miss=0`）；本轮另用差分探针把每条省略号两侧的锚点定位回原文行，确认省略掉的中间句均为原文、且分析层未引用它们。
  - 词表例句逐字：22/22 命中；词头在例句内 22/22。
- 机器层查不出的是 **E1（截短）**——`segment_miss=0` 只证明引语逐字，证明不了「分析越出了引语」。
