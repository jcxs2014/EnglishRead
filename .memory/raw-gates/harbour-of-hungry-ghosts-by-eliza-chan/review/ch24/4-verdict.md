# ch24 判定（Lessons 章 · 快审）

- 机器层：`chapter.sh --json` rc=0；7 块逐字全中；gate 0 阻断。
- 人判：**1 阻断**（引语截短致「作者不重述失言」为假，证据 `text/ch24_lessons.txt:64`）+ 4 提示（漏）。
- `check_summary_names` 提示 → **假红**（导航「Kiamling」是叙述层用名，正文称 Miss Kim）。

## 已核实为正确
- 情诗是**他**用粤语说的，脸红/耳红是**她**（`her ears had gone completely red`），归属无误。
- 「狮子应朝外」是她的判断，不是他的；他接的那句才是失言。
- 捂嘴动作发生在**他讲特里斯坦故事的中途**，不是讲错时（改稿后仍须保持）。
- 结尾 `That was the last thing he remembered` 是她视角外的叙述句，非他的内心。

## 修复复验（2026-10-22 21:35，执行方＝本会话）
- 已按指令改 `ch24 lessons.md:58/60/64`：引语从同段 `“It’s just a lark, they aren’t really providing protection.”` 起（48 词、3 句），中文理解与「为什么」同步改为「先把失言摆出来，再写知道的那一瞬」。
- `bash scripts/chapter.sh "<书>/ch24 lessons.md"` → **CHAPTER_EXIT=0**，引语块 7 / 片段 8 / 查无 0，关键词全在引语内。
- `bash scripts/gate.sh` → **rc=0**（正门 0 条阻断）；`verify_fragments_indep` 580 片段 0 MISS；`check_chinese_layer` 阻断 0。
- 结论：**该阻断已闭合**，本机快审由此 0 条未闭合阻断。
