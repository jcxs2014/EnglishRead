#!/usr/bin/env python3
"""
260810 旧精读 → 定稿格式的机械装配脚本。

旧稿已有：中文理解、句子结构、关键词、表达方式、为什么这样写
旧稿缺失：frontmatter、`> **原句 M:**` 引用块、`### 第 N 段：` 段头、`段落逻辑：` 箭头链

脚本逻辑：
1. 前置 `--- 状态: 未读 ---`（若没有）
2. `### 句 N（...）` / `### N. 主题` / `### N、主题` → `### 第 N 段：主题`
3. `> 英文原句` → `> **原句 M:** 英文原句`（M 段内从 1 开始重置）
4. `> **原句 N:** ...` 已合规 → 保持，但编号按段重置
5. `**理解**：` → `**中文理解：**`（统一命名）
6. 段末追加 `**段落逻辑：** ① → ② → ③`（从该段"为什么这样写"或"理解"内容提取主题）
7. 检查并补齐 `## 词汇分级` / `## 段落逻辑` / `## 可迁移表达`

用法：python3 reformat.py file.md ...
"""
import re, sys, os

def load(p):
    with open(p, "r", encoding="utf-8") as f:
        return f.read()

def dump(p, s):
    with open(p, "w", encoding="utf-8") as f:
        f.write(s)

def reformat(text):
    lines = text.split("\n")

    # 1) frontmatter
    if lines and lines[0].strip() == "---":
        # 已有
        if not any("状态: 未读" in ln for ln in lines[:10]):
            lines = ["---", "状态: 未读", "---"] + lines[2:4]  # 保留旧 fm 但插入新
    else:
        lines = ["---", "状态: 未读", "---"] + lines

    # 2) 处理段头
    new_lines = []
    for ln in lines:
        if re.match(r"^### 第 \d+ 段", ln):
            new_lines.append(ln); continue
        # ### 句 N（主题）
        m = re.match(r"^(### 句 )(\d+)(.*)", ln)
        if m:
            tail = m.group(3).strip().lstrip("（(（(")
            if tail:
                new_lines.append(f"### 第 {m.group(2)} 段：{tail}")
            else:
                new_lines.append(f"### 第 {m.group(2)} 段：内容")
            continue
        # ### N. / ### N、 / ### N：主题
        m = re.match(r"^(### )(\d+)[\s\.\、.、：:]*\s*(.*)", ln)
        if m:
            tail = m.group(3).strip()
            if tail:
                new_lines.append(f"### 第 {m.group(2)} 段：{tail}")
            else:
                new_lines.append(f"### 第 {m.group(2)} 段：内容")
            continue
        new_lines.append(ln)
    lines = new_lines

    # 3) 按 ### 第 N 段 分段，段内重排引用块
    seg_boundaries = [i for i, ln in enumerate(lines) if re.match(r"^### 第 \d+ 段", ln)]
    # 追加尾部边界
    seg_boundaries.append(len(lines))

    for k in range(len(seg_boundaries) - 1):
        s = seg_boundaries[k]
        e = seg_boundaries[k+1]
        # 在 lines[s:e] 内处理
        block_num = 0
        i = s + 1  # 跳过段头
        while i < e:
            ln = lines[i]
            # 已经在块内（不是 > 开头）则跳过
            if not ln.startswith("> "):
                i += 1; continue
            # 找连续 > 行
            j = i
            while j < e and lines[j].startswith("> "):
                j += 1
            # 第一行编号
            block_num += 1
            first = lines[i]
            if "**原句" in first:
                # 已经编号，检查/修正
                m2 = re.match(r"^> \*\*原句 \d+:", first)
                if m2:
                    lines[i] = re.sub(r"> \*\*原句 \d+:", f"> **原句 {block_num}:", first, count=1)
            else:
                # 未编号，加
                body = first[2:].lstrip()
                lines[i] = f"> **原句 {block_num}:** {body}"
            i = j

    # 4) 段末追加 段落逻辑
    # 在每段末尾（下一段前）插入
    new_lines = []
    for k in range(len(seg_boundaries) - 1):
        s = seg_boundaries[k]
        e = seg_boundaries[k+1]
        seg = lines[s:e]
        has_yj = any("**原句" in ln for ln in seg)
        has_logic = any("段落逻辑" in ln for ln in seg)
        new_lines.extend(seg)
        if has_yj and not has_logic:
            # 从该段 "为什么这样写" 或 "理解" 内容提取主题
            themes = []
            for ln in seg:
                m = re.search(r"\*\*(?:中文)?理解\*\*[:：]\s*(.+)", ln)
                if m and len(themes) < 6:
                    t = m.group(1).strip().rstrip("。").rstrip(".").rstrip("；")
                    if len(t) > 25:
                        t = t[:25]
                    themes.append(t)
                # 也可以用 "为什么这样写"
            if not themes:
                themes = [f"原句 {i+1}" for i in range(min(3, block_count_in_seg(seg)))]
            new_lines.append("")
            new_lines.append(f"**段落逻辑：** " + " → ".join(themes))
    lines = new_lines

    text = "\n".join(lines)

    # 5) 补齐尾部章节
    if "## 词汇分级" not in text and "词汇分级" not in text:
        text += "\n\n## 词汇分级\n> 请读者结合旧精读「词汇分级总表」补入。\n"
    if "## 段落逻辑" not in text:
        text += "\n\n## 段落逻辑\n> 全文级逻辑梳理（见逐句精读中的段落逻辑链）\n"
    if "## 可迁移表达" not in text:
        text += "\n\n## 可迁移表达\n> 请读者结合旧精读「可迁移表达」列表补入。\n"

    return text

def block_count_in_seg(seg):
    count = 0
    i = 0
    while i < len(seg):
        if seg[i].startswith("> ") and "**原句" not in seg[i]:
            count += 1
        i += 1
    return count

def main():
    for p in sys.argv[1:]:
        if not os.path.exists(p):
            print(f"SKIP {p}  (not found)"); continue
        t = load(p)
        new = reformat(t)
        dump(p, new)
        # 校验
        checks = {
            "frontmatter": "状态: 未读" in new,
            "原句": "**原句" in new,
            "为什么": "为什么这样写" in new,
            "段落逻辑": "段落逻辑" in new,
            "词汇分级": "词汇分级" in new,
            "可迁移表达": "可迁移表达" in new,
        }
        flags = "".join("✓" if v else "✗" for v in checks.values())
        print(f"{flags}  {p.split('/')[-1]}  size={len(new)}")

if __name__ == "__main__":
    main()
