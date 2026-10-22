# ch28 对账（R3）：`ch28 the tartan scarf.md` ↔ `text/ch28_chapter_28.txt`

取证：`/usr/bin/grep -n -F '<串>' text/<文件>`（禁 git grep）。

## 一、五条「原句」逐字核对

| # | md | 核对 | text |
|---|---|---|---|
| 原句1 | md:24 `I took it from her. I recognised it now. The last time I’d seen it, it had been tied over my neighbour’s eyes as she aimed a hoop.` | ✅ 逐字一致 | text:62 |
| 原句2 | md:34 `This was my only concrete proof. Proof of what, I didn’t know yet…I tied it onto the door handle instead.` | ✅ 逐字一致 | text:113 |
| 原句3 | md:44 `“I thought it was empty, like yours,” said Maggie, watching me carefully. “Have you been eating alright?” Her voice was suddenly soft.` | ✅ 逐字一致，两组弯引号成对 | text:119 |
| 原句4 | md:54 `I am a capable woman. I can chop wood and work a boiler and move house all by myself. “I’m perfectly alright,” I said, tucking my escaping hair back behind my ears.` | ⚠️ 词句逐字无误，但由 **text:122 与 text:125 两个自然段** 直接粘成一条，中间无省略号 | text:122 + text:125 |
| 原句5 | md:64 `I wanted to be someone people could ask for a favour. That was part of building friendships, wasn’t it?` | ✅ 逐字一致（上一句 `He’d asked me for a favour.` 未取，不影响） | text:188 |

## 二、词汇表例句核对（共 26 行）

逐条 grep：`mottled` / `silhouette` / `illicit` / `flatbed` / `papery` / `vicious` / `affectionate` / `assessing` / `lifesaver` / `exodus` / `universes` / `sparkling` / `windscreen` / `poker` / `scarf` / `hoodie` / `driveway` / `truck` / `key` / `needle` / `café` / `doorstep` 全部在 text 中命中，无改写、无错行。

其中三处需记：

- `vicious`（md:93）→ text:206 `Still as vicious as ever.` ✅
- `sparkling`（md:104）→ 例句作 `“And miss out on your sparkling company?`，**引号未闭合**；text:167 原句为 `“And miss out on your sparkling company? Never.” He turned back to me.`
- `scarf`（md:112）→ 例句把 text:32 与 text:35 **两个自然段**粘成一条（`…at the pub last night.” She held out a tartan scarf.`）

## 三、叙述/事实性表述核对

| 位置 | md 表述 | text 依据 | 判定 |
|---|---|---|---|
| md:12 一句话概括 | 「她昨晚把一条格子围巾落在 The Curtyard」 | text:53 Tamsin 当场否认 `“That isn’t mine,” I said.`；text:62 认出它是邻居的；ch46:23 `It was the same tartan scarf I’d tied onto her door handle yesterday.`（出现在邻居卧室）；ch34:26/32 `did you get your scarf back?` / `“Not my scarf.”` | ❌ 归属错：围巾是邻居的，不是 Tamsin 的；同句后半「而那正是蒙在邻居眼睛上的那条」自相矛盾 |
| md:12 | 「"1a 不是空的"这个认知第一次被说出口」 | text:110 `“I think this is my neighbour’s. I can drop it off.”` | ✅ 成立（是她自己第一次说出口） |
| md:14 情感弧线 | 恐怖只在「Maggie 说 1a 一直是空的」 | text:119 `“I thought it was empty, like yours,”` | ✅ 成立 |
| md:16 Tropes | 「鬼不会把围巾落在酒馆」 | text:68 `Definitely not a ghost then. Unless ghosts go to the pub. In the middle of the day.` | ✅ 成立 |
| md:20 叙事手法 | 荒诞内心戏「公民逮捕／非法园艺」 | text:17 `This is a citizen’s arrest! I am charging you with the crime of grand illicit gardening.` | ✅ 成立 |
| md:30 为什么这样写 | 「最后一句把 **ch24** 的场景原样调回来」 | ch24:59 `tartan scarf wrapped around her eyes like a blindfold…aimed The Curtyard’s plastic ‘o’`；ch24:71 `The hoop flew…` | ✅ 章号正确 |
| md:18 人物弧线 | 「缝皮针做钥匙扣」 | ch17:92 `It could probably be used to sew leather.`；ch40:131 `Lucky you used a leatherworking needle.` | ✅ 有据，不是自造 |
| md:52 读者视角 | 「昨晚在酒馆里扔圈的人是谁？」 | 投环发生在 ch24:59/71 那一晚（ch25 她离场、ch26 才是隔壁那场聚会）；ch28:32 Viv 只说围巾是 **昨晚** 落在酒馆的 | ⚠️ 把两个晚上并成一个 |
| md:60 | 「嘴上四个字」 | 中文「我完全没事」五字；原文 `“I’m perfectly alright,”` 三词 | ⚠️ 计数不准 |
| md:126 一句话总结 | 「那天早上她第一次觉得」 | text:209 `For the first time in a long while, I had a feeling…` | ⚠️ 原文是「很久以来第一次」，非绝对第一次 |
| md:82–121 词汇表 | 多行之间夹空行、`silhouette`/`illicit`/`papery`/`hoodie` 等行前无表头 | 见 md:82-85、91-92、97、100、105、108-110、114-116 | ⚠️ 表格结构被打断 |

## 四、判定汇总

判定汇总：**阻断 1 / 提示 6**
