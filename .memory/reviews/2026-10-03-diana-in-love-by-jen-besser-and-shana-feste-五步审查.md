# 《Diana in Love》五步审查报告

- **审查日期**：2026-10-03
- **审查方**：ZCode-Mac（同会话审查——用户在本会话内发起，按 AGENTS 第 10 条「同会话审查的执行要求」完整执行 a–e，未降级）
- **对象**：notes/books/novels/diana-in-love-by-jen-besser-and-shana-feste（22 章正文 + 总览三篇 = 25 md）
- **整改 commit**：`d018092d5`（45 处修复）· 复验 **gate.sh EXIT=0（0 阻断）**
- **门禁原件**：`.memory/raw-gates/diana-in-love-by-jen-besser-and-shana-feste/`（review_a.txt = a 步全量；review_gate_final.txt = 复验终验）

## 缺陷总数与三档分布

**阻断型 42 处（全部已修）＋ 提示型 5 处（只记不改）＋ 假红型 2 处（工具口径，不改）**。子代理三批（ch01–08 / ch09–15 / ch16–22+总览）报告合计 49 条报警，主会话逐条回源复核后确认 42 条真缺陷；无幻觉报警（子代理全部先 grep 落行），1 条升级（ch18 creepy 的三重错误比初判更重）、1 条部分成立（ch04 十七年修辞改判修辞不改）。

### 一、跨章引用章号错位（18 处，均为「上一章/下一章/chNN」指错，引语实体真实）
| # | 位置 | 错误 | 实际 |
|---|---|---|---|
| 1 | ch04:53 | 「下一章对 Petra 一泻千里」 | 礼车在本章（Chapter Three） |
| 2 | ch05:33 | 「上一章 Band-Aid 意象系统」 | Band-Aid 在 ch03（Chapter Two） |
| 3 | ch05:35 | 「上一章买地毯盖地板响」 | 在 ch03 |
| 4 | ch06:35 | 「上一章喊错名字的回声」 | 喊错名字在 ch02（Chapter One） |
| 5 | ch06:71 | 「Arthur 话题第一次浮出水面（上一章只是猫照片）」 | crush 在 ch04、坦白在 ch05（上一章正是坦白本体） |
| 6 | ch07:35 | 「上一章礼车里的 mislaid 独白」 | 在 ch04 |
| 7 | ch08:35 | 「上一章他的 Band-Aid 判词」 | 在 ch03 |
| 8 | ch08:62 | 「上一章 L'Wren 可能会跟 Arthur 上床」 | 在 ch05 |
| 9 | ch09:87 | 「上一章 Band-Aid 判词的反面」 | 在 ch03 |
| 10 | ch11:26 | 「上一章礼车里她说…」 | ch10 无 Petra；礼车在 ch04 |
| 11 | ch15:53 | 「上一章 Oliver 说 You never told me」 | 是 Diana 在本章（ch15）两度追问 |
| 12 | ch19:24 | 「ch17 的 keeping you in my pocket」 | 在 ch13 |
| 13 | ch19:69 | 「ch18 的 weird and tense」 | 在 ch14 |
| 14 | ch21:62 | 「ch07 的 a perfect opening」 | 在 ch04 |
| 15 | ch22:26 | 「ch20 暂停令」 | 在 ch21 |
| 16 | ch22:71 | 「ch16 的 I don't recognize my reflection」 | 在 ch06 |
| 17 | 金句⑰呼应 | 「ch15 的 never great（Oliver 版）」 | 在 ch18 |
| 18 | ch16:89 | 「后文与 Petra 的 mislaid 汇成」 | mislaid 在前文 ch04 |

### 二、无出处事实断言 / 虚构（12 处）
| # | 位置 | 内容 | 复核证据 |
|---|---|---|---|
| 19 | ch18:42 | 「他在 22 岁时就知道」 | 全书无年龄；与时间线冲突（twenty-six again / fifteen years / forties）→ 改「初夜时」 |
| 20 | ch08:51 | 「十四年婚姻」 | 原文 Fourteen. Fifteen? 是与 Jasper 分开的年数；婚龄未给出 → 改「多年」 |
| 21 | 金句⑫ | 同上（十四年婚姻） | 同上 |
| 22 | ch11:26 | 「她说『我不差这一点人情』」 | 全书查无此句（引述虚构）→ 改为 ch04 逐字原句 won't be convinced… |
| 23 | ch11:35 | 「两章之后他会真的搬出地下室」 | 全书未搬出（ch22 仍住）→ 改「到 ch22 他还住在这儿」 |
| 24 | ch13:71 | 「她每天听陌生女人给幻想打分（三星半、四星）」 | 打分机制不存在（三星半是 ch07 Diana 自拟书评）→ 改写 |
| 25 | 金句⑰ | 「每天给陌生幻想打分的职业」 | 同上 |
| 26 | ch22:35 | 「Alicia 的职业（拍电影的老师）」 | 职业未明说 → 改为 freshman shorts screening 证据 |
| 27 | ch18:69 | 「creepy 那句判词（ch16 录音事件）」 | creepy 仅在 ch18 且 Oliver 否认说出（I never said it was creepy）；录音由 Diana 提出 → 重写 |
| 28 | ch18:42/60/132、ch19:132、概述:26 | 「二十年」系列 | 原文只说 for so long；时间线至多约 9 年 → 全改「多年」 |
| 29 | ch22:78 | 「记了整整九章」 | 实为 12 章间隔 → 改「整整一个秋天」 |
| 30 | ch09:51 | 「六个 Yes」 | 实为 7 个（原文实测），且原分解 2+2+3 自相矛盾 → 改「七个…前四后三」 |

### 三、说话人/归属（3 处）
| # | 位置 | 错误 | 实际 |
|---|---|---|---|
| 31 | ch08:62 | Should I let your husband know? 写成 Alicia「找补」 | 对白轮替证明是 Diana 的打趣 |
| 32 | ch18:62 | What would that have sounded like? 写成「由丈夫说出、Miriam 失业」 | You being honest with Oliver? 第三人称 → 是 Miriam 的提问 |
| 33 | ch15:53 | You never told me 归给 Oliver | 是 Diana 对 Oliver 说的 |

### 四、承诺方向颠倒（2 处）
| # | 位置 | 错误 | 实际 |
|---|---|---|---|
| 34 | ch09:89 | 「他让她保证…她应下了」 | Diana 答 I don't know if I can ever do that again（推脱） |
| 35 | ch09:135 + ch10:89 | 「她笑着应了」/「她被许诺」 | 同上（方向+事实双错） |

### 五、分析层英文改写（3 处，六道门禁全绿的盲区）
| # | 位置 | md | 原文 |
|---|---|---|---|
| 36 | ch03:51 | take over the whole mood, the entire room | **It** takes over the whole mood, the entire room |
| 37 | ch18:51 | tender and good but never great | tender and **it was** good but never great |
| 38 | ch15:89 | watch me never move again | Watch me close my eyes and never move again（压缩转述） |

### 六、a2 型引语截短（7 处，修法=扩 span 让引语覆盖分析；中文理解层已覆盖的内容回填引语）
ch02:47（补 He was looking at me like that now.）· ch03:74（补 "It is sad." He looks me in the eye.）· ch07:74（补 She nods.）· ch17:65（补 It wasn't the drugs. Or the DJ, he teases…He kisses my cheek.）· ch17:83（补 After he leaves,）· ch21:38（补 I want to tell him so many things.）· ch21:83（补 Piece of advice…"…school gym.）；ch01:97 为跨段不可扩 → 收窄中文理解；金句②随池同步收窄。

### 七、叙事形式描述失实（1 处）
| # | 位置 | 错误 | 实测 |
|---|---|---|---|
| 39 | ch14:14 | 「他说的每一句都打引号、她说的全裸奔——标点即权力关系」 | 幻想区间双方台词全部无引号（引号对仅短信 "you up?"）→ 重写 |

### 八、总览层（6 处）
概述「你值得」递给 Petra（实为 Alicia ch22 的话）· 金句㉕「说出→**被拒**→出土→留给她的」（无被拒：她答 Yes. I would have.）· 节点1「开幕式**前夜**」（实为当晚到场时）· 节点1「旧咒语原样念出」（实为回忆+同款眼神）· 节点6「麦当劳早餐边交底牌」（实为随后商店门口）· 节点7「枕头边揭晓」（实为从手包里发现）。

### 九、词表/笔误（4 处）
ch18 释义夹英文且词形非原文（hem and haw → 纯中文）· ch07 cornichon 进阶/基础重复收录（删基础档）· ch04「Dirt Diana」笔误 · ch08 导航「夜里」→「傍晚」（时序）· ch11:81 引语缺原文开引号（构建器 span 补回）。

## 提示型（只记不改，5 条）
- ch17「重返十七岁」为修辞非年龄断言（L'Wren 年龄原文未给）。
- ch20「七岁」×2 有原文支撑（seven-year-old / One. Seven years old.）。
- ch07:80「本章结尾」实为午睡段——位置措辞不精确，语义无伤（子代理报提示级，随 total absence 语句保留）。
- ch05:51 已升级修复（原「上一段」实为上一章——已在阻断清单内）。
- WARN 26 条全部为 ≥9 字符长度启发式（基础档疑含超纲词），逐条看过并接受。

## 假红型（工具口径，2 条）
- sweep_analysis_inline ⚠️「00_概述:28 跨章」：00_* 文件为全书层口径，引语标（ch20）且 check_overview_full B 段、check_overview_labels 均判「对 67/66」——工具对 00_* 的跨章提示不适用。
- check_xref_indep「中文式待人判 186」：其中绝大多数为「与 chNN 的 X 对读」式呼应引用（X 为中文描述无英文字面），机械核不了——由 d 步子代理逐对核对覆盖（31 条可机核的由 check_xref_zh 核：命中 31 / 错 0）。

## a–e 执行记录
- **a**：第 3 条门禁全量重跑（原始输出 review_a.txt）：verify 241/241（--full 取证 0）· vocab 561 行 FAIL 0 · entities 0 · corruption 0 · sweep_full 175/0/0/0 · short_quotes 1/1 · anchor 凭空 0 · audit_numbers 4 ⚪ 人判（1 阻断成立=22 岁，其余有据/修辞）。
- **b**：逐章归属换路径——check_chapter_quotes --book-dir 全书模式 175/175（写作期用单章模式）；cliffhanger 边界经子代理逐章 text/ 对照复核。
- **c**：结构双实现——audit_structure 0 + check_struct_indep 0；check_overview_full A 67/查无 0、B 67 对、F 7 对、E H1 0。
- **d**：机械子项用第二实现（check_xref_indep 英文证据 0 报警 / check_analysis_indep 8 落点逐条人判 → 3 真缺陷 / sweep_analysis_inline）；语义二审 = 3 子代理并行逐块核对 176 块 + 总览 66 条（附 2 个真实失败案例 + 防幻觉条款），主会话对全部报警逐条回源复核（5 条最重报警逐一 grep 验证后确认）。
- **e**：总览事实核对——子代理批 C 覆盖 66 条引语逐字 + 说话人窗口 + 概述情节断言逐条 grep 回源；主会话对跨书污染自检（本书人物 Rockgate/Sunny/Trish/Kirby 与他书同名仅为本书内部跨章复现，grep -rl 确认无他书串入；Sandrine Lemaire/Playing with Dolls 为本书内虚构书中书，非真实出版物——概述已按书中书处理）。

## 投毒测试（修完先提交再投毒）
- 向 ch09 分析层注入裸长假英文短语（found you at last in the crowded bar）：sweep_analysis_inline **未报警**（毒句被计为「逐字 1016」+1）——**如实记录：该类「凭空英文短语」的机械防线本轮无效**，其真防线是子代理逐对核对（本轮 42 处阻断正是子代理抓出）。check_analysis_indep 对裸文本不扫（口径为标记片段）。两次投毒后均 git checkout 干净回滚（工作树 0），corruption 复扫 FAIL 0。

## 复验（整改后基线对比）
verify_quotes 241/241 · 逐章 175/175 · vocab 561 FAIL 0 · sweep 175/0/0/0 · corruption 0 · entities 0 · anchor 凭空 0 · audit_structure 0 · check_struct_indep 0 · block_keywords 0 · short 1/1 · 总览 verify 66/66 + full 67/查无 0 + labels 66 对 · **gate.sh EXIT=0（0 阻断）**——较完工基线（同为 EXIT=0）无自伤。

## 同会话审查的已知局限（结论声明）
① d 步子代理为单轮逐对核对，其「说话人窗口」抽查未覆盖全部 176 块的每一条（子代理自报为「抽查+重点块」强度，非逐块 200 字窗口全开）；② 「与 chNN 的 X 对读」式中文跨章引用的机器口径不可达部分，依赖子代理阅读判断，可能存在与子代理同样盲区的漏报；③ 投毒测试显示「凭空英文短语」在机械层无有效防线，此类若子代理漏报则无第二道网。以上供用户判断是否另行指派异实例复核。
