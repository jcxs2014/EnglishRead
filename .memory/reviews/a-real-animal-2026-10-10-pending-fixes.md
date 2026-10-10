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

## 追加（21:08，主会话第二实扫）

### 排版体例偏离（阻断型，仅 ch06）
- 本书 9/10 章的分析层英文片段一律用「」包裹（ch01 25／ch02 26／ch03 15／ch04 38／ch05 25／ch07 43／ch08 51／ch09 44／ch10 47 条），
  **ch06 例外：直双引号 41 条、「」仅 3 条** ⇒ 与全书体例不符，且「」口径的扫描对它近乎失明（主会话第一版检查看到 ch06 只有 1 条片段即此因）。
- ch06 另有 **3 处直撇号**（`hadn't` / `Liam's` 型），而 `text/` 全书 3,082 个 `’`、缩写形态的直撇号 **0 个** ⇒ 字形改写，须还原为弯撇号。
- 修法：只改分析行（**不得动 `> **原句 N:** "…"` 的定界直引号**，verify_quotes 与 gen_overview 池正则都按该定界取串）。

### 提示型（只记不改）
- ch08 有 9 条直双引号，但内容是**书内母亲随笔的篇名**（"Places Beyond" / "Giving Thanks"），非证据片段 ⇒ 体例差异，不判红。
- ch10:71 两条 `⚠️ 跨章`（「I wanted to talk about how it had felt to be the leopard」／「Patty wasn’t curious about that」）实为 ch01 原文，
  md 已显式标注「ch01 text/ 里她讲过」⇒ 指对，合规。
- 词表基础档 `comforter / sunglasses / boathouse / sweatshirt / wallpaper / grandkids / crossword / flashlight / cigarettes` 的
  「疑含超纲词」WARN = 长度 ≥9 字符启发式误报 ⇒ 提示型，一律不改。

### 半成品快照教训（不改 md）
- 21:07 `sweep_analysis_inline` 报 ch06:70 `「sleeping together like lovers」` 🟠部分命中；21:08 重读同一行已是
  `"their bodies breathing together like lovers"`（原文 L1078 逐字连续）⇒ **代理写稿期的门禁输出是快照，不能作为结论**（与记忆「门禁在代理写稿期是半成品快照」一致）。
