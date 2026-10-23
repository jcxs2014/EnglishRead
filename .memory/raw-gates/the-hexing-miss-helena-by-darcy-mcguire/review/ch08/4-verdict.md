# 4-verdict.md · 《The Hexing Miss Helena》ch08 审查判定（深审 R0–R5）

审查员：主会话自审（**同会话盲区见文末**）｜章型：审讯推进章＋婚姻回溯章＋内心独白章｜档位：**深审**（2026-10-23 用户指令）
底稿：`1-suread.json`（R1 先素读，43 事件 / 11 关系 / 7 数字 / 7 未决 / 10 陷阱）→ `2-machine.json`（R2）→ `3-diff.md`（R3）→ 本表（R4 逐块 ＋ R5）
源：`text/ch08_chapter_8.txt`（314 行）｜受审：`ch08 the devil of seven dials.md`（8 块 / 词表 22 条）

---

## 一、四组计数

| 组 | 计数 | 明细 |
|---|---|---|
| **逐字** | **引语 8 / 8 相符，0 错** | `2-machine.json`：`segment_miss=0`、`quote_long=0`、`keyword_bad=0`、`keyword_long=0`、`hole=0`；R0 全书级 `verify_fragments_indep.py`：**312 片段 / 0 MISS**（本章 8 条引语**均无 `…`**，逐条独立取证通过）；词表 **22 / 22** 例句逐字回源命中（`## 本章词汇` 不在 `check_vocab.py` 默认扫描域，本轮自建 `/tmp/vocab_check_hx.py` 补验）、**22 / 22** 词头落在例句内（`/tmp/vocab_head_hx.py`） |
| **对应** | **8 块：8 块对应成立，0 越界** | R4 三问（动词主语／受事／归属方向）逐块核对，见 `3-diff.md` §四；密度不足 0 处；未发现「分析讲的是引语之外的上下文」「讲全书主旨」「只复述字面」三类失配 |
| **形态** | **4 / 4 符合，0 偏离** | H1 `# 08. Chapter Eight` ✓｜导航 **5 项** ✓｜子项 **中文理解／关键词／为什么这样写／读者视角提示** 4 项一致 ✓｜块数 **8** ∈ 本书区间 **6–13** ✓，亦 ∈ 本章 `block_target:[5,8]` ✓（**已触上限**）；`block_count=0`、`struct_bad=0`、`cjk_low=0`、`template=0` |
| **断言** | **共核 22 条：相符 20 ／ 提示 2 ／ 阻断 0 ／ 跳过 0** | 提示 2 条（E1 同义反复、E2 概括过头「都」）；**阻断型条数 = 0** |

**本章无阻断型缺陷。**

---

## 二、判定表（断言 | 证据 | 结论 | 档位）

| # | 断言 | 证据（`text/ch08_chapter_8.txt:行`） | 结论 | 档位 |
|---|---|---|---|---|
| E1 | 原句 2·读者视角提示：「读者得到一条规则：情绪越强，念头越容易被听见。**读心因此要看对方情绪，情绪越强越容易**；」 | `:53` `‘He was frightened. Strong emotions can make it easier. “The Devil’s going to kill me for sure if I fail.” That’s what he thought before he escaped.’` | 前后两个分句**说的是同一件事**（后半句＝前半句换词重述），同一命题连说两遍，读者视角提示的信息量折半 | **提示**（措辞级） |
| E2 | 导航·一句话概括：「认定七晷区**的人都替他办事**」 | `:56` `‘The bastard. It has to be Sinclair. He has every man in the Seven Dials working for him, and half the women as well.’` | 原文是**每个男人**替他办事、**一半的女人**才替他办事；「都」把一半女人也括进去，概括过头。md 同章原句 3·中文理解写的是「每个男人都替他做事，连一半女人也听他差遣」，比导航准确 ⇒ md 内部不一致 | **提示**（措辞级） |

### 与原文相符的 20 条断言（避免「只报问题」的不完整交代）

1. 警司从信上认出「七晷区的魔鬼」达米安·辛克莱，且是**把话当毒吐出来**——`:41` `‘The Devil of Seven Dials. Damien Sinclair.’ He spat the words like poison.` ✓
2. 辛西娅的第一反应是手指发冷、差点把羊皮纸掉了——`:35` `Cynthia’s fingers grew cold. … She nearly dropped the parchment …` ✓（词表 `parchment` 例句逐字同源）
3. 七晷区的人替辛克莱办事（每个男人＋一半女人）——`:56` ✓
4. 警司说辛克莱「杀的人比瘟疫还多」——`:62` `‘A very dangerous man. He’s killed more people than the plague.’` ✓
5. 「海伦娜脸红」＝从奶油色到草莓色——`:65` `Did she imagine the slight flush turning Helena’s skin from cream to strawberries?` ✓
6. 警司手指不停地敲大腿（`incessantly`）——`:71` `Superintendent MacDougal’s finger tapped incessantly against his thigh.` ✓
7. 辛西娅对警司的说法是「陪审式」的：她以「亲爱的」婚姻同行作掩护，但从不追问丈夫的债务——`:74` `‘… it was usually about whether or not there would be roast beef on the menu. It’s been months since we’ve exchanged more than a passing greeting. He certainly wouldn’t deign to share his private schedule or any chums he might have in London’s criminal underworld.’` ✓
8. 婚姻十年回溯确实**插在警司两句问话之间**（`:71` 问「确定他从没提过这个人吗？」→ 回溯 `:74`–`:110` → `:104` 再问「你总该记得他的来往客人」）——✓
9. 丈夫对妻子的三项要求＝漂亮、顺从、能生育；末项未达标，前两项不达标即被休——`:92` `Her job was to be beautiful, obedient, and fertile. She failed in the last aspect, and if she did not excel in the first two obligations, he would divorce her.` ✓
10. 「被休掉比死还难受」是**上流社会太太**的处境，不是个人的说法——`:92` `It was a fate worse than death for any lady of the beau monde.` ✓
11. 她走出书房后「以堪称典范的成功」多年避开丈夫的路——`:95` `Which she had done with exemplary success for years.` ✓
12. 「冷、残酷、闪亮的笼子」是**她自己的定语**（她不愿警司转告哥哥）——`:110` `she certainly didn’t want him running off to tell her brother that Cynthia’s marriage had been a cold, cruel, glittering cage.` ✓
13. 狐狸的话与她自己的念头**同版式排布**，须靠「谢谢／不是在向狐狸道谢」分辨——`:131` `You are a fox. You can’t be talking to me.` … `:137` `I’m a fox. I can do whatever I please.` … `:149` `Thank you. Wait. No. I am not thanking a fox. …` ✓
14. 狐狸自称「很少见，连法力惊人的罗恩都做不到」——`:152` `No. Just very rare. Few earthwitches can communicate with animals. Not even Rowan with her impressive powers.` ✓（`earthwitch`＝土系女巫，md 原文引语保留原词 ✓）
15. 她把话拉回案子、避免在海伦娜面前继续示弱——`:224` `She needed to pull the focus away from her broken marriage and bring it back to the case.` ✓
16. 她坚持「没有更多证据就不能给这个魔鬼定罪」，并主动补上对自己不利的「出于怨恨或愤怒」——`:233` ✓
17. 海伦娜的质问与她的正面回答（「是的。我就是。」）——`:236`、`:242` ✓
18. 「Because she sees me. Not the marchioness. …」是**辛西娅的顿悟**（无引号内心句）——`:257` ✓
19. 警司最后的裁决带保留：「你不是嫌疑人——至少我们不这么认为」——`:296` `‘Well, then. I suppose tha’s our answer. You are no’ a suspect, Lady Burrows. At least, we don’t think so.’` ✓
20. 章末＝一次沉默（`Nothing. Not even a blink.`）＋一句短念（`Damnation. The fox is right.`）——`:308`、`:314` ✓

---

## 三、已核实为正确（防误修，下一轮不得以「读着不对」为由改动）

1. **「海伦娜读不到辛西娅」在 md 里被写成「辛西娅的判断」而非叙述者认证的事实**（原句 8·为什么这样写）——`:311` `Helena might be here to detect Cynthia’s hidden thoughts, but she was the witch with a secret. Perhaps she could read other people’s minds, but she couldn’t detect a thing going on in Cynthia’s head.` 与 `:314` 同为**无引号内心独白**：**成立**，不得改写成「叙述者确认海伦娜读不到」。
2. **「魔鬼」这个名字的来源是闯入者临逃前的念头**（原句 2·为什么这样写）——`:47` `‘Devil. That’s what the intruder thought before he jumped out of the window.’` ＋ `:53` 的转述：**成立**。
3. **「他确信的是辛克莱知情，不是辛克莱下手」**（原句 7·读者视角提示）——`:260` `He might no’ have killed your husband, but I’ll bet all the whisky in Scotland he knows who did it.`：**成立**（引语本身已明写 `might no’`）。
4. **「警司的『一定是』只是判断，不是物证」**（原句 3·为什么这样写）——`:56` `It has to be Sinclair.` 与 `:60` 前后无任何物证；`:227` `tha’ bastard has risen to the top of our suspect list`：**成立**。
5. **「冷、残酷、闪亮的笼子」三个词的中文对应**——`:110` `cold, cruel, glittering cage` ⇒ 冷／残酷／闪亮：**成立**（「笼子」是译者补的比喻词，原文有 `cage`）。
6. **「婚内只有一项功能」的转述**——`:89` `It took Hubert no time at all to make it absolutely clear women held one function in his life.`：原句 4 的「差事」比喻有原文依据：**成立**。
7. **「七晷区」＝ Seven Dials**——`:56` `every man in the Seven Dials`：**成立**（全书统一，无冲突）。
8. **「达米安·辛克莱」＝ Damien Sinclair**——`:41`：**成立**（勿改音译）。
9. **词表 22 条例句全部逐字取自本章**——**成立，不得改写例句**（22/22 逐字回源命中、22/22 词头在例句内）。
10. **原句 5 引语的选段**——md 引语取 `:149` 全句（狐狸与她的念头交织的一整段），**中间未用省略号跳过任何内容**：**成立**，不得「整理」成两段。
11. **原句 3 引语止于 `half the women as well.`**——`:56` 该句在此处断开，md 未越界拼接：**成立**。
12. **「海伦娜是警司的侄女」**——`:65` `‘I suppose that is a question for your niece. She’s the one adept at reading minds.’` ＋ `:293` `She looked away from her uncle.`：**成立**。

---

## 四、覆盖声明与已知盲区

- **本章覆盖**：R1 素读（先于任何 md 打开，43 事件 / 11 关系 / 7 数字 / 7 未决 / 10 陷阱）→ R2 机器层 → R3 三张单子 → R4 逐块 8/8 → R5 判定表，**全流程走完**。
- **本书覆盖（深审进度）**：批 1 = ch02 / ch03 / ch04，批 2 = ch05 / ch06 / ch07，批 3 = ch08（本表）⇒ **7 / 27 章**已完成 R0–R5（ch08 为第 7 章）。ch01 与其余 20 章**只有机器层**（R0 全书级已跑），**未做人判**，不得写成「已审查」。
- **同会话盲区（如实标注）**：本书由本会话在写作期产出，本章亦为写作期读过的章之一；本次仍执行「先素读、写完 `1-suread.json` 才开 md」，但**不能视为完全盲态**。
- **本章特有盲区**：
  - L1（肯特摩尔侯爵／侯爵夫人身份未进 md）被本轮判为「不构成阻断」，理由是 md 谈的是婚姻关系本身、不涉封号；**该判据是本会话自定**——若后续主张「原句 8 的『不是侯爵夫人，是她自己』这一反转必须在 md 里可见」，L1 应升为提示项，须由执行方拍板后再改。
  - E1（同一命题连说两遍）判为**提示**而非**阻断**：属读者视角提示的表述冗余，不改变任何断言的真伪。
- **未做**：五步审查附录 B（a–e 全文）已被 `审查表.md` 归档取代，不重复执行。
