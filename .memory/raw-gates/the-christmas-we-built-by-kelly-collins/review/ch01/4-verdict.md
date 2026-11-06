# 4-verdict · ch01（R4 逐块人判 · 12 块全查）

覆盖声明：R1 子代理盲读（text 全文至末行）→ 主会话 R3 对账 → 主会话逐块 R4。机器层 rc=0（2-machine.json）。

## 逐块判定

| 块 | 断言 | 证据（text/ch01_chapter_1.txt） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 中文理解与引语主语一致（她提前到/计划以失楼收场） | :14 "I arrived fifteen minutes early…Every plan I made while I waited ended with him owning my building" | 对应成立 | 正确 |
| 2 | 分析"好奇心赢了，她过街去看"讲到引语外（第 4 句） | :20 "Curiosity won, so I crossed Main Street and looked through the glass." | 引语选短 → 扩引语含该句（54 词） | 阻断→已修 |
| 3 | 分析括注"后文随即点明大半个街区"指向引语外 | :47 "He wanted most of the block." | 引语选短 → 扩引语含该句（44 词） | 阻断→已修 |
| 4 | 三主体（店/旧物业/新公司）与引语一致；"五周前" | :50 "Five weeks ago, Portland Property Management had sold the building to Cole Development LLC" | 对应成立 | 正确 |
| 5 | 第十二只红雀/前四只 Adele/后七只 Nora | :77 "Adele Fisk, the shop’s previous owner, had marked the first four. I’d marked the next seven." | 对应成立 | 正确 |
| 6 | 手抖/门铃/个人最佳 | :86 "Neither of us mentioned that his hands were shaking…That might have been a personal best." | 对应成立 | 正确 |
| 7 | 分析"诺拉把欢迎礼递过去"——递盒动作在引语前一段 | :116 "I held out the box. “I brought you something.”"（未收） | 分析越界一词 → 中文理解改为"格里芬接过欢迎礼"（不扩块，避免 13 块） | 提示→已修 |
| 8 | 学位/十二年/救镇非榨取 | :191 "I have a degree in structural engineering…I’m not trying to exploit it." | 对应成立 | 正确 |
| 9 | 裂缝三年/水渍/配电箱/屋顶 | :203 "That foundation crack has been spreading for at least three years." | 对应成立 | 正确 |
| 10 | 应急修补/货存开门/基建等旺季后 | :212 "I had kept Winters Wonderland standing with emergency fixes…" | 对应成立 | 正确 |
| 11 | 木柴烟火气/咖啡/不想后退 | :245 "I could smell woodsmoke on his coat and coffee on his breath." | 对应成立；施事：闻的是她、不后退的是她 ✓ | 正确 |
| 12 | 分析"晚七点…挂饰盒开着放在卷尺旁；玻璃接住灯光"——前两句在引语外 | :311 "At seven that evening…caught the light when he moved." | 引语选短 → 扩引语至段首（72 词） | 阻断→已修 |

施事三问抽查（全块过一遍）：块 11"她闻/她不想退"方向 ✓；块 9"他指她的店" ✓；块 5"两代店主接力标年份" ✓——无归属反转。

「第一次/唯一/数字」回原文：`六笔现金`（:47 六 cash sales ✓）·`十二年社区开发`（:191 ✓）·`第十二只`（:77 this one made twelve ✓）·`至少三年裂缝`（:203 ✓）。

修复后机器层：chapter.sh rc=0（12 块，⚠️ 块数偏离本书中位 6——首章四幕+对话密集，理由已记任务表，提示级不修）。

## 已核实为正确（防误修护栏）
1. "Portland Property Management 拥有砖、她拥有店"（block4）——text/ch01:50 原文逐字，勿改。
2. "第十二只红雀；前四只 Adele 标、后七只 Nora 标"（block5）——text/ch01:77 逐字，勿改（ch25 第十三只与之连续）。
3. "结构工程学位＋十二年社区开发经验，不是 MBA"（block8）——text/ch01:191，勿改。
4. "地基裂缝至少扩了三年"（block9）——text/ch01:203 原文 "at least three years"，勿改。
5. 块数 12：新书硬限 2–15 内；首章四幕（查档—贺礼—对峙—对视）+ 对话密集，取舍理由在任务表——勿以中位 6 为由删块。
