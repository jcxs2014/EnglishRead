# ch11 · R3 对账（三张单子）

> 依据：`1-suread.json`（先素读，227 行全读，57 事件 / 10 关系 / 6 数字 / 5 未决 / 12 陷阱）与 `2-machine.json`（rc=0 / verdict ok / blocks=7 / words=2320 / block_target=[4,7] / segments=9）。
> 机器层：`segment_miss=0`（引语逐字）、`quote_long=0`、`keyword_bad=0`、`keyword_long=0`、`struct_bad=0`、`cjk_low=0`、`block_count=0`、`template=0`、`hole=0`、`empty_quote=0`。
> 补验（机器盲区）：本章 7 条引语中**有 2 条含 `…`**（原句 1、原句 6）⇒ R0 全书级 `verify_fragments_indep.py`（312 片段 / 0 MISS）已逐段独立取证通过；本章 22 行词表例句 **22/22 逐字回源命中**（`/tmp/vocab_check_hx.py`：`ch11: rows=22 missing=0`）、**22/22 词头落在例句内**（`/tmp/vocab_head_hx.py`，无输出＝零失配）；**引号配对**探针 `/tmp/pair4_hx.py` 全书扫描 ⇒ **本章 0 处偏离**（全书唯一 1 处在 ch09 原句 7）。

---

## 一、漏（素读有、md 无）

| # | 素读事实（text 行号 + 逐字） | md 状态 | 判定 |
|---|---|---|---|
| L1 | `:134` `A vase in the corner started to quiver. Cynthia sent Helena a warning glance. **One spilled glass was an accident, but if every vessel holding water in his office simultaneously tipped, that was a problem.**` —— 花瓶颤动（＝法术还在活动）＋辛西娅给海伦娜的警告眼神 ＋**「一杯水泼翻可以是意外」这句对冲** | md **未覆盖**；这段既是「海伦娜确实在用法术」的证据，也是**「水杯翻倒到底是不是意外」在原文里唯一的对冲** ⇒ E1（证据等级越级）缺的正是这条反证 | **不构成阻断**（非事件／转折）；但**必须与 E1 一并修**（见 §三 E1 的改法） |
| L2 | `:152` `‘Who else wanted Hubert dead?’` ＋ `:155` `He tsked, shaking his head slowly. ‘A man is only as powerful as ’is secrets.’` —— 辛西娅追问其他嫌疑人、辛克莱以「秘密即力量」拒答 | md **未覆盖**（导航只写「辛克莱否认杀人」，未写他**拒绝透露别人**） | **不构成阻断**（案件推进的支线，非本章主弧） |
| L3 | `:71` `‘We have no intention of offering help to you, Mr Sinclair. Whatever methods the Superintendent used to question you pale in comparison to **the violence you have committed**.’` —— 海伦娜当面把辛克莱称为「施加过暴力的人」（所指不明确：可指对休伯特，也可泛指此刻的威胁） | md **未覆盖** | **不构成阻断**；⚠️ **不得**据此把该句改写成「海伦娜指控辛克莱杀了休伯特」（原文所指不明） |
| L4 | `:158` `But the properties were entailed and her monthly income was generous, but not nearly large enough to accommodate the kind of payments she worried he would expect.`（房产**限定继承**，卖不掉）＋ `:164` `Finally, he opened his mouth and spoke an outrageous sum.`（**原文从未写出数额**）＋ `:179` `Even if she retained access to all of Hubert’s wealth – which she most certainly did not – she couldn’t have fulfilled such a debt.` | md 只在导航／总结里写「巨额债务」「债大到还不起」，未写**数字从未给出**、**地产不可卖**、**她多半已不能支配休伯特的财产** | **不构成阻断**（覆盖取舍）；**建议**在导航补一句「原文始终没有写出那个数目」——这是本章最重要的悬置点之一 |
| L5 | `:191` `And I like owning powerful men.` ＋ `:200` `With Hubert dead, he would own Cynthia instead. One more man dictating her choices. It was enough to make her contemplate drastic measures.` | md 导航·人物弧线只覆盖了辛克莱的「生意人算法」与「把威胁说成关心」，未收「**喜欢占有有权势的男人**」与「**辛西娅考虑激烈手段**」 | **不构成阻断**（人物刻画细部） |
| L6 | `:113` `‘Smith, a towel,’ he growled to the man who had escorted them through the gaming hell and upstairs.` ＋ `:212` `Probably have his burly butler chase after her.` | md **未提管家名为 Smith** | **不构成阻断**；⚠️ 记录在案：**Smith**（管家）与 ch13/ch14/ch17/ch20 的 **Governess Smithers**（恩师）是两个人，**不可混同** |

## 二、编（md 有、原文无）

**0 条。** 逐块核过导航 5 项、原句 1–7 的中文理解／关键词／为什么这样写／读者视角提示、词表 22 行、一句话总结，未发现凭空出现的情节、关系、数字或人物。

已重点排查并**排除**的四处疑点：

- **「她是我的」的方向**——`:89` `She is mine.` 是**辛西娅**对**海伦娜**的念头；ch09 `:245` `Mine.` 是**海伦娜**对**辛西娅**的。md 导航写「把刚冒出的『她是我的』咽了回去」⇒ 方向正确、未与 ch09 混用：**成立**。
- **「你早该切断他」归属海伦娜**——`:125` 辛西娅先说 `‘Bastard! You should have cut him off.’`，`:188` **海伦娜**接着说 `‘Cynthia is right. You should have cut him off.’` ⇒ md 导航·人物弧线把这句挂在海伦娜名下**成立**（不是张冠李戴）。
- **「现金奶牛」「杀欠债人等于自断财路」**——`:122` `Only a fool would kill a cash cow like ’ubert Burrows.` 与 `A wise businessman doesn’t eliminate an avenue of income without due cause.` ⇒ **成立**。
- **「紧接第 10 章办公室对峙」**——ch10 末句 `:272` `‘Did my husband’s debt to you play a role in his untimely death?’` → ch11 `:35` 辛克莱接 `‘I would be careful about ’oo you are accusing of a crime, Lady Burrows.’` ⇒ 跨章引用**成立**。
- **md 没有把 `:203` 式的原文笔误编成情节**（本章无此现象）；md 也**没有**把 `:65`「那道伤是警司留下的吗」写成既定事实 ⇒ **无编造**。

## 三、错（两边都有但不一致）

| # | md 位置 | md 写法 | 原文（text 行号 + 逐字） | 判定 |
|---|---|---|---|---|
| E1 | 导航·Tropes ＋ 原句 5·为什么这样写 ＋ 原句 5·读者视角提示 | 「『**水巫发威**』只用一只翻倒的杯子完成」／「最后才用『水巫』**点明动手的是谁**」／「**水不会自己翻**，屋里的人都看见了」 | `:107` `The glass of water tipped, spilling over the papers in front of him.` —— **被动句、无施事**；`:110` `His low curses were vicious, but Cynthia couldn’t stop the surge of pleasure as she glanced at Helena. **Her waterwitch didn’t take kindly to Sinclair’s bullying. Neither did she.**` —— 这是**辛西娅瞥了海伦娜一眼后读出的神色**，不是叙述者的指认；`:134` `**One spilled glass was an accident**, but if every vessel holding water in his office simultaneously tipped, that was a problem.` —— 原文**明确保留「意外」这一解释** | 原文**从未确认**施事是谁，md 把「暗示／嫌疑指向」写成了「点明」，并让读者以为全书已作定论 ⇒ **证据等级越级**（结论方向不误，措辞与叙事责任归属出错） | **提示**（叙事层措辞级，**本章第一优先修复项**：改 `点明动手的是谁` → `把嫌疑指向旁边那个人`；`:134` 一句须补入分析层或读者视角提示） |
| E2 | 导航·人物弧线 | 「辛克莱……**拿别人的亲人当软肋**，把威胁说成关心」 | `:80` `’ave a care, Miss Blair. It would be a shame to ’ear of any ’arm coming to your shop **or the women working there**.` —— 被威胁的对象是**店铺与店里的女工**；`:44`/`:53` 辛克莱挑衅的是**海伦娜的叔叔**（不是辛西娅的亲人）。原文**没有**「亲人」这一关系 | 「亲人」把「员工／工作场所」换成了「血亲」，且把辛克莱的两套手法（拿海伦娜身边的人开刀 ＋ 拿她的叔叔相激）并成了一种 | **提示**（措辞级） |

## 四、R4 逐块对应（三问）

| 原句 | 中文理解对应 | ①动词主语 | ②受事/宾语 | ③归属方向 | 结论 |
|---|---|---|---|---|---|
| 1 | 把催债信里的措辞递回去，追问给休伯特准备了哪种后果 | 海伦娜说 | 辛克莱信中的措辞 | 「后果」是**给休伯特**的后果 | 对应成立 |
| 2 | 念出「布莱尔小姐」，像解谜；点出警司的侄女姓布莱尔，骂他苏格兰混蛋 | 辛克莱说 | 海伦娜的姓 | 「像在解一道谜」＝他的动作神态 | 对应成立 |
| 3 | 声音像起火前的烟；药妆店最易失火，肥皂乳液挨着放；让她当心 | 辛克莱说 | 海伦娜的店与店里的女工 | 「威胁被拆进具体物件」＝他的手法 | 对应成立 |
| 4 | 念头不请自来、闭嘴、逼自己镇定；海伦娜不属于她 | 辛西娅自述 | 她自己（的动作与呼吸） | 「三层否定」＝她自己划的界 | 对应成立 |
| 5 | 他跳起身抢纸、墨水糊掉数字；她瞥向海伦娜时压不住痛快 | 辛克莱抢纸；辛西娅**瞥**向海伦娜 | 那几页写着数字的纸 | 「快意是从旁边那个人身上借来的」＝**辛西娅**的情绪 | 对应成立（但见 E1：原文未指认施事） |
| 6 | 把杀欠债人算成自断财路；休伯特是「现金奶牛」 | 辛克莱说 | 伦敦统治阶层与自己的钱柜 | 「现金奶牛」指的是**休伯特** | 对应成立 |
| 7 | 摄影在伦敦风靡；她想不出辛克莱要肖像做什么 | 叙述层＋辛西娅自问 | 照片与肖像 | 「除非他打算让照片变成丑闻」＝**辛西娅的推测**，原文未证实 | 对应成立 |

**R4 无阻断。** 未发现「分析讲的是引语之外的上下文」「讲全书主旨」「只复述字面」三类失配。

## 五、形态

`H1 = 11. Chapter Eleven`（形状合规）；导航 5 项；子项 4 项（中文理解／关键词／为什么这样写／读者视角提示）＝本书众数；块数 **7**，落在本书区间 [6,13] 与本章 `block_target=[4,7]` 内（**已触上限**：若因修复增块，会触发 `block_count`）。

### 引号配对（机器层零覆盖，自建探针）

`/tmp/pair4_hx.py` 全书扫描 27 章 ⇒ 全书 **TOTAL 1**（唯一一条在 ch09 原句 7）；**ch11 七个引语块全部配对完整**（含原句 2、原句 4、原句 6 这类从对白中途切起、但首尾引号成对的形态）⇒ **本章引号配对 0 偏离**。

## 六、语料层观察（非 md 缺陷，不计入三张单子）

本章**无**站点宣传行注入（全书 5 章 6 行：ch03:188 / ch08:170+173 / ch13:185 / ch19:197 / ch25:214，见 ch08 的 §六）。本章 7 条引语中 2 条含 `…`（原句 1、原句 6），省略号两侧均为原文，R0 全书级 `verify_fragments_indep.py` 已逐段独立取证（312 片段 / 0 MISS）。

### 跨章术语不一致（进汇总修复指令文件，**本章不改**）

| 词 | 本章写法 | 其他章节写法 | 处置 |
|---|---|---|---|
| apothecary | 药妆店（导航×2 ＋ 原句 3 中文理解） | ch06 词表作「药草店；药剂师」；ch06 例句 `Her apothecary was now the city’s premier beauty shop.` 说明该店实为**美容／药妆**性质 ⇒ 本章写法与店铺性质相合 | 列入汇总，二选一后全书统一 |
| Kentmore | 肯特莫尔侯爵（导航、原句 1） | ch10 与 `00_概述` 作「肯特米尔」 | 列入汇总（多数派＝肯特莫尔） |
