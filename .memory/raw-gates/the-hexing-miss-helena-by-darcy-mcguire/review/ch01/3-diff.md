# 3-diff.md · 《The Hexing Miss Helena》ch01 对账单

审法：R1 素读（`1-suread.json`，16 条事实 + 7 组关系 + 5 处数字）→ R2 机器层（`2-machine.json`，verdict `ok`，6/6 引语逐字命中，pos 344→2909→5516→6796→10154→11572，单段无 `…`、无拼接）→ R3 三张单子（漏／编／错）→ R4 逐块对应。
素读来源：`text/ch01_chapter_1.txt`（273 行）；受审：`ch01 a dead husband.md`（6 块）。

---

## 单子一：漏（素读有、md 无）

| # | 原文事实 | 原文位置 | md 状况 | 结论 |
|---|---|---|---|---|
| L1 | Clio Blair 的登场段：五个月前结识、Clio 在跟哥哥查案子、两人已 recently married、蜜月旅行推到秋天 | `text/ch01_chapter_1.txt:191` | 全章 md 检索 `Clio` = **0 命中**；既未取引语，也未进分析层 | **提示**：Clio 是下一章 Helena 登场的引线（`text/ch02_chapter_2.txt:35` 证实她是 Helena 的表妹），本章未取用但**未写取舍理由** |
| L2 | 七月中午客厅里竟生着炉火（希金斯太太点的），平时这会儿闷热，今天她在发抖 | `text/ch01_chapter_1.txt:263` | 只进了词表例句（sweltering 行），分析层未提 | **提示**：环境反常是后文「有人布置过现场」的伏笔，分析层未取用 |
| L3 | 管家看见 Lord Hubert Burrows 就当场呕吐在门边花盆里；一名男仆面如白纸瘫倒 | `text/ch01_chapter_1.txt:92,95` | md 未提及 | **提示**：属群像细节，非关键转折 |
| L4 | 被辞退的女仆名叫 Lily | `text/ch01_chapter_1.txt:56` | md 检索 `Lily` = **0 命中**；原句 1 只写「辞退她的女仆」 | **提示**：名字未取用（引语块未覆盖该句），但 Lily 与本案后续直接相关 |
| L5 | 辛西娅的茶与咖啡偏好（秘密偏爱咖啡，「a scandalous admission」） | `text/ch01_chapter_1.txt:203` | 只进词表例句 | **提示**：性格细节，非关键 |

> L1–L5 均**不构成阻断**：五项都不是本章的转折或因果链节点；R3「漏」的判据是「关键事件／转折未出现」。按 §0「判定『不修』的，也要进台账」，本节整体登记为**提示型，只记不改**。

## 单子二：编（md 有、原文无）

| # | md 断言 | 核验 | 结论 |
|---|---|---|---|
| C1 | 导航「Tropes」：`文本还明确写出她与丈夫彼此都不爱` | `text/ch01_chapter_1.txt:233` `Cynthia didn’t love her husband. Nor did Hubert ever love Cynthia.` | **相符**（未凭空） |
| C2 | 导航「叙事手法」：`开篇用明媚天气反衬怒气` | `:35` `The warm sunlight streaming through the window did not match her black mood.` | **相符** |
| C3 | 导航「叙事手法」：`魔法转场用"everyone disappeared"硬切` | `:119` `Cynthia blinked, and everyone disappeared.` + `:122` `Magic.` | **相符** |
| C4 | 导航「人物弧线」：`从"准备第一次当面反抗"走到…` | `:38` `Ten years of keeping her mouth shut.` + `:44` `She was going to confront him this time.` | **相符**（十年闭嘴支持「第一次」） |
| C5 | 原句 1「中文理解」：`十年的忍耐被压成三个连续的"十年"` | `:38` 三个 `ten years / Ten years / Ten years` | **相符**；但中文理解只列了后两项（闭嘴、做尽职妻子），第一项「怒火酝酿十年」由「为什么这样写」的「一次具体的冒犯」承担 → **提示**（枚举不全，非错） |
| C6 | 原句 2「为什么这样写」：`一个横陈、一个汇聚` | `:77` `sprawled face down` / `Blood pooled around him` | **相符**（sprawled＝摊开、pooled＝积聚） |
| C7 | 原句 4「中文理解」：`鼠尾草色的藤蔓印花` | `:161` `Soothing cream walls with sage printed vines` | **相符** |
| C8 | 原句 5「为什么这样写」：`最后一句把"婚姻圆满"换成"她本人圆满"` | `:236` `her society marriage was whole and happy. Or that she was whole and happy, for that matter.` | **相符** |
| C9 | 词表 21 条例句 | 逐条回原文：`:62 :50 :86 :251 :263 :239 :74 :170 :35 :44 :59 :104 :155 :53 :203 :89 :38 :158 :104 :104 :86 :104`（`abominable/untenable/heedless/premonition/sweltering/philandering/debauching/sightlessly/vexed/autonomy/vendettas/hysterical/upholstery/swanning/scandalous/conversely/maid/parlour/constable/bobby/scream/tea`） | **全部逐字命中**，无手写编造 |

**单子二结论：0 条「编」。** 全章未出现原文没有的情节、关系或数字。

## 单子三：错（两边都有但不一致）

| # | md 断言 | 原文 | 结论 |
|---|---|---|---|
| E1 | 导航「一句话概括」：`她刚承认自己感到的是解脱` | `:224` `Relief? Well. That’s hardly something one would admit.`；`:230` `She was free.`；`:236` `If she did feel a breath of liberation at his demise…` | **提示（措辞）**：源文两层并存——对外「不会承认」，内心 `:230` 确已承认「She was free」，而 `:236` 又以 `If she did feel` 对冲。md 写「承认」在「内心承认」这一层成立，但与 `:224` 的「不是会承认的东西」相冲，且与本章正文（`:58-66` 原句 5 的中文理解「如果她真的感到一丝自由」）口径不一致。建议改为「她心里那点解脱刚冒头」 |
| E2 | 导航「叙事手法」：`结尾用问句收束，把悬念交给下一章` | `:266` 是问句，但章节在其后还有 3 段（`:269` `Oh dear.`、`:272` `Because she could think of hundreds of reasons.`）才收尾 | **提示（措辞）**：问句在倒数第 3 段，章末落点是内心独白而非问句 |
| E3 | 原句 6「读者视角提示」：`问题落下，章节就断了，她连否认的时间都没有` | 同上，章节未在问句处断 | **提示（措辞）**：与 E2 同源，同一处修即可 |
| E4 | 原句 3「中文理解」：`第二个男人进入她的视线` | `:131` 哥哥 Thomas 已先出现，`:137` `Another man stepped into her line of vision` | **相符**（MacDougal 确是第二个男人） |
| E5 | 原句 3「读者视角提示」：`这间前厅` | `:155-158` 魔法切换后场景已是前厅（`When had she walked to her front parlour?`） | **相符** |
| E6 | 形态：H1 / 导航 5 项 / 子项 4 项 | `2-machine.json` `form`：h1_shape_ok=true、nav_count=5 ok、subitems=中文理解/关键词/为什么这样写/读者视角提示、blocks=6 | **相符**；块数 6 与本书众数 13 有差（`structure.py audit` 已报提示），理由见 `4-verdict.md`「形态」组 |

**单子三结论：0 条「错」（阻断），3 条措辞级「提示」（E1–E3 同源）。**
