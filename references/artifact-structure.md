# 产物目录与交付模式

在业务项目目录调用 `scripts/init_pm_case.py` 的实际安装路径。默认在当前目录的 `.pd/` 写入骨架；`--base-dir` 可指定输出路径，`--nested` 追加 `<slug>/`。

## 公共产物

两种模式都创建：

```text
.pd/
├── brief/
│   ├── 00-request.md
│   └── 01-web-research.md
├── analysis/
│   ├── 01-brainstorm.md
│   ├── 03-evidence-ledger.md
│   ├── 04-demand-backlog.md
│   └── 05-validation-plan.md
├── prd/
└── feishu/
    ├── manifest.json
    ├── publish-plan.md
    └── publish-result.md
```

`brief/01-web-research.md` 按实际决策缺口填写，无联网条件则写限制，不能填造检索结果。证据、需求池和验证计划可保留适用范围说明，但不能把关键未知隐藏成已确认结论。

## 轻量模式 `--profile lean`

`prd/` 下只有 `01-feature-spec.md`，包含问题、目标、取舍、范围、需求规则、主异常流程、验收、指标、上线和复盘。清单只有该 PRD，不创建原型、汇报和运营占位目录。

## 标准模式 `--profile standard`（默认）

额外创建 `analysis/02-jobs-product-lens.md`（产品聚焦判断），以及 `prd/` 下 **19 篇**文档：

| 文件 | 主题 |
| --- | --- |
| `00-business-blueprint.md` | 业务蓝图 |
| `01-project-background.md` | 项目背景 |
| `02-executive-summary.md` | 执行摘要 |
| `03-problem-and-goals.md` | 问题与目标 |
| `04-user-segments-and-scenarios.md` | 用户角色与场景 |
| `05-solution-overview.md` | 方案总览 |
| `06-user-flows.md` | 用户流程 |
| `07-functional-requirements.md` | 功能需求 |
| `08-business-rules-and-acceptance.md` | 业务规则与验收 |
| `09-information-architecture.md` | 功能与信息架构 |
| `10-technical-architecture.md` | 系统边界与技术约束 |
| `11-metrics-risks-dependencies.md` | 指标、风险与依赖 |
| `12-scope-and-release-plan.md` | 范围与版本 |
| `13-interaction-and-content-spec.md` | 交互与内容规范 |
| `14-data-and-analytics.md` | 数据与分析 |
| `15-launch-and-operations.md` | 上线、运营与复盘 |
| `16-milestones.md` | 里程碑 |
| `17-open-questions-and-decisions.md` | 开放问题、决策与变更 |
| `18-appendix-and-assets.md` | 附录与素材 |

为兼容现有用法，保留以下占位文件；仅在用户要求时填充或实现：

```text
prototype/
├── 01-prototype-brief.md
├── 02-screen-flow.md
├── 03-wireframe-notes.md
└── 04-page-coverage-checklist.md
deck/
├── 01-deck-outline.md
└── 02-deck-spec.json
ops/
├── 01-campaign-brief.md
└── 02-creative-matrix.md
diagrams/
└── README.md
```

需要原型时创建 `prototype/web/` 或等价可预览代码。用户只要 brief 时无需代码；请求完整原型时不能只交 brief。PPT 大纲也不等于 `.pptx`。

## 图表产物

实际使用飞书画板时，在 `diagrams/YYYY-MM-DDTHHMMSS/` 中保留该路径需要的源稿、中间产物和预览，例如 `diagram.mmd`、`diagram.svg`、`diagram.json`、`diagram.gen.cjs`、`diagram.png`。不是每条路径都需要所有格式。

每次迭代使用独立目录；同秒多张图也应分配不同的时间戳目录，不覆盖已有产物。成功后将画板 URL 与 token 写入发布结果。失败保留本地产物。具体发布方式见 [feishu-whiteboard.md](feishu-whiteboard.md)。

## 重复运行与清单

- 初始化只创建缺失文件，包括 `manifest.json`，不覆盖人工编辑、文档筛选或发布结果。
- 清单记录标题、slug、模式和 PRD 的绝对路径；旧清单没有模式字段时按标准模式处理。
- 不同标题或模式须使用新目录，避免正文与清单混淆；脚本不自动迁移模式。
- 案例目录移动后需人工检查清单路径。现有案例重复初始化可能增加新模板，但不会自动改写旧 PRD 内容。
- 默认清单只含 `prd/`。`brief/`、`analysis/` 及原始证据不默认发布。

完成与否依本次范围及 [PRD 质量标准](prd-quality-gates.md) 判断，不以空文件、占位目录或文档数量判断。
