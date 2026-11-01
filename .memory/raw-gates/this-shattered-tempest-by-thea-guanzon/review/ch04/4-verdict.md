# ch04 判定（R4 逐块）

块数 8。

| 块 | 引语起头 | 中文理解 ↔ 引语 | 关键词 | 为什么这样写 | 判定 |
|---|---|---|---|---|---|
| 1 | `The Shadowgate had carved a path` | 一致 | 3/3 | 「总会有人来查」的紧迫读解成立 | ✅ |
| 2 | `Now that Talasyn was beside him` | 一致 | 3/3 | 「战术失误不像他」与 `Such tactical missteps were not like him` 相符 | ✅ |
| 3 | `Gods, he’d even forgotten himself` | 一致 | 3/3 | 三类旁观者反应（装作没看见／得意／阴沉）逐一对应 | ✅ |
| 4 | `Alaric knew that she spoke the truth.` | 一致 | 3/3 | 「不再需要别的证据」对应 `He had needed no further proof` | ✅ |
| 5 | `In the month before the Moonless Dark` | 一致 | 3/3 | 「爽快得反常」的伏笔判断成立 | ✅ |
| 6 | `I realize that it’s an unpleasant subject` | 一致 | 3/3 | 「她不是在请示」读解成立 | ✅ |
| 7 | `It takes a single fire tree thirty years to mature.` | 一致 | 3/3 | 「用数字谈代价」与 `thirty years` 相符 | ❌→已修：补「找幸存者 / 通知龙女王」两道命令（标注为紧随段，不冒充引语） |
| 8 | `She went in search of him` | 一致 | 3/3 | 「恐惧拦住她」对应 `but something had stopped her: fear` | ✅ |

## 施事三问

- **谁做的**：烧不烧旅舍（高提议 / 塔拉辛否决）、派谁回 Iantas（阿拉里克派 Ileis）、谁下令找幸存者（塔拉辛）——三项均与原文一致。
- **谁的**：血清来源（Daya Vaikar 的增幅配置）、萨里曼被偷（父亲手里）——归属正确。
- **谁说的**：块 8 的「乌尔杜佳的罪」是塔拉辛心里的话，md 未误记为台词。

## 判定表

阻断 **1**（L1），已修；提示 **2**（一项记事不改，一项已改）；假红 0；跳过 0。

## 已核实为正确

8 条引语逐字命中；块 5 的「一个月前」、块 7 的「三十年」两处可计数断言已回原文取证；修复后 `chapter.sh` rc=0、0 ⚠️，`gate.sh` rc=0。
