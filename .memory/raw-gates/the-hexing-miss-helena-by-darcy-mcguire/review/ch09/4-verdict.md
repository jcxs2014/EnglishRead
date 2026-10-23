# 4-verdict.md · 《The Hexing Miss Helena》ch09 审查判定（深审 R0–R5）

审查员：主会话自审（**同会话盲区见文末**）｜章型：门口拦截章＋关系推进章＋收束章｜档位：**深审**（2026-10-23 用户指令）
底稿：`1-suread.json`（R1 先素读，266 行全读，72 事件 / 13 关系 / 7 数字 / 7 未决 / 10 陷阱）→ `2-machine.json`（R2）→ `3-diff.md`（R3）→ 本表（R4 逐块 ＋ R5）
源：`text/ch09_chapter_9.txt`（266 行）｜受审：`ch09 into the devils den.md`（9 块 / 词表 22 条）

---

## 一、四组计数

| 组 | 计数 | 明细 |
|---|---|---|
| **逐字** | **引语 9 / 9 相符，0 错** | `2-machine.json`：`segment_miss=0`、`quote_long=0`、`keyword_bad=0`、`keyword_long=0`、`hole=0`；R0 全书级 `verify_fragments_indep.py`：**312 片段 / 0 MISS**（本章 9 条引语**均无 `…`**，自建探针确认，无省略号片段可取证）；词表 **22 / 22** 例句逐字回源命中（`## 本章词汇` 不在 `check_vocab.py` 默认扫描域，本轮自建 `/tmp/vocab_check_hx.py` 补验：`ch09: rows=22 missing=0`）、**22 / 22** 词头落在例句内（`/tmp/vocab_head_hx.py`，无输出＝零失配） |
| **对应** | **9 块：9 块对应成立，0 越界** | R4 三问（动词主语／受事／归属方向）逐块核对，见 `3-diff.md` §四；密度不足 0 处；未发现「分析讲的是引语之外的上下文」「讲全书主旨」「只复述字面」三类失配 |
| **形态** | **结构 4 / 4 符合；引号配对 1 处偏离** | H1 `# 09. Chapter Nine` ✓｜导航 **5 项** ✓｜子项 **中文理解／关键词／为什么这样写／读者视角提示** 4 项一致 ✓｜块数 **9** ∈ 本书区间 **6–13** ✓，亦 ∈ 本章 `block_target:[5,9]` ✓（**已触上限**）；`block_count=0`、`struct_bad=0`、`cjk_low=0`、`template=0`；**引号配对**（机器层零覆盖，自建 `/tmp/pair4_hx.py` 全书扫描）全书仅 1 处孤儿闭引号，落在本章原句 7 ⇒ 见 F1 |
| **断言** | **共核 26 条：相符 20 ／ 提示 2 ／ 阻断 4 ／ 跳过 0** | 阻断 4 条＝E1（故事层动作与原文相反）＋E2（叙事层结构断言与原文不符）＋L1（关键转折缺失）＋F1（引号配对偏离）；提示 2 条＝E3（英文歧义）、E4（措辞级） |

**本章有阻断型缺陷 4 条。**

---

## 二、判定表（断言 | 证据 | 结论 | 档位）

| # | 断言 | 证据（`text/ch09_chapter_9.txt:行`） | 结论 | 档位 |
|---|---|---|---|---|
| E1 | 导航·一句话概括：「海伦娜心里冒出一个『我的』，**又把它压了回去**」＋一句话总结：「她心里冒出一句『我的』，**又硬生生按了回去**」 | `:245` `Mine.` → `:248` `The primitive instinct resonated in her bones.` → `:251` `She blinked hard.` → `:254` `What madness is this?` → `:257` `She was water in a glassy pool.` → `:260` `But not now. **Need coalesced with anger**, rising like a wave mighty enough to crash upon the shore and destroy her enemies. It was chaos and power and glory.` → `:263` `She would reclaim her calm later.` → `:266` `This night, she would ride the crest of her magic into the heart of a devil’s lair.` | 原文里她**没有把念头压下去**：`But not now` 明写「不是现在」，`She would reclaim her calm later` 明写平静是「**以后**再取回」，全章收在**与怒气凝聚成攻势、骑着魔法的浪峰闯进魔鬼老巢**上。md 自身亦自相矛盾：原句 9·为什么这样写写「本能先替她**答了话**」、读者视角提示写「已经撑不住了」 | **阻断**（故事层动作与原文相反） |
| E2 | 导航·叙事手法：「**章末**用一串独立成段的短句收束，**最后落到一个单词**」＋原句 9·读者视角提示：「整章的试探、争辩、靠近，**最后落在这么一个短促的词上**」 | `:245` `Mine.` 之后仍有 `:248`/`:251`/`:254`/`:257`/`:260`/`:263`/`:266` 共 **7 段**，末句 `:266` 是**完整句** `This night, she would ride the crest of her magic into the heart of a devil’s lair.` | 「落到一个单词」成立的位置是 `:245`（占全章约 92% 处），**不是章末**；md 把中段的一个段落当成了全章收束。口径证据：同字段在 ch08 写的是「章末用一次沉默和一句短念收束」，与 ch08 `:308`/`:314` 严丝合缝 ⇒ 本字段的口径＝**原文章末** | **阻断**（叙事层结构断言与原文不符） |
| L1 | （漏）md 未覆盖 `:248`–`:266` 的**七段收束** | `:248` `The primitive instinct resonated in her bones.`／`:251` `She blinked hard.`／`:254` `What madness is this?`／`:257` `She was water in a glassy pool.`／`:260` `But not now. Need coalesced with anger…`／`:263` `She would reclaim her calm later.`／`:266` `This night, she would ride the crest of her magic into the heart of a devil’s lair.` | md 9 个引语块**最末一块是 `:245` 的 `Mine.`**；这段收束既是本章的动作落点（海伦娜整夜进巢的决心），也是 E1／E2 两处误判的**共同根因**。属关键转折缺失 | **阻断** |
| F1 | （形态）原句 7 引语块内层以 `’` 结尾 ⇒ 孤儿闭引号 | `:212` `Cynthia raised a chestnut eyebrow. ‘And I couldn’t give a fig what those gossiping ninnies say about me. I’ve recently discovered that maintaining the standards of a proper lady hardly fits the life of a widow. **I’m tired of letting other people’s opinions control my choices. And that includes you, Helena Blair. Think of me what you will. I’m not your problem to solve or your pawn to control.’**` —— md 引语为 `"I’m tired of … your pawn to control.’"`，外层是直双引号 `"`，内层末尾多出 `’`（原文的闭引号），**开引号 `‘` 被切掉时一并丢了** | 全文只有此处有开引号缺失导致的孤儿闭引号。体例对照：ch08 原句 7 同样从对白中间切起（`We’ve been tryin’ to get something on Sinclair…`）但**末尾不带 `’`** ⇒ 本库对「切段引语」的规定是连同闭引号一起去掉 | **阻断**（引号配对偏离） |
| E3 | 原句 1·中文理解：「可**没有裙撑、裙摆又是开衩的**，行动起来更方便」＋读者视角提示：「**开衩是为了跑动**」 | `:35` `but the **lack of** bustle and split skirts would allow greater ability to manoeuvre` —— 英文 `the lack of bustle and split skirts` 语法上 `lack of` 统辖两项（＝**没有**裙撑、**没有**开衩裙摆） | 英文本身歧义，md 取的是另一读法（骑装惯例：有开衩、无裙撑），与实物相合 ⇒ **不判错**，但须留记，以免下一轮被当成错改 | **提示** |
| E4 | 导航·Tropes：「海伦娜**自称只是来阻止麻烦**」 | `:38` `I’m just doing this to stop the foolish woman from getting into **even more trouble**.` | 她说的是「不想让她**惹上更多**麻烦」，不是「来阻止麻烦」。md 同章原句 2·中文理解写的是「不想让那个蠢女人惹上更大的麻烦」，与原文一致 ⇒ md 内部精度不匀 | **提示**（措辞级） |

### 与原文相符的 20 条断言（避免「只报问题」的不完整交代）

1. 海伦娜在黑暗马车里挪身、骑装为便于行动与藏身、哈姆雷特跳上她身旁贴住她——`:35` ✓
2. 「别那样看我……只是不想让她惹上更大的麻烦」的自我说服——`:38` ✓
3. 埃莉的幻象被用作风险依据（`If Ellie’s vision is right`）——`:38` ✓
4. 辛西娅比海伦娜预想的更莽撞——`:38` `more reckless than I thought` ✓
5. 海伦娜对辛西娅的评价三连（dashing / courageous / intriguing）——`:41` ✓
6. 两名最魁梧的男仆＋一名当过赤手拳师的马夫作护卫——`:47` ✓
7. 绿门在街灯下「像灯塔一样」看起来完全无害，实则是「魔鬼的交易」入口、门后是「一千种恶习的巢穴」——`:50` ✓
8. 埃莉幻象里辛西娅被困在 crimson velvet 与 black lace 装点的房间——`:53` ✓（词表 `velvet` 例句即此半句）
9. 距上次问话（ch08 的审问）已过**一周**——`:56` `It had been a week since Helena left Cynthia in her sun-filled parlour.` ✓
10. 拉克兰叔叔拆穿婚姻假相时，海伦娜旁观「一个溺水的女人学会了游泳」——`:62` ✓
11. 叔叔担心辛克莱对她三个侄女下手、她被要求远离——`:71` ✓
12. 叔叔当天带着托马斯冲进七晷区抓人，辛克莱被扣**三小时**后因律师要求释放——`:74`、`:77` ✓
13. 警长（magistrate）要求依法放人；他们**没有确凿证据**关人——`:83` ✓
14. 叔叔与托马斯确信有罪但**缺证据**（`proof`）——`:92` ✓
15. 海伦娜出手的**唯一理由**是「救她是唯一的选项」——`:104` ✓
16. 辛西娅独来是为清债并查明辛克莱是否杀了休伯特（`that debt now falls to me`）——`:149` ✓
17. 辛西娅当面划界：「我不是你的问题，也不是你手里的棋子」——`:212` ✓
18. 海伦娜把手放在辛西娅腰上，比喻「像把风关进笼子」——`:215` ✓
19. 辛克莱的私人办公室邀请指名道姓（`Lady Burrows` / `Miss Blair` / `the marchioness`），且辛克莱早知两人身份——`:236`、`:239` ✓
20. 「Mine.」独立成段、无主语无宾语——`:245` ✓

---

## 三、已核实为正确（防误修，下一轮不得以「读着不对」为由改动）

1. **「Mine.」是海伦娜对辛西娅的占有念头，不是魔宠（哈姆雷特）的宣示**——`:245` `Mine.` 紧接 `:248` `The primitive instinct resonated in her bones.`、`:251` `She blinked hard.`、`:254` `What madness is this?`：归属对象是**辛西娅**（`:257` `She was water in a glassy pool.` 也仍是海伦娜的自况）⇒ **成立**，md 原句 9·为什么这样写「本能先替她答了话」不得改成「对狐狸宣示」。
2. **原句 6「几乎把她击倒」的「她」＝海伦娜**——`:122` `a punch of need nearly knocked **her** over` 的主语是 `need`，而先行目标是刚转过来的**海伦娜**（`Whirling her around to face Helena`）⇒ **成立**。
3. **原句 7「that includes you」把海伦娜并入「别人」**——`:212` `I’m tired of letting other people’s opinions control my choices. And that includes you, Helena Blair.` ⇒ **成立**。
4. **原句 8 的「侯爵夫人」＝辛西娅**——`:236` `you may join the marchioness`；`:62` 亦写 `The stunning marchioness…` ⇒ **成立**。
5. **原句 4 的「上一章的审问」＝ ch08**——`:62` `during Uncle Lachlan’s interview`，`:56` `It had been a week since Helena left Cynthia in her sun-filled parlour.` ⇒ **成立**（时间跨度＝一周，与 ch08 的审讯连续）。
6. **原句 3 的「七晷区那个『魔鬼』名下声名狼藉的俱乐部」**——`:50` `the Devil of Seven Dial’s notorious club aptly named The Devil’s Bargain` ⇒ **成立**（原文是 `Seven Dial` 单数，md 译「七晷区」）。
7. **哈姆雷特没有随行到门口**——`:116` `she slipped out of the carriage, locking a disgruntled Hamlet inside.` ⇒ md 导航只写「带着……狐狸哈姆雷特」，未说他到门口 ⇒ **成立**，不得据导航措辞改写成「狐狸守在门口」。
8. **辛克莱未被定罪**——`:77` `brought to heel … for a grand three hours before his solicitors demanded his release`、`:83` 无证据 ⇒ md 导航「扣人三小时就被律师带走」**成立**，不得写成「被捕」。
9. **「七晷区」＝ Seven Dials**——`:47` `the heart of Seven Dials`、`:50` `Devil of Seven Dial’s` ⇒ **成立**（全书统一，无冲突）。
10. **词表 22 条例句全部逐字取自本章**——**成立，不得改写例句**（22/22 逐字回源命中、22/22 词头在例句内）。
11. **本章 9 条引语无 `…`**，不存在「用省略号跳过原文」的情形 ⇒ 原句 5 的选段止于 `:113` `on a moonless night.`（下一句「河水流向大海」未被收录）属**选段取舍**，不判缺陷。
12. **`split skirts` 的读法**——英文 `the lack of bustle and split skirts` 本身歧义（见 E3）⇒ **不得据中文译法去改英文引语**。

---

## 四、覆盖声明与已知盲区

- **本章覆盖**：R1 素读（先于任何 md 打开，266 行全读，72 事件 / 13 关系 / 7 数字 / 7 未决 / 10 陷阱）→ R2 机器层 → R3 三张单子 → R4 逐块 9/9 → R5 判定表，**全流程走完**。
- **本书覆盖（深审进度）**：批 1 = ch02 / ch03 / ch04，批 2 = ch05 / ch06 / ch07，批 3 = ch08 / ch09（本表）⇒ **8 / 27 章**已完成 R0–R5（ch09 为第 8 章）。ch01 与其余 19 章**只有机器层**（R0 全书级已跑），**未做人判**，不得写成「已审查」。
- **同会话盲区（如实标注）**：本书由本会话在写作期产出，本章亦为写作期读过的章之一；本次仍执行「先素读、写完 `1-suread.json` 才开 md」，但**不能视为完全盲态**。
- **本章特有盲区**：
  - L2（`:167` 「保辛西娅的安全完全次于破案」）判为「不构成阻断」，理由是它属人物刻画细部、md 未作出相反断言；**该判据是本会话自定**——若后续主张「海伦娜跟进去的真理由是案子」必须在 md 可见，L2 应升为提示项，须由执行方拍板后再改。
  - E3 判为**提示**而非阻断：英文 `lack of` 的辖域歧义，无法据原文单向裁定 md 的读法，且 md 读法与骑装实物相合。
  - F1（引号配对）由本会话自建探针 `/tmp/pair4_hx.py` 判出，**该探针未入库**；判据＝「内层以 `’`/`”` 结尾且全块无 `‘`/`“`」，全书扫出 1 条即本章此条。
- **未做**：五步审查附录 B（a–e 全文）已被 `审查表.md` 归档取代，不重复执行。
