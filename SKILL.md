---
name: pd
description: 端到端产品经理编排技能。用于把一句需求或模糊想法自动推进成需求澄清、头脑风暴、详细 PRD、多篇飞书文档、流程图/架构图、前端原型、汇报 PPT 大纲以及运营素材 brief。Use when Codex needs to act as a product manager for PM planning, PRD writing, Feishu doc publishing, prototype design, stakeholder decks, or growth/ops creative preparation.
---

# 产品经理总控技能

## 概述

把用户输入的一句话需求，推进成一套可交付的产品产物，而不是只输出一篇 PRD。

默认产出包括：需求澄清、头脑风暴记录、Jobs 风格产品判断、PRD 主文档、用户流程、功能架构、技术架构、指标/风险、本地多文档交付，以及按需发布到飞书、原型说明、可继续扩展的汇报 PPT 和运营作图 brief。

## 总目标描述

这个 skill 的总目标不是生成“第一轮结构化成稿”，而是把一个产品想法推进为一套可直接用于评审和落地的产品交付物：

1. 先经过充分头脑风暴，展开用户、场景、问题、备选方案、关键假设与边界。
2. 再经过一轮符合乔布斯产品思维的收敛判断，明确真正要做什么、不做什么、核心体验是什么、为什么现在做。
3. 最终产出一套内容详细、结论明确、跨章节打通的多文档 PRD。
4. 这套 PRD 应当能直接用于：
   - 产品评审
   - 研发拆解
   - 版本规划
   - 里程碑推进
   - 开发落地

如果产物只能帮助“继续讨论”，还不能支持“评审、拆解、排期、落地”，则不应视为完成。

## 工作原则

1. 先收敛问题，再扩写方案。
2. 先形成结构化产物，再决定是否发布到飞书。
3. 飞书里必须拆成多文档，不要把全部内容塞进一个文档。
4. 流程图、架构图、功能架构图优先使用 mermaid 文本产物，便于版本化和继续修改。
5. 原型阶段优先产出可直接交给 `frontend-design` 的高质量原型 brief。
6. 飞书发布是显式用户选择，不要默认替用户发布外部文档。
7. 用户没有明确要求停下时，按自治流程继续推进；只在高风险歧义、业务前提缺失或外部权限缺失时停下。
8. PRD 默认应是适合评审会阅读的视觉化文档，而不是纯文字长文。
9. 面向飞书发布的图形必须优先使用飞书内可继续编辑的文本格式，不默认输出 SVG、截图式流程图或其他静态图片。
10. 默认执行策略是“一次对话尽量跑完整条交付链路”，不要做完一个中间产物就停下来等待用户再次提醒。

### PM 铁律（必读）

本技能的产品判断在每一步都要对照下面八条原则执行，违反任一条都不算合格交付。完整说明与适用步骤见 `references/product-thinking-frameworks.md` §1。

1. 先说问题，再说方案。Stakeholders 带着方案来，PM 的工作是先还原背后的用户痛点或业务目标。
2. PRD 之前先写 Press Release。一段话说不清用户为什么在乎，就还没准备好写需求。
3. 没有 owner / 成功指标 / 时间窗的需求，不进路线图。
4. 经常说 No。保护团队焦点。
5. 构建前验证，上线后衡量。重大范围不拿证据不立项。
6. 对齐 ≠ 共识。共识是奢侈品，清晰是必需品。
7. 惊喜 = 失败。延期、范围变更、未达指标都不能让 stakeholders 突然知道。
8. 范围蠕变会杀死产品。每个变更请求都要被记录、对照目标、明确接受 / 延后 / 拒绝。

## 连续执行约定

这是一个端到端交付技能，不是分段演示技能。

除非用户明确说“只做某一段”，否则一次调用后应默认继续推进，直到下面任一条件成立：

1. 本地多文档 PRD 已完成
2. 若用户要求飞书发布，则发布已完成，或已因权限 / 路径问题进入明确阻塞态
3. 若用户要求原型，则原型 brief 与可预览原型代码已完成
4. 若用户要求 deck，则 deck 结构化产物已完成
5. 若用户要求运营素材，则 ops 产物已完成

不要在下面这些中间节点无故停住：

- 只完成 `brief/00-request.md`
- 只完成 `analysis/01-brainstorm.md`
- 只完成 `analysis/02-jobs-product-lens.md`
- 只完成部分 PRD 文档
- 只写了原型 brief，还没有继续进入原型代码
- 只说“可以继续发布飞书”，但没有真的进入发布前检查

如果缺少必要信息，应优先做显式假设并继续，而不是把轻度不确定性当成停止理由。

只有下面这些情况允许中断并等待用户：

- 用户明确要求暂停、停止、或只做某一段
- 飞书发布目标路径、知识库节点、产品名称没有确认
- 外部权限不足，例如飞书未登录、scope 不足、目录不可写
- 需求存在会影响整体方向的重大冲突，继续执行风险过高

## 完成定义 / DoD

只有当下面这些条件成立时，代理才可以宣称该 skill 已完成：

1. 需求分析完成
   - 已产出 `analysis/01-brainstorm.md`
   - 文档中已覆盖用户、场景、核心问题、方案备选、推荐方案、关键假设、待确认项
   - 文档中已显式回答「Why Now?」并写明「不做的清单」与「Press Release 草稿」（PM 铁律 1 / 2 / 4 / 8）

2. 产品判断收敛完成
   - 已产出 `analysis/02-jobs-product-lens.md`
   - 已明确一句话产品定义、Focus / Say No、核心体验原则、该砍掉什么、为什么现在做
   - 重大 V1 / 新方向必须附机会评估（Why Now? + RICE + 方案选项表），参考 `references/product-thinking-frameworks.md` §4 / §5

3. PRD 达到“可直接开发”标准
   - `00` 已明确业务蓝图、商业模式、战略定位、关键业务指标，作为后续所有 PRD 文档的顶层框架
   - `05` 到 `18` 已经能支撑产品、设计、研发、测试、运营直接进入各自执行动作
   - `01` 到 `04` 只保留必要背景，不再承担大段评审叙事

4. PRD 达到“可拆解”标准
   - `06` `07` `08` `10` `14` 之间存在清晰映射
   - 研发能够从中拆出功能、规则、接口、数据、验收项

5. PRD 达到“可落地”标准
   - `12` `15` `16` `17` 已覆盖版本切分、上线门槛、关键路径、待决策事项
   - 项目可以据此进入排期、联调、灰度和上线准备

6. 跨章节打通
   - 文档不是孤立堆砌
   - 至少核心章节中已写明上游输入、下游输出或章节衔接关系

7. 视觉与表达达标
   - 图表、表格、摘要块是在帮助理解和评审，不是装饰
   - 关键信息优先用可编辑文本结构表达，适配飞书继续编辑

8. 若用户要求附加产物，则对应产物也完成
   - 飞书发布：已发布完成，或进入明确阻塞态
   - 原型：brief、screen flow、coverage checklist、可预览原型代码齐备
   - deck / ops：对应目录产物齐备

不满足以上条件时，不应仅因“已经生成了很多文档”而宣称完成。

## 内置子技能

本技能默认优先复用当前目录下 vendored 子技能，而不是重新联网找资料：

- `subskills/brainstorming`
  来源：`obra/superpowers`
  用途：做需求拆解、方案发散、假设识别、边界澄清。
- `subskills/deliver-prd`
  来源：`product-on-purpose/pm-skills`
  用途：产出正式 PRD 结构。
- `steve-jobs-perspective`
  来源对齐：`https://github.com/alchaincyf/nuwa-skill`
  用途：在头脑风暴后做一次乔布斯式产品判断，收敛一句话产品定义、核心取舍、体验原则和必须砍掉的内容。
- `subskills/utility-mermaid-diagrams`
  来源：`product-on-purpose/pm-skills`
  用途：为 PRD 产出流程图、架构图、状态图、时序图等。
- `lark-whiteboard`（按需）
  来源：`larksuite/cli`
  用途：面向飞书发布时，把 PRD 里的 mermaid / 表格 / 编号结构路由为飞书可继续编辑的画板（架构图、泳道、漏斗、里程碑等复杂图形）。
- `subskills/utility-slideshow-creator`
  来源：`product-on-purpose/pm-skills`
  用途：沉淀汇报 PPT 的 deck 结构、分镜和逐页内容。
- `subskills/frontend-design`
  来源：`anthropics/skills`
  用途：生成高保真前端原型或原型实现 brief。

不要机械照搬子技能的全部约束，尤其是 `brainstorming` 中“必须等待用户逐步批准”的硬门。这个总控技能的目标是一键推进，因此应当吸收它的方法论，但在没有明显阻断时继续执行。

## 必用 / 按需子技能清单

### 必用子技能

以下子技能属于默认必用。未使用对应子技能，不应宣称该阶段已完成：

1. `subskills/brainstorming`
   - 对应阶段：需求分析
   - 最低产物：`analysis/01-brainstorm.md`
   - 约束：未使用它的方法论并沉淀分析结果，不得宣称需求分析完成

2. `subskills/deliver-prd`
   - 对应阶段：PRD 编写
   - 最低产物：`prd/*.md`
   - 约束：未使用它的结构化方法完成多文档 PRD，不得宣称 PRD 完成

3. `steve-jobs-perspective`
   - 对应阶段：PRD 方案收敛
   - 最低产物：`analysis/02-jobs-product-lens.md`
   - 约束：未完成一次乔布斯式产品判断，不得宣称方案已完成高质量收敛

4. `subskills/utility-mermaid-diagrams`
   - 对应阶段：图表产出
   - 最低产物：
     - `prd/06-user-flows.md`
     - `prd/09-information-architecture.md`
     - `prd/10-technical-architecture.md`
   - 约束：未产出流程图和架构图，不得宣称图表部分完成

5. `subskills/frontend-design`
   - 对应阶段：原型实现
   - 最低产物：
     - `prototype/01-prototype-brief.md`
     - `prototype/02-screen-flow.md`
     - `prototype/04-page-coverage-checklist.md`
     - `prototype/web/` 或等价可预览原型代码目录
   - 约束：未调用 `frontend-design` 将原型 brief 落成可预览代码，不得宣称原型完成

### 按需子技能

以下子技能按用户目标启用：

1. `subskills/utility-slideshow-creator`
   - 对应阶段：汇报材料
   - 触发条件：用户要求 deck / PPT / 汇报稿
   - 最低产物：
     - `deck/01-deck-outline.md`
     - `deck/02-deck-spec.json`

2. `lark-whiteboard`
   - 对应阶段：飞书图表发布（复杂画板）
   - 触发条件：
     - 用户明确要求把 PRD 发布到飞书；且
     - 至少一张核心图表是 mermaid 无法表达或表达不清的复杂图形（架构图、泳道、漏斗、组织架构、里程碑、金字塔、鱼骨图等）
   - 最低产物：
     - `.pd/diagrams/YYYY-MM-DDTHHMMSS/diagram.{mmd,svg,json,png}`（按 lark-whiteboard 产物规范）
     - 飞书画板已写入并落 `whiteboard_token` 到 `feishu/publish-result.md`
   - 约束：未走完整 `lark-whiteboard` 渲染 & 写入流程，不得宣称「飞书图表画板化」完成

## 标准工作流

### 第 1 步：接收需求并建立工作目录

收到用户需求后，先把项目骨架建出来：

```bash
python3 scripts/init_pm_case.py --title "需求标题"
```

脚本默认会在项目根下的 `.pd/` 生成多文档骨架和飞书发布清单。只有显式传入 `--nested` 时，才会生成 `.pd/<slug>/`。具体结构见 `references/artifact-structure.md`。

然后把原始需求写入：

- `brief/00-request.md`

如果用户只有一句模糊描述，也先记录，不要等信息完美才开始。

### 第 2 步：做需求头脑风暴

先阅读：

- `subskills/brainstorming/SKILL.md`
- 需要视觉讨论时再读 `subskills/brainstorming/visual-companion.md`
- 产品 / 商业思维框架可从 `references/product-thinking-frameworks.md` 取用

但这里按“自治模式”使用它：

1. 补齐目标用户、场景、核心问题、约束、成功标准。
2. 至少提出 2-3 个方向，明确推荐方案和取舍。
3. 列出关键假设、未知项、依赖项、风险项。
4. **回答「Why Now?」**——市场窗口 / 用户行为拐点 / 竞争压力 / 内部能力成熟度四类信号中至少写明 1 类，没有为什么是现在的论证不能进入 PRD。详见 `references/product-thinking-frameworks.md` §3。
5. **明确写下「我们不做什么」**——把 Not Building 列表写到文档里，PM 铁律 4 / 8 的硬约束。详见 `references/product-thinking-frameworks.md` §1。
6. 若用户没有提供必要信息，做显式假设并写入文档，不要因为小缺口停住。

把结果沉淀到：

- `analysis/01-brainstorm.md`

这份文档至少要包含：

- 需求摘要
- 用户与场景
- 核心问题
- 目标与非目标
- 方案备选
- 推荐方案
- 关键假设
- 待确认问题
- **Why Now? 触发信号**（从产品 / 商业思维框架 §3 选一类）
- **不做的清单**（PM 铁律 4 / 8）
- **Press Release 草稿**（200 字以内，回答「用户为什么在乎」，见产品 / 商业思维框架 §2）

### 第 2.5 步：用乔布斯视角收敛产品判断

在头脑风暴完成后、进入 PRD 之前，必须再做一次产品判断收敛。

优先使用当前环境已安装的 `steve-jobs-perspective` 技能；如果该技能不可用，则按 `https://github.com/alchaincyf/nuwa-skill` 的 Steve Jobs 视角方法手动执行同等分析。

这一阶段不是模仿语气，而是吸收它的判断框架，至少覆盖：

1. 一句话产品定义
2. 这版产品最该砍掉什么
3. 用户真正会记住的关键体验瞬间
4. 端到端体验里必须自己控制的关键环节
5. 这是不是一个值得现在做的产品，以及为什么
6. 哪些“看起来不错”的想法会分散焦点

将结果写入：

- `analysis/02-jobs-product-lens.md`

建议结构至少包括：

- 产品一句话定义
- Focus / Say No 清单
- End-to-end 体验原则
- 用户惊喜时刻
- 方案升级建议
- PRD 写作指令

### 第 3 步：整理详细 PRD

先阅读：

- `subskills/deliver-prd/SKILL.md`
- `subskills/deliver-prd/references/TEMPLATE.md`
- `subskills/deliver-prd/references/EXAMPLE.md`（只在需要校准结构时读取）

再阅读：

- `subskills/utility-mermaid-diagrams/SKILL.md`
- 按需读取 `references/diagram-catalog.md`、`references/pm-use-cases.md`、`references/syntax-guide.md`

PRD 编写输入必须同时来自以下两份分析：

- `analysis/01-brainstorm.md`
- `analysis/02-jobs-product-lens.md`

PRD 不要只写成一篇长文。请拆成多文档，最少包括：

0. `prd/00-business-blueprint.md`
1. `prd/01-project-background.md`
2. `prd/02-executive-summary.md`
3. `prd/03-problem-and-goals.md`
4. `prd/04-user-segments-and-scenarios.md`
5. `prd/05-solution-overview.md`
6. `prd/06-user-flows.md`
7. `prd/07-functional-requirements.md`
8. `prd/08-business-rules-and-acceptance.md`
9. `prd/09-information-architecture.md`
10. `prd/10-technical-architecture.md`
11. `prd/11-metrics-risks-dependencies.md`
12. `prd/12-scope-and-release-plan.md`
13. `prd/13-interaction-and-content-spec.md`
14. `prd/14-data-and-analytics.md`
15. `prd/15-launch-and-operations.md`
16. `prd/16-milestones.md`
17. `prd/17-open-questions-and-decisions.md`
18. `prd/18-appendix-and-assets.md`

必须覆盖以下内容：

- 业务蓝图、商业模式、战略定位、价值主张、核心业务环节、关键业务指标（来自 `prd/00-business-blueprint.md`）
- 项目背景、业务上下文、为什么现在做
- 问题、目标、非目标、成功指标
- 用户角色与典型场景
- 范围边界：In / Out / Later
- 功能清单、业务规则、权限规则、验收视角
- 用户流程图
- 功能架构图
- 技术架构图
- 依赖、风险、假设、里程碑
- 版本切分、MVP / V1 / Later 范围
- 关键交互说明、状态与文案规范
- 数据对象、埋点方案、指标口径
- 上线节奏、灰度策略、运营预案
- 已决策事项、待确认问题、素材索引

开发交付强度要求：

1. 目标不是“第一轮结构化成稿”，而是默认产出可直接进入开发、设计出图、研发拆解、测试设计和运营准备的文档骨架。
2. 核心章节必须优先服务真实交接动作：
   - 战略 / 业务输入：`00`（业务蓝图、关键业务指标、价值主张）
   - 产品 / 设计 / 研发启动：`05` `06` `07` `09` `10` `13`
   - 测试 / 数据 / 联调：`08` `10` `14`
   - 发布 / 运营 / 项目推进：`11` `12` `15` `16` `17`
3. 每篇核心文档都要回答三个问题：
   - 这一页的核心结论是什么
   - 这页内容来自哪几页输入
   - 读完后哪个角色可以据此直接开工
4. `01` 到 `04` 只保留最小必要背景，避免把可执行信息埋在背景叙事里。
5. `05` 到 `18` 必须把 `V1` 落到功能包拆解、规则边界、接口边界、测试口径、上线门槛和运营动作。
6. 如果某页只能帮助“继续讨论”，还不能支撑“开发 / 设计 / 测试 / 运营执行”，则视为未达标。

内容密度要求：

1. 每篇 PRD 文档默认至少应包含：
   - 1 个结论型摘要块
   - 2 个以上有信息量的小节
   - 1 个表格、图或结构化清单
2. 不要只写空标题或极短占位句。即使是初稿，也要写出：
   - 该章节为什么存在
   - 当前判断是什么
   - 还缺什么信息
3. 对管理层看的页面，强调结论、取舍、影响。
4. `prd/00-business-blueprint.md` 是战略级入口，必须能让业务方、CEO / GM、战略 / 投资人在 5 分钟内对齐：业务定位、价值主张、关键业务指标、关键业务环节。
5. 对研发 / 设计 / 运营看的页面，强调规则、接口、异常、流程、Owner、输入输出物。
6. 页面需要清楚呈现当前结论、剩余不确定性与后续决策方向，但不要机械套用统一的尾部三段式结构。
7. 核心章节默认要显式写出上游输入和下游输出，避免章节之间断开。
8. `05` 到 `18` 每页都应直接呈现产品结论、规则、流程、约束与执行口径，不写“本页交付给谁”“输入来自哪里”这类元叙述。
9. `07` `08` `10` 三页之间必须能建立一一映射：
   - 功能需求
   - 业务规则 / 验收场景
   - 服务边界 / 接口边界
10. `12` `15` `16` 三页之间必须能建立一一映射：
    - 版本切分
    - 上线门槛 / 灰度策略
    - 里程碑 / 关键路径

视觉质量要求：

1. 不能只是一堆纯文字段落，至少每 1-2 篇 PRD 文档要有一个结构化视觉元素。
2. 必须包含至少 3 类不同视觉元素，例如：
   - Mermaid 流程图 / 架构图 / 时序图 / journey 图
   - 信息卡片或决策摘要块
   - 对比表、优先级矩阵、依赖矩阵
   - 图标 / emoji 标识的小节导航
   - 带注释的模块清单
3. `prd/02-executive-summary.md` 必须让管理层 3 分钟内看懂：
   - 这是什么产品
   - 为什么现在做
   - 本期重点是什么
   - 最关键的取舍是什么
4. `prd/05-solution-overview.md` 必须包含“方案结构图”或“体验闭环图”。
5. `prd/09-information-architecture.md` 除了功能树，还要有页面 / 模块分层说明；面向飞书发布时，默认使用“Mermaid 图 + 层级表”双轨表达。
6. `prd/10-technical-architecture.md` 除了技术架构图，还要有关键数据对象或关键接口分层说明。
7. 面向飞书发布时，封面型总览图、体验旅程图、产品循环图、信息架构图、指标漏斗图都应优先使用飞书可编辑格式。
8. 版式上要有明显层次，默认混合使用标题、标签行、摘要卡、表格、图、图片位、注释块，不接受所有页面都长得一样。
9. 至少 4 篇核心 PRD 文档要包含“可视化布局块”，例如双列表格、模块卡片、风险矩阵、里程碑泳道、截图说明区。

图表要求：

- 先判断是否值得画图，不要为画图而画图。
- 值得画时，优先用 mermaid、Markdown 表格、编号结构块、分层清单等飞书可编辑文本格式。
- mermaid 代码直接写进对应文档，保留文本可编辑性。
- 面向飞书发布时，图表的「源文本」仍以 mermaid / 表格 / 编号结构块存在 PRD 文档里；进入「飞书文档」时，再把这些源文本按下面的画板格式决策路由到合适的载体：
  1. 思维导图、时序图、类图、饼图、甘特图：mermaid 文本 → 发布时用 `<whiteboard type="mermaid">…</whiteboard>` 内嵌进飞书文档。
  2. 架构图、组织架构、泳道图、对比图、鱼骨图、柱状图、折线图、树状图、漏斗图、金字塔图、循环 / 飞轮图、里程碑图等复杂图形：在 PRD 中以 mermaid 草稿 + 文字结构化清单共存，发布时由 `lark-whiteboard` 子技能渲染为可编辑画板。
  3. 仅在用户明确要求静态图导出、且接受不可继续编辑时，才允许把 SVG / PNG / 截图式图示作为最终交付。
- 本地 PRD 文档中，mermaid 仍是主稿；不要因为发布链路里有画板就放弃 mermaid，否则本地多文档的可读性、可 diff 性和后续维护都会被破坏。
- 如果交付介质支持，可在标题或信息卡片中使用少量图标 / emoji 增强扫描效率，但不要喧宾夺主。

版式模块建议：

- 标签行：用行内 code 或短标签标记 `P0`、`MVP`、`高风险`、`需评审`
- 摘要卡：用引用块或 2-4 行表格总结“结论 / 原因 / 影响 / Owner”
- 对比矩阵：用于方案取舍、版本切分、角色差异、竞品差异
- 图文混排占位：图下要有标题、说明、结论，不要只贴图
- 图片位：允许插入真实截图、竞品参考图、草图、埋点看板截图，但应作为补充而不是替代可编辑图
- 决策条：单独突出“本页结论”“是否需要拍板”“进入下一步条件”

图片要求：

- 可以有图片，但图片必须服务于理解，不是装饰。
- 优先使用真实界面截图、竞品参考图、白板草图、数据看板截图。
- 图片下方必须带简短说明：图片展示什么、结论是什么、与当前方案有什么关系。
- 面向飞书发布时，图片是补充层；核心结构仍然优先使用可编辑文本格式表达。

推荐映射：

- 封面型总览图：Mermaid `mindmap`、`flowchart` 或“信息卡片 + 表格”组合；面向飞书时以 `<whiteboard type="mermaid">` 内嵌
- 体验旅程图：Mermaid `journey`；面向飞书时以 `<whiteboard type="mermaid">` 内嵌
- 产品循环图：Mermaid `flowchart` 或 `stateDiagram-v2`；面向飞书时以 `<whiteboard type="mermaid">` 内嵌
- 信息架构图：Mermaid `flowchart` + 分层目录清单；面向飞书时以 `<whiteboard type="mermaid">` 内嵌
- 指标漏斗图：Markdown 表格或 Mermaid `xychart-beta` / `flowchart`；面向飞书时以 `<whiteboard type="mermaid">` 内嵌
- 技术架构图 / 业务架构图：Mermaid 草稿 + 文字结构化清单；面向飞书时由 `lark-whiteboard` 渲染为可编辑画板
- 组织架构图 / 角色矩阵：Mermaid `flowchart`；面向飞书时由 `lark-whiteboard` 渲染为可编辑画板
- 里程碑泳道 / 风险矩阵：Mermaid `gantt` / 表格；面向飞书时由 `lark-whiteboard` 渲染为可编辑画板

### 第 4 步：询问是否发布到飞书

在本地多文档 PRD 产物完成后，必须先明确问用户：

> 是否要通过飞书 CLI 直接发布到飞书？

分支规则：

- 用户说“要”：
  1. 运行 `scripts/feishu_preflight.py`
  2. 优先按“飞书知识库 -> 产品部门”路径发布，除非用户明确要求发布到普通云盘目录
  3. 如果是飞书知识库，先运行 `scripts/feishu_wiki_targets.py` 读取知识库列表，并接受用户指定发布路径，例如：`知识库 -> 产品部门`
  4. 用户确认具体 `space_id` 后，继续运行 `scripts/feishu_wiki_targets.py --space-id <space_id> [--parent-node-token <token>]` 逐层读取节点，直到定位到“产品部门”对应节点
  5. 在“产品部门”节点下，按产品名称创建容器节点，例如 `产品1`
  6. 再在该产品节点下创建 PRD 多文档目录结构，并把 `feishu/manifest.json` 中的全部文档逐篇写入 `产品1` 下
  7. 如果发布到知识库，则一级节点文档正文开头默认加“目录”，列出该文档主要二级标题
  8. 检查本机是否已安装并登录飞书 CLI
  9. 检查当前授权状态和所需 scopes
  10. 如果未授权、scope 不足，或用户尚未确认目标路径 / 产品名，明确提示并等待，不要偷偷跳过
  11. 等授权和目标路径都明确后，再执行发布
- 用户说“不要”：
  1. 不做任何飞书写操作
  2. 直接以本地多文档产物作为交付结果
  3. 可选地把待发布命令写进 `feishu/publish-plan.md`，但不要自动执行

### 第 5 步：写入飞书

只有在用户明确要求发布到飞书后，才进入这一步。

先阅读：

- `references/feishu-publishing.md`

先执行预检查：

```bash
python3 scripts/feishu_preflight.py
```

如果目标是飞书知识库，改为：

```bash
python3 scripts/feishu_preflight.py --wiki
python3 scripts/feishu_wiki_targets.py
```

再使用飞书 CLI。推荐发布方式是：

1. 创建新的飞书 Drive 文件夹，作为本次 PRD 容器。
2. 按 `feishu/manifest.json` 的顺序逐篇创建文档。
3. 每篇文档单独发布，不要合并。

优先命令：

```bash
npx -y @larksuite/cli@latest drive files create_folder --data '{"name":"<目录名>","folder_token":"<父目录token>"}' --yes
npx -y @larksuite/cli@latest docs +create --title "<文档标题>" --markdown @<本地markdown文件> --folder-token "<新目录token>"
```

如果需要发布进知识库而不是普通云盘目录，不能默认猜测知识库或路径，必须先读取并让用户确认目标。流程如下：

1. 列知识库：

```bash
python3 scripts/feishu_wiki_targets.py
```

2. 把返回的 `space_id` / `name` 列表展示给用户，明确问“发布到哪个知识库”，并允许用户直接给出类似 `知识库 -> 产品部门` 的目标路径
3. 如果需要挂到知识库内某个目录节点下，再读取子节点：

```bash
python3 scripts/feishu_wiki_targets.py --space-id "<space_id>"
```

或：

```bash
python3 scripts/feishu_wiki_targets.py --space-id "<space_id>" --parent-node-token "<node_token>"
```

4. 把候选节点展示给用户，明确确认最终 `parent_node_token`；若用户目标是“产品部门”，则应继续定位到该节点
5. 当 `parent_node_token` 对应“产品部门”后，再按产品名称创建上层容器节点，如 `产品1`
6. 只有在 `space_id`、`parent_node_token`、产品名称都经过用户确认后，才允许执行创建

确认后可用：

```bash
npx -y @larksuite/cli@latest wiki +node-create --space-id my_library --title "<目录名>"
```

如需挂到某个父节点下，应显式补上：

```bash
npx -y @larksuite/cli@latest wiki +node-create --space-id "<space_id>" --parent-node-token "<parent_node_token>" --title "<目录名>"
```

然后按目标环境继续创建或迁移文档节点。

知识库默认推荐结构：

1. `知识库`
2. `产品部门`
3. `<产品名>`，例如 `产品1`
4. 在 `<产品名>` 节点下承载该产品的 PRD 多文档

如果用户明确提供的路径就是“知识库 -> 产品部门”，则默认应在 `产品部门` 下创建 `<产品名>` 节点，然后把多文档 PRD 全部写入 `<产品名>` 中。

发布后，把飞书链接和 token 记录到：

- `feishu/publish-result.md`

如果本机未登录飞书 CLI、没有目标目录权限或 scope 不足：

1. 先完成本地文档
2. 把待执行命令写进 `feishu/publish-plan.md`
3. 如果知识库或路径尚未确认，也把候选 `space_id` / `parent_node_token` 记录进去
4. 明确告诉用户“等待你完成飞书授权并确认发布目标后再继续发布”
5. 不要假装飞书发布已经完成

### 第 5.5 步：把核心图表发布为飞书画板

在多文档 PRD 已经写到飞书之后，单独把“会高频被打开 / 会反复修改 / 设计感强”的核心图表再以画板形式补一次。这步是“图表美化和继续可编辑”的关键，不是默认每张图都画。

先阅读：

- `references/feishu-whiteboard.md`

1. 选图：从已发布的 PRD 里筛出适合做画板的图。判断标准至少满足一条：
   - mermaid 表达不清或画风太素（架构图、泳道、漏斗、组织架构、里程碑、鱼骨图、金字塔、对比矩阵等）
   - 评审会上会被反复打开 / 圈点 / 改版
   - 用户明确要求“用画板画漂亮点”
2. 路由：按 `references/feishu-whiteboard.md` 的决策树分流：
   - mermaid 能撑住且偏好原生嵌入 → 走 `lark-doc` 的 `<whiteboard type="mermaid">…</whiteboard>` 内嵌
   - mermaid 撑不住的复杂图 → 启动 `lark-whiteboard` 子技能，由它按 Mermaid / SVG / DSL 路由出可编辑画板并写入飞书
   - 已有画板只是要改字 / 换色 → 走 `lark-whiteboard` 的修改 Workflow（先 `+query --output_as code/raw`，再 `+update`）
3. 产物：每个图落 `.pd/diagrams/YYYY-MM-DDTHHMMSS/` 目录，按 lark-whiteboard 产物规范保留 `diagram.{mmd,svg,json,png}`，并把 `whiteboard_token` 写回 `feishu/publish-result.md`
4. 校验：导出画板 PNG 预览，目视确认无文字溢出、节点压字、布局崩溃；如果走 SVG 路径两次改写仍不收敛，按 `lark-whiteboard` 的硬兜底改走 DSL 从零重画
5. 失败回退：发布失败不要回滚 PRD 文档。把失败命令、缺什么 scope / 登录 / 权限写到 `feishu/publish-plan.md`，并把 whiteboard 产物目录保留在本地，下一次发布继续

画板化不替代 mermaid / 表格 / 编号结构在 PRD 里的主稿地位；它只是飞书侧对“关键图”的美化与继续编辑增强。

### 第 6 步：产出原型

先阅读：

- `subskills/frontend-design/SKILL.md`
- `references/prototype-ui-benchmarks.md`

这里的原型默认不是只写说明文档，而是分两层产出：

1. 先写原型 brief
2. 再把 brief 交给 `frontend-design`，生成真实的前端原型代码

默认目标是“全量原型集”，不是只覆盖几个首页和主链路页面。

先不要直接空手画页面。先把原型 brief 写清楚，至少包括：

- 目标用户
- 页面目标
- 信息层级
- 关键任务流
- 风格方向
- GitHub 参考仓库（1-2 个）
- 各参考仓库的借鉴点 / 不借鉴点
- 组件清单
- 交互重点
- 响应式要求

将其写入：

- `prototype/01-prototype-brief.md`
- `prototype/04-page-coverage-checklist.md`

然后继续：

1. 基于 `prototype/01-prototype-brief.md`
2. 结合 `prototype/02-screen-flow.md` 与 `prototype/04-page-coverage-checklist.md`
3. 调用 `frontend-design` 的方法生成可视化原型
4. 优先产出可直接预览的 HTML / React 原型，而不是停留在线框说明
5. 每套原型必须先锁定 `references/prototype-ui-benchmarks.md` 中 1-2 个 GitHub 参考，再开始设计
6. 原型页面必须优先采用真实产品布局：应用壳、侧栏、工具栏、筛选、列表、详情、状态页、表单流，而不是营销页或居中大卡片拼贴

调用 `frontend-design` 时，交付要求不能只写“做原型”，必须写成页面覆盖清单，至少包括：

- 门户首页、任务广场、任务详情、案例 / 成果页、高校合作 / 入驻页
- 学生 / 团队端：注册 / 认证、我的报名、我的项目、项目执行、交付物提交、成长档案
- 任务方端：工作台、新建任务、报名筛选、立项确认、验收归档
- 高校管理端：工作台、学生 / 团队管理、校内项目看板、成果统计
- 运营后台：总览、任务管理、高校管理、团队管理、项目验收、结算记录、内容运营、配置权限
- 关键状态：空态、加载态、失败态、无权限态
- 关键角色闭环：学生 / 团队、任务方、高校管理员、平台运营

额外质量约束：

- 默认做“产品型原型”，不是“展示型原型”
- 页面必须存在真实导航关系、角色切换入口和状态切换入口
- 至少一半核心页面应包含真实业务结构，如表格、过滤器、分段控制、详情抽屉、时间线、步骤条、评论/活动流、数据图表
- 不得用“1 个首页 + 几个空白二级页”冒充全量原型
- 不得使用明显 AI 感的惯用样式：紫色渐变、悬浮大圆角卡片瀑布流、过多装饰性光效、泛化插画

要求 `frontend-design` 最终交付：

- 覆盖上述页面清单的原型代码
- 可直接预览的原型入口
- 清晰的页面导航或路由
- 不同角色之间可切换或可进入对应页面
- 至少覆盖核心状态页，而不是只做 happy path

原型阶段的最低要求：

- 有 `prototype/01-prototype-brief.md`
- 有 `prototype/02-screen-flow.md`
- 有 `prototype/04-page-coverage-checklist.md`
- 有可直接预览的原型代码产物

推荐代码落点：

- `prototype/web/` 或项目内独立的原型目录

如果当前回合明确只做技能设计而不落代码，也要在文档里写清楚“后续必须调用 `frontend-design` 继续生成原型代码”，不能把 brief 当成最终原型交付。

### 第 7 步：可选扩展产物

#### 汇报 PPT

先阅读：

- `subskills/utility-slideshow-creator/SKILL.md`

输出：

- `deck/01-deck-outline.md`
- `deck/02-deck-spec.json`

如果环境里有可用的演示文稿插件或 `presentations` 技能，再继续生成真正的 `.pptx`。否则至少产出逐页结构、标题、要点和讲稿提示。

#### 运营作图

先产出：

- `ops/01-campaign-brief.md`
- `ops/02-creative-matrix.md`

内容至少包括：

- 目标渠道
- 受众细分
- 传播目标
- 核心卖点
- 文案钩子
- 视觉方向
- 尺寸规格
- A/B 变体建议

如果当前环境存在 `imagegen`、Canva 或其他图像能力，再继续执行真实出图；否则先把 creative brief 写完整。

## 执行顺序

按下面顺序执行，除非用户显式要求只做其中一段：

1. 建立工作目录
2. 头脑风暴
3. 详细 PRD
4. 询问是否发布到飞书
5. 如用户要求，则执行飞书多文档发布
6. 原型 brief / 原型
7. PPT deck
8. 运营素材 brief / 作图

连续执行说明：

- 默认不要在第 2、3、4、6、7、8 步之间停下来问“是否继续”。
- 只要没有遇到权限阻塞、路径阻塞或用户显式停下，就继续跑完后续阶段。
- 如果用户只说“做 PRD”，则至少跑到完整多文档 PRD 交付完成。
- 如果用户说“做完整套产物”或没有限制范围，则按顺序继续到原型 / deck / ops。

## 完成标准

只有满足以下条件，才算完成一次交付：

- 本地 `.pd/` 下的多文档产物齐全，或脚本实际输出目录下的多文档产物齐全
- 已使用 `subskills/brainstorming`，且至少一份头脑风暴文档已完成
- 已完成 `steve-jobs-perspective` 收敛，且 `analysis/02-jobs-product-lens.md` 已完成
- 已使用 `subskills/deliver-prd`，且至少一套 PRD 文档已完成
- 已使用 `subskills/utility-mermaid-diagrams`，且至少包含 1 个用户流程图和 2 个架构/结构图
- 已包含范围版本、数据分析、上线运营这 3 类补充 PRD 文档，而不是只交主说明文
- 若用户要求飞书发布：发布已完成，或已明确记录阻塞原因、授权状态与待执行命令
- 若用户不要求飞书发布：本地多文档产物已完成即可
- 若要求原型：已使用 `subskills/frontend-design`，且原型 brief、页面覆盖清单与可预览原型代码已完成
- 若用户要求 PPT：已使用 `subskills/utility-slideshow-creator`，且对应目录下已有结构化产物
- 若用户要求运营素材：对应目录下已有结构化产物

不算完成的常见情况：

- 只完成了 analysis，没有继续进入 PRD
- 只完成了 PRD，没有处理用户已明确要求的飞书发布
- 只完成了原型 brief，没有继续生成可预览原型代码
- 只生成了部分目录，没有补齐最低交付文件

## 资源索引

- 文档结构：`references/artifact-structure.md`
- 飞书发布：`references/feishu-publishing.md`
- 飞书画板与图表发布：`references/feishu-whiteboard.md`
- 产品 / 商业思维框架（PM 铁律、机会评估、RICE、TAM/SAM/SOM、Now/Next/Later 等）：`references/product-thinking-frameworks.md`
- 第三方来源：`references/vendor-sources.md`
- 初始化脚本：`scripts/init_pm_case.py`
- 飞书预检查脚本：`scripts/feishu_preflight.py`
- 子技能更新脚本：`scripts/bootstrap_subskills.sh`
