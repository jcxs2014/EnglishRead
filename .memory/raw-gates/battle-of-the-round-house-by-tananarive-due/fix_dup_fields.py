#!/usr/bin/env python3
"""battle-of-the-round-house 重复子项字段修复（一次性工具，2026-10-19）。

问题（用户 2026-10-19 指出）：commit 2dca24dca 的「修复」不是翻译，而是**追加**了
第二套无连字符字段（`**中文理解**` / `**为什么这样写**` / `**读者视角提示**`），
原有的 `- **中文理解**` 等英文字段**一字未动** ⇒ 每个引语块有两套子项（AGENTS 第 9 条 c
「重复内容视为缺陷」），且 `check_chinese_layer` 的解析器 `out[cur]=…` 静默取最后一组
⇒ 报「阻断型 0」而原英文字段原封不动（**结构性假绿**）。

本脚本：
  1. 把新增组的内容**替换**进同块的标准字段（`- **X**：` 的值）；
  2. 删除新增组行；
  3. 把错放在「一句话总结」节末尾的组，按块号归位（ch03 块10 / ch04 块8）；
  4. 「一句话总结」节末尾的重复组**整组删除**（那节不该有子项）。

例外：ch04 块 3 的新增组「中文理解」是**跨章错位**（抄自 ch02 块4）⇒ 该块跳过，
由人工重译（见 --skip 名单）。

用法：python3 fix_dup_fields.py [--dry-run] [--apply]
"""
import os
import re
import sys
import tempfile

B = "notes/books/short-story-anthologies/battle-of-the-round-house-by-tananarive-due"
# ⚠️ 文件名**动态取**（不用字面量）：macOS 上字面量路径在某些调用方式下
#    os.path.exists 偶发 False，而 os.listdir 取出的同一名字恒可读——不踩这个坑。
_FILES = sorted(f for f in os.listdir(B) if f.startswith(("ch03", "ch04")) and f.endswith(".md"))
FILES = _FILES

BLK = re.compile(r"^> \*\*原句 (\d+):\*\*")
# 一次拿到「标签 + 值」——⚠️ 不能用 group(0).split('：')：正则只匹配到冒号为止，
#    group(0) 里**没有值**，split 后取到空串（2026-10-19 实测踩到）。
DUP = re.compile(r"^\*\*(中文理解|句子结构|关键词|为什么这样写|表达方式|读者视角提示)\*\*\s*[：:]\s*(.*)$")
STD = re.compile(r"^-\s*\*\*(中文理解|句子结构|关键词|为什么这样写|表达方式|读者视角提示)\*\*\s*[：:]\s*(.*)$")
SUM_HDR = re.compile(r"^## 一句话总结")

# 该块的新增组内容**不可信**（跨章错位），需人工重译 ⇒ 跳过该块的「中文理解」
SKIP_ZH = {("ch04 dickinson county archives closing.md", 3)}


def parse_blocks(lines):
    """返回 [(块号 or None, 起, 止)]，块 = 引语行 → 下一个引语行（或文件末）。"""
    starts = [(i, int(m.group(1))) for i, l in enumerate(lines) if (m := BLK.match(l))]
    out = []
    for k, (s, num) in enumerate(starts):
        e = starts[k + 1][0] if k + 1 < len(starts) else len(lines)
        out.append((num, s, e))
    return out


def collect(lines):
    """收集所有字段：{块号: {标签: 值}}（标准组与新增组分开）。"""
    blocks = parse_blocks(lines)
    std = {}      # 块号 → {标签: (行号, 值)}
    dup = {}      # 块号 → {标签: (行号, 值)}
    tail = {}     # 「一句话总结」节末尾的组（块号未知）
    cur_num = None
    in_sum = False
    for i, l in enumerate(lines):
        if SUM_HDR.match(l):
            in_sum = True
            cur_num = None
        m = BLK.match(l)
        if m:
            cur_num = int(m.group(1))
            in_sum = False
        md = DUP.match(l)
        ms = STD.match(l)
        if md:
            lab = md.group(1)
            val = md.group(2).strip()
            if in_sum:
                tail[lab] = (i, val)
            else:
                dup.setdefault(cur_num, {})[lab] = (i, val)
        elif ms:
            lab = ms.group(1)
            val = ms.group(2).strip()
            std.setdefault(cur_num, {})[lab] = (i, val)
    return std, dup, tail


def main():
    apply = "--apply" in sys.argv
    for fname in FILES:
        path = os.path.join(B, fname)
        lines = open(path, encoding="utf-8").read().split("\n")
        std, dup, tail = collect(lines)
        blocks = [b[0] for b in parse_blocks(lines)]

        # 错放在「一句话总结」节末尾的组：按「最后一个块号」归位
        # （ch03 块10 / ch04 块8 —— 追加脚本把它放到了文件末尾）
        if tail:
            last = blocks[-1]
            for lab, (i, val) in tail.items():
                dup.setdefault(last, {})[lab] = (i, val)
            print(f"{fname}: 「一句话总结」节末尾的 {len(tail)} 个重复组 → 归位到块{last}")

        # 计划：新增组替换标准组
        plan = []      # (行号, 新值)
        del_lines = set()
        for num, d in sorted(dup.items()):
            for lab, (i, val) in d.items():
                del_lines.add(i)
                if (fname, num) in SKIP_ZH and lab == "中文理解":
                    print(f"  ⚠️ 块{num} 的「中文理解」新增组跨章错位 ⇒ 跳过（保留原标准组，待人工重译）")
                    continue
                s = std.get(num, {}).get(lab)
                if not s:
                    print(f"  ⚠️ 块{num} 没有标准字段「{lab}」⇒ 只删新增行")
                    continue
                sline, sval = s
                if sval == val:
                    continue
                plan.append((sline, val, num, lab))
        print(f"{fname}: 块数 {len(blocks)} ｜ 新增组 {len(del_lines)} 行待删 ｜ 替换 {len(plan)} 处")
        for sline, val, num, lab in plan:
            print(f"   块{num} {lab} ← 行{sline+1}")
        if not apply:
            continue
        # 落盘（行级替换，原子）
        new = list(lines)
        for sline, val, num, lab in plan:
            prefix = new[sline].split("：", 1)[0].split(":", 1)[0] if ("：" in new[sline] or ":" in new[sline]) else new[sline]
            # 保留原行的标签与分隔符，只换值
            m = re.match(r"^(\s*-\s*\*\*[^*]+\*\*\s*[：:]\s*).*$", new[sline])
            if m:
                new[sline] = m.group(1) + val
        new = [l for i, l in enumerate(new) if i not in del_lines]
        out = "\n".join(new)
        fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(out)
        os.replace(tmp, path)
        print(f"   ✅ 已落盘 {fname}：{len(lines)} → {len(new)} 行")


if __name__ == "__main__":
    main()
