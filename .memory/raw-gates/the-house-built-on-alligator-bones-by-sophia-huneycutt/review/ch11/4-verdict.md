# ch11 深审判定表（R5）

章：`ch11 aunt virginia confesses letter forgery.md`（书内 Chapter Ten，H1 `# 11. Chapter Ten` ✓）
语料：`text/ch11_chapter_ten.txt`（132 行／7,595 B）
流程：R1 素读（96 条事实／0 MISS）→ R2 机器层（verdict `ok`）→ R3/R4 → 本表

## 四组报数

| 组 | 判据 | 结果 |
|---|---|---|
| 逐字 | 引语块 4／分片 4／MISS 0；无 `…` 拼接块；词表 16 行例句展平逐字 0 MISS；直撇号 0 站 | 🟢 全绿 |
| 对应 | 4 块 anchor 全在素读表内；缺项：:78 天气与 hurricanes、:12 回避与「别被听见」、派对清单本体 | 🟠 阻断 1（C-11-8）＋提示 3（T-11-8／T-11-9／T-11-1） |
| 形态 | nav 5 项 ✓／子项四项 ✓／blocks 4 ∈ [2,4] ✓／words 1248／struct_bad 0 | 🟢 全绿 |
| 断言 | 事件归属（信引来谁）／全称×3／语法误称／章内时序／凭空属性 | 🔴 阻断 7（C-11-1／2／3／4／5／6／7）＋提示 6 |

**本章合计：阻断 8 ／ 提示 9 ／ 假红-不报 9**

## 缺陷形态归因

- **把「未发生的事」写成已发生**（C-11-1）：md 用「引来母女的信」概括一桩**反事实**（重聚从未发生，Mama 已死于手术并发症，ch02:107）。本类与前章 ch09 C-09-5（已出场写成未出场）互为镜像——**跨章状态词（引来／出场／团聚／去世）必须回源核实，不能靠本章语感**。
- **「所有／每桩／每当／全部」四连全称**（C-11-2／3／6／7）：本章导航与块层共出现 4 处全称，全部有反例。⇒ 规则建议：**导航层与「为什么这样写」里的每个全称，落笔前先自问「我能列出反例吗」**，列不出就改成「这两项／这三桩／本章这一笔」。
- **凭空属性靠修辞顺手带入**（C-11-6「与阳光」）：与 ch08 的黑暗养殖正面冲突。生产时对「家族生意」的想象词最容易越过原文设定。
- **章内时序**（C-11-5）：情感弧线把中段的情绪词当成末拍——md:11 这种「起点→中段→落到→最后停在」的四段句式是全库高危模板，**每一段都要对行号**。
- **语法术语**（C-11-4）：与 ch08 C-08-6、O. Henry 批次登记的「语法类别名用错」同族；本章错在把完整句 `That’s why…` 与残句 `Why it had claimed…` 归为同一形态。

## 已核实为正确（下轮勿改坏）

1. `:9` 温室全套：早餐自助餐（香肠／蛋／grits）／与厨房相连的明亮通风房间／Virginia 浇紫色非洲堇／part of Greer House, yet also apart from it／无墙、锻铁＋玻璃／黑白格地砖／**built by her mother**（未误作 Ida）／`Though they barely do better in here` ＋ `This damn house.` ✓——块 1 的中文理解与「铁框玻璃把佛罗里达挡在外面」均对应。
2. `:12` 藤椅黑白条纹坐垫／冰茶／心不在焉地欣赏红色凤梨花／Virginia 细数下午进城散步的安排 ✓（T-11-1 只纠「下午茶」措辞，物件本身正确）。
3. `:15`→`:18` 「问题一成形答案就咔哒落位」＋`“I’d like to work at the farm while I’m here,” I blurted out.` ✓；`:24` 她的两层补充（`Gazzie told me more about it this morning` 是当面对 Virginia 的假话／`less certainly, “Since it’s my heritage and all.”`）——md:13「动机不是好奇而是入场券」有 :12＋:24 双凭据 ✓。
4. `:27` 洒水壶放在格砖地上／坐进旁椅／leaning forward eagerly／`I’m so glad to hear you say that.` ✓；`:21` raised her eyebrows, the hint of a smile ✓。
5. `:33`→`:36` 坦白前的清嗓与「皮肤发麻」✓；`:39` `eyes tracking a mockingbird as it swooped down from the oak tree outside` ＋ `Worried this whole hullabaloo might scare you off.` ✓（词表 :65/:77 两条例句逐字命中）。
6. `:42` `My mind flitted to the farm problems Gazzie had mentioned. They must be more serious than she’d implied.` ✓——md:12「开篇的信露出第二双手」没有把农场故障当成已解释项，留白正确。
7. `:45`→`:51` 坦白两步（先动机后签名熟稔）与 md:14 的顺序判定一致 ✓；`:48` `“And Gazzie signed it?”` 是 Dart 的提问、不是 Virginia 的陈述 ✓（T-11-2 只要求把「仿」的归属说清）。
8. `:57` 双向自陈：`even as part of me acknowledged I’d lied when I emailed her, saying Mama had intended for us to meet. Still—she’d manipulated me into meeting her.` ✓——md:10／md:13 未把 Dart 写成纯受害者（「她自己那封邮件也撒过谎」这一层保留在素读表内，md 若日后补写有据）。
9. `:63` `I froze, blinked away the image. What was wrong with me?`／`:66` `Embarrassed by her confession, she’d looked away.`＋`Caroline` 之名首次出现 ✓／`:69` `anger already overcome by shame`…`To prove I was a kind, forgiving person.` ✓。
10. `:72` 抽回手／翻辫子／摩挲缎带／`Every summer solstice, we celebrate the business’s founding. It’s the anniversary of Ida—` 与 `:75` `“Shooting Ironheart,” I finished, showing off my new knowledge. “Gazzie told me.”` 的接话关系 ✓（知识来源＝ch05:141，md 未误记成本章新得）。
11. `:87` `she’ll never retire, the old donkey`／`wants to name an heir. Publicly`／`She mentioned it during our first dinner together, remember?` 有前章实据：`text/ch06_chapter_five.txt:285` ✓；`:90` `Aunt Virginia couldn’t be younger than seventy`／`at most, a few years after Gazzie’s death` ✓——md 未把这两条当成 Virginia 的自述。
12. `:93` `“Lord, no, Dartrine.”`（叙述者全名由 Virginia 叫出）／`at gunpoint`／辫子咚地砸在胸前／`founding in the late 1800s`／`three generations of Greer women` ✓——md 未把三代名单坐实（正确留白）。
13. `:99` `I’d hoped your mother might take over. But now, it’s up to you.` ✓；`:102` 两只松鼠／HR manager→director／Atlanta／Charlotte／DC／`poorly functioning body` ✓；`:105`→`:108` 「已经选定的继承人」与 `Not even Harrison.` ✓；`:111` `His name hit me like a steel wall.` ✓。
14. `:117` `She’ll change her mind once she sees you’re capable.`／`:120` `learn the entire business before solstice`／`:123` `Despite her resistance, she’s—`…`Family oriented.`（找词的姿态原文自带）✓；`:126`→`:132` 收尾三连 ✓。
15. 词表 16 行例句全部为原文逐字子串（展平＋弯引号归一，0 MISS）。

## 不许裁决（本章内）

- **Harrison 是否真是内定继承人**：`So he was Gazzie’s heir apparent.`（:114）是 Dart 的推论；Virginia 只说 `Not even Harrison.`（:108），Gazzie 本人本章未表态。不得坐实，也不得据此裁决「农场由谁接」。
- **「外人」的定义**：:108 把 Harrison 归入「外人」，但原文未写他的血统／姓氏与 Greer 家的关系；不得推断他与家族有无血亲。
- **「三代 Greer 女性」的名单**：:93 只给代数；不得点名列举（Ida／Virginia 之母／Virginia 与 Gazzie 的具体排位本章未给）。
- **温室「她母亲」是谁**：:9 只说 her mother；与 Ida 是否同一人、她与 Gazzie 的继承顺位，本章一律未写。
- **派对当晚天气「总是配合」是否超自然**：:78 自带 `Somehow,`，本章不作解释；不得裁决。
- **农场正在闹的麻烦**：:42 `whatever the hell was going on at the farm`（:114 亦然）延续 ch08 的未决事项，本章不给内容。
- **Virginia 仿签名的动机边界**：:66 她说 `I didn’t see the harm in it`，:54 Dart 判为「操纵」；两种评价并存，不得裁决谁对。
- **「Mama 本意要让她们相见」**：:57 是 Dart 自己那封邮件里的说法（她自认撒过谎），不得当作 Mama 遗愿的证据。
