# T1 自检 · chasing-kaylee-kringle-by-codi-hall（2026-11-06，同会话自检）

抽样章号（**先定后读**，按 54 章 → 1/5 且 ≥10 章，首末必含，等距每 5 章取一）：
ch00, ch05, ch10, ch15, ch20, ch25, ch30, ch35, ch40, ch45, ch50, ch53 —— 共 12 章（22% > 1/5）。
抽样理由：首章 ch00 定全书语气与反派装置，末章 ch53 覆盖所有支线收束；中间等距覆盖三 POV（Kaylee / Rick / Ansel 插章 ch27 系列在 ch25–50 区间被 ch30/ch45/ch50 间接覆盖）。

## 一、抽样 12 章逐章结论（机器层 + 断言层）
查询方式：`/usr/bin/grep -c "<原文锚点>" text/chNN_*.txt`（命中数均 ≥1），已核项列于下。

- ch00：3 块；「near the Utah border」1 ✓（Holiday 位置断言成立）；无人物关系断言。
- ch05：5 块；「agent for less than a year」1 ✓、「three weeks of vacation」1 ✓（Rick 资历与假期两个数字断言均成立）；「Ansel Atkinson」2 ✓（反派全名首次出现）。
- ch10：8 块；「daily facial recognition search」1 ✓（chapter 内追踪手段自述与 ch00 监控室设定一致）。
- ch15：8 块；「twenty feet tall」1 ✓（土豆雕像高度断言）、「Darigold」1 ✓（蛋奶酒品牌断言）。
- ch20：5 块；「four-bedroom」1 ✓（Marianne 家房型）；「Will Rappaport」1 ✓（书友会唯一男性成员，且在 ch21 才有其全名，ch20 未误称）。
- ch25：8 块；「four children」1 ✓（Rick 排行叙述）、「doing donuts」1 ✓（少年时期对照）。
- ch30：7 块；「thirty books」1 ✓（Ice Planet Barbarians 系列长度断言）。
- ch35：7 块；「case of champagne」1 ✓（他带酒赴会）。
- ch40：9 块；「cheer coach and history teacher」1 ✓（Ashlee 身份）；「fornicating reindeer」装饰细节回源 ✓。
- ch45：9 块；「He found two and flushed those」1 ✓（三只窃听器 = 灯里 1 + 探测器 2，与我写的「拆掉三只」一致）。
- ch50：10 块；「Ahalf dozen government SUVs」1 ✓（六辆车，原书缺空格照录）。
- ch53：10 块；「eight-week courses」1 ✓、「last four classes」1 ✓（学业收束的两个数字）。

结论：12/12 章机器层无阻断，抽查的 16 条数字/身份类断言全部回源命中；未发现指认错人或数字无据。

## 二、总览三篇人判（全篇）
- `00_概述.md`：10 条引语，`overview.py quotes` 10/10 ✅。人读核对：梗概 7 段按「逃亡→猎人→拉锯→清单→反派→镇民战争→留下」推进，与章节顺序一致；三人弧光各一段，均无「谁做了什么」错置（逐条回 text 核过 Kaylee Marie Taylor / Elasia Gutierrez / Wyatt Gipson / Ansel Atkinson 四人关系）。
- `00_金句精选.md`：25 条（圈码①–㉕），块引用格式；`labels` 层 25/25 逐字 ✅、`quotes` 18/18 ✅（短句 <20 字母按工具口径跳过）、无重复文本（Counter 核）。
- `00_情感节点.md`：10 节点、17 条引语，`quotes` 17/17 ✅；节点章号与叙述对应（ch00/ch04/ch17/ch23/ch20/ch21-22/ch29/ch41-44/ch46-48/ch51-53）。
- 「呼应关系」中的圈码引用已逐条回查目标（①↔⑮、②↔③↔⑳、⑨↔⑩、⑪↔⑤、⑯↔㉔、㉑↔㉒、㉓↔⑦），未发现指向错位。

## 三、assertion_scan 六类预筛
`assertion_scan.py` 全量输出 539 行 / 57 文件，原文见 `t1-candidates.txt`。
- ①②③⑥ 读全量（本次逐类扫过）：数字/年数类 82 行、相对章号 100 行、唯一/最 167 行；均按「能指到原文才保留」处理。
- ④⑤ 各抽 20 行：亲属身份类 12 行全读（`Ansel 父亲 Folsom` / `Rick 母亲 indifferent` / `Kaylee 父母` 三组均回源 ✓）。
- 未发现需要改稿的阻断项；`唯一/最` 类命中多为评析性修辞（如「最有效的一句道歉」），按分级从宽处理，不改。

## 四、数字化/事实类改动的回灌检查
本轮写作期未发生「章内改数字后总览未同步」的情形（全书写成后总览才写）。已 `grep` 总览三篇核过的关键数字：两年（逃亡时长）、三十三人、一千五百人、十九项清单、两处「三周」——中英两处一致。

## 五、素读清单复用
ch00–ch53 共 54 份 `production/chNN-suread.json` 全部存在（ch24 曾因锚点大小写不符补跑）；抽样章 ch00/ch05/ch10/ch15/ch20/ch25/ch30/ch35/ch40/ch45/ch50/ch53 的素读锚点回源复核均命中，未见「只写开头的章」。

## 结论
T1 同会话自检：抽样 12/54 章（22%），总览三篇全篇人判，assertion_scan 全量扫过，**阻断 0 条**（提示级若干：模板/评析性修辞按从宽处理）。
缺陷密度 0/12 < 0.2，按 §6.1 不再扩样；未触发 T2（0 条阻断，无同成因类跨 2 章）。
**声明：本 T1 为同会话自检，不构成「已通过审查」；T3 深审未做（待用户发起）。**
