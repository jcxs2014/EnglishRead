# An Eye for Property (Tania Fordwalker) · 任务表
- 体裁：novels（科幻/投机惊悚中篇，Tor；2039 年「Splice of Life」身体租借芯片设定）
- 结构：**epub 无章节结构**（目录页仅 Begin Reading 单条、版权页无篇目，三方一致）＝单一正文流 novella，9,810 词
- 声部：YOU（Rose 第二人称看 Mabel 的生活）/ ME（Rose 亲自控体）/ US（共同意识）/ MABEL（短信署名）——拆章按叙事弧切在声部交界
- 语料：text/ 7 件 + xx_copyright_notice.txt（装置页不写）；拆分自 chapter1.xhtml 单流
- 验收：verify_corpus PASS（expect 7 · anchors ch01=Leary/ch02=Britney/ch03=Tweety/ch04=Jacquelyn/ch05=Mabes/ch06=Soshanna/ch07=Naples · shared=Mabel,Rose · FAIL 0 WARN 0）
- H1：`# NN. Chapter N`（新书默认形态；书内无章标题）
- 批次节奏：1 章/次，每章 chapter.sh rc=0 立刻 pathspec commit；每批前 gate.sh
- 块数按词数建议：ch01 1,770w→4–6；ch02 1,219w→3–4；ch03 1,344w→3–5；ch04 1,276w→3–4；ch05 1,513w→3–5；ch06 1,613w→4–6；ch07 1,073w→3–4

| 章 | 文件名 | 词数 | 内容 | 状态 | commit |
|---|---|---|---|---|---|
| ch01 | ch01 surgery and first handover.md | 1770 | 手术/合同评审/首次交接与首个周末 | 待写 | |
| ch02 | ch02 beach shack.md | 1219 | 海滩棚屋安家/负债/画作/初访大宅 | 待写 | |
| ch03 | ch03 marble silence.md | 1344 | ME 首周末：试衣/搜索/Ben 债务短信/美容院/四星评价 | 待写 | |
| ch04 | ch04 erosion weeks.md | 1276 | 数周蒙太奇：眉毛/麦当劳/失眠/作画障碍/Temu Rose/调解会 | 待写 | |
| ch05 | ch05 friday handover.md | 1513 | Prisha 视频通话/镜子失手/Rose 十年提案信/温暖周/退信 | 待写 | |
| ch06 | ch06 you bitch.md | 1513→实际 1613 | 夜里夺体/US 早晨互搏/砍芯片未遂/Ben 撞破 | 待写 | |
| ch07 | ch07 when im good and ready.md | 1073 | 收买 Ben/伪造新约/那不勒斯/幽灵化结局 | 待写 | |
| 总览 | 00_概述 / 00_金句精选 / 00_情感节点 | — | 最后一章后写 | 待写 | |
| T1 | t1-verdict.md / t1-candidates.txt / 台账一行 | — | gate 全绿后 | 待做 | |
