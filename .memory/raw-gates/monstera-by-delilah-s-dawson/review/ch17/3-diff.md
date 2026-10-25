# ch17 someone gets hurt —— R3 差异单

对照物：`review/ch17/1-suread.json`（R1 独立素读，8 条）＋ `review/ch17/2-machine.json`（R2）。

## 单子一：漏（素读有、md 未体现）
**1 条，已补**：
1. R1 第 3 条（`text/ch17_chapter_17.txt:64` `“Do you have a—a girlfriend?” Lucy asks suddenly, her greatest fear rushing out of her mouth. “Is that why you wore the mask? Or a boyfriend? Or whatever?”`，回答在 `:67` `Saskia shakes her head. “Nope.”`）——md 里 `女朋友`／`口罩`／`Nope` **全部零命中**：这是全章唯一一次由 Lucy 主动改换话题，也是全书唯一一次有人当面问到那只口罩（ch12/ch13/ch15 都出现过、她一直没敢问）。原先把这块内容完全交给导航造成空档。处置：补写为**原句 4**（28 词 2 句），旧 4–8 顺延为 5–9。
- 其余 7 条均有落点：警报与玉米面包／踉跄回跑→导航＋一句话总结（词表 `alarm blares`）；按住烤箱、OFF 键与警告→原句 1＋导航；`nothing wrong with you`→原句 5；沸汤溅背与 `See? Someone gets hurt.`→原句 7；Roger 站在卧室门口→原句 8＋导航；插座与加租十美元→原句 9＋词表 `camera`；`Saskia left the door open`→导航＋一句话总结。
- 块数 8→9（⑱ 配额 3–8 上浮 1 块，见 4-verdict R5 第 9 行）。

## 单子二：编（md 有、素读无）
- 0 条。

## 单子三：错（md 与素读不一致）
- 0 条。三处易错点回源核实：
  1. 导航「手机里的那条提示和烤箱门的响声接替警报」——正确：`:166` `“I got an alert that a fire alarm went off in here.” He holds up his phone` 与 `:187` `after slamming the oven door`。
  2. 导航「那种讨好祖父多年练出来的笑」——与 ch01 立下的设定一致（说谎或讨好时「脸上挂起同情的面具」），本章表现为白板加租十美元。
  3. 导航「警报的 klaxon 被比成祖父讲道」——正确，`:19` 一带（词表 `preaching` 例句逐字命中）。

## 派工人处置（1 条）
- 新增**原句 4**（女朋友／口罩／Nope 一问），块数 8→9；改后复跑 `chapter.sh` rc=0、`structure.py order` 29 md / 180 块 · 0 缺陷、`gate.sh` 正门 0 条阻断（⑱ 提示型含本章 9 块一条）。
