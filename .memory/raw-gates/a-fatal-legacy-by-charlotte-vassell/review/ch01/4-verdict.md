# 4-verdict.md · 《A Fatal Legacy》第 1 章 审查判定

审查员：独立审查员（仅 ch01）｜底稿：`1-suread.json`（R1 先素读）→ `2-machine.json`（R2）→ `3-diff.md`（R3）→ `4-correspondence.md`（R4）
源：`text/ch01_1.txt`（2404 字符）｜受审：`ch01 digby dies on the institute rug.md`
**R2 原始退出码 0，verdict `ok`，机器层四类 issue 全空 ⇒ 本章全部问题落在机器查不了的三类（漏 / 编 / 对应）。**

---

## 一、四组计数（先给数）

| 组 | 计数 | 明细 |
|---|---|---|
| **逐字** | **27 / 27 相符，0 错** | 引语 6 条（md 6 条，机器 `segment_miss=0`；本审查另以**原始文件**独立取证，6/6 原样命中，偏移 71 / 806 / 1061 / 1546 / 1810 / 2340，**无 `…`、无跨段拼接**）＋ 词汇例句 21 条（⭐⭐⭐6 / ⭐⭐7 / ⭐8，`check_vocab.py` FAIL=0，抽查全为本章原句） |
| **对应** | **6 块：5 对应（1 块附「引语覆盖不足」提示）＋ 1 不对应** | 不对应＝**原句 5**（分析讲的「眼睛来自藏品」不是这句引语）；无「密度不足」块；无「讲全书主旨/作者生平」块 |
| **形态** | **4 / 4 符合，0 偏离** | H1 `# NN. 标题` ✓；导航 **5 项** = profile ✓；子项 **中文理解/关键词/为什么这样写/读者视角提示** 四项全齐、6 块一致 ✓；块数 **6** ∈ profile 3–10（亦 ∈ 本书众数 [5,10]，众数中位 7）✓ ⇒ **无偏离，不需写理由** |
| **断言** | **共核 21 条：相符 6 / 提示 13 / 阻断 1 / 跳过 1** | 阻断 1 条见下表 V1 |

**阻断型条数 = 1**（另附书目录级发现 1 项，非本章 md 缺陷）。

---

## 二、判定表（断言 | 证据（章:区间） | 结论 | 档位）

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| V1 | md 原句 5「为什么这样写」：`那双冷硬如钢的眼睛来自这间屋子里的收藏，与开篇铺陈的柜中标本彼此呼应` | 原文 ch01_1.txt **1810–1865**：`He catches a cold steely eye lazily gazing back at him, and he knows that help isn’t coming…`；对照 **1982–2023** `Horatio Combe’s shrine to his obsessions.`、**2340–2403** `The shrunken heads watch from their cabinet as his heart stops.` | 那只眼睛是**回望他的活人（凶手在场）**；「藏品」是另外的东西。md 把凶手改写成藏品，与原文相反，且与同句「不会有人来救」自相矛盾。**md 编造了原文没有的情节关系。** | **阻断** |
| V2 | md 导航「一句话概括」＋文末「一句话总结」：`中毒濒死`（2 处） | 全文无 poison/毒字样；症状见 **806–872**、**1546–1628** | 属推断而非本章文本事实（本书 ch05 才坐实）；应写「疑为中毒／死因未明」。 | 提示 |
| V3 | md 导航＋文末总结：`自家博物馆` / `自己博物馆`（2 处） | **722–803** `the museum had on the second floor`；**1982–2023** | 原文只说是以祖先命名的研究所，从未说归迪吉所有。 | 提示 |
| V4 | md 原句 1 中文理解：`随之而来的是亚历山大大帝式的劫掠足迹与波斯波利斯废墟上的作乐` | **71–378** `…by an appreciative Naser al-Din, the then Shah of Iran, while he followed in the marauding footsteps of Alexander the Great across Central Asia and made merry with the ruins of Persepolis.` | 劫掠足迹与作乐是**赠礼者 Shah 本人**的行状；md 挂到地毯身上。四项事实都在位，差异在从句归属。 | 提示 |
| V5 | md 原句 3「为什么这样写」：`于是毫无防备地私下赴了约` | **874–1516** `…hadn’t ever stopped to consider that this little tête-à-tête wasn’t the best idea. He was a man, after all…` | 原文先赴约、后自辩；md 因果反了，讽刺点（男人自认无风险）丢失。 | 提示 |
| V6 | md 文末「一句话总结」只写`濒死`，无死亡结局 | **2340–2403** `as his heart stops`；md 自己的导航「叙事手法」写`结尾把死者的结局交给柜中标本的凝视` | 章末总结与本章结局、与 md 自身导航不一致。 | 提示 |
| V7 | md 原句 1「为什么这样写」：`这间屋子把掠夺来的东西包装成馈赠` | **493–543** `It had in fact been purchased down Portobello Road to hide an ugly port stain on the floorboard in 1927…`；**2219–2253** `collecting whatever and whoever took his fancy` | 若指地毯则与原文相反（地毯是买的）；若泛指藏品则成立。一句两读，指代须明确（md 自己的导航写的是对的）。 | 提示 |
| V8 | md 原句 1「为什么这样写」引述：`读者读到最后一句"僵硬的标本正在看着他"时` | **2340–2403** `The shrunken heads watch from their cabinet as his heart stops.`；md 原句 6 中文理解作`柜子里那些风干的缩头就这样看着…`、词汇表注`风干的缩头标本` | md 引号内文字既非原文、也与自身译文不一致（「僵硬」≠「风干」）。 | 提示 |
| V9 | 原文 **2256–2339** `Digby’s throat is beginning to close. He turns his head as he struggles to breathe.` 在 md 中零引用 | 全文检索「喉」「throat」0 命中 | 濒死递进最后一级未进引语/分析/词表；md 却在原句 2 立下「留意自下而上推进的顺序」的线索。取捨理由未写。 | 提示 |
| V10 | 原文 **1519–1545** `Digby can’t feel his legs.` 只出现在词表例句 | md 原句 4 引语自 `The coldness,` 起，丢掉同段首句 | 递进第二级无引语、无分析。取捨理由未写。 | 提示 |
| V11 | 原文 **722–803**（六块未译泥板 / 博物馆二楼）只出现在词表例句 | md 检索「二楼」0 命中 | 「博物馆学者」这一断言的唯一具体证据未进分析层。 | 提示 |
| V12 | 原文 **2219–2253**（NW1 破旧联排住宅）只出现在词表例句 | md 检索「NW1」2 次，均在词表例句 | 迪吉的边缘处境未进导航与分析。 | 提示 |
| V13 | 译名与地名书写：人名 `Digby→迪吉`（非通行译法「迪格比」）；导航「视角」写 `卡姆登 Priory Square 的 Horatio Combe 博物馆`（中英混排），而 ch02 同类导航作「卡姆登普里奥里广场」 | md 第 11–12 行；ch02 导航（仅作对照，未细查其内容） | 不影响忠实度，但全书译名/地名体例应统一。 | 提示 |
| V14 | 书目录 `notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/` 内 ch02–ch54 各有**一个无扩展名重复文件**，内容与同名 `.md` 完全相同（`diff -q` IDENTICAL），共 **53 个**（15 个已被 git 跟踪、38 个未跟踪） | `git ls-files` / `git status -uall` / `diff -q` 实测 | Quartz 会把它们当页面渲染出重复页；后续若有人误用 `git add -A` 会一次卷入几十个重复文件。**属书目录级问题，非本章 md 缺陷；请派工人核实来源后清理（只删无扩展名件，保留 `.md`）。** | 提示 |
| V15 | 「说话人」专项 | 本章 6 条引语全为叙述句/内心独白，**无对话引语**，无说话人可错配 | 不适用（本章型为「首章」，生产-审查对照的加权站点是 S1 与形态；说话人项无从判） | 跳过 |
| V16 | 形态四项（H1 / 导航 / 子项 / 块数） | `2-machine.json` 的 `form` 段 | 全部符合 profile，无偏离 | 记录于「形态」组（不计入本表四档） |

### 与原文相符的 6 条断言（一并列明，避免「只报阻断」的不完整交代）
- **1849 年 / 曾曾曾祖父 / Naser al-Din 为时任伊朗 Shah**（**71–378**）✓
- **1927 年购于 Portobello Road**（**493–543**；md 导航作「其实是 1927 年的旧物」）✓
- **Horatio Combe 为其祖先、其 shrine 收藏 relics**（**1982–2023**）✓
- **柜中缩头标本（shrunken heads in cabinet）**（**2340–2403**）✓
- **「以为只是意外」→「明白有人蓄意安排」**（**1664–1708** `hoping desperately that this was an accident`、**1742–1808** `he knows this was done to him on purpose, that it had been planned`）✓
- **「他从未意识到自己在危险中／谁会想伤害一个 soft-bodied intellectual」**（**874–1516**）✓

---

## 三、机器层结果与「假红」判定

| 探针 | 结果 | 判定 |
|---|---|---|
| `bash scripts/chapter.sh "<ch01 md>" --json` | 退出码 **0**，verdict `ok`；`struct_bad=0`、`empty_quote=0`、`keyword_bad=0`、`cjk_low=0`、`segment_miss=0`；引语 6/6 `ok`；形态段 `h1_shape_ok=true`、`nav_count=5`、`subitems_modal` = profile 四项、块数 6 | 全绿，**无假红**（机器未报任何红项，故本报告无一条「假红」档） |
| `python3 scripts/check_vocab.py <书目录>` | FAIL **0**；ch01 无 WARN（26 条 WARN 全在 ch13–ch54，不属本章） | ch01 通过 |
| 本审查自建取证（原始文件、非归一化） | 6/6 引语原样命中，偏移 71/806/1061/1546/1810/2340；无省略号、无拼接 | 与机器一致，互相印证 |

---

## 四、修复优先级（交派工人，本审查员按纪律 4 未改任何书目录 md、未 git add/commit）

1. **V1（阻断）**：原句 5「为什么这样写」中「那双冷硬如钢的眼睛来自这间屋子里的收藏」——须改为**凶手/活人的眼睛**，并与原文「藏品 = shrine + 柜中缩头标本」分开。改这一处后必须重跑 `chapter.sh`。
2. **V4 / V5（错·提示）**：块 1 从句归属、块 3 因果方向——两处都是「为什么这样写」层的解读方向，改正后密度与对应性同时受益。
3. **V2 / V3（提示）**：`中毒`、`自家博物馆`——改为「疑为中毒／死因未明」「他任职的博物馆」。
4. **V9 / V10（提示）**：把 `Digby can’t feel his legs.` 与 `Digby’s throat is beginning to close. He turns his head as he struggles to breathe.` 补成引语或至少在分析中点名，让「自下而上推进」的线索有据。
5. **V14（提示·书目录级）**：清理 53 个无扩展名重复文件（先核实来源，只删重复件）。
