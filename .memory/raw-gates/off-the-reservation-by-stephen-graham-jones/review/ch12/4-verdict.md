# ch12 4-verdict（R4 逐块 + R5 判定）

R2 机器层：2-machine.json rc=0，10 块 10 引语，issues 全空。
R4 人判：10/10 块逐对核 + 施事三问。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 块2「ch04 里那套 Indian Evel Knievel 戏服」跨章指认 | text/ch04:71 戏称原文 + 行86「pale-white jumpsuit stapled flat」 | 有据 | 已核实为正确 |
| 素读#2「丢骨 Crow 地盘」计划未入块 | 素读 anchor 命中 True | 人物内心计划，与 ch19 强呼应，值得补记 | 提示（建议修，本轮不改稿） |
| 素读#1「步行一周」未入块 | 1200 英里已在词汇例句 | 计划细节 | 提示（不修） |
| 块5「干土」与 ch09 墓穴的连接 | text 引语「dry dirt crumbled out」；ch09 挖骨现场 | md 解读（骨粉→附身载体）与 ch11→ch12 因果链一致 | 已核实为正确 |

取证命令记录：
- `/usr/bin/grep -in "Evel Knievel\|stuntman outfit\|jump suit\|jumpsuit" text/ch04_3_pretty_good_for_an_indian.txt` → 行71/86/95；退出码 0
- `/usr/bin/grep -in "sterile and barren at twelve" text/ch06_5_never_without_teeth.txt`（前章 T1 补充证据，此处仅引用结论）
- `/usr/bin/grep -c "excommunicated from the hospital" text/ch03…`（例句抽查法同前章）

## 已核实为正确

- 块7 的驾驶决策链：先「jam her right boot against the brake」（词汇例句）后「punched it」——素读#6「踩死刹车」与素读#7「反过来踩油门」的先后被 md 忠实保留，未混淆。
- 块9 双侧镜像的描述顺序（先表姐后牧师）与原文一致；「grimy-black cassock」未在 md 中直接指认为「普拉特」，只作「木乃伊/普拉特」的呼应联想（ch09 块4 有据），处理克制。
- 块10「three polite knocks」——「礼貌的」这一定语原文所有（polite），md 未夸大。

**结论：阻断 0、提示 2（1 不修、1 建议补记）。本章干净。**
