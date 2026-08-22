# EnglishRead · 小说精读库索引

| 书名（slug） | 作者 | 首出 | 类型 | 字数（内容） | 章数 | 阅读状态 | 精读进度 | 备注 |
|---|---|---|---|---|---|---|---|---|
| a-most-angelic-death | Lesley Gray | 2025 | 犯罪悬疑小说（Painted Illusions Book 1） | ~390,600 | 21（Prologue + Ch1-18 + Epilogue，含 Author's note） | 待读 | 0/21 | 主角 Rita（画家/侦探）与 Ash 搭档破连环艺术家谋杀案 |
| book-lovers | Emily Henry | 2022 | 浪漫喜剧 | ~547,397 | 39（Prologue + 37章 + 尾声） | 待读 | 0/39 | 纽约出版经纪人 Nora 与小城林业专家 Charlie 的夏天 |
| books-that-saved-my-life | Michael McGirr | 2018 | 非虚构/阅读随笔（42 篇，非小说） | ~432,146 | 42（Ch1-40 + Epilogue + A Word of Thanks） | 待读 | 0/42 | ⚠️ 非小说，是"哪些书改变了我的生活"随笔合集，每章评一部经典 + 个人回忆 |

> **说明**：`books-that-saved-my-life` 严格说不是小说——是 McGirr 的读书随笔。放在小说库里只是用户把它当阅读材料处理。如需另开 `essays/` 目录，可后续迁移。

## 阅读状态说明
- **待读**：已放入 library/，未开始精读
- **阅读中**：已读但未精读
- **精读中**：部分章节已写盘
- **精读完成**：精读 + 总结.md 完成

## 使用方式
- 开始新书：`mkdir -p notes/novels/<slug>/library` 并把 epub 放进来；把文本抽到 `text/`；更新本表。
- 精读章节：`notes/novels/<slug>/精读/CH01_章题.md`；每章完成即更新本表"精读进度"列（如 `5/21`）。
- 全书收尾：写完 `notes/novels/<slug>/总结.md`，把状态改为"精读完成"。
