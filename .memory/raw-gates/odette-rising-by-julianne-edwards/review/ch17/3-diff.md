# 3-diff · ch17 saved on the wall（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到仆役区探索（洗衣房两条衬裤/Dendron 房清空如惊愕之口/厨娘房枕上棕发）与「utterly relieved, and utterly lost」——md nav「仆役尽空」承担一部分；两个情绪句未入精读块 | 取舍理由：13 块预算给了身世消化+摧毁+危机+救援四幕 | 提示（不修） |
| 漏 | 轻微 | R1 提到面包房赊账户头（"The Huré household has an account with us"）——md nav 未展开；蛋糕来源在原文有账户细节 | 同上 | 提示（不修） |
| 漏 | 无 | 其余 6 条（不是母亲之女/懦夫候选/砸桌/other nests/镜中 sin/母亲为何不来/冻死盘算/Polo 唯一牵挂/both die/救援/It's all right）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：蓝门叙述＝Merry（ch04 已核）；「We will both die here then」＝她内心；「It's all right」＝Berthe——md 归对 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- 身世消化：text "Cruel enough to force his poor wife to raise her, the baby, as her own?"（1107:1178）↔ md 原句1 上下文 ✅
- 仆役尽空：text "Madame Dendron had gone."（4472:4496）↔ md nav「仆役尽空」✅
- Nanette 推断：text "The woman he’d seen in the shadows must have been the maid, Nanette."（6376:6444）↔ md suread 事实（1-suread.json）✅
- 砸桌：text "the table collapsed, pitching her forward, face smashing into the hard surface"（8536:8614）↔ md 原句3 ✅
- other nests：text "he had made other nests in which to live and pour his love"（9400:9465 邻域）↔ md 原句4 ✅
- 面包房账户：text "The Huré household has an account with us. Madame Dendron settles it weekly."（19318:19394）↔ md nav（蛋糕来源）——提示级未入精读 ✅
- 冻死盘算：text "To die at one’s own choosing and full of cake was surely to die well."（21299:21368）↔ md 原句9 ✅
- 救援：text "there was Berthe, sliding down from the carriage, her cape shimmering"（23680:23749）↔ md 原句12 ✅

## 取证命令示例

/usr/bin/grep -c "To die at one’s own choosing and full of cake" notes/books/novels/odette-rising-by-julianne-edwards/text/ch17_chapter_17.txt → 1；退出码 0
/usr/bin/grep -c "Madame Dendron had gone." notes/books/novels/odette-rising-by-julianne-edwards/text/ch17_chapter_17.txt → 1；退出码 0
