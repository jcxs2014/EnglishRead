# 4-verdict · ch09 double it（T3 深审 2026-11-18）

R1：子代理盲读 8/8（区间验证 0 失败）。R2：chapter.sh --json rc=0。R3：漏 2（轻微，提示不修）/ 编 0 / 错 0。

## 逐块判定（7 块）

| 块 | 断言 | 证据（text/ch09_chapter_9.txt） | 结论 | 档位 |
|---|---|---|---|---|
| 原句1 last to know | 说话人＝Odette（对银行经理）；「在我的工厂」施事归属正确 | "In my factory? But I didn’t hear about this." | 对应 | ✅ |
| 原句2 relentless | 说话人＝银行经理；「父亲素来慷慨」＝经理转述 | "Your father was always generous to the bereaved families." | 对应 | ✅ |
| 原句3 etiquette | 施事：发问＝她；确认合礼＝经理 | "“Is this the right thing to do, to write to them?" | 对应 | ✅ |
| 原句4 proof | 施事：夜里自抚＝她；「不可承认」＝叙述 | "her bulk a kind of proof of her existence. But these were not feelings to which she could ever admit." | 对应 | ✅ |
| 原句5 regarded | 对比：鼠注视量 vs 父亲注视量＝她的推算 | "his bright brown eyes had probably regarded her more than her father’s ever had" | 对应 | ✅ |
| 原句6 attack/retreat | 等式＝叙述层自我诊断；blade 阶梯＝引语尾 | "taking up her blade when they were not enough" | 对应 | ✅ |
| 原句7 mouse dare | 决断＝她；两个 How would she bear it＝引语 | "How would she bear it if she sat in this room for the rest of her life talking to a mouse?" | 对应 | ✅ |

## 修复

无阻断。

## 已核实为正确

- 原句2 「Double it」未入精读块但文件名与导航承担——核实原句 "“Double it. Please,” she said, a little surprised at her forthrightness." 在 text/ch09（1855:1884），导航转述无误。
- 词汇表 hirsute 例句 "a bored, hirsute woman who did her duty, but no more, leaving by the time she was twelve and not replaced."——六岁来/十二岁走逐字。
- 原句5 「though she supposed he must have done when she was small」——md 分析「幼时该抱过吧」的推测语气与原文一致（must have done 推测，非事实断言）。
- 词汇表 chits 例句 "he pushed forward an additional piece of paper, made in favor of a Monsieur Corot of Sèvres."——受款人方向正确（付给 Corot 家）。

已核实为正确（R5.5 固定节）：以上各条后续不得以「读着不对」为由改动，除非给出反证。
