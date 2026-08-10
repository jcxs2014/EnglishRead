# EnglishRead 记忆库（跨 IDE 共享）

## 是什么
中文母语者的英文**逐句精读**知识库。目标：从"看中文翻译"过渡到"直接读懂英文原文"。

## 关键路径
- 工作区根：`~/Documents/Works/EnglishRead/`
- 根目录规则：`AGENTS.md`（精读工作流）、`README.md`（工作流说明）、`COLLABORATION.md`（协作板）
- 协作脚本：软链接自 `~/Sites/OpenCodeFiles/multi-ide-template/`

## 来源与目录
- `parisreview/`（主力，RSS 带全文）：
  `<日期%Y-%m-%d_%A>/##_slug.txt`（原文）+ `##_slug_精读.md`（报告）+ `index.json`（索引）
- `economist/`（按期刊发行日期）：`260725/` 等；报告 `Title_snake_case.md`
- 待启用：`quantamagazine/`、`aeon/`
- 避开：The Atlantic / The New Yorker（付费墙，RSS 无全文）

## 每日工作流
1. `python3 fetch_paris.py` — 抓取 RSS 全文，建目录 + `index.json`
2. `python3 scan.py` — 扫描题材/敏感度/字数，人工挑 3–5 篇
3. AI 精读 → 写 `##_slug_精读.md`（与原文同目录）

## 精读规则
- 不做逐词翻译；show, don't tell；克制与留白
- 报告要素：原句 / 自然中文 / 句子结构 / 关键词 / 地道表达 / "为什么这样写"
- 长难句专项：找主干→修饰→从句→恢复逻辑→整体理解
- 交互指令：继续 / 详细解释这个句子 / 只讲语法 / 只讲词汇 / 测试我 / 不要翻译

## 协作约定（跨 IDE）
- 同一目录多 IDE 共享文件系统，写入即同步，**无需 git pull/push**
- 时间戳一律 **UTC**（`date -u '+%Y-%m-%d %H:%M UTC'`）
- 消息/commit 前缀：`[IDE名-机器名]`
- 记忆目录：`.memory/`（本文件为共享记忆宿主）

## 敏感内容处理
- 预判优先：政治/宗教极端/暴力/争议话题 → 跳过或交 `english-read` 子代理
- 例：`04_shen-yun` 标 HIGH 已 SKIP；`01_jonestown` 学术处理
- MiniMax 触发 1027 → english-read 子代理接管后续分析

## 现状（2026-08-10）
- `parisreview/2026-08-10_Monday/` 精读 5 篇：02 / 05 / 06 / 07 / 10
- `economist/` 已读期：260606–260801