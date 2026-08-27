# 修复指令：100 Great Short Stories 全量引文返工（指派：Hermes-Mac）

> 发起：[ZCode-Mac] @ 2026-08-27 09:30 UTC。本文件是自包含任务书，不依赖会话上下文。
> 结论先行：**该书面下的 99 个精读文件中仅 15 个通过全量引文核对（174/838 = 21%）**，其余约 84 篇需按本文流程返工。此前报告中"99/99 全部匹配"的结论只核对了每篇第①条引文，不能作为放行依据。

## 一、背景与证据

工具 `scripts/verify_quotes.py`（本次已固化入仓）把每篇精读 md 的 ①-⑩ 编号引语块逐条抽取，与 `library/*.epub` 展平全文做「去空白+大小写+标点无关」比对。

当前基线（可自行复现）：

```bash
python3 scripts/verify_quotes.py \
  "notes/books/short-story-anthologies/100 Great Short Stories by James Daley" \
  "notes/books/short-story-anthologies/100 Great Short Stories by James Daley/library/100 Great Short Stories - James Daley.epub"
```

实测输出末行：`总计 174/838 引文可核实（21%）；完全干净文件 15/99`。

虚构引文的典型例子（精读里写的 vs epub 里实际写的）：

| 文件 | 精读引文 | epub 原文 |
|---|---|---|
| 65 Open Window | "My aunt will be down presently," said the child. "She said so." | "My aunt will be down presently, Mr. Nuttel," said a very self-possessed young lady of fifteen |
| 87 Coffin Maker | "Adrian was a coffin-maker, and he had been a coffin-maker for thirty years." | 普希金原文首句与此完全不同 |
| 57 White Silence | 首句写 husky；真实首句为 "Carmen won't last two days." | 文件整体 0/9 命中 |

病根：生成时未把原文放进上下文，靠书名/文学常识脑补。前次 Hermes 重写的 ch95/ch99 用了正确方法并拿到 10/10——**证明方法可行**。

## 二、保留清单（15 篇，不动）

`02 05 06 07 08 09 10 12 14 15 16 17 20 95 99`

## 三、返工范围（84 篇）与优先级

按风险从高到低分三批：

- **P0（最高危，几乎全部 0 命中）**：ch26、63–66、68–91 中 0 分段（含 65/73/76/79/84/85/87/88/89 等——注意其中多篇曾被"人工核实 ✅"，但那是错判）
- **P1（1–3/10 残留大量虚构句）**：ch13、18–58 区间大部分
- **P2（轻度修补即可到 10/10）**：ch01(8/10)、ch98(9/10)、ch11(5/10)、ch97(2/10)、ch92(3/10)、ch96(3/10) 以及其他 7–9 分的文件——只需替换失真句子

## 四、每篇标准作业流程（SOP）

1. **提取原文**：从 epub 找到该故事的 html 分册，展平为纯文本存
   `notes/books/short-story-anthologies/100 Great Short Stories by James Daley/text/ch<NN>_<slug>.txt`
   （text/ 已在 .gitignore，不入 git）。epub html 有首字母下沉标签，去标签时不要在字母间引入空格。
2. **通读原文**再动笔；引语块中的英文**必须逐字取自该 txt**，禁止凭记忆转写；确需省略中间文字用 `…` 且保证省略号两侧都是原词。
3. **格式保持不变**：`# NN. 标题` / 作者行 / 故事梗概（基于原文校订）/ ①-⑩ 十处（中文理解 / 句子结构 / 关键词 / 表达方式 / 为什么这样写，子项间空行，引用块内只有英文原句）/ 三档词汇表（词条须真的出自文本）/ 一句话总结。frontmatter `modified` 保持或更新为当日。
4. **批次提交**：每 4–6 篇一个 commit，message 前缀 `fix(100stories): …` 并注明 `[Hermes-Mac]`。提交前 `git pull --no-edit`。
5. **⚠️ 多实例并行防护**：本机有多个 IDE 在同一目录工作。`git add` 时只 add 本任务的明确路径清单，禁止 `git add -A` / `git add .`，避免裹挟他人未提交的修改。
6. **验收门禁**：每批 commit 前对该批文件逐个跑：

   ```bash
   python3 scripts/verify_quotes.py "<book_dir>" "<epub>"
   ```

   要求每篇显示 `10/10 ✅`（若该篇引语块不足十处则全部命中）。任一 ❌ 都必须回炉后才可 commit。

## 五、完成标准与收尾

- [ ] 全部 84 篇 verify 通过（脚本总账应为 838/838 或注明合理豁免）
- [ ] `.memory/daily/<当日>.md` 记录进度与各 commit hash
- [ ] COLLABORATION.md 发消息宣布完成（附最终 verify 输出摘要），更新任务看板行
- [ ] **不要 push**——push 需用户确认后统一执行

遇阻塞或对某篇归属存疑，在 COLLABORATION.md 给 [ZCode-Mac] 留言，不要猜。
