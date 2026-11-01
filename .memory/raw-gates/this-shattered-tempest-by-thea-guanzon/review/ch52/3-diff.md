# ch52 R3 对账 / R4 逐块复核

- 章文件：`notes/books/novels/this-shattered-tempest-by-thea-guanzon/ch52 the vigil at talasyns bedside.md`
- 素读：`review/ch52/1-suread.json`（events 6 条以上均为原文取证）
- 块数：修前 5 → 修后 **6**（本章 1349 词）

## R3 三张单子

**漏**（素读有、md 无）：1 条

| # | 素读事件（取证） | 处置 |
|---|---|---|
| L1 | E5 和约与重建（`text/ch52_chapter_fifty_two.txt:20`，截三句 24 词） | 新增原句 4（`a bit of a mess · peace treaty · rebuilding`） |

**编**（md 有、原文无）：0 条。

**错**（两边不一致）：0 条。

## 提示（不阻断，记一行）

- P1：E2 认出第八月的碎片（`:8`，27 词、低于硬线） → 块 2 提示逐字标注 `the shard of the eighth moon`

E5（他跟她说和约、重建、利苏残部，「我需要你在我身边」）修前五块全无覆盖——那一整段 119 词、12 句，只能截三句。

## 复跑

- `bash scripts/chapter.sh` rc=0、0 ⚠️
- `python3 scripts/attic/check_para_span.py` OK
