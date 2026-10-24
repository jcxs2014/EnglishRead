# ch25 对账（A Murmuration）

机器层：`bash scripts/chapter.sh "…/ch25 a murmuration.md" --json` → **rc=0**，verdict `ok`，4 块，引语 4/4 逐字命中，`segment_miss=0`、`empty_quote=0`、`struct_bad=0`、`keyword_bad=0`、`cjk_low=0`、`template=0`、`hole=0`；本书该章块数目标区间 `block_target=[3,5]`，4 块在区间内。

> 本章与 ch69 同名（`text/ch25_a_murmuration.txt` vs `text/ch69_a_murmuration.txt`），内容完全不同。本报告只对 ch25；所有引文均取自 `text/ch25_a_murmuration.txt`。

## 一、漏（素读有、md 无）

**本项 0 条。** 素读 12 条逐条比对「本章导航 + 8 个块位置（实际 4 块）+ 一句话总结」，关键事件与转折都在：邀约与绕屋（块 1）、闭眼入室与鸟群启动（块 2、「导航」）、Clare 的动机（块 3）、接吻与「找到心的同伴」（块 4）、停车场的难题与电话（导航 + 总结）。**本章的转折点＝接吻/「this is how we begin」，已进块 4**，故不判漏。

## 二、编（md 有、原文无）

**本项 0 条。** 逐条核过：红砖平房/绿瓦/黄边（`:23`）、闭眼与手温（`:37`）、成百上千只鸟与细铁丝（`:42`）、冰白葡萄酒（`:76` “cold white wine”）、佩斯利沙发与颜料罐（`:50`）、“把心里的黑拿出来给人看”（`:114`）、停车场与电话（`:134-143`）均在原文。

## 三、错（两边都有但不一致）

### E1【提示】「阳光下的红酒与大笑」——酒是在室内喝的，原文也没有「大笑」

md 导航（`ch25 a murmuration.md:12`）：

> 温度走了一个来回：屋外的暖阳、屋里的骤冷、鸟群的黄昏，再回到阳光下的红酒与大笑。

原文（`text/ch25_a_murmuration.txt:71`、`:76`）：

> She comes in, sets the tray on a little table next to me, uncorks the wine and pours each of us a glass. Clare sits next to me, and we clink glasses and drink in silence for a few minutes.
> Now, sitting together here in Clare’s bright little office, sipping cold white wine…

酒从头到尾在 Clare 的小办公室里喝；两人到户外只有两件事：走到车边、道别（`:134`）。原文的情绪词是 “smile shyly”（`:123`）、“a big smile”（`:143`），没有「大笑」。判提示：场景细节错位，不影响情节走向。

### E2【提示】「蜡与漆的气味」——原文是「香与万寿菊，带一点腐蚀性」

md 导航（`:15`）：

> 感官写得密：冷气、蜡与漆的气味、鸟叫、指尖的温度。

原文（`:50`）：

> It smells marvelous and reminds me of incense and marigolds, though there is a slightly caustic edge to the scent.

原文只给「香（incense）+ 万寿菊（marigolds）+ 一点刺鼻」。md 的「蜡」大概来自那支未点的蜡烛（`:32` “an unlit candle”），「漆」大概来自红漆小桌（`:32` “red lacquered table”）——这是从物件反推的气味，原文并未说它们有气味。判提示。

## 四、R4 逐块对应（人判）

| 块 | 引语（原文行） | 中文是不是在讲这句 | 主语 | 受事/宾语 | 归属方向 | 结论 |
|---|---|---|---|---|---|---|
| 原句 1 | `:23` “Beck: Clare has invited me…” | 是 | Clare 邀；I＝Beck 走侧径 | 屋后那间画室 | “her studio”＝Clare 的工作室 ✓；“per her instructions”＝按 Clare 的吩咐 ✓ | 对应成立 |
| 原句 2 | `:42` “I open my eyes…birds, not crows but something smaller” | 是 | Beck（睁眼/辨认） | 悬空黑影＝鸟 | — | 对应成立 |
| 原句 3 | `:103-104` “That’s how I’ve been feeling…” | 是 | Clare | 自己的感受、想站的位置 | “harried by something I couldn’t see”＝被看不见的东西追 ✓ | 对应成立 |
| 原句 4 | `:119` “We scoot closer…heart’s companion” | 就引语本身是；但**起点太晚**：紧接在这句之前的触发链（对视、Beck 的玩笑、Clare 脸红、抓手）整段没进块 | Beck（叙述者）与 Clare 双主语 | 吻、彼此 | “my heart’s companion”→ 说话人是 Beck ✓（md 中文理解为「她」＝Beck） | 提示（P3） |

## 五、块外提示（6 条）

**P1｜Beck 的贵格会（Quaker）身份只出现在词汇表**

原文 `:76`：

> As a Quaker, I have always found quiet very restorative; I crave it.

md 中该句唯一出现处是词汇表（`ch25 a murmuration.md:66`，`restorative` 的例句），正文四个块、「本章导航」「一句话总结」全部没有提她信贵格会。取证：

```
$ /usr/bin/grep -nE "Quaker" "ch25 a murmuration.md" ; echo rc=$?
66:| restorative | 让人恢复元气、安神的 | As a Quaker, I have always found quiet very restorative; I crave it. |
rc=0
```

这条不是可有可无的标签：它解释了本章「安静＝恢复」这一整套价值判断（“I crave it”），也解释了她在鸟群里不喊叫、只等 Clare 说完的举止。判提示（md 有主题层面的「谈静」，只是没落到人物身份）。

**P2｜视角换人（Clare → Beck）没有被点明**

原文 `:23` 章首署名 `Beck:`；本章是第一人称，但说话人从前面几章的 Clare 换成了 Beck（本章末尾“this is how we begin”是第一段关系的起点）。md 只引了带 `Beck:` 的那半句，`中文理解`里写「日记先记下这趟邀约」，`叙事手法`（`:15`）只说「第一人称现在时」，没有一句交代「谁的第一人称」。读者若跳过引号里的 `Beck:`，会把本章误读成 Clare 自述。

**P3｜块 4 起点太晚，接吻的触发链被整段删掉**

原文 `:119`（块 4 引语之前紧接着的部分）：

> “Hmm. Speaking as someone whose Blackness is on display all the time, are you sure you want to do that?” I mean it as a joke but Clare turns bright red and stares at her lap. … She looks up at me and there is an expression of such worry and vulnerability and naked longing on her face that I reach over and take her hand. Her fingers curl around mine. We sit still, touching hands, looking into each other’s eyes. I feel strange, as though I’ve just seen my soul in a mirror.

块 4 从 “We scoot closer together on the sofa” 起引，上面整段被切掉；`/usr/bin/grep -nE "soul in a mirror"` → `rc=1`。后果：接吻在 md 里变成「喝着酒就靠近了」，而原文的因果是「一句玩笑伤到她 → 她脸红低头 → 她抬眼时那份赤裸的渴望 → Beck 才去抓手 → 对视 → 靠近」。这正是 R4 要追的「谁先动的手、为什么」。

顺带一处词面损失：原文的笑点靠大小写——Clare 说的是小写 `blackness`（心里的黑），Beck 回的是大写 `Blackness`（作为黑人被围观的身份）。这一处双关正是那句玩笑会伤人的原因，md 里 `Blackness` 整词不出现（`grep -nE "Blackness"` → `rc=1`），只译成「心里的黑」，双关全平。

**P4｜手机看真实鸟群那段没进任何块**

原文 `:84-85`（Clare 掏手机放视频）与 `:94`（“Probably there is a predator, maybe a hawk. There’s a whole scientific discipline, flocking behavior…”）。md 中 `grep -nE "flocking"` → `rc=1`；总结只有「谈群飞的鸟」。这段给了作品一个现实参照（椭圆→锥→蘑菇），也是 Clare 少见的「解释自己」的时刻。

**P5｜日期与三人年龄：md 说抬头给了，正文却没抄**

原文 `:18`：

> Saturday, April 17, 2010 (Clare is 38, Beck is 34, Alba is 8)

md `叙事手法`（`:15`）写「日记体抬头先给出日期与三人的年纪」，但 md 任何位置都没有出现 `2010-04-17` / `38` / `34` / `8`。这是「说了有、实际没有」的自指缺陷。

**P6｜末句未引**

原文 `:143`：

> …and wonder what I should do with myself in the blank hours until she calls and this is how we begin.

md 总结收在「车开走之后，她开始等一个电话」——把 `and this is how we begin` 这半句丢了，而这半句才是本章（也是这段关系）的点题。`grep -nE "how we begin"` → `rc=1`。

## 六、R4 总评

四块都落在引语所讲的那句话上，没有跑题块，密度也够。问题集中在**块选点**：本章的物理与情感推进是「牵手（鸟群中）→ 抓手（沙发上）→ 吻」三级，md 只收了第三级，前两级都没进块（P3 里一并指出）。另外，本章是全书第一次把叙述权交给 Beck，md 对此零解释（P2）——这是形态层最该补的一句。
