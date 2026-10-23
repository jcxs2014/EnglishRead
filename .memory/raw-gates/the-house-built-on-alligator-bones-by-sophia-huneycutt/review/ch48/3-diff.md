# ch48（Chapter Forty-Seven）R3/R4 差异与定点核验

## 探针
- v48（词表例句回源）：17 行全命中，0 flagged。
- ap48（直撇号）：0 处。
- in48（块内嵌英文）：not-in-book 2 条均为模板 token（'Chapter Forty-Seven'／'Tropes'），干净。
- span48（反引号自检）：见文末。（首跑曾因 cwd 在书目录、全书语料路径解析为空而 1 条 MISS，从 repo 根复跑已通过。）

## 阻断
（无）

## 提示
| # | 位置 | md 现状 | 原文 | 说明 |
|---|---|---|---|---|
| P-48-1 | md L10 | 「末句是『我邪恶，且被爱着』」 | text/ch48_chapter_forty_seven.txt:219 `I am wicked, and I am loved. Apparently, both things can be true.` —— 原文末段还有后半句，md 引号内截短 | 建议补全或去掉引号改为概述 |

## 假红
（无）

## R4 定点核验（导航层断言逐条回源）
- 拉转椅转身坐下拦路：text:84 ✅
- 病房默写好的话（mentally write a speech in case he cornered me）：text:99（词汇例句）✅
- "Just let me go"：text:111 ✅
- 拿走拐杖掷床上、双手被握、拇指打圈：text:117 ✅
- 吻额头（回忆，text:24）与吻太阳穴（章末拥抱，text:126）两处各自命中，md L10/L11/L26 分别对应，不冲突 ✅
- "Don't go"／"Stay"：text:129 起 ✅
- 请 Virginia 烧画像及掺身体部位的画：text:153 ✅
- 皮送回 Egans Creek 沼泽：text:168 ✅
- Virginia 白发披背坐门廊摇椅望草坪（窗外望见）：text:171 ✅
- "You sure she's forgiven me?"／"Does that make you feel better?"：text:174/:177 ✅
- "How could I have said no?"：text:141 ✅
- "seemingly happy ending"：text:192 ✅
- 撞同学头进水泥地并乐在其中：text:204 ✅
- "I came to realize, bit by bit"＋三个 as 从句（city inspector stare at his check／Ironheart's skin 沉入沼泽／驶过 mainland bridge）：text:207 ✅（city inspector＋支票＝与序章 ch01:15 的跨章呼应点，与快审护栏一致）
- 马萨诸塞与 Maine 之间观景台：text:213 ✅
- 末段 "I am wicked, and I am loved."：text:219 ✅
- Harrison 手在上臂停一下退回门框（前半）vs 整个握住（后半）：text:18/:117 ✅
- bolt gun 打 Ginny 脸：原句 4 逐字（v 探针覆盖）✅
- Ida 画像残骸、斧插心口：text:153 ✅
- "It was a huge sacrifice, and we will never, ever forget it."：词汇表例句 ✅
- Ginny 说 "she was beyond saving"（原谅的最后稻草）：text:177 ✅

## 查无声明
- 无新增查无项。

## 快审护栏复核
- 本章不涉 Michelle 死因两版本／Leon 多版本新增内容；Mama 与 Gazzie 在 text:207 的「not my fault」清单里 md 已按原文保留「Gazzie 项只说不是她的错、未写成死亡」这一留白，符合不裁决红线。
- 「Gazzie was right all along」（text:57）为 Harrison 台词转述，md 未升格为叙述者结论。

## 已核实为正确
- P-48-1 证据逐字级；其余导航断言 20 项全命中。
- 情感弧线（怕被看穿→要求走→愣住→转冷→有保留的平静）、Tropes 层与原文一致。
- 词汇表 17 词头例句全部回源。
