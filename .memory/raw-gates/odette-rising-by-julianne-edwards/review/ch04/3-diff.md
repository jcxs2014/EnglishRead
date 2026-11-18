# 3-diff · ch04 the blue door（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到「六七岁时才被允许跟 Dendron 上街买东西」（text/ch04 "when she was six or seven, she had been allowed to go on the morning shop"）——md 未引此段 | 取舍理由：出厂前史由 ch10 的「十一岁起被停带出门」承担闭环；ch04 精读块预算（5 块/短章）让给了血案线 | 提示（不修，理由如上） |
| 漏 | 无 | 其余 7 条（两个月字条未拆/父亲作息/R Merry 两次巴黎/pulped 细节/蓝门+女人/Dendron 处置+Dr. Vaissier/shadows 爆发）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：pulped/蓝门/厨房桌全部＝Merry 台词；「brown」＝叙述层——md 归对 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- 两个月/字条未拆：text "Two months had passed since her visit to the factory"（69:121）↔ md 导航「两个月昏睡」+「Beauclerc 的字条堆在门厅」✅
- 父亲作息：text "rising at seven, leaving at eight, home at five"（456:503）↔ md nav「七点起身、八点出门、五点归」✅
- Merry 两次巴黎：text "Once to visit my mother, and the second to fetch Monsieur Huré home."（1482:1550）↔ md 原句1 分析「两次巴黎」✅
- pulped：text "His kneecap was smashed. His face split. Bitten through his tongue."（2268:2335）↔ md 原句2 ✅
- 蓝门：text "The house had a blue door. I don't know where."（5660:5706）↔ md 文件名与导航「蓝门血案」✅
- 处置链：text "Me and Madame Dendron. We put him on the table, and she inspected him."（6144:6214）↔ md 原句3 ✅
- shadows：text "there had been shadows shrouding Edouard Huré from view"（4496:4551）↔ md 原句4 分析「档案法」✅

## 取证命令示例

/usr/bin/grep -c "The house had a blue door" notes/books/novels/odette-rising-by-julianne-edwards/text/ch04_chapter_4.txt → 1；退出码 0
/usr/bin/grep -c "rising at seven, leaving at eight, home at five" notes/books/novels/odette-rising-by-julianne-edwards/text/ch04_chapter_4.txt → 1；退出码 0
