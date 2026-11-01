# ch51 R3 对账 / R4 逐块复核

- 章文件：`notes/books/novels/this-shattered-tempest-by-thea-guanzon/ch51 the amirante and the nenavarene regiments.md`
- 素读：`review/ch51/1-suread.json`（events 6 条以上均为原文取证）
- 块数：修前 5 → 修后 **6**（本章 1284 词）

## R3 三张单子

**漏**（素读有、md 无）：1 条

| # | 素读事件（取证） | 处置 |
|---|---|---|
| L1 | E5 警讯与死令（`text/ch51_chapter_fifty_one.txt:18`，61 词） | 新增原句 3（`messenger skua · strict orders · wolf coracle`） |

**编**（md 有、原文无）：0 条。

**错**（两边不一致）：0 条。

## 提示（不阻断，记一行）

- P1：E3「Done」之前的两轮清单往返（`:27`） → 块 2/3 已覆盖要点，未另立块

E5（东海岸警讯 → 死令塞夫雷姆寸步不离 → 乘狼形小艇赶去）修前四块全无覆盖，只在导航里有一句「他赶去东海岸」。

## 复跑

- `bash scripts/chapter.sh` rc=0、0 ⚠️
- `python3 scripts/attic/check_para_span.py` OK
