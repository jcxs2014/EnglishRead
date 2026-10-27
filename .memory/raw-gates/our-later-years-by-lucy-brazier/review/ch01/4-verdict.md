# ch01 判定（R5）

| 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|
| 全篇「只有 13 句」 | text/ch01_introduction.txt 0–1179：逐句切分得 13 句（含 `Nothing to see here.`、`But these women were future pioneers.`） | 正确 | — |
| 「字符数 约 1,180，正文 205 词」 | 同上，`len(s)=1179`、`len(s.split())=205` | 正确 | — |
| 块数 6（本书众数 10） | 2-machine.json form.blocks=6、block_median=10.0、block_range=[6,10] | 短文（205 词）6 块已覆盖 13 句全部；⑳ 对 <3 章书强制 5–10 块 | 提示 |
| H1 `01. Introduction（…）` | form.h1_shape_ok=true | 正确 | — |
| 子项五件齐 | form.subitems_modal 与 profile 完全一致 | 正确 | — |
| 引语逐字 6/6 | quotes.py verbatim 6/6 ✅；verify_overview 无关 | 正确 | — |
| 中文密度 | 2-machine.json counts 无阻断 | 正确 | — |

## 已核实为正确（防误修）
- **「只有 13 句」看似与 `(?<=[.?!])\s+` 切出的 12 句冲突**，实因呼语 `Dear women of London,` 以逗号收尾、与下一问同段：按语义断句仍是 13 句（含 `Nothing to see here.`）。→ text/ch01:1–1179
- **概览写「约 1,180 字符」** 是四舍五入，精确值 1,179；不是错误。
- **块 1 引语含两个问句 + 破折号定语从句**，`chapter.sh` 判 1–3 句 / 53 词，合规；不要因「看着长」拆块。
