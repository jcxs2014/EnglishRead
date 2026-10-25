# ch28 now there are two —— R3 差异单

对照物：`review/ch28/1-suread.json`（R1 独立素读，8 条）＋ `review/ch28/2-machine.json`。

## 单子一：漏（素读有、md 未体现；本章块数从 6 补到 8，仍在 ⑱ 3–8 内）
1. R1 第 3 条后半（`text/ch28_chapter_28.txt:34` `Hit me, scratched me, told me she wished I’d never been born. I never knew which side of her I’d get.`）——原来只写了「时好时坏、虐待」，具体动作与「后悔生下她」都缺。处置：**补为原句 3**（3 句 51 词）。
2. R1 第 5 条前半（`:55` `I thought it would just look like she’d OD’d.`）——md 里 `过量` 零命中，而这是 Lucy 唯一一次交代自己的算盘。处置：与「祖父知情」并列**补为原句 5**（2 句 29 词），旧的「两个也许」独立为**原句 6**（2 句 14 词）。
3. R1 第 1 条后半（`:16` 尸床上种的是卷心菜、胡萝卜和萝卜）——第 27、28 两章 md 均零命中。处置：写入一句话总结。
4. 源文 `:55` 末句 `And I guess now we know he buried her in the backyard. I always wondered what happened to her body.`——md `后院` 零命中。处置：写入一句话概括。
- 有落点的 4 条：Lucy 从背后抱住 Saskia、低声说十四岁杀母→原句 2；母亲十五岁生下她、瘾者、时好时坏→原句 2；靠着怒火与失眠的那一夜→原句 3 前半；保险箱密码、手写罪状与遗嘱冲进马桶→原句 5（旧）＋导航；章末那句「不是心脏病发，对吧」→原句 7（旧 6）＋导航。

## 单子二：编（md 有、素读无）
- 0 条。

## 单子三：错（md 与素读不一致）
- 0 条。四处回源核实：`:34` 的 `wished I’d never been born` 与三个动词；`:49` `grabbed a pillow`；`:55` `OD’d`／`feathers in her mouth`／`keyed locks`／`nailed shut`／`I was just as rotten as my mother`；`:16` `cabbage`／`radishes`。

## 派工人处置（3 条）
- 新增原句 3、5，拆分旧原句 4 为 5、6，重新编号为 1–8；一句话概括补后院与菜畦两处。改后 `chapter.sh` rc=0、`structure.py order` 29 md / 191 块 · 0 缺陷。
