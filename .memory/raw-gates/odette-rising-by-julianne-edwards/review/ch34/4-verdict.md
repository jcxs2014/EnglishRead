# 4-verdict · ch34 light your lamp（T3 深审 2026-11-18）

R1：子代理盲读 8/8（区间验证 0 失败）。R2：rc=0。R3：漏 1（轻微，提示不修）/ 编 0 / 错 0。
（T3 机器层阶段已修：概述「Stabat Mater」非原书词 → 改书内措辞「十字架下母亲悼歌」，check_entities 复绿。）

## 逐块判定（11 块）

| 块 | 断言 | 证据（text/ch34_chapter_34.txt） | 结论 | 档位 |
|---|---|---|---|---|
| 原句1 leave-taking | 说话人＝Berthe；「jejune」判词＝她 | "This, Odette, is the leave-taking of a colossus." | 对应 | ✅ |
| 原句2 adorned | 施事：着盛装＝Berthe；不敌女像柱＝叙述比较 | "they were no match for Berthe, who stood statuesque yet lithe" | 对应 | ✅ |
| 原句3 choir | 施事：齐声＝百人合唱；震动=她 | "vibrating through her body in a way that was thrilling" | 对应 | ✅ |
| 原句4 lament | 联想＝她（唱给她一个人=错觉） | "as if Verdi had written it for her" | 对应 | ✅ |
| 原句5 arrows | 施事： slicing =四女声；落泪=她与 Berthe（泪洗她的疤） | "the droplets slipping down her cheeks, bathing her scar." | 对应 | ✅ |
| 原句6 benediction | 施事：按头顶＝Berthe；解读=Odette | "It was some kind of benediction." | 对应 | ✅ |
| 原句7 lioness | 说话人＝Berthe（信）；收信人=Odette | "You are a lioness and the most bravehearted woman I know." | 对应 | ✅ |
| 原句8 parting gift | 说话人＝Berthe；知 Merry 之事＝信中自陈 | "I have acted: one parting gift" | 对应 | ✅ |
| 原句9 stifling | 说话人＝Berthe；羞耻判词＝信 | "Shame is too stifling an emotion for women like us." | 对应 | ✅ |
| 原句10 absolution | 说话人＝Louis；「loved you even more」＝他的裁定 | "she must have loved you even more than I thought." | 对应 | ✅ |
| 原句11 hang in space | 施事：形容消瘦=叙述；不回头=Merry | "He did not look back." | 对应 | ✅ |

## 修复

无阻断（本章仅机器层阶段的总览实体修复，已另行提交）。

## 已核实为正确

- 原句1 「You do not understand, you are jejune.」＝原文逐字；md 词汇表 jejune 例句一致。
- 原句4 「a mother whose son had been taken, tortured, and killed」——md 分析「母亲悼歌」的读法与原文对 Stabat Mater 内容的描述一致（原书未点名曲名，md 已改用书内措辞）。
- 原句8 「one parting gift」——md 分析「以命抵命」的定性来自信文与 Louis 的「Victor Gagnon is dead」并读。
- 原句10 「she must have loved you even more than I thought」——Louis 台词逐字；md 分析「翻译成爱」的表述一致。

已核实为正确（R5.5 固定节）：以上各条后续不得以「读着不对」为由改动，除非给出反证。
