# 产物目录结构

`scripts/init_pm_case.py` 默认会生成如下目录：

```text
.pd/
├── brief/
│   └── 00-request.md
├── analysis/
│   ├── 01-brainstorm.md
│   └── 02-jobs-product-lens.md
├── prd/
│   ├── 00-business-blueprint.md
│   ├── 01-project-background.md
│   ├── 02-executive-summary.md
│   ├── 03-problem-and-goals.md
│   ├── 04-user-segments-and-scenarios.md
│   ├── 05-solution-overview.md
│   ├── 06-user-flows.md
│   ├── 07-functional-requirements.md
│   ├── 08-business-rules-and-acceptance.md
│   ├── 09-information-architecture.md
│   ├── 10-technical-architecture.md
│   ├── 11-metrics-risks-dependencies.md
│   ├── 12-scope-and-release-plan.md
│   ├── 13-interaction-and-content-spec.md
│   ├── 14-data-and-analytics.md
│   ├── 15-launch-and-operations.md
│   ├── 16-milestones.md
│   ├── 17-open-questions-and-decisions.md
│   └── 18-appendix-and-assets.md
├── diagrams/                            # 飞书画板产物根，按 lark-whiteboard 规范
│   └── YYYY-MM-DDTHHMMSS/               # 单次画板的产物目录
│       ├── diagram.mmd                  # Mermaid 源码（Mermaid 路径）
│       ├── diagram.svg                  # SVG 源码（SVG 路径）
│       ├── diagram.json                 # DSL / OpenAPI 中间产物
│       ├── diagram.gen.cjs              # 坐标计算脚本（DSL 路径）
│       └── diagram.png                  # 渲染预览
├── deck/
│   ├── 01-deck-outline.md
│   └── 02-deck-spec.json
├── ops/
│   ├── 01-campaign-brief.md
│   └── 02-creative-matrix.md
├── prototype/
│   ├── 01-prototype-brief.md
│   ├── 02-screen-flow.md
│   ├── 03-wireframe-notes.md
│   └── 04-page-coverage-checklist.md
└── feishu/
    ├── manifest.json
    ├── publish-plan.md
    └── publish-result.md
```

如果显式传入 `--nested`，输出目录会变成 `.pd/<slug>/`。

## diagrams/ 目录与 lark-whiteboard 协同

`diagrams/` 是面向飞书画板的本地产物根。每张被升级为画板的图都按 `lark-whiteboard` 的产物规范落在一个 `YYYY-MM-DDTHHMMSS/` 子目录里，文件名固定为 `diagram.mmd` / `diagram.svg` / `diagram.json` / `diagram.gen.cjs` / `diagram.png`。

约束：

1. 子目录名严格用本地时间 `YYYY-MM-DDTHHMMSS`，不含冒号和时区
2. 同一张图迭代多次，每次用一个新时间戳子目录，保留历史
3. 画板发布成功后，必须把 `whiteboard_token` 与画板 URL 写回 `feishu/publish-result.md`
4. 画板失败不要删除本地产物目录，授权恢复后继续重试

详细决策树与命令模板见 `references/feishu-whiteboard.md`。

## 文档拆分原则

1. 一个主题一篇文档。
2. 图和正文尽量放在最相关的那篇文档里。
3. 飞书展示顺序以 `manifest.json` 为准。
4. PRD 文档名保持稳定，便于脚本和发布流程复用。
5. PRD 默认应包含多种视觉元素，不应退化成纯文字长文。

## 最低交付要求

- `analysis/01-brainstorm.md`
- `analysis/02-jobs-product-lens.md`
- `prd/00-business-blueprint.md`
- `prd/01-project-background.md`
- `prd/06-user-flows.md`
- `prd/09-information-architecture.md`
- `prd/10-technical-architecture.md`
- `prd/12-scope-and-release-plan.md`
- `prd/14-data-and-analytics.md`
- `prd/15-launch-and-operations.md`
- `prototype/01-prototype-brief.md`
- `prototype/02-screen-flow.md`
- `prototype/04-page-coverage-checklist.md`
- `feishu/manifest.json`

缺少这些文件时，不应声明任务已完成。

飞书画板产物（`diagrams/...`）不是默认最低交付；当且仅当用户要求把关键图升级为画板时才需要。
