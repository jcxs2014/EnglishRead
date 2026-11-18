# T1 自检 verdict · oubliette-by-l-v-russell

抽样章（29 章 → 1/4 = 8 章，首末必含，等距）：**ch01, ch05, ch09, ch13, ch17, ch21, ch25, ch29**
抽样理由：>40 章阈值未到（29 章），按 1/4 分级取 8 章；首章（世界观建立）与末章（Epilogue 收束）必含，其余按 ch01 起等距 +4 取。
断言扫描全量：t1-candidates.txt（970 行候选，六类预筛命中 113 行）。

## 逐章核查

### ch01（terror or ash）
- 断言：日期 MARCH 1821 ✓（text 首行）；Veronica/Hope/Lord Horewith 人名 ✓；绿裙 ✓
- 「noose that hanged her many years before」→ text 原句 ✓
- 关键词行 silent/sways/scraping/noose → 引语内逐字 ✓
- **缺陷 0**

### ch05（a kiss without teeth）
- 断言：五十二秒计数 ✓（text "thirty seconds, forty, fifty-two"）；「pigs and men」✓
- 「I am neither judge nor jury」✓；「We shared a body, a womb」✓
- 金句篇 ⑫/⑬ 引语逐字（overview 28/28 ✅ 已证）
- **缺陷 0**

### ch09（the ladies banquet）
- 断言：十一位 Ladies ✓（text "eleven of society's most prestigious ladies"）；For now ✓
- 「eleven」数字在导航与引语一致 ✓
- ⚠️ 提示型：概述篇未引用本章（覆盖 26/29 提示，Sylvatica 过渡章未提——见台账备注）
- **缺陷 0（阻断）**

### ch13（i am full）
- 断言：四人野餐（Oren/Anne/Edward/Rue）✓；Edward 金发卷胡须雀斑 ✓
- 「I am full」✓；「I do not embrace her back」✓
- **缺陷 0**

### ch17（a mirror of madness）
- 断言：母亲记忆错认婚约（That is Anne's wedding invitation）✓
- 白猫手套=白猫皮：ch23 揭示、ch17 无此内容（时序正确）✓
- 「I am not so unlike Veronica」✓
- **缺陷 0**

### ch21（the rats go to war）
- 断言：鼠群直奔 Ladies ✓；「Always.」宽恕条款 ✓
- 「I am tired.」结尾 ✓
- 金句篇 ⑮ Lady Pengelly「burden」标注 ch07 ✓（overview labels 0 待判已证）
- **缺陷 0**

### ch25（scraps and suffering）
- 断言：黑泪忏悔 ✓；「a thousand times」✓（text 原文 a hundred…a thousand——引语含两段数字，逐字 ✓）
- 「And I will be your suffering.」指向 Oren ✓（ch26 兑现）
- ⚠️ 提示型：引语「a hundred…a thousand」含原文自带省略号——keywords.py 补丁后逐字 ✓
- **缺陷 0（阻断）**

### ch29（as it should be）
- 断言：白猫回归（thinner, ribs visible）✓；scythe ✓；五种态度并列 ✓
- 「It matters little now」✓；「As it should be.」终句 ✓
- **缺陷 0**

## 汇总

- 抽样 8 章，**阻断 0 / 提示 2**（均为覆盖类提示，非内容缺陷）
- 读了 t1-candidates.txt 候选 970 行（六类预筛命中 113 行逐条人工判读）
- T1 为**同会话自检**（非异会话验收）
- 结论：T1 通过，无阻断；T2/T3 不触发

## 台账

见 `.memory/review-ledger.md` 追加行（审查方=自检）。
