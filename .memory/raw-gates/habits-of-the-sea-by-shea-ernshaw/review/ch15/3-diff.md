# ch15 素读 vs md 差异（人判）

素读清单：`1-suread.json`（17 条事实，锚点全部命中 `text/ch15_chapter_fourteen.txt`）。

## 查出的问题

### D1 · 场景错：坦白发生在岛上的屋里与菜园小径，不在木筏上 🔴

- **位置**：md:8（一句话概括）
- **改前**：`Ellie 在漂流的木筏上逼 Clay 交代那桩瞒了整本书的旧事`
- **改后**：`Ellie 在自家厨房与菜园小径上逼 Clay 交代那桩瞒了整本书的旧事`
- **原文依据**：
  - `text/ch15_chapter_fourteen.txt:16`：`It’s been three days since we landed in Nova Scotia, three days since I stood in front of Nana’s house and said goodbye to James.`
  - `:40`：`he stands at the sink, washing dishes`（厨房）
  - `:88`：`He strides down the steps, stopping on the path that leads to the garden`（菜园小径）
  - `:61`：`The raft is too unsteady, not seaworthy`（木筏只是他提的逃生方案，两人并不在筏上）
- **判据**：全章坦白段落发生在岛上的厨房与小径；`raft` 只是对话里假设的逃生工具。

### D2 · 数字单位错：`五年或六个月` 应为 `五个月或六个月` 🔴

- **位置**：md:12（叙事手法）
- **改前**：`2062 年、五年或六个月、二十年、几英里宽的死鱼带`
- **改后**：`2062 年、五个月或六个月、二十年、几英里宽的死鱼带`
- **原文依据**：
  - `text/ch15_chapter_fourteen.txt:362`：`It’s probably been five months, maybe six, since we last saw the mainland`
- **判据**：`five months, maybe six` 是「五个月，也许六个月」；写成「五年」把岛上时间放大十二倍。

### D3 · 人物弧线把「不知所措」写成「作出决定」 🟡

- **位置**：md:11（人物弧线）
- **改前**：`并在他中弹的腹部上做出全章唯一真正属于治疗师的决定——子弹留在体内，她缝的是伤口`
- **改后**：`并在他中弹的腹部上做出全章唯一真正属于治疗师的处置——她找不到出口、不敢往里挖，于是只清创、缝合，子弹留在了体内`
- **原文依据**：
  - `text/ch15_chapter_fourteen.txt:961`：`I feel around to his back, searching for an exit hole, but don’t find one. The bullet is still inside him. But I have no idea if I should go into his flesh and try to pull it out, or if I’ll do more damage.`
- **判据**：原文写的是「完全没有主意」，不是「决定保留」；结果相同（子弹留下），但施事与心理状态不同。

### D4 · 一句话总结指代错乱：`他有船却说她没有` 🟡

- **位置**：md:239（一句话总结）
- **改前**：`他有船却说她没有`
- **改后**：`他有船却说没有路`
- **原文依据**：
  - `text/ch15_chapter_fourteen.txt:115`：`“I told ye I didn’t. I told ye… there was no way back. But I lied.”`
- **判据**：他否认的是「自己有船／有退路」，不是「她没有船」；`她` 这个主语把施事挪到了错误的人身上。

### D5 · 错字：`形同陌陌` 🟡

- **位置**：md:9（情感弧线位置）
- **改前**：`前半是全书最长的一次同处一室却形同陌陌`
- **改后**：`前半是全书最长的一次同处一室却形同陌路`

## 已核实为正确（不要改坏）

- 「两枪打中 Bosch（肩、胸口各一）」：`:789` 顺序正确（先肩、后胸）。
- 「假上将的制服小两号」：`:720` `his uniform is at least two sizes too small`。
- 「Kochek 死因不确定」：`:1021` 明写 `may have been the bullet in his upper chest… or the trauma to his skull`，md 未指定死因，**正确**。
- 「2062 年」「Sarkak＝旧格陵兰」「母舰掉头离开」：`:612` `:666` `:1060`，**正确**。
- 块 6 未把「船被潮水卷走」写成 Clay 故意藏船：`:127` 是他准备次日告知、次日船已被潮水带走，md 的「被潮水夺走」与该表述一致，**不要改成「他又把船藏起来」**。
