# 4-verdict.md · 《The Hexing Miss Helena》ch02 审查判定（深审 R0–R5）

审查员：主会话自审（**同会话盲区见文末**）｜章型：建立章（接首章现场）｜档位：**深审**（2026-10-23 用户指令「继续执行深审 R0–R5 全章」）
底稿：`1-suread.json`（R1 先素读，14 事件 / 9 关系 / 6 数字）→ `2-machine.json`（R2）→ `3-diff.md`（R3）→ 本表（R4 逐块 ＋ R5）
源：`text/ch02_chapter_2.txt`（269 行）｜受审：`ch02 the dead marquess.md`（6 块 / 词表 22 条）

---

## 一、四组计数

| 组 | 计数 | 明细 |
|---|---|---|
| **逐字** | **引语 6 / 6 相符，0 错** | `2-machine.json`：`segment_miss=0`、`quote_long=0`；本轮独立探针再验 6/6 命中原文，**无 `…`、无跨段拼接**；词表 **22 / 22** 例句逐字回源命中（本书用 `## 本章词汇`，`check_vocab.py` 默认只扫 `## 词汇` ⇒ 该层**门禁盲区**，本轮自建探针补验），且 22/22 词头出现在例句内 |
| **对应** | **6 块：5 块对应，1 块越界（提示）** | R4 三问（动词主语／受事／归属方向）逐块核对；原句 1–4、6 的中文分析全部落在引语内；**原句 5 的读者视角提示引用了引语外的 `:125`**（E3）。密度不足 0 处 |
| **形态** | **4 / 4 符合，0 偏离** | H1 `# 02. Chapter Two` ✓｜导航 **5 项** ✓｜子项 **中文理解／关键词／为什么这样写／读者视角提示** 4 项一致 ✓｜块数 **6**，落在本书区间 **6–13**（众数 10）内，取到下限；`block_count=0`、`struct_bad=0` |
| **断言** | **共核 14 条：相符 10 ／ 提示 3 ／ 阻断 1 ／ 跳过 0** | 阻断 1（C1）＋提示 3（E1、E2、E3） |

**阻断型条数 = 1。**

---

## 二、判定表（断言 | 证据 | 结论 | 档位）

| # | 断言 | 证据（`text/ch02_chapter_2.txt:行`） | 结论 | 档位 |
|---|---|---|---|---|
| C1 | 导航·情感弧线位置：「开头还有**使魔与表亲之间的玩笑**」 | `:38` `Hamlet, her familiar and constant companion, twitched his fluffy copper tail…`；`:44` `He didn’t appreciate the mess the marquess left when he departed. That is, if Lord Hubert Burrows had actually departed.`；Clio 首次出现于 `:47` `Helena watched carefully as Clio Blair crouched…`；与使魔有关的玩笑另在 `:173`/`:176`（Sir Robin 对海伦娜）与 `:260` `‘Murderer!’ Sir Robin ruffled his feathers at Hamlet, who yipped his reply.` | 开头只有**海伦娜与其使魔**的互动，冷幽默（`departed`）出自海伦娜本人；**不存在「使魔与表亲之间的玩笑」** | **阻断**（虚构互动） |
| E1 | 导航·一句话概括：「**海伦娜依成色断定**它属于侯爵夫人」 | `:251` `The jewellery was far too expensive to belong to anyone but the lady of the house.`（叙述者）；`:257` `‘It would seem the facts are leading us to Lady Burrows.’`（海伦娜） | 成色判断属叙述者，海伦娜只是顺推结论；归属偏移，不影响情节 | **提示** |
| E2 | 原句 1·中文理解：「狐狸那种奇特的、**咯咯作响**的低吼」 | `:38` `The strange clicking growl, indicative of foxes, never ceased to charm Helena.` | `clicking`＝咔哒作响；「咯咯」读作轻快笑声，与狐狸的咔哒声不合 | **提示**（措辞） |
| E3 | 原句 5·读者视角提示：「……却仍在最后一句**承认自己已经被吸引**」 | `:137` `And nothing about Cynthia Burrows was safe.`（引语末句）；`:125` `If Helena could keep her emotions separate from the investigation, she could certainly control her attraction to the suspect.`（引语之外） | 引语末句只说「不安全」，「承认被吸引」的原文在引语前的 `:125`；按 R4 属对应越界，影响轻微 | **提示**（对应越界） |

### 与原文相符的 10 条断言（避免「只报问题」的不完整交代）

- 侯爵是「肯特莫尔侯爵」且姓伯罗斯：`:35` `the very dead Marquess of Kentmore`、`:251` `Lord Hubert Burrows` ✓
- Clio 是辛西娅的**姻亲姐妹**（sister-in-law）：`:86` `Lady Cynthia Burrows, Clio’s new sister-in-law.`；`:161` `she is my sister-in-law and a dear friend` ✓（Clio 嫁的是辛西娅的哥哥托马斯，见 ch01:191）
- 鬼魂没有留下：`:74` `‘I don’t think his spirit remains. I feel… nothing.’` ✓
- 克莱奥是 firewitch、能与鬼魂对话并看它们的记忆：`:83` `Clio was a firewitch who could speak with ghosts and see their memories.` ✓
- 海伦娜是读心者、手段是「偷」念头：`:107` `Helena would steal the thoughts from Cynthia’s head and learn if Lady Burrows was a murderess.` ✓
- 拉克兰叔叔交代四条事实、其中「我要杀了那个人」被数名女仆听见：`:194`–`:206` ✓
- 海伦娜是 sapphic、火刑排第二、可用 witchwater 灭火：`:137` `Being a sapphic ranked just beneath being a witch… she could easily douse the flames with her witchwater` ✓
- 丑闻会毁掉她的名声**与养活一家人的生意**：`:137` `the scandal of such accusations would ruin her reputation and, by extension, the business which provided her family’s living.` ✓
- 吊坠＝红宝石＋盘绕的金蛇＋干血：`:251` ✓
- 结尾海伦娜带路走向辛西娅的起居室：`:257` `She strode forward and plucked the jewellery from her cousin’s open hand.`、`:269` `Turning, Helena led the way to Lady Burrows’ front parlour` ✓

---

## 三、已核实为正确（防误修，下一轮不得以「读着不对」为由改动）

1. **「她是克莱奥新近的姻亲姐妹」**（原句 3·中文理解）——依据 `:86` `Clio’s new sister-in-law.`：Clio 已嫁辛西娅的哥哥托马斯，`sister-in-law` 成立，**不得改成「朋友」或「表姐」**。**成立**。
2. **「判断他的鬼魂是否还留着，正是克莱奥这一趟要办的事」**（原句 2·中文理解）——依据 `:44` `Determining whether his ghost lingered was a task her cousin was here to accomplish.`：**her cousin 指 Clio**，成立。**成立**。
3. **「罗宾爵士……把衔着的东西乖乖丢进克莱奥掌心」**（原句 6·中文理解）——依据 `:251` `Blinking an obsidian eye at his mistress, he dutifully dropped the object into Clio’s palm.`：Sir Robin 是 Clio 的魔宠，**归属正确**。**成立**。
4. **「狐狸嫌脏这一点让气氛松了一下」**（原句 2·读者视角提示）——依据 `:42`–`:44` `He was not a fan of all the blood. Sticky and quite stale.`／`Hamlet was incredibly fastidious.`：**成立**。
5. **「最后一句改用价钱反推主人」**（原句 6·为什么这样写）——依据 `:251` `The jewellery was far too expensive to belong to anyone but the lady of the house.`：**成立**（注意这正是 E1 提示的另一半——判断出自叙述者，md 的「为什么这样写」没写错，错的是导航那句把判断安到海伦娜头上）。
6. **词表 22 条例句全部逐字取自本章**（行号分布见 `3-diff.md` 机器层小节）——**成立，不得改写例句**。

### 取证命令（「零命中」类断言自证）

```
/usr/bin/grep -c -E "Willow|母亲|布莱尔宅|药铺" "ch02 the dead marquess.md"
  → 输出 0；退出码 1（无命中）
/usr/bin/grep -n -E "pulled Clio into a tight hug" text/ch04_chapter_4.txt
  → 输出 200:The proper lady pulled Clio into a tight hug. …；退出码 0
```
（`text/` 被 `.gitignore` 排除，故一律用 `/usr/bin/grep` 显式路径，不用 `git grep`；退出码 1＝真查无。）

---

## 四、覆盖声明与已知盲区

- **本章覆盖**：R1 素读（先于任何 md 打开）→ R2 机器层 → R3 三张单子 → R4 逐块 6/6 → R5 判定表，**全流程走完**。
- **本书覆盖（深审进度）**：批 1 = ch02 / ch03 / ch04（**3 / 27 章**已完成 R0–R5）。其余 24 章**只有机器层**（R0 全书级已跑），**未做人判**，不得写成「已审查」。
- **同会话盲区（如实标注）**：本书由本会话在写作期产出，本章也是写作期读过的章之一；本次仍执行「先素读、写完 `1-suread.json` 才开 md」，但**不能视为完全盲态**。
- **未做**：五步审查附录 B（a–e 全文）已被 `审查表.md` 归档取代，不重复执行。
