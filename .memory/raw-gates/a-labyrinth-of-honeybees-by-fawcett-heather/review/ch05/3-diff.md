# ch05 The Attack at the Falls — R3 对账（素读 ↔ md）

素读件：`review/ch05/1-suread.json`（8 条，锚点 `/tmp/t3_validate.py` 复核异常 0）
被查件：`notes/books/short-story-anthologies/a-labyrinth-of-honeybees-by-fawcett-heather/ch05 the attack at the falls.md`（185 行）
原文：`text/ch05_the_attack_at_the_falls.txt`（ch05:NN = 段落号）

## 一、编（md 有、原文无）

无。本章 md 的全部事实断言（烧园威胁／伏击／神庙剁桃／栽赃计划／刺杀公主／森林神附身）均可回原文。

## 二、漏（素读有、md 无）

| 编号 | 素读事实 | 原文 | md 侧 | 档位 |
|---|---|---|---|---|
| 漏-1 | 祭司被审问官一刀刺死 | ch05:91 `The inquisitor killed him in one swift, almost negligent movement, jamming his dagger into the priest’s throat.` | 导航与总结均未提（总结止于"接住倒下的他"） | 提示（中） |
| 漏-2 | 公主自述：近一个月前上山途中遭袭，侍从与飞马被杀 | ch05:54 `Nearly a month ago ... they killed my attendants and pegasus.` | 未记 | 提示（中） |
| 漏-3 | 审问官指认弓手是国王的人、且自己曾与其中一人同训 | ch05:58 `Those were the king’s archers. Their training was unmistakable ... I trained with one of them.` | 未记（这是"国王出卖他"的直接证据） | 提示 |
| 漏-4 | 中箭跪地时箭袋已空 | ch05:24 `He reached for another arrow ... The quiver was empty.` | 未记 | 提示（低） |
| 漏-5 | 上一章赌局落空：两人都猜错（隔天他就到了） | ch05:1 `We were both wrong. The following day brought the royal inquisitor to the temple.` | 未记（ch04 赌"一个月/三天"的回收） | 提示（低） |

## 三、错（主语／因果／数字／时序／措辞）

### 错-1（提示·低）md:55「末句只有九个词」
- md 侧：`ch05 the attack at the falls.md:55`（块 3 表达方式）
- 原文侧：ch05:27 `The woman went down with the arrow in her throat.` —— The/woman/went/down/with/the/arrow/in/her/throat = **10 个词**
- 判定：计数差 1 → 提示（低）。

### 错-2（提示）md:145（块 10 中文理解漏译第三句）
- md 侧：`ch05 the attack at the falls.md:145` 只译了"神退回／女神离开"与"他倒下我接住"，**未译** `I turned to see that the princess wore an expression similar to the inquisitor’s.`（ch05:106 第 3 句）
- 判定：引语四句、中文三句，读者看不到公主的表情这一环 → 提示。

### 错-3（提示·低）md:121「从前脸上的脸属她，现在脸上的脸属别人」
- 原文侧：ch01:12 `The faces of a dozen people flitted across the royal inquisitor’s face`（第一章的"脸"同样出现在**审问官**脸上，只是属她的幻象）
- 判定：表述把"幻象 vs 附身"简化为"属她/属别人"，易被读成前几章的脸长在她自己脸上 → 措辞不准，提示（低）。

## 四、数字与专名核对

| 项 | md | 原文 | 结论 |
|---|---|---|---|
| 段数/词数 | 10 块（本章 3955 词） | `chapter.sh`：words 3955 | ✅ |
| 神数 | 未写数字 | ch05:57 `By the Eighty-Three` | ✅ 无冲突 |
| 刺客人数 | 未写数字（"一场伏击"） | ch05:15/19/25（至少四名弓手，一女三男） | ✅ 未写数即无错 |
| 中箭部位 | 腹部（"插在躯干上"） | ch05:23 `through his stomach`；:45 公主视角 `His breath had shallowed` | ✅ |
| 她如何救下公主 | 拽绷带使他失衡 | ch05:79 `I yanked on the bandages in my panic, throwing him off-balance ... only a glancing scrape` | ✅ |

## 五、已核实为正确（看似可疑、回原文成立）

- md:10「国王下令若不合作就烧掉花园」→ ch05:6 `the king has said that I may burn your gardens to the ground if you refuse to cooperate` ✅
- md:10「继承人一直藏在神庙里剁桃子」→ ch05:42 `At the table stood the king’s heir, chopping peaches with her mouth full.` ✅
- md:10「国王派刺客杀死自己的税吏、把罪栽给女神」→ ch05:62 `the king sent assassins here with orders to murder his own tax collectors ... pin the crime on you` ✅
- md:10「森林神借他的身体现身」→ ch05:93–96（面孔闪过 `not a vision this time` → `the Forest God replied`）✅
- md:12「她要救的这个人正在杀她保护的人」→ ch05:77–91 ✅
- md:13「冷静得像早已练习过」→ ch05:64 `as if she were well practiced` ✅
- md:13「被女神当面拆穿'狠心杀手'的名声」→ ch05:47–48 `Why does everyone think I’m some hardened killer?` / `Because you are?` ✅
- md:79「几个月没听见的神」→ ch05:48 `It had been months since the Goddess had spoken to me.` ✅
- md:107「她那双手做过的所有事在这里突然有了分量」→ ch05:28–29（按伤口、解围巾）＋:79（拽绷带）✅
- md:135「国王的敌意只是漫长战争里的一个瞬间」→ ch05:102（两神自成形起为敌）✅
- 词表 11 条例句全部逐字出自本章 ✅
