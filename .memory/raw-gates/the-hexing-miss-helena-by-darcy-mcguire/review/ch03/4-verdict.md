# 4-verdict.md · 《The Hexing Miss Helena》ch03 审查判定（深审 R0–R5）

审查员：主会话自审（**同会话盲区见文末**）｜章型：对话／审问章（前半辛西娅 POV，后半海伦娜 POV）｜档位：**深审**（2026-10-23 用户指令）
底稿：`1-suread.json`（R1 先素读，21 事件 / 12 关系 / 6 数字）→ `2-machine.json`（R2）→ `3-diff.md`（R3）→ 本表（R4 逐块 ＋ R5）
源：`text/ch03_chapter_3.txt`（346 行）｜受审：`ch03 helena calls on cynthia.md`（9 块 / 词表 22 条）

---

## 一、四组计数

| 组 | 计数 | 明细 |
|---|---|---|
| **逐字** | **引语 9 / 9 相符，0 错** | `2-machine.json`：`segment_miss=0`、`quote_long=0`；独立探针再验 9/9 命中原文；**原句 7 的 `…`（`heard… nothing.`）是原文自带的省略号，两侧各自命中**，非跨段拼接；词表 **22 / 22** 例句逐字回源命中（`## 本章词汇` 不在 `check_vocab.py` 默认扫描域，本轮自建探针补验），词头在例句内 22/22 |
| **对应** | **9 块：9 对应，0 不对应，0 密度不足** | R4 三问（动词主语／受事／归属方向）逐块核对通过；含 4 块引语（`原句 3/4/7/8`）为叙述者引语，动作主语与原文一致 |
| **形态** | **4 / 4 符合，0 偏离** | H1 `# 03. Chapter Three` ✓｜导航 **5 项** ✓｜子项 **中文理解／关键词／为什么这样写／读者视角提示** 4 项一致 ✓｜块数 **9** ∈ 本书区间 **6–13**（众数 10），亦 ∈ 本章 `block_target:[5,9]` ✓；`block_count=0`、`struct_bad=0` |
| **断言** | **共核 17 条：相符 13 ／ 提示 3 ／ 阻断 1 ／ 跳过 0** | 阻断 1（C1）＋提示 3（E1、E2、L2） |

**阻断型条数 = 1。**

---

## 二、判定表（断言 | 证据 | 结论 | 档位 |

| # | 断言 | 证据（`text/ch03_chapter_3.txt:行`） | 结论 | 档位 |
|---|---|---|---|---|
| C1 | 导航·人物弧线：「辛西娅从自责失礼的女主人，走到**用粗话命令管家**、当面顶回海伦娜」 | `:140` `‘Hodges, have Cook make a tray of sandwiches.’`；`:146` `Cynthia rolled her eyes. ‘Yes. Fine. Brandy as well, if you must. Thank you.’`；`:149` `The butler bowed, his cheeks flushing slightly as he shut the door behind him.`；粗话在 `:152` `‘Now, will someone please tell me what the bloody hell is going on here?’`（管家已退场，且是对满屋人说的） | 命令管家全程客气；**粗话既不在那个场景、也不是对管家说的**，属动作与说话人归属错 | **阻断** |
| E1 | 一句话总结：「本想用一枚沾血的吊坠**撬开对方的嘴**」 | `:258` `She had only pulled out the locket to rattle Cynthia and see if that knocked loose whatever was blocking Helena’s power to read her thoughts.` | 吊坠的用途是**摇松封锁让读心生效**，不是让辛西娅开口；因果归属偏移 | **提示** |
| E2 | 原句 1·读者视角提示：「一头**浓烈的红发**」 | 同块中文理解「焦赭、铜红，还带一点绯」＝`:35` `burnt umber, copper, a hint of crimson` | 同一块内前后口径不一（`焦赭`≠`红发`） | **提示**（措辞） |
| L2 | 分析层未覆盖 `:294`–`:333`（辛西娅认领项链并说明来历、叔叔的心里话、托马斯护妹、Clio 背书、辛西娅自述婚姻疏离） | `:294` `‘It is mine. I won’t try to deny it. … I gave it back several months after we were married.’`；`:315` `‘You can’t think Cynthia killed her husband just because of a locket.’`；`:333` `‘…I don’t know why he was in possession of my locket, but I do know I didn’t kill him.’` | md 六块引语按 `:170 → :194 → :222 → :249 → :345` 排列，跨过了整段辩解回合；导航「当面顶回海伦娜」已点到，故事线不缺，故不判阻断 | **提示**（覆盖偏薄） |

### 与原文相符的 13 条断言（避免「只报问题」的不完整交代）

- 海伦娜与狐狸发色同为「垂死太阳的颜色」：`:35` ✓
- 海伦娜此前拒绝辛西娅的一切示好（茶会／沙龙／花园派对／Gunter's 与 Rotten Row）：`:41` ✓（词表 `overture` 例句即此句）
- 辛西娅自责「失职」并自认是「合格的女主人」：`:62` ✓
- 房中「只有他们五个」、声音不属于房中任何人：`:74` ✓
- 狐狸舔嘴的动作被辛西娅读成「智力的闪光」：`:77` ✓
- 管家叫 **Hodges**，辛西娅夺回吩咐权：`:131`、`:140` ✓
- 读深了时虹膜会变银并发光：`:225` `She knew her irises would lighten to silver and glow when she accessed her magic to delve so deeply into someone’s head` ✓（「水系读心者」这一条出自 ch02:110 `As a waterwitch, Helena’s powers…`，**ch03 未重述**，不得挂在本章名下）
- 辛西娅的念头三次读不到（`:222`、`:234`、`:339`），而房里其他人的念头全都能读：`:279` ✓
- **魔宠不会离开自己的女巫**：`:246` ✓
- 魔法通常沿**母系**遗传，也有非魔法家族女性自发显能的例外：`:267` ✓
- 项链是金底红宝石、盘着金蛇：`:288` ✓
- 辛西娅的说法：约会时休伯特所赠、婚后几个月就还了回去：`:294` ✓
- 辛西娅是「肯特莫尔侯爵夫人」、是「正经而端庄」的一方：`:306`、`:333` ✓

---

## 三、已核实为正确（防误修，下一轮不得以「读着不对」为由改动）

1. **「一个在明处发火，一个在暗处发慌」**（导航·情感弧线位置）——依据 `:152` 辛西娅当众发火 vs `:219` `Helena tried very hard to keep the panic at the bay.`／`:255` `Except bloody everything!` 海伦娜独处时才崩：**成立**。
2. **「读心者偏偏读不到嫌疑人，而她的使魔主动倒向对方膝头」**（导航·Tropes）——依据 `:237` `And then her familiar left her side to put his head on Cynthia’s fecking lap.`、`:279` `Every mind in the elegantly decorated room was open to her. Except Cynthia’s.`：**成立**。
3. **「她认定这次接触一定能击碎那位端庄侯爵夫人身上的所有屏障」**（原句 9·中文理解）——依据 `:345` `The contact was sure to shatter whatever shields were protecting the proper and staid marchioness.`：**成立**（`staid`＝端庄古板，与词表释义「拘谨稳重」一致）。
4. **「省略号让沉默有了长度」**（原句 7·读者视角提示）——依据 `:222` 原文即写 `heard… nothing.`：**成立**（这是原文自带的省略号，不是拼接）。
5. **「克莱奥、托马斯与麦克杜格尔警司也在这间屋里」**（导航·一句话概括）——依据 `:50` Clio 进门、`:95` 麦克杜格尔在场、`:107` 托马斯落座：**成立**。
6. **「这枚吊坠在她手里像诱饵，而不是礼物」**（原句 5·读者视角提示）——依据 `:258` `She had only pulled out the locket to rattle Cynthia and see if that knocked loose whatever was blocking Helena’s power to read her thoughts.`＋`:291` `‘Go on, take it. If it’s yours.’ Helena was baiting her.`：**成立**（注：这条**反着印证 E1**——吊坠的用途是摇松封锁，故一句话总结的「撬开对方的嘴」需改）。
7. **词表 22 条例句全部逐字取自本章**——**成立，不得改写例句**。

---

## 四、覆盖声明与已知盲区

- **本章覆盖**：R1 素读（先于任何 md 打开）→ R2 机器层 → R3 三张单子 → R4 逐块 9/9 → R5 判定表，**全流程走完**。
- **本书覆盖（深审进度）**：批 1 = ch02 / ch03 / ch04（**3 / 27 章**已完成 R0–R5）。其余 24 章**只有机器层**（R0 全书级已跑），**未做人判**，不得写成「已审查」。
- **同会话盲区（如实标注）**：本书由本会话在写作期产出，本章亦为写作期读过的章之一；本次仍执行「先素读、写完 `1-suread.json` 才开 md」，但**不能视为完全盲态**。
- **未做**：五步审查附录 B（a–e 全文）已被 `审查表.md` 归档取代，不重复执行。
