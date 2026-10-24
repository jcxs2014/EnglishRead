# ch10 Tabula Rasa — 判定（R5）

- 机器层：`bash scripts/chapter.sh "…/ch10 tabula rasa.md" --json` → **rc=0**，verdict=ok，块数 3、words 691、segments 3、查无 0、空引号 0、子项缺 0、关键词缺 0、形态偏离 0，`issues` 全空。
- 素读锚点：8/8 命中（`facts= 8 bad= 0`）。
- 报数：**逐字 0 / 对应 0 / 形态 0 / 断言 0 阻断、4 提示**——漏 2、编 0、错 2。

## 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 漏：他旧日的口味（摇滚／rockabilly／英伦入侵／朋克／早期乡村／Dylan）全无 | `text/ch10_tabula_rasa.txt:38` “I used to listen mostly to rock and roll. I liked rockabilly, but I liked a lot of other stuff, too: British Invasion bands, punk, early country music, Dylan.” | `grep -c -F "rockabilly"` 与 `"Dylan"` 对 md 均为 **0**；`grep -nE "摇滚\|朋克\|乡村"` 零命中、退出码 **1**。:11 只有「无意间成了学徒」 | 提示 |
| 漏：收藏名单（Riley／Glass／Pärt／Oliveros／Reich → 勋伯格／贝尔格／韦伯恩 → Tallis）全无 | `:68` “spending whole days listening to Terry Riley, Philip Glass, Arvo Pärt, Pauline Oliveros, Steve Reich, and then skipping backward to Schoenberg, Berg, Webern, then early composers like Thomas Tallis.” | 七个名字 `grep -c -F` 全为 **0**；:11 只「极简主义与更早的作曲家」；词汇表未收任何一个 | 提示 |
| 编：md :13「他却在其中放松下来」 | `:63` “I surprised myself: I realized that I liked it, a lot.”；全章 `grep -nE "relax\|settle"` 零命中、退出码 **1** | 原文无「放松」，只有「很喜欢」；属引申不属新事实，故不判编 | 提示 |
| 错：md :15「写声音时句子被……推长，写身份崩塌时反而短促」 | 实测（Python 按 `. ! ? ”` 切句计词）：`:33` 身份段 7 句／均值 **16.7**／最长 29；`:47` 声音段 7 句／均值 **8.4**／最长 23 | 方向与实测**相反**；成立的只有「分号把音色串成一句」，最短句在 :78–79 的收尾 | 提示（形态·文风断言） |
| 8 条素读事实 | `1-suread.json`，逐条整串比对 `bad= 0` | 无漏无编的大项 | 假红（核后成立） |
| 12 条词汇例句 | 脚本整串比对 `rows=12 miss=0` | 逐字无误，未跨章 | 假红（核后成立） |
| 3 块 R4 对应 | `3-diff.md` 第四节 | 三问全过；块 1 的铺垫句取自 :23，已在表内注明 | 假红（核后成立） |
| 负向断言「Alba 没说过一句关于写作的话」 | 她的台词仅 4 处：`:47` “You probably won’t like it.”、`:48` “So?”、`:57–58` “La Monte Young… What did you make of it?”、`:67` “Oh, yeah.”；`:43`／`:53` 两句是 Zach 的 | 断言成立，未把 Zach 的话记到她名下 | 假红（核后成立） |
| 抬头 `Alba is 24, Zach is 24` | `:18` “Saturday, October 25, 2025 (Zach is 24, Alba is 24)” | 原书原文，且与 ch09（23/24）自洽；md 未据本章年龄外推，`grep -nE "42\|四十二"` 零命中、退出码 **1** | 假红（按派工方口径延伸） |

## 处置建议（只报不改）

1. `:11` 补两个短句即可同时消掉 L1 与 L2 的一半：「他从前只听摇滚（rockabilly、朋克、Dylan），是她把她父亲的音响架进客厅，他才开始听极简主义——La Monte Young、Terry Riley、Philip Glass，一路往回听到勋伯格与 Tallis」。名字取三个即够，不必全列。
2. `:13` 删「他却在其中放松下来」，改为「他意外地发现自己很喜欢」。
3. `:15` 把「写声音时句子推长／写身份崩塌时短促」改为「写声音时用分号把整段音色装进一个句子；写身份时反而拆成短句收束」，或直接引用 :78–79 的四个短句作对照。

## 已核实为正确

- **日期／年龄**：`:18` “Saturday, October 25, 2025 (Zach is 24, Alba is 24)”；2025-10-25 确为周六；md :11／:80 一致，本章「我」判给 Zach 正确（:15）。
- **曲名＋年份**：`:57` “La Monte Young, Trio for Strings. It’s from 1958.”；md 未写错作曲家、未把 1958 写成别年。
- **ground zero 与标题**：`:57` “It’s kind of ground zero for minimalism.” 与标题 tabula rasa（:13「擦净的书写板」）分属两处，md 未混用。
- **停笔的三层原因**：`:33` 怕笔记本落到别人手里（外部风险）；`:73` uncertainty 与「为别人的认可而写」（内部）。md :11／:12 分层处理，未把「怕」写成「倦」。
- **「她是被听见的人」**：`:68` “She would answer questions if I asked, but mostly we listened together”；`:58` “What did you make of it?”。:14 的判断有原文支撑。
- **12 条词汇**：全部落本章（`miss=0`），`accidently` 的拼写问题已在释义中注明「原文拼写如此」（`:38` 原文确为 accidently）。
- **本子的位置**：`:28` “My notebook is under the nightstand.”；:27「本子放在地板附近，是随手塞进去的」与原文不冲突（under 表下方，未写成「抽屉里」）。
- **未越界**：全章未出现 ch06 的 `Alba is 42`，md 无年龄推算。
