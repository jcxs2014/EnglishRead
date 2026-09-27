# Quartz 配置红线（从 AGENTS.md 迁出，2026-09-27）

> 这些是**站点/CSS/frontmatter 配置**规则，与精读执行流程无关，每本书开工都用不到。
> 迁出是为把 AGENTS.md 压回 harness 指令注入预算（65,536 B）以内。
> **改 Quartz 配置时才读本文件**；`/quartz.config.yaml`、`site/custom.scss` 相关改动以本文件为准。

## Quartz 配置红线

### 排序规则
- 章节书籍（chXX / 01-XX 命名）+ 有编号的文档，frontmatter 必须加 `modified:"YYYY-MM-DD"`（首 commit 日期）
- 使 created-modified-date 插件读 frontmatter，所有章节同日期 → alphabetical 正序
- 双套独立排序：Explorer（侧边栏）按 displayName localeCompare；PageList（文件夹页）按 modified date desc → alphabetical fallback

### typography 规则
- **css2 的 `family=` 参数永远单一字体名**，组合栈放 `custom.scss` 的 `:root` 变量
- 如 `quartz.config.yaml` typography.body 写成 CSS 栈 `"Lora, Noto Serif SC"` 会导致 Google Fonts 400

### 前端定制哲学
- 不模拟原生行为，变量层组合字体，砍无引用装饰系统
- 给 Quartz 加行为前先读插件 dist 确认原生是否覆盖
- 每个 CSS 自定义规则都针对真实 class 名，发明的新类名不会生效

### YAML 炸弹模式
- frontmatter title 含 `: `（冒号空格）或斜杠 `/` 时需加引号，否则 Quartz 解析失败
- 预防规则：所有 frontmatter 值含 `: ` / `,` / `?` / `"` / `'` 都应加引号
