# ch50 R3 对账 / R4 逐块复核

- 章文件：`notes/books/novels/this-shattered-tempest-by-thea-guanzon/ch50 the hukteras three day voyage.md`
- 素读：`review/ch50/1-suread.json`（events 9 条以上均为原文取证）
- 块数：修前 6 → 修后 **9**（本章 23 词）

## R3 三张单子

**漏**（素读有、md 无）：3 条

| # | 素读事件（取证） | 处置 |
|---|---|---|
| L1 | E3 凯德赶到（`text/ch50_chapter_fifty.txt:25`，38 词） | 新增原句 2（`hail of bolts · red-and-orange · Sardovian phoenix`） |
| L2 | E5 军团三人现身（`:36`，63 词） | 新增原句 4（`Shadowforged · throwing knife · crossbow`） |
| L3 | E6 穿以太空间、挡在跪着的阿拉里克身前被刺（`:50` 末两句，25 词） | 新增原句 5（`on her feet · kneeling · stomach`） |

**编**（md 有、原文无）：0 条。

**错**（两边不一致）：0 条。

## 提示（不阻断，记一行）

- P1：E4 陶壳炸弹（`:28`，26 词、原文以破折号悬空） → 块 2 提示逐字标注；不单独成块
- P2：E8「因为我爱你」之后的死亡（`:58`，26 词） → 块 9 已在引语内覆盖至 `I love you`，其后描写在提示里说明

E3 凯德驾凤凰小艇赶到、E5 影铸军团三人挡敌、E6 塔拉辛穿以太空间挡剑被刺——修前六块一块未覆盖；E4 陶壳炸弹只有碎片段（26 词、无句末），改在新增块的读者视角提示里逐字标注。

## 复跑

- `bash scripts/chapter.sh` rc=0、0 ⚠️
- `python3 scripts/attic/check_para_span.py` OK
