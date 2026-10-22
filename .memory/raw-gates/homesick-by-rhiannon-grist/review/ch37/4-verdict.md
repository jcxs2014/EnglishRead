# ch37 4-verdict

- 文件：`ch37 the herd and the hill of bones.md`（128 行）
- 结论：**2 阻断 / 3 提示**

## 阻断

### B1 词汇表「⭐ 常用」档断裂：表行后空行 + 无表头的 5 行
- 位置：`ch37 the herd and the hill of bones.md:113-123`
- 现状：
  113–114 是表头与分隔行，115 是 `| wren | 鹪鹩 | A wren trilled in the branches above. |`，116–118 三个空行，119–123 直接接 `| tusks | 獠牙 | … |`、`| claws | … |`、`| corpses | … |`、`| skull | … |`、`| key | … |`，没有表头、没有分隔行。
- 问题：后半截五行脱离表格，渲染时会掉出表外或并进上一段；这正是 2026-10-22 复核指令 §1-D 定为阻断的“词汇表行破损”（`|`-行不以 `|` 结尾或含 `| |` 的同类结构损坏）。`check_vocab.py`/`gate.py` 不报此类，只能人眼抓。
- 建议改后：删掉 116–118 的空行，让 119–123 紧接 115 行，恢复成一张表；或在 116 处补一行表头 `| 词/短语 | 释义 | 原文例句 |` 与分隔行 `|---|---|---|`，把 tusks–key 五行接成第二张表。

### B2 读者视角提示把老妇人安到了“上一章”，且状态写错
- 位置：`ch37 the herd and the hill of bones.md:82`
- 现状：「老妇人**上一章**还坐在轮椅里**打鼾**。」
- 问题一（章号错标）：第 36 章全章没有老妇人。取证：
  - `/usr/bin/grep -rn -i "wheelchair" text/ch3[0-9]_chapter_*.txt` → 只命中 `text/ch37_chapter_37.txt:170`，rc=0；ch36 无。
  - `/usr/bin/grep -rn -i "old woman\|old lady" text/ch*_chapter_*.txt` → 命中 ch11:80/86、ch22:29/38/65、ch37:170/182/191、ch38:131、ch40:14 起；ch36 无。
  她**最近一次**出场是第 22 章（`text/ch22_chapter_22.txt:29`「I heard the squeak of the old woman’s wheelchair.」／`:65`「The old woman snorted as he jolted her back into momentum.」），再早是第 11 章（`text/ch11_chapter_11.txt:80`「He clutched the handles of the wheelchair carrying the sleeping old woman」／`:86`「The old woman in the chair stirred in her sleep.」）。
- 问题二（状态不准）：第 11 章是“睡着”、第 22 章是“被颠得哼了一声”（snorted），没有“打鼾”（snoring）。
- 建议改后：「老妇人第 22 章还坐在轮椅里打瞌睡（第 11 章也在轮椅上睡着），本章醒来后的第一件事是喊停，然后说“该聊聊了”，手里是一卷红线。」

## 提示

1. `:44`（原句 3）｜引语跨段：`text/ch37_chapter_37.txt:56`「I recognised their faces!」是独立一段，`:59`「I saw Fergus rooting…」另起一段。建议中间加 `…`。
2. `:54`（原句 4）｜引语跨段：`:74` 段末「…that quiet pressure to be productive.」之后，`:77`「Produce or be the product.」是单独一行成段。建议在引语中保留换行或加 `…`。
3. `:74`（原句 6）｜引语跨段：`:182`「The old woman huffed.」与 `:185`「“Enough,” she said…」之间隔着空行。建议加 `…` 或拆成两条。
4. `:20`（导航·叙事手法）｜「暴力段落用极短的句子切成碎片」——大体对，但原文这段其实多用**长句**（`:65` 一整段三个动作一气写完），短句集中在 `:77`–`:83` 的口号与 `:95`–`:113` 的内心短句。建议改成「暴力段落用长句一气推完，再用短句口号与内心短句切开」；此条不改也不算错。
5. `:12`（导航·一句话概括）｜「每具骷髅嘴里都咬着一把比她更旧的钥匙」——“更旧”只对**越往堆里走**的那些成立（`text/ch37_chapter_37.txt:161`「getting older and older as if going back through time」），紧挨着她的那具未必更旧。建议改「一把把越来越旧的钥匙」。此条为细节精度，不改也可。

## R4 三问

1. **谁做的**：本章有两层施事。**现实层**只有 Tamsin：她自己走进林子、自己幻想长毛、自己爬上尸山躺下（`text/ch37_chapter_37.txt:26`／`:149`）。**幻象层**：Fergus 用獠牙捅死青少年（`:65`「Fergus ran his tusk into the kid’s stomach as easy as plunging a spoon into whipped cream.」），青少年群起撕他、拔掉一只眼（`:65`），旧同事们咬颈吃掉两个 Grayson 女孩（`:68`），Rowan 扯掉一个同事的头（`:98`）；**shadow（影子）**只是旁观与进食（`:62`／`:86`「The shadow on the edge of the clearing cackled. Cackled with a too-wide grin.」／`:119`「sat that shadow」），没有动手杀谁。**老妇人**是唯一制止者：`Enough`（`:185`）。
2. **什么关系／谁欠谁**：兽群＝**她认识的人**（Fergus、村里的青少年、Viv、Maggie、旧同事、Grayson 女孩、父亲眼镜的鹤、鹿腿女人、Rowan）——“熟人长兽件”，不是陌生人。shadow＝邻居（too-wide grin 与 ch35:104「that wide, tooth-filled smile」同一记号），本章它**没有索要任何东西**，只是吃；她与它的关系在这一章被她自己改成“让位”：`text/ch37_chapter_37.txt:14`「Let the thing that was my neighbour take the house, take my life, my identity.」——复制体–本体在此不是抢夺，是**本体自愿交出**（这是全书的转折）。老妇人–shadow＝压制关系（一声“够了”即驱走）；老妇人–Tamsin＝**债权人**姿态：她递出钥匙求救（`:176`「I reached out to her, offering the key in my hand.」／`:179`「Help me… I want to stop this, but I don’t know how.」），老妇人接下这个请求。谁欠谁：Tamsin 欠自己一次“承认”（`:143`「I was a fucking monster.」）；她对邻居不欠，对 Fergus 等村人也不欠——本章的债是**她与这栋房子/这条血脉**之间的，钥匙是凭证。
3. **数字与死因**：**没有真实死亡**——所有杀戮都发生在幻象/梦里，章末她“醒了”（`:203`「Then she pulled the knot tight and I woke.」）。幻象内的死法有据：青少年被獠牙捅腹、肋骨架被掰开（`:65`／`:89`）；两个女孩被咬颈吃掉（`:68`）；一个同事被扯掉头（`:98`）。**钥匙年代**共五档：`Square-head keys became small brass keys became sturdy iron keys became simple picks of metal became a slab of wood.`（`:161`）——五档，不是“无数把”。无年龄、无日期、无金额；md 未编数字（`md:128` 只说“一把更旧的钥匙”，属精度问题，见提示 5）。

## 已核实为正确（下一轮不要改坏）

- 原句 1、2、5 逐字命中 `text/ch37_chapter_37.txt:8 / 26 / 134`，均为单段连续。
- 原句 3 的前半句 `I recognised their faces!` 确在 `:56`，后半句在 `:59`——两段相接，md 未改字。
- 原句 6 的 `“Enough,”` 后确实接 `she said to the creature on the pile.`（`:185`），且 `She’d barely raised her voice…` 同段，引语文字无误。
- “老妇人上一章打鼾”之外的读者视角判断（“从酒馆里的怪老太变成掌控者”“手里是一卷红线”）有据：红线轴在 `:194`「In her lap she had a spool of red thread.」。
- 导航“空心山”不是编的：`text/ch14_chapter_14.txt:158`「“That’s a hollow hill.”」、`text/ch27_chapter_27.txt:44`「Fergus’s story about the hollow hill」、`text/ch46_chapter_46.txt:59`「Hollow hill. Fairy hill.」。
- Viv 的斑马不是 md 编的：`text/ch34_chapter_34.txt:23`「a simple sweatshirt with one neon pink zebra in the centre of it today」、`text/ch15_chapter_15.txt:59`、`text/ch28_chapter_28.txt:41`「Loves a zebra.」——“前面的玩笑成了预言”成立。
- 一句话总结“把她从梦里叫醒”有据（`:203`），不是把梦写成现实。
- 词汇表 ⭐⭐⭐/⭐⭐ 两档共 14 条例句全部逐字落在 `text/ch37_chapter_37.txt`（undergrowth `:5`、pelt `:26`、monochrome `:35`、guttural `:50`、countenance `:59`、progeny `:134`、sphincters `:149`、saplings/bramble/hawthorn `:23`、leathery `:26`、feverish `:35`、loping `:50`、splintered `:104`、scattershot `:116`），表行完整；只有“常用”档断裂（见 B1）。
