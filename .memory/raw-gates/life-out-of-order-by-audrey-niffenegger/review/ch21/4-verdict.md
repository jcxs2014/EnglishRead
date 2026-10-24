# ch21 Rebecka Charles — 判定表

机器层：`bash scripts/chapter.sh ".../ch21 rebecka charles.md" --json` → **rc=0**，verdict=ok，
块数 8（本书中位 6，限 2–15）、引语段 8（8/8 `ok:true`，查无 0）、空引号 0、子项缺 0、关键词坏 0、CJK 低 0、2613 词。
**机器 rc=0，人判 1 处阻断。**

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 引语逐字 | `2-machine.json` quotes 8 段全 `ok:true`（pos 669 / 1093 / 1338 / 1810 / 2847 / 4652 / 5966 / 11445） | 通过 | 假红（无问题） |
| 「守着 Henry 的骨灰」发生在画廊 | `text/ch21_rebecka_charles.txt:39` "Henry’s ashes are in a minimalist Japanese urn which sits on a small red table near the entrance to my studio." | 骨灰在画室门口；Ando Gallery 里只有长椅与屏风，md:132 把两处并成一景 | **阻断** |
| 介绍前只见了两面 | `text/ch21_rebecka_charles.txt:50`（12-10 同坐长椅）、`:74`（12-17 同坐长椅）、`:108`（3-18 衣帽间擦肩，"I’m standing near the coat check room … when she comes in"） | 三面；md:13"两次偶遇"少算衣帽间那次 | 提示 |
| 号码是手机发送 | `text/ch21_rebecka_charles.txt:343` "Here," she says, thumb-typing much faster than I ever could. "I’m sending you Beck’s number." | md:11"塞给她号码" | 提示 |
| 短引语块（23 词）是否该改 | `text/ch21_rebecka_charles.txt:156` "“Here I am,” I reply. I take her hand and feel a future fall into place. Does she feel it, too?"；上句 `:152` "“Oh, there you are,” she says" | 引语内已含本章最重的句子，**不判违规**；但块内中文把首句解成"回答"而对象在引语外，建议并入上句或补一句提示 | 提示 |
| Beck 是黑人女性 | `text/ch21_rebecka_charles.txt:95` "she has dark eyes, heavy brows, a small tilted nose, a wide mouth; she’s Black." | 原句 5 引语含此句，md:61 的中文理解整句跳过 | 提示 |
| 午餐桌的两种失去 | `text/ch21_rebecka_charles.txt:218` "My husband is lost."；`:268` "I am—waiting."；`:250` "I’m just imitating my own work." | md 只有导航一句概括，8 块中无一块落在午餐前段 | 提示 |
| 两个孤独（近里尔克） | `text/ch21_rebecka_charles.txt:352` "Two solitudes that greet each other, and have coffee, and all that."；`:357` "I smile at the almost-Rilke quote." | 原句 8 引语与中文都止于 "Make stuff happen"，未收 | 提示 |
| 离婚 | `text/ch21_rebecka_charles.txt:321` "She’s going through a messy divorce." | md 全文未提 | 提示 |
| 形态：H1 「21. Rebecka Charles」、导航 5 项、四子项齐、8 块 | `2-machine.json` form 全绿（h1_shape_ok true、nav_count 5、subitems_modal 四项） | 通过 | 假红（无问题） |

## 报数（四组）

- **逐字**：8/8 通过，0 失败（含 23 词短块）。
- **对应**：8 块全通过；1 块（原句 6）附"引语偏短"提示，不判违规。
- **形态**：全绿（8 块 / 2613 词 / block_range 3–10）。
- **断言**：11 条断言，4 通过、**1 阻断**、6 提示。

**本章 rc=0，阻断只有一处（骨灰位置），一句话即可改完。**

**改法**：md:132 改为「Clare 一再回到芝加哥艺术学院那间昏暗的日本画廊，守着 Henry 留下的一句说不出口的话」，或保留"骨灰"但改成「她守着画室门口那只骨灰瓮」（`text/ch21_rebecka_charles.txt:39`）。

## 已核实为正确（防下一轮误修）

1. `text/ch21_rebecka_charles.txt:18` "Thursday, December 10, 2009 (Clare is 38, Beck is 33)" —— 本章跨 2009-12 到 2010-03；md 未写具体年月不算错（缩写体例允许），**不要**据此判漏。
2. `text/ch21_rebecka_charles.txt:144` "Rebecka Charles, meet Clare DeTamble." —— 全名 Rebecka Charles，昵称 Beck；md 两处都对，勿统一成"Rebecca"（原文是 **Rebecka**，无 c）。
3. `text/ch21_rebecka_charles.txt:152/:156` —— 衣帽间那次是 **Clare 先说** "Oh, there you are"，介绍那次是 **Beck 先说**；md:11「这句错位的对答在几天后的正式介绍里被说回来」**方向正确**，勿改成"Clare 又说了一遍"。
4. `text/ch21_rebecka_charles.txt:178` "the paintings that were stolen from the Gardner Museum in 1990" —— 加德纳失窃案是 1990 年；md:81 未误写成 1991。
5. `text/ch21_rebecka_charles.txt:187` "My cat Ida B, the one who died right before I came to Chicago" —— 猫叫 Ida B（不是"Ida"）；md 未收此块，若补写勿简写成 Ida。
6. `text/ch21_rebecka_charles.txt:213` "I lost my husband a few years ago. I mean, I didn’t lose him; he died." —— Clare 的丈夫是**死**，Beck 的丈夫是**lost**；md:11「丈夫也『lost』」用法正确，勿把 Henry 写成"失踪"。
7. `text/ch21_rebecka_charles.txt:39` 与 `:45` —— "At first I was immobilized by grief." 是她守丧初期每天来此哭泣；不是 Beck 的处境，md 未误植。
8. `text/ch21_rebecka_charles.txt:366` "Hey, it’s Clare. How are you?" / "Not too bad. I have an almond croissant and an espresso and it’s a pretty day." —— 短信内容与"三分钟后"的间隔；md:132"次日一条短信换来一句『还不错』"准确。
