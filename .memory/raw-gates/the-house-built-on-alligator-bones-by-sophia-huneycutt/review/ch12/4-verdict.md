# ch12 深审判定表（R5）

章：`ch12 dart sent to digitize files.md`（书内 Chapter Eleven，H1 `# 12. Chapter Eleven` ✓）
语料：`text/ch12_chapter_eleven.txt`（163 行／7,094 B）
流程：R1 素读（82 条事实／0 MISS）→ R2 机器层（verdict `ok`）→ R3/R4 → 本表

## 四组报数

| 组 | 判据 | 结果 |
|---|---|---|
| 逐字 | 引语块 4／分片 4／MISS 0；无 `…` 拼接块；词表 16 行例句展平逐字 0 MISS；直撇号 0 站 | 🟢 全绿 |
| 对应 | 4 块 anchor 全在素读表内；缺项：:126（Virginia 逼记账／两座分场）、:78（画像的笑）、:150、:84 | 🟠 阻断 2（C-12-5／C-12-6）＋提示 2（T-12-6／T-12-7） |
| 形态 | nav 5 项 ✓／子项四项 ✓／blocks 4 ∈ [2,4] ✓／words 1154／struct_bad 0 | 🟢 全绿 |
| 断言 | 形态误称／归因结构结论／与本章相抵／施事／跨章全称预言 | 🔴 阻断 5（C-12-1／2／3／4／7）＋提示 3 |

**本章合计：阻断 7 ／ 提示 7 ／ 假红-不报 8**

## 缺陷形态归因

- **「把叙述者推断当结构结论」的新变体**（C-12-2／C-12-3）：Dart 在本章两次即时归因（:66 `Of course. He’d suggested a task…` 与 :141 `Gazzie was sending a message`），md:12 把前者升格成「农场真正的运转握在中层手里」，md:34 又据 Virginia 的一句话得出「Gazzie 不在规则链里」——两条都与本章的明写命令（:63/:69/:93/:147）相抵。⇒ 规则建议：**「谁在真正掌权」类结论，必须先枚举本章所有 `X said/commanded/orders` 落点后才行文**。
- **语言单位误称**（C-12-1）：`single-word sentences` → 「单音节对白」。与前章 ch11 C-11-4（把完整句称作残句）同属「分析层的形式判定」类，且本章 md:10 与 md:14 自相矛盾，属可在自查里发现的一类（**同卷两处口径不一致＝报警信号**）。
- **短章的画像级线索被词表吸收**（C-12-6）：`pronounced`／`gaze` 进了词表例句，却没进导航——生产时「进了词表＝已登记」的错觉。⇒ 规则建议：**凡原文带 `Again`／`Since the last time`／`again I noticed` 的复看句，必须落进导航或某个块，不接受只出现在词表。**
- **对冲词漏收**（C-12-3/C-12-5 的 `Or so she said. I wasn’t around then.`；T-12-5 的 `seemed`；T-12-7 的 `Presumably`）：本章叙述者对每条关键情报都挂了对冲，md 三处把对冲摘掉后写成了已然。同族：ch09 C-09-1、ch11 T-11-4。

## 已核实为正确（下轮勿改坏）

1. `:9` 全段：次晨 Gazzie 在 SUV 旁等她、`without a word of complaint`／`I assumed our bonding session had a stronger effect than I’d thought`／到场时 Harrison 俯在前台与 Nova 深谈／两人停话转身 `appraise us` ✓——md:11「起点是温的」有凭据。
2. `:12`→`:21` 介绍链（`Nova, you remember Dart. Harrison, this is Dart.`／`“We’ve met,” I said stiffly.`／`“Briefly,” Harrison clarified.`／`“He manages the farm for me. What he says goes.”`）✓ md:12 的「Harrison 的地位被 Gazzie 当众坐实」逐字对应。
3. `:24` `like I was just along for the ride, like I wasn’t here to upend the current order of things`／`Out of Gazzie’s view, Harrison smirked at me`／`the sinking suspicion he wouldn’t make this easy`／`Before I could repress the urge, I narrowed my eyes at him` ✓——md:13「一日内反复」的两极正是这两句。
4. `:30`→`:45` 漏水段全链：`“Goddammit,” she groaned.`／Harrison `Rained pretty heavy last night`／Nova `Think the crack in the break room’s related?`／`“Call the roofers after the plumbers come by… We’re under warranty.”`／`“On it,” Harrison said smoothly.` ✓（md:24 未把「break room 那道裂」写成同一道，正确留白）。
5. `:39` `Roof leaks, I decided, must be a recurring problem, like the algae.`／`It wasn’t run-down; it was spotless, the front desk and filing cabinets well-kept.`／`Nature just seemed intent on interfering with the property.` ✓——md:24 引用 `Nature…` 时标明是「Dart 自己给出的判词」✓。
6. `:48` `Suck-up. I rolled my eyes, and he pursed his lips, attempting to hide another smirk.`／`:51` `oblivious to our exchange`＋`Pushing her glasses into her hair`＋`Dart has volunteered to digitize our files.` ✓（md:10「被 Harrison 提议成数字化档案」的措辞与 :51 `volunteered`／:63 `Harrison pointed out`／:66 `He’d suggested` 的链条不冲突）。
7. `:54` `After the way she’d opened up yesterday, I’d hoped she’d let me shadow her, learn more about the farm.` ✓——**时间线自洽**：ch10 夜谈＝ch11 早餐同一日清晨，本章是次日，故 yesterday 指夜谈日 ✓。
8. `:57` `She spoke without inflection.`＋Princess Diana’s ghost／alligator-skin fedora 的荒诞假设 ✓（md:14 的「低温喜剧化」判定成立，只是「单音节」错）。
9. `:60`→`:66` `grateful that Nova had teed me up`／`He smiled sweetly, tilting his head an inch to the side.` ✓。
10. `:75`→`:81` Nova 的橄榄绿 macramé 手袋／润唇膏 leisurely／`trying to wrangle my expression into something resembling calm`／`her gladiator sandals dragging on the low-pile carpet`／Yes. No. 单字作答／`She wasn’t invested in Greer Fine Alligators` ✓——md:44「连最不在乎这份工的人」由此而来 ✓。
11. `:84`→`:99` 金属双门＋上方第二只摄像头／方形窗里的亮白走廊／`Presumably, this was the processing area`／山羊胡亮绿 T 恤男／`Everything behind that door is off-limits`／`Gazzie’s orders.`／`It’s dangerous. Alligators and all.` ✓。
12. `:105`→`:117` `There’ve been accidents in the past.`／`telling myself Gazzie would give me a proper tour later`／储藏室 `floor to near-ceiling`／`festering for years, if not decades`／`Mildew perfumed the air`／`They date back to the seventies.`／Dart 抬嗓门指望 Gazzie 听见 ✓。
13. `:123`→`:135` `If the business had started in the Victorian era, there would be multiple rooms stuffed with papers.`／`Nova looked like she didn’t want to be around now, either.`／`you can throw out anything dated before 2009… dig back more than ten years` ✓（两个数字逐字）。
14. `:138`→`:156` `shooting me a sympathetic glance`／`Heat spread across my cheeks`／`You’re not one of us. Even Nova had picked up on it.`／`Company policy. No unauthorized guests or employees outside administrative areas.`／:156 的四单项证据清单 ✓。
15. `:159`→`:162` `I cracked open the first lid, and the mildew smell intensified.`／`Resigned, I pulled out the first file.` ✓（md 未把结尾写成悬念，处理正确）。
16. 词表 16 行例句全部为原文逐字子串（0 MISS）。

## 不许裁决（本章内）

- **档案为何缺失**：:135 `even with so much missing` 只给状态，缺什么、谁弄缺的，本章一律未写；不得推断被销毁或被搬走。
- **Harrison 的血统／姓氏与 Greer 家的关系**：:21 只说他替 Gazzie 管农场，:126 的「外人」判定在 ch11；本章不得坐实他是否继承人。
- **上锁那一侧到底有什么**：:84 的 `Presumably`＋:87 的 `off-limits`＋:99 `It’s dangerous. Alligators and all.`＋:105 `There’ve been accidents in the past.` 四层都只给禁令与模糊理由，不得补写事故内容。
- **「几天前那桩未命名事故」是否发生在外面**：:150 是 Dart 的推断（`must have happened outside`），且她把 :57 听到的 `out back` 当成依据；不得裁决。
- **Ida 画像的笑是否真的变了**：:78 `Since the last time I’d seen her, the smile on her lips seemed more pronounced.` 带 seemed；超自然与否一律不裁决。
- **「Virginia made Gazzie start tracking paperwork」的可靠性**：Nova 自己加了两层对冲（`Or so she said. I wasn’t around then.`），不得当成既定行政史。
- **山羊胡男员工与 ch08 的喂料工是否同一人**：原文未写。
- **「Gazzie 在放话」是否为 Gazzie 的本意**：:141 是 Dart 的解读，本章 Gazzie 无对应台词；不得裁决她是否真有此意。
