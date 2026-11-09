# ch03 4-verdict

| 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|
| R1 8/8 锚点全命中 | 1-suread.json | 一致 | — |
| 块5 施事：Everett tells Ruth（Perry 归属） | text/ch03「Perry is practically Brooks's horse," Everett tells Ruth」 | 正确 | — |
| 块6 施事：Jody 拆台（tipsy at a bar 一句的说话人） | text/ch03 对话轮 | 正确（Jody） | — |
| 块4 施事：Brooks 接管解释（I take over Ev's explanation） | text/ch03 | 正确 | — |
| 块9 数字：turned eighteen / Two years later | text/ch03:9206–9374 | 正确 | — |
| 块6 跨章引用 ch02「还有几个月学业」 | /usr/bin/grep -n "few months" text/ch02_1_ashton.txt → 无命中，退出码 1；text/ch03:104、text/ch27:155 命中 | **跨章引用错章** | 阻断→已修 |
| 漏：Ruth「reason we met」钩子 | 见 3-diff | 提示（非转折，不修） | 提示 |

## 已核实为正确

- 块1「Fishers own the neighboring land, running a horse rescue」——马术救援场设定原文（ch03 开篇段）。
- 块11「This month can't go by fast enough」逐字；「两条 POV 指向同一日期」的收束读法成立。
