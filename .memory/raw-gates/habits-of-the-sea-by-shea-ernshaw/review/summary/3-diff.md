# 总结层（概述 + 金句精选 + 情感节点 + 19 章一句话总结）人判差异

判据：`docs/rules/生产-审查对照.md` S5 ①「总览事实断言错：关系 / 死因 / 数字」，
按六类逐句过：**身份 · 关系 · 谁做了什么 · 谁欠谁 · 谁被替罪 · 数字**。每条回到 `text/` 明文。

## A. 事实错（阻断）

### A1 · 两块石头被读成「替代物」（三处同源）

- 位置：`00_概述.md:10`（第 1 段）、`00_金句精选.md:18`（①「为什么重要」）、`00_情感节点.md:10`（节点一）
- 现状：`双胞胎只得以两块小石头代替` / `两个没出世的婴儿被换成两块小石头` / `又回屋取来两块小石头…代替一对没足月的双胞胎`
- 应为：`双胞胎被写成「两块石头」`（比喻，不是替代物）
- 依据：`text/ch01_prologue.txt:26` `He strode back to the house to retrieve the two smaller bodies. They were merely stones, tiny as garden squash, not yet ripe.` + `:29` `the night Clay Lockhart buried his wife and his newly born twins in the soil beside the sea`
- 结论：埋下去的就是那对双胞胎本身；`merely stones` 是对未成熟尸身的贬抑式比喻，不存在「用石头顶替」。

### A2 · 母亲「再婚生子」与原文不符

- 位置：`00_情感节点.md:22`（节点二）
- 现状：`四个月后母亲再婚生子，却再没提过接她回去`
- 应为：`四个月后母亲交了一个带着三个孩子的男人，从此再没提过接她回去`
- 依据：`text/ch02_chapter_one.txt:28` `She met someone, a man at the company… He already had three kids… But she never asked me to come.`
- 结论：原文没有再婚、没有新生儿；她连「来接」都没提过。

### A3 · 挂坠的来处被挪到「废弃度假村」

- 位置：`00_情感节点.md:46`（节点四）
- 现状：`她在废弃度假村找到那枚挂坠`
- 应为：`她从行李箱里的羊毛围巾中翻出那枚一直带着的挂坠，把它串到 Nana 给的贝壳项链上`
- 依据：
  - `text/ch06_chapter_five.txt:117` `I shower… then dig through my suitcase until I find the wool scarf. Folded inside is the small locket.`
  - `text/ch06_chapter_five.txt:120` `I unclasp the chain… and I slide the locket onto the chain.`
  - 废弃度假村是**另一座岛**（ch12–ch13 的荒滩），与 ch06 的法罗群岛无关。
- 结论：挂坠一直由她随身带着；这是「把两座岛的事混成一件」。

### A4 · 贝壳项链写成「从树上解下来」

- 位置：`00_情感节点.md:70`（节点六）
- 现状：`同一棵树上解下来的贝壳项链`
- 应为：`Nana 给的那枚贝壳，加上 Clay 在岸边捡到、亲手钻孔串上链子的牛角贝`
- 依据：`text/ch09_chapter_eight.txt:543`–`:549` `Found it on the shore, reminded me of the one ye wear—` / `Made a small hole… For yer necklace.`
- 结论：原文没有「树」；第二枚贝壳来自岸边。

### A5 · 报纸的来处错（「Nana 家找到的剪报」）

- 位置：`00_金句精选.md:140`（⑪「上下文」）
- 现状：`她在 Nana 家找到 1952 年的旧报纸剪报`
- 应为：`她想起十二岁那年之后在当地图书馆读到的 1952 年报纸文章`
- 依据：`text/ch04_chapter_three.txt:316` `I think about the newspaper article from 1952—the one I read at the local library after that night.`
- 结论：不是剪报、不在 Nana 家，是图书馆里读到的文章。

### A6 · 母羊那一夜被写成「难产」

- 位置：`00_金句精选.md:202`（⑯「上下文」）
- 现状：`岛上第二个冬天，母羊难产那夜，他在羊圈里接生`
- 应为：`岛上头一年的羊圈接生夜（母羊与羊羔都平安），他在羊圈里接生`
- 依据：
  - `text/ch08_chapter_seven.txt:283` `he’s helping the tiny lamb emerge into the world` / `“Aye, the ewe and lamb look fine.”`（不是难产）
  - 本章全文无 `winter`／「第二个冬天」字样（`grep -c winter` = 0）
- 结论：难产是**他妻子**那一夜的属性，被错移到母羊身上——正是「谁被替罪」类错位。

## B. 层别错（提示）

### B1 · 传说层被写成事实层

- 位置：`00_概述.md:10`（第 1 段）`极度的哀恸撕裂了地面…`；`00_金句精选.md:22`（②「为什么重要」）`不是鬼神、不是天灾，是一个人的悲伤大到把地壳撑裂`
- 依据：`text/ch01_prologue.txt:56` 整段以 `In the years that followed, stories sifted from neighbor to neighbor…` 起头（传说体）；`:62` 又列出「他大概跳崖了」等互相矛盾的说法；尾声 `text/ch19_epilogue.txt:16` 自称 `a fable`。
- 说明：ch01 自己的「读者视角提示」已经点明「这里是别人转述的版本」，总览却写成事实，属于层别不一致。

### B2 · 「三个星期」无原文支撑

- 位置：`00_情感节点.md:58`（节点五）
- 依据：ch08 全文无 `three weeks`／`weeks`；ch07 只写 `Been two days since I brought ye up from the shore.`
- 说明：可删或改为「住了些日子」。

## C. 假阳（已核实为正确，不要改）

- `check_summary_names` 的 7 条提示全部为假阳：ch05 / ch08 / ch11 是**第一人称章**（正文只有 `I`，导航用 Ellie 属合法指称）；ch19 那条原文是「Ellie、Clay、Nana 都不再被点名」。
- `00_概述.md` 的 16 条引语是**行内**形态，`overview.py quotes` 口径外（工具限制），但 `overview.py full` 报「A 整串 命中 100 ｜ 查无 0」，已逐条核过。
