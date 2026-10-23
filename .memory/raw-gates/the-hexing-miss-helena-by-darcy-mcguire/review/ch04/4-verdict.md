# 4-verdict.md · 《The Hexing Miss Helena》ch04 审查判定（深审 R0–R5）

审查员：主会话自审（**同会话盲区见文末**）｜章型：对话密集章（揭密场景）｜档位：**深审**（2026-10-23 用户指令）
底稿：`1-suread.json`（R1 先素读，30 事件 / 10 关系 / 4 数字）→ `2-machine.json`（R2）→ `3-diff.md`（R3）→ 本表（R4 逐块 ＋ R5）
源：`text/ch04_chapter_4.txt`（336 行）｜受审：`ch04 a frigid touch.md`（10 块 / 词表 22 条）

---

## 一、四组计数

| 组 | 计数 | 明细 |
|---|---|---|
| **逐字** | **引语 10 / 10 相符，0 错** | `2-machine.json`：`segment_miss=0`（片段数 15）、`quote_long=0`；独立探针再验 10/10；**原句 4/6/8/9/10 共 5 条含 `…`，逐段独立取证：每一片段各自是原文中的连续串**（R0 全书级 `verify_fragments_indep.py`：312 片段 / 0 MISS）；词表 **22 / 22** 例句逐字回源命中（`## 本章词汇` 不在 `check_vocab.py` 默认扫描域，本轮自建探针补验），词头在例句内 22/22 |
| **对应** | **10 块：9 块对应，1 块越界（阻断）** | R4 三问（动词主语／受事／归属方向）逐块核对；**原句 7 的中文理解与「为什么这样写」分析的是引语起点之前的原文**（E1）——按 R4「讲的是引语之外的上下文 → 引语选短了」；**原句 8 的读者视角提示含一条被原文推翻的否定断言**（E3）；密度不足 0 处 |
| **形态** | **4 / 4 符合，0 偏离** | H1 `# 04. Chapter Four` ✓｜导航 **5 项** ✓｜子项 **中文理解／关键词／为什么这样写／读者视角提示** 4 项一致 ✓｜块数 **10** ∈ 本书区间 **6–13**（众数 10，即众数位）✓，亦 ∈ 本章 `block_target:[6,10]` ✓；`block_count=0`、`struct_bad=0` |
| **断言** | **共核 17 条：相符 13 ／ 提示 1 ／ 阻断 2 ／ 跳过 0** | 阻断 2（E1 截短、E3 否定断言错）＋提示 1（E2） |

**阻断型条数 = 1。**

---

## 二、判定表（断言 | 证据 | 结论 | 档位 |

| # | 断言 | 证据（`text/ch04_chapter_4.txt:行`） | 结论 | 档位 |
|---|---|---|---|---|
| E1 | 原句 7·中文理解「辛西娅咽了一下，纤细的喉咙收紧，又挺直肩膀，慢慢呼出一口气，才转向哥哥托马斯」＋「为什么这样写」的「开口之前先写身体：吞咽、喉咙收紧、挺肩、缓缓呼气」 | `:188` `Cynthia swallowed, her delicate throat constricting as she squared her shoulders. She exhaled slowly before addressing her brother. ‘Thomas. I stood with you when your reputation was in tatters. …’`；md 引语起点为 `'Thomas.` | 被分析的四个身体动作全在**引语之外**（前端截短，非省略号省略） | **阻断** |
| E2 | 原句 2·中文理解：「辛西娅先反问一句"你说的都是些什么鬼话"」 | `:65` `‘You don’t say? What the bloody hell is going on?’` | 原句为两句：讥讽反问 `You don’t say?` ＋ `What the bloody hell is going on?`；中文并成一句并换了语气 | **提示**（直接引语误判） |
| E3 | 原句 8·读者视角提示：「**她没有抱住谁**，只往后靠、摇了摇头」 | `:200` `The proper lady pulled Clio into a tight hug. ‘You can never lose me, Clio. …’` | 同一行原文写明辛西娅**把克莱奥紧紧搂进怀里**；md 的否定断言被原文直接推翻 | **阻断** |

### 与原文相符的 13 条断言（避免「只报问题」的不完整交代）

- 抓住手的触感是「冰冷湖水＋电鳗」、力量电流穿过却不肯松手：`:35` ✓
- 辛西娅的命令口气「无法忽视」、海伦娜「从不对命令反应良好」：`:68` ✓
- 海伦娜她们**不向巫团与血亲以外的人**透露能力，且她「曾犯过一次错、代价致命」：`:77` ✓
- 克莱奥把辛西娅认作**家人**：`:80` `‘She is family now, Helena. And she needs to understand.’` ✓
- 巫师团四位：**Ellie、海伦娜、罗恩姨妈、Clio**：`:89`、`:149` ✓（本书 ch02:212 亦作 `Aunt Rowan`）
- 辛西娅否认杀人且「绝不会让朋友或家人陷入险境」：`:110` ✓
- 蓝火由「flickered」到「flared」、露在掌心：`:137` ✓
- 托马斯当年在**德文公爵夫人的乡间派对**上查出 Clio 是女巫，当时在查**比奇利子爵的谋杀案**：`:164` ✓
- 辛西娅当年为托马斯与整个上流社会对峙（duchess／viscountess／marchioness／debutante 四层头衔）：`:188` ✓
- 托马斯认错：「I never doubted your loyalty, Cyn. I should have told you.」：`:191` ✓
- 辛西娅说「你现在是我姐姐了、秘密由我守着」并拥抱 Clio：`:134`、`:200` ✓
- 克莱奥的判断「她不是嫌疑人，辛西娅什么也没做错」出自托马斯：`:224` ✓
- 拉奇兰叔叔的原话是苏格兰方言 `‘I’m not accusin’ her. But I canna’ claim her innocence withou’ proof.’`、以及明天问话、林肯出庭：`:287`、`:266`、`:320` ✓

---

## 三、已核实为正确（防误修，下一轮不得以「读着不对」为由改动）

1. **「sister 把姻亲关系改写成她一直想要的姐妹」**（原句 8·为什么这样写）——依据 `:200` `‘You can never lose me, Clio. I have longed for a sister who would love Thomas the way he deserved.’`；「姻亲」这一层由 ch02:86 `Lady Cynthia Burrows, Clio’s new sister-in-law.` 与 ch03:152 `Cynthia’s eyes widened as she turned to her brother.` 支撑：**成立**。
2. **「省略号跳过的是她对这门婚事的评语」**（原句 8·为什么这样写）——依据 `:200` 省略号两侧为 `… the way he deserved.` 与 `Nothing can change that.’`，中间被跳过的是 `From the moment we met, I knew you were perfect for my brother, and your friendship has been a boon to me.`：**成立**（省略号两侧均为原文，且分析未越界）。
3. **「省略号跳过她对自己的解释」**（原句 10·为什么这样写）——依据 `:323` 与 `:329` 之间被跳过的是 `Especially after the way she had already treated the marchioness. … Which was another reason to tell Uncle Lachlan of her inability…`：**成立**。
4. **「水旋先于问话到达」**（原句 9·为什么这样写）——依据 `:245`→`:248` 的先后顺序：**成立**。
5. **「语气却已经把屋里的敌意按住」**（原句 8·读者视角提示后半句）——依据 `:200`–`:203`（辛西娅拥抱后「往后靠、摇头」，随后 `:202` 全体反应）：**成立**。⚠️ 同一条提示的**前半句「她没有抱住谁」已判为 E3 阻断**，不得据本条保留前半句。
6. **「收束落在她没说出口的辩解上」**（导航·叙事手法）——依据 `:335` `Cynthia’s snort of derision made reading her thoughts unnecessary. Not that Helena noticed. Or cared.`：**成立**（末句是海伦娜未说出口的否认）。
7. **词表 22 条例句全部逐字取自本章**——**成立，不得改写例句**。注：`serene` 的例句 `And yet you stand here, serene and accepting.` 恰是原句 9 被 `…` 省掉的句子，**两处并不冲突**（词条例句独立取自原文）。

---

## 四、覆盖声明与已知盲区

- **本章覆盖**：R1 素读（先于任何 md 打开）→ R2 机器层 → R3 三张单子 → R4 逐块 10/10 → R5 判定表，**全流程走完**。
- **本书覆盖（深审进度）**：批 1 = ch02 / ch03 / ch04（**3 / 27 章**已完成 R0–R5）。其余 24 章**只有机器层**（R0 全书级已跑），**未做人判**，不得写成「已审查」。
- **同会话盲区（如实标注）**：本书由本会话在写作期产出，本章亦为写作期读过的章之一；本次仍执行「先素读、写完 `1-suread.json` 才开 md」，但**不能视为完全盲态**。
- **未做**：五步审查附录 B（a–e 全文）已被 `审查表.md` 归档取代，不重复执行。
