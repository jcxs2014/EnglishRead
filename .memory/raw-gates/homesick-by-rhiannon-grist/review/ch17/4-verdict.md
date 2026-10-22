# ch17 4-verdict

- 文件：`ch17 no blood no bodies.md`
- 结论：**阻断 2 / 提示 5**

## 阻断

### B1 导航 + 一句话总结：把“和从前一样封着”写成“比从前更死”（程度反）

- 位置：导航·Tropes 兑现/反转（行16「门封得比从前更死」）、一句话总结（行107「一扇比从前封得更死的门」）
- 原文证据：`text/ch17_chapter_17.txt:80` 「The plaster looked and felt as sealed as ever.」
  - 取证：`/usr/bin/grep -n 'as sealed as ever' text/ch17_chapter_17.txt` → `80:...The plaster looked and felt as sealed as ever.`（退出码 0）
  - 同段紧接「It was as if it had been cemented shut, almost part of the brickwork.」＝ 封得像砌进砖里，是**依旧**的封闭状态，不是“比从前更死”。
- 影响：md 把“无变化”升级成“更封闭”，等于替原文加了一层超自然推进；本章的要点恰是“门没有任何变化，所以要么我没砍到人，要么发生了别的事”。
- 建议改为：「那扇门依旧封得和搬进来时一样，水泥似的砌在砖里，看不出昨夜被开过的痕迹」

### B2 “最后这十四个词”：词数无据（实为 11 词）

- 位置：原句4 · 为什么这样写（行60「整章的重量就压在最后这十四个词上」）
- 原文证据：`text/ch17_chapter_17.txt:125` 「Or maybe she’s lying cold on the floor of her basement.」
  - 取证：`python3 -c "print(len('Or maybe she’s lying cold on the floor of her basement.'.split()))"` → `11`（把 she’s 拆成两词也只有 12）
- 影响：计数断言无据，且 14 与任何切分都不符；同类计数在门禁里属“未判”，但读者可数。
- 建议改为：「整章的重量就压在最后这一句上」（去掉数字，或写“十一个词”）

## 提示

1. **原句4 跨自然段拼接**（行54）：`Maybe she was just hungover in bed…` 出自 `text:122`，`Or maybe she’s lying cold…` 出自 `text:125`，两者之间隔一整段（`text:123-124` 为空行）。建议中间加「……」或拆成两句引，避免合成一段连续引语。
2. **叙事手法描述与原文不符**（行20「三段一停的短句节奏（记得／不记得／然后呢）」）：`text:8` 是三个并列的「I remembered…I remembered…I remembered…, and then darkness.」，没有“不记得”那一段；"不记得"在 `text:5`（开篇）。建议改为「三段『I remembered』＋一句『and then darkness』的收束」。
3. **“不属于这个年代的针”是原文未言的推测**（行16）：`text:92` 只说「Maybe it had belonged to the leatherworker Fergus talked about.」——可能属于 Fergus 讲的皮革匠，没有断代。建议改为「一枚不像家常针线盒里那些的粗弯针，可能正是 Fergus 说的皮革匠的」。
4. **“宽慰从第一段就开始”位置偏移**（行14）：原文的 relief 出现在下楼查验之后（`text:98` 「Relief flooded my body」），开篇几段是自我开脱（`text:23-26`），不是宽慰。建议改为「她的开脱从第一段就开始，宽慰要到地下室查完才来，最后一句又被自己推翻」。
5. **导航未点明“她以为昨夜砍中的是邻居”**（行12/18）：`text:5` 与 `text:53`（「She’d fallen through the door and I’d left her.」）都指向同一个对象；md 只说“没有查看邻居”，读者难以还原“她以为一斧劈在邻居身上”。建议在“一句话概括”里补明对象（属漏，非转折变形，故列提示）。

## R4 三问

1. **谁做的**：本章不给答案，md 也守住了不可靠叙述（行16「读者和主角一样不知道昨晚发生了什么」）——**与原文一致，不阻断**。原文自身只给两种互斥解释：她砍了人（`text:26` 辩护叙事、`text:53` 弃之不顾）／她砍了空气（`text:101` 「No monsters. No blood. No bodies.」）。
2. **关系/谁欠谁**：md 未做“谁欠谁”的断言；本章的关系事实是“她把邻居丢在地上过夜、没报警没叫救护车”（`text:53`），md 行18 如实落在“她没做的两件事”上，**无倒置**。
3. **数字与死因**：本章无死亡。数字仅 B2 一处（词数），已阻断。“没有尸体”有据（`text:101` 「No blood. No bodies.」）；斧刃无血、指上黑灰可来自柴屑或锅炉油（`text:74`），md 行12「斧刃上只有一点黑灰」属可接受的压缩转述。

## 已核实为正确（下一轮不要改坏）

- 原句1 逐字：`text:26` 「I could see my defence. I was home, chopping wood, someone surprised me in the dark. I startled. I swung.」
- 原句2 逐字：`text:68` 三句相连，`still sealed over` 译“仍然封着”正确（行36）。
- 原句3 逐字：`text:92`，`tinsel-like` / `robustness` / `sew leather` 译法无偏移。
- 结尾“冷冷地躺”对 `lying cold`，未加“死了”之类原文没有的判定——**保留这种克制**。
- 词汇表例句均可在 `text/` 命中（juddered/viscera/haphazardly/gore/residue/glint/pinprick/cemented 等）。
- H1 形态 `# 17. Chapter Seventeen` 与 ch18 一致（`ch18 the begonias and the unknocked door.md:8`）。
