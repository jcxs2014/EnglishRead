# ch27（Chapter Twenty-Six）三张单子与逐块对应

R1：`review/ch27/1-suread.json`（51 facts / MISS 0，先素读后开 md）。
R2：`review/ch27/2-machine.json`（chapter.sh rc=0，无阻断、无报警）。
探针：v27 词表 16 行 0 旗标；ap27 ASCII 撇号 0、backtick span 0 MISS；in27 内嵌英文未命中 3 处＝模板例外恒 2（`Chapter Twenty-Six`、`Tropes`）＋1 体裁词（`rivals-to-lovers`，rivals-to-lovers trope 通行写法），均判非缺陷。

## 漏

- 导航五项、四块精读、词表 16 行、总结齐备；本章无「整段漏」。
- 提示级：导航未提 Harrison 解安全带/抱她回房/背身等照护细节，属选材取舍，不算漏。

## 编（凭空）

- 查无凭空引语、凭空动作、凭空物种。alligator/tilapia/possum/beetle/maggots 均在原文。

## 错（含对应层）

### C-27-1【阻断·对应·在场者漏写】人物弧线抹掉 Mama 例外，并新造「第一次有了观众」

- 位置：`ch27 a kiss on the cheekbone.md` L13（人物弧线）。
- 原文：text/ch27_chapter_twenty_six.txt L111 — "No one had complimented my artwork in over twenty years. No one besides Mama had seen more than a glimpse of it since she'd pulled me out of school, and she certainly never described it as beautiful."
- 两点错：
  1. 「自打 Mama 把她从学校接出来，二十多年没人看过、没人夸过」——原文明写 **No one besides Mama** had seen：Mama 是例外，被 md 抹掉；且「二十多年」的口径挂在「没人夸」（complimented）上，「退学后没人看」是另一条（more than a glimpse），md 把两条焊成一条。
  2. 「她的画第一次有了观众」——同句反证（Mama 看过，哪怕只是 more than a glimpse）。
- 改前（L13）：
  `- **人物弧线**：Dart 与 Harrison 的关系在本章从对手滑向被照顾者，她承认他身边更安心；她的画第一次有了观众——自打 Mama 把她从学校接出来，二十多年没人看过、没人夸过，如今有人建议送画廊，她开始重新给画定性：depiction，不是 moral failing。她给自己的验证方式仍是同一套：掐进掌心，用痛感确认现实。`
- 改后：
  `- **人物弧线**：Dart 与 Harrison 的关系在本章从对手滑向被照顾者，她承认他身边更安心；她的画二十多年来第一次被夸——自打 Mama 把她从学校接出来，除了 Mama，没人看过它的全貌，也从没人夸过，如今 Harrison 建议送画廊，她开始重新给画定性：depiction，不是 moral failing。她给自己的验证方式仍是同一套：掐进掌心，用痛感确认现实。`
  - 「第一次被夸」与「二十多年」共用同一条原文口径（"No one had complimented my artwork in over twenty years"），自洽；Mama 例外以「看过它的全貌」的反向写法落回原文（Mama 也只是 more than a glimpse）。

### 提示级（只记不改或执行方酌改）

- P-27-1 一句话概括「让她二十多年来第一次面对**来自外面**的 beautiful」——「来自外面」是推断：原文只说二十多年没人夸、Mama 从不称它 beautiful，「Mama 算不算外面」原文未设口径。建议改为「二十多年来第一次有人夸她的画」。位置 L10。
- P-27-2 Tropes「她只能靠掐掌心的痛确认它**真实发生过**」——原文验证对象是 "Was I asleep?"（是否在做梦），「真实发生过」为等义改写，含义无损。位置 L12。
- P-27-3 情感弧线「结尾两句回环又把它整个拖回去」与精读原句 4 的读者提示均把两句回声读成「指向她自己」——原文第二句确实落到 "exactly like Mama talking about me"，判定成立；第一句 "describing a monster" 的宾语是 Gazzie，md 未写错宾语，判正确（此条为「查无误」记录）。

## 逐块对应（R4）

| 块 | 引语逐字 | 中文对应 | 关键词 | 施事/归属/地点/时序 |
|---|---|---|---|---|
| 原句 1（inches/视线） | ✅ 逐字 | ✅ | ✅ 4/4 | ✅ 搜寻答案的主语＝His eyes；时点 After Henri's party 无漂移 |
| 原句 2（pre-party） | ✅ 逐字 | ✅ | ✅ 4/4 | ✅ "I assumed" 免责标记被 md 点名 |
| 原句 3（二十多年） | ✅ 逐字 | ✅ | ✅ 4/4 | ⚠️ 块内中文理解正确（"除了她"）；错在弧线层 → C-27-1 |
| 原句 4（out of time） | ✅ 逐字 | ✅ | ✅ 5/5 | ✅ 掐手心的对象＝Was I asleep?；两句回声顺序 monster→Mama 正确 |

## 词表核对

- 16 行（高级 6／进阶 6／常用 4），例句逐字 0 旗标，词头均在语料中。`Chagrined` 大写词头＝例句句首原形，判正确。
