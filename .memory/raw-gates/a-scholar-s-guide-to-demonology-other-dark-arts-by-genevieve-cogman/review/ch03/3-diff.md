# ch03 对账（R1 素读 ↔ `ch03 chapter two.md`）

素读：`review/ch03/1-suread.json`（8 条，8/8 命中）。md：`ch03 chapter two.md`（11 块）。

## 漏（素读有、md 无）

| 素读事实 | 原文 | 处置 |
|---|---|---|
| Phil 拒吻戒指的玩笑 | `text/ch03_chapter_two.txt:7` `As long as I’m not expected to kiss your ring` / `:10` `Oh, that comes later` | 取舍：寒暄玩笑，本章 11 块已覆盖主谈话线，不单独立块 |
| 校长说地下室堆着旧器械，让 Phil 空时收拾 | `:196` `We do have a few old pieces of equipment in the cellars` | 取舍：不单独立块，改在「叙事手法」以一句点出伏笔（已补） |
| 柯基抬头轻吠一声 | `:52` `gave a little chuff` | 取舍：块 2 已覆盖柯基的拟人化 |

## 编（md 有、原文无）

无。逐块引语经 `quotes.py verbatim --full` 整串取证，`❌ 全书查无 0`。

## 错（两边都有、不一致）

| 位置 | 问题 | 证据 | 档位 | 处置 |
|---|---|---|---|---|
| 块 5 中文理解 | 含被 `…` 省略的 `Are you really going to be stubborn about this?` | `:76` 该句在引语的 `…` 之外 | 阻断 | 已删该句 |
| 块 10 为什么这样写 | 引「校规传统」解释必修制，该句在块外后文 | `:166` `A school tradition` | 阻断 | 已重写为只讲本块 |
| 块 11 | `volumes` 译作「卷子」 | `:214` `those volumes` 指《剑桥拉丁文教程》那几册 | 提示 | 改「那几册书」 |
| 块 8 读者视角提示 | 「守住秘密」无原文支撑 | 全章无她在家守密的表述 | 提示 | 改为「这份薪水是她往后几年的活路」 |
| 块 5 第一个 `…` | 两侧原文紧邻（`achieve things. But`），未跳内容 | `:76` | 提示 | 删该 `…` |
| 导航一句话概括 | 「原是一位富人的私人书房」是 Phil 的推断 | `:13` `must have been his private study` | 提示 | 改「Phil 从陈设推断」 |

## 假红

- `quotes.py full` 报 ch03 的 7 条 🔶「跨标签拼接」：`/tmp/t3_ellipsis.py` 逐块回 `text/` 定位，`para_breaks = 0`，均为 epub 内联标签造成，非跨自然段缝合 ⇒ 判假红，不修。
