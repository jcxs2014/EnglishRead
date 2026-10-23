# ch46（Chapter Forty-Five）R3/R4 差异与定点核验

## 探针
- v46（词表例句回源）：18 行全命中，0 flagged。
- ap46（直撇号）：md 5 处，全在导航/分析层行内英文（L10、L12、L13、L46、L54），逐条回源见阻断 C-46-1。
- in46（块内嵌英文）：not-in-book 3 条中 'Chapter Forty-Five' 与 'Tropes' 为模板 token（预期）；'yet like' 见假红 F-46-1。
- span46（反引号自检）：见文末。

## 阻断
| # | 位置 | md 现状 | 原文 | 判型 |
|---|---|---|---|---|
| C-46-1 | md L10/L46（"It's her"）、L12（"I've always had it in me"）、L13（"Aren't you going to say anything?"）、L54（"She's not in control of your actions. You are."） | 分析层行内英文 5 落点用直撇号 | text/ch46_chapter_forty_five.txt:63 `“It’s her,” Gazzie spat.`；:183 `“I’ve always had it in me,”`；:27 `“Aren’t you going to say anything?”`；:90 `“She’s not in control of your actions. You are.”` —— 原文全部弯撇号 | C 型（行内英文非逐字·直撇号，⑩/⑯ 先例） |
| C-46-2 | md L10 | 「砖拔出后是一个柜大小的空腔」 | text:40 `The brick had hidden a hollow the size of a filing box.` —— filing box＝文件盒/档案盒，与「柜」差一个数量级 | C 型（事实错译） |

## 提示
| # | 位置 | md 现状 | 原文 | 说明 |
|---|---|---|---|---|
| P-46-1 | md L13 | 「品尝鳄鱼湿指」 | text:111 `To savor an alligator’s blood wetting my fingers.` —— 尝到的是「鳄鱼血沾湿手指」，md 压缩掉 blood 后可读成「品尝湿的鳄鱼手指」 | 修饰错位，建议改「尝到指上鳄鱼的血」 |

## 假红
| # | 位置 | 串 | 判定 |
|---|---|---|---|
| F-46-1 | md L64 | `yet like` | 叙事手法分析里自造的语法标签（「用 like… yet like… 把两个比喻叠在同一张脸上」），非引语、原文整串查无；in46 探针按引语口径核查致报。属「分析层自造连字标签」假红先例 |

## R4 定点核验（导航层断言逐条回源）
- 画框落地崩出一颗牙（mother-of-pearl→tooth by the fireplace）：text:36 ✅
- 两英尺见方未上漆砖墙＋单块松砖：text:36 ✅
- 罐内容（画笔/金箔/圆球/褐液/骨白颜料/最里面深色头发/另两只是牙和血）：text:40/:45 ✅
- 画像上贝母镶嵌是牙、酒红（maroon）裙上颜料是血、白云人骨颜料、人皮胶：text:45 ✅
- 追问 Whose→Gazzie 推砖不答→"It's her"：text:63 ✅
- 呕吐：text:48 ✅
- "She asked me to."（她要求我这么做的）：text:78 ✅
- "Everything you are… is because of her."（你的一切也是因为她）：text:93 ✅
- 判词「她和他们一样自私」：text:96 `Mama was as selfish as any of them.` ✅
- 三件被推动的事（撞 Michelle 头/推 Mama 脖子向后折/鳄鱼血沾指）：text:111 ✅
- 酸茉莉＋步枪托抵太阳穴：text:129 ✅
- Ida 现身（wine-red dress、bloat、半透明、比以往清楚）：text:132 ✅
- 同一把割祭鳄的刀顶腹：text:144 ✅
- 十五英尺 Ironheart 浮现（barely there, an impression in the air）：text:147 ✅
- Ida 抓不存在的步枪、"Ironheart was distracting her"：text:153/:156 ✅
- 抖腕后刀落地：text:168 ✅
- Gazzie "You don't have it in you, either"→"I've always had it in me"/"How do you think your daughter died?"：text:171/:183 ✅
- 破窗 jagged shard、推入、皮如鳄鱼皮对剥皮刀：text:114/:186 ✅
- Ironheart 抓脚把 Ida 拖入地板之下：text:225/:231 `pulled her beneath the floorboards` ✅
- 血染康乃馨粉：text:237 ✅
- Gazzie 笑到流泪＋"You really are a Greer"：text:258/:261 ✅
- 只剩 Virginia 抽泣：text:270 ✅
- 买通殡仪员下葬空棺：text:66 ✅
- Virginia 张嘴想求停手又闭、Harrison 抓肩、Virginia 右眼肿脸颊裂：text:120 ✅
- Ida 抬手命令→叙述者手指抽动、手臂被拽向玻璃：text:201 ✅
- Virginia 跪查脉搏、Harrison 拉上沙发：text:240 ✅
- Gazzie 可为 Ida 烧掉整个镇子：text:99 ✅
- "Or maybe it was Ironheart she stared at; she'd never mentioned actually seeing it."：text:159 ✅

## 查无声明
- 无新增查无项；`yet like` 的查无（`/usr/bin/grep -n "yet like" text/ch46_chapter_forty_five.txt`，0 命中、退出码 1）即 F-46-1 的取证。

## 快审护栏复核
- 本章不涉 Michelle 死因两版本、Leon 多版本、Mama 三口径等红线；`neck snapped backward`（text:111）是叙述者引用 Mama 之死的口径之一，md 未合并其他口径，符合「不裁决」。

## 已核实为正确
- C-46-1 五落点、C-46-2、P-46-1、F-46-1 证据均为原文逐字级。
- 情感弧线（麻木→恶心→追问→判词→迟疑→动手→胜利/松气）、Tropes 层与原文事件顺序一致。
