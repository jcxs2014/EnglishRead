# 4-verdict.md · 《The Hexing Miss Helena》ch07 审查判定（深审 R0–R5）

审查员：主会话自审（**同会话盲区见文末**）｜章型：审问场景＋动作场面＋视角切换章｜档位：**深审**（2026-10-23 用户指令）
底稿：`1-suread.json`（R1 先素读，89 事件 / 15 关系 / 7 数字 / 8 未决 / 18 陷阱）→ `2-machine.json`（R2）→ `3-diff.md`（R3）→ 本表（R4 逐块 ＋ R5）
源：`text/ch07_chapter_7.txt`（397 行）｜受审：`ch07 the locket opens.md`（10 块 / 词表 22 条）

---

## 一、四组计数

| 组 | 计数 | 明细 |
|---|---|---|
| **逐字** | **引语 10 / 10 相符，0 错** | `2-machine.json`：`segment_miss=0`、`quote_long=0`、`keyword_bad=0`、`keyword_long=0`、`hole=0`；R0 全书级 `verify_fragments_indep.py`：**312 片段 / 0 MISS**（本章含 `…` 的原句 8 逐段独立取证通过）；词表 **22 / 22** 例句逐字回源命中（`## 本章词汇` 不在 `check_vocab.py` 默认扫描域，本轮自建 `/tmp/vocab_check_hx.py` 补验）、**22 / 22** 词头落在例句内（`/tmp/vocab_head_hx.py`） |
| **对应** | **10 块：10 块对应成立，0 越界** | R4 三问（动词主语／受事／归属方向）逐块核对，见 `3-diff.md` §四；密度不足 0 处；未发现「分析讲的是引语之外的上下文」「讲全书主旨」「只复述字面」三类失配 |
| **形态** | **4 / 4 符合，0 偏离** | H1 `# 07. Chapter Seven` ✓｜导航 **5 项** ✓｜子项 **中文理解／关键词／为什么这样写／读者视角提示** 4 项一致 ✓｜块数 **10** ∈ 本书区间 **6–13** ✓（众数位），亦 ∈ 本章 `block_target:[6,10]` ✓（**已触上限**）；`block_count=0`、`struct_bad=0`、`cjk_low=0`、`template=0` |
| **断言** | **共核 20 条：相符 16 ／ 提示 4 ／ 阻断 0 ／ 跳过 0** | 提示 4 条（E1 措辞自相矛盾、E2 无据「撬保险箱」、E3 归属方向错、E4 指代含混）；**阻断型条数 = 0** |

**本章无阻断型缺陷。**

---

## 二、判定表（断言 | 证据 | 结论 | 档位）

| # | 断言 | 证据（`text/ch07_chapter_7.txt:行`） | 结论 | 档位 |
|---|---|---|---|---|
| E1 | 导航·Tropes：「海伦娜的水魔法**制住了**贼，却把他送出墙外」 | `:176` `She pooled her powers, throwing a blast of water that tumbled the boy across the manicured lawn, inadvertently aiding his escape. He recovered his feet and dove through the hedges before she could lobby a second attack.` | 她**没有制住**他，这一击反而帮他逃出；「制住了」与同句「送出墙外」自相矛盾；md 同章「一句话概括」写的是「反倒帮他逃走」，与原文一致 | **提示**（措辞级，md 内部不一致） |
| E2 | 导航·一句话概括：「三人上三楼撞见**正在撬保险箱**的窃贼」 | `:158` `He was holding a painting he’d just removed from the wall. Behind the painting was the steel glint of Hubert’s safe.`；`:185` `she turned from the window to assess whether the thief had managed to open the safe.` | 他刚**取下画作**，保险箱**尚未打开**（`:185` 还在确认是否被打开） | **提示**（措辞级） |
| E3 | 导航·Tropes：「辛西娅主动把开保险箱的责任揽到自己身上，等于**替海伦娜**挡了一次怀疑」 | `:363` `‘It was my idea.’ Cynthia didn’t need to give Helena another reason to mistrust her.` | 她抢责是**为自己**（不给海伦娜多一个怀疑她的理由），**受益方不是海伦娜** | **提示**（归属方向错） |
| E4 | 原句 10·为什么这样写：「信里**把对方称作魔鬼**」 | `:396` `The deadline has passed. Fulfil your bargain or pay your debt in full. Breaking a deal with the Devil carries profound consequences.` | 信中的「你」＝收信人，**魔鬼是收信人所交易的对象**；中文「对方」最自然读成「收信人」，会被读成「收信人＝魔鬼」 | **提示**（指代含混） |

### 与原文相符的 16 条断言（避免「只报问题」的不完整交代）

1. 承认异能「本质上觉得不对」＋自幼三条不可打破的规则（不显露力量／不信任／不爱）——`:35`、`:38–47` ✓
2. 破戒后被「榛色眼睛像暗森林」「香草与忍冬像爱情咒」击溃理智——`:50` ✓
3. 童年：从家里逃出、跑离母亲、血顺手臂滴下；母亲「变成别的东西——可怕而扭曲」——`:56` ✓
4. 童年：罗恩姨妈家是十五分钟路程、跑五分钟就到，**到时姨妈不在**——`:56`、`:59` ✓
5. 童年：从空气中抽水、踩着一条水河奔跑、水河如雾消失；坎贝尔太太接住她、问「你在流血，小姑娘」——`:62`、`:65` ✓
6. 童年：在纯粹的慌乱中把一切告诉坎贝尔太太，「在倾诉中毁掉自己的整个世界」——`:68` ✓
7. 回来后拒绝怜悯（「最不需要的是可能面对绞刑的女人的怜悯」）＋「如果你藏了什么秘密，你的念头会出卖你」——`:74` ✓
8. 辛西娅从裙褶取出吊坠、承认昨天撒谎；海伦娜一向知道谁在说谎「直到现在」——`:89`、`:92–95` ✓
9. 吊坠打开＝两张微型小像；对面不是辛西娅；十多年前她的脸在他对面——`:107–125` ✓
10. 辛西娅不认得那个女人；「我知道我丈夫拈花惹草」；海伦娜怒其冷酷、称此举「存心的残忍」——`:131`、`:134` ✓
11. 三楼走廊末幅油画＝婚后不久委托；窃贼取下画作、画后是保险箱的钢光；男仆被绑在地板上——`:146`、`:158` ✓
12. 海伦娜的水浪把贼掀过修剪整齐的草坪、「无意中帮了他的忙」、他钻进树篱逃脱——`:176` ✓
13. 保险箱内＝账本、散纸、珠宝盒、上漆珐琅盒；DOSD 反复出现、欠款巨大；辛西娅「即便能证明清白也已算是毁了」；Newgate 负责她的食宿直到被绞死——`:242`、`:291`、`:303`、`:321` ✓
14. 「有罪的人能做出无穷无尽的背叛」与「那正好，我不是有罪」；两人近得能数清鼻梁上的肉桂色雀斑——`:251`、`:254` ✓
15. 「你。就是你让我害怕」；触碰＝电流、像焦糖和盐；猛然想起海伦娜能读心、自己的念头已被听去——`:257`、`:333`、`:336`、`:342` ✓
16. 「能证明辛西娅无罪的证据」＝海伦娜第一次叫她的名字；羊皮纸三句＝期限已过／履约或全额还债／与魔鬼毁约的后果——`:378`、`:396` ✓

---

## 三、已核实为正确（防误修，下一轮不得以「读着不对」为由改动）

1. **「吊坠不是爱情的证物，而是丈夫转送情妇的旧物」**（导航·Tropes 反转）——`:113` `‘This is not my necklace.’ … ‘At least, not any more.’`、`:125` `When he gave me that locket, more than ten years ago, my face was opposite his.`、`:134` `To take a gift he’d given her in their courtship to a mistress was wilfully cruel.`：**成立**。
2. **「贼在心里怕『魔鬼』要他的命，信上又出现『魔鬼』，两处前后呼应」**（导航·叙事手法）——`:164` `Fucking hell! The Devil’s going to kill me for sure if I come back without it.` 与 `:396` `Breaking a deal with the Devil carries profound consequences.`：**成立**（且「本章都没有点名」亦成立）。
3. **「DOSD 是反复出现的字母组合」**（原句 8）——`:291` `A curious combination of letters was repeated often. DOSD.`：**成立**，不得改写成机构名或人名。
4. **「Newgate＝监狱」**（词表 `noose` 一行）——`:321` `Newgate will be in charge of my room and board until I hang for murder.`：**成立**（不得译作「新城门」）。
5. **「爆炸出的一把火药……」式比喻**——原句 9 的「电的意象」——`:333` `letting the electricity run through her until she was nothing but light`：**成立**（原文确有 `electricity`／`currents of power`，非译者添加）。
6. **「辛西娅说自己无罪，海伦娜却在数她鼻子上的雀斑」**（原句 7·读者视角提示）——`:254` `They were so close, Helena could count the cinnamon freckles on the bridge of Cynthia’s nose.`：**成立**（归属方向正确：数雀斑的是海伦娜）。
7. **「原句 3 的『主动权始终在她手上』」**（为什么这样写）——`:89` 吊坠一直藏在裙褶里、辛西娅自己挑出来晃着并说 `‘I lied to you yesterday.’`：**成立**。
8. **「忍冬／金银花」**（导航·叙事手法用了「金银花」）——`:50` `vanilla and honeysuckle pouring from her like some kind of love spell`：**本章成立**。（⚠️ ch06 同一英文词写作「忍冬」，属**跨章术语不统一**，进汇总修复指令文件，本章不改。）
9. **「罗温姑妈」**（导航·一句话概括）——本章英文为 `Aunt Rowan`（`:56` `Aunt Rowan’s was a fifteen-minute walk …`）：**本章成立**。（⚠️ ch24/25/26 与总览三篇写作「姨妈」，属**跨章术语不统一**，进汇总文件，本章不改。）
10. **词表 22 条例句全部逐字取自本章**——**成立，不得改写例句**（22/22 逐字回源命中、22/22 词头在例句内）。
11. **原句 8 的引语省略位置**——md 引语以 `…` 跳过 `While some were instalments, most were withdrawals. A curious combination of letters was repeated often. DOSD.`，省略号两侧均为原文，片段独立取证 0 MISS：**成立**。

---

## 四、覆盖声明与已知盲区

- **本章覆盖**：R1 素读（先于任何 md 打开，89 事件 / 15 关系 / 7 数字 / 8 未决 / 18 陷阱）→ R2 机器层 → R3 三张单子 → R4 逐块 10/10 → R5 判定表，**全流程走完**。
- **本书覆盖（深审进度）**：批 1 = ch02 / ch03 / ch04，批 2 = ch05 / ch06 / ch07 ⇒ **6 / 27 章**已完成 R0–R5（ch07 为第 6 章）。其余 21 章**只有机器层**（R0 全书级已跑），**未做人判**，不得写成「已审查」。
- **同会话盲区（如实标注）**：本书由本会话在写作期产出，本章亦为写作期读过的章之一；本次仍执行「先素读、写完 `1-suread.json` 才开 md」，但**不能视为完全盲态**。
- **本章特有盲区**：L1（三条规则未进 md）被本轮判为「不构成阻断」，理由是 md 的分析本身准确、只是引语选段从 `:50` 起；**该判据是本会话自定**，若后续主张「破戒」必须给出规则才能自洽，则 L1 应升为提示项——须由执行方拍板后再改。
- **未做**：五步审查附录 B（a–e 全文）已被 `审查表.md` 归档取代，不重复执行。
