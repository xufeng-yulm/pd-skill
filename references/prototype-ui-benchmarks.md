# GitHub Prototype UI Benchmarks

在生成 `prototype/web/` 原型前，先从下面的 GitHub 开源产品里挑 1-2 个最贴近场景的参考对象。目标是借鉴信息层级、布局密度、导航方式、状态设计和交互组织，不是照抄品牌视觉。

## 选择规则

1. 只选和业务类型接近的参考，不要把监控台做成营销站，也不要把运营后台做成作品集。
2. 每轮原型最多锁定 2 个参考，避免风格混杂。
3. 产出时必须写明：
   - 参考仓库
   - 借鉴点
   - 不借鉴点
4. 不得照搬 logo、品牌色、插画、文案。

## 推荐参考库

### 1. `midday-ai/midday`
- GitHub: <https://github.com/midday-ai/midday>
- 适合：SaaS 工作台、财务/运营总览、需要“高级但克制”的后台
- 借鉴点：
  - 密度高但不拥挤的卡片和表格编排
  - 工具型顶部导航和筛选区
  - 安静的中性色 + 少量功能色

### 2. `calcom/cal.com`
- GitHub: <https://github.com/calcom/cal.com>
- 适合：多角色工作台、预约/配置流、复杂设置页
- 借鉴点：
  - 多步骤配置流程
  - 列表、表单、详情页之间的跳转组织
  - 适合 B 端的功能型页面节奏

### 3. `outline/outline`
- GitHub: <https://github.com/outline/outline>
- 适合：知识库、协作平台、文档中心、内容管理
- 借鉴点：
  - 侧栏 + 内容区的层级稳定性
  - 文本与工具栏的平衡
  - 平静、可长期使用的 UI 节奏

### 4. `appsmithorg/appsmith`
- GitHub: <https://github.com/appsmithorg/appsmith>
- 适合：复杂后台、配置台、编排型工具、运营/管理系统
- 借鉴点：
  - 三栏/多栏工作区
  - 面板式信息组织
  - 大量状态和控件共存时的可读性

### 5. `openstatusHQ/openstatus`
- GitHub: <https://github.com/openstatusHQ/openstatus>
- 适合：监控、状态页、指标看板、告警/健康度界面
- 借鉴点：
  - 时间序列和状态面板的排布
  - 状态颜色的克制使用
  - 运维场景里“扫一眼就知道发生了什么”的结构

## 页面类型到参考的映射

| 页面类型 | 优先参考 |
| --- | --- |
| SaaS 工作台 / 运营后台 | `midday-ai/midday`, `appsmithorg/appsmith` |
| 配置中心 / 表单流 / 多角色后台 | `calcom/cal.com`, `appsmithorg/appsmith` |
| 知识库 / 内容管理 / 协作空间 | `outline/outline` |
| 数据监控 / 任务状态 / 项目健康度 | `openstatusHQ/openstatus`, `midday-ai/midday` |

## 禁止项

- 紫蓝渐变 + 大圆角卡片 + 空洞 hero 文案
- 只做首页，不做角色闭环和状态页
- 只有 mock 卡片，没有真实列表、表格、详情、筛选、空态、错误态
- 用营销站布局冒充业务系统
- 页面之间没有路由或导航关系
