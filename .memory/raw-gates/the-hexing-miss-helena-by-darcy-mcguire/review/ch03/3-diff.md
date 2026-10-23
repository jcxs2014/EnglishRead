# 3-diff.md · ch03《helena calls on cynthia》对账三张单子

审查员：主会话自审（**同会话盲区见 4-verdict.md 末节**）｜章型：对话／审问章（POV 中段切换）
基准：`text/ch03_chapter_3.txt`（346 行，1 基行号）｜底稿：`1-suread.json`（21 事件 / 12 关系 / 6 数字）
R2：`2-machine.json`（`chapter.sh --json` 退出码 0，verdict `ok`）

---

## 一、漏（素读有、md 无）

| # | 素读（原文逐字） | 行 | md | 判定 |
|---|---|---|---|---|
| L1 | `Clio’s cousin had rejected any overture Cynthia made of friendship. Her blatant refusal to accept invitations to tea parties, salons, garden parties, or countless outings to Gunter’s and Rotten Row with Clio and Ellie during the summer season had stung most acutely.` | :41 | 导航只作「社交尴尬」四字带过；引语层未取（该句已作词表 `overture` 的例句） | **不构成阻断**：导航已概括，词表已留原文 |
| L2 | `‘It is mine. I won’t try to deny it. But I haven’t seen it in years. Hubert gave it to me when we were courting. I gave it back several months after we were married. I haven’t seen it since then.’` | :294 | **引语层完全未取**：md 的六块引语按 `:170 → :194 → :222 → :249 → :345` 排列，**跨过了 :294–:333** 整段（辛西娅认领项链并说明来历、拉克兰叔叔的心里话、托马斯护妹、Clio「辛西娅连只苍蝇都舍不得伤害」、辛西娅自述婚姻疏离） | **提示**（分析层覆盖偏薄）：导航「当面顶回海伦娜」已点到该回合，故事线不缺；故不判阻断。但 `:294` 与 `:333` 是本章嫌疑人唯一的正面辩解，读者只从导航与一句话总结看不到 |
| L3 | `Is it because you killed the bastard?`（拉克兰叔叔心里话）＋`‘You can’t think Cynthia killed her husband just because of a locket…’` | :303、:315 | md 未取 | **不构成阻断**：与 L2 同段，导航已含「指控—辩解」轮廓 |

**结论：关键转折 0 漏；分析层覆盖偏薄 1 处（L2）。**

---

## 二、编（md 有、原文无）

| # | md 写的 | 原文 | 判定 |
|---|---|---|---|
| C1 | 导航·人物弧线：「辛西娅从自责失礼的女主人，走到**用粗话命令管家**、当面顶回海伦娜」 | 命令管家时她极其客气：`:140` `‘Hodges, have Cook make a tray of sandwiches.’`、`:143` `‘Of course, madame. And the, err, the brandy?’`、`:146` `Cynthia rolled her eyes. ‘Yes. Fine. Brandy as well, if you must. Thank you.’`；管家 `:149` `The butler bowed, his cheeks flushing slightly as he shut the door behind him.` **已经退场**；粗话出现在其后的 `:152` `‘Now, will someone please tell me what the bloody hell is going on here?’`，且是对满屋人说的 | **阻断**（动作/说话人归属错：粗话不在命令管家的场景里，也不是对管家说的） |

---

## 三、错（两边都有但不一致）

| # | md 写的 | 原文 | 判定 |
|---|---|---|---|
| E1 | 一句话总结：「本想用一枚沾血的吊坠**撬开对方的嘴**，却发现自己的读心术在辛西娅身上彻底失灵」 | `:258` `She had only pulled out the locket to rattle Cynthia and see if that knocked loose whatever was blocking Helena’s power to read her thoughts. The plan backfired spectacularly.`——**吊坠的用途是摇松封锁、让读心术生效，不是让对方开口** | **提示**（因果/动机归属偏移） |
| E2 | 原句 1·读者视角提示：「读者先看见的是一头**浓烈的红发**」 | 同块中文理解写的是「焦赭、铜红，还带一点绯」＝`:35` `burnt umber, copper, a hint of crimson`；同一块内前后口径不一 | **提示**（措辞；与本块中文理解自相矛盾） |

---

## 四、机器层与本轮人判的分工

- `2-machine.json`：`segment_miss=0`、`quote_long=0`、`keyword_bad=0`、`struct_bad=0`、`cjk_low=0`、`hole=0`、`block_count=0`（ch03 9 块 / 2,938 词，`block_target:[5,9]`）。
- 独立复核（探针在 `/tmp`，不入库）：
  - 引语逐字：9/9 命中原文；**原句 7 含 `…`（`heard… nothing.`），两侧各自命中原文**，属原文自带的省略号，非拼接。
  - 词表例句逐字：22/22 命中；词头在例句内 22/22。
- 机器层查不出的是 C1（动作归属）、E1/E2（因果与措辞）、L2（覆盖偏薄）——**全在中文分析层**。
