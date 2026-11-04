# T1 自检判定 · the-art-lovers-by-fiona-mcintosh

抽样章（先定后读，2026-11-04）：**ch01 / ch05 / ch10 / ch14 / ch19 / ch23 / ch28 / ch32 共 8 章**
——32 章按 1/4 抽样（17–40 章档），首章末章必含，其余等距（01→05→10→14→19→23→28→32）。
素读锚点复验：8 章 suread JSON 全量重放，**59/59 锚点全部命中**（ch01–28 各 8 条、ch32 6 条）。

## 总览三篇全篇人判（六类逐条回 text/ 核验）

- 「十二年的挨打/婚姻」（概述·ch22·ch31）：1942-09 成婚（ch01「September」+「sixteen」）→ 1954 = 12 年，与 ch20「It's been twelve years」一致 ✅
- 「婚后生下酷似 Ganni 的 Danjel」：ch14「About two years into her miserable marriage, after a miscarriage, she had given birth to Danjel」+「echo her brother Ganni」✅
- 「Maria 姓 Albertis / 丈夫 Francesco 在 Gozo」：ch29「'Albertis,' she confirmed」+ ch24「he's away working... Gozo」✅
- 「Blunt：前 MI5、传闻叛国、剑桥同窗」：ch15 三处原文支撑 ✅
- 「女王不到二十分钟的访问」：ch25「Her visit hadn't quite taken twenty minutes」✅
- 「Michael 怀在意大利 / 丢失过孩子」：ch32「I carried him in Italy... I'd lost a child… before Danjel」✅
- 「Matteo 移居加拿大 / Ganni 战死 / 母亲死于外孙出生后不久（心脏疑）」：ch17 Maria 通报逐句对应 ✅

## 缺陷清单（位置 / 改前 / 改后 / 原文依据）

1. **00_概述.md:15**：「生下酷似**亡兄**的 Danjel」→「生下酷似**死于战火的弟弟 Ganni** 的 Danjel」
   —— ch14「her little brother Ganni」（弟弟）；ch17「Ganni was killed during the war」。
2. **ch27 the lovers garden.md:77**：Lawrenz 台词「My brother told me」被译成「**我哥哥**告诉我」→「他哥哥（实为**弟弟** Robertu）递话」
   —— Lawrenz 为长子（ch03「the younger son」指 Robertu），其 brother 是弟弟。
3. **ch31 my answer is no.md:91**：「她**十五年**婚姻」→「她**十二年**婚姻」
   —— 1942-09 至 1954-04 约 11.5 年，书内口径 twelve years（ch20）。
4. **00_金句精选.md:132**：「她**第一次**把家暴说给懂的人听」→ 改为「不同于 ch13 借『表亲』化名的求助，这次以真名实姓」
   —— ch13 已有向医生夫妇的（化名）求助，第一次断言不成立。
5. **ch25 the blood signature theory.md**：「**一夜情**不解释它」→「**那晚的热度**不解释它」
   —— 措辞误导（两人非 one-night 关系），非事实错误，顺带修正。
6. **ch22 you are weak.md 词汇表**：「pinioned」例句不命中本章 → 换本章真实词「recoiled」
   —— pinioned 在 ch20 语料（B 类：章归属错），ch22 text 有「they both recoiled as if it had been white hot」。

## 断言扫描（t1-candidates.txt）

`assertion_scan.py` 全书输出 534 行：①相对章号 24（逐条人工读，全部成立）/ ②绝对断言 90（抽查+否定词 grep）/ ③年龄数字 213（重点核 12/14/15/16 岁与婚龄，1 错已修）/ ④亲属身份 163（grep 哥哥弟弟兄长子岳母小叔，2 错已修）/ ⑤方向施受 23（全读，0 错）/ ⑥场景方位 7（全读，0 错）。金句 25 条 Counter 去重 = 25 唯一。

## 结论

- 阻断 4 条 + 提示 2 条，**全部当场整改**；整改后 `gate.sh` EXIT=0（404/404 引语、结构 0、损坏 0、块序 0）。
- 同一成因类（亲属称谓）跨 2 处出现 → 已按规则自动执行 T2 断言全扫（本文件 §断言扫描即 T2 记录）：③④类 376 行经定向 grep 逐类核毕，余 0 未核。
- 复验：gate EXIT=0 · verify_fragments 422/422 · structure order 32/32 章 0 缺陷 · corruption 0。
