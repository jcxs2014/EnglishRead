# ch05 4-verdict

- 文件：`ch05 the bridge and the fifty pound notes.md`
- 结论：**阻断 0 / 提示 4**

## 阻断

（无）

## 提示

1. **位置**：导航·一句话概括"她向推着轮椅老伴的老先生问早"；一句话总结"推着轮椅老伴的老先生"。
   **问题**：原文只说 "pushing a wheelchair bearing an equally ancient lady"（`text/ch05_chapter_5.txt:167`），从未说两人是夫妻；`grep -i -E "wife|husband|widow"` 无命中（exit=1）。"老伴"是替作者补上的亲属关系，与本章"世界根本不解释自己"的调子相反。
   **建议**：改为"推着轮椅、椅上坐着一位同样苍老的老太太的老先生"。

2. **位置**：词汇表·⭐⭐ 进阶 anorak 释义"防风外套，连帽衫式外套"。
   **问题**：anorak 是带帽的防风/冲锋外套（英式常用，正对应本章徒步者的装束），"连帽衫"是 hoodie；同章正文提到同事穿的是 "hoodies and t-shirts"（`:53`），两个词被注释混成一件衣服。
   **建议**：改为"带帽防风外套，冲锋衣"。

3. **位置**：词汇表·⭐⭐⭐ 高级 standoffish 行，原文例句列空白。
   **问题**：该词在原文出现且是全章自我审判的落点：`text/ch05_chapter_5.txt:149` "Standoffish. Snobbish. A cold fish."（导航·人物弧线也引了这句）。
   **建议**：例句填 "Standoffish. Snobbish. A cold fish."

4. **位置**：导航·人物弧线"那是她唯一一次被人主动邀请"。
   **问题**："唯一一次"是全书级断言，但上一章邻居已经主动邀她进屋：`text/ch04_chapter_4.txt:140` "“Would you like to come in?”"；本章范围内也只覆盖职场。绝对化之后与 ch04 相抵。
   **建议**：改为"那是她在城市/职场时期唯一一次被人主动邀请"。

## R4 三问

1. **谁做的**：喊"早"的是梯磴上的灰胡男人（`:17`）；嘟囔"乡下不是该很友好吗"的是**他的同伴**（`:26` "one of the man's companions muttered"），md 写"其中一人嘟囔"归属正确；说"抱歉，我有事"的是 Tamsin（`:140`），md 未推给 Issy；掉钱的是老先生（`:185` "fluttered out of his pocket"），不是 Tamsin 掉的——md 原句5 分析"她可以捡走"正确；放屁的是老人（`:194`）。
2. **关系/谁欠谁**：老人与轮椅上的老太太关系**原文未交代**（见提示1）；Issy 是同事、不是上司；打电话的"大概是 Mel"是 Issy 的推测，md 未坐实为 Mel 本人；Alan 是邻桌同事，md 未给他别的关系。
3. **数字与死因**："两张五十镑"有据（`:185` "Two fifty-pound notes."）；"六点"有据（`:131` "By the time it came to six o’clock"）；"两号大"有据（`:167` "two sizes too big for her"）。本章无死亡；"a dying pink butterfly" 是比喻，md 原句5 按比喻处理，正确。

## 已核实为正确（下一轮不要改坏）

- 导航对全章三段结构的概括与原文一致，无章号错标：徒步者（`:14-29`）→ 办公室闪回（`:41-164`）→ 桥头（`:167-206`）。
- 原句 1–6 六条引语逐字无误；`:17` 的 "similarly anoraked"、`:32` 的 "hiker, dogwalker and weekender"、`:44` 的 "Do no harm, take no shit."、`:194` 的 "a low, singular parp" 均可原样检得。
- "父亲是邮差、母亲是护士"（`:44` "My dad was a postman, my mother a nurse."）正确，未编造职业。
- "她没有电脑、只有笔记本和座机"（`:47` "There was no computer. Just a branded notebook and a desk phone."）正确。
- 山/浪与挥手同词（wave）的读法有据，属分析而非事实断言。
