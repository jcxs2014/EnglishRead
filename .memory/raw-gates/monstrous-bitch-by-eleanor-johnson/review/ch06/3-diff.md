# ch06 对账（R3）

素读：`1-suread.json`（8 条，全部带 `text/ch06_4_taming_and_reframing_the_monstrous_bit.txt:行` + 逐字 + 字符区间，子代理已脚本校验 `count==1`）。
机器：`2-machine.json`（rc=0，15 块，引语 15 段全 ok，空引号 0，子项齐全，中文密度合格）。
md 293 行，15 块 + 词汇 26 条。原文 193 行 / 46,250 字符（去空白，实算一致）/ 8,803 词。

## 一、漏（素读有、md 无）

无。素读 8 条全部有落点：

| 素读事实 | md 落点 |
|---|---|
| L83《女巫之锤》约 1486、克雷默 | 原句 11、结构列表 16 |
| L87 1484 被 Innsbruck 主教 Georg Golser 驱逐 | 结构列表 16 邻域、概览 L18 |
| L90 轻罪升重罪、capital punishment、untold tens of thousands | 概览 L18、结构列表 14、可质疑处 2 |
| L186 1604 英格兰无实证亦可处死；苏格兰/荷兰/法国/瑞士约 1550 | 结构列表 14 邻域、可质疑处 2 |
| L175 被烧女巫的女儿被逼站火刑堆旁遭鞭打 | 原句 14、结构列表 19 |
| L60 Eusebius/Origen/Augustine 论 magic 来自恶魔 | 结构列表 13 |
| L35 基督教用笔刺死莉莉丝与拉米亚（对马尔杜克用箭） | 概览 L18、结构列表 9、原句 3 邻域 |
| L49「if Mary is going to live, Lamia is going to have to die」 | 概览 L18、原句 8 邻域、证据链 |

## 二、编（md 有、原文无）

无。逐条核过：

- 「十二世纪 Alanus de Insulis 保留掐死婴儿、吮吸童血，却抽掉实体性」←「**Alanus de Insulis** … She feeds … on human flesh … **lamiae are known to prey on young children by suffocating them and sucking out all their blood**」（概览 L18、结构列表 8）
- 「Rabanus Maurus 把拉米亚读作异端与伪善者」←「the ninth-century CE biblical commentator **Rabanus Maurus** says of biblical lamiae that they **represent heretics or hypocrites**」
- 「《启示录》17 章」←「The beginning of **Revelation 17** explains how the Whore of Babylon came across the surging waters… (17:1–2)」
- 「Federici 圈地与猎巫同步」←「As **Silvia Federici** has argued, the systematic persecution of witches is intimately tied to the consolidation of private property… areas where there was a **high degree of enclosed land**」
- 「Reginald Scot《巫术的发现》1584 否认女巫存在」←「**Reginald Scot's Discoverie of Witchcraft (1584), which forcefully denies the existence of witches**」
- 「十四世纪的瘟疫进一步刺激迫害」←「the advent of the **Black Death in the late fourteenth century stimulated witch persecution**」
- 「1532 年《卡罗利纳法典》」←「the earliest law that made witchcraft punishable by death passed in **1532: the so-called Carolina, an imperial Spanish code**」（原文自己写 Spanish，md 未改）

## 三、错（两边都有但不一致）

### 1. 【提示】「中文理解」里留着未译的英文常用词

- md:106（原句 4 的中文理解）：「玛利亚的力量并不在于强壮、 **cunning**、魔法、暴力、召魂的能力…」——原文该处是 `her cunning`。
- md:238（原句 15 的中文理解）：「父权一旦控制不了那些 **womb**，就只有把装着这些 **womb** 的女人妖魔化并杀掉，同时杀掉那些…控制 **womb** 的女人」——同一句里三处；前一句已用「子宫」，此处突然切回英文。
- 判断：两处都不是专名或术语（本书体例允许 Monstrous Bitch／lamia 等原文术语留英），是把普通英文词漏译，属 S3「英文夹杂」。合判一条提示，改法：`cunning` → 「狡黠」；三处 `womb` → 「子宫」。

## 四、本文件读过的候选行

`assertion_scan.py` 对 ch06 报出的行全部人读（①相对章号、②绝对断言、③数字、④亲属、⑤方向）；另对 `Malleus／1484／Golser／1604／tens of thousands／Carolina／1275／1360／Black Death／have to die／Rabanus／Alanus／Revelation 17／Federici／Scot／maternal mortality` 十六个关键串做了定位（脚本在 `/tmp/t3mb/`）。
