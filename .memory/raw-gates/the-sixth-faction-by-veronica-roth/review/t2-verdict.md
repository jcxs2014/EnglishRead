# T2 断言全扫结论（同一会话，子代理分批核；非异会话审查）

**触发**：T1 自检在同会话查出 5 条阻断（≥3 ⇒ 自动进 T2）。T2 不做通读抽检，改做**全量断言扫**——把 `assertion_scan.py` 的 1147 行候选逐行回 `text/` 核，六类口径：① 相对章号 ② 绝对断言 ③ 年龄/数字/计数 ④ 亲属身份关系 ⑤ 方向施受债务 ⑥ 场景方位时距。另把总览三篇（00_概述 / 00_金句精选 / 00_情感节点）的全部中文断言一并纳入。

**分批**：6 批，候选切成 `chunk1.txt`–`chunk6.txt`，每批一个只读 `text/` 的审查子代理（不给审查表、不给 md 结论），产出 `t2-chunk1.md`–`t2-chunk6.md`；主会话逐条落修并复验。

## 一、统计

| 批 | 覆盖 | 缺陷 | 阻断 | 提示 |
|---|---|---|---|---|
| chunk1 | ① 全部 33 行 + ② 前半（总览 + ch01–ch33） | 11 | 2 | 9 |
| chunk2 | ② 中段（ch01–ch33 深读） | 11 | 8 | 3 |
| chunk3 | ch10–ch33 全核 | 13 | 1 | 12 |
| chunk4 | ch33–ch53（192 条） | 30 | 7 | 23 |
| chunk5 | 候选 769–960（186 条） | 10 | 4 | 6 |
| chunk6 | 候选 961–1147（185 条） | 8 | 1 | 7 |
| **合计** | 1147 行候选逐行回原文 | **83** | **23** | **60** |

## 二、阻断类（23 条，全部已修并复验）

- **Abnegation 被写成「无派别者」（5 处，同一根因）**：ch41 两处（「无派别者的走廊」实为 "the hallway of an Abnegation apartment"；"why I really left Abnegation"）、ch43 三处（"I'm not sure when Abnegation members learn about it"、"I wanted to belong to Abnegation"）。chunk2/chunk4 均独立报出。
- **「上一章」被当成「上一条同 POV 线」（5 处）**：ch20 三处（实际指 ch17，ch19 是 Four 章）、ch25 两处（实际指 ch23，ch24 是 Caleb 章）、ch36 一处（实接 ch35，中间隔 ch34 审问）。本书 POV 在 Tris / Four / Caleb 间交替，是结构性成因。
- **归属错**：ch15 「骗过真话血清」写成她本人做过（原文 "the Mender's mother tricked the truth serum"）；ch42 「他回一句你让我想起我母亲」实为 Natalie 说；00_概述「他（Four）对母亲说的第一句话是『我要杀他』」实为 Evelyn 说（`she says`）；00_概述「她托女儿给儿子带话」——Tris 不是 Evelyn 的女儿。
- **场景错位**：ch46 「Jeanine 在 Natalie 的厨房里」实为 Dauntless 模拟室（ch45）；00_情感节点 节点九「母亲在楼梯上中弹」实为仓库水箱边对射后倒下。
- **动作主语反了**：ch41 「Hub 顶上他跳她跟」实为她先伸手、自己迈出去把他带下去（"I step off the edge, and I take him with me."）；ch41 「她问他想要什么」实为他问 "What do you want?"、她答 "You"。
- **计数错**：ch01 「一年只被允许照三次镜子」实为每三个月一次（一年四次，同文件另一处自己写对）；ch60 「同一句 eyes are so dark 出现三次」实为两次；ch55 「两个 There can't be a reality」实为一个主句 + 两个 Or where。
- **引语不存在**：ch11 「母亲说『你什么都不用说』」全书查无此句，实为 "It didn't work, did it? The excision, I mean."。

## 三、提示类（60 条，已逐条落修）

主要是三类：**词数口径**（「四个词」实为三个、「六个词」实为四/五个、「十六个词」实为十八等，约 25 处）；**顺序/方位/末句归属**（ch39 Sly 先问鞋、ch44 子弹在厨房台面、ch52 速度在倒数第二句、ch53 童年句在倒数第二句）；**无据加码**（「二十年前」「十三岁的 Mae」「凉」「数瓷砖」「坐姿」等原文没有的细节）。

## 四、复验

- 逐条改动落盘后：`bash scripts/chapter.sh` 62/62 rc=0（含 23 章改动）；`/tmp/sf_quotecheck.py "<书目录>"` 查无块数 0（引语逐字）、引号配对；`/tmp/sf_vocabcheck.py` 词汇例句 0 条不符。
- 总览三篇在 `.overview_templates/ov_00_*.md.tpl` 改后 `python3 scripts/gen_overview.py "<书目录>"` 重生成（不手改产物）。
- `bash scripts/gate.sh "<书目录>"` ⇒ **正门结论 0 条阻断型、rc=0**；⑭ 总览引文可核实；⑰ 引语块前缀/编号/孤儿/泄漏 ✅；⑳ 整书体检全 0。

**结论**：T2 全扫查出 83 条（阻断 23 / 提示 60），全部就地修复并复验；无遗留阻断。本结论为**同一会话**产物（子代理只读 `text/`、不看 md 结论），不构成异会话审查。
