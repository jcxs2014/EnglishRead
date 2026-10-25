# ch02 · R3 对账（Chapter One，md：`ch02 chapter one a new person.md` / 原文 `text/ch02_chapter_one.txt`，35,295 字符 / 6,356 词）

R1 事实 8 条（独立子代理，锚点 8/8 唯一命中）。

## 漏（素读有、md 无）

| # | 素读事实 | 原文锚点 | md 位置 | 判 |
|---|---|---|---|---|
| L1 | 母亲给她发短信：巴黎大信封（école 的录取）已寄到 | `her mother texted her that`（五个月前） | 原句 11 只处理「十二个词」的回信，未收短信内容 | 提示：该信封在 ch03 厨房争吵里正面展开，ch02 收「回信内容」更主线 |
| L2 | Catherine 周一凌晨四点醒、六点出门 | `she woke up at 4` | 无 | 提示：时间细节未收，不影响本章判断 |
| L3 | Seb 五十一岁、身体健康、猝死是「total shock」 | `Seb was only fifty-one, a`（309） | 原句 7 的原文引语含 `His heart, in his sleep`，但 md 叙述未点年龄 | 提示：年龄在本章属他人转述（问句实为问自己），md 已用「毫无理由地被击倒」承其意 |

## 编（md 有、原文无）

| # | md 表述 | 原文核查 | 判 |
|---|---|---|---|
| F1 | 导航「正沿着湖跑她**二十年来的第一个双程**」 | 原文 `text/ch02_chapter_one.txt:442`：`She’s closing her second loop and the corner of land jutting into the lake is coming up.`；`First time in twenty years`（261 行）指的是**独自生活**，不是跑步史 | **阻断**：把「今天的第二个环」写成「二十年来的第一个」，且把「独居二十年首次」移植给跑步 → 已改为「她今天的第二个环」 |
| F2 | 人物弧线「把答案押在**七英里之外**的水边」 | 全书 ch02 无任何 mile/km 距离表述（`grep -nE "[0-9]+ (mile|kilometer|km)" text/ch02_chapter_one.txt` → 0 命中，退出码 1） | **阻断**：凭空数字 → 已改为「湖湾尽头的那片水边」 |

## 错（两边都有但不一致）

| # | md 表述 | 原文 | 判 |
|---|---|---|---|
| — | 未发现。「十一平方米」「八层无电梯」「五周」「八月一日」「十二个词」「一八八二年二月」均与原文一致 | — | 通过 |

## 逐字复核（本章词汇例句，13 条中抽 4 条高风险）

| 例句 | 原文命中 | 判 |
|---|---|---|
| `It felt the same as having a crush, that nervousness that love would not be requited.` | ✓ | 通过 |
| `Her heart crumpled like someone balling up a bad first draft, which is to say, her heart crumpled performatively.` | ✓ | 通过 |
| `Madame leveraged herself up by pressing her elbows down on the railing.` | ✓ | 通过 |
| `The tips were decent, but it was too expensive for there to be regulars so there was no friendly chit-chat to help the day pass.` | ✓ | 通过 |

取证：`grep -n -i -m6 "miles\|kilometre\|runs\b" text/ch02_chapter_one.txt`（显式路径、非 git grep）；距离类 0 命中，`second loop` 见 442 行。
