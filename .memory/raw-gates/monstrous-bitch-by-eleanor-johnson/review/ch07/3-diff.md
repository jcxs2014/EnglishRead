# ch07 对账（R3）

素读：`1-suread.json`（8 条，全部带 `text/ch07_5_the_season_of_the_witch_dramatically_.txt:行` + 逐字 + 字符区间，子代理已脚本校验 `count==1`）。
机器：`2-machine.json`（rc=0，15 块，引语 15 段全 ok，空引号 0，子项齐全，中文密度合格）。
md 286 行，15 块 + 词汇 26 条。原文 272 行 / 40,476 字符（去空白，实算一致）。

## 一、漏（素读有、md 无）

无。素读 8 条全部有落点：

| 素读事实 | md 落点 |
|---|---|
| L20 十七世纪剧作家推动终结「女性＝女巫」妖魔化 | 原句 1、概览 L18、结构列表 1 |
| L27《麦克白》三女巫分说/接话/齐声＝triune 不圣三位一体 | 原句 2、结构列表 2 |
| L115 女巫之力来自古典月神 witch-bitch 而非撒旦 | 原句 6、结构列表 7 |
| L123 米德尔顿《女巫》(1616) 赫卡忒是极老人类女人 | 概览 L18、结构列表 7 |
| L141 剧中女巫未被处死/未受审，因提供社会服务 | 原句 8、结构列表 9 |
| L149 1621 埃德蒙顿寡妇 Elizabeth Sawyer 被审定罪处死 | 概览 L18、原句 9 |
| L216 Hutchinson 1706 写成、1718 出版 | 概览 L18、结构列表 12 |
| L225 16 世纪以来 countless thousands 女性无充分证据被处死 | 概览 L18、结构列表 14 |

## 二、编（md 有、原文无）

无。逐条核过：

- 「十四岁的弗朗西丝·霍华德／十三岁的埃塞克斯第三伯爵罗伯特·德弗鲁克斯／从未圆房」←「In 1604, a **fourteen-year-old** girl named **Frances Howard** was married to a **thirteen-year-old** boy named **Robert Devereux, 3rd Earl of Essex**… they apparently **never consummated** the marriage」
- 「1736 年英国非罪化」←「**In 1736, King George decriminalized witchcraft in Great Britain**」
- 「迫害自 1650 年前后起收敛」←「The most intensive period of witch persecution throughout Europe **began to taper in about 1650**」
- 「米德尔顿《女巫》1616」←「**Thomas Middleton, The Witch (1616)**」
- 「1706 写、1718 出版」←「**In 1706, Hutchinson wrote** his own refutation … **In 1718, he finally published** his work: An Historical Essay Concerning Witchcraft」
- 「用臀部乳头给撒旦之狗哺乳，所以她被处死」←「sealing the pact by allowing the dog to **suck her blood from her rump nipple**… **Rump-nipple wet-nursing a Satan-dog was not an appropriate behavior for a seventeenth-century English Christian woman, so she was executed**」（因果是原文自己的）
- 「拉玛什图早已闯进她家，杀掉了她的婴儿」←「**Lamashtu has entered into her home, killed her baby**」

## 三、错（两边都有但不一致）

无。逐块比对未发现主语、因果、数字或时序上的不一致。

## 四、本文件读过的候选行

`assertion_scan.py` 对 ch07 报出的行全部人读（①相对章号、②绝对断言、③数字、④亲属、⑤方向）；另对 `Frances Howard／Devereux／1604／fourteen／thirteen／1736／1650／Middleton／1616／1706／1718／triune／executed／killed her baby` 十五个关键串做了定位（脚本在 `/tmp/t3mb/`）。
