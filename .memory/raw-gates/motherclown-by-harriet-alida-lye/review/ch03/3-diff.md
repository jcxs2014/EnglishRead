# ch03 · R3 对账（Chapter Two，md：`ch03 chapter two the colour blue.md` / 原文 `text/ch03_chapter_two.txt`，43,561+ 字符 / 7,744 词）

R1 事实 8 条（独立子代理，锚点 8/8 唯一命中）。

## 漏（素读有、md 无）

| # | 素读事实 | 原文区间 | md 位置 | 判 |
|---|---|---|---|---|
| L1 | 住处没装窗帘、天亮即醒 | 35–88 | 原句 1 收了「婊子澡」与八层楼，未收窗帘 | 提示（细节） |
| L2 | 洗碗时女儿说信封写的是「去巴黎、当小丑」 | 5950–6014 | 原句 4 直接进到「问题是她想离开我」，未写触发场面 | 提示：信封内容在 ch02 已交代，ch03 收后续心理，取舍成立 |
| L3 | 女儿第一个词是 dada，早于 mama，即最亲爸爸 | 9592–9650 | 无 | 提示（亲子关系细节，md 未用，不构成缺漏） |
| L4 | 她已五周没见女儿 | 17060–17112 | 无 | 提示（数字，ch02 出过同一数字） |
| L5 | 课程每天十小时、每周五天 | 33063–33111 | 原句 13 只收「blue 不是 a blue thing」，未收课时 | 提示（数字细节） |

## 编（md 有、原文无）

| # | md 表述 | 原文核查 | 判 |
|---|---|---|---|
| F1 | 原句 11 分析「她刚宣布要去的城市，是**她十九岁没能去成的地方**」 | `grep -n -i "nineteen" text/ch03_chapter_two.txt` → 0 命中（退出码 1）。全书中 Catherine 的「十九岁」只出现在 ch16（`“I was nineteen.”` 讲怀孕）与 ch21（十九岁被以甜美居高临下的态度对待），**都不是「没去成巴黎」** | **阻断**：把后期章节的信息提前且改写 → 已改为「她刚宣布要去的那个城市，在欧洲——那是她一辈子没去过的地方」（据 ch05 `Europe was always for other people`） |

## 错（两边都有但不一致）

| # | md 表述 | 原文 | 判 |
|---|---|---|---|
| — | 未发现。「Common 八层楼」「ell e 十一平」类细节与原文一致；「下一句立刻说它让她恐惧」经核成立（`The question wasn’t rhetorical—it terrified her.`） | — | 通过 |

## 已核实（本章易被误判的两处）

| md 说法 | 原文 | 结论 |
|---|---|---|
| 「最后那句疑问不是修辞，下一句立刻说它让她恐惧」 | `text/ch03_chapter_two.txt:269` `The question wasn’t rhetorical—it terrified her.` | 成立 |
| 「Tomas 说我们不是成为蓝的东西，而是成为蓝」 | 原句 13 `We be blue, not a blue thing.` | 成立（`be the thing` 的 the 曾在生产期漏掉，已修） |

取证：`/usr/bin/grep -n -m3 "nineteen" text/ch03_chapter_two.txt` → 无输出，退出码 1；`/usr/bin/grep -n -A2 "perfect thing" text/ch03_chapter_two.txt` → 269 行含 `terrified her`。
