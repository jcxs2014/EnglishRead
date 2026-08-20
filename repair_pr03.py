#!/usr/bin/env python3
"""
Repair PR03 (the-bit-player) — 补上定稿格式外壳。

当前结构：
- 已有 frontmatter-like 元数据（title/source/url 等）但不是 --- 状态:未读 --- 格式
- 已有 `### 句 N（...）` 格式，需改成 `### 第 N 段：...`
- 已有原句引用（> **原句 N:** 已在内）
- 已有为什么这样写
- 缺：状态:未读 frontmatter、段落分组（6段）、段末段落逻辑、词汇分级三档表、长难句专项、精读结束总结

策略：
1. 把前部 frontmatter 改成 --- 状态: 未读 --- + 标准概览
2. 把 ### 句 N 拆成 6 段，每段加 `**段落逻辑：** → 链`
3. 保留原文"词汇分级总表"但改成三档表格式
4. 加 长难句专项 / 精读结束总结 / 可迁移表达
"""

import re

D = "/Users/jcxs2014/Documents/Works/EnglishRead"
PATH = f"{D}/parisreview/2026-08-10_Monday/03_the-bit-player_精读.md"

with open(PATH, "r", encoding="utf-8") as f:
    text = f.read()

# --- 1. 替换头部 frontmatter 块（第一个 --- 到第二个 --- 之间的元数据） ---
# 找第一段 frontmatter
m = re.search(r"^---\n.*?---\n", text, re.DOTALL)
if m:
    old_front = m.group(0)
    new_front = "---\n状态: 未读\n---\n"
    text = text.replace(old_front, new_front, 1)

# --- 2. 重写标题 ---
text = text.replace(
    "# 精读报告：The Bit Player — My Father with Steve Zissou",
    "# The Bit Player: My Father with Steve Zissou（龙套：我与父亲的史蒂夫·齐苏）— 精读分析",
)

# --- 3. 插入概览 + 段落脉络表（替换 "一、文章是什么" 那一段） ---
old_intro = re.search(
    r"^## 一、文章是什么\n.*?(?=\n## 二、段落逻辑总览)", text, re.DOTALL | re.MULTILINE
)
if old_intro:
    new_intro = """## 概览

**来源**：The Paris Review（2026-07-27），作者 Molly Cooper。**主题**：女儿回忆父亲——一位《纽约客》前太空记者，事业衰退、离异、独居后，2002 年在罗马片场被临时选为 Wes Anderson 电影《水中生活》里的一个**bit player（龙套）**。文章以"童年的命中注定伏笔 → 中年落魄 → 片场受挫 → 父亲的反复重讲 → 女儿多年后才懂 → 8 秒独一影像"为脉络，写下一位"一生是配角"的父亲，在人生最后一次演出里被命运选中的故事。**结构**：全篇用 `***` 分六段，构成三幕——童年伏笔 → 中年低谷与片场受挫 → 身后回望与主题升华。**段落脉络**：童年电梯里的命中注定伏笔 → 事业坠落与离异 → 女儿赴好莱坞 → 父亲被临时选中 → 片场背词屡败 → 父亲反复重讲与 8 秒独一影像。**金句**：*"there was a sense of something appropriate, even fated perhaps"* / *"In 2016, he died."* / *"the only recording I have of him is this scene, an eight-second clip"*。

"""
    text = text[:old_intro.start()] + new_intro + text[old_intro.end():]

# --- 4. 合并所有"段落逻辑总览"、"段落逻辑：箭头链"两节为一句"段落逻辑（全文）"，并把 `### 句 N（...）` 改成 `### 第 N 段：...`，同时按段落重组 ---

# 先把旧的 "## 二、段落逻辑总览" 到 "## 四、逐句精读（重点）" 之间的所有内容替换
old_logic = re.search(
    r"^## 二、段落逻辑总览\n.*?(?=\n## 四、逐句精读)", text, re.DOTALL | re.MULTILINE
)
if old_logic:
    new_logic = """## 段落逻辑（全文）

| 段 | 时段 | 主题 | 核心情绪 |
|---|---|---|---|
| 1 | 80 年代 | 童年：父亲与默瑞在电梯里的命中注定相似 | 伏笔 / 童年想象 |
| 2 | 80–90 年代 | 父亲事业坠落、离异、独居窘迫 | 落魄 / 白描之痛 |
| 3 | 2000 年代初 | 女儿赴洛杉矶、罗马片场 | 过渡 / 空间接近 |
| 4 | 2002 年夏末 | 父亲被临时选中、打车去试镜 | 转折 / 命运扣合 |
| 5 | 拍摄当天 | 父亲背词屡败、默瑞双臂交叉 | 高潮 / 沉默的痛 |
| 6 | 2002→2016 | 父亲反复重讲、2016 去世、8 秒独一影像 | 升华 / 极致克制 |

"""
    text = text[:old_logic.start()] + new_logic + text[old_logic.end():]

# 把剩余 "## 四、逐句精读（重点）" 改成 "## 逐句精读"
text = text.replace("## 四、逐句精读（重点）", "## 逐句精读")

# --- 5. 把 ### 句 N（...）改成 段落分组 + ### 第 N 段：主题 ---
# 分组依据（按文章自然段落）：
seg_map = {
    1:  ("第 1 段：童年伏笔——电梯里与默瑞的命中注定相似", [1, 2]),
    2:  ("第 2 段：中年坠落——父亲事业衰退、离异、独居", [3, 4, 5]),
    3:  ("第 3 段：过渡——女儿赴好莱坞与罗马片场", []),
    4:  ("第 4 段：被选中——临时试镜与荒诞成功", [6, 7]),
    5:  ("第 5 段：拍摄当天——背词屡败、默瑞沉默、女儿溜走", [8, 9, 10, 11]),
    6:  ("第 6 段：回望——父亲反复重讲、女儿的读懂、8 秒独一影像", [12, 13, 14, 15, 16, 17, 18, 19, 20]),
}

# 找到所有 ### 句 N（...） 并替换为 ### 第 N_seg 段：主题 或 保留为原句行
for seg_num, (title, orig_ids) in seg_map.items():
    # 段前导：第一次出现的 ### 句 orig_ids[0] 前面加段头
    if orig_ids:
        first = orig_ids[0]
        pat = rf"^### 句 {first}（"
        m2 = re.search(pat, text, re.MULTILINE)
        if m2:
            # 加段标题，替换该行开头 "### 句 first（...）" 为 "### 第 seg_num 段：title\n\n### 句 first（...）"
            # 但只替换一次
            pre = "### 第 " + str(seg_num) + " 段：" + title + "\n\n### 句 " + str(first) + "（"
            text = text[:m2.start()] + pre + text[m2.start() + len(f"### 句 {first}（"): ]

# 剩下的 ### 句 N（...）保留不动（不再重复加段头）

# --- 6. 给每段加段落逻辑 ---
seg_paralogic = {
    1: '**段落逻辑：** 童年观察父亲和默瑞电梯里的相似 → 用 "wry grin" 塑造两人共同的微笑气质 → "to my young ears" 限定的童年视角 → "fated" 伏笔埋下，二十年后才被回收',
    2: '**段落逻辑：** 太空兴趣衰退 → 被《纽约客》解雇 → 独居窘迫（一居室 / 冷冻鸡肉派 / 第一次洗衣服，三个白描） → "just slightly out of reach" 的父女疏离感',
    3: '**段落逻辑：** 女儿是最小的孩子、总觉得自己是 "afterthought" → 加州之旅让她 "够不着" 父亲 → 到好莱坞工作、被派罗马片场',
    4: '**段落逻辑：** 半好笑半好奇的心态 → 打车去试镜 → 磕磕巴巴却 "bespoke potential" → 破折号插入猜测语气 → 荒诞地被选中',
    5: '**段落逻辑：** 20 年后父亲 vs 默瑞的并置对照 → 背词失败的节奏模仿（a name wrong, a phrase left out...）→ 默瑞双臂交叉沉默旁观 → 女儿溜出片场',
    6: '**段落逻辑：** dine out → feast 用词递进 → 父亲三个 "重写" 动作（写文章 / 改汽艇 / 放假奥斯卡）→ "stirred something deeper in him" 情感转折 → Zissou 电影主题与父亲人生互文 → 2016 去世 → 8 秒独一影像',
}
# 在每段的最后一个"### 句 N" 分析块后追加段落逻辑
# 找到每个段落的末尾（下一个 ### 第 N 段 之前的位置）
segs_order = list(seg_map.keys())
insertions = []
for i, seg_num in enumerate(segs_order):
    if seg_num in seg_paralogic:
        # 找到 ### 第 seg_num 段 的起始
        m3 = re.search(rf"^### 第 {seg_num} 段：", text, re.MULTILINE)
        if m3:
            start = m3.start()
            # 下一段起始
            end = len(text)
            if i + 1 < len(segs_order):
                next_seg = segs_order[i+1]
                m4 = re.search(rf"^### 第 {next_seg} 段：", text, re.MULTILINE)
                if m4:
                    end = m4.start()
            # 在 [start, end) 末尾（## 逐句精读 结束之前）追加段落逻辑
            # 末尾找最后一个 `---` 分隔线之前的位置
            sub_end = end
            # 找末尾 ---
            last_dash = text.rfind("---", start, end)
            if last_dash != -1 and last_dash > start + 20:
                sub_end = last_dash
                text = text[:sub_end].rstrip() + "\n\n" + seg_paralogic[seg_num] + "\n\n" + text[sub_end:]

# --- 7. 把"词汇分级总表"改三档 ---
# 已有三档表了（### ⭐⭐⭐ / ### ⭐⭐ / ### ⭐），只是没包 ## 词汇分级
text = text.replace("## 十、词汇分级总表", "## 词汇分级")

# --- 8. 长难句专项（基于现有 "## 十一、重要语法结构" 改造） ---
old_grammar = re.search(
    r"^## 十一、重要语法结构\n.*?(?=\n## 十二、最值得重读)", text, re.DOTALL | re.MULTILINE
)
if old_grammar:
    new_long = """## 长难句专项

**1. 句 2 —— 童年伏笔存在句 + 铺排式肖像**
> Both were tall, of medium build, with soft, rounded features, blue eyes, wavy brown hair (fair to say somewhat disheveled), and a wry, ready grin. In this comparison, to my young ears at least, there was a sense of something appropriate, even fated perhaps, about these elevator encounters.
- 主干：*Both were tall... there was a sense of something... about these elevator encounters*
- 嵌套：一连串 *of/with* 形容词短语做表语并列；*to my young ears at least* 插入语限定了视角；*even fated perhaps* 两个副词 *even* + *perhaps* 叠用，把\"命中注定\"写得半真半幻
- 读法：先读完 *Both were tall...* 全串肖像，再读 *there was a sense of...* 存在句——两个主干各自完整，靠 *In this comparison* 串接

**2. 句 7 —— 破折号插入语 + 情态推测**
> Never noted for his acting talent, he fumbled his way through the reading, misdelivering the lines. But something—perhaps his distinctive manner of speaking, an unplaceable, mid-Atlantic lockjaw, or some element of his signature tatty style—must have bespoken potential.
- 主干：*he fumbled his way through the reading, misdelivering the lines* 主句 + *something must have bespoken potential* 主句
- 嵌套：破折号里塞了三个并列的\"猜测选项\"（*manner of speaking / lockjaw / tatty style*），是作者自己的犹豫语气；*must have bespoken* = 过去情态推测
- 读法：跳过破折号读 *something must have bespoken potential* 是核心；破折号是装饰，读完主句再回头品味三个猜测

**3. 句 8 —— 20 年并置对照 + 条件从句省略**
> In the decade or two since they had stood side by side in an elevator, my father and Murray had stopped resembling each other, if they ever really had.
- 主干：*my father and Murray had stopped resembling each other*
- 嵌套：*since they had stood...* 过去完成时时间状语；*if they ever really had* 省略了 *resembled each other*——**作者自己怀疑童年的相似是否真实**
- 读法：先抓主干 *father and Murray had stopped resembling each other*，再看 *since* 从句交代起点，最后看 *if* 从句的自嘲

**4. 句 20 —— 层层嵌套的收束句**
> ...the only recording I have of him is this scene, an eight-second clip, cut into the middle of a busy party montage, in which he briefly leans forward across an old tube-television screen and delivers the correct, final version of his line...
- 主干：*the only recording I have of him is this scene*
- 嵌套：*an eight-second clip* 同位语 → *cut into...* 过去分词定语 → *in which...* 定语从句
- 读法：一层一层剥开：先读 *is this scene*，再看 *an eight-second clip* 是什么，再看 *cut into a montage* 位置在哪，最后看 *in which he...* 里面发生了什么

"""
    text = text[:old_grammar.start()] + new_long + text[old_grammar.end():]

# --- 9. 把 "最值得重读的 5 句" 改成 "精读结束总结" ---
old_top5 = re.search(
    r"^## 十二、最值得重读\n.*?(?=\n## 十三、写作技巧总结)", text, re.DOTALL | re.MULTILINE
)
if old_top5:
    new_summary = """## 精读结束总结

这是一篇把**伏笔、互文、白描、数字收束**四种散文技法融为一体的家族回忆。Molly Cooper 用父亲 8 秒的龙套片段，写了一生——父亲失业、离异、独居，被命运意外选入 Wes Anderson 的片场；他背词屡败、沉默离场，回家却把这件事变成了反复重讲的盛宴。二十年后女儿才懂：父亲的反复重讲不是吹牛，而是他一生被命运触动的唯一时刻。

**四组金句**：① *\"a sense of something appropriate, even fated perhaps\"*（童年伏笔）；② *\"defrosted chicken pot pies for dinner most nights, and learned to do laundry for the first time\"*（白描之痛）；③ *\"dine out on... feasted\"*（用词递进）；④ *\"the only recording I have of him is this scene, an eight-second clip\"*（数字收束）。

**核心技法**：① 伏笔 20 年回收（电梯相似 ↔ 片场重逢）；② 并置对照（父亲 vs 默瑞 / 父亲 vs Zissou）；③ 白描代替抒情（一居室 / 冷冻鸡肉派 / 洗衣服）；④ 句式模仿内容（省略句并列模拟背词失败节奏）；⑤ 数字收束（8 秒 = 一生）。

"""
    text = text[:old_top5.start()] + new_summary + text[old_top5.end():]

# --- 10. 保留 "写作技巧总结" 作为附加参考（去掉编号） ---
text = text.replace("## 十三、写作技巧总结", "## 写作技巧笔记")

# --- 11. 可迁移表达（已在 "## 十四、可迁移表达"，改为标准标题） ---
text = text.replace("## 十四、可迁移表达", "## 可迁移表达")

with open(PATH, "w", encoding="utf-8") as f:
    f.write(text)

print("PR03 repaired. New size:", len(text))
