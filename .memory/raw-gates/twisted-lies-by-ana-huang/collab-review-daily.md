**Twisted Lies 五步审查结论（2026-10-16，Opencode-Mac，同会话执行）**

**【a 步 · 第 3 条门禁全量重跑】** 18 步全过、0 阻断型、gate.sh 退出码 0
verify_quotes 340/340（60/60 干净）· check_chapter_quotes 57/57 · check_vocab FAIL 0（WARN 232 提示型）· check_entities 0 · corruption_scan 0 · sweep_full 命中 202／跨章 0／查无 0 · check_anchor 凭空造词 0 · audit_structure 0 · verify_overview_quotes 54/54 · check_overview_full B 标签 60 对／0 不符 · check_block_keywords 阻断 0
**交付材料三样齐全**：① 门禁原件（`.memory/raw-gates/twisted-lies-by-ana-huang/`）② 总览自检（本日志）③ **跨书污染自检**（本轮补做，见 raw-gates/2026-10-16-审查-跨书污染自检.txt：独特全名 Christian Harper／Stella Alonso／Julian Kensler／Kage／Mike Kurtz／Ayana／Ricardo 均**仅本书**命中；Bridget／Maura／Nina 等常见名他书命中属同名不同人）

**【b 步 · 逐章归属】** `check_chapter_quotes.py` 逐章独立调用 57/57，全部「X/X in chNN text」

**【c 步 · 结构第二实现】** `check_struct_indep.py` 抓出 **1 处真缺陷**：ch31 原句 1 的「中文理解」缺冒号（`**中文理解**Stella …`）。同一缺陷 `audit_structure` 报 0 —— **印证「子项检查是假阴性高发点」**。已修，复跑 0

**【d 步 · 语义二审】** 6 批子代理（286 块引语↔分析逐对）+ 三个 `*_indep.py`
- `check_analysis_indep`：1128 条分析层英文片段全部逐字命中；报 4 条「整串查无但每词在书里」→ 人判：**2 条真缺陷**（ch01 `practically raised her` 应为 `me`；ch04 `before I could second guess herself` 应为 `myself`）已修；2 条为去对话标签引用（本库通行写法，提示型）
- `check_xref_indep`：134 处 chNN 指认、英文证据报警 0、中文式待人判 102 → 自建提取器（换实现）逐条回查跨章指认（章节文件 8 处），**全部属实**；唯 ch06 一处措辞不精确（把「走廊里的寒意」写成「回家路上」）已修
- 子代理结论：**阻断型 7 + 提示型 20**（说话人反转 0 处、跨章搬句 1 处）

**【e 步 · 总览层事实核对】** 人物身份／关系／死因／结局／数字逐条 grep 原文，修 4 处：Dante 并非「Delamonte 的创始人」（Delamonte 的联系人是 Luisa；Dante 是 Christian 的第一位客户兼老友）· Maura 病症原文为 **Alzheimer's**（非泛称失智症）· Julian 是 Mirage 一位过世住户的孙子（非「她公寓里的住户」）· Christian 是**帮她做**自己的品牌，不是替她接手

**【整改清单（已提交 `4c537490f`，28 文件）】**
阻断型 7 条：
1. ch17:57 规则内容写反（约束对象错＋第三条语义错＋引语省略被当作覆盖）
2. ch33:15/123 跨章引语误植（「我陷入麻烦了」实为 ch34，且两章「一句话总结」逐字雷同）
3. ch31:25 主语错配（Stella 问的是 Christian 会怎么做）
4. ch40:15/123 引语译法主语颠倒（是「你还不够了解他」，不是「他不了解你」）
5. ch51:45/49 人称错配（`you` 指 Stella）
6. ch55:61 出处错（Magda 是**母亲本人的画作**、以母亲命名，不是父亲盗来的藏品）
7. ch50:104 词汇例句改词形 `discrete`→`discreet`
提示型中的**确凿事实错已修 16 处**：ch01 房东时序 · ch09 七点→近八点 · ch05 笑的人写反 · ch12 成千万→九十多万 · ch17 脸红时序 · ch18 主语×2 · ch23 炸车时空 · ch28 错别字「家家」 · ch35 害怕方／引用错挂 · ch36 说话人 Julian · ch36 归属 · ch38 说话人 · ch47/ch48 摘要伪引号 → 原文逐字 · ch02/ch07/ch15/ch21/ch26/ch39 分析引用块外句

**【假红型（已记录，不改内容）】**
- `verify_fragments_indep` 9 条 MISS：来源 epub「标点前空格」排版瑕疵（`Stop .`／`Tonight ?`／`cup !`／`fucked .`），去空格归一后全部逐字命中
- `check_overview_full` ch40 引语判「跨标签拼接」：来源弯撇号 `’` vs md 直撇号 `'`，5 个片段逐条 flat 命中
- 子代理报的 ch24/ch27/ch29/ch32/ch47/ch50「查无」经复核同为**斜体词后空格**所致

**【投毒测试（修完已提交后执行，纪律 #3）】**
`check_struct_indep` 删掉 ch01 一个子项 → 报「缺陷 1 处」✅；`check_block_keywords` 把关键词换成虚构词 `zygomorphic` → 报「关键词不在本块引语内」✅；还原后 0 修改、git status 干净

**【整改后复跑】** gate.sh 退出码 0／0 阻断型 · verify_quotes 340/340 · verify_overview_quotes 54/54 · check_struct_indep 0 · corruption_scan 0

**【局限（如实标注）】** 本次为**同一会话**审查：d 步语义二审已改由子代理执行（附真实失败案例与防幻觉条款），但审查方与执行方仍同属本会话，对**自身写作盲区**的覆盖弱于异实例复核；建议后续如遇全书级争议再指派另一实例复核。
