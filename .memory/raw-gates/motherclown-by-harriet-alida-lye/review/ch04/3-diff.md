# ch04 · R3 对账（Chapter Three，md：`ch04 chapter three a witness.md` / 原文 `text/ch04_chapter_three.txt` / 6,257 词）

R1 事实 8 条（独立子代理，锚点 8/8 唯一）。

## 漏（素读有、md 无）

| # | 素读事实 | 原文锚点 | md 位置 | 判 |
|---|---|---|---|---|
| L1 | 订的是明晚的红眼航班 | `She opens the ticket-booking website`（216–292） | 原句 1 只写「单程票更贵」，未写红眼／明晚 | 提示（细节，不影响「单程」这一判断） |
| L2 | 房源要求先付两千欧押金，她付了两个月共六千 | `The posting stipulates a two-thousand-euro`（1619–1687） | md 正文未收金额（ch14「被骗六千欧」是同一笔） | 提示（数字细节；ch14 会正面出现） |
| L3 | Laura 的儿子 Charlie 与 Elisabeth 同龄（相识时都是六个月） | `Elisabeth and Charlie, Laura’s son,`（4827–4882） | 未收 | 提示（关系细节，后文用得上但不属本章主线） |
| L4 | 她回家把到达时间与住址邮件发给女儿 | `Catherine emails Elisabeth her arrival`（11311–11368） | 未收 | 提示（与 ch02「女儿不回信」呼应，md 未点） |
| L5 | Laura 听到决定后停顿，反问「去哪里」 | `A pause. “Go where?” Not`（7943–7997） | 原句 6 只有她自己的辩解，未收 Laura 的反应 | 提示（md 已用原句 7 的「死亡/生命」对答承担 Laura 的反驳） |

## 编（md 有、原文无）

| # | md 表述 | 原文核查 | 判 |
|---|---|---|---|
| — | 未发现。导航与十五块的中文叙述均可回指原文 | — | 通过 |

## 错（两边都有但不一致）

| # | md 表述 | 原文 | 判 |
|---|---|---|---|
| E1 | 原句 8 分析「bravest 这个词放在**四十一岁**的女人身上」 | `text/ch02_chapter_one.txt:345`：`Catherine is forty. Only forty!`；ch01 原句 4 `She was only forty.`。全书无 forty-one | **阻断**：年龄多算一岁 → 已改「四十岁」 |

## 逐字复核（抽样）

| 例句 | 原文命中 | 判 |
|---|---|---|
| `She ends up booking a one-way, even though it’s more expensive.` | ✓ | 通过 |
| `Tonight is the night.` 类短句不属本章词汇 | — | 跳过 |

取证：`/usr/bin/grep -rn "四十一" notes/books/novels/motherclown-by-harriet-alida-lye/*.md` → 仅本章 1 处（已修）；`/usr/bin/grep -n -i -E "forty-one|forty one|forty\b" text/*.txt` → 无 forty-one，只有 `Catherine is forty. Only forty!`（ch02:345）。
