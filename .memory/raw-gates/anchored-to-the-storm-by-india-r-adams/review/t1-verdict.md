# T1 自检 verdict · anchored-to-the-storm-by-india-r-adams（2026-11-04）

抽样：**ch01 / ch06 / ch11 / ch15 / ch20**（20 章 × 1/4 = 5，等距含首末；先写入本行后开始读）。
方法：assertion_scan 350 行（①②③⑥ 全量 238 行、④⑤ 抽 42 行）+ 总览三篇全篇人判 + 抽样 5 章 suread 锚点复验（8/8·8/8·9/9·9/9·10/10 全命中）+ 事实回源 grep 4 条全命中 + 金句 25/25 唯一（Counter 去重核验）。

## 缺陷与整改（10 处，全部当场落地）

| # | 位置 | 改前 | 改后 | 原文依据 |
|---|---|---|---|---|
| 1 | 00_概述 梗概¶1 | 把他从医院"领养"走 | 把他从寄养家庭"领养"走 | text/ch04_west_one.txt:24 "A man was adopting our Johnny"（医院是十岁坠海后的事，ch08:126） |
| 2 | 00_概述 梗概¶7 | Sea-Dude（Karon） | Sea-Dude（Maddox 猜即 Karon） | text/ch17_east_nine.txt:388 "Karon. He must be the Sea-Dude."（原文为推测） |
| 3 | ch01 导航·叙事手法 | 结尾三个短段五词、十词、十六词 | 二十三词、十六词、六词 | text/ch01_east_one.txt:449/453/456 逐词实测 |
| 4 | ch06 原句5·为什么这样写 | 六位数密码 | 四位密码 | text/ch06_west_three.txt:123 "Zero-four-nine-nine"＝4 位 |
| 5 | ch09 原句12·为什么这样写 | 答案只有十个词 | 答案只有八个词 | text/ch09_east_six.txt:347 "From the bomb attached to a bridge's pillar."＝8 词 |
| 6 | ch17 原句10·读者视角提示 | 纠正了他八年的认知 | 纠正了他自以为孤身流亡的认知 | Weathers 收留时长原文无"八年"之据（八年属 ch08 放逐线） |
| 7 | ch19 原句11·为什么这样写 | 遗焗 | 遗嘱 | 错字 |
| 8 | ch18 原句1·中文理解 | 父亲让 Gage 互相残杀 | 父亲逼他与别的无辜孩子对打 | text/ch18_west_nine.txt:18 "fight another innocent" |
| 9 | 金句① 呼应关系 | 'age ten'在 ⑯（ch10 车祸账）…兑现 | 在 ch02 的枪声记忆与 ch08 的'十岁死期'对账时兑现 | ⑯=ch10.8 与 age ten 无关（编号漂移）；实际兑现点是 ch02 块4/ch08 |
| 10 | 金句⑤ 呼应关系 | ch15 他回咬出第二个符号（Sarah 在 ch20 亲眼擦洗） | ch17 咬痕已愈合为同样神秘符号；ch20 胸前前所未见新符 | text/ch17_east_nine.txt:145 + text/ch20_west_ten.txt:299（胸前符非"回咬"产物） |

（金句㉒"与 ⑭⑰ 构成书名三部曲"复核为原文即正确，未改。）

## 收尾核验

- 修复后整书 gate.sh EXIT=0（0 条阻断型）。
- 总览三篇：verify_overview_quotes 50/50（100%）；金句唯一数 25/25；节点 17 条引语逐字回查通过；中文叙述断言按六类回源（概述 7 段逐段对 text/ 核）。
- 读了哪些候选行、共几行：t1-candidates.txt 全档 350 行——①相对章号 8 行全读、②绝对断言 81 行全读、③年龄数字 146 行全读、⑥场景方位 3 行全读、④亲属身份 60 行抽 22 行、⑤方向施受 38 行抽 20 行。
- ⚠️ 本 T1 为**同会话自检**（写作方自查，非异会话审查）；按规程此项不写作"已通过审查"。
