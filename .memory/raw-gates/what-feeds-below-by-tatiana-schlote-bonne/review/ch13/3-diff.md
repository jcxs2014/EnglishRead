# ch13 对账（R3）

> R1 素读：`review/ch13/1-suread.json`（facts 8，锚点 8/8 命中 text/，start-end 一致）
> R2 机器层：`review/ch13/2-machine.json`（chapter.sh --json，verdict=ok；块 10 / 引语 10 / segments 11 / segment_miss 0）
> R4 人判：`review/ch13/4-verdict.md`（10/10 块逐块核对）

## 漏（R1 有、md 无）
- 无（正文十块）。R1 8 条（淤泥中失视觉与绳、拟态 Jade 带路、抢咬嘴、割下 mindripper、撕成两半、洞角两名潜水员、游了两小时找她、循定位器哔声找到 Flint）全部由导航或块覆盖。

## 编（md 有、原文无）
- 无。mindripper、meat puppet、emergency locators、Breccia 插页均可回原文命中。

## 错（两边都有但不一致）
- 错 1【提示级】导航 `:10`「真 Jade 用口令验明身份」：原文的真 Jade 验明方式是掐手臂（`text/ch13_chapter_thirteen.txt:117`「Jade pinches my arm, twisting the skin.」）＋下刀割下 mindripper，**没有任何口令环节**。
- 错 2【提示级】Tropes `:12`「Jade 必须先答出一个蠢词才能被相信」：同错 1，口令不在本章。
- 错 3【提示级】一句话总结 `:165`「再由真 Jade 用一句蠢暗号与一把刀把她捞回来」：同错 1。
- **口径**：口令 Codswallop 在全语料只出现于 `text/ch04_chapter_four.txt:217/219` 与 `text/ch10_chapter_ten.txt:13`——`/usr/bin/grep -rn -i "codswallop" text/` 仅这两处命中。ch09 md:170「她已经知道自己必须先听见那句 Codswallop」与 ch10 md 的口令用法成立，不在本次修改范围。

## 结论
R3 三单：漏 0、编 0、错 3。漏 0、编 0、错 3（均为跨章挪用口令的三处表述，提示级）。已列入修复指令。
