# R3 对账 · ch15（R1 素读 8 条 vs md 10 块→修复后 11 块）

## 漏（素读有、md 无）

| R1 # | 事实 | 判定 | 处置 |
|---|---|---|---|
| R1#3 后半 | 父亲拒绝跨罢工纠察线的原话（"Dammit to hell, Maddy. I can't cross the picket line."）——他的道德支点 | **阻断（漏）** | **已同步修复**：插入新块 原句5（10 词，逐字命中 text:52 段），后续块顺延为 6–11；chapter.sh rc=0，commit 4910d1a90 |
| R1#7 | 汗屋主持者 Chibenashi 的身份（老同学的表亲、Horse Lake 来访） | **提示（不修）** | 导航「一句话概括」与「人物弧线」均已点名「汗屋导师 Chibenashi」，其吻别场景由块10 逐字覆盖；籍贯/亲戚细节属人物说明 |

**其余 R1#1/2/4/5/6/8 全部有块覆盖**（四件大事→块1、摔伤→块2、烟雾信号→块3、神之情人→块6、圣灰星期三→块8/9、通讯/袜子→块11）。

## 编（md 有、原文无）

- 导航「Maddy / 《人物》杂志 / AIM」← text:7 段 ✓
- 块2「boots over noggin」← 逐字 ✓
- 块6「众神的情人」← "She was a god whore" ✓
- 块8「额头、鼻子、下巴和胸口」← "her forehead, her nose, her chin, and her chest" ✓
- 块11「Rez Resistance newsletter」← 逐字 ✓

**编 0 条。**

## 错（两边都有但不一致）

- 施事：块2 "her eighty-two-year-old dad tumbled down the basement stairs"——摔落者=父亲 ✓；"Hadn't she contacted a contractor"——联系承包商者=Maddy ✓。
- 施事：块5（新）"I can't cross the picket line"——拒绝者=父亲 ✓。
- 施事：块8 "caused graceful Father Reilly to spill ashes"——致洒者=Maddy（fumbled）、洒灰者=Reilly，md「害得优雅的 Reilly 神父把圣灰洒了」方向正确 ✓。
- 施事：块10 "he broke their routine…kissed her"——施动=Chibenashi、受事=Maddy ✓。
- R1#2 骨盆伤（broken pelvis）在块2 中文理解未出现但在导航「一句话概括」有「摔下地下室楼梯骨折」——骨折与 pelvis 一致（text:58 段 "The orthopedic surgeon was able to realign the fracture"）✓。

**错 0 条。**
