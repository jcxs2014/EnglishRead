# A Real Animal — 主会话独立核验待修清单（2026-10-10 20:55）

> 本文件由主会话现写的**第二实现**（`.box-agent-scratch/ara_check.py`，已投毒自证可失败）产出，
> 独立于 9 项门禁。每条已当场 grep 取证。

## 阻断型（必须改）

1. **ch09 L28**：分析层片段 `「uncovering darkness」` **不是原文连续串**。
   原文（`text/ch09_duplicitous_existence.txt` L32）：
   `I need us to be constantly uncovering each other’s darkness and depth of being.`
   ⇒ 违禁令 1（分析层英文作证据须逐字）。修法：改为 `「uncovering each other’s darkness」`。
   归属确认：该句在 ch09 本章，章号无误；只是被缩写了。

## 已判假红（不改 md）

2. **ch08 L42 `「when your kids…turn thirteen」`**：省略号拼接，`…` 两侧 `kids` / `turn` 皆为原词，
   原文连续串见 `text/ch08_the_halls.txt` L103。合规 ⇒ 报警来自我的第二实现不认 `…`，属工具局限。
3. **ch10 L71 `「I wanted to talk about how it had felt to be the leopard. But Patty wasn’t curious about that.」`**：
   逐字在 **ch01** text L48 区段，且 md 已显式标注「ch01 text/ 里她讲过」⇒ 跨章引用指对，合规。
4. **ch05 L49 / L63 曾见 `”」` 型英文引号混入**：主会话 20:44 快照捕获，20:50 重扫
   （签名 `”」`、`「“`、行内 `「」` 计数不平衡三项）**全部 0 命中** ⇒ ch05 代理交付版已自纠。
   收尾时随全量 `sweep_analysis_inline` 再复扫一次。

## 交付状态快照（20:55）

- ch01 已提交 `619a491a2`；ch02 `735e6d252`；ch03 `7b6e9175a`。
- ch04–ch10 md 全部落盘；第二实检逐章：**引语块 8／编号连续／全部逐字在本章**；
  子项四件套各 8；词表 36 行（ch03 为 37），词头与例句全部逐字在本章，释义列纯中文。
- raw-gates 已落盘：ch01 ch02 ch03 ch05 ch07 ch08 ch09 ch10（**ch04、ch06 尚缺**，其代理未回报）。
