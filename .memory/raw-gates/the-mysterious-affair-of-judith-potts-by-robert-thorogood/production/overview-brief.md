# 总览三篇派工单 · The Mysterious Affair of Judith Potts

> 仓库根：`/Users/jcxs2014/Documents/Works/EnglishRead`
> 书目录：`notes/books/mystery-thriller/the-mysterious-affair-of-judith-potts-by-robert-thorogood/`
> **引语池**：`/tmp/jp/quote_pool.txt`（312 条，全部来自已过门禁的章节块，格式 `[chNN|原句N] 英文原句`）

## 铁律

1. **引语只能从 `/tmp/jp/quote_pool.txt` 里挑，逐字复制**，一个字都不许改、不许截断、不许用 `…` 缝合。
2. 每条引语在金句/情感节点里写成独立成行的 `> "英文原句"（chNN）`。
   ⚠️ `（chNN）` 里的章号必须与引语实际出处的章一致（用池子里的标签）。
3. **同一文件内不得收录同一句引语两遍**（首尾呼应除外，且须有结构意图）。
4. 中文叙述句里的**人名 / 亲属关系 / 谁做了什么 / 谁欠谁 / 数字**六类断言，
   落地前必须回 `text/chNN_*.txt` 找到支撑句；找不到就不写。
   译名一律用本书既有写法：朱迪思、艾勒尼、贝克斯、苏齐、塔妮卡·马利克、贝思尼·怀斯、
   加里·怀斯、哈里·阿斯奎特、玛丽·珀特、菲利波斯·德米特里乌、米凯拉·帕菲德斯、
   奥利弗·贝雷斯福德、塞雷娜·萨克森、迈克·萨克森、贾米拉·哈利勒、布伦丹·佩里、
   安吉拉·格列佛、哈莱福德勋爵、艾琳·帕菲德斯。
5. 三篇的 H1 必须与文件名语义一致：`# 《The Mysterious Affair of Judith Potts》概述` 等。
6. frontmatter 与本书章节一致：
   ```
   ---
   状态: 未读
   modified: "2026-10-26"
   ---
   ```
7. 完成后必须跑：
   ```
   python3 scripts/overview.py quotes "notes/books/mystery-thriller/the-mysterious-affair-of-judith-potts-by-robert-thorogood/"
   python3 scripts/overview.py full   "notes/books/mystery-thriller/the-mysterious-affair-of-judith-potts-by-robert-thorogood/"
   python3 scripts/overview.py labels "notes/books/mystery-thriller/the-mysterious-affair-of-judith-potts-by-robert-thorogood/"
   ```
   三条都不得出现 ❌。**epub 在 `library/` 下，跑之前先确认命令带上 epub 路径**。
8. **不许 git add / commit / push**（多实例共用工作树）。

## 篇目与篇量（写作目标，不是门禁）

- `00_概述.md`：梗概 **6–8 段** + 主题 **3 个** + 人物弧光（主角各一段：朱迪思、艾勒尼、苏齐或贝克斯）
- `00_金句精选.md`：**25–30 句**，圈码 `①`–`㉟`（全书唯一、连续、不重置），每句 4 子项：
  **中文** / **上下文** / **为什么重要** / **呼应关系**
  （「呼应关系」里引用其他金句的编号，必须逐条回查该编号对应的引语确实谈的是那件事）
- `00_情感节点.md`：**8–10 个节点**，`## 节点一` … `## 节点九`（全书唯一、连续），
  每节点 = 叙事概括（1–2 段）+ 2–3 句关键引语

## 本书剧情骨架（供你定位，细节仍须回原文核）

- 朱迪思·波茨（Judith Potts）：马洛镇的名侦探/谜题爱好者，退休后做家务侦探；四十九年前在科孚岛
  （Corfu）涉嫌导致希腊裔丈夫菲利波斯·德米特里乌（Philippos Demetriou）溺亡；本书开篇，
  菲利波斯的女儿艾勒尼·帕菲德斯（Eleni Paphides）上门指控她。
- 艾勒尼（Eleni）：菲利波斯与米凯拉·帕菲德斯（Michaela Paphides）的女儿；持有旧卷宗与伪造照片，
  声称母亲当年告诉她朱迪思害死了父亲；实为被人利用。
- 好友团：牧师太太贝克斯·斯达林（Becks Starling）、遛狗师兼电台节目主持苏齐·哈里斯（Suzie Harris）、
  警督塔妮卡·马利克（Tanika Malik，ch11 后被停职）。
- 新案：前国脚加里·怀斯（Gary Wise）在自己家后林中中枪身亡；畅销作家迈克·萨克森（Mike Saxon）
  在自家花园办公室外中枪。两人死前都被同一号码勒索，凶手使用同一把枪。
- 嫌疑人：哈里·阿斯奎特（Harry Asquith，作家代笔）、塞雷娜·萨克森（Mike 的妻子，实为代笔者）、
  贾米拉·哈利勒（Jamilah Khalil，Mike 的私人助理兼情人）、哈莱福德勋爵（Lord Harleyford，
  失势贵族，有地狱火俱乐部洞穴）、电视节目主持人安吉拉·格列佛（Angela Gulliver，盯梢者）。
- 真相：警探布伦丹·佩里（Brendan Perry）是勒索者与两起谋杀的真凶；他利用艾勒尼的丧父之痛与
  伪造照片陷害朱迪思；朱迪思当年确实主动抽掉排水软管致菲利波斯溺亡（蓄意，非失手）。
- 朱迪思一度离境（末班渡轮去法国），后独自租车前往科孚岛核实，最后用第二本马耳他护照返回伦敦。
- 结局：三女在地狱火洞穴的尽头用「手包捆绑」制服布伦丹；真相大白，朱迪思把黄铜戒指（排水软管螺母）
  抛入泰晤士河。

⚠️ 上面每一条**都要回 `text/` 核到支撑句**才能写进概述；核不到就改写或不写。
