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

## 文档拆分原则

1. 一个主题一篇文档。
2. 图和正文尽量放在最相关的那篇文档里。
3. 飞书展示顺序以 `manifest.json` 为准。
4. PRD 文档名保持稳定，便于脚本和发布流程复用。
5. PRD 默认应包含多种视觉元素，不应退化成纯文字长文。

## 最低交付要求

- `analysis/01-brainstorm.md`
- `analysis/02-jobs-product-lens.md`
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
