# T1 自检 verdict · public-access-afterworld-by-jane-schoenbrun

抽样章（78 章 → 1/5 = 16 章，t1_plan.py）：**ch01 ch06 ch11 ch16 ch22 ch27 ch32 ch37 ch42 ch47 ch52 ch57 ch63 ch68 ch73 ch78**
抽样理由：78 章 >40 阈值 → 1/5 至少 10 章；t1_plan 等距取 16（首末章自然在列）。
断言扫描全量：t1-candidates.txt（842 行候选，六类预筛）；抽样章 165 行逐条人判。
总览三篇：三篇全篇为同会话自写+自判，引语 90/90 经 verify_overview_quotes 机器核验（全部取自 gate 已验证的章 md 引语块）。

## 逐章核查

### ch01（foreword）
- ③数字：旁白者「十七岁」✓（text 有 seventeen）；「三十集（实际上只录音了二十九集）」✓（text thirty/二十九 in）
- ②「They put us in hospitals」they 指名分析=风格判断，非事实断言 ✓
- 缺陷 0

### ch06（majestic diner）
- ③七月四日烟花/火车站 ✓（text）；⑥「望着窗外」为读景判断 ✓
- 缺陷 0

### ch11（septic tank theory）
- ③nine months ✓、三十美元一小时 ✓（text 原句）
- ④「姐姐 Was」✓（text："My sister was trans, too."）
- 缺陷 0

### ch16（the stolen laptop）
- ③一小时前上传 ✓（text）
- ②「视频店在此第一次成为彼岸的名字」❌——text 首现是 **ch06**（Jim："The video store," Jim told her）→ 已修复为「ch06 已由 Jim 点名…在 Jules 的告别里再次成为」
- 缺陷 1（已修）

### ch22（the crash）
- ①对照 ch17 Prison and escape ✓（ch17 text 原句）
- 缺陷 0

### ch27（abels death）
- ②「ch21 三次失败的求救」❌——ch21 实为两次（Kyle 未接、妈妈三声转留言）→ 已修复为「两次（Kyle 未接、妈妈三声转留言）」
- 缺陷 1（已修）

### ch32（the shadowless photo）
- ④「你妹妹」❌与 ch11「姐姐」不一致（英文 sister 无年龄标记，两章须一致）→ 已统一为「姐姐」
- ③「你当时没有影子」✓（text："you don't have any shadow at all"）
- 缺陷 1（已修）

### ch37（the repaired tape）
- ③「unsafe 一词第二次出场（ch35 说过一次）」❌——全书 unsafe 实际分布在 ch20/ch23/ch37，本章为第三次 → 已修复
- ②「本章先于 ch02 的『Blockbuster 已倒闭』多年」❌表述倒置——ch02 旁白确写「Blockbuster, before it closed」（回溯声口），ch37 场景在其后 → 已修复为引 ch02 原文
- ③156 人失踪（ch13）✓；对照 ch06 ✓
- 缺陷 2（已修）

### ch42（the compound）
- ②「2024 年架在棚顶」❌虚构年份（text 无 2024）→ 已改为「如今架在棚顶」
- ①对照 ch26 的 Conductor ✓（ch26 text 有 Conductor）
- ③「十二座木屋」✓（text：about a dozen wooden cabins）；total wash ✓
- 缺陷 1（已修）

### ch47（stockholm syndrome）
- ✓（bathtub/Stockholm 均在 text；「第一次敲响」为叙事判断）
- 缺陷 0

### ch52（son of chimotera）
- ④「儿子 Marshall」✓；①对照 ch30 卧室袭杀 ✓（ch30 text）
- ③蜡笔论/brown ✓
- 缺陷 0

### ch57（5 31 am）
- ①对照 ch26 三猴告示牌 ✓（ch26 与 ch49 均有 monkey 告示，引 ch26 成立）
- ①对照 ch29「We'll take you soon」✓（ch29 text）
- 缺陷 0

### ch63（11 51 am）
- ③「唯一爱过的人」✓（text：the only person Jules Estrada ever loved in their whole stupid life）
- ①对照 ch59 heart skip a beat ✓
- 缺陷 0

### ch68（the therapy session）
- ②「两个愿望隔着三季对齐」❌——ch02（Ep1）到 ch68（Ep10）非三季 → 已改为「隔着整本书」
- ①对照 ch65 创造问句 ✓
- 缺陷 1（已修）

### ch73（the two names）
- ①对照 ch14 改名括号 ✓（text rest in peace/live forever 均在）；ch26 Subject 档案 ✓
- 缺陷 0

### ch78（postscript five years later）
- ①「对照 ch02 章名的豆袋椅之夜——上一次她在掐」❌——扼颈戏实际在 **ch38**（text："the threat of being strangled"），ch02 只有初吻 → 已改引 ch38
- ③still seventeen/黑色连帽衫 ✓；①对照 ch76 半句判词 ✓
- 缺陷 1（已修）

## 汇总

- 抽样 16 章，缺陷 8 处（ch16/ch27/ch32/ch37×2/ch42/ch68/ch78），**全部当场修复**并复跑单章门禁 EXIT=0。
- 密度 = 8/16 = 0.5 → 落在「按规定比例」档；同因类（①相对章号/③虚构数字/④亲属一致性）已在 16 章内全扫，未发现系统性模式（缺陷为散发笔误而非流程缺陷）。
- 高危类交叉验证：①相对章号 23 行全查（对照句均在被引章 text 内）；②绝对断言抽样核（156 人/十二座/45 秒/32 屏全 ✓）；④亲属全查（sister 统一、Elliot/Willa 夫妻、Fisch/Kyle 叔侄 ✓）。
- 总览三篇：全篇人判 + 90/90 引语机器核验 + ⑮ 标签对账仅 1 条 ⚠️（ch46/ch72 双章出现的原句，实出自 ch46，判断无误）。

## 结论

- T1 通过：8 处修复全部落地，整书 gate.sh EXIT=0（最后复跑于总览三篇之后）。
- T1 为**同会话自检**（非异会话验收），有效率未测，建议异会话复跑校准。
- 台账行见 `.memory/review-ledger.md`（审查方=自检）。
