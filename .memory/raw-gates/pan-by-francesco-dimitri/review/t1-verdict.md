抽样章号（动手前写定）：ch01 / ch05 / ch09 / ch13 / ch17 / ch21 / ch25 / ch30 —— 30 章按 1/4 抽 8 章，首末必含，其余等距（1,5,9,13,17,21,25,30）。
另加：总览三篇全篇人判；assertion_scan 643 行候选全读（六类：①相对章号 28 ②绝对断言 161 ③年龄数字 273 ⑥场景方位 11 ⑤方向施受 76 ④亲属身份 94）。

| # | 位置 | 改前 | 改后 | 原文依据 |
|---|---|---|---|---|
| 1 | 00_金句精选.md 全 30 条 | `**呼应关系**：呼应关系：…` | 单前缀 | 形态缺陷（脚本拼接重复），无原文 |
| 2 | 00_金句精选.md #24 上下文 | 「Renzo 帮家里跑腿挣到一点钱」 | 「Michele 帮家里跑腿…」 | ch02: `fucking Renzo` 是 Luca 的弟弟，不是 Michele 家人 |
| 3 | 00_情感节点.md:26 | 「Renzo 一家在贫困里挣扎」 | 「Michele 一家…」 | 同上 |
| 4 | 00_概述.md 末夜段 | 「四个孩子轮流揍他，Giada 落下第一拳」 | 「Giovanni 先动手，Wendy 一拳打胃，Giada 最后补上」 | ch29 XXXII: `“Hold still,” says Giovanni…punches him` / `punches him in the stomach` / `“You already had one,” complains Giada. “I haven’t.”` |
| 5 | 00_概述.md 人物弧光 Giovanni | 「最后被 Giada 拦住，不必殉葬」 | 飞舟锚绳旁欲与海盗同焚，Giada 点破「你只是想再逃一次」，他活下来，回城清点家产、起诉 Dal Mare 诽谤 | ch29:1144-1195 `“I wanted to die doing the right thing.”` / `“You’ll get plenty of chances before the night is over.”`；ch30:159-165 |
| 6 | 00_金句精选.md #9 上下文 | 「Giovanni 在旧论文里找到」 | 「Michele 读父亲的黑笔记本」 | ch09:108（黑笔记本、Horned God/Diana/Artemis 交替大写） |
| 7 | 00_金句精选.md #9 中文理解 | 「以缩写出现」 | 「交替称作 Diana 或 Artemis」 | ch09 原文 `referred to interchangeably` |
| 8 | 00_金句精选.md #22 上下文 | 「众人追问飞行原理」 | 「Wendy 与 Giada 沙滩做爱后初次飞起，Tinker Bell 在地上给的答案」 | ch21:609-612 |
| 9 | 00_金句精选.md #24 呼应 | 「Asphalt 与 Car 的婚礼」 | 「Asphalt 与 Car 的快速交配、Traffic 在旁起舞」 | ch14:281 |
| 10 | 00_金句精选.md #26 呼应 | 「第 29 章那把『书是疫苗』的政策」 | 「第 26 章十项管控与焚书之夜」 | 疫苗论见 ch25:399；政策与焚书见 ch26 |
| 11 | 00_金句精选.md #13 中文理解 | 截断「失去……」 | 「失去灵魂——也只能这么说」 | ch12 原句 |
| 12 | 00_金句精选.md #1 / #30 | `Michelle` / 「树精」 | `Michele` / 「萨堤尔」 | 全书人名与 ch30 原文 `the satyr` |
| 13 | 00_情感节点.md 节点六标题 | 「十七年的信」 | 「十七封信，1975–2012」 | ch15 十七封信跨 1975–2012 |
| 14 | 00_概述.md / 00_情感节点.md | 「失去了母亲这一辈最后的保护者」 | 「失去了 Luisa 与导师 Irene」 | 章内死者是 Luisa（ch19）与 Irene（ch20），非「上一辈全体」 |
| 15 | 00_概述.md 主题一 | 「第 21 章 Tinker Bell 说神诞生于众人的狂欢」 | 「Tinker Bell 用精灵断代史说明人类不再相信、戏法仍在只是没人知道往哪看」 | ch21:93 |
| 16 | ch25 lupercalia.md:9 | 「Giada 在罗马中央图书馆查到」 | 「Giada 在图书馆里查到」 | ch25 原文只写 `the library`，未写 central |

处置与判定：
- 阻断 16 处全部就地修复（总览层 15、章层 1），修复后 `chapter.sh` ch25 rc=0、`gate.sh` 复跑 EXIT=0。
- 章层缺陷 1 处 / 已读 8 章 = 密度 0.125 < 0.2，本可停；但阻断总数 ≥3，按 §6.1 自动进 T2 断言全扫：643/643 行候选逐行回源，另修 2 条上下文误置（#6、#8），T2 后残留 0。
- 抽样 8 章 suread 全部 rc=0；事实回源抽查通过（ch09 `one-page article`、ch13 `Adamaria`、ch17 `Baddy Long Legs`、ch21 `Tito the saxophonist`、ch25 电子卡进图书馆、ch30 出院/沙发/Pineto 清算）。
- 未做：无（T1 三件产物齐全：本文件 + t1-candidates.txt 657 行 + 台账一行）。
- 说明：T1 为同会话自检，非异会话复核。
