# T1 自检 · a-labyrinth-of-honeybees-by-fawcett-heather（同会话自检，非验收）

抽样章（先定后读）：**ch01 · ch06**。理由：N=6 → ceil(6/8)=1 → 下限 2 章 → 首章与末章必含，其余等距无需补位。
总览三篇：本体裁 short-story-anthologies 无总览（overview=0，gate ⑭⑮ 均报「不适用」）⇒ 第 2 步空过。
候选行读取范围：`t1-candidates.txt` 全 76 行候选（① 1 行 / ② 18 行 / ③ 46 行 / ④ 4 行 / ⑤ 7 行）；①②③⑥ 读全量，④⑤ 各 7 行（<20，故全读）。

## 一、修掉的缺陷（3 条；均非「谁做的」类，机器层已能被部分抓到）

1. 位置 `ch01 the royal inquisitor.md:33`
 改前「**十几张**人脸在审问官脸上飞快掠过」
 改后「**十二张**人脸在审问官脸上飞快掠过」
 依据 `text/ch01_the_royal_inquisitor.txt:23`「The faces of a dozen people flitted across the royal inquisitor’s」——dozen＝十二；原文随后 escalate 到 Two dozen faces. A hundred.
 性质：数字断言误译（③ 桶命中行）。`chapter.sh` 改后 rc=0。

2. 位置 `ch04 the balcony.md:10`（导航一句话概括）
 改前「他的手下骑马闯迷宫被飞马掀翻，**三个人一死一逃**」
 改后「他的手下骑马闯迷宫被飞马掀翻，**两个人先后死在迷宫里，最后一个仆人带着飞马逃走**」
 依据 `text/ch04_the_balcony.txt:39`「whatever that had killed **two of his men**」＋`:31`「the inquisitor’s remaining servant … he and his pegasus were gone」（同文件 `:86` 一句话总结原本已写「两个人先后死去、一个逃走」，导航与总结自相矛盾，本次统一为总结的版本）。
 性质：可数断言＋同文件互斥。`chapter.sh` 改后 rc=0。

3. 位置 `ch06 farewell.md:19` 关键词栏 `hate me till my last breath` → `hate me till his last breath`
 依据 本块引语原文「still I knew that he would hate me till **his** last breath」。
 性质：笔误导致关键词不在引语内——`gate.sh` ⑱ 曾判**阻断**，已修并复跑 rc=0。

（另有 2 条提示型已修：`ch05:153` 行内英文 `fall back towards the floor` → 逐字 `fell back towards the floor`（gate ⑩ 🟠 部分命中 → 修后 0）；ch05 原句 10 引语曾跨段跳句拼接被 `chapter.sh` 判查无，补回中间句后连续。）

## 二、抽样章素读复核（第 4 步）

- `ch01-suread.json` 9 条锚点、`ch06-suread.json` 8 条锚点——`suread.py --check` 全部 ✅ 命中，0 查无。
- 回源抽验 3 条：ch01「The king has sent me to investigate the deaths of two of his tax collectors」(`text/ch01:37`)；ch01「Their bodies were found in the Blue River」(`text/ch01:79`)；ch06「he would hate me till his last breath」(`text/ch06:5`)——与事实条目一致。
- 引语块原文邻域：ch01 第 2 块（`text/ch01:23` 幻象段）确认引语止于 `amusement or boredom`、未越界；ch06 三块邻域（`:5`／`:16`／`:19`）确认无跳句、无跨段拼接。

## 三、六类判定（一句话总结 6 条）

ch01 相符（鬼魂随行 `:13`／自称 groundskeeper `:49`）· ch02 相符（国王派女儿来查税吏、「She never returned」`:103`；三条岔路 `:81`）· ch03 相符（家＝神庙、园子；蜂蜜罐）· ch04 **已修**（见上 §1.2）· ch05 相符（国王下令烧园 `:3`；派刺客杀自己税吏栽赃 `:62`）· ch06 相符。
→ 阻断合计 **0 条**（<3）⇒ **不进 T2**。

## 四、保留的非阻断提示（记审查表）

- 块数分布：ch02=8、ch05=10 与本书中位 3 相差大（`structure.py audit` ⚠️ 2 条）。判定保留：bookform 契约对 2,400–4,500 词给 6–12 块，长篇按 epub 场景切块属常态，本书形态范围 3–10 由 chapter.sh 认可。
- ch03 块数 6 超出 chapter.sh 启发式区间 3–5（契约给 4–6）——保留，两套区间本身冲突。
- gate ⑪ 结构缺陷 0、⑲ 中文层阻断 0、④ corruption_scan 0。
