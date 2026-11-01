# T1 自检：the-splintered-sun-by-tad-williams

抽样章（56 章 >40 ⇒ 1/5、至少 10 章；首末必含、余等距取 5）：ch01 / ch06 / ch11 / ch16 / ch21 / ch26 / ch31 / ch36 / ch41 / ch46 / ch51 / ch56（12 章）。

## 查出并已就地修（4 条，均属总览层）

1. `00_概述.md:14` 改前「在 Hernystir 边境的客栈里…从二楼阳台坠下」→ 改后「在首都 Hernysadharc 的客栈里…在顶层房间外的阳台上摊牌（声音大到足以惊醒客人），随后从那阳台坠下」。依据：ch01 正文 `balcony outside the top-floor room, which protruded some twenty cubits above the cobbled courtyard` 与 `loud enough that the inn's guests must be waking up`；ch01 精读导航亦作「剧团回到首都 Hernysadharc 待夏」。「边境」「二楼」两处均无原文支撑。
2. `00_概述.md:14` 改前「几十里外的 Garnerhouse」→ 改后「同一座城里，另一头的 Garnerhouse Quay」。依据：ch02 正文 `Garnerhouse Quay, one of the capital’s least stylish neighborhoods`（与 Salt Hill 同属首都 Hernysadharc，不是「几十里外」）。
3. `00_概述.md:74` 改前「对 Flann 说「你欠我」」→ 改后「对 Daley 说「你欠我这次」」。依据：ch18 正文 `“You owe me this, boy,” she said`——是 Vedra 对 Daley 说，不是对 Flann。
4. `00_概述.md:84` 改前「最直白的一次自白来自 Bellicent：「唯一的真奖赏是权力」」→ 改后「来自 Hagan——他对被俘的 Mearna 说…」。依据：ch40 正文该句前有 `should know the answer to that, Lady Mearna… Phelan took all you had`，说话人是审讯 Mearna 的里夫 Hagan；Bellicent 在 ch40 不在场。

## 复核通过、未改（抽验）

- 年龄/数字：ch01 `ten summers`、ch02 `fourteen years`、ch05 `fifteen summers`、ch44 `Six days had passed for Mearna`、ch45 `scarcely a dozen years old` —— 与各章导航/总结写法一致。
- 12 个抽样章 `suread.py` 复用素读清单：12/12 全命中、EXIT=0。
- 总览引语逐条 grep 原文：`00_概述.md` 12/12、`00_金句精选.md` 29/29、`00_情感节点.md` 19/19，共 60/60 全中（改后复验仍全中）。
- assertion_scan 预筛：②192 行全量读、③624 行全量扫（只余修辞计数，无事实断言）、⑥40 行全量读、④⑤各抽 20 行（抽中均为分析性文字，无语义错置）。
- 抽样章人判：12 章导航 5 项 + `## 一句话总结` 全文通读，无跨章断言、无「后文/全书」式断言；`structure.py order` 0 缺陷（4 章不可判定：ch06/09/10/13，均因段内 `…`，已手工验过递增）。

## 结论

- 阻断 0 条；提示级 4 条（已全部就地修复并复验，`gate.sh` EXIT=0）。缺陷密度 4/12 ≈ 0.33（<0.5，不触发加抽；4 条同一成因「总览概括把章级细节写成近似值」，已逐条回源改正）。
- 读了 `t1-candidates.txt` 全部 1116 行中的 ② 192 行 + ③ 624 行 + ⑥ 40 行全量、④⑤ 各 20 行抽读，另读 12 章导航与总结全文、总览三篇全篇。
- **T1 为同会话自检**，不构成异会话验收；异会话复核仍待发起。
