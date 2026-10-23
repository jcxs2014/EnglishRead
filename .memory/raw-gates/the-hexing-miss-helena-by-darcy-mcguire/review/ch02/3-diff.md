# 3-diff.md · ch02《the dead marquess》对账三张单子

审查员：主会话自审（**同会话盲区见 4-verdict.md 末节**）｜章型：建立章（接首章现场）
基准：`text/ch02_chapter_2.txt`（269 行，1 基行号）｜底稿：`1-suread.json`（14 事件 / 9 关系 / 6 数字）
R2：`2-machine.json`（`chapter.sh --json` 退出码 0，verdict `ok`）

---

## 一、漏（素读有、md 无）

| # | 素读（原文逐字） | 行 | md | 判定 |
|---|---|---|---|---|
| L1 | `A fact Helena knew well thanks to her mother. Willow Blair had been the prettiest of her three sisters, and the most monstrous.` | :155 | 全文 0 次「Willow」「母亲」 | **不构成阻断**：人物背景一句话，非本章转折 |
| L2 | `Clio’s spells and potions created the coveted beauty products they sold… Helena worked the counter while Clio conjured miracles in the cellar.`／`…since Clio left Blair House to live with her husband.` | :53 | md 未提药铺与布莱尔宅 | **不构成阻断**：场景背景 |
| L3 | `‘Cynthia is not like my mother, or yours.’`／`Not every stranger is an enemy.`（Clio 的心念，被海伦娜当场否掉） | :218、:224 | md 未提这一次被驳回的辩护 | **不构成阻断**：支线心念；但它是「陌生人未必是敌人」这一主题在本章的落点 |
| L4 | `‘Hide the truth!’ Sir Robin nodded his head.`／`Helena raised a brow at the sarcastic raven, whose timing was generally less than ideal.` | :173、:176 | md 只写「使魔斗嘴」，未点名 Sir Robin 的这句 | **不构成阻断**：md 的 Tropes 一句已概括 |

**结论：关键转折 0 漏。** 本章五个关键节拍——鬼魂缺席 → 克莱奥无法指认凶手 → 拉克兰叔叔四条事实 → 海伦娜改读活人的心 → 吊坠现形并指向侯爵夫人——md 全部覆盖（导航「一句话概括」一句串起）。

---

## 二、编（md 有、原文无）

| # | md 写的 | 原文 | 判定 |
|---|---|---|---|
| C1 | 导航·情感弧线位置：「开头还有**使魔与表亲之间的玩笑**」 | 开头 `:38`–`:44` 只有**海伦娜与她的使魔哈姆雷特**（狐狸甩尾巴、嫌血脏、`:44` 她那句冷幽默 `That is, if Lord Hubert Burrows had actually departed.`）；Clio 直到 `:47` 才出现。全章与使魔有关的玩笑另有两处：`:173`/`:176`（Sir Robin 对海伦娜）与 `:260`（`‘Murderer!’ Sir Robin ruffled his feathers at Hamlet, who yipped his reply.`＝两个使魔互呛）。**没有「使魔与表亲」之间的玩笑** | **阻断**（虚构互动） |

---

## 三、错（两边都有但不一致）

| # | md 写的 | 原文 | 判定 |
|---|---|---|---|
| E1 | 导航·一句话概括：「**海伦娜依成色断定**它属于侯爵夫人」 | `:251` 的成色判断在**叙述者**：`The jewellery was far too expensive to belong to anyone but the lady of the house.`；海伦娜本人只说 `:257` `‘It would seem the facts are leading us to Lady Burrows.’` | **提示**（归属偏移：成色判断归叙述者，海伦娜只是顺推结论） |
| E2 | 原句 1·中文理解：「狐狸那种奇特的、**咯咯作响**的低吼」 | `:38` `The strange clicking growl, indicative of foxes` | **提示**（措辞：`clicking`＝咔哒作响；「咯咯」读作轻快笑声，与 fox 的咔哒声不合） |
| E3 | 原句 5·读者视角提示：「……却仍在最后一句**承认自己已经被吸引**」 | 引语原文止于 `:137` `And nothing about Cynthia Burrows was safe.`——该句说的是「不安全」，不含承认；「吸引」的原文在**引语之前**的 `:125` `If Helena could keep her emotions separate from the investigation, she could certainly control her attraction to the suspect.` | **提示**（对应越界：读者视角提示引用了引语外的 `:125`，按 R4 口径属「引语选短」，但影响轻微，建议改写而非扩引语） |

---

## 四、机器层与本轮人判的分工

- `2-machine.json`：`segment_miss=0`、`quote_long=0`、`keyword_bad=0`、`struct_bad=0`、`cjk_low=0`、`hole=0`、`block_count=0`（ch02 6 块 / 2,226 词）。
- 独立复核（本轮自建探针，脚本在 `/tmp`，不入库）：
  - 引语逐字：6/6 命中原文（`/tmp/quote_check_hx.py`），无 `…`、无跨段拼接。
  - 词表例句逐字：22/22 命中（本书用 `## 本章词汇`，**`check_vocab.py` 默认只扫 `## 词汇`，本轮自建探针补上这一盲区**）；词头出现在例句内 22/22。
- 机器层查不出的是 C1（虚构互动）、E1/E3（归属与对应）——**都在中文分析层**。
