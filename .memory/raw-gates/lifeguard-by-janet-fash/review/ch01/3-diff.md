# ch01 · R3 对账（漏 / 编 / 错）

- 对账基准：`1-suread.json`（R1 素读，独立代理，只读 `text/`）+ 本章 md + `text/ch01_*.txt`
- 逐字底稿：`2-machine.json`（R2 第二实现，重跑后 verdict=ok，15 块查无 0）
- 章名：Chapter One: 1974

## 单子一：漏（素读有、md 无）

| R1 事实 | 判定 | 理由 / 落点 |
|---|---|---|
| R1「Helen 递毛巾给 Barbara」「Barbara 把 Peter 的衣服塞进马桶」 | 非漏 | 同一场景已由原句 2（Peter 追 Barbara 扒泳衣）与原句 4（母亲那句话）承载；后续动作属细节 |

## 单子二：编（md 有、原文无）

| md 位置 | 断言 | 判定 | 依据 |
|---|---|---|---|
| （无） | — | 自建 §0.2 严口径扫描：分析层专名若整章原文都没有 ⇒ 0 处（凭空生词 0） |

## 单子三：错（两边都有但不一致）

| 位置 | md 写法 | 原文 | 判定 |
|---|---|---|---|
| 原句 3 中文理解把「Helen」写进分析层，而该块引语只说 “she”，人名不在本块引语内 | §0.2 阻断：分析里出现的每个人名/动作/关系，都必须在这段引语里 | text/ch01_chapter_one_1974.txt:  引语「It wasn’t until we started playing rugby…Just like Barbara taught me, I told her to  | 已修：中文理解改用「对方」，「我教妹妹」改「我让她去选」 |
| 中文理解写「在 Sandy Hook，表姐 Patricia…」——Sandy Hook 不在本块引语内 | 提示型（地点类，非人名/动作/关系；本章原文确有该地点） | text/ch01_chapter_one_1974.txt:  「…there were two beaches there: the bay…; and Sandy Hook, just over the bridge, where t | 只记不改 |

## 本章结论

- 漏：1 条（其中阻断 0）
- 编：0 条
- 错：2 条（阻断 2）
- 本章阻断合计：**2**
