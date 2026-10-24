# ch24 对账（To Bring the Moonlight into a Chamber）

机器层：`bash scripts/chapter.sh "…/ch24 to bring the moonlight into a chamber.md" --json` → **rc=0**，verdict `ok`，8 块，引语段 8/8 全部命中（`pos` 见 2-machine.json），`segment_miss=0`、`empty_quote=0`、`struct_bad=0`、`keyword_bad=0`、`cjk_low=0`、`template=0`、`hole=0`。⚠️ 机器只验「引语是否在 text 里逐字存在」，验不了「块选得够不够、中文讲的是不是这句」。

## 一、漏（素读有、md 无）

### L1【阻断】Isadora 自发开口 +「Consciousness?」整段未进任何块、也未进导航

素读第 9 条：走出画廊后，Isadora 忽然对着两人说「You make my heart sing」，Beck 追问是否意识，答「No. But something less random than usual.」。

原文（`text/ch24_to_bring_the_moonlight_into_a_chamber.txt:356`）：

> Out of nowhere comes a voice: “You make my heart sing.” Beck and I stand quiet and still, waiting for more, but nothing comes.

原文（同文件 `:366-370`）：

> “Consciousness?” I ask.
> "No. But something less random than usual. I need to figure out what." Beck sounds apologetic, but eager.

md 侧取证（`/usr/bin/grep -nE`，退出码如下）：

```
$ /usr/bin/grep -nE "heart sing" "ch24 to bring the moonlight into a chamber.md" ; echo rc=$?
rc=1
$ /usr/bin/grep -nE "Consciousness" "ch24 to bring the moonlight into a chamber.md" ; echo rc=$?
rc=1
```

`rc=1` = md 全文零命中：既没有引语块，也没有在「本章导航」「一句话总结」里带一句。而这条是本章工作室场景的收尾钩子——Beck 自己承认「比平时更不像随机」，也是后文 Isadora 线的第一粒种子。按作业单「关键事件/转折未进任何一块或导航 ⇒ 阻断」，判阻断。

### L2【提示】4 月 9 日这个日期与两人年龄没进 md

原文 `:18`：

> Friday, April 9, 2010 (Clare is 38, Beck is 34)

md 全文无 `2010` / `38` / `34`（`/usr/bin/grep -nE "April 9" …md` → `rc=1`）。本书同批 ch29 的导航是写了日期的（`ch29 henry calls home.md:11` 开头即「2010 年 7 月 18 日凌晨」），故此处属体例不齐而非无据；日期不是本章转折，降为提示。

### L3【提示】VR 博物馆整段无块，仅靠导航一句带过

原文 `:279-330` 共约五十行：底特律美术馆 Rivera《Detroit Industry Murals》→ 卢浮宫侧厅维米尔《The Concert》（加德纳失窃画）→ V&A → 加尔各答 Marble Palace → 新奥尔良教堂（祭坛上全是假肢）→ 银行保险库（情书与蛇蜕）→ Art Institute 的 Ando Gallery。8 个引语块里没有任何一块落在这段上；「本章导航」只有「带她戴上头显逛一座收容失物的虚拟博物馆」一句，「一句话总结」补了三处地名。

同段还有一句本章最锋利的台词，`/usr/bin/grep -nE "six days old"` 在 md 中 `rc=1`（零命中）：

> 原文 `:347`：“It’s the room that’s the ghost. The light you’re seeing is already six days old.”

判提示而非漏：导航已覆盖该场景大意（不属于「未进任何一块或导航」），但块选点严重前重后轻，全章最长的视觉段没有精读。

### L4【提示】「头颅是雇研究生做的」未进块

原文 `:77`：

> “No,” Beck replies, grimacing. “I hired a grad student to make it, but I’m not too excited about the result.”

md `grep -nE "grad student"` → `rc=1`。原句 3 只写到「露出一个钟表脑袋」，原句 4 直接跳到它开口，中间这段「不是她做的、她也不满意」被跳过；不影响主线，判提示。

## 二、编（md 有、原文无）

未发现。逐条核过导航与八块的断言：半球铁架、十二英尺（原文 `:30` "about twelve feet high"）、黑天花板、服务器、胶带 X、虹膜扫描、图灵 Child Machine、失窃维米尔、《Where the Wild Things Are》、Toll House 饼干，均能在 text 找到对应句。**本项 0 条。**

## 三、错（两边都有但不一致）

### E1【阻断】原句 7 引语截短，末尾断言被紧接着的原文否证

md 引语（`ch24 …md:79`）止于：

> "…That’s what was missing, all that time I spent here in this dim gallery, mourning: the outside world."

原文同一段（`text/…ch24…txt:351`）在这句之后还有一整句：

> I feel the weight of my sadness shift—it still hangs over me, but I can begin to look forward and imagine my life after Henry’s death.

md 的「为什么这样写」（`ch24 …md:85`）据此下判断：

> 她没有说悲伤结束，只说知道自己缺什么——这是两种不同的进展，作者选的是后一种。

原文恰恰两样都说了：悲伤仍在（"it still hangs over me"）**且**「能开始往前看、能想象 Henry 死后的生活」（"I can begin to look forward and imagine my life after Henry’s death"）。所以「作者选的是后一种（只知道自己缺什么）」与原文相反。这是典型的「引语截短 → 分析停在旧句」，按「两侧都有但不一致」判错、阻断。（md 导航 `:12` 写「悲伤还压着，人却开始往前看」是对的，说明错的只是这一块。）

### E2【提示】「三年没肯回去的地方」把两件事并成一件

md 读者视角提示（`ch24 …md:87`）：

> 「外面的世界」既是字面上的雨与风，也是她三年没肯回去的地方。

原文 `:309`：

> I am grateful for Beck’s gift; I don’t want to explain that I’ve been weeping in this room for three years.

原文的「三年」修饰的是「在这间屋里哭」，不是「没回到外面的世界」；md 把「哭了三年」改写成「三年没肯回去」，方向（谁对谁）变了。判提示：读者提示层可以引申，但这是把原文事实关系替换掉。

## 四、R4 逐块对应（人判）

对每块只问：这段中文是不是在讲这句引语？再追三问：动词主语 / 受事宾语 / 归属方向（by·to·from·of）。

| 块 | 引语（原文行） | 中文是不是在讲这句 | 主语 | 受事/宾语 | 归属方向 | 结论 |
|---|---|---|---|---|---|---|
| 原句 1 | `:23` hunch / find name / phone | 是 | Clare（I） | 名单上的 Beck 名字、电话那头的 Beck | of tenants＝楼里的租户名单 ✓ | 对应成立 |
| 原句 2 | `:24` sensor / iris / Museum of Lost Souls | 是 | Beck | 锁、Clare | "a friend of Richard’s"＝Richard 的朋友 ✓（md 写「Richard 那位…朋友」） | 对应成立 |
| 原句 3 | `:68` scoots / pushes / whisks off plastic | 是 | Beck | 带轮台子、塑料布 | — | 对应成立 |
| 原句 4 | `:82` taps / jaw shuts / girlish voice | 是 | Beck（操作）、head（动与说） | Clare 的全名 | "Hello, Clare DeTamble!" 直呼其名 ✓ | 对应成立 |
| 原句 5 | `:206` Child Machine theory | 是 | Beck | Isadora 的童年 | Turing 的观点＝转述 ✓ | 对应成立 |
| 原句 6 | `:225` "To find beauty and goodness…" | 大体是，但**引语起点截在句中**：丢掉了 Beck 直接回答 Clare 的 "True beauty is not elitist. I want Isadora to be able to love." | Beck | 美与善、Isadora | — | 提示（引语选短，见 T4） |
| 原句 7 | `:351` "I wonder if Beck sensed…" | **不完全是**：只讲到「缺的是外面的世界」，下一句的「往前看」被切掉，分析还据此下了反证结论 | 原文 "when she sat next to me" 的 she＝Beck；md 写成「她…坐到她身边」，两个「她」指向不明 | 悲伤、外面的世界 | — | **错（E1）** + 提示（T5） |
| 原句 8 | `:374` Toll House cookies / Wild thing | 是（止于 "I think I love you."） | Clare（唱）、Alba/Kimy（做饼干） | Alba | 歌是唱给 Alba 的 ✓ | 提示（T6：截短丢掉 Kimy 的 "It's about time"） |

**T4/T5/T6 明细**

- T4：`text/:225` 原文是 "“True beauty is not elitist. I want Isadora to be able to love. To find beauty and goodness in places that humans might not."；md 引语从第三句起，前两句（对 Clare「美是精英主义」的正面反驳）消失，读者看不到这段是应答。
- T5：`text/:351` "I wonder if Beck sensed my unhappiness when **she** sat next to me in this room"——主语是 Beck；md `:81` 写「当初她在这间昏暗展厅坐到她身边时」，两个「她」无法区分谁坐谁旁边。
- T6：`text/:379-387`：

  > “You’re in a good mood,” Kimy says approvingly. … “It’s about time,” Kimy replies. “Here, Alba, let’s wash these dishes.”

  md 这块的中文理解只写到 Clare 唱歌，Kimy 这两句评语（旁人点出她终于缓过来了）没有进块，也没有进导航/总结。

## 五、R4 总评

八块中文都落在引语所讲的那句话上，没有出现「讲全书主旨/作者生平」的跑题块；密度也够（每块都答了为什么这样写，不是复述字面）。两处硬伤都出在**块尾**：原句 7 截短致结论反了（E1），原句 8 截短丢掉旁人反应（T6）。另一类问题是**选点前重后轻**（L3）：前 8 行的门口戏占两块，五十行的虚拟博物馆一块没有。
