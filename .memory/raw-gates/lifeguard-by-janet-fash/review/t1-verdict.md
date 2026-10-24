# T1 自检 · lifeguard-by-janet-fash

抽样章（先定后读）：**ch01、ch10、ch20** —— N=20，取 ceil(20/8)=3 章，最少 2、最多 6；首章 ch01 与末章 ch20 必含，第 3 章按等距取 ch10（(1+20)/2 附近）。

## 一、阻断型（全部已修并复验）

| # | 位置 | 改前 | 改后 | 原文依据 |
|---|---|---|---|---|
| 1 | ch11 原句2 关键词 | `swim test` | `the test / another assignment / couldn’t even swim` | 引语作 "Stein used the test"、"get them another assignment"、"couldn’t even swim"；`structure.py keywords` 判块内锚定为阻断项 |
| 2 | ch18 原句2 关键词 | `no recourse` | `any recourse` | 引语作 "without the lifeguards having any recourse" |
| 3 | ch18 原句11 关键词 | `a slap on the wrist` | `a slap on his wrist` | 引语作 "with barely a slap on **his** wrist"——worker 把习语改成了通用说法 |
| 4 | ch18 原句11 中文理解 | 挨了一记不痛不痒的**手掌** | 挨了一记不痛不痒的**巴掌** | 同上（slap = 巴掌，非「手掌」） |
| 5 | ch20 导航/总结 | 十九条图说明 | 十八条图说明 | 原文 `text/ch20_photographs.txt` 实数 18 条说明（另加标题行与摄影师网址） |
| 6 | ch02/ch03/概述/情感节点 | **姐弟俩** | **姐妹俩** | Janet 与 Helen 是两姐妹（ch02「把妹妹 Helen 拉进来」） |
| 7 | ch01/ch03/概述 | Barbara 是「**同龄偶像**」 | Barbara 是「**比她年长四岁的偶像**」 | ch01 原文 "she was four years older than me" |
| 8 | ch17 | 4 块（低于本书区间下限） | 补第 5 块（2006 年 Boris Braverman 在棚屋聚会被轮奸） | 原文章节重点被漏；补后 5 块回到本章建议区间 3–5 |
| 9 | 00_金句精选 / 00_情感节点 | 10 条引语丢了开头弯引号 | 全部 53 条引语与章节块**逐字节一致** | 用章节块引语集合做等值比对，非去标点比对 |

## 二、提示型（记录不修）

- ch20 引语 3 块 vs 本书中位 10：本章是图说明体（18 条说明），按篇幅比例 3 块合理，故不补。
- ch02「21 岁」、ch03「二十一岁」为推算值：ch01 明载 1974 年十五岁、四年后十九岁 ⇒ 1980/81 年二十一岁。
- ch05「三十六名救生员」原文作 "three dozen guards"；ch10「九十七街/九十四街」原文作 "97th to the 106th office" / "94th Street"；ch19「三十一年前」由原文 "in 1994" 推算；ch15「二十三万美元」原文作 "$230,000"；ch20「十八条」为原文段落实数。

## 三、工具侧发现（不记入 md）

- `scripts/chapter.sh` 对**不存在的文件**同样返回 rc=0（输出「已有章 md：0 / 引语块合计：0」）——若不自己核对文件存在，会提交一章空章。提交脚本已加存在性断言。
- `structure.py keywords` 的块内锚定比契约文字（「本块引语**或**本章原文」）更严；自建复验工具口径已改严对齐，否则同类缺陷会漏到门禁才暴露。

## 四、覆盖

- 机器层：gate.sh rc=0（0 阻断型）· 190 块逐字 190/190 · 总览引文 53/53 · structure.py order 20 md/190 块 0 缺陷 · anchor 凭空造词 0 · sweep_analysis_inline 逐字 682/❌0 · audit_numbers 不符 0（⚪不可机械核查 43 项已全部回原文核）· 抽查四脚本 rc=0。
- 件数对账：章节 md 20 == text/ 提取件 20，章号集合完全一致；总览 3 篇。
- 人判：①相对章号 5/5 · ②绝对断言 74/74 · ③年龄数字 259/259 · ⑥场景方位 6/6 全量读；⑤方向施受 42 抽 20、④亲属身份 32 抽 20（抽样 40 行全读）。另对全书分析层 207 个数字 token 做机械化逐个回原文核对（中文数字→英文拼写、序数词、金额、年份），残留 10 项全部逐条核实为「原文另有写法或可由已载事实推得」。
- 抽样章素读清单：ch01/ch10/ch20 复用 `production/chNN-suread.json`，suread.py 复验 rc=0，锚点全命中。
- 总览三篇全篇人判：概述 8 段梗概 + 3 主题 + 3 人物弧光，专名与数字全部回 `text/` 对账（仅书名/作者/出版社/年份来自版权页，已核）；金句 30 句 4 子项齐全、编号 ①–㉚ 连续唯一；情感节点 10 节点、2–3 句关键引语、章号标签覆盖 ch01–ch20 全 20 章。

**T1 为同会话自检，非异会话终审。**
