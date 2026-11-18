# T1 自检 · odette-rising-by-julianne-edwards（2026-11-18）

抽样章（先定后读，9/36＝1/4，含首末章）：**ch01, ch05, ch10, ch14, ch18, ch22, ch26, ch31, ch36**。
方法：assertion_scan 六类全量产出（699 行）→ ①相对章号 43 行全读；②③④⑥ 按类抽查＋全部 00_* 总览层逐条回源；⑤ 抽 8 行；
抽样章复用素读清单（suread --check 9/9 锚点全中）；金句 25 条唯一性 Counter 核验＋呼应圈码逐条回查。
缺陷密度：① 类在 20+ 章的导航/分析层出 11 条阻断（≥0.5）→ 按规则自动进 T2 断言全扫（同因类跨 ≥2 章）；
T2 范围＝①全量 + ②③④⑤⑥ 总览层/数字/亲属逐条回源（15/15 ✅）。

## 修复清单（13 条阻断，全部复绿）

| 位置 | 改前 | 改后 | 原文依据 |
|---|---|---|---|
| ch13:125 | 「下一章的烟与沙拉就是收据」 | 「话音未落，烟与沙拉就是收据」 | 烟蒂事件发生在本章（ch13 原句12） |
| ch13:135 | 「下一章见面时的气氛」 | 「两人下次见面的气氛（ch19 的茶会）」 | Berthe 下次现身是 ch19（非 ch14） |
| ch14:43 | 「上一章她刚被那幅画击中」 | 「ch12 到访时她刚被那幅画击中」 | Cassatt 画在 ch12（Feld 二访） |
| ch17:12 | 「上一章的仇人成为本章的恩人」 | 「Le Neptune 的仇人成为本章的恩人」 | 沙拉烟蒂在 ch13，非 ch16 |
| ch17:176 | 「上一章把烟摁进她沙拉的女人」 | 「Le Neptune 那晚把烟摁进她沙拉的女人」 | 同上 |
| ch24:55 | 「是下一章的伏笔」 | 「这个悬念随他的背影悬置」 | ch25 未写安葬去处的兑现 |
| ch25:125 | 「下一章起，她要造的不是房子」 | 「此后她要造的不是房子」 | 重建决策在本章，动工在 ch30 |
| ch31:33 | 「第三条路（下一章的解法）」 | 「第三条路（后面的解法）」 | 解法在 ch34，非 ch32 |
| ch35:9 | 「携丧子之痛的儿子」 | 「携丧母之痛的儿子」 | 亡者为妻/母（Beauclerc 丧妻、Joseph 丧母） |
| 00_概述:10 | 「二十岁的 Odette Huré」 | 「十年没出过家门的 Odette Huré」 | 章内仅 ch11 "I am twenty-one years old"；ch01 无年龄依据 |
| 00_概述:22 | 「扛了二十年的羞耻」 | 「扛了二十余年的羞耻」 | ch21 "obese twenty-two-year-old"；Dendron "Twenty-one years" |
| 00_概述:46 | 「Lionesses kill their tamers」 | 「Lionesses have a habit of killing their tamers」 | ch23 逐字原句（verify_overview_quotes 抓） |
| ch20:43 | 「1897 年真实的 Bazar de la Charité 惨案织进衣料」 | 「1897 年巴黎慈善义卖大火（Bazar de la Charité）的影子织进衣料」 | 原文仅 "a fashionable charity market"，未点名（分析措辞降格为影射） |

另两处同因类早批修复（本轮 ① 扫描前已提交）：ch19 shimmering 例句（ch17 句误植）→ ch19 "as if under a spell"；
ch28 prig 例句（ch27 句误植）→ ch28 dizzyingly；ch22 词头 fared→fare（A 类词形）。

## 总览三篇人判（六类）

- ①相对章号：00_* 无「上一章/下一章」式相对指认 ✅（全部使用绝对章号）。
- ②绝对断言：概述 8 段梗概逐条回源 ✅（工厂 Rue Brancas／巴黎房产 Six Rue Jean Bart／蓝门／Gagnon＝匿名结账人／charade／Elizabeth Perkins／Avenue Gabriel，均在 text/ 命中）。
- ③年龄数字：二十余年（Dendron "Twenty-one years"＋ch21 "twenty-two"）✅；「百人合唱」「132 souls」未进总览叙述 ✅。
- ④亲属身份：生母＝来访英国女仆 Elizabeth Perkins（ch23 Ned＋ch28 相片）；Berthe 姐姐 Grace（ch28）；Merry 仅母亲在 Avenue Gabriel（ch11）——全部 text/ 支撑 ✅。
- ⑤方向施受：Gagnon 结账（ch30 揭底）、Polo Merry→Odette→Nanette→Merry（ch02→31→36）、大衣 Feld→Merry（ch12→14）方向全对 ✅。
- ⑥场景方位：Le Neptune／Rue Jean Bart／Saint-Cloud 猎舍／Castel Odette 均在 text/ 命中 ✅。

## 候选行读量

t1-candidates.txt 共 699 行（①43＋②219＋③205＋④178＋⑤27＋⑥13＋头部）。
已读：① 43/43 全量；②③④⑤⑥ 总览层全部命中行＋各类抽样（④ 抽 20、⑤ 抽 8、⑥ 全量 13）；合计精读约 120 行＋概述三篇全篇两遍。

## 结论

T1 为同会话自检（非验收）：阻断 13 条全修复复绿；同因类（导航层相对章号）跨 ≥2 章触发 T2 断言全扫，
T2 总览层/数字/亲属回源 15/15 ✅。金句 25 条唯一（Counter 核验）、呼应圈码 25/25 对位、
总览引语 verify 15/15＋24/24＋情感节点全中。gate EXIT=0（382/382 引文 100%、38/38 干净文件）。
T3 深审未做（待用户发起）。
