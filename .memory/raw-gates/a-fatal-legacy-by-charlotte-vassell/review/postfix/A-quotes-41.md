# A-quotes-41.md · 增量复核任务 A · 41 条例句整句核验

- 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/`（记作 `$B`）
- 取清单命令：`git show 16b4f5738 --unified=0 -- '*.md' | grep -E '^\+\|' > /tmp/afl41.txt` → `wc -l` = **41**（与指令一致 ✓）
- **当前文件为准**：逐条按「词头 + 释义」在现文件中定位行，取现值（不拿 `git show 16b4f5738` 里的旧文本比）。
  ⇒ 41 条里 **40 条现值与 diff 旧文本逐字相同**；**唯一不同的是 ch05 `flats`**（`16b4f5738` 旧值 → `54016ca69` 已修），本表按现值核。
- 命中判据：`grep -F` 整串命中本章 `text/<文件>`（命中 ≥1 次算通过，0 次为阻断）。剥外层引号后另核一次，两者均 ≥1。
- 引号三态判据（**补记第 3 条口径**）：扫描例句，`‘`/`“` 记 +1、`’`/`”` 在 d>0 时记 −1，**d>0 ⇔ 悬空开引号**。
- 直/弯引号不一致按**提示型**判（§一·4）。
- 档位：**通过**＝核过且无缺陷；**阻断**＝必须改；**提示**＝只记；**假红**＝先修工具；**跳过/未核**＝给不出证据。

## 汇总

| 项 | 数 |
|---|---|
| 清单行数 | 41 |
| 整句逐字命中 | **41 / 41**（不命中 **0**） |
| 悬空开引号（d>0） | **0** |
| 孤儿收引号（无配对开引号） | **0** |
| 直/弯引号不一致 | **0** |
| 含 `…`（须分段查） | **0** |
| 两片段拼接（跨叙述标签 / 跨自然段） | **0** |
| 档位：通过 41 ｜ 阻断 0 ｜ 提示 0 ｜ 假红 0 ｜ 跳过 0 | |

引号态分布：**成对（完整引语）12 条** ＋ **无引号（裸摘录）29 条** ＝ 41。
（12 条成对＝4/11/13/14/15/18/19/22/30/33/34/6；其余 29 条为「原文该处仍在延续 ⇒ 去掉开引号」的真·片段，与 `16b4f5738` 提交说明的 A 类 12 / B 类 29 分类完全吻合。）

## 逐条明细

| # | 章 | 词头 | md 位置 | 例句（现值，逐字） | 整句命中 | 命中处 | 引号态 | 悬空 | 档位 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ch05 | `disbanded` | `ch05 the poisoned salad is investigated.md`:105 | You must be pretty disappointed that your special unit has been disbanded. A bit of a shock when that happened so suddenly. | **Y**（1 次） | `text/ch05_5.txt:44` | 无引号（裸摘录） | 0 | 通过 |
| 2 | ch05 | `flats` | `ch05 the poisoned salad is investigated.md`:124 | Half of the flats are empty. Investment properties. | **Y**（1 次） | `text/ch05_5.txt:144` | 无引号（裸摘录） | 0 | 通过 |
| 3 | ch10 | `whizzbang` | `ch10 caius cooks korean pancakes.md`:67 | I hung out with Innogen my old neighbour today, and her husband is a whizzbang surgeon down at St Barts. | **Y**（1 次） | `text/ch10_10.txt:50` | 无引号（裸摘录） | 0 | 通过 |
| 4 | ch11 | `offloading` | `ch11 matt and amy sort digbys papers.md`:101 | ‘He was serious if he was offloading the collection.’ | **Y**（1 次） | `text/ch11_11.txt:129` | 成对（完整引语） | 0 | 通过 |
| 5 | ch13 | `catalogue` | `ch13 matt and amy hunt for the real isolde.md`:96 | Not according to the catalogue. We accounted for everything. | **Y**（1 次） | `text/ch13_13.txt:135` | 无引号（裸摘录） | 0 | 通过 |
| 6 | ch16 | `backstory` | `ch16 isolde burrell denies the letters.md`:109 | ‘So someone used her life as the backstory for this “fake Isolde”.’ | **Y**（1 次） | `text/ch16_16.txt:226` | 成对（完整引语） | 0 | 通过 |
| 7 | ch16 | `ex-boyfriend` | `ch16 isolde burrell denies the letters.md`:111 | Me and my ex-boyfriend, Andy. | **Y**（1 次） | `text/ch16_16.txt:105` | 无引号（裸摘录） | 0 | 通过 |
| 8 | ch19 | `half-cut` | `ch19 the post office box leads to harrogate.md`:61 | No, the guy who reported it was apparently half-cut. | **Y**（1 次） | `text/ch19_19.txt:128` | 无引号（裸摘录） | 0 | 通过 |
| 9 | ch19 | `school dinner lady` | `ch19 the post office box leads to harrogate.md`:67 | Beverley? No. A bit too school dinner lady for Diggers. | **Y**（1 次） | `text/ch19_19.txt:47` | 无引号（裸摘录） | 0 | 通过 |
| 10 | ch19 | `PO Box` | `ch19 the post office box leads to harrogate.md`:74 | The PO Box is located in Barnet and was paid for by a Mrs Beverley Parkin, her address is in Harrogate. | **Y**（1 次） | `text/ch19_19.txt:20` | 无引号（裸摘录） | 0 | 通过 |
| 11 | ch19 | `Arrivederci` | `ch19 the post office box leads to harrogate.md`:82 | ‘Arrivederci.’ | **Y**（1 次） | `text/ch19_19.txt:155` | 成对（完整引语） | 0 | 通过 |
| 12 | ch21 | `trialling` | `ch21 benedict reports a break in.md`:64 | Well, I found out this morning that the Met is trialling a computer program that can track faces across multiple pieces of footage. | **Y**（1 次） | `text/ch21_21.txt:38` | 无引号（裸摘录） | 0 | 通过 |
| 13 | ch21 | `security` | `ch21 benedict reports a break in.md`:74 | ‘The Post Office in Barnet where the PO Box is located has security footage but only covering the days that the last three letters were likely sent or received.’ | **Y**（1 次） | `text/ch21_21.txt:32` | 成对（完整引语） | 0 | 通过 |
| 14 | ch21 | `covering` | `ch21 benedict reports a break in.md`:75 | ‘The Post Office in Barnet where the PO Box is located has security footage but only covering the days that the last three letters were likely sent or received.’ | **Y**（1 次） | `text/ch21_21.txt:32` | 成对（完整引语） | 0 | 通过 |
| 15 | ch21 | `received` | `ch21 benedict reports a break in.md`:76 | ‘The Post Office in Barnet where the PO Box is located has security footage but only covering the days that the last three letters were likely sent or received.’ | **Y**（1 次） | `text/ch21_21.txt:32` | 成对（完整引语） | 0 | 通过 |
| 16 | ch21 | `multiple` | `ch21 benedict reports a break in.md`:79 | Well, I found out this morning that the Met is trialling a computer program that can track faces across multiple pieces of footage. | **Y**（1 次） | `text/ch21_21.txt:38` | 无引号（裸摘录） | 0 | 通过 |
| 17 | ch21 | `computer program` | `ch21 benedict reports a break in.md`:80 | Well, I found out this morning that the Met is trialling a computer program that can track faces across multiple pieces of footage. | **Y**（1 次） | `text/ch21_21.txt:38` | 无引号（裸摘录） | 0 | 通过 |
| 18 | ch21 | `apparently` | `ch21 benedict reports a break in.md`:88 | ‘Apparently not.’ | **Y**（1 次） | `text/ch21_21.txt:50` | 成对（完整引语） | 0 | 通过 |
| 19 | ch21 | `coincidence` | `ch21 benedict reports a break in.md`:89 | ‘It could be a coincidence but we are running out of leads fast with this one.’ | **Y**（1 次） | `text/ch21_21.txt:50` | 成对（完整引语） | 0 | 通过 |
| 20 | ch22 | `M&S Food` | `ch22 matt questions beverley parkin.md`:83 | Hang on, Nigel. I think I dropped a card in M&S Food the other month. | **Y**（1 次） | `text/ch22_22.txt:95` | 无引号（裸摘录） | 0 | 通过 |
| 21 | ch24 | `seances` | `ch24 benedict opens his basement.md`:67 | Well, I was told by the old lady I bought the house off in 1973 that her mother had told her that the lady who lived here before their family did, had performed seances down here. | **Y**（1 次） | `text/ch24_24.txt:131` | 无引号（裸摘录） | 0 | 通过 |
| 22 | ch24 | `makeshift` | `ch24 benedict opens his basement.md`:83 | ‘It used to be the pantry and the kitchen when the house had servants, but now it really is just a makeshift library.’ | **Y**（1 次） | `text/ch24_24.txt:89` | 成对（完整引语） | 0 | 通过 |
| 23 | ch24 | `basement door` | `ch24 benedict opens his basement.md`:98 | Yes, like I said, the basement door was open. | **Y**（1 次） | `text/ch24_24.txt:101` | 无引号（裸摘录） | 0 | 通过 |
| 24 | ch27 | `zoo` | `ch27 callie has dinner with eulalia.md`:125 | We should get membership to the zoo when the baby is a toddler. | **Y**（1 次） | `text/ch27_27.txt:26` | 无引号（裸摘录） | 0 | 通过 |
| 25 | ch27 | `toddler` | `ch27 callie has dinner with eulalia.md`:126 | We should get membership to the zoo when the baby is a toddler. | **Y**（1 次） | `text/ch27_27.txt:26` | 无引号（裸摘录） | 0 | 通过 |
| 26 | ch31 | `supermodel` | `ch31 a second body is found at priory square.md`:79 | He probably purchased it before the finance bros moved in when it was the early days of Kate Moss and Sienna Miller supermodel boho. | **Y**（1 次） | `text/ch31_31.txt:125` | 无引号（裸摘录） | 0 | 通过 |
| 27 | ch31 | `accident` | `ch31 a second body is found at priory square.md`:107 | This one looks like an accident. | **Y**（1 次） | `text/ch31_31.txt:47` | 无引号（裸摘录） | 0 | 通过 |
| 28 | ch31 | `intruder` | `ch31 a second body is found at priory square.md`:110 | He was in the middle of a live-stream when an intruder was spotted on camera. | **Y**（1 次） | `text/ch31_31.txt:29` | 无引号（裸摘录） | 0 | 通过 |
| 29 | ch33 | `pentagram` | `ch33 the missing journal volume.md`:123 | I noticed there was a marking on the wall in his basement kitchen level that looked like a pentagram. | **Y**（1 次） | `text/ch33_33.txt:237` | 无引号（裸摘录） | 0 | 通过 |
| 30 | ch35 | `procrastinating` | `ch35 peter simpson calls on callie.md`:110 | ‘I was procrastinating earlier and read a report in the British Medical Journal on the effects of London pollution on tiny lungs.’ | **Y**（1 次） | `text/ch35_35.txt:284` | 成对（完整引语） | 0 | 通过 |
| 31 | ch37 | `salad` | `ch37 robbie takes over the case.md`:105 | Right, so let me get this straight: Digby Combe-Watson is killed by a poisoned salad by a woman supposedly called “Isolde” who was dressed as his intern. | **Y**（1 次） | `text/ch37_37.txt:44` | 无引号（裸摘录） | 0 | 通过 |
| 32 | ch47 | `Harrogate` | `ch47 mel comes out of surgery.md`:86 | Digby had been to Harrogate. | **Y**（1 次） | `text/ch47_47.txt:50` | 无引号（裸摘录） | 0 | 通过 |
| 33 | ch47 | `dodgy` | `ch47 mel comes out of surgery.md`:88 | ‘A lot of dodgy metaphors.’ | **Y**（1 次） | `text/ch47_47.txt:59` | 成对（完整引语） | 0 | 通过 |
| 34 | ch47 | `metaphors` | `ch47 mel comes out of surgery.md`:89 | ‘A lot of dodgy metaphors.’ | **Y**（1 次） | `text/ch47_47.txt:59` | 成对（完整引语） | 0 | 通过 |
| 35 | ch48 | `dogsbody` | `ch48 the case is rebuilt on the board.md`:97 | Picking that little incel to be her dogsbody was a stroke of genius. | **Y**（1 次） | `text/ch48_48.txt:98` | 无引号（裸摘录） | 0 | 通过 |
| 36 | ch48 | `subterranean` | `ch48 the case is rebuilt on the board.md`:99 | Is it possible that someone knocked through a basement wall and into any subterranean ruins? | **Y**（1 次） | `text/ch48_48.txt:286` | 无引号（裸摘录） | 0 | 通过 |
| 37 | ch48 | `alibied` | `ch48 the case is rebuilt on the board.md`:101 | Isolde was alibied by a friend called Keisha Jones who she was out running with in Walthamstow. | **Y**（1 次） | `text/ch48_48.txt:301` | 无引号（裸摘录） | 0 | 通过 |
| 38 | ch48 | `corpse` | `ch48 the case is rebuilt on the board.md`:126 | A corpse is a corpse. | **Y**（1 次） | `text/ch48_48.txt:41` | 无引号（裸摘录） | 0 | 通过 |
| 39 | ch48 | `taxi driver` | `ch48 the case is rebuilt on the board.md`:127 | Quick thinking of him to get the taxi driver to call the station. | **Y**（1 次） | `text/ch48_48.txt:26` | 无引号（裸摘录） | 0 | 通过 |
| 40 | ch53 | `hundreds` | `ch53 callie is finally sick.md`:95 | Yeah, hundreds of them. | **Y**（1 次） | `text/ch53_53.txt:53` | 无引号（裸摘录） | 0 | 通过 |
| 41 | ch54 | `plummeted` | `ch54 there is no heartbeat.md`:131 | That was necessary, and practical. Drug deaths have plummeted. Tourism is up. Who cares if I made a little from it? | **Y**（1 次） | `text/ch54_54.txt:286` | 无引号（裸摘录） | 0 | 通过 |

## 复现命令（逐条）

```bash
cd ~/Documents/Works/EnglishRead
B=notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell
# 例句取现值（词头 + 释义定位）
grep -n '^| whizzbang |' "$B/ch10 caius cooks korean pancakes.md"
# 整句命中
grep -F -c 'I hung out with Innogen my old neighbour today, and her husband is a whizzbang surgeon down at St Barts.' "$B/text/ch10_10.txt"
```

## 需要书主裁决的两点（只记，不改）

1. **ch05 `flats`（行 124）现值**：`Half of the flats are empty. Investment properties.`
   - 原文 `text/ch05_5.txt:144`：`‘No one on the square saw anything,’ Matt said, checking over his emails on his phone. ‘Half of the flats are empty. Investment properties. But one of the houses at the very end has a doorbell camera. …’`
   - 现值是**跨两个话轮的中途摘录**（前半在第 1 轮 `Matt said,` 叙述标签之前，后半在标签之后）。
   - 按 §一 的两类假红口径：两半**各自逐字命中**同一行原文，且现值本身是原文的**连续子串**（`grep -F` 命中 1 次）⇒ **不算拼接，不判红**。
   - 引号态：无开无收、无悬空 ⇒ 通过。
2. **ch24 `seances`（行 67）**含 `I was told … her mother had told her`，ch24 `basement door`（行 98）含 `like I said` ——
   这两处是**对白内容本身**，不是被拼进去的叙述标签；上下文回读已确认（`text/ch24_24.txt` 同段完整）。⇒ 不判拼接。

## 结论

任务 A **41/41 全部整句逐字命中，0 悬空引号，0 直弯不一致，0 拼接**。
本轮增量（`16b4f5738` + `54016ca69`）在这 41 条上**未发现缺陷**，无需改动任何一行。
