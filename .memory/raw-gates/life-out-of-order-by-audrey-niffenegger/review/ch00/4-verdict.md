# ch00 判定表（R5）

机器：`bash scripts/chapter.sh ".../ch00 prologue life out of order.md" --json` → **rc=0**；块数 4；引语段 4（全 ok，segment_miss 0）；空引号 0；查无 0；子项缺 0；关键词 4 行（英文，中文比 0.0，`keyword_bad` 0）；块中位 6 行、区间 3–10；`block_hint` 空。无法判定项：无。

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| md:15「结尾三句都以 I 开头」 | `text/ch00_life_out_of_order.txt:46`「I look back and regret all the lies. I try not to hurt people. **But mostly, I just try not to panic.**」——第三句以 But 开头 | 与原文不符（2/3 以 I 开头） | 提示 |
| md:35「一句比一句短，最后一句最长」 | `text/ch00_life_out_of_order.txt:21`「I have loved time travel and I have wished to be done with it; I’ve seen what it did to my dad.」「He died when I was five.」「Time travel killed him and time travel keeps throwing him back into my life.」→ 词数 22 / 6 / 14 | 与原文不符（第三句长于第二句；最长是第一句） | 提示 |
| md:11「她说自己「同时有两个丈夫」」 | `text/ch00_life_out_of_order.txt:42`「I might look at Zach out in the backyard, mowing our mossy grass」；`:46`「instead of two at once」 | 成立；但 md 全章未出现 Zach / Oliver 两名字（见下行取证） | 假红（事件已进导航） |
| 「Zach / Oliver 在 md 中 0 次」 | 命令：`/usr/bin/grep -nE "Zach|Oliver" "ch00 prologue life out of order.md"` → 无输出，**exit=1**；同命令对 `text/ch00_life_out_of_order.txt` → `42:` 命中，**exit=0** | 事实成立：两个丈夫的姓名未落到 md | 提示 |
| md:13「父亲的时间旅行传给了女儿」 | `text/ch00_life_out_of_order.txt:16`「A few genes have gone wrong in me in just the right way to produce this bad fit with the present」；`:21`「Time travel killed him」 | 原文未明写「父亲→女儿」的遗传链，属推断 | 提示 |

## 计数

- 阻断 0（漏 0 / 编 0 / 错 0）
- 提示 3（形态 2 + 细节 1；「遗传」一条并入形态外的推断提示，已单列）
- 假红 1
- 跳过 0

## 已核实为正确

1. md:11「父亲在她五岁时死去」 ← `text/ch00_life_out_of_order.txt:21`「He died when I was five.」——数字（五岁）逐字对。
2. md:14「她承认自己说谎的方式是「不说全」，而不是编造」 ← `:26`「I don’t lie, but I don’t tell everything, either, if I can help it.」——方向没写反。
3. md:15「中间夹一串分号列举（父亲冻掉的双脚、母亲的闭门不出、母亲的新约会）」 ← `:26`「he lost both his feet to frostbite; she is desolate since you died and almost never leaves the house; Dad is worried about you; Mama is dating someone new but she feels guilty about it」——三条细节全对，且 `by`/`since` 的方向没搞反（是**父亲**冻掉脚、**母亲**闭门不出）。
4. md:35「她没有用「失去」这类词，只说 killed」 ← `:21` 原文确为「Time travel killed him」，无 lost 一词。
5. 词汇 13 条例句全部逐字落在 `text/ch00_life_out_of_order.txt`（`:21`/`:26`/`:27`/`:37`/`:42`/`:46`），无改写。
6. 「两个丈夫」不是 md 编的：`:42` 同段并列 Zach（mowing our mossy grass / my once-and-always husband）与 Oliver（wake up with Oliver beside me in bed）。
