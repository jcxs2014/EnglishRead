# ch02 对账（R3）

素读：`1-suread.json`（7 条，全部带 `text/ch02_introduction.txt:行` + 逐字 + 字符区间，子代理已脚本校验 `count==1`）。
机器：`2-machine.json`（rc=0，10 块，引语 10 段全 ok，空引号 0，子项齐全，中文密度合格）。
md 233 行，10 块 + 词汇 25 条。原文 22,340 字符（去空白）/ 4,178 词。

## 一、漏（素读有、md 无）

无阻断。逐条比过素读 7 条：

| 素读事实 | md 落点 |
|---|---|
| 定义 + 六项文化突变 | 概览 L18、结构列表 5、核心论点 L46 |
| 犬形联想约四千年、狗脸狗头 | 概览 L18、结构列表 6 |
| 约公元前 2300–1800 年「旧时期」+ 拉玛什图至少两千年 | 结构列表 12 |
| 旧期之末父权神学政治凝结 + 提亚马特之死＝第一次突变 | 结构列表 13 |
| 中世纪与拉玛什图/Lamia/Lilith 共享核心特征 | 结构列表 16 |
| 乔丹·彼得森把女性＝混乱、男性＝秩序 | 结构列表 15、证据链 L55、可质疑处 L64 |
| 二十/二十一世纪之交电影把她复活为复仇者与女英雄 | 结构列表 19、块 10 |

## 二、编（md 有、原文无）

无。

**特别核过、不算编的一条**：md:33「旧巴比伦时期约公元前 2300 至 1800 年」——原文 `text/ch02_introduction.txt` 作「In **Old Period** Mesopotamia, from about **2300 BCE to 1800 BCE**」，年份与区间逐字相符；「旧巴比伦」是对 `Old Period` 的补全，不是自造。同理 md:34「旧巴比伦末期」＝「toward the end of the Old Period」。

## 三、错（两边都有但不一致）

### 1. 【阻断】核心论点把「父权最惧怕的」写成「女性最惧怕的」——施受反转

- 原文 `text/ch02_introduction.txt`：`This book tells how Patriarchy has needed—for literally thousands of years—to embody in monstrous form **the things about women that it has most desperately feared**: their sexuality, their reproductive power, and their voice.`
- md:49：「父权必须把**女性最惧怕的东西**——性、生育力与声音——化为怪物形态」
- 判断：原文的主语是父权（`it has most desperately feared`），宾语是「关于女性的那些东西」；md 把「惧」的主体换成了女性，等于说「女性害怕自己的性与生育力」。同句词汇表 `lexical talisman` 条所引原文与全书其余各处（ch01 四项恐惧、ch06「父权恐惧的是女性的力量」）都站在父权一侧，此处是孤例反转。
- 改法：`化为怪物形态的是父权最惧怕的、关于女性的那些东西——性、生育力与声音`。

### 2. 【阻断】核心术语「怪物女性」与全书「怪物母狗」不一致（8 处）

- 原文（`text/ch02_introduction.txt`）：`I will call this trope the Monstrous Bitch.` / `What do I mean by calling her that—a bitch? Why use that word? Well, first, I want to highlight and defamiliarize the rampant misogyny…`
- md 侧把 `Monstrous Bitch` 译作「怪物女性」：
  - `ch02 introduction.md:14`（章节定位「怪物女性的特征定义」）
  - `:37`（结构列表 16「怪物女性以性激进…」）
  - `:57`（证据链「怪物女性的四项特征」）
  - `:119`（原句 5 中文理解「数千年来，怪物女性被恶魔化」）
  - `:131`（原句 6 中文理解「杀死一位格外重要的怪物女性——海之女神提亚马特」）
  - `:155`（原句 8 中文理解「怪物女性不再是超自然」）
  - `:167`（原句 9 中文理解「怪物女性挣脱了父权的控制」）
  - 另 `00_金句精选.md:32`（第 ③ 条标题「怪物女性反咬造她的手」）与 `:36`（`**中文**` 正文）
- 全书对照：`怪物母狗` 在 ch03–ch13 与总览三篇共出现 385 次，`怪物女性` 只出现在 ch02（8 次）与 `00_金句精选.md`（2 次）。
- 判断：作者用 `bitch` 是**故意保留污名并加以 defamiliarize**（原文紧接着就说 `What do I mean by calling her that—a bitch? Why use that word?`），译成「怪物女性」把污名抹平，且与其余 12 章术语断裂。

### 3. 【提示】同一结构列表内「古巴比伦」与「旧巴比伦」并用

- `ch02 introduction.md:33`：「12. **古巴比伦的起点**：旧巴比伦时期约公元前 2300 至 1800 年…」——标题用「古巴比伦」、正文用「旧巴比伦」，原文只有一个 `Old Period`；md 内部两种叫法指同一段。

### 4. 【提示】「罗马的崛起」丢了 `Romanitas`

- 原文两处列举：`the rise of Romanitas`（`text/ch02_introduction.txt`，`these last six` 之后那句）与 `the ascendency of the Roman Empire`（`these last six` 那句本身）。
- md:18 取「罗马的崛起」，覆盖了后一句，但没体现 `Romanitas`（罗马性/罗马精神）这层意思。因原文自己两处措辞不同，判提示。

## 四、本文件读过的候选行

`assertion_scan.py` 对 ch02 报出的行全部人读（①相对章号、②绝对断言、③数字、④亲属、⑤方向）；另把 `1-suread.json` 7 条逐条回原文比对，并对 `旧时期/2300/1800/two thousand/2022/Dobbs/traditionally female dominated/these last six` 八个关键串做了逐串定位与上下文打印（见 `2-machine.json` 之外的 `/tmp` 探针输出，未落 raw-gates）。
