# 4-verdict.md · 《The Hexing Miss Helena》ch06 审查判定（深审 R0–R5）

审查员：主会话自审（**同会话盲区见文末**）｜章型：双 POV 并置章（家庭群像＋受问场景）｜档位：**深审**（2026-10-23 用户指令）
底稿：`1-suread.json`（R1 先素读，72 事件 / 17 关系 / 7 数字 / 7 未决 / 10 陷阱）→ `2-machine.json`（R2）→ `3-diff.md`（R3）→ 本表（R4 逐块 ＋ R5）
源：`text/ch06_chapter_6.txt`（325 行）｜受审：`ch06 the blair women table.md`（10 块 / 词表 22 条）

---

## 一、四组计数

| 组 | 计数 | 明细 |
|---|---|---|
| **逐字** | **引语 10 / 10 相符，0 错** | `2-machine.json`：`segment_miss=0`、`quote_long=0`、`keyword_bad=0`、`keyword_long=0`、`hole=0`；R0 全书级 `verify_fragments_indep.py`：**312 片段 / 0 MISS**（本章含 `…` 的原句 6 逐段独立取证通过）；词表 **22 / 22** 例句逐字回源命中（`## 本章词汇` 不在 `check_vocab.py` 默认扫描域，本轮自建 `/tmp/vocab_check_hx.py` 补验）、**22 / 22** 词头落在例句内（`/tmp/vocab_head_hx.py`） |
| **对应** | **10 块：10 块对应成立，0 越界** | R4 三问（动词主语／受事／归属方向）逐块核对，见 `3-diff.md` §四；密度不足 0 处；未发现「分析讲的是引语之外的上下文」「讲全书主旨」「只复述字面」三类失配 |
| **形态** | **4 / 4 符合，0 偏离** | H1 `# 06. Chapter Six` ✓｜导航 **5 项** ✓｜子项 **中文理解／关键词／为什么这样写／读者视角提示** 4 项一致 ✓｜块数 **10** ∈ 本书区间 **6–13** ✓（众数位），亦 ∈ 本章 `block_target:[6,10]` ✓（**已触上限**）；`block_count=0`、`struct_bad=0`、`cjk_low=0`、`template=0` |
| **断言** | **共核 21 条：相符 16 ／ 提示 5 ／ 阻断 0 ／ 跳过 0** | 提示 5 条（E1 措辞、E2 无据「连夜」、E3 引用被省略内容未披露、E4 视角描述不完整、E5 词表释义）；**阻断型条数 = 0** |

**本章无阻断型缺陷。**

---

## 二、判定表（断言 | 证据 | 结论 | 档位 |

| # | 断言 | 证据（`text/ch06_chapter_6.txt:行`） | 结论 | 档位 |
|---|---|---|---|---|
| E1 | 原句 1·为什么这样写：「也把海伦娜放回一个由**女性长辈围坐**的位置」 | `:35` `Women cut herbs at this table, knitted together the fabric of their family … Blair women strung together like beads of amber, stretching back to the 1600s, all gathered here to share burdens from the past, devise plans for the future, and savour the sweetness of the present, safe in the circle of sisterhood that bound them.` | 围坐者是**历代布莱尔女巫（含海伦娜自己与后代）**，非围在她身边的长辈；md 的「由女性长辈围坐」与原文不符 | **提示**（措辞级） |
| E2 | 导航·一句话概括：「辛西娅穿着**连夜染黑**的丧服」 | `:201` `The hasty dye job didn’t completely hide the pattern of what had once been her favourite day dress. … Her laundress had done the best she could with so little time` | 原文只写「仓促的染色」「时间不多」，**无「连夜」**；md 同文件末尾「一句话总结」写的是「穿着染黑的丧服」，**md 内部亦不一致** | **提示**（措辞级） |
| E3 | 原句 6·为什么这样写：「黑痕不匀，旧花样仍透出来，**白底蓝花与蕾丝被具体点出**」 | `:201` `A white and blue floral affair with lace around the collar and sleeves.` —— md 引语以 `…` 跳过该句 | 分析引用了**引语中被 `…` 省略的内容**而未披露省略；同段其余分析（黑痕不匀、原花样透出）均在引语内 | **提示**（分析层披露不足；与 ch04 E1「前端截短」不同类） |
| E4 | 导航·叙事手法：「前半贴海伦娜，靠厨房里的对话和日常动作推进」 | `:110–117` 以**埃莉的认知为锚**（`She was well aware of Lord Burrows’ murder, as there were no secrets amongst the Blair women, but her particular powers would be of no help in the investigation.`）；`:119` 才回到海伦娜内心（`She promised herself she would visit Barty’s Confectionery …`） | 前半并非单视角；md 的原句 4 正出自该段（其中文理解本身正确） | **提示**（视角描述不完整） |
| E5 | 本章词汇·⭐基础 `air` 释义「空气」 | `:113` `Ellie was tied to the air, and that ephemeral element aided in her disconcertingly accurate visions of the future.`（另见 `:89` 海伦娜＝水、`:167` 姨妈＝土） | 此处 `the air` 指**风元素**，释义只给「空气」会让读者以为普通空气 | **提示**（词表释义级） |

### 与原文相符的 16 条断言（避免「只报问题」的不完整交代）

1. 樱桃木桌代代相传、划痕与污渍「讲述祖先历史」、布莱尔女巫可追到 1600s——`:35` ✓
2. 罗恩姨妈端来蒲公英茶并命令「喝」；茶有净化之效、用蜂蜜与她的治愈之力调甜——`:38`、`:41` ✓
3. 埃莉带着雪白雪貂奥菲利娅冲进厨房、「你的气场有点……不对劲」——`:47`、`:53` ✓
4. 气场描述的三次改口（shimmery→murky→foggy）与「摔跤与飞翔的区别在于最后那声巨响」——`:56–68` ✓
5. 「我还能操控我的元素」＋水涡扫过房间、给所有植物洒露水＋姨妈「你总是浇得太多」、植物集体颤抖——`:83–92` ✓
6. 「只读不了她的」＋辛西娅变成 hex、plague 渗入感官、忍冬与香草、绿与褐的条纹——`:95` ✓
7. 「我还没那么在乎那个女人到要去讨厌她的地步」＝叙述者点破的「Liar」——`:101–104` ✓
8. 埃莉主动替班、叙述者评「这份心意非常厚道」、海伦娜「像个忘恩负义的人」——`:116` ✓
9. 辛西娅「搅动她灵魂里平静的水面」，海伦娜「一点也不喜欢」——`:185` ✓
10. 童年七个蒙福年头、十六岁离乡间庄园上 finishing school、白桦条——`:246`、`:252` ✓
11. 染黑的花裙盖不住原花样＋守丧服配色与**两年社交隔离**——`:201`、`:207` ✓
12. 守寡第一夜：银色月光、夏夜歌声、井然有序的生活惊人地碎裂、「她开始记起」——`:255` ✓
13. Cotswold 附近的寡居宅邸、一街外的联排住宅、年金、婚后保留的父亲遗产——`:267` ✓
14. 拒绝考虑定罪的可能＋「麦克杜格尔警司和他那位让人恼火（又漂亮）的**侄女**」＋「脆弱而令人敬畏的自由礼物」——`:273` ✓
15. 手指相触 ⇒「萤火虫在血液里炸开」的比喻＋比昨天更强、诱人三倍——`:279`、`:282` ✓
16. 辛西娅抢先发问「你会施什么魔法」、语气装轻松实则急切＋海伦娜末句「我读心思」——`:300`、`:324` ✓

---

## 三、已核实为正确（防误修，下一轮不得以「读着不对」为由改动）

1. **「表亲」指埃莉**（原句 4·中文理解「反倒是她的表亲主动提出替她顶明天的班」）——`:116` `so her cousin could accompany Uncle Lachlan to interview Lady Burrows`；`:98` 埃莉称 Clio 为 `my new sister-in-law` ⇒ 表亲＝埃莉：**成立**。
2. **「侄女」指海伦娜**（原句 8·中文理解「麦克杜格尔警司和他那位……侄女」）——`:273` `Superintendent MacDougal and his infuriating (beautiful) niece` ⇒ 叔侄关系：**成立**。
3. **「萤火虫」是比喻而非实写**（原句 9·中文理解「像有萤火虫在她血液里炸开」）——`:279` `Fireflies erupted in Cynthia’s bloodstream` 为通感写法；md 用「像有」已标明比喻：**成立**。
4. **「忍冬」是 honeysuckle 的合法译法**（原句 3·中文理解「闻到的全是忍冬与香草」）——`:95` `all she could smell was honeysuckle and vanilla`：**本章成立**。（⚠️ ch07 与 ch25 同一英文词写作「金银花」，属**跨章术语不统一**，进汇总修复指令文件，不在本章改。）
5. **「罗温姑妈」是本书既有用法**（导航·人物弧线、原句 4 等）——本章英文为 `Aunt Rowan`；⚠️ ch24/25/26 与总览三篇写作「姨妈」，属**跨章术语不统一**，进汇总文件，本章不改。
6. **「守寡第一夜」的时间锚**（原句 7）——`:255` `on the first night of her widowhood`；`:243` `after her discovery the night before` 与 ch05 末尾打开吊坠同一夜：**成立**。
7. **「被问话的人抢先向问话者发问」**（导航·Tropes 反转之一）——`:300` `she determined to attack first … ‘Tell me, what magic do you conjure?’`：**成立**。
8. **「能读人心的女巫偏偏读不到她最想读的人」**（导航·Tropes 反转之一）——`:95` `I can read people’s thoughts. Just not hers.`：**成立**。
9. **「该悲伤的寡妇在守寡第一夜感到的是自由」**（导航·Tropes 反转之一）——`:255`、`:261` `Completely free.`、`:264` `How could she pretend sadness after experiencing such a rush of unadulterated joy?`：**成立**。
10. **词表 22 条例句全部逐字取自本章**——**成立，不得改写例句**（22/22 逐字回源命中、22/22 词头在例句内）。
11. **原句 3 引语的收束位置**——md 引语在 `pixie-shaped eyes.` 处收住，与原文 `:95` 一致（原文其后还有听觉一句，md 未取，见 `3-diff.md` L6）；**引语本身逐字正确，不得擅自补齐或改写**。

---

## 四、覆盖声明与已知盲区

- **本章覆盖**：R1 素读（先于任何 md 打开，72 事件 / 17 关系 / 7 数字 / 7 未决 / 10 陷阱）→ R2 机器层 → R3 三张单子 → R4 逐块 10/10 → R5 判定表，**全流程走完**。
- **本书覆盖（深审进度）**：批 1 = ch02 / ch03 / ch04，批 2 = ch05 / ch06 ⇒ **5 / 27 章**已完成 R0–R5（ch06 为第 5 章）。其余 22 章**只有机器层**（R0 全书级已跑），**未做人判**，不得写成「已审查」。
- **同会话盲区（如实标注）**：本书由本会话在写作期产出，本章亦为写作期读过的章之一；本次仍执行「先素读、写完 `1-suread.json` 才开 md」，但**不能视为完全盲态**。
- **本章特有盲区**：E3（分析引用被 `…` 省略的内容）与 ch04 E1（引语前端截短）**同属「分析越出引语」族但不同类**，本轮按「省略号已标示省略」判为提示；该判据是本会话自定、**未经第二实现或异实例复核**，若下一轮有人主张按 ch04 同判为阻断，须先统一判据再批量改。
- **未做**：五步审查附录 B（a–e 全文）已被 `审查表.md` 归档取代，不重复执行。
