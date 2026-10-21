# 4-verdict.md · ch25《The Police Station》判定表

- 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch25 scott brown goes missing.md`
- 权威源：`text/ch25_25.txt`（245 行 / 10177 字符）
- md 快照：sha256 `743f937f9495db3dbaf4afc6905c41477265d5af291ac71d46d6e18303e911ce`（HEAD `a363a8883`，2026-10-21 14:35:04 +0200）
- R2 机器层：`bash scripts/chapter.sh "…/ch25 scott brown goes missing" --json` → **退出码 0**，`verdict=ok`；`counts = {blocks 8, segments 8, segment_miss 0, struct_bad 0, empty_quote 0, keyword_bad 0, cjk_low 0}`（原始输出存 `2-machine.json`）
- 附带机器层：`python3 scripts/bookform.py "<书目录>"` → 退出码 0；`python3 scripts/check_vocab.py "<书目录>"` → 退出码 0，FAIL 0（WARN 26 条全部落在 ch13/ch18/ch19/ch21/ch26/ch33/ch34/ch39/ch41/ch46/ch50/ch52/ch54，**无一条指向 ch25**）；`python3 scripts/corruption_scan.py "<书目录>"` → 退出码 0，FAIL 0 处。

## 覆盖声明

- 本次审查**只负责第 25 章**，其余 53 章**不在本次范围内**（同一书目录另有他实例在审 ch20/ch22/ch23/ch24/ch26/ch07 等章），**不得把本章结论外推为全书结论**。
- 本章为「对话密集 + 章末 cliffhanger」型章，按 `docs/rules/生产-审查对照.md` 加重了 S2（跨话轮/拼接）与 S3（说话人、施事归属）两层；R4 八块逐块人判已全做。
- 未查项：全书级总览三篇、跨章引用（`check_crossref`）不在本次委托范围 ⇒ **标「跳过」**。

---

## 一、逐字组（引语与例句的英文逐字）

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | md 的 8 个引语块引语全部逐字命中原文 | `2-machine.json` → `quotes[8].segments[*].ok = true`，`segment_miss = 0`；复核用独立脚本取 md 中 8 条引语原文串逐条 `in text/ch25_25.txt` → 8/8 FOUND（长度 83 / 44 / 147 / 116 / 269 / 353 / 286 / 177 字符） | 成立 | — |
| 2 | 无省略号缝合、无跨话轮拼接 | 8 条引语中 0 处含 `…`/`…`；`2-machine.json` 中每块 `segments` 数均为 1，块 3/5/6/7/8 的超长引语在 `text/` 中均为**一条连续原句**（非拼接），例：块 8 `text/ch25_25.txt:230` 全句 177 字符连续存在 | 成立 | — |
| 3 | 引语带引号与嵌套引号（`“ery”`、`“fake Isolde”`）与原文一致 | `text/ch25_25.txt:53` `‘Something “ery”.’`；`:230` `“fake Isolde”`；md 对应位置逐字相同 | 成立 | — |
| 4 | 词汇表 26 条例句逐字来自本章原文 | 逐条 `example in text/ch25_25.txt` 判定 → 26/26 命中（另 3 行 MISS 为表头 `词/短语 \| 例句`）；含长例句 `md:84`、`md:101`（L87 全句）、`md:86`（L87 片段）、`md:82`（L81 全句） | 成立 | — |

**逐字组：4/4 断言成立，缺陷 0。**

## 二、对应组（每块中文是不是在讲这句引语）

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 8 块全部「对应」，无「讲全书主旨／作者生平」的不对应块 | `4-correspondence.md` 逐块判定；块 1/2/3/4/5/6/7/8 均以引语本身为主语 | 成立 | — |
| 2 | 8 块说话人全部核对通过（专家／凯厄斯×3／艾米×3／凯厄斯），无错配 | `text/ch25_25.txt:20`（specialist）、`:32`、`:53`、`:96`、`:135`、`:230`（Caius）、`:50`、`:62`（Amy）；md 块 3/4/5/6/7/8 的主语标注与原文一致 | 成立 | — |
| 3 | 8 块施事／受事方向与原文一致，无「谁的／谁欠谁」反转 | 块 8：`Digby had a sexual interest in “fake Isolde”` 归迪吉、`poor Scott … might’ve too` 归斯科特（`:230`）；块 3 艾米认的是**包**不是包上的人（`:50`）；块 7 面包卷归 Digby、法棍归 Amy（`:135`） | 成立 | — |
| 4 | 无「只复述字面、没有为什么这样写」的密度不足块 | 8 块均含「为什么这样写」且均为写法层说明（频次即画像／一个「但是」做实对照／物证路线／残缺线索／借街区日常升格物证／链条合拢／食物交叉／并类模式）；`cjk_low = 0` | 成立 | — |
| 5 | 块 8 的「为什么这样写」「读者视角提示」用了引语之外的现场物证（独自备好酒、两只杯子、空相框） | 原文 `text/ch25_25.txt:221`（`an empty photo frame`／`A bottle of open but untouched Chablis`／`Two glasses … and an optimistic condom`）；块 8 引语范围 `:230` 不含这些物件 | 讲的是引语之外的上下文 ⇒ 引语偏短 | **提示** |

**对应组：5 条断言中 4 条成立，1 条提示（无阻断）。**

## 三、形态组（H1／导航／子项集／块数 vs 本书众数与 profile）

| # | 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|---|
| 1 | H1 形态 | `md:7` `# 25. The Police Station`；`2-machine.json.form.h1_shape_ok = true`；`bookform.py` → `H1 写法：{'N.': 54}`（本书 54 章全部「N.」式） | 与本书众数一致 | — |
| 2 | 章节小标题与书内既有形态一致 | 原文 `text/ch25_25.txt:17` `The Police Station`；md H1 作 `25. The Police Station` | 一致 | — |
| 3 | 导航项名与项数 | `md:11-15` 五项：**一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法**；`bookform.py` → `导航项（众数，5 项）：一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法`；`form.nav_count = 5`，`nav_missing = []` | 一致 | — |
| 4 | 子项集 | `2-machine.json.form.subitems_modal = [中文理解, 关键词, 为什么这样写, 读者视角提示]`，与 `profile_subitems` 完全相同；md 每块四子项齐备（`struct_bad = 0`） | 一致 | — |
| 5 | 块数 | `form.blocks = 8`；本书 `block_median = 7.0`、`block_range = [5, 10]`；`profile mystery-thriller` 允许块数 `3–10` | 8 落在 5–10 区间内且符合 profile ⇒ **无偏离**（不需写理由） | — |
| 6 | 词汇表结构 | `### ⭐⭐⭐ 高级 / ⭐⭐ 进阶 / ⭐ 基础` 三档齐备，例句全属本章；`check_vocab.py` 对本书 FAIL 0 且 26 条超纲 WARN 无一条指向 ch25 | 一致 | — |

**形态组：6/6 成立，偏离 0（故无需理由行）。**

## 四、断言组（漏／编／错，事实断言逐条）

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | md 应交代 Scott「昨天与今天都没来上班、他从不迟到、非常尽职」，这是警方上门的因果前提 | 原文 `text/ch25_25.txt:108` `‘I knew it when Scott didn’t come to work yesterday and again today. I hoped he was sick maybe and forgot to call.’`；`:114` `‘Yeah, very. He’s never been late before. He’s very conscientious. Is he in trouble?’`；`:120` `‘Yeah,’ Jodie said, opening her laptop and retrieving the details.`。md 侧：`迟到`0／`失踪`0／`地址`0 次；`md:11` 与 `md:120` 由「问出他叫斯科特·布朗」直接跳到「见到他的尸体」 | 关键转折缺失（章题即「goes missing」） | **阻断** |
| A2 | md 应交代死因与 Barry 的法医判断（腹部一刀、刺到肝、快速休克、只有一处刺伤） | 原文 `text/ch25_25.txt:194` `‘Stabbed in the gut. I’d say they nicked his liver. Not a nice way to go. He would’ve gone into shock quite quickly though,’ … ‘One stab wound. The killer thought they’d done enough.’`。md 侧：`法医`0／`巴里`0／`肝`0／`休克`0；`刺`1 次仅在 `md:103` 词汇例句 `carotid` | 关键事件缺失（本章唯一的死亡场景分析层空缺） | **阻断** |
| A3 | 「不是职业杀手」这一判断应进入分析层 | 原文 `:197` `‘Professional kill?’`、`:200` `‘Oh no, I should say not… A professional would’ve gone straight for an artery like the carotid. No one would survive that.’`。md 侧仅 `md:103`／`md:116` 两条无释义词汇例句 | 结论被保留（孤独的男人模式）、证据层未落地 | 提示 |
| A4 | 应写出 Caius 的核心因果假设：Scott 因送信到 P.O. Box 知道太多而被灭口 | 原文 `:224` `…then killed Scott because he knows too much about them from delivering the letters to the PO Box or …`。md 侧 `信箱`0／`P.O. Box`0 | 关键因果链缺失 | 提示 |
| A5 | 章末推问链（Priory Square 猎场 / `Is she spiralling?` / `She sounds cool. I’d like to be her friend`）应有落点 | 原文 `:239` `‘And she has a hunting ground around Priory Square.’`、`:242` `‘Is she spiralling?’`、`:245` `‘She sounds cool. I’d like to be her friend,’ Amy said.`。md 侧仅 `md:15` 概括「她有猎场」，`失控`0／`spiralling`0／`Priory Square`0 | 章末落点只有概括没有原句 | 提示 |
| A6 | Amy 的投毒焦虑（面包没吃几口 / 怀疑菠菜）与 `:179` 的 `‘Regulate your own emotions and behaviour, bitch.’` | 原文 `:185` `‘Starving, but the point still stands.’ She hadn’t eaten much of her baguette. She’d kept thinking about poisonings, and wondered if the spinach in hers was what she thought it was.`；`:179`。md 侧 `投毒`0／`毒`0 | 人物节拍缺失 | 提示 |
| A7 | Jodie 的身份应为共同所有人（co-owner） | 原文 `:90` `She introduced herself as Jodie, the co-owner of the bakery.`；md `md:11` `面包店女店主朱迪` | 中文压缩过度（合伙人≠店主），不影响剧情 | 提示 |
| A8 | 块 7 读者视角提示的「香味」在原文没有 | md `md:66` `艾米的依据是香味和罂粟籽`；原文 `:135` 艾米只是 `She looked down at her honey-roasted goat’s cheese, sundried tomato, spinach and tapenade baguette uncertainly.`（低头看，未闻）；本章唯一 `smell` 在 `:161` `They smelled him before they saw him.`（尸臭） | 编·细节级 | 提示 |
| A9 | 块 5「他就住在附近、每天上班路过」是推断而非原文 | md `md:51`；原文只有 `:59` `‘So he’s local.’` 与 `:62`（他是店员） | 编·推断被写成事实 | 提示 |
| A10 | 块 4「本区只有一个（店名）」原文无此断言 | md `md:45`；原文 `:56` 只写艾米认出 Purple Toad Bakery | 编·断言 | 提示 |
| A11 | 块 2「为什么不能寄给收信人本人」原文未在本章断言 | md `md:31`；相关只有 `:224`（Caius 的推测）与 `:167`（Amy 的问句） | 编·断言（写成读者追问尚可，预设为陈述） | 提示 |
| A12 | 「整条樱草山／整条街」与原文人口口径不合 | md `md:13`／`md:49`／`md:51`／`md:52`；原文 `:56` `Everyone in Primrose Hill was shuffling their baguettes around in them.` | 编·口径（区域 vs 一条街） | 提示 |
| A13 | 「被搬空的家具」比原文重 | md `md:13`；原文 `:224` `His ex moved out and took half the furniture with them.`（搬走一半；且原文还写明餐桌压痕还在地毯上） | 编·程度 | 提示 |
| A14 | 块 1 中文理解与本章导航对「两个女人」的频次口径应统一 | md `md:21` `两个女人只在三天里的两天出现过` vs `md:11` `两个女人各来两天`；原文 `:26` `‘Two women both came in on two of the three days and one man came in on all three.’`（原文两读皆通） | 错·md 内部不自洽 | 提示 |
| A15 | 块 8「might've too」应译为「也对假伊索尔德有兴趣」，非「难以幸免」 | md `md:70` `看上去恐怕也难以幸免`；原文 `:230` `poor Scott with his hopeful condom looks like he might've too`（`too` 承接 `a sexual interest in “fake Isolde”`） | 错·语义漂移（欲望 → 被害） | 提示 |
| A16 | 导航里的分部名 | 审查开始时 `md:11` 为 `在分部「A WEDNESDAY IN MAY」里`（自造措辞）；已由他实例在 `a363a8883`（2026-10-21 14:35:04，commit message 注明「19 章分部名改回书内真实标题（A X IN MAY 是自造措辞）」）改为 `在分部「WEDNESDAY」里` | 现状已正确，本轮无需改动 | 提示（已修） |
| A17 | 全书总览三篇与跨章引用（`check_crossref`） | — | 不在本次委托范围（只负责 ch25） | **跳过** |

**断言组：核 17 条 → 阻断 2（A1、A2）／提示 14（A3–A16）／跳过 1（A17）。**

---

## 五、四组数（唯一上报口径）

| 组 | 分子/分母 | 缺陷 | 说明 |
|---|---|---|---|
| **逐字** | 引语 8/8 逐字命中；词汇例句 26/26 逐字命中；省略号拼接 0 处 | **0** | 机器 `segment_miss=0` + 独立脚本复核一致 |
| **对应** | 8/8 块对应（不对应 0、密度不足 0、引语选短/溢出 1＝块 8） | **1 提示** | 无阻断 |
| **形态** | H1 ✓／导航 5 项 ✓／子项 4 项 ✓／块数 8（众数 7，范围 5–10，profile 3–10）✓ | **0 偏离** | 无偏离，故不写理由行 |
| **断言** | 核 17 条（漏 6／编 7／错 3 ＋ 跳过 1） | **阻断 2**（A1 失踪前提层缺失、A2 死因层缺失）／提示 14／跳过 1 | 明细见上表与 `3-diff.md` |

**阻断型条数：2。**

---

## 六、R5-补 · 「零命中」类断言的自证（命令 + 输出 + 退出码）

```
# 1) 本章专属判据点名项：身高 / 发色 / 咖啡馆习惯（md 与原文都应为零）
$ cd notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell
$ /usr/bin/grep -cniE 'hair|blond|blonde|height|tall|short man|café|cafe|coffee' text/ch25_25.txt
0
（退出码 1＝无命中；配套 python 逐词扫描 hair/blond/height/tall/café/cafe/coffee 均为 0，smell=1 见下）
⇒ 结论：text/ch25_25.txt 全章不含身高、发色、咖啡馆习惯；
        md 侧同样为 0（md「咖啡」1 次＝md:102 词汇 gloss「卡布奇诺（咖啡）」，非 Scott 的习惯）——
        ⇒ md 没有凭空造出这三项，属**正确的不写**，不是漏写。
        （这三项属 ch30《scott left a trail of coffee cups》「咖啡杯轨迹」与 ch29 的内容，不在 ch25 语料内。）

# 2) 本章唯一一处 smell 的位置（用于判定 md:66「香味」为编）
$ /usr/bin/grep -nE "smell|scent|aroma" text/ch25_25.txt
161:Caius waited to the side as the front door to Scott’s flat was broken down. They smelled him before they saw him. Barry went in first followed by forensics.
（退出码 0，1 命中）—— 是尸臭，不是面包的香味。

# 3) 分部名零命中的口径说明（不能当伪证）
$ /usr/bin/grep -rn "WEDNESDAY" text/ > /tmp/z2 2>&1; echo $?
1
（0 行命中）—— text/ 提取件只保留小节标题（如 :17 The Police Station），**不保留分部标题**，
   故「查无」≠ 原文没有；该条已由他实例在 a363a8883 改回「WEDNESDAY」，现状正确。

# 4) 死因关键词在原文的行号（用于 A2 的逐字证据）
$ /usr/bin/grep -nE "Stabbed|liver|shock|Professional|carotid" text/ch25_25.txt
194:‘Stabbed in the gut. I’d say they nicked his liver. Not a nice way to go. He would’ve gone into shock quite quickly though,’ Barry said, looking down at the body in front of him. ‘One stab wound. The killer thought they’d done enough.’
197:‘Professional kill?’
200:‘Oh no, I should say not,’ Barry said, standing back as the body bag was being zipped up. ‘They were lucky. A professional would’ve gone straight for an artery like the carotid. No one would survive that.’
224:‘He’s just gone through a break-up,’ Caius said to Amy as she re-entered the room. …
（退出码 0，4 命中）
```

---

## 七、已核实为正确（防误修，护栏）

以下写法「读着像错」，回原文核对后**成立**，后续任何人不得以「读着不对」为由改动：

1. `md:11` `恩菲尔德的一间旧市政公寓` ↔ `text/ch25_25.txt:145` `It was ex-council in Enfield.`（ex-council＝前市政／市政住房楼；中文「旧市政公寓」成立）。
2. `md:11` `只有一封信` ↔ `text/ch25_25.txt:32` `‘But the man only has a letter,’ Caius said`；`md:120` `只带一封信` 同 ✓。
3. `md:13` `空相框` ↔ `text/ch25_25.txt:221` `On the mantlepiece was an empty photo frame. It was in pride of place and yet showed nothing off.`（在壁炉架上、不在桌上；md 未说它在桌上 ✓）。
4. `md:13`/`md:73` `没动过的 Chablis` ↔ `:221` `A bottle of open but untouched Chablis`（开了但没喝）✓。
5. `md:13`/`md:73` `两只杯子` ↔ `:221` `Two glasses were sat next to it` ✓（与酒和安全套同在边桌）。
6. `md:13` `一枚乐观的安全套` ↔ `:221` `an optimistic condom` ✓。
7. `md:11` `三天邮局监控` ↔ `:20`/`:29`（监控对象是邮局 `entering the Post Office`；演示地点才是警局 `left the incident room`）——md 把「警局的事故室」与「邮局的录像」并置，未误称邮局在警局 ✓。
8. `md:15` `三场戏（警局／面包店／公寓）用星号分隔` ↔ 原文两个 `* * *` 分隔（L73、L140）⇒ 三场 ✓。
9. `md:11` `见到他的尸体` ↔ `:161`–`:221` 破门、Barry 验尸 ✓。
10. `md:12` `视角不进任何死者内心` ↔ 全章无 Scott／Digby 内心句 ✓。
11. `md:58` `画像第一次有了工作单位` ↔ `:62` T 恤＝店员 ⇒ 他有雇主 ✓。
12. 词汇 gloss `md:97` `different-shaped | 形状各异的` ↔ `:62` `a variety of different-shaped loaves` ✓；`md:101` `crustless | 不带外皮的` ↔ `:87` `crustless butternut squash quiches` ✓。
13. `md:39`（块 3 读者视角提示）「先认包，再认包上的字，再认衣服上的图案」↔ `:50`→`:53`→`:62` 的原文顺序 ✓。

---

## 八、修复建议（只给方向，本轮未改 md、未 git add/commit）

1. **A1（阻断）**：在「线索结构」或「一句话概括」补一句因果——Jodie 说他昨天与今天都没来上班、他从不迟到非常尽职，警方因此拿到住址上门。
2. **A2（阻断）**：在块 8 的「为什么这样写」或「读者视角提示」补 Barry 的结论（腹部一刀、刺到肝、快速休克、只有一处刺伤；**不是职业杀手**），使「孤独的男人＝模式」这一收束有证据支撑。
3. 提示级可一并处理：A4（P.O. Box 送信）、A5（`Is she spiralling?` / `I'd like to be her friend`）、A8（「香味」改「罂粟籽与自己那份法棍」）、A15（「难以幸免」改「恐怕也对假伊索尔德有兴趣」）、A12（「整条樱草山」改「樱草山一带」）、A14（块 1 与导航口径统一）。
