# ch10 素读 vs md 差异（人判）

素读清单：`1-suread.json`（18 条事实，锚点全部命中 `text/ch10_chapter_nine.txt`）。

## 查出的问题

### D1 · 关系错：James 是未婚夫，戒指是订婚戒，不是「丈夫的婚戒」 🔴

- **位置**：md:11（一句话概括）、md:240（一句话总结）
- **改前**：`她把丈夫的婚戒锁进抽屉`
- **改后**：`她把未婚夫的订婚戒指锁进抽屉`
- **原文依据**：
  - `text/ch04_chapter_three.txt:68`：`“He asked me to marry him,” I answer bluntly… the engagement band isn’t there.`
  - `text/ch10_chapter_nine.txt:433`：`I remove James’s ring and hold it in my palm.`
  - `text/ch10_chapter_nine.txt:439`：`James won’t know I have taken it off.`
- **判据**：全书她与 James 从未结婚（求婚发生在 ch03 前夜）；`engagement band` 明示为订婚戒。

### D2 · 施事归属反转：掉头是「她自己决定的」，风暴是把船往外推的那一方 🔴

- **位置**：md:11（导航）、md:12（情感弧线位置）
- **改前**：`她在风暴里把船掉头` ／ `前段靠一场海上风暴完成身体上的折返`
- **改后**：`她在风暴来临前自己把船掉头` ／ `前段先由她自己掉头、再被一场风暴几乎推回大洋，最后潮水把她送回岸上`
- **原文依据**：
  - `text/ch10_chapter_nine.txt:160`：`but now I lift the oars, pressing them down into the water, heaving the boat back toward the thing I’ve dreamed about most of my life.`（掉头，此时风暴未至）
  - `text/ch10_chapter_nine.txt:176`：`Waves spill over the bow… The storm has found me.`（风暴随后才来，方向是把她推离岛）
  - `text/ch10_chapter_nine.txt:191`：`I can feel it pushing me away—farther from the island.`
  - `text/ch10_chapter_nine.txt:263`：`the tide seems to carry me, as if it never wanted me to leave the island after all.`
- **判据**：三处方向相反：她→岛（自愿）、风暴→离岛、潮水→回岛。把「转折」记在风暴名下，等于把她的决定改写成天意。

### D3 · 事实断言：岛并没有「二十年不再回来」，那是她当时的担心 🔴

- **位置**：md:11（导航）
- **改前**：`岛一度消失、二十年不再回来，潮水却又把她推回岸上`
- **改后**：`岛一度消失、她甚至以为要再过二十年才会回来，潮水却很快又把她推回岸上`
- **原文依据**：
  - `text/ch10_chapter_nine.txt:206`：`Or maybe… it’s truly gone—slipped back into a ribbon of time, and it won’t return for another twenty years.`（`maybe`＝她的推测）
  - `text/ch10_chapter_nine.txt:254`：`there, in the distance, a tiny, almost imperceptible mass.`
  - `text/ch10_chapter_nine.txt:266`：`I made it back.`
- **判据**：原文用 `maybe` 标注这是她的推测，且同一场景内岛即重新出现；导航把它写成事实，且与后半句「潮水又把她推回岸上」自相矛盾。

### D4 · 数字略：`二十多年` 与本书自己的 19 年不符 🟡

- **位置**：md:61（原句 4 的「为什么这样写」）
- **改前**：`她逃了二十多年，逃的方式是不承认`
- **改后**：`她逃了将近二十年，逃的方式是不承认`
- **原文依据**：
  - `text/ch04_chapter_three.txt:16`：`it’s taken nineteen years and a mountain of therapy for me to get over what happened`
  - `text/ch07_chapter_six.txt:96`：`the man I met almost twenty years ago`
- **判据**：本书自报 19 年；ch07 口语化为 `almost twenty years`（不足二十）。写「二十多年」（超过二十）与两处都冲突。

## 已核实为正确（不要改坏）

- 块 14「Ye did.」译作「你已经偷走了」：上文是 `I thought I already stole that?`（偷走灵魂的玩笑），应答指向「偷」而非「做」，**正确**。
- 块 13「这是她第一次对他说」：全书 `I love you` 仅 4 处，ch06 那处是她**发给 James 的短信**（`text/ch06_chapter_five.txt:185`），对 Clay 说确实是本章首次，**正确**。
- 块 9 分析「往后它会进抽屉」：`:436` `I open the bedside drawer and tuck it in the far back`，**正确**。
- 块 6 分析「顺手解释了上一章里几小时对一周」：ch02 的 `missing for a whole week` 与本章规则一致，**正确**。
- 块 15 分析对「松开」只作让步式推断（`看起来不是…而是…`），原文确实只给先后不给动机，**保持现状**。
