# ch18 The Anti-Darling — 判定表

机器层：`bash scripts/chapter.sh ".../ch18 the anti-darling.md" --json` → **rc=0**，verdict=ok，
块数 4、引语段 5（0 查无）、空引号 0、关键词坏 0、子项缺 0、CJK 低 0、251 词。

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 引语全部逐字 | `2-machine.json` quotes[0..3] 全部 `ok:true`，pos 231/425/688/762/1050；人工复核 md:19/29/39/49 与 text 一致 | 通过 | 假红（无问题） |
| 全名 Isadora Ida Charles Hardwick | `text/ch18_the_anti_darling.txt:16` "My name is Isadora Ida Charles Hardwick." / md:11 | 一致 | 通过 |
| 姐姐的母亲是 Clare（不是 Beck） | `text/ch18_the_anti_darling.txt:34` "Beck is my mother, Alba is my sister, my sister’s mother is Clare." | 方向正确 | 通过 |
| Lucinda 与她是双向归属 | `text/ch18_the_anti_darling.txt:34` "Lucinda is my darling, and I am hers." / md:31 | 方向正确 | 通过 |
| 记忆宫殿房间数 81,337 | `text/ch18_the_anti_darling.txt:34` "a memory palace with 81,337 rooms" / md:11 八万一千三百三十七 | 数字与位数正确 | 通过 |
| 她住在 Museum of Lost Souls | `text/ch18_the_anti_darling.txt:40` "I live in the Museum of Lost Souls." / md:51 | 一致 | 通过 |
| 母亲说爱她，她追问是否分等级 | `text/ch18_the_anti_darling.txt:40` "Do you love me? Yes, she says, I love you. Does she love me like she loves Clare?" / md:11、md:86 | 一致 | 通过 |
| 四处典故（Wild Thing / walrus / Velveteen Rabbit / book of love） | `text/ch18_the_anti_darling.txt:25、35、40`，md:15 逐一列出 | 一致 | 通过 |
| 「原句 1」引语在 creeping catlike 截断，丢掉 "I am made of electricity and regret." | text:29 该句确在引语之后；md:73 词汇例句保留整句 | 引语选短（未丢事实） | 提示 |
| 「原句 3」引语从 walrus 起，丢掉 gardener/curator | `text/ch18_the_anti_darling.txt:34-35` "I am the gardener. I am the curator. I am the walrus."；md:14 导航已写"园丁、馆长" | 引语选短（导航有落点） | 提示 |
| md:57「She gives and she takes 那句被省略号挡在中间」 | `text/ch18_the_anti_darling.txt:40` 省略号实跨 6 句（She gives… → Who wrote the book of love?） | 跨度描述过窄 | 提示 |
| 形态：H1 `18. The Anti-Darling`、导航 5 条、四子项齐、块中位 6（限 2–15） | `2-machine.json` form: h1_shape_ok=true, nav_count=5, block_median=6.0, block_range=[3,10] | 通过 | 假红（无问题） |

## 报数（四组）

- **逐字**：5/5 通过，0 失败。
- **对应**：4 块，2 通过、2 提示（原句 3 覆盖不全；原句 4 省略跨度过大）。
- **形态**：H1/导航/子项/块数/密度全绿。
- **断言**：13 条断言，10 通过、3 提示、0 阻断。

**本章 rc=0，无阻断。** 提示 3 条（均为"引语选短"，事实未丢；若下一轮要修，优先补原句 4：把 `Yes, she says, I love you` 与 `Does she love me like she loves Clare?` 收进块内，或明确写"省略号跨过母亲回答与三级比较"）。

## 已核实为正确（防下一轮误修）

1. `text/ch18_the_anti_darling.txt:34` "my sister’s mother is Clare" —— 姐姐的母亲是 Clare；不要因为 Beck 是"母亲"就改成 Alba 的母亲是 Beck。
2. `text/ch18_the_anti_darling.txt:34` "Lucinda is my darling, and I am hers." —— and I am hers 是"我也是她的"，不是"她是我的"；md:31 译法正确。
3. `text/ch18_the_anti_darling.txt:34` "81,337 rooms" —— 八万一千三百三十七，md:11 汉字数字正确，勿改成"八万多间"。
4. `text/ch18_the_anti_darling.txt:35` "To be loved is to be changed." —— 原文是"被爱就是被改变"（被动），不是"爱会改变人"。
5. `text/ch18_the_anti_darling.txt:40` "She gives and she takes." —— 原文并列，不是"她给了又拿走"的因果；md:57 的"给的同时也拿走"读法成立。
6. 全章无日期抬头、无场景，只有 Isadora 一个声音 —— 与 `text/ch18_the_anti_darling.txt:12-46` 完全一致，md:11"全章没有日期抬头，也没有场景"正确。
