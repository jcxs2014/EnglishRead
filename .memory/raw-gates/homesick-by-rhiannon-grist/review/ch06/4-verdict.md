# ch06 4-verdict

- 文件：`ch06 macaroni pie and a tagged photo.md`
- 结论：**阻断 1 / 提示 1**

## 阻断

**阻断 1（"十年"是原文没有的数字）**
- 位置：导航·一句话概括"想起自己十年写促销邮件'对着虚空喊叫'"。
- 原文证据：`text/ch06_chapter_6.txt:77` 只说 "I spent my career writing to the five in one thousand"；`:83` "It was a lucky line of work to fall into in my twenties."（二十多岁入行）。全库检索 `text/` 也没有任何 "ten years" / "a decade"：

```
$ /usr/bin/grep -rn -i -E "ten years|a decade" text/
（无输出）
```

- 问题：她现年三十几岁（ch03:14 "in my thirties"）、二十多岁入行，读者可以推算"大约十年"，但原文没写；md 把推算写成事实，属于 R4 第 3 问明令阻断的"数字无据"。
- 建议改为：「想起自己整个职业生涯都在写促销邮件、"对着虚空喊叫"」——把时长交回原文的 "my career"。

## 提示

1. **位置**：词汇表三个档次标题"⭐⭐⭐ 高级 / ⭐⭐ 中级 / ⭐ 基础"。
   **问题**：本书其余章节的档名是"高级 / 进阶 / 常用"（如 ch05:81/93/105）。同一本书两套档名，读者会以为"中级"与"进阶"是不同档。
   **建议**：改回"⭐⭐ 进阶""⭐ 常用"。

## R4 三问

1. **谁做的**：点单、问推荐、脱口说"食物"、占插座、删留言、拉黑、合电脑、逃走，全是 Tamsin 做的，md 归属无误。留言来自"旧同学"（`:143` "a comment from an old school friend I hadn't spoken to in years."），标记她的是房产中介（`:152` "The comment was on a post from the estate agents who sold me the house."），md 均未张冠李戴。端派的是给她点单的同一个女人（`:110` "The same woman who'd taken my order"），md 写"店员"正确。
2. **关系/谁欠谁**：中介是卖房方、不是房东；旧同学是"多年没说过话"的熟人，不是朋友或仇人；咖啡馆店员是陌生人。md 未把任何一方写成亲属或雇主，正确。"被她标记"的方向也对：是中介标记她，不是她标记中介。
3. **数字与死因**："万分之五"有据：`:77` "zero point zero five per cent"＝0.05%＝万分之五，md 换算正确（注意原文后句 "the five in one thousand" 若按 0.05% 算应为千分之零点五，是原文自身的松动，md 取百分比一侧，可接受）；"两个插座"有据（`:71` "taking up both sockets"）；"百分之三十七"有据（`:188` "Only thirty-seven per cent charged."）；"三家咖啡馆/三家餐馆/百分百安格斯"有据（`:5`）。"十年"无据，已列阻断。本章无死亡。

## 已核实为正确（下一轮不要改坏）

- 原句 1–6 六条引语逐字无误：`:5`（bunting/jam jars）、`:17`（duck-egg blue / ceramic stands）、`:71`（escaped / both sockets）、`:104`（So what if / Everyone hates their job）、`:164`（worst thing about the internet / missing persons groups）、`:179`（the noise echoed / gone silent）。
- 导航对落点的概述全部可回溯：桥边小店（`:8`）、Maggie's Café（`:17`）、macaroni pie（`:53`）、窗边插座（`:71`）、无回信（`:119`）、"Congrats on the move!"（`:146`）、中介帖（`:152`）、删评拉黑合电脑（`:176`）、落在店里的派（`:191`）。
- "对着虚空喊叫"对应 `:77` "It had often felt like screaming into the void."，是原文比喻，未错置。
- 词汇 20 条例句均可逐字检得；"skittish""jeopardy""enigmatic""dilapidation" 的释义与语境相符。
