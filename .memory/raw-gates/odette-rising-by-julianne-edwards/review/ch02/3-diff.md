# 3-diff · ch02 the mouse and the will（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 无 | R1 8 条（刀片乙醇/挂条谢客/三天三夜+Merry 名与年龄/赠鼠+Polo 命名+重新点单/律师信/遗产清单/132 人/失言 cruelty）md 全覆盖 | — | 无漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：B7 "Of course I am not acquainted with this area of Paris" 说话人＝律师（紧跟 Odette "No, sir" 之后、由律师继续陈述购置日期；Odette 下一句才是 "That's his birthday"）——md 归律师 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- 自伤装备：text "a wafer of a blade, stolen and stashed with torn cloths and ethanol"（480:547）↔ md 原句1 ✅
- Merry 名与年龄：text "Merry? The English word for 'happy'?" + "about seventeen; four years younger than her"（1539:1606 邻域）↔ md 导航「约十七岁、比她小四岁」✅
- 遗产三件：工厂（Rue Brancas）/巴黎房产（Six, Rue Jean Bart，购于去年二月八日＝父生日）/存款（8140:8215）↔ md 原句6+原句7 ✅
- 132 人：text "one hundred and thirty-two souls under his employ"（10215:10271）↔ md 词汇表 appraised 例句 ✅
- 失言：text "he can't very well ask your father, can he?" he hissed（10364:10426）↔ md 原句8 ✅

## 取证命令示例

/usr/bin/grep -c "one hundred and thirty-two souls" notes/books/novels/odette-rising-by-julianne-edwards/text/ch02_chapter_2.txt → 1；退出码 0
/usr/bin/grep -c "the eighth of February last year" notes/books/novels/odette-rising-by-julianne-edwards/text/ch02_chapter_2.txt → 1；退出码 0
