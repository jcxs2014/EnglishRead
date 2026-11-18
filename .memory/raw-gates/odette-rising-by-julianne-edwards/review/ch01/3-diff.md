# 3-diff · ch01 the funeral from the window（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条事实，区间/锚点 100% 命中验证）；R2：chapter.sh --json rc=0。

## 三单对账（R1 素读 vs md）

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 无 | R1 8 条事实（报丧/邻居/十年/决定出门/三裙一帽/车夫推/紫杉跪倒/棺落坑）md 全覆盖 | — | 无漏 |
| 编 | B8 分析「儿子还在旁边偷看她」 | boy "stole looks" 在墓园场（text/ch01:124 区间 12400 附近），本块引语（送葬途中）无儿子动作 | 分析把墓园动作提前挂到送葬块 | **阻断→已修**（改括注说明+删提示句） |
| 编 | B9 提示「十年来第一次被陌生人伸手」 | 本章车夫已触碰（text/ch01 "He took her by the elbow, and she started at being touched"）；引语内亦无伸手 | 与本章前文及 ch28 "no one ever had"（指她的肉褶）矛盾 | **阻断→已修**（改为「跪倒后第一个赶来的外人」） |
| 错 | 无 | 主语/因果/数字/时序逐块核对一致 | — | 无错 |

## R1 有、md 叙述层亦有的关键事实（抽查回源）

- 报丧死因：text "A failure of his heart, she had said"（区间 1666:1726）↔ md 导航「心脏衰竭猝死」✅
- 邻居画像：text "a tall man of about thirty, with a slender face and black hair"（3120:3182）↔ md 导航「瘦高、黑发、约三十」✅
- 出行装备：text "three dresses... loose-fitting linen smocks"（5988:6060）↔ md 原句3 分析「只有三件宽松亚麻罩裙」✅
- 上车方式：text "he put his shoulder to the back of her thigh and heaved"（9775:9831）↔ md 原句5「用肩膀顶住她大腿后侧把她硬推进车厢」✅
- 结局：text "soon the coffin was disappearing into the dark pit"（16438:16488）↔ md 原句10「棺材落进坑」场景 ✅

## 取证命令示例

/usr/bin/grep -c "stole looks at her" notes/books/novels/odette-rising-by-julianne-edwards/text/ch01_chapter_1.txt → 1（墓园段）；退出码 0
/usr/bin/grep -c "took her by the elbow" notes/books/novels/odette-rising-by-julianne-edwards/text/ch01_chapter_1.txt → 1；退出码 0
