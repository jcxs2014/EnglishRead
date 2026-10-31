# ch04 对账（R1 素读 ↔ `ch04 chapter three.md`）

素读：`review/ch04/1-suread.json`（8 条，8/8 命中）。md：`ch04 chapter three.md`（12 块）。

## 漏（素读有、md 无）

| 素读事实 | 原文 | 处置 |
|---|---|---|
| 高年级宿舍在三、四楼，Head Girl 住塔楼单间 | `text/ch04_chapter_three.txt:4` `The senior dormitories are a bit further along, on the third and fourth floors` | 取舍：与块 1 同段，块 1 只取「低年级分寝」那半句；其余属走廊解说，不另立块 |
| 校长说自己教比较宗教课 | `:97` `I take comparative religion classes` | 取舍：与块 6/块 3 同属师生对话，md 未取；无断言依赖 |

## 编（md 有、原文无）

| 位置 | md 写法 | 原文 | 档位 | 处置 |
|---|---|---|---|---|
| 块 2 读者视角提示 | 「她却只当是自己紧张」 | `:19` 只写 `She could almost smell the rotting earth from where she stood`，没有「当作紧张」的心理说明 | 提示 | 改为「她把它当成布景的一部分，没有多问一句」 |

## 错（两边都有、不一致）

| 位置 | 问题 | 证据 | 档位 | 处置 |
|---|---|---|---|---|
| 导航一句话概括 | 「集体向她讨一整周的免作业」 | `:283`–`:289` 只是 **Faith 一人**对 Phil 下指令，其余人 `oddly deferential` 地沉默 | 阻断 | 改「由菲丝一人替全班讨」 |
| 块 2 为什么这样写 | 用「她随即承认观测台改作储藏室」立论，该句在块外 | `:16` `At the moment, storage.` | 阻断 | 已改为只用块内两处措辞立论 |
| 块 5 为什么这样写 | 用「那是一块实心木门」立论，该句在被 `…` 跳过处 | `:82` `It was a solid piece of wood.` | 阻断 | 已改为只用块内 `little savages`/`creatures` 立论 |
| 块 9 为什么这样写 | 用「那是抛光用的宝石粉」这一句立论，该句在块外 | `:241` `that’s jeweller’s rouge` | 阻断 | 已改为只讲块内的家务规矩 |
| 块 12 引语 | 「I never joke」是全章封口，却不在引语内 | `:334` `‘My dear,’ Miss Jagerson said. ‘I never joke.’` | 阻断 | 引语延长到该句（用 `…` 跳过 Phil 的追问） |
| 块 3 读者视角提示 | 「芬自己追问珍本与黑市」——黑市是校长提的 | `:28` `selling them on the black market` | 提示 | 改「她自己补上珍本猜测、又顺口提到黑市」 |

## 假红

- 块 5 的引语跨了 `…`：跳过的是 `The other woman glanced at the door nervously…`——真实存在的三句，不是缝合。
- `quotes.py full` 报 ch04 的 🔶 条目：`/tmp/t3_ellipsis.py` 复核 `para_breaks = 0`，epub 内联标签所致，判假红。
