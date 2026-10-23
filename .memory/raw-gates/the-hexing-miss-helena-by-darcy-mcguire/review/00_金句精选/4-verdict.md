# 4-verdict.md · 《The Hexing Miss Helena》`00_金句精选.md` 审查判定

审查员：主会话自审｜层：**总结层（人判全篇）**｜文件：181 行 / 25 条（①–㉕），每条含「中文 / 上下文 / 为什么重要 / 呼应关系」四项
审查方式：审查表 §0 快审「总览三篇全篇」——逐条核「中文↔英文逐字」「上下文场景」「为什么重要」「呼应关系所引章号与原文」。
取证纪律：所有「查无」用 `/usr/bin/grep` 显式路径并记录退出码；不用 `git grep`。

---

## 一、四组计数

| 组 | 计数 | 明细 |
|---|---|---|
| **逐字** | **引语 35 / 35 相符，0 错** | `overview.py quotes`：本文件 35/35 ✅（行内引语 48 行，已核）；`overview.py full`：整串命中、查无 0、标注与实章不符 0 |
| **对应** | **25 条：24 对应，1 不对应（提示），0 密度不足** | 逐条核「中文给出的动作/说话人/方位/时距」是否与英文引语及其所在段落一致；不对应 1 条＝J8（誓词第四分句的**方向与所属**）。⚠️ 25 条中文均为**意译**，本层判「对应」不判「逐字」 |
| **形态** | **4 / 4 符合** | H1 `# 《The Hexing Miss Helena》金句精选` ✓｜25 条编号连续 ①–㉕ ✓｜每条四项齐备（中文 / 上下文 / 为什么重要 / 呼应关系）✓｜章号标注形如（chNN）✓ |
| **断言** | **共核 68 条：相符 50 ／ 提示 4 ／ 阻断 5 ／ 跳过 0** | 阻断 5 条＝J1／J2（年龄错：七岁 → 九岁或十岁）、J3（时序写反：吻之前/之后）、J4（虚构动作：她对着警察承认）、J5（时序：舞会散场后）；提示 4 条＝J6（方位）／J7（场景）／J8（对应方向）／J9（句读） |

**阻断型条数 = 5。**

---

## 二、判定表（断言 | 证据 | 结论 | 档位）

| # | 断言 | 证据（`text/<文件>:行`） | 结论 | 档位 |
|---|---|---|---|---|
| J1 | `:41` 呼应关系「亚麻壁橱里那个**七岁**的孩子同源」 | `text/ch13_chapter_13.txt:158` `‘I was near to nine or ten. She was the daughter of one of our neighbours. We used to play together. … Clara and I hid together in a linen cupboard. I remember the smell of starch and pears. She pressed her body against mine in the small space and everything in me came alive. It was then I knew.’` | 壁橱那件事发生时海伦娜**九岁或十岁**；「七岁」是 ch21 她母亲被烧死时的年龄（`text/ch21_chapter_21.txt:332` `‘I was seven.’`） | **阻断**（数字错） |
| J2 | `:81` 上下文「ch13 马车里的坦白，她第一次讲出**七岁**那年的事」 | 同上 `ch13:158` `I was near to nine or ten` | 同上：马车里她讲的是**九岁或十岁**那年的壁橱往事 | **阻断**（数字错） |
| J3 | `:95` 上下文「ch15 客厅里的**那个吻之后**，两人用一个只有彼此听得懂的称呼自居」 | `text/ch15_chapter_15.txt:237` `‘Cyn and Hel. What a pair we make.’`；`:239` `Cynthia closed the distance between them. She paused a moment away from Helena’s lips, waiting for permission.`；`:241` `‘Kiss me.’ The need in Helena’s voice was unmistakable.`；`:243` `It was the sweetest kiss she had ever experienced` | 「Cyn and Hel」这句话在 **`:237`**，即吻（`:241`–`:243`）**之前**；md 写成「吻之后」＝时序写反 | **阻断**（时序写反） |
| J4 | `:11` 上下文「ch01 尸体刚被发现，她**对着警察承认**了自己那点见不得人的如释重负」 | `text/ch01_chapter_1.txt:267` `‘Lady Burrows, it gives me no pleasure to ask, but I must. Is there any reason you might want your husband dead?’`；`:269` `Oh dear.`；`:271` `Because she could think of hundreds of reasons.`（全章 271 行，到此结束） | 她**没有答出口**：警司问完，读者看到的是她的内心（`Oh dear.` ＋ 心里有一百个理由）。本条所引英文（`If she did feel a breath of liberation…`）是**叙述者**的假设句，不是她的供词；md 写成了对警察的承认＝虚构动作 | **阻断**（谁做了什么：虚构动作） |
| J5 | `:179` 上下文「ch27 **舞会散场后**的最后一段」 | `text/ch27_chapter_27.txt:344` `‘Is it rather hot in here?’ Helena gave Clio a meaningful look. … ‘I think I’ll take a turn on the terrace.’`；`:346`–`:348` 两人借故离场走向露台；`:355` `I will love you for the rest of my days, Helena Blair.`；`:358` `will you dance with me, my love?`；`:364` `they swayed to a melody playing only for them as Hamlet stood sentinel` | 舞会**正在进行中**：两人借故上露台，露台独白与共舞都发生在舞会未散时。md 写「散场后」＝时序错 | **阻断**（时序） |
| J6 | `:67` 上下文「ch09 俱乐部的人请辛西娅上楼，海伦娜**在楼梯口**只闪过这一个词」 | `text/ch09_chapter_9.txt:240` `inviting them upstairs to his personal office`；`:245` `Mine.`；`:247` `The primitive instinct resonated in her bones.` | 「上楼」有据（`:240`），**「楼梯口」这个方位无据**：原文只写辛克莱把她们往上层办公室请，`:245` 的 `Mine.` 是海伦娜在赌厅里的心声，`:247` 明确是「本能」而非在楼梯口 | **提示**（方位无据） |
| J7 | `:144` 上下文「ch22 她**在新宅子里**给自己下的定义」 | `text/ch22_chapter_22.txt:135` `Cynthia continued to calmly wrap her puppy figurines and place them in a crate that was slowly filling with the items she planned to take with her to the **dowager house waiting in the Cotswold district**.`；`:183` `I am going to put my dowager house to good use.`；`:258` `Every object in Cynthia’s house…`；`:240` `She was a sapphist. A witch. And a powerful woman who would no longer be subject to the whims of others.` | 说这句话时她**还在自己宅里打包**（dowager house 只是「waiting in the Cotswold district」，尚未搬入）；「新宅子」不成立，且与节点九「守寡的宅子」自相矛盾 | **提示**（场景错） |
| J8 | `:171` 中文「……并**把你的心安放为我的庇护所**，直到我的岁月尽头」 | `text/ch27_chapter_27.txt:53` `‘Cynthia, I will love you with my body. Seek you with my mind. Honour you with my spirit. And provide your heart sanctuary for the rest of my days.’` | 原文 `provide your heart sanctuary` ＝**为你的心提供庇护所**（受事＝你的心，庇护所是给它的）；md 写成「把**你的心**安放为**我的**庇护所」：方向反了（心成了庇护所），且「我的」挂到了庇护所上（原文的 `my` 属 `my days`）。方向错＝对应缺陷 | **提示**（对应·方向与所属；见「已核实为正确」第 3 条） |
| J9 | `:96` 为什么重要「……而它出现在一个**谁都没有许诺以后的时刻**」 | `text/ch15_chapter_15.txt:237` `‘Cyn and Hel. What a pair we make.’`；`:243` 吻；誓约在 `text/ch27_chapter_27.txt:53` | 语义可通，但「许诺以后的时刻」在中文里读作「在某个时刻之后无人许诺」，与作者要说的「此刻还没有人为将来许诺」相反；属句读歧义（改 J3 后此句才与其余表述自洽） | **提示**（句读歧义） |

### 与原文相符的 50 条断言（避免「只报问题」的不完整交代）

**逐条核过的 25 条「中文＋英文」引语**（全部逐字命中且语义对应成立；括注＝所属条目）
① ch01 解脱 ✓｜② ch03 嫉妒 ✓｜③ ch04 电鳗 ✓｜④ ch05 摔下基座 ✓｜⑤ ch06 银色月光 ✓｜⑥ ch07 带电的线 ✓｜⑦ ch07 催债信／现金奶牛 ✓｜⑧ ch08 漂亮顺从多生 ✓｜⑨ ch09「我的」✓｜⑩ ch12 我唯一怕的是自己的欲望 ✓（说话人＝辛西娅，见「已核实为正确」5）｜⑪ ch13 亚麻壁橱 ✓｜⑫ ch14 我受够了男人 ✓｜⑬ ch15 Cyn and Hel ✓（**内容对，位置错＝J3**）｜⑭ ch18 光之女巫 ✓｜⑮ ch18 他没有取人性命 ✓｜⑯ ch20 灵魂被织在一起 ✓｜⑰ ch21 她死是因为我 ✓｜⑱ ch21 女神落下的诅咒 ✓｜⑲ ch22 我恋爱了 ✓｜⑳ ch22 萨福式的女人 ✓（**场景错＝J7**）｜㉑ ch23 母亲的吞噬之爱 ✓｜㉒ ch24 面对死亡不再撒谎 ✓｜㉓ ch25 女神，来接我走 ✓｜㉔ ch27 四句誓词 ✓（**中文方向错＝J8**）｜㉕ ch27 露台共舞 ✓（**时序错＝J5**）

**「上下文」场景核验（25 条中 20 条成立）**
① ch01 尸体刚被发现 ✓｜② ch03 辛西娅第一次登门、海伦娜在门厅嫉妒 ✓｜③ ch04 第一次尝试读心 ✓｜④ ch05 守寡第一夜、火光里 ✓｜⑤ ch06 守寡的第一个夜晚 ✓｜⑥ ch07 独处面对债务与旧账 ✓｜⑦ ch07 一封没有署名的催债信落到她手里 ✓｜⑧ ch08 被迫回忆这桩婚姻给自己定下的规格 ✓｜⑨ ch09 俱乐部的人请辛西娅上楼 ✓（方位错＝J6）｜⑩ ch12 照相之前，两人在暗处单独说话 ✓｜⑪ ch13 马车里的坦白 ✓（年龄错＝J2）｜⑫ ch14 晚宴桌上 ✓｜⑬ ch15 ✓（时序错＝J3）｜⑭ ch18 她看着辛西娅被利珀特的话刺痛 ✓｜⑮ ch18 她读利珀特的脑子 ✓｜⑯ ch20 罗温姨妈解释魔宠 ✓｜⑰ ch21 告白之后的夜里 ✓｜⑱ ch21 她解释自己为什么从不敢承认那是天赋 ✓｜⑲ ch22 这场谈话之后 ✓｜⑳ ch22 ✓（场景错＝J7）｜㉑ ch23 终于看清身上那条危险的谱系 ✓｜㉒ ch24 被关在抽干了水的房间里 ✓｜㉓ ch25 子弹出膛的一瞬 ✓｜㉔ ch27 卧室 ✓（中文方向错＝J8）｜㉕ ch27 ✓（时序错＝J5）

**「呼应关系」所引章号与原文（25 条中 24 条成立）**
① ch20「丈夫一死，她就不再欠任何人」✓｜② ch23 母亲的吞噬之爱 ✓｜③ ch15「我很想吻你」✓｜④ ch14「我受够了男人」✓｜⑤ ch11 现金奶牛 ✓｜⑥ ch04 电流是同一个比喻的两次出现 ✓｜⑦ ch11「一头现金奶牛」✓｜⑧ ch22「她不再受制于任何人的任性」✓｜⑨ ch12「我唯一怕的是自己的欲望」✓｜⑩ ch20「灵魂不能交织」✓｜⑪ ch21「我七岁」✓（**J1 的对照句，属实**）｜⑫ ch22 推开门 ✓｜⑬ ch27 收尾 ✓｜⑭ ch26 姨妈「我们不做伤害」✓｜⑮ ch25 辛克莱「都想毁掉他」✓｜⑯ ch24 灵魂织进挂毯 ✓｜⑰ ch22「被爱吓退」✓｜⑱ ch25「用自己的血解开封印」✓｜⑲ ch24 濒死时承认 ✓｜⑳ ch08 漂亮/顺从/多生 ✓｜㉑ ch12 同一担心 ✓｜㉒ ch23 母亲的结局 ✓｜㉓ ch24「死后留在世上守望爱人」✓｜㉔ ch18 旧誓 ✓｜㉕ ch09「我的」首尾相扣 ✓

---

## 三、机器层

- `overview.py quotes` → **RC=0**；本文件 **35/35 ✅**；行内引语 48 行（已核，建议迁为引用块，**本轮不迁**）；总览引文 86/86（100%）；完全干净文件 3/3。
- `overview.py full` → **RC=0**；整串命中、**查无 0**、标注与实章不符 0、章节覆盖 27/27。本文件 3 条跨标签拼接为**提示**（`overview.py` 自带判级，不判红）。
- `bash scripts/gate.sh` → RC=0，0 条阻断（全书级）。
- ⚠️ 本文件 9 条缺陷（J1–J9）**全部落在门禁覆盖不到的中文断言层**：门禁只核引语逐字与标签章号，核不了「上下文场景对不对」「年龄对不对」「时序对不对」。

---

## 四、已核实为正确（防误修，下一轮不得以「读着不对」为由改动）

1. **⑪ 呼应关系引 ch21「我七岁」——成立，不要因为 J1 就把这里也改成九岁。** 依据：`text/ch21_chapter_21.txt:332` `‘I was seven. Old enough to have done something. And I tried, but my powers weren’t enough to stop the fire.’`。**七岁＝那场火；九岁或十岁＝壁橱**，两个年龄各有其主。
2. **⑬ 的英文引语与中文逐字相符，错的只是「上下文」的时序。** 依据：`text/ch15_chapter_15.txt:237` `‘Cyn and Hel. What a pair we make.’`。修 J3 时**只改 `:95` 的上下文一句**，不得动 `:94` 的引语与中文。
3. **㉔ 中文前三分句「以我的身体爱你／以我的心念寻你／以我的灵魂敬你」——成立，勿改。** 依据：`text/ch27_chapter_27.txt:53` `I will love you with my body. Seek you with my mind. Honour you with my spirit.`。⚠️ 第 4 分句另有问题（J8），**只改第 4 分句**。
4. **㉕ 中文（两人随着只放给她们的曲子摇动、哈姆雷特放哨）——成立，勿改。** 依据：`text/ch27_chapter_27.txt:364`。错的是「舞会散场后」这个上下文（J5）。
5. **⑦ 的说话人未指名，不构成错误；概述层已核实该句出自辛西娅。** 依据：`text/ch12_chapter_12.txt:270`（说话人＝辛西娅）。本条 ⑦ 的**上下文**「ch12 照相之前，两人在暗处单独说话」与原文一致（`ch12:155` `‘I need to speak with Lady Burrows before we begin. Privately.’`）。
6. **⑪ 的「中文」（壁橱那段直译）——成立，勿动。** 依据：`text/ch13_chapter_13.txt:158` 逐字对应；**只有 `:81` 上下文里的年龄错**。
7. **① 的英文引语（`If she did feel a breath of liberation…`）逐字无误。** 依据：`text/ch01_chapter_1.txt`（叙述者句）。错的是 `:11` 上下文把它说成「对警察承认」（J4）。
8. **行内引语体（48 行）不判红**——`overview.py quotes` 明示「已核，但建议迁为 `> "…"（chNN）` 引用块」，是体裁建议不是缺陷；**不要在本轮为迁体裁重排本文件**（会动 35 处已核引语）。

---

## 五、覆盖声明与已知盲区

- **本文件覆盖**：人判**全篇**（25 条 ①–㉕，逐条核四项），68 条断言全部回源取证。
- **全书覆盖**：机器层 27/27 章 + 总览三篇；人判 **ch01 / ch10 / ch18 / ch27 = 4 / 27 章** ＋ 总览三篇全篇；其余 23 章**仅机器层**。
- **本层盲区（如实标注）**：与 `00_概述.md` 同——本层**没有**「先素读再开 md」的顺序纪律（总览的形态就是先读成品再核）；独立性弱于 ch10。补偿：每条断言要求显式行号，且对「年龄／时序／说话人」三类专门回源（J4 即由此查出，且**同一句英文在概述层的正确写法反证了本条的误读方向**）。
- **未做**：深审 R0–R5 全章未执行；快审升级条件已命中，**须提请用户确认，本会话不自行升级**。
