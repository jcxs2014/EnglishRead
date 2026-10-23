# ch06 · R3 对账（三张单子）

> 依据：`1-suread.json`（先素读，325 行全读，72 事件 / 17 关系 / 7 数字 / 7 未决 / 10 陷阱）与 `2-machine.json`（rc=0 / verdict ok / blocks=10 / words=3344 / block_target=[6,10]）。
> 机器层：`segment_miss=0`（引语逐字）、`quote_long=0`、`keyword_bad=0`、`struct_bad=0`、`cjk_low=0`、`block_count=0`、`template=0`。
> 补验（机器盲区）：`verify_fragments_indep.py` 全书 312 片段 0 MISS；本章 22 行词表例句 22/22 逐字命中（`/tmp/vocab_check_hx.py`）、22/22 词头落在例句内（`/tmp/vocab_head_hx.py`）。

---

## 一、漏（素读有、md 无）

| # | 素读事实（text 行号） | md 状态 | 判定 |
|---|---|---|---|
| L1 | `:113` `Ellie was tied to the air …`（埃莉属**风**系、能读气场）；`:167` `As an earthwitch, she could influence both flora and fauna`（罗恩姨妈属**土**系） | md 只呈现海伦娜的**水**系（`:83–89` 原句 2），另两人的元素归属全章未提 | **不构成阻断**（背景设定，非情节转折；且不影响任何引语对应） |
| L2 | `:122` All Things Bright and Beautiful＝罗恩姨妈逃出苏格兰后开设、如今是全城顶级美容店；产品由 Clio 与姨妈制作；主要竞品 Madame Rachel 把砷、铅、白垩掺进有毒混合物 | 只以词表 `apothecary` 的例句形式出现，导航与分析层未展开 | **不构成阻断**（背景设定） |
| L3 | `:110` 埃莉「我本该窥探可怜人的未来，也许能让他免于这种惨烈结局……命运有平衡天平的本事，我不认为侯爵在讨好它们的 favor」——对埃莉风系幻象能力与命数伏笔的说明 | 只以词表 `marquess` 的例句形式出现，导航与原句分析层未展开 | **不构成阻断** |
| L4 | `:249–:252` 童年：她生日那天保姆被解雇、托马斯被送去上学、斯迈斯女教师到来；「淑女般的笑容与柔软的手掩住暴君的灵魂」；白桦条；十六岁离乡间庄园去上 finishing school | 原句 7（`:255`）的引语只到「她开始记起」，md 未把「记起」的具体内容（童年暴政）点出 | **不构成阻断**（原句 7 的读者视角提示已用「秩序碎裂之前的自己」暗示） |
| L5 | `:119` 海伦娜答应回程去 Barty's Confectionery 买煮柠檬糖谢表姐 | md 全章未提 | **不构成阻断**（闲笔） |
| L6 | `:95` 原文第三种感官 `All she could hear was the low melody of Cynthia’s voice.` | 原句 3 的引语在第二种感官（眼睛）后收住；md 的中文理解与分析（「嗅觉与视觉」）与自己的引语一致 | **不构成阻断**（选句取舍，非错配） |

## 二、编（md 有、原文无）

**0 条。** 逐块核过导航 5 项、原句 1–10 的中文理解／关键词／为什么这样写／读者视角提示、词表 22 行、一句话总结，未发现凭空出现的情节、关系、数字或人物。

已重点排查并**排除**的两处疑点：

- 「表亲／表姐」指埃莉：`:116` `she had volunteered to cover Helena’s shift on the morrow so her cousin could accompany Uncle Lachlan to interview Lady Burrows.`；`:98` 埃莉自称 `my new sister-in-law` 指 Clio ⇒ 「她的表亲」＝埃莉，md 写法成立。
- 「侄女」指海伦娜：`:273` `Superintendent MacDougal and his infuriating (beautiful) niece` ⇒ 麦克杜格尔与海伦娜是叔侄，md 写法成立（见 `:273`）。

## 三、错（两边都有但不一致）

| # | md 位置 | md 写法 | 原文（text 行号 + 逐字） | 判定 |
|---|---|---|---|---|
| E1 | 原句 1·为什么这样写 | 「也把海伦娜放回一个由**女性长辈围坐**的位置」 | `:35` `Women cut herbs at this table, knitted together the fabric of their family, devised spells for healing and protection … Blair women strung together like beads of amber, stretching back to the 1600s, all gathered here to share burdens from the past …` —— 围坐者是**历代布莱尔女巫（含海伦娜自己与后代）**，不是围在她身边的长辈 | **提示**（措辞级） |
| E2 | 导航·一句话概括 | 「辛西娅穿着**连夜染黑**的丧服」 | `:201` `The hasty dye job didn’t completely hide the pattern of what had once been her favourite day dress. … Her laundress had done the best she could with so little time` —— 原文只说「仓促的染色」「时间不多」，**未说连夜**；同章末尾「一句话总结」写的是「穿着染黑的丧服」，md 内部也不一致 | **提示**（措辞级） |
| E3 | 原句 6·为什么这样写 | 「黑痕不匀，旧花样仍透出来，**白底蓝花与蕾丝被具体点出**」 | `:201` `A white and blue floral affair with lace around the collar and sleeves.` —— 该句**位于 md 引语的 `…` 省略段之内**（md 引语只保留 `…` 两侧），分析直接引用了被省略的内容而未披露省略 | **提示**（分析层披露不足；与 ch04 E1「前端截短」不同类——此处省略号已标示省略，且省略仍在同一句群内） |
| E4 | 导航·叙事手法 | 「前半贴海伦娜，靠厨房里的对话和日常动作推进」 | `:110–117` 一段以**埃莉的认知为锚**（`She was well aware of Lord Burrows’ murder, as there were no secrets amongst the Blair women, but her particular powers would be of no help in the investigation.` / `her particular powers would be of no help`）；`:119` 才回到海伦娜内心（`She promised herself she would visit Barty’s Confectionery …`） | **提示**（视角描述不完整） |
| E5 | 本章词汇·⭐基础 `air` | 释义「**空气**」 | `:113` `Ellie was tied to the air, and that ephemeral element aided in her disconcertingly accurate visions of the future.` —— 此处 `the air` 是**风元素**（与 `:89` 海伦娜的水、`:167` 姨妈的土构成三元素），释义只给「空气」会误导读者 | **提示**（词表释义级） |

## 四、R4 逐块对应（三问）

| 原句 | 中文理解对应 | ①动词主语 | ②受事/宾语 | ③归属方向 | 结论 |
|---|---|---|---|---|---|
| 1 | 传了几代的樱桃木桌 + 祖先历史 | 海伦娜坐在桌旁 | 桌面光泽/划痕/污渍 | 「讲述祖先历史」 | 对应成立 |
| 2 | 承认仍能操控元素 + 当场演示 | 她答「不」；水涡出现、扫过房间 | 露水洒在所有植物上 | 她证明自己 | 对应成立 |
| 3 | 一道甩不掉的咒 | 辛西娅变成 hex | 感官被侵入 | 她闻到/看到的是辛西娅 | 对应成立 |
| 4 | 表亲替班 + 问话在明天 | 埃莉主动提出替班 | 海伦娜的班 | 「明天由拉奇兰叔叔问话」 | 对应成立 |
| 5 | 搅动灵魂里平静的水面 | 辛西娅搅动 | 海伦娜的灵魂 | 「一点也不喜欢」＝海伦娜 | 对应成立 |
| 6 | 染黑的花裙 + 寡妇的规矩 | 辛西娅搓着黑痕；染色没盖住花样 | 旧日常裙 | 丈夫死后第二天 | 对应成立 |
| 7 | 守寡第一夜 + 秩序碎裂 | 她浸在月光里、开始记起 | 井然有序的生活 | 「碎裂」的是那生活 | 对应成立 |
| 8 | 拒绝考虑定罪 + 自由礼物 | 她拒绝考虑；必须说服警司与其侄女 | 清白、自由 | 「不打算交给任何人」 | 对应成立 |
| 9 | 手指相触 + 血液里的萤火虫 | 海伦娜取杯碟；两人手指相触 | 辛西娅体内的感觉 | 「萤火虫在血液里炸开」是比喻 | 对应成立 |
| 10 | 抢先发问「你会施什么魔法」 | 辛西娅迎住目光、端茶、问话 | 对方会施的魔法 | 「心里急不可耐」＝她自己 | 对应成立 |

**R4 无阻断。** 未发现「分析讲的是引语之外的上下文」「讲全书主旨」「只复述字面」三类失配（E3 为引语跨度内省略内容的披露问题，已单列）。

## 五、形态

`H1 = 06. Chapter Six`（形状合规）；导航 5 项；子项 4 项（中文理解／关键词／为什么这样写／读者视角提示）＝本书众数；块数 10，落在本书区间 [6,13] 与本章 `block_target=[6,10]` 内（**已触上限**：若因修复增块，会触发 `block_count`）。
