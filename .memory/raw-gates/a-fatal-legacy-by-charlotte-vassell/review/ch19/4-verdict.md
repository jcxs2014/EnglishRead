# 4-verdict · ch19《A Fatal Legacy》审查判定表

> 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch19 the post office box leads to harrogate.md`
> 权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch19_19.txt`
> 落盘：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch19/`
> 档位四分：**阻断**（与原文不符/缺失）／**提示**（措辞正当或引申过头）／**假红**（工具判错）／**跳过**（没查）。
> 硬约束：每条「阻断」必须带 `text/<文件>:<行>` 与该处**原文逐字**；给不出逐字证据的只能写「未核」（跳过型）。

---

## 0. 四组数（只报这四组，不给单一「阻断 0」）

| 组 | 计数 | 明细 |
|---|---|---|
| **逐字** | **6/6 通过，0 阻断** | 6 条引语**整串**（含外层 ‘’）在 `text/ch19_19.txt` 中**连续命中**（自写 Python 全串比对，命中位 41/619/1042/2277/2829/4129）；`chapter.sh` 独立重建后同样 6/6 ✅。本章 **0 处省略号拼接**（6 条引语无一含 `…`），0 处跨话轮拼接，0 处跨章搬句，0 处词形/术语/零命中告警 |
| **对应** | **6/6 成立，0 需退引语，0 密度不足，0 施事反转** | 逐块见 `4-correspondence.md`；6 块均含"为什么这样写"（密度达标），0 块讲全书主旨/作者生平，R4 固定三问（主语／受事／方向）6/6 一致 |
| **形态** | **一致 3 项 ／ 偏离 2 项（均已给理由）** | H1／导航项名与项数／子项集 **三项与本书众数与 profile 全一致**；偏离：①**块数 6**（本书中位 7.0、范围 5–10 → 在区间内、低于中位 1 块，理由见下）；②**未标注所属分部「A TUESDAY IN MAY」**（本书 54 章中 26 章带分部标注，ch19 不在其中） |
| **断言** | **核验 25 条：阻断 1 ／ 提示 11 ／ 通过 13** | 明细见 §2；另 1 条机器报警判为**假红**（`check_vocab` 的「toothbrush 超纲」），见 §2.1 |

---

## 1. 逐字层（R2 机器层 + 自写第二实现）

| 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|
| 6 条引语逐字命中原文 | `text/ch19_19.txt:20`[40,263]、`:32`[618,758]、`:47`[1041,1448]、`:83`[2276,2816]、`:89`[2828,3353]、`:128`[4128,4320] | 自写 Python 全串包含判定 6/6 True；`2-machine.json` `quotes[].segments[].ok` 全 true、`segment_miss: 0` | 通过 |
| 引语在原文中连续（无 `…` 缝合） | 同上 | 6 条引语无一含省略号；首尾锚点间隔均等于引语自身长度，无跨段拼接 | 通过 |
| md 未改写引语内字词（含外层引号 ‘ ’） | 同上 | md 引语行外层为 `"…"` 行内 `‘…’`，与源文一致 | 通过 |

## 2. 断言层（人判：漏／编／错／事实断言／说话人／施事）

| # | 断言 | 证据（章:区间 / md 行） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | 原句 1 三项信息的顺序是「地点→付款人→地址」，收尾在「只买了三个月」 | `text/ch19_19.txt:20`[40,263]：`The PO Box is located in Barnet and was paid for by a Mrs Beverley Parkin, her address is in Harrogate. They only bought it for three months.` | 与原文一致 | 通过 |
| A2 | 原句 1「谁付的钱 → 钱付给了谁 → 人在哪」这个顺序 | 同上 | 源句顺序为地点→付款人→地址；「钱付给了谁」不在引语内（原文只有 `paid for by`）；且与同块 `:22` 自述顺序不一致 | 提示 |
| A3 | 本章有「一张收据」 | `text/ch19_19.txt:20`：`opening the email`＋`the information from the Post Office`；`grep -c -i receipt text/ch19_19.txt` → `0`，退出码 1 | 本章无收据实物；md 四处用「收据」为比喻性引申（且任务简报本身用此措辞） | 提示 |
| A4 | 原句 2 说话人＝Matt | `text/ch19_19.txt:32`[618,758]（源文未标说话人） | 依全书严格轮换推定：`:20` 显名 Matt → `:23` 显名 Caius → 轮换 `:26`=Matt、`:29`=Caius、`:32`=**Matt**、`:35`=Caius、`:38` 显名 Matt ✓ 全部自洽 | 通过（见 §4） |
| A5 | 原句 3 说话人＝Nathan | `text/ch19_19.txt:41` 显名 `said Nathan`、`:47`[1041,1448] | 一致 | 通过 |
| A6 | 原句 4 说话人＝Nathan | `:83`[2276,2816]（Nathan 独白续段） | 一致 | 通过 |
| A7 | 原句 5 说话人＝Nathan | `:89`[2828,3353] | 一致 | 通过 |
| A8 | 原句 6 说话人＝Tiny Simm | `:116` 显名 `Tiny Simm came into the incident room`、`:122` `‘Seven.’`、`:128`[4128,4320] | 一致（且 `:119/:122/:125/:128` 为 Caius–Simm 严格交替） | 通过 |
| A9 | Nathan 买酒、Digby 表白、姐姐把妹妹拽走 | `:89`：`I kept buying jugs of cheeky woo woos`／`Digby declared his undying love`／`pulled away into the night by her sister` | 三个施事归属全部一致（买酒＝Nathan、表白＝Digby、拽走＝姐姐） | 通过 |
| A10 | 「叫 Posh Digby」是全班同学一起叫 | `:47`：`we all called him Posh Digby at uni` | 一致（未写成 Nathan 独自叫） | 通过 |
| A11 | Digby 只是**自称**策展人（md 写成「讲…的故事」） | `:83`：`saying that he was a curator in a museum down in London` | md 保住了「自称」层，未写成他真是策展人 | 通过 |
| A12 | 「在伦敦一家博物馆**当馆长**」 | `:83`：`a curator in a museum` | curator＝策展人/馆员，「馆长」职级上移一格；与同块关键词 `curator in a museum` 不一致 | 提示 |
| A13 | 「她从没被人这样正眼看过」 | `:83`：`It was **as if** Digby was the only man who’d ever seen her` | 原文为揣测语气，md 写成事实 | 提示 |
| A14 | 妹妹「**独自出现在哈罗盖特**」 | `:77`[1901,2232]：`There was this girl there **with her troll of a sister**.`；`:89`：`pulled away into the night **by her sister**` | 与源文两处相反；md 自身 `<md>:38` 又写对「酒馆里有两个姐妹」⇒ 内部亦矛盾 | **阻断** |
| A15 | 本章「排除掉**一圈**人」 | `:32`[618,758] 只排除 Bev 一人；md `<md>:29` 自写「**排掉一个人**」 | 数字口径与源文及 md 自身都不一致 | 提示 |
| A16 | Simm「**从不敢进屋**」 | `:116`：`Tiny Simm moved on the spot. He felt like he was sticking his head above the parapet.` | 原文只写紧张＋怕出风头；「不敢进屋」是引申 | 提示 |
| A17 | Nathan 把「一场命案包成一次好玩的周末」 | `:89`：`It was a fun day.`（Nathan 全段未提命案） | 被包成「好玩周末」的是那次艳遇，不是命案 | 提示 |
| A18 | Simm 报的是「今天早上 Priory Square **七号**」的入室盗窃、报警人半醉、未失窃 | `:116`：`a break-in was reported on Priory Square this morning`；`:122`：`‘Seven.’`；`:128`：`apparently half-cut` | 逐字一致 | 通过 |
| A19 | 「Priory Square＝案发地」 | `text/ch01_1.txt:17`：`The Horatio Combe Institute, Priory Square, Camden`；`text/ch45_45.txt:20`：`the steps to 35 Priory Square` | 案发地在 Priory Square；博物馆在 **35** 号，与七号是同一广场的不同门牌 ⇒ md「七号与博物馆的地址连起来读」成立 | 通过 |
| A20 | 「三年前」的一次日游、当天往返、末班车回约克 | `:95`：`‘Three years ago.’`；`:59`：`we went for the day`；`:89`：`nearly missed the last train back to York` | 一致 | 通过 |
| A21 | 「一个至今没被叫出名字的女孩」 | `:77`/`:83`/`:89` 全程只以 `this girl`／`the younger one`／`the beauty` 指称，本章未具名 | 一致 | 通过 |
| A22 | 本章所属分部「A TUESDAY IN MAY」 | epub TOC `OPS/TOC.xhtml`：`TUESDAY` 分部下辖 16–20；分部文件 `OPS/s027-Part-005.xhtml` 首行 `TUESDAY`，位于 `OPS/s031-Chapter-019.xhtml` 之前 | 归属**正确**，但 md 全文未标注（`grep -i "tuesday\|分部" <md>` → 退出码 1）；本书 54 章中 26 章带此标注 | 提示 |
| A23 | 缺「身份盗用 / Digby 正搬去 York」这条线索 | `:26`[464,515]：`Do you think it was some sort of identity theft?`；`:29`[517,616]：`Although Digby was going to move to York, wasn’t he?` | 两段对话 md 完全未收（6 条引语、导航五项、总结均无）；Harrogate↔York 的桥因此缺失；主干情节不缺 ⇒ 提示 | 提示 |
| A24 | 缺 Caius 开场的「周末小住 / 快下班」话头 | `:23`[265,462]：`It was just the sort of place to go for a weekend away. A baby moon, maybe? Caius checked his watch. It was coming up to the end of their shift.` | 氛围/过场级内容，md 未收；不承载情节转折 ⇒ 提示 | 提示 |
| A25 | 缺 Caius 计划去 Barnet 邮局调监控 | `:107`[3505,3633]：`‘I’ll get hold of Barnet Post Office and get the CCTV for the days that the letters were posted,’` | md 全文无「监控/CCTV」；而本书 `ch25 scott brown goes missing.md:11` 已用「**三天邮局监控**」承这条线 ⇒ 该伏笔立在本章，md 漏收 | 提示 |

### 2.1 机器报警的分类（先读行再定性）

| 报警 | 证据 | 结论 | 档位 |
|---|---|---|---|
| `check_vocab.py`：「ch19 … [基础] 基础档疑含超纲词「toothbrush」」 | 该 lane 输出中同型告警另有 **17 章**（ch21/ch26/ch33/ch34/ch39/ch41/ch46/ch50/ch52/ch54 等），皆为「基础档收了略超纲的常见名词」 | `toothbrush` 是普通基础名词，放 ⭐基础 合理；**工具口径过宽**（同类噪声遍布全书），本条不成立 | **假红** |
| `check_vocab.py` 首次以 md 路径调用时报「正文章节 0 个」 | 该脚本需**书目录**参数 | 属**调用口径错**，非书的问题；改以书目录重跑 → `--- FAIL (0) ---`，词条行合计 1458 | **假红** |
| `corruption_scan.py` / `check_chinese_layer.py` 以 md 路径调用报「该目录下无 md 文件 / 书目录不存在」 | 同上，需书目录 | 同上；改以书目录重跑 → 损坏扫描 FAIL 0、报告 0；中文层 391 块密度 100%、阻断型 0 | **假红** |
| `verify_corpus.py` 的 3 条 WARN | 「未给 --expect」「未给 --anchors」「ch23 疑似页码 bleed」 | 均为**本次调用未传参数**导致的提示，非本章缺陷；`--- P0-0 语料验收: PASS（FAIL 0 / WARN 3）---` | 提示（工具口径） |

## 3. 形态组（R2 form + 本书众数/profile）

| 维度 | 本书众数 / profile | 本章实际 | 结论 | 档位 |
|---|---|---|---|---|
| H1 | 54/54 章皆 `N. <场景标题>` 形（`bookform.py`：`H1 写法：{'N.': 54}`） | `# 19. The Police Station` | 一致；场景标题 `The Police Station` 与源文 `text/ch19_19.txt:17`、epub `OPS/s031-Chapter-019.xhtml` 同名 ✓ | 通过 |
| 导航项名与项数 | 众数 5 项：**一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法** | 5 项，项名与项序完全相同（`<md>:11`–`:15`） | 一致（`nav_count_ok: true`，`nav_missing: []`） | 通过 |
| 子项集 | 众数 4 项：**中文理解 / 关键词 / 为什么这样写 / 读者视角提示**（= profile `mystery-thriller` 子项 4 项） | 6 块全部为这 4 项 | 一致（`subitems_modal` = profile_subitems） | 通过 |
| 块数 | 本书中位 **7.0**，范围 **5–10**；profile 块数 3–10 | **6** | 偏离中位 1 块，落在本书区间内。**理由**：本章是纯对话推进章，Nathan 的整段回忆被切成两块长引语（`:83`、`:89`），其余四块各占一场问答（PO Box 信息 / Bev 排除 / 妹妹 / Simm 报案），合并会越过单块可读长度 | 提示（已给理由） |
| 分部标注 | 26/54 章在导航项里标注所属分部（本书非众数义务） | **无**；本章属 `A TUESDAY IN MAY`（epub TOC 与 `s027-Part-005.xhtml` 已核） | 偏离（缺标注） | 提示 |
| 词汇表 | 全书 lane `--- FAIL (0) ---`；本章 25 条，例句**全部逐字命中本章**（自写脚本 25/25，0 miss） | 通过 | 通过 |

## 4. 已核实为正确（防误修，固定一节 —— 后续任何人不得以「读着不对」为由改动，除非能给出反证）

1. **原句 2 的说话人＝Matt（源文未标说话人，此处为推定；推定成立）** —— `text/ch19_19.txt:20` 显名 Matt（`Matt said`）→ `:23` 显名 Caius（`Caius checked his watch`）→ 按全书严格轮换：`:26`=Matt、`:29`=Caius、`:32`=**Matt**、`:35`=Caius、`:38` 显名 Matt（`Matt put Nathan on speakerphone`）——**链条两端锚点均自洽**。md `<md>:26` 写「Matt 先排除了一层」正确，**不要改成 Caius**。⚠️ 附注：这是本章**唯一**靠推定（而非原文标注）成立的说话人归属；`:32` 的归属推定依据是严格轮换，若日后有人质疑，可补证 Matt 在本章另一处的说话人锚点（`:20`、`:38`、`:50`、`:56`…）。
2. **「Digby 只是自称策展人」** —— `text/ch19_19.txt:83`：`saying that he was a curator in a museum down in London`。md `<md>:38` 用「拼命讲自己在伦敦一家博物馆当…的故事来打动她」保住了**自称**性质（他在吹牛），没有把「他真是策展人」当事实写。**正确**（只有「馆长」这个职称用词另见 A12 提示）。
3. **「Priory Square＝案发地」「七号与博物馆地址连起来读」** —— `text/ch01_1.txt:17`：`The Horatio Combe Institute, Priory Square, Camden`；`text/ch45_45.txt:20`：`the steps to 35 Priory Square`。博物馆在 **35** Priory Square，入室案在 **7** Priory Square（`text/ch21_21.txt:20`：`a certain Benedict Carr-Ridge who lived at 7 Priory Square`），同属一个广场。md `<md>:52`、`:53` 的说法成立，**不要改成「同一栋楼」**。
4. **「买酒的是 Nathan，不是 Digby」** —— `text/ch19_19.txt:89`：`I kept buying jugs of cheeky woo woos`。md `<md>:44` 归属正确。
5. **「叫 Posh Digby 是全班一起叫」** —— `text/ch19_19.txt:47`：`we all called him Posh Digby at uni`。md `<md>:32` 写「大学里都叫他」正确。
6. **「三年前的一次日游、末班车回约克」** —— `text/ch19_19.txt:95`：`‘Three years ago.’`；`:59`：`we went for the day`；`:89`：`the last train back to York`。md `<md>:11`、`:44`、`:99` 全部逐字对得上。
7. **「一个至今没被叫出名字的女孩」** —— 本章全程只用 `this girl`／`the younger one`／`the beauty`，未具名；md `<md>:11`、`:41`、`:99` 的说法成立。

## 5. 取证三件套（凡「查无」一律附命令＋输出＋退出码）

```
# 「本章无 receipt」
/usr/bin/grep -c -i "receipt" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch19_19.txt
  → 0        退出码 1
# 「全书 receipt 命中位置（证明本书『收据』另有所指）」
/usr/bin/grep -rn -i "receipt" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/
  → ch04:35, ch04:62, ch04:68, ch16:205, ch16:223, ch27:176, ch32:137      退出码 0
# 「md 无 identity theft / 无『搬』」
/usr/bin/grep -n "identity theft" "notes/.../ch19 the post office box leads to harrogate.md"   → 退出码 1
/usr/bin/grep -n "搬" "notes/.../ch19 the post office box leads to harrogate.md"              → 退出码 1
# 「md 无分部标注」
/usr/bin/grep -n -i "tuesday\|分部" "notes/.../ch19 the post office box leads to harrogate.md" → 退出码 1
# 「本书 54 章中 26 章带分部标注」
/usr/bin/grep -rl "分部" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/*.md → 26 个文件   退出码 0
# 「Priory Square / 案发地」
/usr/bin/grep -n "Priory Square" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/*.txt → 退出码 0
  （ch01:17 与 ch02:17 = 研究所地址；ch19:116 = 本章报案；ch21:20 = 7 Priory Square；ch45:20 = 35 Priory Square）
```
（全部使用**显式文件路径**的 `/usr/bin/grep`；未用 `git grep`、未用 rg 默认 ignore 规则——`text/` 被 `.gitignore` 排除，用那两类工具会得到假零命中。）

## 6. 覆盖声明

- **本轮人判范围：仅 ch19**（R1 素读 → R2 机器层 → R3 三张单子 → R4 逐块对应 → R5 判定表）。
- 其余 53 章**只有机器层**，**不得记作「通过」**：`bash scripts/gate.sh "<书目录>"` 退出码 **0**、「正门结论：0 条阻断型」、391 引语块密度 100%、逐字 1880 ✅、`verify_corpus.py` PASS、`corruption_scan.py` FAIL 0 —— 但这些是**机器口径**，未做人判。
- 本章类型：**对话密集章 + 回溯章**（Nathan 一段长独白承担时间线回溯），按 `docs/rules/生产-审查对照.md` 的「章型加权」，S2（跨话轮拼接）与 S3（说话人/施事）为本章重灾区 → 本次已对 6 块逐块做了 R4 固定三问（主语／受事／方向），**0 处施事反转**；6 条引语 **0 处跨话轮拼接、0 处省略号缝合**。
- 独立性说明：R1 素读**先于**开 md，且 `1-suread.json` 已落盘（含 18 条动作级事件＋13 条人物关系＋6 组数字/日期，全部带原文字符区间）；R2 机器层与本文件的引语核对用**第二实现**（自写 Python 全串包含判定），不复述既有分析。

## 7. 结论（给修复方）

- **阻断型 1 条**：`<md>:41`「独自出现在哈罗盖特」与 `text/ch19_19.txt:77`（`There was this girl there with her troll of a sister.`）及 `:89`（`pulled away into the night by her sister`）相反。改法：→「**和姐姐一起出现在哈罗盖特**」。
- **提示型 9 条 + 2 条漏收**（共 11 条）：A2、A3、A12、A13、A15、A16、A17、A22、A23（断言层 9 条）+ A24、A25（漏收 2 条）。均不阻断交付，但「唯一那条阻断」修完须**重跑 R2**（不能以「现在 0」代替「每处都修过」）。
- **四组数**：逐字 **6/6 通过 / 0 阻断**；对应 **6/6 成立 / 0 选短 / 0 密度不足 / 0 施事反转**；形态 **3 项一致 / 2 项偏离（块数 6 < 中位 7.0，已给理由；未标分部 A TUESDAY IN MAY）**；断言 **25 条核验：阻断 1 / 提示 11 / 通过 13**（另有 1 条机器报警判假红、3 条工具调用口径假红）。
