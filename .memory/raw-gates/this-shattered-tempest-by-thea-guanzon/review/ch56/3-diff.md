# ch56 R3 对账 / R4 逐块复核

- 章文件：`notes/books/novels/this-shattered-tempest-by-thea-guanzon/ch56 epilogue five years later.md`
- 素读：`review/ch56/1-suread.json`（`char_total` 37666，events 8 条，逐条带原文区间）
- 块数：修前 12 → 修后 **14**（本章 6508 词，建议 12–15 块）

## R3 三张单子

**漏**：2 条

| # | 素读事件（取证） | 处置 |
|---|---|---|
| L1 | E2 尼亚姆哈答「夜帝晚出发、只差几个小时」并对偷猎者一事「极为不满」（`text/ch56_epilogue.txt:9`，53 词 / 5 句） | 新增原句 3（取前两句，30 词；关键词 `a message · behind schedule · a couple`） |
| L2 | E5 旗舰抵达、他弯腰把女儿抱进怀里、她搂着脖子讲个不停（`:34`，67 词 / 3 句） | 新增原句 8（`collapsed into · scooped · chattered away`） |

**编**（md 有、原文无）：0 条。

**错**（两边不一致）：0 条。

## 提示（不判阻断，已在 md 内标注）

- E1（尼亚姆哈落步随行、梳理积压文书，`:4` 末句）与 E4（希拉雅用生硬水手通用语说「踹偷猎者的屁股」，`:24`，27 词、低于 30 词建议区间）都不是独立成段的完整拍子，已在**原句 1** 与**原句 5** 的「读者视角提示」里逐字标注「不在本块引语内」。
- 章末露骨段落未摘引（与 ch18/ch21/ch42/ch54 一致的处理）。

## 复跑

- `bash scripts/chapter.sh` rc=0、0 ⚠️（块数 14 落在本次本书区间 5–14 内）
- `python3 scripts/attic/check_para_span.py` OK
- `bash scripts/gate.sh` GATE=0（579/579 引文可核实 100%）

素读的其余事件（E3/E6/E7/E8）修前即有块覆盖，逐块核对与「中文理解」一致。
