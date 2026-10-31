# ch02 对账（R1 素读 ↔ `ch02 chapter one.md`）

素读：`review/ch02/1-suread.json`（8 条，8/8 命中）。md：`ch02 chapter one.md`（10 块）。

## 漏（素读有、md 无）

| 素读事实 | 原文 | 处置 |
|---|---|---|
| 司机把车停在校门外，让她自己走完最后一段 | `text/ch02_chapter_one.txt:13` `You can walk from here.` | 取舍：不单独立块；导航「一路说明」与块 3/4 已覆盖司机对学校的告警口吻，此句只交代下车地点 |
| Elizabeth 年龄「十八，或者看着很成熟的十七」 | `:91` `She was clearly eighteen – or a notably mature seventeen` | 取舍：人物弧线只取她的职能与体态，不记年龄；本章无断言依赖此数 |

## 编（md 有、原文无）

无。`quotes.py verbatim --full` 整串取证，10 块引语全部命中，`❌ 全书查无 0`。

## 错（两边都有、不一致）

| 位置 | 问题 | 证据 | 档位 | 处置 |
|---|---|---|---|---|
| 导航一句话概括 | 「被那位 Head Girl 训斥又获礼遇」——她把训斥的对象写成了 Phil | `:94` `We do not trample visiting parents` 是对**冲撞 Phil 的女生群**说的，Phil 是被护住的一方 | 阻断 | 已改「当众训斥冲撞她的女生、随即又对她以礼相待」 |
| 块 6 读者视角提示 | 「而后文没有任何人回答这个问题」是全书级否定断言 | 无法用原文逐字证伪，也不能坐实 | 提示 | 改「本章没有回答这个问题」 |
| 词表 `pointing` | 释义「指向，朝……朝」残缺 | 词形与例句均对，仅释义坏 | 提示 | 改「指向；朝向」 |

## 假红

- 块 7 引语跨两次话轮（`We do not…trample visiting parents`）——原文本身就是被叙述打断的一句，引语内保留了 `the girl said` 的插入语 ⇒ 属原貌，不是跨话轮拼接。
- `quotes.py full` 报 ch02 的 🔶 条目：`/tmp/t3_ellipsis.py` 复核 `para_breaks = 0`，为 epub 内联标签，判假红不修。
