# ch12 R3 对账 + R4 逐块判定（R3 对账员 / R4 逐块判定员）

- 书：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/`
- md：`ch12 chapter 12.md`（137 行；7 个引语块 md L20/31/42/53/64/75/86）
- 素读：`review/ch12/1-suread.json`（8 条 fact）
- 原文：`text/ch12_chapter_12.txt`（261 行）
- 判定方法：逐 fact → 逐 md 落点；「编」类一律回 `text/` 核实并附原文行号；引语块↔分析行对应性逐块核（同一 md 文件内、相邻）。
- 本次**未修改任何既有文件**，只写本文件。

---

## 0. 先说三条前置核查结论

1. **无移章/编（序章污染）**：`ch12 chapter 12.md` 全文 grep `Brigitte` / `芭蕾舞鞋` / `耳鸣` / `tinnitus` / `序章` / `prologue` / `ch00` = **0 命中**。md 写的镜子是「试鞋镜 / mirrors for trying on shoes」（`ch12 chapter 12.md:22`），与 `text/ch12_chapter_12.txt:6` 一致；序章的「mirrors where girls admired their ballet slippers」只在 `text/ch00_prologue.txt:21`。⇒ **md 没有把序章的事写成 ch12 的事**。
2. **引语逐字**：7 个引语块全部在 `text/ch12_chapter_12.txt` 中**逐字连续命中**（原句1=text L6；原句2=text L21–84；原句3=text L87–156；原句4=text L162–165；原句5=text L168；原句6=text L186；原句7=text L198–261）。**没有编造的引语**。
3. **三行无归属诗确认是 ch12 独有**：`text/ch00_prologue.txt` grep `thorn` / `left one memory` = 0 命中；`text/ch12_chapter_12.txt:9/12/15` = `When she left, she left one memory` / `A thorn sticking right into me` / `A thorn stuck in my heart`。⇒ 素读 F1 的「三行诗」是本章新增，**md 完全未收**（详见 R3 F1）。

---

## 1. R3 三张单子（8 条 fact 逐条判）

### F1｜Alba 在 Claire's 童品店醒来：分阶段亮灯／像一记耳光／芭蕾舞裙溅红／照试鞋镜／九个耳环（一耳 5 一耳 4）／"那段毫无记忆的预约一定漫长、不卫生、残忍" ／**夹在醒来到下一节之间的三行无归属诗**

| 素读事实 | md 落点 | 判定 |
|---|---|---|
| F1 主干：醒来、灯分阶段亮、亮如耳光、舞裙溅红、试鞋镜、头发结块脸有血污、耳朵九个耳环（5+4、银色、结痂棕黑）、预约"漫长/不卫生/残忍" | `ch12 chapter 12.md:20`（引语逐字 = text L6）、`:22`（中文理解）、`:24`（关键词）、`:26`（句子结构）、`:28`（为什么这样写） | ✅ 一致 |
| **F1 子项：三行无归属诗**（`When she left, she left one memory` / `A thorn sticking right into me` / `A thorn stuck in my heart`） | **无**（md 全文 grep 三行 = 0 命中；原文 `text/ch12_chapter_12.txt:9`、`:12`、`:15`） | ❌ 漏 |

> F1 判语：**部分漏**——主干 ✅ 一致，**三行诗 ❌ 漏**（且这三行是 ch12 相对序章的新增内容，正是本章特别提示要查的项）。
> 附带：md 词汇表 `ch12 chapter 12.md:128` 有 `pom-poms | 彩球 | "pom-poms and all the glitter"`，该例句逐字见 `text/ch12_chapter_12.txt:18`（在引语块外，见第 3 节）。

### F2｜女孩现时形象（靠陈列架、红色泳衣、只露长腿、抱着 Switch 手柄盒）＋ Alba 假装没注意 ＋ 女孩在彩球与亮片间显得更小 ＋ 女孩挺翘的小鼻引发 Alba 怀旧 ＋ **Alba 鼻梁被公园秋千误撞歪、从未矫正、习惯了不够对称的鼻子**

| 素读事实 | md 落点 | 判定 |
|---|---|---|
| F2 主干：对歌对峙（"我不知道你唱到哪了，重来我跟上"／"那不是唱那是说话，唱！"／嗓音嘶哑／"那是副歌，不算"／"因为人人都知道副歌"／"人人都知道，因为它永不过时"） | `ch12 chapter 12.md:31`（引语逐字 = text L21–84）、`:33`、`:35`、`:37`、`:39`、`:40` | ✅ 一致 |
| **F2 子项：女孩现时外貌整段**（陈列架／红泳衣／只露长腿／抱着 Switch 手柄盒／Alba 假装没注意／在 pom-poms 与 glitter 中显得更小／"perfect upturned nose"引发怀旧） | **无**（该段 `text/ch12_chapter_12.txt:18` 不在任何引语块内；md 分析层 0 命中） | ❌ 漏 |
| **F2 子项：Alba 鼻梁被秋千撞歪**（"an errant swing hit her face and knocked her bridge off center"／从未矫正／习惯了不够对称的鼻子） | **无**（md 全文 grep `errant swing` / `knocked her bridge off center` / `鼻梁` / `秋千` / `翘鼻` = 0 命中；原文 `text/ch12_chapter_12.txt:18`） | ❌ 漏 |

> F2 判语：**部分漏**——对歌部分 ✅ 一致；**女孩现时形象段与鼻梁被秋千撞歪 ❌ 漏**。
> ⚠️ 注意别误判：md 里的 `红色泳衣`（`:66`、`:88`、`:94`）指的是**十二岁 Alba 记忆里的泳衣**（text L168/L213），**不是**本章现场那个女孩的红泳衣（text L18）——两处不能互相顶账。
> ⚠️ 附带：女孩在现时场景里抱着 **Switch 手柄盒**（text L18）是与 ch17（Alba 藏手柄）的情节连线，md 完全没写。

### F3｜"你对我耳朵做了什么？" → "我给你戴了些银耳环" → "九个。要不是那个该死的章鱼，我会戴更多" → 骂脏话对白 → 动机"为了让你记住"／"你真的很喜欢圆环耳环" → "我忘了戴，或者没时间"

| 素读事实 | md 落点 | 判定 |
|---|---|---|
| F3 全部 | `ch12 chapter 12.md:42`（引语逐字 = text L87–156）、`:44`、`:46`、`:48`、`:50`、`:51` | ✅ 一致 |

> F3 判语：✅ 一致（含中文层逐句翻译，无截断）。
> 核对点：md `:44` 把"九个。要不是那个该死的章鱼，我会戴更多"译作"九个。要不是那个该死的章鱼，我会戴更多"——原文 `text/ch12_chapter_12.txt:96` 是 girl 说的（"she said, raising her voice"），md 未误标主语。✔

### F4｜"你在忘记你自己。耳环只是个开始" ＋ 三样被忘之物（耳环／Camp La Tortuga Ligera／我） ＋ "你该看看我的露台"／"我看过。不够" ＋ "我开始消失了……几乎没人留下了" ＋ Alba "我希望你早点消失" ＋ 女孩扯耳环（有的松开、有的撕破耳垂）＋ 用破运动鞋踢她腰侧 ＋ Alba 蜷成一团哭、营地回忆涌上心头

| 素读事实 | md 落点 | 判定 |
|---|---|---|
| F4 全部 | `ch12 chapter 12.md:42`（引语 = text L87–156，含 L150/L153/L156）、`:44`（中文理解含扯耳环/踢/蜷起哭）、`:46`、`:48`、`:50`、`:51` | ✅ 一致 |

> F4 判语：✅ 一致。核对点：md `:44` 译"她扯得那么用力，有的耳环松开了，有的却撕破了她的耳垂"＝原文 L156 `She pulled so hard that some hoops unfastened, while others tore through her earlobe`；"用一只破旧的运动鞋踢了她的腰侧"＝`kicked her in the side with one worn-out sneaker` ✔。
> ⚠️ 瑕疵（非事实错）：`ch12 chapter 12.md:44` 有一处**未翻译的英文**「当girl走过来」——应为"当女孩走过来"。属中文层残留，不影响本 fact 判定。

### F5｜营地前史闪回：2005 年 El Prat 机场扩建**径直穿过** Camp La Tortuga Ligera ＋ 关闭后鬼魂留下 ＋ 其他营地同理（Toro Bravo、La Ballena Alegre）＋ 老访客搬到 Cornellà/L'Hospitalet/Bellvitge/Gavà/El Prat 但"分身"仍在 La Tortuga 度假 ＋ 各年龄层、多数是常年晒黑的少年儿童，含 12 岁的 Alba ＋ 鬼魂住进被遗弃的露营车与小木屋 ＋ 父母在酒吧玩纸牌飞镖 ＋ 母亲做三明治、**逼孩子到外面吃以免弄碎屑** ＋ **每周五雷打不动打宾果** ＋ 孩子继续足球联赛、没水也跳泳池降温、衬垫起皮 ＋ DJ 放 'El Venao'、女孩们踩准舞步

| 素读事实 | md 落点 | 判定 |
|---|---|---|
| F5 全部 | `ch12 chapter 12.md:53`（引语逐字 = text L162–165）、`:59`（句子结构逐句含碎屑/宾果/足球/泳池衬垫/El Venao/舞步/sun-bleached hair）、`:57`（关键词 play bingo / El Venao）、`:61`（为什么这样写）、`:62`（读者视角）、`:66`（中文理解） | ✅ 一致 |

> F5 判语：✅ 一致（内容齐备）。但 **`:55` 中文理解**在「母亲们给孩子们做三明治，为了……」处用省略号收尾，**未在中文层覆盖**后半段（碎屑→宾果→足球→泳池→El Venao→舞步）——该缺口由 `:59` 句子结构与 `:57` 关键词补齐，故记 R4 密度不足（见 R4 表 原句4），R3 不判漏。
> 核对点：md `:61` 把 "And on Fridays, without fail, they'd drop whatever they were doing and play bingo" 与 **Diana 的鬼故事**（宾果女士）相连——该鬼故事确在 `text/ch10_chapter_10.txt:774–798`（Diana 视角），连线成立 ✔。md 未标章号，无错标。

### F6｜回现实：女孩挑指甲（**iridescent lilac**）→ 坐地上开盒 → **"Wait a sec"** 把 Switch 手柄塞进自己泳衣里保管 → 美甲：给 Alba **左手**每根指甲点胶、贴 press-ons、伸长手臂、扇开手指、检查 → "What do you think? Cute, right?" ‖ 然后 Alba 二十年：嫁高中男友→带车位公寓→第一个孩子→停工→面包车→第二个孩子是女孩→失去父亲→65 寸电视→第三个孩子是男孩→包办所有节日 → 忘记自主："Alba 只是周围人的延伸" → **"She didn't believe she was oppressed"** → **"Diana was wrong to think she'd never been happier"** → **"But the murmur of the campground was always with her"** → 二十年渴望那个"括号"（唯一责任＝玩得开心，甚至忘了自己有父母）→ **"Her memories were no longer enough. They didn't work for her anymore."**

| 素读事实 | md 落点 | 判定 |
|---|---|---|
| F6 上半（二十年人生清单 + 失去自主 + "Alba 只是周围人的延伸"） | `ch12 chapter 12.md:75`（引语逐字 = text L186）、`:77`、`:79`、`:81`、`:83`、`:84` | ✅ 一致 |
| **F6 子项：美甲场景**（挑 iridescent lilac 指甲、"Wait a sec"、Switch 手柄塞泳衣、点胶贴甲、左手、扇手指、"Cute, right?"） | **无**（`text/ch12_chapter_12.txt:174`、`:177`、`:180` 不在任何引语块内；md 全文 grep `iridescent lilac` / `Wait a sec` / `dotted each fingernail` / `fanned her fingers` / `Cute, right` = 0 命中） | ❌ 漏 |
| **F6 子项：Alba 二十年反思段**（"她不认为自己受压迫"／"Diana 错了"／"营地的低语始终伴随"／"她花了二十年渴望那个括号"／"她的记忆已不够用了，它们不再对她起作用"） | **无**（`text/ch12_chapter_12.txt:189`、`:192` 不在任何引语块内；md grep `oppressed` / `Diana was wrong` / `murmur` / `memories were no longer enough` / `parenthesis` / `twenty years longing` = 0 命中） | ❌ 漏 |

> F6 判语：**部分漏**——二十年人生清单 ✅ 一致；**美甲场景 ❌ 漏**；**"不受压迫 / Diana 错了 / 营地低语 / 记忆已不够用" 整段 ❌ 漏**。
> 附注：md 词汇表 `ch12 chapter 12.md:131` 有 `press-ons | 贴甲 | "each of the press-ons"`（例句逐字见 `text/ch12_chapter_12.txt:177`），**只算一个词条命中，不能顶掉整个美甲场景的缺失**。
> ⚠️ 这段是"Alba 为何恨自己人生"的动机核心，漏掉后 md 对"autophobia"（见第 4 节需人判项）的解释链在章内**没有原文支撑**。

### F7｜"你希望我死了" → 忘了我我就死 → Alba 逐条列要记住的东西（红泳衣、旧 Victoria 鞋、小雀斑鼻、被晒浅的头发、DJ、海滩上的 Camela 卡带、Diana 在小屋里猛放 El Último de la Fila、在浴室化妆不让爸妈看见、所有人戴 Caravaca 十字架的夏天、Mom 在海滩昏倒、两人连睡几天、用冰块和别针穿肚脐所以一周不能游泳）→ 女孩"那是蠢事" → 入口招牌生锈、被树吞掉 → Alba "几天前，我在露台上就看到它在融化" → 女孩落泪"那就是因为你决定要忘记我们"

| 素读事实 | md 落点 | 判定 |
|---|---|---|
| F7 全部 | `ch12 chapter 12.md:86`（引语逐字 = text L198–234）、`:88`（中文理解逐条对应）、`:90`、`:92`、`:94`、`:95` | ✅ 一致 |

> F7 判语：✅ 一致。核对点：md `:88` 的记忆清单逐项对应原文 L213 ✔（"Caravaca 十字架""冰块和别针穿肚脐""一周不能游泳"都在）。
> ⚠️ 关联瑕疵（已核实原文，不判错）：md `:88`/`:92`/`:94` 把 "Mom fainted on the beach" 译作 "Mom 在海滩上昏倒"，而 `text/ch12_chapter_12.txt:213` 是 "when Mom fainted on the beach"——一致 ✔。另一处：素读 F7 写"两人连睡几天"，原文 L213 为 "Diana and I were so scared we slept in the same bed for days"，md 译 "Diana 和我害怕得连续几天睡在同一张床上" ✔。

### F8｜结局：女孩唱 "I long for you, you're forgetting me" → 长久悲伤地看她 → 转身走向出口 → Alba 扶陈列柜艰难跟随 → 首饰在身后尖叫、女孩在几米外走向扶梯 → "等等！别走！" → 眨眼、继续走、**连翻四个筋斗**（Alba 的筋斗曾是全家骄傲、没人再记得）→ 几秒赶到扶梯口、乘上去 → Alba 到底部时女孩已在中层桥栏杆上俯视 → "Don't!" 挥一根手指、腿太软 → 二楼女孩换到更远的桥、拉开数米、背对爬上栏杆 → "No! Please! Wait!" → 女孩.balance 在栏杆上（纤细、圆屁股、金色马尾）→ 抬起双臂像要跳进虚空 → "Alba's body roared" → 触手从她腹部射出、穿过毛衣、撕开内脏 → Alba 昏倒、触手继续 → 展开扑向女孩、女孩躲不开、试图翻过边缘 → 触手拥抱她、抚她的头发、拍抚她、把她拖回 Alba 身边 → **"who unknowingly devoured the girl as she slept"**

| 素读事实 | md 落点 | 判定 |
|---|---|---|
| F8 全部（结局链条直到"devoured the girl as she slept"） | `ch12 chapter 12.md:86`（引语逐字 = text L198–261，**含 L237–261 全段高潮**）、`:92`（句子结构末句＝`"They embraced her, stroked her hair, petted her, and then dragged her back over to Alba, who unknowingly devoured the girl as she slept."`）、`:90`（关键词 railing / tentacles devour / unknowingly）、`:94`（为什么这样写：railing、body roared、embraced、devoured）、`:10`+`:137`（导航与一句话总结均写 "tentacles emerge and 'devour' girl / ends with Alba unknowingly devouring the girl"） | ✅ 一致 |

> F8 判语：✅ 一致（**md 各层都有，且结论与素读完全对齐**）。
> ⚠️ 但 `ch12 chapter 12.md:88` 中文理解在"Alba 赶紧追上去，生怕自己会看不见她。"处**戛然而止**，**没覆盖扶梯顶部栏杆 / 二楼 / 女孩站上栏杆 / 触手 / 吞噬**——本章高潮在中文层缺席（句子结构层有）。记 R4 密度不足（见 R4 表 原句7），R3 不判漏。

---

## 2. R3 三张单子 · 汇总

| 类别 | 条数 | 落点 |
|---|---|---|
| ✅ 一致 | 4 条 fact 整条一致（F3、F4、F5、F7）+ 2 条 fact 主干一致（F1、F2）+ 2 条 fact 主干一致（F6、F8） | — |
| ❌ 漏 | **4 个子项**（分布在 3 条 fact：F1 / F2 / F6） | 见上表 |
| ❌ 编 | **0**（7 个引语块逐字命中原文；md 引语层与词汇层例句全部回 `text/` 核实，无凭空造句） | — |
| ❌ 错 | **0**（导航/一句话总结与素读结局事实一致；无移章、无错标章号、无人数/身份错） | — |

**漏项清单（4）**
1. 三行无归属诗（`text/ch12_chapter_12.txt:9`、`:12`、`:15`）——md 无。
2. 女孩现时外貌段（`text/ch12_chapter_12.txt:18` 全体：红泳衣／Switch 手柄盒／鼻梁被秋千撞歪）——md 无。
3. 美甲场景（`text/ch12_chapter_12.txt:174`、`:177`、`:180`）——md 无。
4. Alba 二十年反思段（`text/ch12_chapter_12.txt:189`、`:192`）——md 无。

---

## 3. 没进扫描集的内容（显式列出）

**A. `text/ch12_chapter_12.txt` 中不被任何引语块覆盖的行（md 无法从引语层覆盖到）**
| 原文行 | 内容 | md 是否有任何提及 |
|---|---|---|
| L1 | 章节号 "12" | 不适用 |
| L9 / L12 / L15 | 三行无归属诗 | **无** |
| L18 | 女孩现时形象 + Alba 鼻梁被秋千撞歪 | **无** |
| L174 | Alba 蜷地哭；女孩在陈列架上挑指甲、选了 iridescent lilac、坐下开盒 | **无** |
| L177 | "Wait a sec" + Switch 手柄塞泳衣 + 美甲（左手、点胶、贴甲、扇手指、检查） | **无** |
| L180 | "What do you think? Cute, right?" | **无** |
| L189 | 无人解释这种依附 / "She didn't believe she was oppressed" / "Diana was wrong to think…" / "the murmur of the campground was always with her" / 二十年渴望那个括号 | **无** |
| L192 | "Her memories were no longer enough. They didn't work for her anymore." | **无** |

**B. md 中我未作事实判定的部分（避免把"未扫"说成"干净"）**
- frontmatter `ch12 chapter 12.md:1–4`、H1 `:6`：无事实断言，未判。
- 词汇分级表 `:97–131`：例句**逐字**核过（`no-man's-land`/`autonomous`/`unknowingly devoured`/`El Prat airport`/`Toro Bravo`/`La Ballena Alegre`/`Camela`/`El Último de la Fila`/`Caravaca crosses`/`cartwheels`/`Victoria sneakers`/`nine hoops in total`/`tutus`/`pom-poms`/`escalator`/`mezzanine`/`press-ons` 全部命中原文）；**`ch12 chapter 12.md:115` 例句 `"when the DJ played ‘El Venao’"` 非逐字**（原文 `text/ch12_chapter_12.txt:165` 为 `when the DJ played “El Venao,”`，引号形式 + 逗号位置不同）——已核实内容确在原文，**不判编**。
- 引语块之间的散文过渡段（md 引语块之间被合并的相邻段落）不单独判事实。
- `text/` 中 ch12 之外的章节只用于**核实 md 是否有移章/错标**（已查 ch00 / ch05 / ch10 / ch11 / ch14 / ch16），未对那些章节做事实判定。

---

## 4. 需人判（不猜，交人）

| # | 位置 | 问题 | 我已核到的事实 |
|---|---|---|---|
| N1 | `ch12 chapter 12.md:72`、`:73` | md 断言"她自 2005 年起就在那里，**如今约 2025 年**"、"时间线（2005-2025）"——**2025 这个年份原文没有**（`text/` 全书只有 `2005` 一个年份） | 原文只有 2005（`text/ch12_chapter_12.txt:162`）与"for twenty years after that"（L168）/"she had spent twenty years longing"（L189）。⇒ 2005+20 的换算是**md 的推算**（已用"约"字限定），非原文事实。请人判：分析层允许此类推算，还是应删。 |
| N2 | `ch12 chapter 12.md:73`、`:84`、`:137` | md 引入 **"Alba 的自闭恐惧 / autophobia"**——本章原文无此词 | 词条在**跨章**原文 `text/ch05_chapter_5.txt:543`："autophobia, the irrational fear of being alone"（**怕独处**，不是自闭症）。⇒ 内容确在原文（不判编），但属**跨章引入**；且中文译名"自闭恐惧"极易被读成自闭症，**与原文定义（怕独处）易生歧义**；`:137` 写成 "Alba's autophobia = fear of forgetting"（把"怕独处"直接等成"怕遗忘"），属措辞漂移。请人判是否改写为"独处恐惧"。 |
| N3 | `ch12 chapter 12.md:10`、`:137` | 导航写 "**girl reveals** Camp La Tortuga Ligera ghost backstory"，但 2005/鬼魂/关闭过程那段是**叙述者闪回**（`text/ch12_chapter_12.txt:162–168`），不是女孩口述 | 女孩口述的是"我开始消失了，像营地消失了……"（text L150）。⇒ 摘要层主语略偏。请人判是否改为"叙述插入营地前史闪回"。 |
| N4 | `ch12 chapter 12.md:61`（属 原句4 的"为什么这样写"） | 该行引用了 "Twelve-year-old Alba, with her red swimsuit and sun-bleached hair"，此句在 `text/ch12_chapter_12.txt:168`，属**原句5** 的引语块（md `:64`）而不在原句4 块内 | 属同一文件、相邻的**有意的回响式引用**（原文确有此句），按硬性纪律 1（禁止跨块拼装"错位"）**不判引语选短**。但请人判是否改注"见原句5"以免读者误以为在原句4 内。 |
| N5 | `ch12 chapter 12.md:44` | 中文理解里出现未翻译的英文"**当girl走过来**" | 应为"当女孩走过来"。属中文层残留，不改事实。 |

---

## 5. R4 逐块对应人判（7 个引语块）

| 块 | 引语首 20 字 | 判定 | 依据（哪一行分析） |
|---|---|---|---|
| 原句 1 | "Alba came to in the dark, spra" | 对应 | 中文理解 `:22`（逐句对应该块 text L6）、关键词 `:24`、句子结构 `:26`、为什么这样写 `:28`、读者视角 `:29`（"convulsions"/"nine hoops" 均在块内；`:29` 的 ch11 镜像对照已核实 `text/ch11_chapter_11.txt:87–99` 成立） |
| 原句 2 | "'I know that song,' she said to t" | 对应 | 中文理解 `:33`（整段对应对话）、关键词 `:35`、句子结构 `:37`、为什么这样写 `:39`、读者视角 `:40`；分析对象全在 text L21–84 内 |
| 原句 3 | "'What did you do to my ears?' Al" | 对应 | 中文理解 `:44`、关键词 `:46`、句子结构 `:48`、为什么这样写 `:50`、读者视角 `:51`；分析对象全在 text L87–156 内 |
| 原句 4 | "In 2005, the El Prat airport expa" | 密度不足 | 中文理解 `:55` **以"……"收尾**，未覆盖碎屑→周五宾果→足球联赛→没水也跳泳池/衬垫起皮→DJ 'El Venao' 女孩踩舞步（`text/ch12_chapter_12.txt:165`）这一整段；该缺口由句子结构 `:59`、关键词 `:57`、为什么这样写 `:61` 补齐 ⇒ 块本身对应，但中文层密度不够 |
| 原句 5 | "As the years went by, the ghosts of L" | 对应 | 中文理解 `:66`、关键词 `:68`、句子结构 `:70`、为什么这样写 `:72`、读者视角 `:73`；分析对象全在 text L168 内（`:72` 的 2025 推算见 N1，不影响对应性） |
| 原句 6 | "If Alba had taken refuge for too lon" | 对应 | 中文理解 `:77`、关键词 `:79`、句子结构 `:81`、为什么这样写 `:83`、读者视角 `:84`；分析对象全在 text L186 内 |
| 原句 7 | "'You wish I were dead,' the girl sa" | 密度不足 | 中文理解 `:88` **止于"Alba 赶紧追上去，生怕自己会看不见她。"**，未覆盖**本章高潮**（扶梯顶部栏杆/二楼/女孩爬上栏杆/触手射出/吞噬，text L249–261）；句子结构 `:92`、为什么这样写 `:94`、关键词 `:90` 有覆盖 ⇒ 块本身对应，但中文层漏掉高潮段 |

**R4 小结**：对应 5 · 密度不足 2（`:55`、`:88`）· 引语选短 0 · 不对应 0。
**未判**：无（7/7 块均已判）。
