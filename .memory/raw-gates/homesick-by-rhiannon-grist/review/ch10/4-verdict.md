# ch10 4-verdict

- 文件：`ch10 never being perceived.md`
- 结论：**阻断 1 / 提示 2**

## 阻断

**阻断 1（引语频次无据：这句话全书只出现一次）**
- 位置：原句3·读者视角提示"她紧接着说'Always losing myself'（又走神了）。**这句话在全书出现多次**，每次都发生在别人看不见她的时候。"
- 原文证据：`text/ch10_chapter_10.txt:41` "There I go again, I thought. Always losing myself." ——全书仅此一处。检索命令与输出：
  - `/usr/bin/grep -rn -E "lose myself|lost myself|losing myself" text/` → 只有 `text/ch10_chapter_10.txt:41` 与 `text/ch30_chapter_30.txt:38`（"“Sorry, I sort of lost myself there.”"，是另一句话、另一个场景），`echo $?` = 0
  - `/usr/bin/grep -rn -i "always losing" text/` → 只有 `text/ch10_chapter_10.txt:41` 一处，`echo $?` = 0
- 问题：把一个只出现一次的句子写成"全书出现多次"的口头禅，等于替作者虚构了一条贯穿 57 章的主题句；读者照此去别章找，必然找不到，进而怀疑全书的互文标注都不可信。后半句"每次都发生在别人看不见她的时候"也因此失去对象（唯一一次是在独自泡澡，属同义反复而非规律）。
- 建议改为：「她紧接着说"Always losing myself"（又走神了）——这句整本书只在此处出现一次，而它偏偏发生在她独处、没人看得见她的时候；越是没人看，她越容易把自己弄丢。」

## 提示

1. **位置**：导航首句；一句话总结。
   **问题**：原文 `text/ch10_chapter_10.txt:8` 是 "I hadn't brought any **bubble bath** with me"——她没带的是浴液/泡泡浴，不是"浴盐"（bath salts）。正因为没有泡沫，她才看得见水下自己的身体；换成"浴盐"这一因果就断了（浴盐也会让水变浑）。
   **建议**：改为"没带泡泡浴，水面清得能看见整个身体"。

2. **位置**：词汇表 ⭐⭐⭐ 高级·noticeably。
   **问题**：noticeably（明显地）是常用副词，与同表 fastidiously / warped / sulking 不在一个难度档；本章 ⭐ 常用 里已收 surface / soap / taps 这类更基础的词，分级尺度反而更松。
   **建议**：noticeably 移到 ⭐⭐ 进阶，或换成例句里更值得记的搭配 "grown noticeably cold"。

## R4 三问

1. **谁做的**：热水、劈柴、生火都是 **Tamsin 自己**（`:5` "Hot steaming water, courtesy of my hands."）；抬脚检查伤口、决定再下地下室、猜 1a 内部、搓肥皂、出浴，全是她一个人的动作，本章没有第二个人在场。md 未把任何动作派给别人。
2. **关系/谁欠谁**：隔壁 1a 是**女性邻居**（`:26` "I still didn't know her name."，且指明"我跟他/她说过话"时用的是 her），两人已在 ch04 见过面、握过手，本章仍是互不知名；md 全程用"她"、称 1a 为"那半栋房子"，与 ch04 已修正的"同一栋石屋两半"一致。md 提到的"删评论、屏蔽旧友"确属 ch06 的旧同学，不是 1a——归属正确。
3. **数字与死因**：本章除"1a/1b"外**没有任何数字**（无年龄、金额、日期），也**无死亡**；脚伤是刺伤（`:20` "the puncture wound"），已封口、未感染（`:20` "It didn’t look infected, thank God."），md 未把它升级成重伤或死因。"昨天"的时间点有据（`:20` 前后文 "yesterday"，与 ch02 扎脚、ch09 地下室一致）。

## 已核实为正确（下一轮不要改坏）

- 原句 1/2/3 全部逐字：`:8`（never being perceived 整段）、`:20`（pulled at the wound / a tiny sulking mouth / didn’t look infected）、`:38`（warped and elongated / shadow shattered / grown noticeably cold）。
- "capable body / strong body / sore body" 三个短句确在 `:11`/`:14`/`:17` 连续成段，人物弧线"三个短句连排"的判断成立。
- "一处细节也不肯放过"的两处小比喻（"赌气的小嘴"、"泡出硬棱"）均为原文所有（`:20`/`:38`），不是译者的添加。
- 章际呼应"ch06 咖啡店里被人看见的不适"**有据**：`text/ch06_chapter_6.txt:161` "I watched the road outside the window, suddenly feeling eyes on me." 与 `:179` "I saw myself as they must see me."——此处不要按"编细节"改掉，最多把"恐慌"降格为"被注视的不适"。
- "没有事件、只有她在水里想事情"的定性准确：全章 44 行、无对话、无第二人出场。
- 词汇表除 noticeably 一条外，例句均可逐字检得（fastidiously / elongated / bloated / sulking / warped / puffy / wrinkled / infected / hoarder / doily / ripples / foam / daydreaming）。
