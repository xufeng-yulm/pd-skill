<div align="center">

![pd-skill logo](assets/logo.svg)

# pd-skill

<p><strong>面向 AI 工作流的产品文档系统，用于生成视觉化 PRD、飞书知识库发布、原型 brief 与上线级规划产物。</strong></p>

<p>
  <img src="https://img.shields.io/badge/PRD-18%20Docs-2563EB?style=flat-square" alt="18 doc PRD" />
  <img src="https://img.shields.io/badge/Publishing-Feishu%20Wiki-0F766E?style=flat-square" alt="Feishu Wiki" />
  <img src="https://img.shields.io/badge/Visuals-Mermaid%20Native-7C3AED?style=flat-square" alt="Mermaid Native" />
  <img src="https://img.shields.io/badge/Lens-Jobs%20Product%20Review-F59E0B?style=flat-square" alt="Jobs Lens" />
</p>

<p>
  <a href="./README_EN.md">English</a> · 中文
</p>

<p>
  <a href="#概览">概览</a> ·
  <a href="#产出内容">产出内容</a> ·
  <a href="#工作流">工作流</a> ·
  <a href="#快速开始">快速开始</a> ·
  <a href="#飞书发布">飞书发布</a>
</p>

![pd-skill banner](assets/banner.svg)

</div>

---

## 概览

`pd-skill` 不是一个只会吐出单篇 PRD 的提示词，而是一套完整的产品交付系统。它会把一句产品需求推进为一组结构化产物，包括：

- 需求分析
- Jobs 风格产品判断
- 多文档 PRD
- 可编辑的视觉图表
- 原型 brief 与原型交接
- 飞书知识库发布
- deck 大纲与运营 brief

默认输出面向真实评审场景，而不是单纯把信息塞进 Markdown。文档结构会尽量让产品、设计、研发、运营、管理层都能在同一套产物里读到自己关心的部分，而不需要二次翻译。

## 为什么做这个

大多数 AI 生成的 PRD 都有同一类问题：

- 太短
- 太泛
- 把战略、体验、执行混成一篇
- 看上去完整，但并不适合评审
- 发布到飞书后，图表变成静态内容，后续很难继续编辑

`pd-skill` 用下面的约束来解决这些问题：

1. 强制头脑风暴
2. 强制 Jobs 产品判断层
3. 强制多文档拆分
4. 强制优先可编辑视觉结构
5. 强制明确飞书知识库发布规则

## 产出内容

### 核心分析

| 产物 | 作用 |
| --- | --- |
| `analysis/01-brainstorm.md` | 问题澄清、假设、备选方案、推荐方案 |
| `analysis/02-jobs-product-lens.md` | 一句话定义、聚焦决策、体验原则、应该砍掉什么 |

### PRD 系统

PRD 默认拆成 18 篇文档，每篇面向明确主题，避免一篇文档又长又散：

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

### 配套交付

| 目录 | 作用 |
| --- | --- |
| `prototype/` | 原型 brief、页面流、覆盖清单 |
| `deck/` | 汇报 deck 大纲与 JSON 结构 |
| `ops/` | 运营 brief 与创意矩阵 |
| `feishu/` | manifest、发布计划、发布结果 |

## 设计标准

这套技能输出的 PRD，目标是比普通 Markdown 文档更像正式项目交付物。

### 视觉语言

- Mermaid 优先图表
- 摘要卡与评审看板
- 对比矩阵
- 里程碑泳道
- 信息层级表
- 带说明的截图 / 参考图位

### 飞书优先原则

核心图表在发布后必须仍然可编辑。默认优先级为：

1. `Mermaid`
2. Markdown 表格
3. 编号结构块

静态图片只能作为补充材料，不能承载核心结构。这也是为什么架构、旅程、漏斗、信息架构不应该依赖 `SVG`、`PNG` 或截图本身。

## 工作流

```mermaid
flowchart LR
    A["用户需求"] --> B["初始化工作区"]
    B --> C["头脑风暴"]
    C --> D["Jobs 产品判断"]
    D --> E["18 篇 PRD 生成"]
    E --> F["是否发布到飞书"]
    F --> G["原型 brief / 原型"]
    G --> H["Deck + 运营产物"]
```

### 标准执行顺序

1. 初始化工作目录
2. 生成 brainstorm 文档
3. 生成 Jobs 判断文档
4. 生成多文档 PRD
5. 询问是否发布到飞书
6. 如需要，发布到知识库或云盘
7. 继续原型 / deck / ops 产物

## 差异点

| 维度 | 常见 PRD prompt | `pd-skill` |
| --- | --- | --- |
| 作用域 | 单篇 markdown | 18 篇文档系统 |
| 产品判断 | 通常没有 | 明确的 Jobs 风格过滤层 |
| 视觉质量 | 以文字为主 | 图表、表格、评审卡、图片位 |
| 飞书发布 | 临时组织 | 明确的知识库路径规则 |
| 发布后可编辑性 | 常常较差 | 优先飞书原生可编辑结构 |
| 交接质量 | 通用描述 | 面向产品 / 设计 / 研发 / 运营拆分 |

## 输出目录示例

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
│   ├── ...
│   └── 18-appendix-and-assets.md
├── prototype/
├── deck/
├── ops/
└── feishu/
```

## 快速开始

在当前项目下创建一个产品案例目录：

```bash
python3 scripts/init_pm_case.py --title "需求标题"
```

如果要生成嵌套目录：

```bash
python3 scripts/init_pm_case.py --title "需求标题" --nested
```

## 飞书发布

默认不会自动发布到飞书。只有在用户明确要求后才进入发布流程。

### 默认知识库结构

推荐路径：

```text
知识库 -> 产品部门 -> 产品名
```

例如：

```text
知识库 -> 产品部门 -> 产品1
```

然后把完整的多文档 PRD 全部写入 `产品1` 节点下。

### 发布流程

1. 运行 `scripts/feishu_preflight.py`
2. 确认知识库路径，通常是 `知识库 -> 产品部门`
3. 定位 `产品部门` 节点
4. 在其下创建产品节点，例如 `产品1`
5. 将 `feishu/manifest.json` 中的所有 PRD 文档逐篇写入该节点

### 发布前检查

- 飞书 CLI 可用
- 登录与 scopes 有效
- 知识库路径已确认
- 产品部门节点已确认
- 产品名称已确认
- 核心图表发布后仍然可编辑

## 能力矩阵

| 能力 | 是否包含 |
| --- | --- |
| Brainstorming | Yes |
| Jobs 风格产品复盘 | Yes |
| 视觉化 PRD 结构 | Yes |
| 可编辑 Mermaid 图表 | Yes |
| 飞书知识库发布 | Yes |
| 原型 brief | Yes |
| Deck 输出 | Yes |
| 运营 brief | Yes |

## 仓库结构

| 路径 | 作用 |
| --- | --- |
| [SKILL.md](./SKILL.md) | 总控编排契约 |
| [references/artifact-structure.md](./references/artifact-structure.md) | 输出目录与最低交付结构 |
| [references/feishu-publishing.md](./references/feishu-publishing.md) | 飞书发布流程 |
| [subskills/deliver-prd/references/TEMPLATE.md](./subskills/deliver-prd/references/TEMPLATE.md) | PRD 模板参考 |
| [scripts/init_pm_case.py](./scripts/init_pm_case.py) | 工作区骨架生成脚本 |

## 说明

- 整套 PRD 设计得足够厚，是为了更像真实内部项目文档，而不是提示词堆出来的摘要。
- 视觉丰富度服从可编辑性，飞书原生结构优先于静态好看图。
- 允许插入图片，但图片必须带说明，且整体结构不能依赖图片本身。
