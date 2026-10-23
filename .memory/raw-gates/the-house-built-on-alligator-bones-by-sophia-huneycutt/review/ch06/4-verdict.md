# ch06 深审判定表（R5）

章：`ch06 long lost granddaughter meets gazzie.md`（书内 Chapter Five，H1 `# 06. Chapter Five` ✓）
语料：`text/ch06_chapter_five.txt`（367 行）
流程：R1 素读（74 条事实／0 MISS）→ R2 机器层（后台批 `b2m0vkj06`，verdict `ok`）→ R3 三张单子 → R4 逐块对应 → 本表

## 四组报数

| 组 | 判据 | 结果 |
|---|---|---|
| 逐字 | 引语块 10／分片 15／MISS 0；机器层 quote_long 0、segment_miss 0；直撇号探针（`/tmp/apos.txt`）本章 0 站 | 🟢 全绿 |
| 对应 | R4 逐块回源：10 块 anchor 全在素读表内；漏项按「整块信息单元缺失」计 | 🟠 阻断 4（C-06-7 三幅画／C-06-8 手腕与折翼鸟／C-06-9 phosphate deal／C-06-10 Michelle 在场）＋提示 5（P-06-10～P-06-13、P-06-1 参照物） |
| 形态 | nav 5 项 ✓／子项四项齐 ✓／blocks 10 ∈ [6,10] ✓／words 3204／struct_bad 0／keyword_bad 0 | 🟢 全绿（词表两行共用同一例句、四个本章新词未收录＝P-06-14 提示） |
| 断言 | 分析层／导航层的归属·时序·全称·计数·凭空·词源 | 🔴 阻断 6（C-06-1 母女凭空、C-06-2 全称跨章失据、C-06-3 计数、C-06-4 凭空事件、C-06-5 词源、C-06-6 章内时序）＋提示 9 |

**本章合计：阻断 10 ／ 提示 14 ／ 假红-不报 6**

## 缺陷形态归因（供全局汇总用）

- 亲属称谓凭空（C-06-1）：把 sister 关系写成母女——与本项目既有事故同类（Mara／Sharise／Patty 长幼反转家族）；本章的证据就在同一页（:165），属「就近可查却未查」。
- 全称断言跨章失据（C-06-2、P-06-9）：「不是出自任何家人的介绍」「压在每轮情绪末尾」——两条都是把「本章没写」扩成「全书没有／每轮都是」；核法＝`/usr/bin/grep -rn "great-great" text/ch0[1-5]*.txt`。
- 章内时序（C-06-6）：开席动作挪到饭毕——本库缺陷簇第一名，本章再现。
- 计数（C-06-3）：同一文件内「四个词」对、「两个词」错两处 ⇒ 不是口径问题，是未数。
- 词源／外部知识（C-06-5）：新形态，建议进全局类「非文本语言学断言」。
- 漏（C-06-7～C-06-10）：四个整块单元，其中两个是本文明显的未来回收点（:129 `That image lingered for a long time afterward`、:192 女人挖大宅），漏掉的代价最大。

## 已核实为正确（下轮勿改坏）

1. `:21 This was the original.` 的「四个词」计数、以及「床头那幅是复制品」的推论方向 ✓（:24 `my own copy` 佐证）。
2. 跨章预告「同一件东西还会分出两个版本」✓：后文确有原作／复制品分裂（ch13:150、ch16:279、ch30:114、ch43:15 `the single original portrait containing only a few strands of hair`）。
3. `:27` 两个 like 从句的主语从 it（颜料）滑到 she（画中人）✓；`began again`＝并非头一回 ✓（ch05:156 已有一次）。
4. 名字后置论 ✓：Harrison 之名本章首现于 :168 `“Harrison’s waiting.”`，叙述者的对号在 :171；:36 的初描写不含姓名。
5. 「身份信息分给三张不同的嘴」✓：:51＋:90（Harrison）／:165（Virginia 说 `forgive your grandmother`）／:285（Gazzie 只给继承人结论）。
6. 厨房半句争吵 ✓：:110 `“—unbelievable. I’m sick of—”`、:112 `“—thank me later for—”`，叙述者确实听不全。
7. 「借眼睛」两次账目与递进 ✓：:45 `this stranger the family member, me the intruder` → :303 `a pathetic hanger-on`。
8. 重构段的否定式推论描述 ✓：:300 `Aunt Virginia had never claimed Gazzie wanted me at Greer House; she’d said she wanted me to visit, so she could get to know me.`＋`She must have told Gazzie…`＋`That’s what they’d been fighting about.`
9. 章末「恶意不需要观众」的落点 ✓ 只在 :363-366（洗碗机后、楼梯前对鳄鱼皮 `stomping past`）成立；晚餐段不成立（见 P-06-8 的限定改法）。
10. `:159 “Not a compliment.”` 紧跟在 `:158 “Thank you.”` 之后、更正先于叙述者反应（:162 `My mouth popped open.`）✓。

## 不许裁决（本章内）

- Virginia 与 Gazzie 谁是姐姐／谁是妹妹：原文只 `her sister`（:165）、`the sisters’ dynamic`（ch08:192），排行不写——只可写「姐妹」，不得补长幼。
- 「she changed her last name」所指：原文 `Mama, presumably.`（:153）是叙述者推断；不得写成定称（P-06-4）。
- Ida 是否确为曾曾祖母：Harrison 的 :90 与叙述者 :93 `So my instincts had been correct; Ida was a relative. A fairly close one.` 是本场的说法；ch05:219 的条件式与 ch30/ch43 的「原作含头发」属后续材料，本章不裁决超自然是否真实。
- :27 画下「水面下有生物轮廓」与 :192 女人挖宅：只登记意象，不断言其指涉何事。
- Michelle 之死的地点与方式：本章只给「活着站在舵位」的回忆（:234），不得与 ch04:168 的新闻报道合并成结论。
