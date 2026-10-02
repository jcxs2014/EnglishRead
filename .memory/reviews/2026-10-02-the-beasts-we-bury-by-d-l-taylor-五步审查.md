# 《The Beasts We Bury》独立五步审查 · 缺陷清单

- **书目录**：`notes/books/novels/the-beasts-we-bury-by-d-l-taylor/`
- **审查方**：Qoder-Mac（**同会话**——按 AGENTS 第 10 条，此处**不适用**「执行方自行发起自审」的降级条款，a–e 全部完整执行）
- **日期**：2026-10-02
- **审查基线**：`7281fc793`（29 章 + 总览三篇，全绿入库）

---

## 结论

**不予放行 → 整改后放行。**

机械门禁从 a 到 e **全部通过**，但 d/e 两步的人判在**总览层**查出 **10 处阻断型**，
其中 **9 处是「引语逐字对、中文逐字对、错的只是配对」**——这类缺陷在本项目是最难机械检出的一档，
指纹比对、flat 比对、结构扫描、章节标签对账**全部看不出来**。

---

## a 步 · 第 3 条提交门禁全量重跑（不信报告数字）

| 项 | 结果 |
|---|---|
| lane | 完整 lane（有 epub） |
| `verify_quotes` | **263/263（100%）· 干净 31/31**；`--full` 整串取证 0 |
| `check_vocab` | 1026 词条 **FAIL 0**；WARN 17（16 条长度≥9 启发式＝提示型；1 条 `ch05 snow-white` 高级档混入常用词＝提示型，已记不改） |
| `check_entities` | 0 个未知实体 |
| `corruption_scan` | FAIL 0 |
| `sweep_full` | 本章命中 224 ｜ 跨章 0 ｜ 拼接 0 ｜ 查无 0 |
| `check_short_quotes` | 3/3 命中 |
| `check_chapter_quotes` | **29/29 逐章 in-chapter** |
| 块覆盖 / 结构 / 凭空造词 / 空段 | 29/29 ｜ 0 ｜ 0 ｜ 0 |
| `sweep_analysis_inline` | **1040 条全逐字 / 零命中 0** |

## b 步 · 逐章归属

29 章逐一 `check_chapter_quotes`，**全部 X/X in chNN text**，零跨章。ch01 的 1 条短引语
（`Am I strong enough yet?`）经 `check_short_quotes` 命中，且经二实现确认是该文件**末句**。

## c 步 · 结构扫描

- `audit_structure`（第一实现）：结构缺陷 0 / 提示 0 / 映射不一致 0
- `check_struct_indep`（**第二实现**）：29 个 md，缺陷 0
- ⚠️ 按规则**未把第一实现的 0 当作「子项齐全」的证明**——第二实现独立复核后一致。
- 总览三篇：`check_overview_full` H1 语义错配 0

## d 步 · 语义二审

**机械子项（全部用第二实现，不复述写作期的尺子）**

| 脚本 | 结果 |
|---|---|
| `check_analysis_indep` | 抽出分析层英文 **330 条，全部逐字命中** |
| `check_xref_indep` | chNN 引用 105 处：英文证据报警 **0**；中文式待人判 53 处 |
| `check_xref_zh` | 章号+短语命中 20 ／ 错 0 ／ POV 错 0 |
| `sweep_full` | 跨标签拼接 0 ／ 查无 0 |
| 主会话自建三检查器 | A 类阻断型 **0** · 关键词 225 块 0 未锚定 · 专名 0 伪造 |

**人判 → 10 处阻断型（全部在总览层）**

### ⭐ 缺陷类 A：引语↔中文错配 9 处（本书新形态）

根因是**手写 `{Q:NN:seq}` 索引时没核对该索引指向哪一条引语**。
引语逐字正确、中文逐字正确，**错的只是配对** ⇒ 所有机械层无感。

定位法（可复用）：把「我写的【中文】」与「引语池自带的【中文】」做相似度比对，
低相似度即错配，再按同章内最佳匹配回填正确索引。

| # | 误写索引 | 正确索引 | 我写的中文（实际描述的是） |
|---|---|---|---|
| 1 | `{Q:3:2}` | `{Q:3:1}` | 我以为讲「八岁进鬼城」，实指「进 Citadel 快一年」 |
| 2 | `{Q:17:4}` | `{Q:17:3}` | 「少信我一点」在 #3，#4 是「焊死镯子」 |
| 3 | `{Q:18:2}` | `{Q:18:4}` | 我以为讲「树与住客」，实指「她答应得太痛快」 |
| 4 | `{Q:26:8}` | `{Q:26:7}` | 我以为讲「没有秘密」，实指「我现在得走」 |
| 5 | `{Q:27:8}` | `{Q:27:6}` | 我以为讲「Azele 只派一人」，实指「抓锅拿铲」 |
| 6 | `{Q:28:4}` | `{Q:28:6}` | 我以为讲「改誓词」，实指「Captain 念的是在位者誓词」 |
| 7 | `{Q:28:8}` | `{Q:28:2}` | 我以为讲「自己走出来」，实指「星芽花冠」 |
| 8 | `{Q:29:4}` | `{Q:29:5}` | 我以为讲「父与堂兄的暗面」，实指「换住处与屏障」 |
| 9 | `{Q:29:8}` | 保留 #8，**四条子项整条重写** | 「我走出去」全书无对应引语 |

### ⭐ 缺陷类 B：结局主体搞反（1 处，事实错误）

原文 ch29 结尾：**被锁在壁橱里的那个人自己踹开门走出来**，说「Try it.」
——**不是 Mancella 走出去**。我原写的 ㉕「我走出去」、节点十「她仍没有开门／最后她走了出来」均反了。

已改：㉕ 改写为描述那人踹门而出；节点十标题改「Try it.」并写明走出的是谁；
概述结局段重写为「结局不是停在一扇门前，是那扇门被从里面踹开了」。

## e 步 · 总览层事实核对

### 交付材料自检

| 材料 | 结果 |
|---|---|
| ① 第 3 条门禁原始输出（逐行） | `.memory/raw-gates/the-beasts-we-bury-by-d-l-taylor/` 两份，336 行，已入库 |
| ② 总览自检声明 | 总览带标注引语 **53 条，逐条回该章 `text/` 核，MISS = 0**；9 条关键断言的原文支撑行号见下 |
| ③ 跨书污染自检 | 15 个专名逐个 `grep -rlw` 全库 books/：**污染 0**；3 处命中经判性质为无关同名（见下） |

### 关键断言的原文支撑（逐条回源）

| 断言 | 支撑 | 结果 |
|---|---|---|
| Mance 是 Silver 的昵称 | ch09 `He started calling me by the nickname` | ✅ |
| 在位者矛盾·A 侧 | ch25 `I am the Prime now` | ✅ |
| 在位者矛盾·B 侧 | ch26 `Now that I’m the Prime` | ✅ |
| 父亲那句是威胁非事实 | ch25 `From your prison cell` | ✅ |
| 壁橱者是「像」非「是」 | ch29 `is a girl who looks like me` | ✅ |
| Alect 被 seize 无后续 | ch25 `Now seize him` | ✅ |
| Mara 年龄矛盾·年长侧 | ch04 `her reclusive older sister`／ch03 `big-sisterly confidence` | ✅ |
| Mara 年龄矛盾·年幼侧 | ch19 `Or Mara at ten` | ✅ |

### 章节标签对账

`check_overview_full` B 段：**53 对 / 标注与实章不符 0**。
⚠️ 该段**只验「引语逐字命中章 == 标注章」**，对说话人、人物、关系、结局**零覆盖**——
本轮 9 处错配全部逃过它，就是这句警告的实证。**标签对 ≠ 内容对。**

### 双向验收（反向计数）

对各写作代理交来的「没敢下判断」清单逐条反向计数，确认**没有被照抄成事实**：

| 项 | 结果 |
|---|---|
| 父亲生死 ／ 结局和解 ／ 兄弟关系 ／ Guerre 与 Alect 是否同一人 ／ Sangua 死因 ／ 剑的来历 ／ 倒计时连续 ／ 爆炸物归属 ／ Vie 生死与身份 | 全部 **0 处** ✅ |
| Mara 的魔法 | 命中 1 处 → **回源为假红**：ch11 紧邻前句即 `Father tried to force Mara's magic to manifest`，有充分支撑 |

### 新增：书内第二处自相矛盾 —— Mara 是姐姐还是妹妹

| 指向 Mara **更年长** | 指向 Mara **更年幼** |
|---|---|
| ch01 `an older sister merely entertaining a younger sister's ridiculousness` | ch19 Alect `Or Mara at ten`（Mancella 八岁） |
| ch03 `with big-sisterly confidence` | ch03 `Mara and I are going in at eight and ten years of age`（Mara 在前） |
| ch04 `It could have been her reclusive older sister` | |

**不予裁决。** 处置：分析层 **17 处**「姐姐/妹妹」一律中性化为 `Mara`
（**引语原文与英文例句照录不动**），概述新增该矛盾条目并列两处证据。

---

## 整改后终验

```
gate.sh A 组 15 项           EXIT=0
verify_quotes                263/263（100%）· 干净 31/31 · --full 整串取证 0
check_vocab                  1026 词条 FAIL 0
sweep_full                   本章命中 224 ｜ 跨章 0 ｜ 拼接 0 ｜ 查无 0
逐章归属                      29/29
分析层行内英文                1040 条全逐字 / 零命中 0
结构 / 凭空造词 / corruption  0 / 0 / 0
verify_overview_quotes       EXIT=0
check_overview_full          整串 54 命中 0 查无 ｜ 标签 53 对 0 不符 ｜ H1 0 错配
主会话三检查器                A 类 0 ｜ 关键词 225 块 0 未锚定 ｜ 专名 0 伪造
```

整改 commit：`7b4dd8a39`

---

## 假红型（工具或判据错了，**未动 md**）

| 报警 | 回源结论 |
|---|---|
| 「Mara 的魔法」反向计数命中 1 处 | **假红**。ch11 原文紧邻前句 `Father tried to force Mara's magic to manifest`，表述有充分支撑 |
| 「Mara 的魔法在基础档」「Vie 死了」等跨书同名报警 | **假红**。Rooftop→Astarion「Rooftop Henry」、Vie→Lace、Gore→「Kensington Gore」（街道名，非本书的 Prime Gore），均为他书无关同名 |
| `check_crossref` 报「0 对」 | **真空绿**。本书跨章引用是裸 `chNN` 形态，不在该工具的 `chNN "引语"` 口径内 |

---

## 审查过程自身的四条纪律 · 本轮遵守情况

1. **换检查路径必须换实现** —— 已用 `check_analysis_indep` / `check_xref_indep` / `check_struct_indep`
   三个第二实现跑机械子项，未复述 `audit_structure` / `check_crossref` / `sweep_analysis_inline`。
   ⚠️ 报告中仍写明：**这三个脚本各只在本库 1 本书上验证过**。
2. **自省不构成防线** —— 真正的防线是那个回查动作：总览 9 处错配是**用相似度比对池内中文**查出来的，
   不是靠「我写的时候很小心」。Mara 年龄矛盾是**逐条 grep 两处原文**查出来的。
3. **改内容前 dry-run** —— 本轮改 md 全部用带 `assert` 的行级脚本（锚点命中数必须恰好 1、
   替换必须生效），未用过整文件 Write 覆盖章节。
4. **大面积同类报警先读行再改** —— Mara 年龄类共 17 处同型，**先只改 1 处验证判据成立**，
   再批量；改完复查发现 4 处空格粘连与 1 处漏改（ch03），单独修正后才收尾。

---

## 已知局限（同会话审查，如实标注）

- **说话人／人物是否正确**这一类，实测不可靠机械化（全库 315 本只 1 条真缺陷、假阳约 1/3），
  本轮靠 d 步人判 + 子代理附真实反例，**未做成检查器**。
- **同会话审查**在「我自己的写作倾向」层可能有系统性盲区。本轮 10 处阻断型**全部出现在总览层**
  （即我自己最后写、且引用索引靠手填的部分），**章节层由子代理写，主会话抽查 16 块未再发现同类错配**——
  这个分布本身提示：**风险集中在主会话自己最后动过手的地方**。
- 本轮**未做**全书逐块人判（225 块）：d 步分三批派子代理 + 主会话抽查，
  覆盖重点是高风险的「引语↔分析对应」与总览层。

# b 步 · 逐章归属（29 章逐一）

--- ch01 ---
ch01 father announces the jaguar hunt.md: 7/7 in ch01 text（另有 1 条短引语未校验）
--- ch02 ---
ch02 silver climbs the cliff to break into the castle.md: 8/8 in ch02 text
--- ch03 ---
ch03 mancella enters the broken citadel at eight.md: 8/8 in ch03 text
--- ch04 ---
ch04 silver lures mancella into the kitchen with a torte.md: 8/8 in ch04 text
--- ch05 ---
ch05 mancella waits for starsprouts and confronts marc on the tower.md: 8/8 in ch05 text
--- ch06 ---
ch06 silver smuggles the apology letter past guerre.md: 8/8 in ch06 text
--- ch07 ---
ch07 mancella sees the academy and is ordered to kill a student.md: 8/8 in ch07 text
--- ch08 ---
ch08 silver bargains for the herald sword.md: 8/8 in ch08 text
--- ch09 ---
ch09 the sealed market and the practice fight.md: 8/8 in ch09 text
--- ch10 ---
ch10 the fake death match in the arena.md: 8/8 in ch10 text
--- ch11 ---
ch11 monster and mara black room.md: 8/8 in ch11 text
--- ch12 ---
ch12 trophy room confessions and the sword.md: 8/8 in ch12 text
--- ch13 ---
ch13 apology ride and the border ambush.md: 8/8 in ch13 text
--- ch14 ---
ch14 battlefield rescue and the sunk boat.md: 8/8 in ch14 text
--- ch15 ---
ch15 the boat and the almost kiss.md: 8/8 in ch15 text
--- ch16 ---
ch16 silver unlocks the bracelet and steals the letters.md: 8/8 in ch16 text
--- ch17 ---
ch17 mance jumps the gap and snaps the bracelet shut.md: 6/6 in ch17 text
--- ch18 ---
ch18 silver brings her to his hovel and guerre arrives.md: 7/7 in ch18 text
--- ch19 ---
ch19 alect splits in two and mancella runs for the castle.md: 8/8 in ch19 text
--- ch20 ---
ch20 mance cuts off his insignia and runs for the castle.md: 6/6 in ch20 text
--- ch21 ---
ch21 mancella finds the dining room full of blood.md: 7/7 in ch21 text
--- ch22 ---
ch22 silver digs vie out and rereads the letter.md: 7/7 in ch22 text
--- ch23 ---
ch23 mara confesses the necklace that takes.md: 8/8 in ch23 text
--- ch24 ---
ch24 silver reads the letters aloud.md: 8/8 in ch24 text
--- ch25 ---
ch25 the bottle was not the one she threw.md: 8/8 in ch25 text
--- ch26 ---
ch26 silver wakes with her hand in his.md: 8/8 in ch26 text
--- ch27 ---
ch27 azele turns the stumps to ash.md: 8/8 in ch27 text
--- ch28 ---
ch28 she rewrites the vow and the crown.md: 8/8 in ch28 text
--- ch29 ---
ch29 the girl in the closet says try it.md: 8/8 in ch29 text

# c 步 · 结构扫描

## audit_structure（第一实现）
=== 精读结构扫描（the-beasts-we-bury-by-d-l-taylor）===
  扫 32 个 md、275 个引语块；多数派必备节：（无，不判）
  本书主流子项（自推断，不套外部模板）：中文理解、为什么这样写、关键词、读者视角提示 ｜ 引语众数 8
  ❌ 结构缺陷 0 ｜ ⚠️ 提示 0 ｜ 🔀 映射不一致 0
EXIT=0

## check_struct_indep（第二实现，d 步规格要求用它）
=== 独立结构扫描：29 个 md，缺陷 0 处 ===
EXIT=0

---

## 附：a/b/c 步原始输出

```

# d 步 · 机械子项（第二实现）

## check_analysis_indep（分析层行内英文·第二实现）
抽出分析层英文片段 330 条
✅ 全部片段在全书 text/ 逐字命中
EXIT=0

## check_xref_indep（跨章引用·第二实现）
=== chNN 引用 105 处：英文证据报警 0 处 ／ 中文式待人判 53 处 ===
EXIT=0

## check_xref_zh（中文式跨章引用，写作期已跑，此处复跑）
=== 跨章引用：章号+短语/POV 命中 20 / 错 0 / POV 错 0 ===
EXIT=0

## sweep_analysis_inline（终验标准件）
=== 分析层行内英文逐字核查（the-beasts-we-bury-by-d-l-taylor）===
  参照集：text/（29 个提取件） + epub 交叉验证 ；扫 32 个 md（引语行与 YAML frontmatter 已跳过）
  落点 #14 表格单元格：1202 个表格行、968 条裸英文单元格片段（带引号的单元格由引号/反引号通道覆盖，不重复计）
  ✅ 逐字 1033 ｜ ⚠️ 跨章 0 ｜ 🔶 拼接 0 ｜ 🟠 部分命中 0 ｜ 🟡 词形 0 ｜ ⚪ 术语 0 ｜ 🔧B类语料缺 0 ｜ ❌ 零命中 0 ｜ 跳过 28
```
