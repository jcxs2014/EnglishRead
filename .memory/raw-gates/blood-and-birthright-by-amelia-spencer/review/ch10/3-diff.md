# 3-diff · ch10（素读 12 条 vs md 10 块）

## 漏（素读有、md 无）
- 无。事实 1–12 中，10 条转折点全部入块；事实「葬礼/摇椅」「鸡尾酒廊布景」为场景肌理，已在块 1 与导航覆盖。

## 编（md 有、原文无）
- 无。10 块引语逐字命中（chapter.sh 查无 0）。

## 错（两边不一致）
1. 块 4 读者视角「被复活的 Archivists 体系后来追捕过 Iris」：施事错置。原文追捕主语是中央图书馆——ch05："during The Central Library’s hunt for her"（text/ch05_chapter_5.txt）；ch05 另有 Miles 口径 "while Guardians hunted her"。无任何原文支持 Archivists 体系猎杀 Iris。→ **阻断，已改**（改为「复活 Archivists 的决定出自 Atalanthya，而追捕她的是中央图书馆（ch05 原文）」）。
   ⚠️ 整改过程自纠：首次修复误写「本块原句的 hunt for her」——该短语在 ch05 不在本块；已二次修正为 ch05 出处，并复核 /usr/bin/grep -l "hunt for her" text/*.txt → 仅 ch05_chapter_5.txt。

## 已核实为正确
- 块 2「I am the reason she left the Library」：text/ch10 命中，因果归属（Iris 离馆为 Aeloria）与原文语序一致。
- 块 4「雇主是 Atalanthya」：原文 "it was me who you called upon"——Aeloria 对 Atalanthya 说 you=Atalanthya 召唤，归属正确。
- 块 4「Atalanthya 以沉默回应」：text/ch10 "Atalanthya pursed her lips, remaining quiet." 命中。
- 块 9 两个理由的归属：better woman=Emerson、Adrien followed=同人质逻辑，与原文从句结构一致。
