# ch07 深审判定表（R5）

章：`ch07 mothers handwriting on the closet wall.md`（书内 Chapter Six，H1 `# 07. Chapter Six` ✓）
语料：`text/ch07_chapter_six.txt`（100 行／5,915 B＝短篇档）
流程：R1 素读（36 条事实／0 MISS）→ R2 机器层（`2-machine.json` verdict `ok`）→ R3/R4 → 本表

## 四组报数

| 组 | 判据 | 结果 |
|---|---|---|
| 逐字 | 引语块 3／分片 3／MISS 0；三条墙句与两段引语逐字核对 ✓；直撇号探针本章 0 站 | 🟢 全绿 |
| 对应 | 3 块 anchor 全在素读表内；但本章四条墙句只落地三条、Mama 的直接引语整句缺失 | 🟠 阻断 2（C-07-6 `Death was our beginning`、C-07-7 `No one is safe around you`）＋提示 3 |
| 形态 | nav 5 项 ✓／子项四项 ✓／blocks 3 ∈ 短篇 target [2,3] ✓／words 1015／struct_bad 0 | 🟢 全绿（词表未收 `skeleton key`/`Polaroid`/`hall monitor`/`croaked`＝P-07-7） |
| 断言 | 导航与总结层的事实／归属／外貌／裁决 | 🔴 阻断 5（C-07-1 不画画、C-07-2 短发、C-07-3 钥匙↔把手、C-07-4 裁决门外、C-07-5 whir↔creaking 借口）＋提示 4 |

**本章合计：阻断 7 ／ 提示 7 ／ 假红-不报 6**

## 缺陷形态归因

- 短篇章的特有失效方式：块数被档位允许（3 块），承重信息就全压在导航五项里 ⇒ 本章 5 条阻断中 4 条落在 md:10／md:12／md:13／md:14 这四行导航句上。⇒ 短篇章的人判重点应是导航层，不是块层。
- 道具归属漂移（C-07-3）：`hidden in the intricate handle` 被搬到钥匙上——与本项目既有「道具张冠李戴」同类（ch05 的 fifteen feet、ch02 的一人深）。
- 悬置项被关掉（C-07-4）：md:13 与 md:46 在同一文件内互相推翻；这类「导航裁决、块层存疑」的组合要在总账里单列。

## 已核实为正确（下轮勿改坏）

1. :43 `The Greers built their fortune on alligator bones` 逐字、位置（:33 墙的底部、银色马克笔）✓；md:20 中文理解逐项对应 ✓。
2. 三条墙句的引用与顺序 ✓：:43（第一，md:18）／:68 `The devil’s inside` 与 :71 `She’s in us`（并排两条，md:14／md:36）；「一遍比一遍潦草」✓ :64。
3. 「Mama 的笔迹」认定 ✓ :36；「比她长大的那版不优雅、更年轻更少练习」✓。
4. 临终话的完整两段 ✓ :75 `She’s in you, she’d croaked, the whites of her eyes shining in the dark, her shaking finger pointed at me in accusation. She’s in you, too.`；`too` 的扩展论断 ✓。
5. 互文三联 ✓ :75 `You’d better tame that devil in you, girl`／:68／:71——三处同章相邻，md:14 成立。
6. 月光作为照明器的三级递进 ✓ :21／:39／:64。
7. 反锁与决定的先后 ✓ :81（决定对质）→ :84（`turned the skeleton key in the lock`）→ :87（floorboard creak）→ :93（jasmine/perfume）→ :96 `"Hello?" I whispered.` → :99（叹息）。
8. 钥匙来源可回溯 ✓ `text/ch05_chapter_four.txt:201` `If you want extra privacy, there’s a key in your lock.`——md:10「那把钥匙」不是凭空，只是形状归属要改（C-07-3）。
9. :21 男孩的两项给定（tan suit／two or three years younger than Mama／dull-eyed）＋「她几乎没注意他」✓，md 词表收录但未引申身份 ✓（正确：本章不给身份）。

## 不许裁决（本章内）

- 门外是否有者／气味属谁／叹息是否幻听：:93、:96、:99 三条全部未决，且本项目对本书「超自然是否真实发生」一律不裁决。
- 墙句是谁在何时写下、共几条（原文只给四条可见＋「各种角落、一遍又一遍」，无总数）：不得写成「全部」或给出条数结论。
- 棕褐色西装男孩的身份（ch07 唯一出现，无名、无关系）：不得指认为 Leon／任何家族成员。
- 「She’s in us / She’s in you」中「she」指谁：:78 是叙述者自己的断定（`certainly Gazzie was the “she” in question`），不得升为文本事实，也不得指认为 Ida／鳄鱼灵。
- Mama 离开 Greer House 的原因：:78 只说 `Something bad had driven Mama from Greer House`，不得补写为何。
