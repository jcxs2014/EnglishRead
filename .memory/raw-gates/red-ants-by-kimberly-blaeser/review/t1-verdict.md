# red-ants T1 同会话自检（2026-10-31）

抽样章号与理由：全书 17 篇，17–40 章档 → 抽 1/4 = ceil(17/4) = **5 章**；首末必含，等距取
**ch01、ch05、ch09、ch13、ch17**（步长 4）。章号在动手前写定，不是读完后挑的。

说明：本书为 short-story-anthologies 体裁，**无总览三篇**（体裁 profile overview=0，用户 2026-09-18 拍板），
故「总览三篇全篇人判」与「改过的事实回灌总览」两项不适用。

## 抽样章素读复验（suread --check 全锚点命中）

| 章 | suread 复验 | 事实回源（抽 3 条 grep） | 引语邻域/说话人 |
|---|---|---|---|
| ch01 | 8/8 ✅ | drowning 判定✓ $15,000 罚款✓ Chief of Pirates✓ | 讣告为叙述者转引✓ |
| ch05 | 8/8 ✅ | five-foot-two✓ X-Acto knife✓ 3:00 a.m.✓ | 「murder」出自 Wally 声部✓ |
| ch09 | 9/9 ✅ | twenty-eight itches✓ Seventeen✓ Just two✓ | 「Just two」为 Aanakwad 担架上说出✓ |
| ch13 | 9/9 ✅ | twenty hours✓ crane clan✓ Harvest Festival✓ | 判决句为法官 Henry Small Oak✓ |
| ch17 | 8/8 ✅ | Vanessa Dundon✓ Hamburg in 2014✓ first-born daughter✓ | 「新脸/声带」为 Claude 台词✓ |

引语邻域：5 章全部引语在生产期经整篇通读 + chapter.sh 逐字（151 块查无 0）；抽说话人归属（对话密集章 ch05/ch09/ch13/ch17）无错置。

## assertion_scan 六类预筛（t1-candidates.txt，合计 247 行）

- ②绝对断言 26 行：**全量读**。其中「唯一/最」类 9 处逐条核：ch05:107「唯一伸手」、ch05:131「唯一质疑」、
  ch08:43「唯一一课」均有原文直接支撑（ONLY LANIE BOTHERED / Was I the only one / the single lesson）；
  其余（ch09「唯一的光源」「最催泪」、ch13「第一次碰撞」等）属评析修辞，按 30-writing 分级**从宽只记不改**。
- ③年龄数字 145 行：**全量读**。全部为引语内数字的中文转写，逐条与原文核对（两年/五岁/十六岁/二十八/
  十三+十四/十七份/十岁/二十四小时/二十小时/五词/二十床对三十五间/82 岁/五小时半/四十年/2014 等）——**0 处不符**。
- ⑥场景方位 2 行：全量读，无方位断言缺陷。
- ⑤方向施受 32 行：全量读（超出抽 20 行要求），无施受错置。
- ④亲属身份 42 行：全量读（超出抽 20 行要求）。Aanakwad–Tyrus 兄弟、Mikwam 母子、Rusty 男友、
  「老人」（ch16 刻意不指认亲属，与原文一致）等亲属关系均与原文相符。

## 缺陷清单（T1 期间新发现）

无新增阻断。生产期已修复的缺陷（均在 T1 前的批次 gate 抓出并已提交修复）：
ch07 块序（原句7/8）、ch09 块序（原句5/6）、ch16 块序（原句4/5）、ch05 引语漏字（couldn’t）、
ch08 关键词（turning→turned small rocks over）、ch12/ch13/ch09/ch17 关键词长度与词形。

缺陷密度 = 0 阻断 ÷ 5 章 < 0.2 → 按判据可停，不再加抽。

## 候选行回读记录

读了 t1-candidates.txt 全部候选行：**247 行 / 17 文件**
（②26 + ③145 + ⑥2 全量；④42、⑤32 因总量小亦全量读，超出「各抽 20 行」的最低要求）。
每条 ③ 类数字均与对应 text/ 原文核对；每条 ② 类「唯一/最」断言按分级处置记录如上。

## 结论

- 机器层：gate.sh **EXIT=0**（20 lane，0 阻断）；corruption_scan FAIL 0；audit_numbers 不符 0；块序缺陷 0。
- 人判层：抽样 5/17 章素读复验全过、事实回源 15/15 命中、候选 247 行全读、新增阻断 0。
- **T1 为同会话自检**，不构成异会话审查通过；T3 深审未做（待用户发起）。
