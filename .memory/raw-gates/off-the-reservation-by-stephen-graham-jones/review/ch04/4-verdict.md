# ch04 4-verdict（R4 逐块 + R5 判定）

R2 机器层：2-machine.json rc=0，7 块 7 引语，issues 全空。
R4 人判：7/7 块逐对核 + 施事三问。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 块6「她等了四个月、设了无数次局」无据且与 ch02 矛盾 | text/ch04 无「等待四个月」表述；ch02 text「for a few graveyard shifts…in the dead kid's room」；「four months」在 ch02:41 主语为 wreck | 分析层把「车祸后四个月」错置为「Seine 等了四个月」 | **阻断** |
| 块2「右手」 | 引语「a hand flipping the passing lane off」 | 左右未言明，「右」为添加 | 提示（不修） |
| 导航「今天出院」 | text/ch04:164「You're out as of today…Released, finished, done.」 | 有据 | 已核实为正确 |
| Christian 与 Seine 的亲属称谓（ch04「niece's only son」vs ch09「older cousin」） | text/ch04 anchor 命中验证 True | 原文内部口语差异，md 各自忠实原文 | 提示（不修，防后人「统一」改坏） |

取证命令记录：
- `/usr/bin/grep -n "four months\|waiting" text/ch04_3_pretty_good_for_an_indian.txt` → 行23/56/167/224，无「Seine 等待四个月」；退出码 0
- `/usr/bin/grep -in "today\|out of here\|go home\|leave" text/ch04_3_pretty_good_for_an_indian.txt` → 行164 命中「You're out as of today」；退出码 0
- `/usr/bin/grep -n "releas\|discharge\|check out" …` → 0 命中（退出码 1，故换词重查，如上）

## 已核实为正确

- 导航「今天出院」：text/ch04:164 原文明写，后续不得以「ch02 说是两天后」为由改动——ch02 的「two days」是 Seine 数日前的话，ch04 已到当天。
- 块3「四十三岁怎么就太大了？」的疑问句式保留了原文的反讽（how was forty-three too old?），非 md 添乱。
- 块4 Conrad 死亡细节六要素（Minnesota／Leech Lake 小孩／Nokia／六十时速／坡道／飞天）与素读#4 全部一致。

**结论：阻断 1（块6 编造等待时长）、提示 2（不修）。**
