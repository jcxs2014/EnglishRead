# ch01 · R3 对账（漏 / 编 / 错）

- 对账基准：`1-suread.json`（R1 素读，独立代理，只读 `text/`）+ 本章 md + `text/ch01_prologue.txt`
- 逐字底稿：`2-machine.json`（R2 第二实现，verdict=ok；10 块 / 18 片段查无 0）
- 章名：Prologue（POV：Daniel /「Him」）

## 单子一：漏（素读有、md 无）

| R1 事实 | 判定 | 理由 / 落点 |
|---|---|---|
| 爆炸炸死了叙述者；爆炸后他没落在预想的地方 | 非漏 | 原句 1 |
| 房间：冰冷、无个性、全白；他「倒不是不感激」；缺的是「明显的永劫」 | 非漏 | 原句 1 |
| 第三个人是杀人犯，名字上过报纸，满口缺牙导致咬字含糊，坐在叙述者旁边 | 非漏 | 原句 4 |
| 第四人：蓬头垢面、先前拒绝自我介绍，盘腿坐在地上 | 非漏 | 原句 5 |
| **政客先说「Why keep the three of us waiting?」，随即改口「Why keep the four of us waiting?」并补一句「No offense, ma’am」** | **漏（提示型）** | md 原句 2 的读者视角提示把改口的前一态写成裸「我们」，**跳过了「three」这一步** ⇒ 不是缺内容，是「写成了错的那一步」，改法见单子三第 1 条 |
| 灰袍人凭空出现；四个人立即签字，叙述者只犹豫一瞬 | 非漏 | 原句 6、原句 10 |
| 灰袍人给的报酬＝永恒的舒适房间与定期餐食＋免受地狱折磨；「Employment」条款 | 非漏 | 原句 8 |

## 单子二：编（md 有、原文无）

| md 位置 | 断言 | 判定 | 依据 |
|---|---|---|---|
| （无） | — | 自建 §0.2 严口径扫描：分析层专名 ∉ 本块引语 4 处候选（Agency / Executive Suite / Inhuman Resources / Daniel），**全书查无 0**；逐条回原文核：Agency＝ch01:79 机构名；Executive Suite、Inhuman Resources ＝ ch26/ch29/ch18 等后文地名；Daniel ＝ 叙述者本名（后文才给出） | 无凭空生词 |

## 单子三：错（两边都有但不一致）

| 位置 | md 写法 | 原文 | 判定 |
|---|---|---|---|
| 原句 2 读者视角提示 | 「政客**第一句话只说「我们」**；等他稍后改口成「the four of us」」 | `text/ch01_prologue.txt:31` 逐字："Why keep the three of us waiting?" → `:37` 逐字："Why keep the four of us waiting?" | **阻断**：改口的前一态是「the **three** of us」，不是裸「我们」；「three」正是把那不报姓名的女人排除在外的那个 tell（他随即补「No offense, ma’am」） |
| 原句 10 读者视角提示 | 「他后来那句「我几乎为自己做的事感到庆幸」」 | 全书 grep：`/usr/bin/grep -rn "grateful" text/ch*.txt` → 8 处命中，**无一句是这个意思**；语义最近的一处是 `text/ch24_chapter_twenty_three.txt:127`："It was one of the few times in my existence when I was almost glad to do what I do."（是「几乎为自己**正在做的这份差事**感到高兴」，不是「为自己**做过的事**感到庆幸」）；`grep -rniE "for what i'?ve? done" text/ch*.txt` → 退出码 1（零命中） | **阻断**：引语指认不实——中文引语在原文中不存在，且未给章号，读者定位不到 |

## 本章结论

- 漏：1 条（阻断 0 · 提示型 1）
- 编：0 条
- 错：2 条（阻断 2）
- 本章阻断合计：**2**
