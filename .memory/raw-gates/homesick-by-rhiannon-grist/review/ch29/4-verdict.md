# ch29 4-verdict

- 文件：`ch29 the forestry garage.md`
- 结论：**1 阻断 / 4 提示**

## 阻断

### B1 词汇表「常用」档 108–122 行整段破损（表格被正文段切断）
- 位置：`ch29 the forestry garage.md:108-122`
- 现状：`| banned | 被禁的 | “How long were you banned for?” |` 之后，原文三段对白被当成表格续行塞进来（`“Six months.”`、`“Six months? `），随后 `| saluted | … |` 又被 `Rowan saluted. |` 重复一遍；渲染后表格中断、出现游离引语与重复行。
- 原文证据：对白确为三个独立自然段——`text/ch29_chapter_29.txt:125`「“How long were you banned for?”」、`:128`「“Six months.”」、`:131`「“Six months? How come it’s taken you so long to retake the tests?”」（`/usr/bin/grep -n "Six months" text/ch29_chapter_29.txt` → 128、131，rc=0）。
- 建议改后（保留 108、118、122 三行，删除 109–121 全部游离行）：
```
| banned | 被禁的 | “How long were you banned for?” |
| saluted | 敬礼 | Rowan saluted. “I consider myself telt.” |
| scrunched | 皱起 | Her eyebrows scrunched together even more, which was impressive. |
| shed | 棚屋 | It had the same lovely, musty, earthy smell as a garden shed. |
```
- 备注：承 2026-10-22 复核指令 §1-D（词汇表行破损）同一口径；附 A 只登记了本章第 93 行 `handicap`（现已带尾 `|`），**108–122 这段不在附 A**，属新见。

## 提示

1. `:30`｜「读者刚读完上一章的斧头与围巾」——ch28 只有围巾、全书无 axe：`/usr/bin/grep -n -i "axe" text/ch28_chapter_28.txt` 无命中（rc=1）。斧头意象出自 ch09/ch11/ch18。建议改「读者刚读完上一章的围巾，也还记得前几章那把斧头」。
2. `:70`｜「它不来自 **Rowen**」——人名拼错，全书为 Rowan。改「Rowan」。
3. `:72`｜「把**前十七章**的『自卫』叙事彻底翻面」——本章是第 29 章，此前共 28 章，17 无据。建议改「前二十八章」或「此前各章」。
4. `:12`｜导航把 Maggie 送别整段（改建谷仓、温室、咖啡馆道歉、叮嘱喂饭）略去；事实无误，但这是 Tamsin 社交修复的唯一正面节拍。提示级，可在导航一句话概括补半句，不补也不算错。

## R4 三问

1. **谁做的**：Rowan 开车送 Maggie 回家 → 问早饭、逼她吃三块燕麦饼（`text/ch29_chapter_29.txt:8`）→ 带她进林业车库搬树苗（`:41`,`:47`）→ 把卡车钥匙抛给她（`:59`）。Tamsin 开车回程（`:77`）、向 Maggie 道歉（`:26`）、旁听路怒自述、结尾盘算撞车（`:158`）。全章无第二施事者动手。
2. **什么关系 / 谁欠谁**：Rowan＝邻居兼雇主（她替他植树，`:44`「exciting world of tree planting」）；Maggie＝熟人/朋友（咖啡馆相识，`:29`）；Tamsin 单向受惠（早餐、信任、工作），无金钱债务、无亲缘。复制体/1a 线本章完全不出现。施害-受害归属：路怒受害者是**另一名女司机**（`:122`「She hadn’t done anything」），Rowan 是施害方且已认错；Tamsin 是潜在施害方（`:158`）。
3. **数字与死因**：`at least three`（燕麦饼，`:8`）、`a few years back`（丢照，`:92`）、`Six months`（禁驾期，`:128`）、`a few tries`（扛树苗，`:56`）——全部有逐字依据，md 正文未误用任何数字。**本章无死亡**；「smacking an axe into someone’s face」是她的幻觉假设（`:11`），不是案件事实。

## 已核实为正确（下一轮不要改坏）

- 原句 1–5 逐字命中 `text/ch29_chapter_29.txt:11 / 77 / 116 / 155 / 158`（含 `It’s criminal`、`the petrol use`、`until it cracked`、`rant at him in the pub`、`crash the truck just right`）。
- 官方措辞「Excessive use of the horn. Threatening other drivers. Driving irresponsibly.」逐字（`:116`）。
- 受害司机为女性、且「had right of way」是录像回放后确认的（`:122`）——md 未写反施害/受害。
- 「Tourists never saw this place. Only staff. And their friends.」（`:47`）未被误写成"对外开放"。
- 词汇例句 `handicap` / `footage` / `deficiency` / `hallucinate` / `traipsed` / `compost` / `cinder` 均出自本章原文。
