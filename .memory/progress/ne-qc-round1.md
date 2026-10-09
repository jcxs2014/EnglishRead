# Null Entity 写章期质检记录（round 1，2026-10-09 21:51）

工具：`scripts/attic/ne_strict.py`（逐章口径）＋ 主会话回源。目的：在代理自查轮进行时**只记录、不改动**
（项目记忆「代理的改稿轮次会覆盖主会话在它之前落盘的任何修改」）。

## 已判为假红（跨章引用已标注，勿改）

`ne_strict` 按「本章 text/」判定，天然看不见**带章号标注的跨章引用**。以下三条逐条回源核实为真：

| md 位置 | 断言 | 回源结果 |
|---|---|---|
| `ch21` 为什么这样写（原句①） | 「上一章以 `The world went white.` 收尾（ch20 末行可核）」 | ✅ ch20 `text/` **最后一段正文**逐字即 `The world went white.` |
| `ch21` 读者视角提示（末块） | 「下一章第一句 `We fell for a blissful eternity.`（ch22 首行可核）」 | ✅ ch22 首个正文段逐字命中 |
| `ch21` 为什么这样写（原句②） | 「两人上一章还在场：ch20 里 `"I'm sorry," you gasped at Rahn and Sira`」 | ✅ 该串在 ch20 `text/` 逐字命中 |

⇒ **终验口径**：`ne_strict` 的「分析层英文非本章逐字」报警，若同一行内已写 `chNN`／「上一章」／「下一章」
且该串在**所指标注章**逐字命中 ⇒ 判假红。

## 曾报现已消失（代理自查轮改掉了，21:49 报、21:50 复核不在文件中）

- ch10：`Sable Veonya`、`was betrayal`、`chose it anyway`
- ch14：`emptied out`
- ch15：`fall into you`（原句④实为 `I fell into you.` ⇒ 彼时是词形改动，已不存在）
- ch10：导航项 3 < 4（现文件已 4 项）

⇒ 这批**只作痕迹记录**，终验时按当轮实际输出重新判，不复用本表结论。

## 待各组交付时处理（21:55 记，**主会话此刻不改，防被自查轮覆盖**）

1. **ch11 同章双文件（并发写事故）**：`ch11 cheap echoes of me.md`（19865 B，23:50，8 块，`18/18`，ne_strict FAIL 0）
   与 `ch11 your own directory.md`（11717 B，23:53，6 块，`9/9`，FAIL 0）。两份**都过机械门禁**、
   首块引语相同 ⇒ 只能按**归属**裁决：按派活表 ch11 属 **ne-g5（ch11+ch12+ch13）**。
   ⇒ 待 ne-g4 / ne-g5 报告到达后核对各自声明的章号范围，**保留属主那份**，另一份按属主意愿处置（先移出书目录，不删）。
   ⚠️ 早前 `/tmp/ne_g4_vocab_ch09…ch23.txt`（15 份）已显示 g4 的活动范围超出其 ch09+ch10 指派，是本冲突的成因线索。
2. **ch02 `check_chapter_quotes` 1 条 MISS，且 MISS 串是中文**：
   `MISS: Sable Alzian 的两肩在烧，手腕脚踝被束缚磨得生肉发白。…`
   ⇒ 该组把**中文译文的整段引用**写进了全角引号 `“ ”`，被验证器当成引语提取（**工具按引号提取，不分中英文**）。
   处置方向：**去掉包裹译文的全角引号**（译文直写，不加引号），不是改英文。属主 ne-g1（ch02+ch03）。
3. **ch06 一处直撇号（字形不符）**：`ch06:57` 分析层写 `the Subsidiary's voice box`，而本书 `text/`
   **直撇号 0 / 弯撇号 1178** ⇒ 全书应为 `Subsidiary’s`。属主 ne-g2（ch04+ch05+ch06）。
   另需回源确认该串逐字（`filtered through the Subsidiary’s voice box`）。

## 工具侧一条判据修正（已落 `scripts/attic/ne_intake.py`）

原判据「`check_chapter_quotes` 命中数 == 原句块数」是**整类假红**：该工具还提取分析层与词表里的
引号串，8 块的章可报 `18/18`、`30/30`、`53/53`。改为 **分子=分母 ∧ 无 MISS ∧ 块数∈3–8**。
同时把「同章多文件」从静默取第一份**改为显式报警**（就是上面第 1 条能被抓出来的原因）。


## 事实底稿（ne-facts-part1，ch01–ch12）对开工推断的推翻

- **ch01 全文未出现 `LYREBIRD`** ⇒「I＝LYREBIRD」在 ch01 不可断言（此前记忆已记为推断，现已取证）。
- `my Wylla` 首点 **ch02 L151**。
- 「I＝LYREBIRD」最强明文等式 **ch07 L105**，证据链止于 **ch12 L93**。
- **ch06 身体互换后 I/you 的指代对象换体** ⇒ 分析层凡写「I 是……的身体」须按章核对互换点前后。
- 悬置点（总览层不得断言）：ch12 末 `Hello, Sable` 说话者未点名 (ch12 L201)；
  Sable 双姓 Alzian/Veonya 与 Fyster 全名关系 ch01–12 未交代（I 坚持 Veonya，ch09 L117）；
  身体互换机制原文明写不知 (ch06 L243, L261)。
