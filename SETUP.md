# EnglishRead：GitHub Actions 构建 + Wrangler 部署 收尾清单

本目录的 `deploy.yml` 把 EnglishRead 的构建从 Cloudflare Git 集成挪到 GitHub Actions，
部署仍用 `wrangler deploy` 推回 **englishread** Worker（`englishread.jcxs2014.workers.dev`）。
上线前必须完成下面 4 步，否则会双构建冲突或部署失败。

## 项目事实（来自 web-build-docs/englishread-build.md）
- 静态站点生成器：**Quartz v5**（Node.js）。
- 内容源：`notes/`（Markdown + YAML frontmatter），约 **18000+** 个 md（books 17760 篇持续增长）。
- 构建产物：`site/public/`（输入 ~18k 推算输出 ~29k 文件）。
- 部署：`wrangler.jsonc` → `assets.directory: ./site/public`，Worker 名 `englishread`。
- 现状：`.github/` 为空，Cloudflare 直连 GitHub 仓库、在 CF 构建机跑 `bash build.sh` 自动上线（Git Method B）。

## 0. 为什么要迁（现状对撞的墙）
Cloudflare Workers Builds 构建机 = **8GB 内存 / 20 分钟硬超时**（官方 limits-and-pricing）。
18000+ 篇笔记下：解析约 20 分钟起步（贴着超时），堆需 6GB（8GB 机器余量紧张）。
GitHub Actions `ubuntu-latest` = **4 vCPU / 16GB 内存、默认 job 超时 360 分钟**——两堵墙同时解除。
公开仓库 Actions 分钟数免费；私有仓库有 2000 分钟/月配额（按当前构建 ~30 分钟算约 60 次/月，需留意）。

## 1. 配置两个 secret
仓库 → Settings → Secrets and variables → Actions → New repository secret：
- `CLOUDFLARE_API_TOKEN`：Cloudflare 控制台创建的 API Token。
  - 建议用 "Edit Cloudflare Workers" 模板（Custom 权限勾 `Account > Workers Scripts > Edit` + `Read`；若涉及 KV/D1/R2 再补）。
- `CLOUDFLARE_ACCOUNT_ID`：你的 Cloudflare 账户 ID（可在 wrangler.jsonc 里加 `account_id` 代替放 secret，二选一；这里按文档方案 A 放 secret）。
- 当前 `wrangler.jsonc` 没有 `account_id` 字段，所以**账户 ID 必须**通过 secret 或写入 wrangler.jsonc 提供，否则 `wrangler deploy` 失败。

## 2. 关闭 Cloudflare 的 Git 自动构建（关键，避免双构建）
现在 EnglishRead 靠 Cloudflare Git 集成（push 即自动构建部署）。启用本 Actions 后必须关掉它，
否则一次 push 会触发**两次**构建/部署，互相冲突。

Cloudflare 控制台：
- Workers & Pages → 选中 `englishread` → **Settings** → **Build** / **Build & deployments**
- 将 "Production branch" / "Automatic deployments" 置空或关闭（不同界面版本叫 "Disable deployments" 或把生产分支改成 None）。
- 本质：断开 Git 与生产部署的绑定。

> 验证：push 一次，确认只有 GitHub Actions 出现部署记录，Cloudflare 的 Deployments 面板不再因同一次 push 自动新增。

## 3. 确认构建环境（已在 workflow 内处理，但请知悉）
- **Node 22** + `NODE_OPTIONS="--max-old-space-size=6144"`：18000+ 篇笔记时 Quartz 主进程反序列化会 OOM，6GB 堆是必需（build.sh 已设 commit 8adfc5bf，workflow 再注入一层保险）。
- `build.sh` 内含：进入 `site`、`npm install --legacy-peer-deps`、`npx quartz build -d ../notes`、以及 Python 去除 `public/static/contentIndex.json` 的 `content` 字段（避开 **Workers 25MB 单文件限制**）。
  - ubuntu-latest 自带 python3，此步无需额外安装。

## 4. ✅ frontmatter 冒号问题（已修复，2026-10-14）
全库扫描 18151 个 md，致命错误恰好 37 处，全部在 `devil-inside` 一书，已修复并推送：
commit `a163e5583`（37 个 title 加双引号，YAML 逐文件验证 37/37 通过）。
**遗留动作**：书籍生成侧（Hermes 流水线）的 frontmatter 模板仍不引 title——下本带冒号的书还会炸，
应在生成器补"title 一律双引号"规则；也可在本 workflow 加一步 frontmatter lint 提前报错。

## ⚠️ 重要：这条路线没有解决"文件数/体积"上限
本方案把"在哪构建"从 Cloudflare 搬到 GitHub Actions，但**最终仍 `wrangler deploy` 回 Workers**，
Workers 静态资源上限不变：**Free 计划 20,000 个文件 / Paid（$5/月）100,000 个**（需 wrangler ≥ 4.34.0），
25 MiB 单文件上限也仍在（Free/Paid 同限）。

**当前推算：~29k 输出文件 > Free 的 20,000 → Free 计划下即使 GHA 构建成功，上传仍会失败。**
出路三选一：
1. **升级 Workers Paid**（$5/月 → 100,000 文件上限）：改动最小，直接解锁；
2. **books 拆分**：独立 Worker 子站或 R2 外置，从根上解除（工作量大）；
3. **GitHub Pages 托管**（方案 B，见 englishread-build.md）：无文件数硬上限，但失去 Workers 特性。

缓解手段（已有/仍需保持）：`contentIndex.json` 去 `content`（已在 build.sh，commit 8adfc5bf 同期）。
本方案胜在改动最小、保留 Workers 生态与 `*.workers.dev` 域名，并解除构建超时/内存两堵墙；
但**文件数上限必须与上面三选一配套，否则部署仍失败**。
