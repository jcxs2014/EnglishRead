# 4-verdict.md · 《The Hexing Miss Helena》ch05 审查判定（深审 R0–R5）

审查员：主会话自审（**同会话盲区见文末**）｜章型：单人独处章（内含管家/友人对话）｜档位：**深审**（2026-10-23 用户指令）
底稿：`1-suread.json`（R1 先素读，43 事件 / 9 关系 / 7 数字 / 6 未决）→ `2-machine.json`（R2）→ `3-diff.md`（R3）→ 本表（R4 逐块 ＋ R5）
源：`text/ch05_chapter_5.txt`（183 行）｜受审：`ch05 the bobbies search.md`（7 块 / 词表 22 条）

---

## 一、四组计数

| 组 | 计数 | 明细 |
|---|---|---|
| **逐字** | **引语 7 / 7 相符，0 错** | `2-machine.json`：`segment_miss=0`、`quote_long=0`、`keyword_bad=0`、`keyword_long=0`、`hole=0`；R0 全书级 `verify_fragments_indep.py`：**312 片段 / 0 MISS**（本章含 `…` 的原句 6 逐段独立取证通过）；词表 **22 / 22** 例句逐字回源命中（`## 本章词汇` 不在 `check_vocab.py` 默认扫描域，本轮自建 `/tmp/vocab_check_hx.py` 补验）、**22 / 22** 词头落在例句内（`/tmp/vocab_head_hx.py`） |
| **对应** | **7 块：7 块对应成立，0 越界** | R4 三问（动词主语／受事／归属方向）逐块核对，见 `3-diff.md` §四；密度不足 0 处；未发现「分析讲的是引语之外的上下文」「讲全书主旨」「只复述字面」三类失配 |
| **形态** | **4 / 4 符合，0 偏离** | H1 `# 05. Chapter Five` ✓｜导航 **5 项** ✓｜子项 **中文理解／关键词／为什么这样写／读者视角提示** 4 项一致 ✓｜块数 **7** ∈ 本书区间 **6–13** ✓，亦 ∈ 本章 `block_target:[4,7]` ✓（**已触上限**）；`block_count=0`、`struct_bad=0`、`cjk_low=0`、`template=0` |
| **断言** | **共核 17 条：相符 14 ／ 提示 3 ／ 阻断 0 ／ 跳过 0** | 提示 3 条（E1 导航措辞、E2 中文理解等义性、E3 指代不明）；**阻断型条数 = 0** |

**本章无阻断型缺陷。**

---

## 二、判定表（断言 | 证据 | 结论 | 档位）

| # | 断言 | 证据（`text/ch05_chapter_5.txt:行`） | 结论 | 档位 |
|---|---|---|---|---|
| E1 | 导航·情感弧线位置：「这是案发当天从下午延伸到深夜的一段**独处时光**。」 | `:56` `After the infuriating Miss Helena Blair and Superintendent MacDougal had taken their leave, Clio and Thomas insisted on staying with her for the remainder of the afternoon.`（Clio 与托马斯整下午在场；希金斯太太亦在场至 `:110`） | 与原文**不一致**：全章并非独处 | **提示**（措辞级；同段「一句话概括」已写明「在克莱奥坦白魔法……的余波里」，不构成情节层错误） |
| E2 | 原句 2·中文理解：「证明自己**不止是一块**果冻奶油挞」 | `:74` `before she could show him that she did, in fact, have more backbone than a jelly cream tart` | 「有更多骨气」不等于「不止是一块挞」；中文把「比挞更有骨气」改成「不止是一块挞」，**语义不等价** | **提示**（译法级） |
| E3 | 原句 4·中文理解：「火苗在她**姻亲**的掌心燃起」 | `:119` `she had seen fire flicker to life in her sister-in-law’s palm` | `sister-in-law` 在本章语境指当章坦白魔法的**嫂子 Clio**（`:59` Clio 解释魔法；`:59` `Clio apologised … then explained exactly how her magic worked`）。md 只写「姻亲」，读者无法定位是谁；**指代不明** | **提示**（措辞级） |

### 与原文相符的 14 条断言（避免「只报问题」的不完整交代）

1. 警察搜过辛西娅的套房、尽量不弄乱；希金斯太太怒气冲冲地收拾复位——`:35` ✓
2. 管家抱怨「那些无赖不尊重女士隐私」、扯紧毯子；叙述者称她「用动作与忙碌处理痛苦」，辛西娅钦佩这一点——`:38`、`:47` ✓
3. 管家说要「跑到苏格兰场」告诉警长「你更可能飞上月球而不是杀人」——`:50` ✓
4. Clio 先道歉、再解释魔法如何运作；坦白令她难以承受，但「两人之间再没有秘密」让她略感宽慰——`:59` ✓
5. 休伯特的灵魂**没有逗留**，她永远无法对他说出心里话——`:68` ✓
6. 愤怒叠在震惊之上、压倒悲伤；她恨他抢先把自己弄死——`:74` ✓
7. 管家「我想不出谁会想杀伯罗斯勋爵」——`:77` ✓
8. 辛西娅点破赌局、洗衣女工的「蜂蜜加杜松子酒」、情妇与「必定树敌」——`:83` ✓
9. 管家「反正不是你，谁说不是就是该死的蠢货」→ 僵住 → 小狗摆件倒扣 → 道歉——`:98` ✓
10. 每晚一小杯白兰地「 hardly damage a reputation already in tatters」；休伯特不在，没人再审核她的要求——`:113` ✓
11. 「是那只狐狸。我知道。哈姆雷特。」＋掌心之火、集体亮起的灯无法归因于煤气线 ⇒ 听见狐狸不再荒唐——`:119` ✓
12. 「三条刺眼的不当理由」（丈夫被杀当天不该觉得某人迷人／女士不该觉得另一位女士迷人／对方还是女巫）＋「也许是海伦娜下了爱情咒」——`:128-137`、`:140` ✓（原文两处均为「未证实」的猜测，md 保留了这个不确定）
13. 吊坠来历：第二次公开约会、父亲指示她必须答应、婚后第二个月他带着别的女人的香气与雪茄杜松子酒味回家、她扯下吊坠砸向他、他嘲笑她破碎的天真——`:149` ✓
14. 「我已没有悲伤……从婚姻第一天到最后一天他一直是残酷的陌生人」＋「享受这次跌落」的宣言＋打开吊坠回望十年后肺里的空气全部涌出、末句 `‘That bastard.’`——`:146`、`:173`、`:176-182` ✓

---

## 三、已核实为正确（防误修，下一轮不得以「读着不对」为由改动）

1. **「莉莉被辞退」**（原句 1·中文理解「可女仆已被辞退」；导航·为什么这样写「第二句把莉莉、她被辞退这件事和乱作一团的仆役串起来」）——`:35` `Usually, Lily would be putting her to bed, but with the lady’s maid sacked …`；`/usr/bin/grep -n -w -E "Lily|lady’s maid" text/ch05_chapter_5.txt` → 唯一命中 `:35`；`/usr/bin/grep -n -w "Lily" text/ch01_chapter_1.txt` → `:56 she told Cynthia Lily had been dismissed.`、`:59 Lily was an excellent maid.`（退出码 0）；ch16 `:65` 另作 `Lily had recently been a young maid in the household`。⇒ **被辞退的侍女即莉莉，md 写法成立**，不得据素读阶段的怀疑去改。
2. **「小狗摆件」**（原句 3·中文理解「那只小狗摆件还倒扣在她手里」）——`:98` 原文即 `She froze, the puppy upside down in her hands.`，中英对位一致。素读阶段担心的 `:44` `spaniels`（西班牙猎犬摆件）是**另一处**（壁炉架上的摆件群），md 本章并未把「小狗」用于那一处，**不构成缺陷**。
3. **「原句 6 的省略号跳过的是大段往事」**（原句 6·为什么这样写）——`:149` 原文中 `In the madness of the afternoon, Superintendent MacDougal had never reclaimed the damning piece of evidence.` 与 `Then Hubert came home early one morning, two months into their marriage, …` 之间被 `…` 跳过的正是求婚/定情/婚后两个月的前情：**成立**。
4. **「省略号两侧均为原文」**（原句 6）——R0 全书级 `verify_fragments_indep.py` 312 片段 / 0 MISS 覆盖：**成立**。
5. **「管家用『damn fool』把体面撕开一道口子」**（原句 3·为什么这样写）——`:98` `anyone who says differently is a damn fool`，且紧接 `She froze, the puppy upside down in her hands.`：**成立**。
6. **「生气比悲伤先到场」**（导航·情感弧线位置；原句 2·读者视角提示）——`:74` `Rage layered over her shock and vastly dominated her grief.`：**成立**。
7. **「欲望与发现女巫同级」**（原句 5·为什么这样写）——`:122` `Which was nearly as shocking as discovering witches in her midst.`：**成立**。
8. **「享受坠落＝主动选择」**（原句 7·为什么这样写）——`:173` `I’m going to bloody well enjoy the fall.`：**成立**。
9. **词表 22 条例句全部逐字取自本章**——**成立，不得改写例句**（本轮 22/22 逐字回源命中、22/22 词头在例句内）。

---

## 四、覆盖声明与已知盲区

- **本章覆盖**：R1 素读（先于任何 md 打开，43 事件 / 9 关系 / 7 数字 / 6 未决）→ R2 机器层 → R3 三张单子 → R4 逐块 7/7 → R5 判定表，**全流程走完**。
- **本书覆盖（深审进度）**：批 1 = ch02 / ch03 / ch04，批 2 = ch05 ⇒ **4 / 27 章**已完成 R0–R5（ch05 为第 4 章）。其余 23 章**只有机器层**（R0 全书级已跑），**未做人判**，不得写成「已审查」。
- **同会话盲区（如实标注）**：本书由本会话在写作期产出，本章亦为写作期读过的章之一；本次仍执行「先素读、写完 `1-suread.json` 才开 md」，但**不能视为完全盲态**。
- **本章特有盲区**：本会话自行补写的 `/tmp/vocab_check_hx.py`、`/tmp/vocab_head_hx.py` 两个探针**不入库**（raw-gates 只放结论层），其口径（词表例句逐字回源、词头落在例句内）在本章成立，但**未经第二实现交叉验证**——下一轮若改动 `## 本章词汇` 节，须以同样口径复验。
- **未做**：五步审查附录 B（a–e 全文）已被 `审查表.md` 归档取代，不重复执行。
