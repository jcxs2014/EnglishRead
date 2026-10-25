# ch01 · R3 对账（Prologue，md：`ch01 prologue a dream of leaving.md` / 原文 `text/ch01_prologue.txt`）

R1 事实 7 条（子代理独立素读，锚点 7/7 唯一命中）。

## 漏（素读有、md 无）

| # | 素读事实 | 原文锚点 | md 位置 | 判 |
|---|---|---|---|---|
| L1 | 她想起女儿在 Max 家 | `Then she remembered Elisabeth was at Max’s house.`（589–638） | 无（导航只说「第一个念头是女儿」） | 提示：非转折，md 未收此环境细节；女儿在 Max 家这一事实后续章节自会交代 |
| L2 | 她穿 Seb 坚持让她穿的橙色反光紧身裤 | `the reflective orange leggings Seb insisted she wear`（935–987） | 无 | 提示：细节未收；该物象在 ch08 回忆里复现，ch01 未收不构成缺漏 |
| L3 | 往日她出门跑步他会在床上开始看书，那天早上他没动 | `when she went out for her run. But that morning, he hadn’t moved`（1564–1628） | 原句 5 的分析提到「身体先于意识知道出了事」，未写「他往常这时候会看书」 | 提示：对照句未点明，判断不受影响 |

## 编（md 有、原文无）

| # | md 表述 | 原文核查 | 判 |
|---|---|---|---|
| — | 未发现。导航与六个块的叙述性内容均可回指原文（「她想要自由」「她怕失去女儿的爱」属对原句 1、6 的概括） | — | 通过 |

## 错（两边都有但不一致）

| # | md 表述 | 原文 | 判 |
|---|---|---|---|
| E1 | 导航一句话概括「发现丈夫已经**僵硬**」 | `text/ch01_prologue.txt:22`：`He was cold as a river stone.`（全文无 stiff / rigor / 尸僵类词） | 阻断（轻）：把「冷」升格为「僵硬」，属原文没有的体征 → 已改「已经冷透」 |

## 逐字复核（本章词汇例句）

| 例句 | 原文命中 | 判 |
|---|---|---|
| `There was grief in that moment; she wanted the reassurance of her daughter’s face every morning.` | 1 次 | 通过 |
| `Already, she felt buoyant at the thought of the endorphins to come.` | 1 次 | 通过 |
| `The solidity of him, keeping the covers taut.` | 1 次 | 通过 |
| `She checked her reflection in the closet mirror.` | 1 次 | 通过 |

取证命令（本章全部 grep 均用显式路径 + `/usr/bin/grep`，不用 `git grep`/rg）：
`cd notes/books/novels/motherclown-by-harriet-alida-lye && for s in "she wanted the reassurance of her daughter" "buoyant at the thought of the endorphins" "The solidity of him" "closet mirror"; do grep -c "$s" text/ch01_prologue.txt; done` → 1/1/1/1，退出码 0。
