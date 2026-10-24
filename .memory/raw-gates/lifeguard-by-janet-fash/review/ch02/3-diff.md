# ch02 · R3 对账（漏 / 编 / 错）

- 对账基准：`1-suread.json`（R1 素读，独立代理，只读 `text/`）+ 本章 md + `text/ch02_*.txt`
- 逐字底稿：`2-machine.json`（R2 第二实现，重跑后 verdict=ok，13 块查无 0）
- 章名：Chapter Two: 1980

## 单子一：漏（素读有、md 无）

| R1 事实 | 判定 | 理由 / 落点 |
|---|---|---|
| R1「哥哥 Alex 嫌两个妹妹挤进他的棚，整个夏天不说话」 | 非漏 | 属支线人物关系，不是本章转折（本章转折＝自愿下水救人→被推责→Helen 那一拳）；md 块 4/5 已覆盖中尉罚站这条主线 |

## 单子二：编（md 有、原文无）

| md 位置 | 断言 | 判定 | 依据 |
|---|---|---|---|
| （无） | — | 自建 §0.2 严口径扫描：分析层专名若整章原文都没有 ⇒ 0 处（凭空生词 0） |

## 单子三：错（两边都有但不一致）

| 位置 | md 写法 | 原文 | 判定 |
|---|---|---|---|
| 原句 3 中文理解写「她想 Helen 既然爱游泳」，本块引语只说 “she”，人名不在本块引语内 | §0.2 阻断 | text/ch02_chapter_two_1980.txt:  引语「It wasn’t until we started playing rugby…Just like Barbara taught me, I told her to  | 已修：中文理解「Helen」→「对方」；为什么这样写「我教妹妹」→「我让她去选」 |
| 原句 9 中文理解写「Freddie 站在回岗亭的路上」，本块引语从 “He noticed neither of us | §0.2 阻断 | text/ch02_chapter_two_1980.txt:  原文「As we were walking back to the shack, Freddie, the borough coordinator, was standing | 已修：引语向前扩一句（47→64 词，仍在 30–70 词内，且仍是原文连续一段） |

## 本章结论

- 漏：1 条（其中阻断 0）
- 编：0 条
- 错：2 条（阻断 2）
- 本章阻断合计：**2**
