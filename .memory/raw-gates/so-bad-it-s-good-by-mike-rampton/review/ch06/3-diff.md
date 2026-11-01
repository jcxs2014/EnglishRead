# ch06 Deliciously Terrible Food Jokes 对账（R3）

素读：8 条事实 / 3 条关系 / 3 个数字，只读 `text/ch06_deliciously_terrible_food_jokes.txt`（3,219 字符，40 非空段）。

## 单子一 · 漏

无。素读 8 条事实（chew-chew 火车、Heinz spill the beans、佛系热狗、oysters shellfish、impasta、ambidextrose、cantaloupe、Tortilla/两根香肠/nacho）全部在 10 块或证据链中有位置。正文 31 条 + 奶酪小节 6 条 = 37 条，精读 10 条，取舍已在「结构」栏写明。

## 单子二 · 编

无。10 块引语逐字命中（`:17 :22 :32 :42 :58 :65 :85 :95 :145 :200`）；`They’ve just finished shooting Tortilla: The Movie. That’s a wrap!`（`:95`）与 md 引语完全一致。

## 单子三 · 错

**阻断 1（已修）· 计数**：md「字符数」栏写"正文 31 条"、一句话总结写"本章三十七条"，实测正文 30 条 + 奶酪 6 条 = **36 条**（40 非空段 = 2 标题 + 30 正文 + 2×“Cheese jokes” + 6 奶酪）。
- 改前：`正文 31 条，Cheese jokes 小节 6 条` / `本章三十七条几乎全在词与词的接缝处做手术`
- 改后：`正文 30 条，Cheese jokes 小节 6 条（共 36 条）` / `本章三十六条几乎全在词与词的接缝处做手术`

其余核对无错：`They’ve just finished shooting Tortilla: The Movie. That’s a wrap!`（`:95`）逐字一致；「两根香肠」条（`:145`）大写 "WHO" 是原文强调。

## 结论

阻断 1（计数 37→36，已修）/ 提示 0 / 假红 0。修后 `chapter.sh` rc=0。
