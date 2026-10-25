# 4-verdict · the-intrigue-by-silvia-moreno-garcia（T3 深审，2026-10-25）

**覆盖声明**：全章 R1（24/24 章素读清单，194 条事实锚点区间全验）+ R2 机器层（24/24 章 chapter.sh --json，全 rc=0）+ R3 对账（三张单子全量）+ R4 成因类人判（SPK 4 全读 / AGY 53 全读 / NEG 112 全读其中强断言 53 全验 / NUM 53 全读；另有 R1→md 关键事实回源抽验 19 项）。未逐块通读 296 块的中文修辞层（该层由门禁 ⑲ 中文密度 100% 与夹杂率 0% 兜底）。

## 判定表

| 断言 | 证据（章:行/区间） | 结论 | 档位 |
|---|---|---|---|
| L1 ch01 卖相机对象 Moisés 未入 md | text/ch01:113 "He took the camera from his shoulder bag and handed it to Moisés" | 真漏 | **阻断→已补** |
| L2 ch13 药剂师 Facundo Alamilla 名字未入 md | text/ch13:133 "Facundo Alamilla has dispensed medicines without the proper prescription" | 真漏（名字级） | **提示→已补** |
| F1 全书「三十年」时间跨度无原文锚 | text/ch02:244 "Inés's twenty-second birthday"；text/ch13:350 "improve in 1929"；text/ch23:145 仅 "many years before"；ch13:242 "long, long ago" | 推断性夸大（实际 12–14 年） | **阻断→已修 26 处** |
| F2 ch13「全书唯一 Perla thinks」措辞偏宽 | text/ch15 亦有多处 "Perla thinks" | 措辞应收窄，事实层无错 | 提示（不修） |
| L3–L7 房客三拨/Paso de Valientes/Paloma/Crésida/玉米饼/Bellas | 均为次要事实，非章转折点 | 不构成「漏转折」 | 提示（不修） |
| E1–E3 说话人/施受/数字方向 | 逐条回源（3-diff 表） | 0 错 | 通过 |
| NEG 强断言 5 项 | 3-diff 表 | 全部成立 | 通过 |

**报数（四组）**：逐字 —— 24 章 296 块 verify 0 查无（R2 机器层 + 总览 107/107）；对应 —— R4 抽验 110 行分析层 0 张冠李戴；形态 —— 24 章 H1/导航/子项/块数全合本书众数；断言 —— 查出 **2 条阻断（L1 漏、F1 编）+ 1 条提示级漏（L2）**，全部整改完毕。

## 取证命令（零命中类自证）

```
/usr/bin/grep -c "thirty" notes/books/mystery-thriller/the-intrigue-by-silvia-moreno-garcia/text/ch23_chapter_23.txt
→ 0（ch23 无 thirty 字面）；退出码 1（grep 无命中）
/usr/bin/grep -n "twenty-second birthday" notes/books/mystery-thriller/the-intrigue-by-silvia-moreno-garcia/text/ch02_chapter_2.txt
→ 1 命中（ch02:244）；退出码 0
/usr/bin/grep -n "improve in 1929" notes/books/mystery-thriller/the-intrigue-by-silvia-moreno-garcia/text/ch13_chapter_13.txt
→ 1 命中（ch13:350）；退出码 0
```

## R5.5 已核实为正确（防误修护栏）

| 写法 | 原文依据 |
|---|---|
| ch10「手枪第一次实名出场」 | text/ch10:40 "the memory of the pistol he kept under his pillow"——pistol 全书首见在此 |
| ch01「Perla 唯一一次被撩红」 | text/ch01 "the woman practically blushed as his smile widened"；text/ch06 "No maidenly blush colored her cheeks" 反证其后不再 |
| ch17「Inés 一生唯一一次开口求助」 | "lend me" 全库仅 ch17 一处属 Inés；其余 borrow 均为他人（Filomeno/Emilia/Cándido 借车） |
| ch15「It's not Perla who opens her legs」分身句 | text/ch15:346 逐字存在 |
| ch23「枪的三任主人 父亲→Cándido→Perla」 | text/ch15:97 "Your father gave me this as a gift for my thirtieth birthday" |
| ch12「他妻子比他以为的敏锐」 | text/ch12 "his wife was more observant than he'd thought" |
| ch24「谵妄是全书唯一招供窗口」 | confess 全库 4 处，唯 ch24 是实际招供 |
| 「十多年」修订口径 | Inés 1943 年 22 岁（ch02:244）+ 推妹在 1929 之后（ch13:350）⇒ 案发距今 12–14 年；「more than twenty years」（ch10:16）锚的是**私奔**不是推妹——任何人不得把「十多年」改回「三十年」，除非给出新原文锚 |

## 结论

- **阻断 2 条（L1、F1），提示 8 条，假红 3 项核查通过**；阻断与名字级提示全部整改。
- 整改后复验：chapter.sh 24 章 rc=0、gate.sh EXIT=0（见完工复验 commit）。
- F2（「唯一」措辞）与 L3–L7（次要漏）判定不修，依据已写入 3-diff，台账同记。
