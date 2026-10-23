# ch38（Chapter Thirty-Seven）深审 R5 判定

> 机器层：`2-machine.json` rc=0，8 块精读，segment_miss 0。
> R1 素读：`1-suread.json` 15 facts，全部回源命中（MISS 0）。

## R3 三张单子

- **词表**：v38 探针 13 行，例句逐字命中 13／13。
- **撇号**：ap38 直撇号 token 2（md L13 `didn't`、L84 `doesn't`，均为引原文）→ **阻断 C-38-1**；backtick span 0。
- **块内嵌英文**：in38 未命中 3，其中模板 2，剩 1（`house-bones-Ida`）→ 假红 F-38-1。

## 判定汇总

- **阻断：1**
  - **C-38-1**（引原文用 ASCII 直撇号，先例 C-34-2／C-35-1 同型）：
    - md L13「her acceptance didn't warm me」——原文 text/ch38_chapter_thirty_seven.txt:99 为弯撇号 `didn’t`。
    - md L84 关键词行「doesn't know」——原文 L198 为弯撇号 `doesn’t`。
- **提示：1**
  - **P-38-1**：导航「Aunt Virginia 攥着她冰凉的手臂」——原文 L229 "she grasped my arm again. Her fingers were cold, her grip bruising, not unlike Mama's."：冰凉的是 Virginia 的手指，攥住的是 Dart 的手臂；中文「冰凉的」修饰「手臂」造成归属错位，宜改「用冰凉的手指攥住她的手臂」。
- **假红：1**
  - **F-38-1**：in38 探针标 `house-bones-Ida` 全书查无——原句1「为什么这样写」层的分析者自造连字标签，三要素（house／bones／Ida）均在 L9 原文，非引语形态、无凭空内容，不构成缺陷。

## R4 逐块对应（8 块）

| 块 | 取证（text/ch38_chapter_thirty_seven.txt） | 结论 |
|---|---|---|
| 原1 150磅／beneath Greer House／gloat | L9 逐字 | ✓ |
| 原2 Begging a fainting spell／haint | L15 逐字 | ✓ |
| 原3 mirror／perverse fervor／electrified／collarbone | L18 逐字 | ✓ |
| 原4 beehive／blush／rifle | 引语逐字（机器层+suread 核） | ✓ |
| 原5 acceptance didn’t warm me／eel／devil | L99 逐字（md 引文撇号形态见 C-38-1） | ✓（内容） |
| 原6 purple bruise diagonally／napkin／double take | L132 逐字 | ✓ |
| 原7 Dart doesn’t know this／Beaumont to Greer／show up to court | L198 逐字 | ✓（内容） |
| 原8 without any fuss／wrenched／scraping | L246 逐字 | ✓ |

## 导航层断言

| 断言 | 取证 | 结论 |
|---|---|---|
| 拒绝仪式性献祭、认出自己狂热带 | L15／L18 | ✓ |
| 「我只会更糟」 | L21 "I'd only gotten worse." | ✓ |
| 风暴 Flora、鸟群先哑、止痒膏、露台素描、与画像保持距离 | L33 逐字 | ✓ |
| 撤离公路按住逃路、等待点名继承人 | L33（Savannah 想法＋traffic report dissuaded＋waiting…name me heir） | ✓ |
| Cat One 升级 | L48 | ✓ |
| Ida let me be, presumably appeased | L36 | ✓ |
| 宾客水晶杯「太多」、玫瑰香婴儿粉「令人窒息」、黄玫瑰花尖发褐 | L45 逐字 | ✓ |
| 含羞草鸡尾酒递进（third mimosa） | L48／L102 | ✓ |
| Mama 改姓 Beaumont 令说话人不快 | L78 "how miffed she'd been…Mama changed her last name to Beaumont" | ✓ |
| Harrison 求一句私密话、被她躲开 | L144 "Can we go somewhere private?"＋L151 made myself conspicuous | ✓ |
| Gazzie 站高五级台阶、「象征性又上镜，以防有人发社交媒体」 | L165 逐字（five steps／Symbolic and picturesque／social media） | ✓ |
| 文件当天上午已签 | L192 "Signed the paperwork this morning." | ✓ |
| 改姓程序 Beaumont→Greer、未经她同意 | L198 | ✓ |
| 画像黑水泛涟漪、墙里低鸣、Virginia 与她都盯着 | L180／L183 "black water rippled"／L186 "A low hum began in the walls" | ✓ |
| Virginia 攥臂留话「需要逃离就打给我」 | L229／L231 "Call me if you need to get out of here."（冰凉归属见 P-38-1） | ✓（内容） |
| Leon 房门后哽咽、自问「我得到了一切，不是吗？」 | L240／L246／L252 "I'd gotten everything I wanted. Hadn't I?" | ✓ |

## 已核实为正确

- 引语 8 块逐字（s38 15 facts MISS 0；机器层 segment_miss 0）。
- 词表 13 行例句逐字。
- 导航/弧线/手法层 16 项断言回源命中；时序（剥皮间→白昼→派对→致辞→空房）与原文一致。
- 直撇号仅 2 处且已列阻断；无数量断言异常；人物关系（Harrison 25 岁等）本章未涉。
