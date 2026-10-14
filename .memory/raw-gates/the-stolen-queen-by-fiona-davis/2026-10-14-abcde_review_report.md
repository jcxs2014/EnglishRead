# The Stolen Queen 独立五步审查（a–e）结论

- 书目录：`notes/books/mystery-thriller/the-stolen-queen-by-fiona-davis/`
- 审查方：Opencode-Mac（**同会话审查**——用户 2026-10-14 本会话发起；执行方＝审查方）
- lane：**完整 lane**（epub 在位）
- 规模：34 章 + 总览三篇 = 37 md ｜ 引语块 **253** ｜ 词条 894 ｜ 金句 25 ｜ 情感节点 8

---

## a 步：第 3 条提交门禁全量重跑（不信报告数字）

原始输出：`2026-10-14-a_review_gates_full.txt`

| 门禁 | 结果 | 档 |
|---|---|---|
| verify_corpus | PASS（FAIL 0 / WARN 1＝未传 `--anchors`） | 提示型 |
| verify_quotes | **277/277（100%）**，干净 35/35 | ✅ |
| verify_quotes --full | 整串取证 0 | ✅ |
| check_vocab | **FAIL 0**（WARN 20＝词长≥9 启发式） | 提示型（只记不改） |
| check_entities | 0 未知实体 | ✅ |
| corruption_scan | **FAIL 0**（U+FFFD／双句号） | ✅ |
| sweep_full | 本章 251 ｜ 跨章 0 ｜ 拼接 1（ch28 合法跨段省略）｜ **查无 0** | ✅ |

**语料层边界复核（换口径自建）**：每章 `text/` 必须只含自己的 `Chapter <Ordinal>` 且不含任何他章序号 ⇒ **异常 0/34**（无合并／拆分）。用 `(?![\w\-])` 负向断言排除 `Twenty` 误匹配 `Twenty-One` 的自造假阳。
WARN 1 的处置：本书为**双 POV 交替**（Charlotte／Annie 逐章换），已用 `--shared Charlotte,Annie` 豁免，并另跑上表边界复核替代 `--anchors`。

## b 步：逐章归属

`check_chapter_quotes.py` 全 34 章 → **每章 X/X in chNN text，零跨章**（原文见 a 步文件）。
cliffhanger 边界专项：ch15→ch16（Met Gala 失窃夜）、ch20→ch21（墓顶坍塌）、ch32→ch33（屋顶旧账）三段跨章对话，逐段读前后章 `text/` 确认引语归属跟随**对话实际发生章**。

## c 步：结构扫描（＋换实现）

| 检查 | 结果 |
|---|---|
| audit_structure | 结构缺陷 0 ｜ 提示 0 ｜ 映射不一致 0 |
| **check_struct_indep**（第二实现） | 34 md，**缺陷 0** |
| check_quote_blocks | 前缀完整 · 编号连续无撞车 · 无孤儿分析 · 无自查泄漏 |
| check_quote_order | 顺序缺陷 0 章（ch28 不可判） |
| check_overview_full | A 查无 0 ｜ B 标签不符 0 ｜ F 不符 0 ｜ C 0 ｜ E H1 错配 0 |
| `grep -m1 '^# ' 00_*.md` | 三篇 H1 与文件名语义一致 |
| md 件数 == text 件数 | 34 == 34（`00_*` 三篇另计） |

## d 步：语义二审（引语↔分析逐对）

- 机械层（第二实现）：`check_analysis_indep` 426 条分析层英文**全部逐字命中**；`check_xref_indep` chNN 引用 139 处英文证据报警 0。
- 人判层：**4 个子代理并行**覆盖 253 块（ch01–09 / ch10–17 / ch18–25 / ch26–34），每批附本库真实失败案例（100G ch86 引语分析不对应 · Such a Fun Age 18 处引语截短 · Room 11 处人物误归 · Bookshop by the Bay 6 处说话人反转）＋防幻觉条款（报警须并列 md 与 text 双证据）。
- 结论：**引语层 0 缺陷**——253 块逐字命中（含省略号拼接的**尾片段**）、说话人反转 **0**、人称/性别/主语错配 **0**、引语截短 **0**、关键词锚定 253/253。
- 主会话抽查复核子代理结论 5 处（ch29 原句4＝Annie、ch34 原句5＝Fatima、ch31 原句4＝Mrs. H、ch30 原句4＝Frederick、ch33 原句5＝Annie 内心）——**全部与原文窗口一致**。

## e 步：总览层事实核对

总览引语：`verify_overview_quotes` **49/49**；`check_overview_labels` **50/50** 标注章逐字；`check_overview_full` B 段标签对 15／不符 0。
**另跑自建独立脚本**（与上述工具不同实现）：抽出总览内 99 条拉丁片段 + 101 个 `（chNN）` 标注，逐条 flat 比对 ⇒ **全部逐字命中且归章正确**。
事实层：人物身份／关系／结局逐条对 ch28–ch34 交叉核对（Layla＝Fatima、Mona 非其女、Henry 幸存、项链材质 gold and glass、项链来历 anonymous one-year loan、Hathorkare 浮雕被凿改于 Saukemet II 时期）。

---

## 缺陷清单

### 阻断型（7 条，已全部整改）

| # | 文件 | 问题 | 证据（text/ 原文） | 整改 |
|---|---|---|---|---|
| 1 | `00_概述.md` L72 | 叙事结构断言「双线双视角交替…**逐章轮换**」与章节实际不符；且把「1979 埃及」只归 Annie 线 | 实际 POV 序：C,C,A ×5 组（ch01–15），ch16 起 C,A 交替；ch34＝Charlotte 1979 Egypt | 改为「双视角、三条时间线」，写明三章一轮→逐章交替 |
| 2 | `00_金句精选.md` ㉓（ch28）上下文 | 「**屋顶**摊牌」场景错 | ch28：飞机自开罗返纽约，埋伏设在 Met **Temple of Dendur 展厅**；`rooftop` 全书 0 次 | 改「神庙展厅摊牌」 |
| 3 | `00_金句精选.md` ⑬（ch16）中文 | 「**青瓷**女王」材质错（且同条「为什么重要」写「青金女王」，自相矛盾） | ch01：`the Cerulean Queen was made of finely polished lapis lazuli` | 改「青金女王」 |
| 4 | `ch16 threatening note and stolen queen.md` 中文理解 ×2 | 同 #3 | 同上 | 改「青金女王」 |
| 5 | `00_情感节点.md` 节点二 | 「**同一个月**，她发现自己怀孕了」时间错 | ch05 末：`and a month later, she discovered she was pregnant` | 改「一个月后」 |
| 6 | `ch34 mother daughter reunion.md` 为什么这样写 | 「比 survival **或 survival** 更中性」重复词（编辑残留） | — | 改「比 survival 更中性」 |
| 7 | `ch14 grief work…md` 中文理解 ＋ `00_金句精选.md` ⑪ 中文 | 中文行内混入英文单词：「神情却 **still** 安详」 | — | 改「神情却依然安详」 |

### 提示型（5 条，只记并就地收紧措辞）

| # | 文件 | 问题 | 证据 | 处置 |
|---|---|---|---|---|
| 1 | `00_金句精选.md` ⑯（ch19）上下文 | 「母亲的**闪婚**」——ch19 是求婚（`“Brad proposed!”`），婚礼在 ch31（`Joyce’s marriage to Brad`） | 订婚 ≠ 结婚 | 改「母亲突然宣布订婚」 |
| 2 | `ch10` 第4块 为什么这样写 | 「本馆**第一任**馆长」——属文本外历史知识 | 原文仅 `was made director in return` | 删「第一任」 |
| 3 | `00_情感节点.md` 节点五 | 「废弃**蓄水池**地道」——原文是蓄水池的雨水渠，非蓄水池本体 | ch17：`an obsolete storm drain for the park’s reservoir` | 改「公园蓄水池的废弃雨水渠地道」 |
| 4 | `00_情感节点.md` 节点六 | 「失足**踩碎物件**」——实际是踩到一只木乃伊化的鹅 | ch21：`That’s a mummified goose you stepped on` | 改「失足踩到一只木乃伊化的鹅」 |
| 5 | `ch11` 第7块 读者视角提示 | 「1978 年 Charlotte 也是靠搭扣背面认出项链的」——ch01 是她**问**出搭扣背面有无王名圈，据此确认身份 | ch01：`“Does it have the cartouche of Hathorkare on the back of the clasp?”` | 收紧为「正是问出…才确认了项链的身份」 |

### 假红型（2 条，先修工具／流程）

| # | 现象 | 判据 |
|---|---|---|
| 1 | ch10–17 子代理把 ch11「1978 年认物」报为「无支撑」 | 它只查了 **ch10**，证据在 **ch01** ⇒ 误报；该项本身成立，降为提示型 5 |
| 2 | ch26–34 首轮子代理块数报 **69**（实际 **67**） | 计数不可信 ⇒ **整份报告作废重跑**；重跑后逐文件实测 67/67 一致，抽查 3 处说话人结论均正确 |

---

## 审查过程自身的四条纪律（执行情况）

1. **换检查路径必须换实现**：c/d 步结构层用 `check_struct_indep`、分析层用 `check_analysis_indep`、跨章用 `check_xref_indep`（均为第二实现）；总览标签另跑**自建脚本**，不复述 `check_overview_full` 口径。✅
2. **自省不构成防线**：把 139 处 `chNN` + 紧随叙述短语**全量抽出逐条回查原章**（不依赖某个脚本）；据此查出阻断型 #2（屋顶）与提示型 #1/#5。✅
3. **现写脚本先 dry-run / 报告为 0 先怀疑脚本**：自建边界复核第一版把 `Chapter Twenty` 误配 `Chapter Twenty-One`，报出 13 章「异常」——先读行确认是**自己正则**的问题（补 `(?![\w\-])`），未改任何 md。✅
4. **大面积同类报警先读行再改**：子代理「ch11 假红」先读原行确认证据章号，未照单改；`青瓷→青金` 先 grep 全库确认仅 3 处。✅

**投毒测试**（原件 `2026-10-14-poison_tests.txt`，**先提交后投毒**）：把金句㉔章标 ch29 改成 ch07 ⇒ `check_overview_labels` 报「标注与实章不符（标注 ch7，实章 ch29）」✅；在 ch03 导航层塞 `the moon rose over the crooked chimney.` ⇒ `check_nav_layer` 报「全书查无 ⇒ 阻断型」✅；把 ch05 引语搬进 ch07 ⇒ `check_chapter_quotes` 报 `7/8 in ch07 text` + MISS ✅。三毒测完 `git checkout` 还原，`git status` 空。

---

## 审查后残留复扫（2026-10-14 追加，用户追问「修复了吗」触发）

⚠️ **首次整改不完整**：上表整改时只改了「发现该缺陷的那个文件」，未把同一措辞在**章节导航层**的副本一并 grep。复扫全库后新查出 **4 处同一缺陷的复制体**，已补修：

| # | 文件·行 | 原措辞 | 依据（text/ 原文） | 改为 |
|---|---|---|---|---|
| 13 | `ch17 tunnel ambush and framing.md` L10 一句话概括 | 「在**废弃蓄水池地道**里与他正面遭遇」 | ch17：`an obsolete storm drain for the park's reservoir` | 「在公园蓄水池的废弃雨水渠里」 |
| 14 | `ch21 the canopic box rescue.md` L10 一句话概括 | 「Annie 失足**踩碎物件**」 | ch21：`That's a mummified goose you stepped on` | 「失足踩到一只木乃伊化的鹅」 |
| 15 | `ch21 the canopic box rescue.md` L12 情感弧线位置 | 「墓室里**踩碎木乃伊鹅**的羞耻触底」 | 同上 | 「踩到木乃伊化的鹅」 |
| 16 | `ch19 thrown out and taken in.md` L10 一句话概括 | 「撞上 Joyce 的**闪婚订婚**」（自相矛盾：闪婚≠订婚） | ch19：`“Brad proposed!”` / `my mother got engaged`；婚礼在 ch31 | 「撞上 Joyce 突然宣布订婚」 |

**缺陷总计数更正：阻断型 7 + 提示型 5 = 12 条（16 处落点）**——4 条缺陷各有一份被复制到章节导航层。

**复扫判据**：对 12 条缺陷的**全部措辞**（`青瓷`／`survival 或 survival`／`神情却 still`／`屋顶摊牌`／`第一任`／`废弃蓄水池`／`踩碎`／`同一个月，她发现自己怀孕`／`逐章轮换`／`搭扣背面认出`）做全库计数 ⇒ **全 0**。`闪婚` 余 2 处经核为 **ch14 Charlotte 与 Henry 自家的 shotgun wedding**（`their shotgun wedding at the Metropolitan House`），属正当措辞，不改。

**过程教训（应写进下次 SOP）**：**「修复即同步」不能只同步到「发现缺陷的那个文件」**——本书同一事实在「章节导航层」与「总览三篇」两处各写一遍（同一措辞习惯），只改总览会留下导航层的旧说法。**正确做法：每修一条，先对旧措辞做一次全库 grep，改完再复扫一次计数归零**（本次即靠复扫才发现）。六道门禁对此**完全不可见**（导航层中文与总览中文都不进英文提取口径）。

**补修后复跑**（原件 `2026-10-14-residue_rescan_and_regates.txt`）：`gate.sh` 退出码 0（0 条阻断型）｜`corruption_scan` FAIL 0｜`verify_quotes` 277/277｜`verify_overview_quotes` 49/49｜`check_nav_layer` ❌0/⚠️0｜`check_keywords_verbatim` 0｜`check_analysis_indep` 426 条逐字全中。

---

## 同会话审查的已知盲区（供用户判断是否另行指派异实例复核）

1. **执行方＝审查方**：本次审查由写作同一实例完成。d 步语义二审虽委派 4 个子代理（异实例），但**a/b/c/e 与整改由本人执行**——对自己写的内容存在「想当然」风险，尤其是总览事实层。
2. **说话人类缺陷机械上不可靠**：本项目已实测 `check_speaker_consistency.py` 命中约 1/3 假阳、全库 315 本仅 1 条真缺陷，故**未进门禁**；本轮 253 块的说话人判断**依赖子代理 + 主会话抽查 5 处**，未做 253 块全量人判。
3. **子代理报告可靠性有实测缺口**：本轮 4 个子代理中 **1 个计数错误**（已作废重跑）；其结论只抽查了 5 处。若需更高保证，建议异实例对 ch10–34 重做一轮 d 步。
4. **「标签对 ≠ 内容对」**：`check_overview_full` 的 B 段只验「逐字命中章 == 标注章」，对**说话人、人物、关系、结局零覆盖**——本轮总览的内容正确性靠**自建脚本 + 人工交叉核对**，非门禁保证。
5. **中文叙述层是最大机械盲区**：本轮 12 处缺陷**全部**落在六道门禁结构上不覆盖的中文层（场景／材质／时间／称谓／叙事结构），且 6 道门禁在整改前后**均为全绿**。
