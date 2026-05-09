# pd-skill

端到端产品经理编排技能。

目标不是只写一篇 PRD，而是把一句需求推进成一套可交付的产品产物，包括需求分析、多文档 PRD、流程图/架构图、原型 brief、按需飞书发布、Deck 结构和运营素材 brief。

## 当前能力

- 需求头脑风暴
- Jobs 风格产品判断收敛
- 多文档 PRD 生成
- Mermaid 流程图、体验图、架构图
- 飞书多文档发布
- 原型 brief 与前端原型交接
- Deck 大纲与 JSON 结构
- 运营素材 brief

## 关键更新

### 1. 头脑风暴后，强制进入 Jobs 收敛

在 `analysis/01-brainstorm.md` 之后，默认继续生成：

- `analysis/02-jobs-product-lens.md`

这一层用于收敛：

- 一句话产品定义
- Focus / Say No
- 这版最该砍掉什么
- end-to-end 体验原则
- 用户会记住的关键瞬间
- 对 PRD 的写作指令

默认优先对齐 `alchaincyf/nuwa-skill` 的 Steve Jobs 视角方法，并复用当前环境里的 `steve-jobs-perspective` 技能。

### 2. PRD 默认是视觉化文档，不是纯文字长文

PRD 不再只追求“完整”，还要求“适合评审会快速扫描”。

默认会优先产出这些结构化视觉元素：

- 封面型总览图
- 体验旅程图
- 产品循环图
- 信息架构图
- 指标漏斗图
- 方案结构图
- 技术架构图

### 3. 飞书优先使用可编辑格式

面向飞书发布时，核心图形默认采用可编辑文本格式：

1. `Mermaid`
2. Markdown 表格
3. 编号列表 / 分层清单 / 文本卡片

默认不使用：

- `SVG`
- `PNG / JPG`
- 截图式图示

这意味着 PRD 发布到飞书后，图形主稿仍然可以继续改，而不是只能看。

## 标准工作流

1. 初始化工作目录
2. 生成头脑风暴文档
3. 生成 Jobs 产品判断文档
4. 生成多文档 PRD
5. 询问是否发布到飞书
6. 如需要，发布到 Drive 或 Wiki
7. 继续原型 brief / 前端原型
8. 按需补 Deck 与运营素材

## 产物结构

默认生成在 `.pd/`：

```text
.pd/
├── brief/
├── analysis/
│   ├── 01-brainstorm.md
│   └── 02-jobs-product-lens.md
├── prd/
├── prototype/
├── deck/
├── ops/
└── feishu/
```

其中 PRD 最少包括：

1. `01-project-background.md`
2. `02-executive-summary.md`
3. `03-problem-and-goals.md`
4. `04-user-segments-and-scenarios.md`
5. `05-solution-overview.md`
6. `06-user-flows.md`
7. `07-functional-requirements.md`
8. `08-business-rules-and-acceptance.md`
9. `09-information-architecture.md`
10. `10-technical-architecture.md`
11. `11-metrics-risks-dependencies.md`
12. `12-scope-and-release-plan.md`
13. `13-interaction-and-content-spec.md`
14. `14-data-and-analytics.md`
15. `15-launch-and-operations.md`
16. `16-milestones.md`
17. `17-open-questions-and-decisions.md`
18. `18-appendix-and-assets.md`

## 图形约定

### 执行摘要

- 封面型总览图
- 体验旅程图
- 本期重点卡片

### 方案总览

- 产品循环图
- 方案结构图
- 模块清单

### 信息架构

默认使用双轨表达：

- Mermaid 图
- 层级表

这样在飞书里调整导航、页面、模块层级时更顺手。

### 指标部分

- 北极星指标
- 过程指标
- 指标漏斗表

## 快速开始

初始化一个案例目录：

```bash
python3 scripts/init_pm_case.py --title "需求标题"
```

如果要生成嵌套目录：

```bash
python3 scripts/init_pm_case.py --title "需求标题" --nested
```

## 飞书发布

本技能不会默认自动发布到飞书。

只有用户明确要求发布时，才会：

1. 运行 `scripts/feishu_preflight.py`
2. 优先确认 Wiki 路径，默认推荐：`知识库 -> 产品部门`
3. 在 `产品部门` 下按产品名创建节点，例如 `产品1`
4. 按 `feishu/manifest.json` 顺序逐篇发布到 `产品1`

发布前会优先检查：

- 飞书 CLI 是否已登录
- 权限与 scopes 是否足够
- 目标路径是否已确认
- 如果是知识库发布，是否已经确认产品部门节点与产品名称
- Mermaid / 表格等核心图形是否适合飞书内继续编辑

## 相关文件

- [SKILL.md](./SKILL.md)
- [references/artifact-structure.md](./references/artifact-structure.md)
- [references/feishu-publishing.md](./references/feishu-publishing.md)
- [subskills/deliver-prd/references/TEMPLATE.md](./subskills/deliver-prd/references/TEMPLATE.md)
- [scripts/init_pm_case.py](./scripts/init_pm_case.py)
