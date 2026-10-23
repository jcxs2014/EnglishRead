# ch38（Chapter Thirty-Seven）R3/R4 差异与取证

## 探针

| 探针 | 结果 |
|---|---|
| v38（词表例句逐字） | 13 行，flagged 0 |
| ap38（直撇号＋backtick span） | ASCII 撇号 2（L13 didn't／L84 doesn't，均引原文）→ C-38-1；span MISS 0 |
| in38（非块内嵌英文） | 未命中 3：`Chapter Thirty-Seven`（模板）、`Tropes`（模板）、`house-bones-Ida`（→F-38-1） |

## 阻断取证

- **C-38-1**：
  - `/usr/bin/grep -n "didn’t warm me\|doesn’t know this" text/ch38_chapter_thirty_seven.txt` → L99 `didn’t`（弯）、L198 `doesn’t`（弯）；md L13/L84 为直撇号。rc=0。

## 定点取证（/usr/bin/grep，text/ch38_chapter_thirty_seven.txt）

- L9 150-pound／beneath Greer House／gloat；L15 Begging a fainting spell／haint；L18 mirror／fervor／collarbone；L21 "I'd only gotten worse."
- L33 Flora／"the birds had already quieted"／anti-itch cream／sketching on the patio／evacuating；L36 "Even Ida let me be, presumably appeased with yesterday's slaughter."
- L42 deviled eggs／Mimosas；L45 "Too many guests carrying delicate crystal glasses"／"suffocating scents of rose perfume and baby powder"／"tips of the petals had already begun to brown"
- L48 Cat One hurricane；L78 "My daughter wasn't one for tradition"＋Mama Beaumont；L99 eel／devil in their hearts；L102 "handed me my third mimosa"
- L132 purple bruise／diagonally／napkin／double take；L144 "Can we go somewhere private?"
- L151 "I'd made myself conspicuous"；L165 "Gazzie climbed five steps…Symbolic and picturesque, in case anyone posted on social media."
- L180 Virginia studying Ida's portrait；L183 "the black water rippled"；L186 "A low hum began in the walls"
- L192 "Dart's a natural…Signed the paperwork this morning."；L198 "Dart doesn't know this…from Beaumont to Greer…show up to court next week"
- L229 "she grasped my arm again. Her fingers were cold, her grip bruising, not unlike Mama's."；L231 "Call me if you need to get out of here."
- L240 Leon's bedroom door；L246 "A sob wrenched forth…teeth scraping my palm"；L252 "I'd gotten everything I wanted. Hadn't I?"

## 查无声明（命令+输出+退出码）

- `/usr/bin/grep -n -i "sign" text/ch38_chapter_thirty_seven.txt`（导航写作期初探用 "signed" 单数全小写）→ 首轮 grep "signed" 无输出 rc=1；改 grep -i 后命中 L192 "Signed the paperwork this morning."（大写 S 句首）——非缺陷，首轮模式大小写问题。
- `/usr/bin/grep -n "house-bones-Ida" text/ch38_chapter_thirty_seven.txt` → 无输出 rc=1（分析层自造标签，见 F-38-1）。
