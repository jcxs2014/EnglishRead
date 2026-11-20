# ch06 4-verdict（T3 深审 · 边审边改）

R1：review/ch06/1-suread.json（8 条，子代理盲读，自检 PASS）。
R2：review/ch06/2-machine.json（chapter.sh --json verdict=ok，rc=0；10 块 11 片段逐字全 ok）。

## R4 逐块对应（人判）

| 块 | 引语↔中文理解 | 关键词 | 施事三问 | 结论 |
|---|---|---|---|---|
| 1 | 围殴噩梦 | the same age as me/beating me to death/pinned 在引语 | boy=施暴者、I=受击者 ✓；"pinned by Jacque Denue and his three friends" 施事一致 ✓ | 对应 |
| 2 | 导师拥抱与开课 | warm grizzly bear/let's have another lesson/out of this cold 在引语 | He=Francois 张臂、I=她冲入 ✓；"leaned into my face" 施事 Francois ✓ | 对应 |
| 3 | 武器三选 | a rock, a big stick, and a rope/Weapons are all around you 在引语 | "Here's…" 说话人=Francois（text 邻域）✓ | 对应 |
| 4 | 不许哭 | the fight's over/count on you being scared/won half the fight 在引语 | They=霸凌者们赌她怕 ✓；"他们每次都赌" 方向一致 ✓ | 对应 |
| 5 | 以小博大 | Kick the knees/stomp on the toes/smash his face 在引语 | 祈使句主语=受训的她、指导者 Francois ✓ | 对应 |
| 6 | 蜗牛托词 | smashing some snails/pestering the horses 在引语 | 说话人=Francois（对 Papa 撒谎）✓；中文"谎话编得越具体越显出慌"锚在话轮上 ✓ | 对应 |
| 7 | 狼来了之问 | hunt for food/take your kill/musket 在引语 | 说话人=Helena、受问者=Papa ✓（第一人称自述章）✓ | 对应 |
| 8 | 小保护神 | clutched/feel safer already/My little protector 在引语 | He clutched me=Papa 搂她 ✓；称呼受者=她 ✓ | 对应 |
| 9 | 失败复盘 | the most dangerous Lycanthru/frighten me into submission/cowered 在引语 | I wasn't prepared=她 ✓；被吓屈服 ✓ | 对应 |
| 10 | 恐惧终局 | view me the same way/stop fearing me/I would be dead 在引语 | he=Grenault、they=其他 Lycanthru ✓；多段省略号两段各自完整（text 相邻完整段）✓ | 对应 |

跨章引用核章号：
- 块5 分析原写"第 2 章的雪地伏击"——**阻断（编）**：grep 取证 ch02/ch09 无 snow；已改"月夜围猎"（moonlight 为 ch02 text 逐字）。
- 块10 分析 "ch02 'No fear' 的恐惧经济学"——text/ch02_2.txt 有 "No fear." 独立段 ✓ 章号正确。
数字回原文：8 岁/同龄（the boy had been eight years old, the same age as me）✓。

## 查出与处置

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| "雪地伏击"场景编造 | grep snow：ch02 0 命中 exit 1；ch09 0 命中 exit 1 | 改"月夜围猎" | **阻断→当场修** |
| 梦醒未尖叫/编借口/格挡断指未入块 | 转折层已由块2/3/4/6 覆盖 | 不修 | 提示（依据：同场景铺陈与手段细节，转折与课程义全收） |

## 修复动作（边审边改）

块5 分析改"月夜围猎"。修后 chapter.sh rc=0，pathspec 提交。

## 已核实为正确

- 块2 分析"灰熊的比喻先给温度再给体型"——原文 "like a warm grizzly bear with its cub"（text/ch06_6.txt 逐字）。
- 块8 中文"语气里一半是宠溺，一半是他自己没说出口的欣慰"——属解读，锚在 "He gaped at me, blinking. Then he threw his head back and laughed."（text 逐字）的行为链上。
- 块10 引语 "… And then I would be dead." 前段 "If he taught…altogether." 与末段均为 text/ch06_6.txt 相邻完整段（596–599 与 602 行邻域），多段合法。
