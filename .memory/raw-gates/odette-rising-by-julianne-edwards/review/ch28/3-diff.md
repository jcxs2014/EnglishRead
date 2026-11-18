# 3-diff · ch28 castel odette（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到 Berthe 住父亲旧床（羽绒垫托请）、Louis 天天探视被拒、Castel Odette 命名场、Ned 誓言守护（含 Feld 与孩子们）、相片来自 Grant 家宅合影——md nav/原句上下文承担（命名与誓言未入精读块） | 13 块预算给了 pimp 揭底/镜子/Doudou/badness 四幕 | 提示（不修） |
| 漏 | 无 | 其余 7 条（spirit 被剜/pimp+paid off+for fun/corrupted 权力网/mirror raw+wordless/Doudou+Aphrodite+一拳/without equal+the end/brothel 十三岁+Grace/相片镜像+badness+放下）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「Victor Gagnon」＝Grimard；「I was taken to a brothel」＝Berthe；「He did not hate you…You took on his feelings of badness」＝Ned——md 归对 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- spirit 被剜：text "As if whoever had cut her face had also cut out her spirit." ↔ md 原句1 ✅
- paid off：text "He did the only thing he could: he paid him off." ↔ md 原句2 上下文（suread）✅
- corrupted：text "protected by the men he has corrupted" ↔ md 原句3 ✅
- 镜子：text "“It will always be raw.”" ↔ md 原句4 ✅
- Doudou：text "My grandmother said I was the ‘Aphrodite of the Windward Islands.’" ↔ md 原句5/6 ✅
- brothel：text "“I was taken to a brothel.”" ↔ md 原句10 ✅
- badness：text "“You took on his feelings of badness.”" ↔ md 原句12 上下文 ✅
- 放下：text "Perhaps it’s time to let them go." ↔ md 原句13 ✅

## 取证命令示例

/usr/bin/grep -c "Castel Odette" notes/books/novels/odette-rising-by-julianne-edwards/text/ch28_chapter_28.txt → 1；退出码 0
/usr/bin/grep -c "You took on his feelings of badness" notes/books/novels/odette-rising-by-julianne-edwards/text/ch28_chapter_28.txt → 1；退出码 0
