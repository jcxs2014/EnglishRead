# ch05 · R3 对账（三张单子）

> 依据：`1-suread.json`（先素读，183 行全读）与 `2-machine.json`（rc=0 / verdict ok / blocks=7 / words=2112 / block_target=[4,7]）。
> 机器层：`segment_miss=0`（引语逐字）、`keyword_bad=0`、`struct_bad=0`、`cjk_low=0`、`block_count=0`。
> 补验（机器盲区）：`verify_fragments_indep.py` 全书 312 片段 0 MISS；本章 22 行词表例句 22/22 逐字命中（`/tmp/vocab_check_hx.py`）、22/22 词头落在例句内（`/tmp/vocab_head_hx.py`）。

---

## 一、漏（素读有、md 无）

| # | 素读事实（text 行号） | md 状态 | 判定 |
|---|---|---|---|
| L1 | `:56` `After the infuriating Miss Helena Blair and Superintendent MacDougal had taken their leave, Clio and Thomas insisted on staying with her for the remainder of the afternoon.` —— Clio 与托马斯整个下午都陪着辛西娅；希金斯太太亦在房中至 `:110` | md 导航「情感弧线位置」称全章为「一段**独处时光**」 | **不构成阻断**，转 E1（措辞级）—— md 同段「一句话概括」已写明「在克莱奥坦白魔法……的余波里」，属表述松紧问题 |
| L2 | `:83` 辛西娅向管家点破丈夫的赌局、洗衣女工的蜂蜜杜松子酒、情妇与「他必定树敌」 | 本章未选此段引语 | **不构成阻断**（选句取舍；该段是推理方向而非情节转折） |
| L3 | `:98` 希金斯太太失言后的道歉 `‘I’m ever so sorry, your ladyship.’` | 引语截到 `She froze…`，但导航「人物弧线」已写「会骂粗话、会失态道歉的一面」 | 不构成阻断 |
| L4 | `:146` 内心独白「He has been a cruel stranger to me from the first day of our marriage to the last.」 | 导航「人物弧线」写「她对休伯特的怒意没有转成原谅」 | 已覆盖，不构成漏 |

## 二、编（md 有、原文无）

**0 条。** 逐块核过导航 5 项、原句 1–7 的中文理解／关键词／为什么这样写／读者视角提示、词表 22 行、一句话总结，未发现凭空出现的情节、关系、数字或人物。

已重点排查并**排除**的两处疑点：

- 「莉莉被辞退」：md 导航「为什么这样写」写「第二句把莉莉、她被辞退这件事和乱作一团的仆役串起来」。
  取证：`/usr/bin/grep -n -w -E "Lily|lady’s maid" text/ch05_chapter_5.txt` → 命中 `:35`（唯一一处）；
  `/usr/bin/grep -n -w "Lily" text/ch01_chapter_1.txt` → 命中 `:56` `she told Cynthia Lily had been dismissed.`、`:59` `Lily was an excellent maid.`；退出码 0。
  ⇒ **成立**：被辞退的侍女即莉莉（ch16 `:65` 另称 `Lily had recently been a young maid in the household`），md 写法正确。
- 原句 1 中文理解「女仆已被辞退」：与原文 `the lady’s maid sacked` 一致。

## 三、错（两边都有但不一致）

| # | md 位置 | md 写法 | 原文（text 行号 + 逐字） | 判定 |
|---|---|---|---|---|
| E1 | 导航·情感弧线位置 | 「这是案发当天从下午延伸到深夜的一段**独处时光**。」 | `:56` `Clio and Thomas insisted on staying with her for the remainder of the afternoon.`（Clio 与托马斯整下午在场；希金斯太太亦在场至 `:110`） | **提示**（措辞级） |
| E2 | 原句 2·中文理解 | 「证明自己**不止是一块**果冻奶油挞」 | `:74` `before she could show him that she did, in fact, have more backbone than a jelly cream tart` | **提示**（措辞级） |
| E3 | 原句 4·中文理解 | 「火苗在她**姻亲**的掌心燃起」 | `:119` `she had seen fire flicker to life in her sister-in-law’s palm` —— 此处 sister-in-law 即当章坦白魔法的嫂子 Clio（`:59` Clio 解释魔法；`:119` `her sister-in-law’s palm`） | **提示**（指代不明） |

## 四、R4 逐块对应（三问）

| 原句 | 中文理解对应 | ①动词主语 | ②受事/宾语 | ③归属方向 | 结论 |
|---|---|---|---|---|---|
| 1 | 搜查 + 管家收拾 + 缺人手 | 警察搜、希金斯太太收拾、莉莉侍候、希金斯太太撑住家务 | 辛西娅的套房、毯子 | 「她被辞退」= 莉莉（已取证） | 对应成立 |
| 2 | 愤怒盖过悲伤 | 愤怒盖过震惊；休伯特把自己弄死 | 她没机会展示骨气 | 「他没把她放在眼里」= 休伯特 | 对应成立 |
| 3 | 管家失言 | 希金斯太太说、僵住 | 那只小狗摆件倒扣 | 「这事绝不是辛西娅干的」 | 对应成立 |
| 4 | 火与灯 | 她见过火与灯 | 辛西娅 | 「听见狐狸的声音」 | 对应成立 |
| 5 | 欲望 | 她曾有轻微悸动 | 海伦娜带来的牵引 | 「从未」 | 对应成立 |
| 6 | 证物与旧事 | 警司未收回证物；休伯特清晨回家；她扯下吊坠砸向他 | 吊坠 | 他嘲笑她的纯真 | 对应成立 |
| 7 | 宣言 | 她拒绝、享受坠落 | 她不是完美淑女/无辜新娘 | 「休伯特娶的」 | 对应成立 |

**R4 无阻断。** 未发现「分析讲的是引语之外的上下文」「讲全书主旨」「只复述字面」三类失配。

## 五、形态

`H1 = 05. Chapter Five`（形状合规）；导航 5 项；子项 4 项（中文理解／关键词／为什么这样写／读者视角提示）＝本书众数；块数 7，落在本书区间 [6,13] 与本章 `block_target=[4,7]` 内（**注意**：若因修复增块，7 已达上限，会触发 `block_count`）。
