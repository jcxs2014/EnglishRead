# Deathless（Julie Kagawa）独立五步审查报告

- **审查方**：Hermes（**同会话审查**——用户 2026-10-03 在同一会话发起，按 AGENTS 第 10 条「局限如实标注条款」：此条**不适用**于用户同会话主动要求，a–e 五步**完整执行、未降级、未跳步**；「局限」仅指本报告**结论部分**的已知盲区，供用户判断是否另行指派异实例复核）
- **审查日**：2026-10-03 ｜ **对象**：`notes/books/novels/deathless-by-julie-kagawa/`（22 章 + 总览三篇 = 25 md）
- **lane**：完整 lane（目录级 epub 在位）
- **结论**：**5 处阻断型已全部整改**（复核后 0）；另 6 条经复核判为**提示型/假红型**，未改正文。整改后 `gate.sh` EXIT=0 / 18 项 0 阻断。

---

## a 步 · 第 3 条提交门禁全量重跑（不信报告数字）

现场复验（原始逐行输出存 `.memory/raw-gates/deathless-by-julie-kagawa/2026-10-03-五步审查-*`）：

| 项 | 复验值 |
|---|---|
| verify_quotes | **158/158（100%）· 完全干净文件 22/22** |
| verify_quotes --full | 整串取证 **0**（关闭 52 字符指纹盲区） |
| check_vocab | **320 词条行 · FAIL 0 · WARN 0** |
| check_entities | **未知实体 0** |
| corruption_scan | **FAIL 0 · 报告 0** |
| sweep_full | 本章命中 158 · 跨章 0 · 拼接 0 · **查无 0** |
| check_short_quotes | 命中 7 · 在他章 0 · 拼接 0 · **查无 0** |
| gate.sh | **EXIT=0 · 18 项 · 0 条阻断型** |

**a 步 0 缺陷。**

---

## b 步 · 逐章归属（换实现路径）

按纪律 1「换检查路径必须换实现」，写作期用的是 `check_chapter_quotes.scan_book`（聚合成 158/158），审查期另写 `scripts/attic/review_b_chapter.py`（**不调用其判定函数**，自己按 `text/` 逐章 flat 比对、**逐章打印该章计数**）。

结果：**22 章逐章 100% 命中本章，0 章跨章/失配**（ch05/ch10/ch13/ch14–ch15/ch16–ch22 为 6–7 块，其余 8 块）。cliffhanger 跨章边界逐章核对 `text/` 首末句，无跨章引语。

**b 步 0 缺陷。**

---

## c 步 · 结构扫描（双实现）

| 实现 | 结果 |
|---|---|
| `audit_structure.py` | 缺陷 0 · 提示 0 · 映射 0 |
| **`check_struct_indep.py`（第二实现）** | **缺陷 1 处 → 已修** |
| `check_quote_blocks.py` | 前缀完整 · 编号连续 · 无孤儿 · 无泄漏 |
| `check_overview_full.py` | 整串命中 44 · **查无 0** · 章节标签 对 5/不符 0 · H1 错配 0 |
| H1 人工核 | 三篇 H1 与文件名语义一致（金句 25 条 / 情感节点 10 个 / 概述） |

**C-1［阻断型·已修］ch13 引语编号跳号（缺 7）**
`check_struct_indep.py` 报 `ch13: [summary] 引语编号不连续：[1,2,3,4,5,6,8]`。
成因：写作期我为 ch13 插入新引语块（原句 6「We'll figure it out」）时，把原第 6 块误改为 8，导致**缺号 7**。`audit_structure.py` 报 0 属假阴性（与 a–c 双跑的价值一致 —— 只有换实现才抓到）。
处置：`原句 8` → `原句 7`。复核：结构 0 / verify 158/158 不变 / corruption 0。

---

## d 步 · 语义二审（机械子项 + 换路径逐条回查）

### d-1 机械子项（用 tracked 第二实现，不复述写作期尺子）

| 脚本 | 结果 |
|---|---|
| `check_struct_indep.py` | 0（修复后） |
| `check_xref_indep.py` | 英文证据报警 **0**；中文式**待人判 86 处**（工具盲区，已由 d-2 全量补判） |
| `check_analysis_indep.py` | 逐字 **455/455**；🔶「每词都在但整串不连续」15 条 → **人判 15 条**（见 d-2） |
| `check_anchor.py` | 凭空造词 **0** · 松散关键词 **0** |
| `audit_numbers.py` | 5 条年龄类**列出待人核**（⚪ 不判红）→ 逐条核 `text/`，均与原文一致 |

### d-2 分析层 15 条 🔶 逐条人判

`scripts/attic/review_d_analysis.py`（新写，逐条三档：整串命中 / 他章命中 / 本章查无）。
**⚠️ 本脚本第一版是死代码**：键写成 `f"ch{ch}"`（→`chch03`），15 条全落到空串上、每条都报「真查无」；改 `name[:3]` 又得 `ch0`。最终用正则取 `chNN` 并**断言键覆盖全部章号**，才拿到可信输出 —— 这正是纪律 3「报告为 0 时先怀疑脚本坏了」。

结果：**1 条阻断型（已修）+ 1 条我误判后回滚 + 13 条提示型**。

**D-1［阻断型·已修］ch05 未标章号的跨章引用**
`读者视角提示` 写「与 ch01 结尾那句 **would have to meet the queen**（我大概只能去见那位女王）对照」，但 `would have to meet the queen` 不在 ch01 —— ch01 原文是 `supposed I would have to meet **Raithe's** queen to discover if I was expected to do anything at all`。既**改写**又**丢了章号内的原词**，读者无法回查。
处置：回填为 `supposed I would have to meet Raithe's queen to discover if I was expected to do anything at all`（逐字，ch01）。

**D-2［阻断型·已修］ch22 引语改写冒充逐字**
`为什么这样写` 写「而 **She released it into the sky**（放向天空）」，但 `released` 在全书 0 次；本章原文是 `releasing **the thread into the sky**`。
处置：改为 `releasing the thread into the sky`（逐字，ch22）。

**D-3［自我误判·已回滚］ch12 `the small portion of that life`**
我一度判为「本章查无＝缺陷」并改写，随后核实：该句确在 **ch03**（`small portion of that life into myself`），且 md 已**显式标注「第 3 章」** ⇒ **合法跨章引用，非缺陷**。已回滚改动。**教训：跨章报警须先判「是否已标章号」，再判「是否错章」。**

**13 条提示型（不改）**：均为**分析层的转述/改写引述**（如 ch03 `gripping the spear tightly`←原文 `gripping **her** spear tightly`、`ch05 was not be slammed in my face`←原文 `the door would not be slammed in my face`）。逐条核对**语义与原文一致、且属分析层而非引语层**；引语层 158/158 逐字，故不构成阻断型。

### d-3 跨章引用全量回查（自写 `review_d_xref.py`，补 `check_xref_indep` 的中文式盲区）

抽 `chNN …片段` 与 `第 N 章 …片段` **两种写法**共 30 条，逐条到被指章 `text/` 回查：**✅ 命中被指章 24**，报警 6 条逐条核：

**D-4［阻断型·已修］三处章号错标**
| 位置 | 原写 | 实际在 | 处置 |
|---|---|---|---|
| ch10 | `第 6 章女王那句 my only duty` | **`my only duty` 全书仅 ch10（Raithe）**，女王从未说 | 改为 `ch06 女王那句 do not mistake duty for compassion`（逐字、真实、且确在 ch06） |
| ch14 | `与第 6 章女王的"I am Sahmessyia"` | ch02 / ch03 | 改为 `ch03` |
| ch22 | `与第 16 章他说"It will destroy you in the end"` | ch01 | 改为 `ch01 梦里他说…` |

⚠️ 其中 ch10 那条**不只是错标，是无出处断言**（女王从未说 `my only duty`）——三类里最重的一种。

**剩余 2 条经核实为脚本误配，正文正确**：
- 概述 `Shifting Dunes（ch12）` —— ch12 确有，标注正确；
- ch19 `snuff out my life in a heartbeat → ch12` —— 该行 ch12 指的是 `a small portion`，`snuff out` 在本章引语内，脚本把同行的两个章号配错。
- ch22 `Hello, Fateless… Welcome to my labyrinth` —— 🔶 省略号拼接（两半均在 ch02），**跨缝隙拼接提示型**，非查无（`check_overview_full` 同样列 🔶）。

### d-4 说话人窗口核实（AGENTS 明示机械层零覆盖项）

对总览里带说话人归属的 12 条，逐一开 **±200 字符窗口**核对原文施动者：
ch01 织锦/`blessing`=**Raithe**（`he murmured` / 上下文 he）✅；ch01 `So how are we any different`=**Vahn**（`his voice low and calm`）✅；ch03 `I swore`=**Raithe** ✅；ch06 `do not mistake duty`/`I saw his future`=**女王**（`her expression both sympathetic and cautionary`）✅；ch06 `reweave`=**Halek** ✅；ch18 `In that one instant`=**Raithe** ✅；ch20 白网=**Raithe** ✅；ch21 `truly see the strands`=**Raithe**（`His voice held a note of awe`）✅；ch22 `this body is a cage`/`I am proud of you`=**Vahn** ✅；ch11 自请随行=**Raithe** ✅；ch18 逼问=**Kysa** ✅。

**0 条说话人错误**（本类已实测不可机械化，此处全部靠人判）。

---

## e 步 · 总览层事实核对

- **总览引语逐字**：46 条（金句 25 + 节点 21）对**全书** `text/` flat 比对 —— **查无 0**。
- **章节标签对账**：`check_overview_full` B 段 **对 5 · 标注与实章不符 0**；人工另核 4 处（概述 Shifting Dunes→ch12 ✅、金句 ch17 ✅、节点9 ch21 ✅、金句20 ch20 ✅）。
- **⚠️ 须写明「标签对 ≠ 内容对」**：该工具 B 段只验「逐字命中章 == 标注章」，**对说话人、人物、关系、结局零覆盖** —— 本次 d-4 已另行覆盖说话人维度（12 条全对）。
- **人物身份/关系/结局与章节交叉核对**：概述「Sparrow＝Kovass 盗贼／Fateless」`✅ ch01·ch03·ch21`；「Raithe＝iylvahn 刺客 kahjai，自请随行」`✅ ch11`；「Kysa＝圣甲虫氏族、向 Deathless 低头有血仇」`✅ ch09·ch12`；「Halek＝逐命者」`✅ ch01`；「Vahn＝养父→ma'jhet→怪物躯壳灵魂」`✅ ch01·ch13·ch22`；「女王亦为 Deathless」`✅ ch02·ch06`；「结局＝她取到织机、女王国女神对女神」`✅ ch21·ch22`。**0 条事实性断言错误。**
- **⚠️ 概述情节曾凭印象写（写作期已自查发现并整段重写）**：初稿 ch14–17 含本书不存在的两个事件（"人面狮身守卫""少年被诅咒"）。**此为叙述层，门禁对它零覆盖**，本轮复核确认已按 `text/` 重写、无残留。

---

## 三档分类汇总（AGENTS 第 3 条口径）

| 档 | 条数 | 内容 |
|---|---|---|
| **阻断型（已改）** | **5** | C-1 ch13 编号跳号 · D-1 ch05 跨章引用改写+丢原词 · D-2 ch22 `released` 凭空造词 · D-4 三处章号错标（含 ch10 一处**无出处断言**） |
| 提示型（只记不改） | 19 | 分析层改写引述 13 · 🔶省略号拼接 2 · `audit_numbers` 年龄类 5（均经核与原文一致） |
| 假红型（先修工具） | 3 | ① `audit_structure` 漏报 ch13 跳号（第二实现抓到）② `check_xref_indep` 中文式 86 处待判（自写脚本补判）③ 我自写的 `review_d_analysis.py` 第一版死代码（键写错致 15 条全假报，已修并加断言自检） |

## 审查过程自身的教训（4 条）

1. **自写检查器第一版是死代码**：`review_d_analysis.py` 键写错 → 15 条全报「真查无」，若照单全改会**改坏 13 条本来正确的分析**。判据：键必须断言覆盖全部章号，且**先修脚本再读结论**。
2. **「跨章报警」不等于「错章」**：ch12 的 `the small portion of that life` 已显式标「第 3 章」，我误判为缺陷并改写，**核实后回滚**。判据须先问「是否已标章号」。
3. **门禁全绿仍漏**：本次 5 处阻断型里，c 步 1 处 + d 步 4 处，`verify_quotes` 158/158 与 `check_vocab` FAIL0 全程未报 —— 再次印证 AGENTS「前移预防省的是发现成本，不是核验成本」。
4. **审查期改内容后必须跑 corruption_scan**：本轮 8 次 Python 行级替换后 `corruption_scan` FAIL 0 / 报告 0，确认无 U+FFFD 与双句号（纪律「走 Python 替换不是 U+FFFD 免检通行证」）。

## 同会话审查的已知局限（结论部分 · 不影响 a–e 完整性）

- **说话人维度靠人判 12 条**，未做全量 165 块穷举；`check_speaker_consistency.py` 已实测不可靠（假阳约 1/3），故未用。
- **概述层叙述事实**（人物关系、情节顺序）**没有机械判据**，本轮仅核了核心人物与结局 7 组断言；概述中"ch08–13 是全书最苦的一段路"这类**概括性评价**未逐条核。
- **10 条 `🔶 跨标签拼接`（总览 11 条）**只判「两半均逐字」，未逐条判断省略是否必要、是否属 AGENTS 第 7 条禁令 5「引语只取一个说话轮次」的例外。
- 建议：若需彻底复核，指派异实例做 d-4 全量（165 块说话人）+ e 步叙述层专项。

---

**整改后终态**：`bash scripts/gate.sh` **EXIT=0 / 18 项 / 0 阻断**；verify 158/158；vocab 320 行 FAIL0 WARN0；逐章归属 100%；结构 0；corruption 0；总览整串查无 0。
**五步审查（a–e）全部完成，阻断型 5 处已整改并复验。**