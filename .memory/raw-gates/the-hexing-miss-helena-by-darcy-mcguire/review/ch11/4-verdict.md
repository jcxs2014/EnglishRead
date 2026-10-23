# 4-verdict.md · 《The Hexing Miss Helena》ch11 审查判定（深审 R0–R5）

审查员：主会话自审（**同会话盲区见文末**）｜章型：审讯推进章＋威胁对峙章＋内心转折章｜档位：**深审**（2026-10-23 用户指令「继续执行深审 R0–R5 全章」）
底稿：`1-suread.json`（R1 先素读，227 行全读，57 事件 / 10 关系 / 6 数字 / 5 未决 / 12 陷阱）→ `2-machine.json`（R2）→ `3-diff.md`（R3）→ 本表（R4 逐块 ＋ R5）
源：`text/ch11_chapter_11.txt`（227 行）｜受审：`ch11 the devils price.md`（7 块 / 词表 22 条）

---

## 一、四组计数

| 组 | 计数 | 明细 |
|---|---|---|
| **逐字** | **引语 7 / 7 相符，0 错** | `2-machine.json`：`segment_miss=0`、`quote_long=0`、`keyword_bad=0`、`keyword_long=0`、`hole=0`、`empty_quote=0`；R0 全书级 `verify_fragments_indep.py`：**312 片段 / 0 MISS**（本章 7 条引语中 **2 条含 `…`**——原句 1、原句 6——已逐段独立取证通过）；词表 **22 / 22** 例句逐字回源命中（`/tmp/vocab_check_hx.py` → `ch11: rows=22 missing=0`；`## 本章词汇` 不在 `check_vocab.py` 默认扫描域，本轮自建补验）、**22 / 22** 词头落在例句内（`/tmp/vocab_head_hx.py`，无输出＝零失配） |
| **对应** | **7 块：7 块对应成立，0 越界** | R4 三问（动词主语／受事／归属方向）逐块核对，见 `3-diff.md` §四；密度不足 0 处；未发现「分析讲的是引语之外的上下文」「讲全书主旨」「只复述字面」三类失配 |
| **形态** | **5 / 5 符合，0 偏离** | H1 `# 11. Chapter Eleven` ✓｜导航 **5 项** ✓｜子项 **中文理解／关键词／为什么这样写／读者视角提示** 4 项一致 ✓｜块数 **7** ∈ 本书区间 **6–13** ✓，亦 ∈ 本章 `block_target:[4,7]` ✓（**已触上限**：因修复而增块会触发 `block_count`）；`block_count=0`、`struct_bad=0`、`cjk_low=0`、`template=0`；**引号配对 0 偏离**（`/tmp/pair4_hx.py` 全书扫描 ⇒ 全书 TOTAL 1，唯一一处落在 ch09 原句 7） |
| **断言** | **共核 24 条：相符 22 ／ 提示 2 ／ 阻断 0 ／ 跳过 0** | 提示 2 条（E1 证据等级越级、E2 措辞级「亲人」）；**阻断型条数 = 0** |

**本章无阻断型缺陷。** 两条提示均属**叙事层措辞级**，不改事实、不改归属方向，修复不涉引语层、不涉词表层。

---

## 二、判定表（断言 | 证据 | 结论 | 档位）

| # | 断言 | 证据（`text/ch11_chapter_11.txt:行`） | 结论 | 档位 |
|---|---|---|---|---|
| E1 | 导航·Tropes：「『**水巫发威**』只用一只翻倒的杯子完成」；原句 5·为什么这样写：「最后才用『水巫』**点明动手的是谁**」；原句 5·读者视角提示：「**水不会自己翻**，屋里的人都看见了」 | `:107` `The glass of water tipped, spilling over the papers in front of him.` —— **被动句、无施事**；`:110` `His low curses were vicious, but Cynthia couldn’t stop the surge of pleasure as she glanced at Helena. Her waterwitch didn’t take kindly to Sinclair’s bullying. Neither did she.` —— 这是**辛西娅瞥了海伦娜一眼后读出的神色**，叙述者从未指认施事；`:134` `One spilled glass was an accident, but if every vessel holding water in his office simultaneously tipped, that was a problem.` —— 原文**明确保留「意外」这一解释** | 原文**从未确认**是谁打翻了水杯；md 把「暗示／嫌疑指向」写成了「点明」，并让读者以为全书已作定论 ⇒ **证据等级越级**（结论方向不误，措辞与叙事责任归属出错）。**本章第一优先修复项**：改 `点明动手的是谁` → `把嫌疑指向旁边那个人`；`:134` 这句对冲须补入分析层或读者视角提示 | **提示**（措辞级） |
| E2 | 导航·人物弧线：「辛克莱始终按生意人的算法行事：不杀那头会不断生钱的『现金奶牛』，**拿别人的亲人当软肋**，把威胁说成关心」 | `:80` `’ave a care, Miss Blair. It would be a shame to ’ear of any ’arm coming to your shop **or the women working there**.` —— 被威胁的对象是**店铺与店里的女工**；`:44` `There’s a superintendent at Scotland Yard ’as nieces with the name of Blair. Lachlan MacDougal.`／`:53` `’auled me down to Newgate…` —— 辛克莱挑衅的是**海伦娜的叔叔**。原文**没有**「亲人」这一关系 | 「亲人」把「员工／工作场所」换成了「血亲」，并把辛克莱的两套手法（拿海伦娜身边的人开刀 ＋ 拿她的叔叔相激）并成了一种 ⇒ 归属方向错位 | **提示**（措辞级） |

### 与原文相符的 22 条断言（避免「只报问题」的不完整交代）

1. 海伦娜拿辛克莱自己的催债信逼他交代「后果」——`:41` `‘You sent a note reminding the Marquess of Kentmore that he was overdue in paying his debt. What was the phrase you used… “breaking a deal with the Devil carries profound consequences”, I believe… So, I wonder, what kind of consequences did you have in mind for Hubert?’` ✓
2. 原句 2 的「像解一道谜」是辛克莱玩味她名字的神态动作——`:44` `He paused, contemplating her name like a puzzle.` ✓
3. 辛克莱点破「警司的侄女」：苏格兰场有位警司，侄女姓布莱尔，拉克兰·麦克杜格尔——`:44` ✓
4. 「脑袋比两块木板还厚的苏格兰混蛋」——`:44` `A Scottish bastard with an ’ead thicker than two planks.` ✓
5. 原句 3 的威胁被拆进具体物件：一排排肥皂、乳液——`:80` `So many flammable products all sitting next to each other in neat little rows of soaps and lotions.` ✓
6. 威胁连店里的女工也算进去——`:80` `or the women working there` ✓
7. 原句 4「念头不请自来／闭嘴／用鼻子呼吸」——`:89` `She is mine.` ＋ `:92` `The thought came unbidden and she snapped her mouth shut before it could escape. Breathing through her nose, she forced herself to calm.` ✓
8. 原句 4 的「三层否定」——`:92` `Helena did not belong to her. The enigmatic woman would never belong to anyone but herself.` ✓
9. 原句 5「抢纸跳身、墨水糊成不可辨的污斑」——`:110` `He snatched the parchment and leapt to his feet… Ink blurred across the pages he shook, turning neat rows of numbers into indecipherable blotches.` ✓
10. 原句 5「快意是从旁边那个人身上借来的」＝辛西娅的情绪、不是她的施法——`:110` `Cynthia couldn’t stop the surge of pleasure **as she glanced at Helena**` ✓
11. 原句 6「杀光欠债人＝伦敦统治阶层被清空、自己的钱柜也一样」——`:122` `London’s ruling class would be culled, as would me coffers.` ✓
12. 原句 6「明智的生意人不会无缘无故砍掉一条进项」＋休伯特是「很赚钱的进项」——`:122` `A wise businessman doesn’t eliminate an avenue of income without due cause. And your ’usband was a very lucrative avenue of income.` ✓
13. 「现金奶牛」指休伯特——`:122` `Only a fool would kill a cash cow like ’ubert Burrows.` ✓
14. 原句 7「摄影在伦敦正当红、照相馆开遍街角」——`:221` `Photographs were all the rage in London, with studios cropping up on every corner.` ✓
15. 原句 7「除非他打算让照片变成丑闻」是辛西娅的推测、原文未证实——`:221` `But what the devil would Sinclair do with portraits of Cynthia and Helena? Unless he planned for them to be scandalous.` ✓
16. 导航·人物弧线「辛克莱按生意人的算法行事：不杀那头会不断生钱的现金奶牛」——`:122` ✓（同 13）
17. 导航·人物弧线「辛西娅第一次让占有欲冒头又立刻纠正」——`:89`（未出口的 `She is mine.`）＋ `:92`（随即否认）✓
18. 导航·人物弧线「第一次意识到丈夫的债要她一个人扛」——`:158` `If you inform me of the sum, I will make arrangements.` ＋ `:179` `Even if she retained access to all of Hubert’s wealth – which she most certainly did not – she couldn’t have fulfilled such a debt.` ✓
19. 导航·叙事手法「全章贴辛西娅的限知」——`:35`–`:227` 通篇为辛西娅所见所感，海伦娜与辛克莱的话皆为带引号对白 ✓
20. 导航·一句话总结「他最后不要钱，只要她和海伦娜的照片」——`:215` `‘I want pictures. Of you. And ’er.’` ✓
21. 导航·Tropes「黑帮头目坐镇赌场」——`:104` `you should never ’ave brought her into my kingdom` ＋ ch10 `:133` `As the owner of a gambling hell` ✓
22. 导航·一句话总结「辛克莱反手点破她是警司麦克杜格尔的侄女、又拿药妆店起火相胁」——`:44` ＋ `:80` ✓

---

## 三、已核实为正确（防误修，下一轮不得以「读着不对」为由改动）

1. **「她是我的」是辛西娅对海伦娜的未出口念头，方向与 ch09 相反**——ch11 `:89` `She is mine.`（辛西娅 → 海伦娜）；ch09 `:245` `Mine.`（海伦娜 → 辛西娅）。md 导航写「把刚冒出的『她是我的』咽了回去」⇒ **方向正确、未与 ch09 混用**，成立。
2. **原句 4 的引语**刻意不含 `She is mine.` ——md 的中文理解写「一个念头不请自来，她赶在它出口之前闭上嘴」，并明说「这一段不重述念头的内容」⇒ **成立**，不得「补全」引语。
3. **「你早该切断他」归属海伦娜**——`:125` 辛西娅先说 `‘Bastard! You should have cut him off.’`，`:188` **海伦娜**接着说 `‘Cynthia is right. You should have cut him off.’` ⇒ md 导航·人物弧线把它挂在海伦娜名下**成立**（不是张冠李戴）。
4. **「现金奶牛」「杀欠债人等于自断财路」**——`:122` 逐字 ⇒ 成立。
5. **「紧接第 10 章办公室对峙」的跨章引用成立**——ch10 `:272` `‘Did my husband’s debt to you play a role in his untimely death?’` → ch11 `:35` 辛克莱接 `‘I would be careful about ’oo you are accusing of a crime, Lady Burrows.’` ⇒ 连续对白，成立。
6. **债务数额原文从未写出**——`:164` `Finally, he opened his mouth and spoke an outrageous sum.` ⇒ md 只写「巨额债务」「债大到还不起」而未给数字，**成立**，不得回填数字。
7. **「她多半已不能支配休伯特的财产」是原文措辞**——`:179` `which she most certainly did not` ⇒ md 未写成「她已经一无所有」，成立。
8. **房产限定继承**——`:158` `But the properties were entailed` ⇒ 她卖不掉地产是制度原因，成立。
9. **管家名为 Smith**，与 ch13/ch14/ch17/ch20 的 **Governess Smithers** 是两个人，**不可混同**——`:113` `‘Smith, a towel,’` ⇒ 成立。
10. **`:71`「the violence you have committed」所指不明**——md 未把它改写成「海伦娜指控辛克莱杀了休伯特」，成立；**不得**在修复时加入该指认。
11. **`:65` 嘴角的愈合伤口无人证实**——md 原句 3 未把「那道伤是警司留下的吗」写成既定事实，成立。
12. **`:140` `brown bread` ＝ 一堆面包 ＝ 死（伦敦俚语）**，不是真的面包——成立。
13. **`carte de visite` 原文拼作带 e**，须逐字照抄（`:221`）——成立，不得改写为 `carte-de-visite` 或 `carte de visite` 的其他变体。
14. **原句 6 引语中的 `…`** ——`:122` 原文即以 `… Only a fool would kill a cash cow like ’ubert Burrows.’` 断开，md 未越界拼接；R0 全书级 `verify_fragments_indep.py` 已逐段取证（312 片段 / 0 MISS）。
15. **词表 22 条例句全部逐字取自本章**，**不得改写例句**——22/22 逐字回源命中、22/22 词头在例句内。
16. **词表分隔行 `|------|`** ——本章用 `|------|------|------|------|`，与 ch03/04/06/10–16 一致；GFM 合法，**不判缺陷**（ch01/02/05/07/08/09/11 中 17 章用 `|---|---|---|`，两种均为合法 GFM 表格）。

---

## 四、覆盖声明与已知盲区

- **本章覆盖**：R1 素读（先于任何 md 打开，57 事件 / 10 关系 / 6 数字 / 5 未决 / 12 陷阱）→ R2 机器层 → R3 三张单子 → R4 逐块 7/7 → R5 判定表，**全流程走完**。
- **本书覆盖（深审进度）**：批 1 = ch02 / ch03 / ch04，批 2 = ch05 / ch06 / ch07，批 3 = ch08 / ch09 / ch10，批 4 = ch11（本表）⇒ **10 / 27 章**已完成 R0–R5（ch11 为第 10 章）。ch01 与其余 17 章**只有机器层**（R0 全书级已跑），**未做人判**，不得写成「已审查」。
- **同会话盲区（如实标注）**：本书由本会话在写作期产出，本章亦为写作期读过的章之一；本次仍执行「先素读、写完 `1-suread.json` 才开 md」，但**不能视为完全盲态**。
- **本章特有盲区**：
  - E1 判为**提示**而非**阻断**：结论方向（是海伦娜一方动的手）与读者获得的印象不错，且改法为措辞级 ＋ 补一句 `:134`；但若执行方认为「把暗示写成点明」已触及叙事责任归属的越级，**其修复集合完全相同**（改 `点明动手的是谁` ＋ 补 `:134`），档位归属不影响改法。
  - E2 的判据是「原文未出现血亲关系」这一可核事实（`:80` /`:44` /`:53`）；已同时核对全书，`kinship` 类表述在本章**只**出现在 `:101` `whatever nightmare Hubert had dragged Cynthia into` 与 `:53` 的 uncle 场景，均非「拿辛西娅的亲人当软肋」⇒ 判据不外溢。
  - L1–L6 六条「漏」全部不构成阻断（L1 为 E1 的配套证据，已在 E1 改法中吸收）；其中 L4（债务数额从未写出、地产限定继承、财产多半不可支配）虽属重要悬置点，但 md 现有写法未与之矛盾 ⇒ 判为覆盖取舍而非错写。
- **未做**：五步审查附录 B（a–e 全文）已被 `审查表.md` 归档取代，不重复执行。
