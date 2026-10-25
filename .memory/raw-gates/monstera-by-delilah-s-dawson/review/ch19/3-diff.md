# ch19 the limits of normal —— R3 差异单

对照物：`review/ch19/1-suread.json`（R1 独立素读，8 条，2026-10-25 新做的 T3 版）＋ `review/ch19/2-machine.json`（R2）。

## 单子一：漏（素读有、md 未体现）
**2 条，均已补**：
1. R1 第 2/3 条（`text/ch19_chapter_19.txt:25` `She read a story on Buzzfeed last week about a man who went to the hospital for suspected lung cancer, but when the doctors cut him open, they instead found a tiny fir tree. Two inches of life, quietly germinating in a human lung.`）——md 只在导航 Tropes 里一句「翻出肺里长冷杉的旧闻」，`两英寸` 零命中。这段是本章唯一一条「外部先例」，Lucy 正是拿它去套自己眼前的怪事。处置：补写为**原句 1**（44 词 2 句），旧 1–5 顺延为 2–6。
2. R1 第 7 条（`:85` `Lucy eats her soup—with toast, as she will never want to smell cornbread again—and reads her book and works on a puzzle and goes to bed. She thinks about Saskia, because these days, she always thinks about Saskia, but now the thoughts come with doubts.`）——md 里 `吐司` 零命中，且「现在想起 Saskia 会带着疑虑」这层转折完全缺席。处置：补写为**原句 5**（45 词 2 句），旧 5 顺延为 7。
- 其余 6 条有落点：眼角小苗→导航＋原句 6；六英寸拥抱→原句 3；`Not sure. See you later!`→导航（4 处提及）；橡皮门挡→导航＋原句 4；玉米面包气味→原句 7；章末 `No! You bitch!`→导航＋一句话总结。
- 块数 5→7（⑱ 3–8 内）。

## 单子二：编（md 有、素读无）
- 0 条。

## 单子三：错（md 与素读不一致）
- 0 条。两处回源核实：
  1. 导航 `That’s wild` 与 `Not sure` → `:31`／`:58` 逐字命中。
  2. 导航「一个人被关在家里将近十年」→ 原句 4（`:100`）承载，ch14/ch15/ch17 的同一口径一致。

## 派工人处置（2 条）
- 新增**原句 1**（Buzzfeed 冷杉与两英寸）与**原句 5**（吐司、拼图与 doubts），块数 5→7；改后复跑 `chapter.sh` rc=0、`structure.py order` 29 md / 184 块 · 0 缺陷。
