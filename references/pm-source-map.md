# 方法来源与中国场景适配

核查日期：**2026-09-16**。以下页面在本次升级中实际读取。清单是选用依据，不是社区排名，也不表示覆盖全部主流方法。公开经验不等于已做用户研究。

## 本次参考与采用

| 来源 | 具体页面 | 采用内容 | 本地适配 |
| --- | --- | --- | --- |
| Product on Purpose / PM-Skills | [项目](https://github.com/product-on-purpose/pm-skills)、[实验设计](https://github.com/product-on-purpose/pm-skills/blob/main/skills/measure-experiment-design/SKILL.md) | 发现、定义、交付、衡量、迭代；预先定义实验指标与结果条件 | 扩展证据、验收、上线复盘；区分计划和真实结果 |
| Pawel Huryn / PM Skills | [项目](https://github.com/phuryn/pm-skills)、[机会解决方案树](https://github.com/phuryn/pm-skills/blob/main/pm-product-discovery/skills/opportunity-solution-tree/SKILL.md)、[优先级方法](https://github.com/phuryn/pm-skills/blob/main/pm-execution/skills/prioritization-frameworks/SKILL.md) | 目标→机会→方案→实验；按任务选择方法 | 不照搬固定方案数量；加入销售、大客户及实施成本 |
| 人人都是产品经理 / 张二十三 | [卖的是产品，做的却还是项目：B2B软件商品化最容易忽略的一步](https://www.woshipm.com/pd/6462863.html)，2026-09-10 | 谁买、为何买、买什么、怎么交易、怎么交付；产品与项目边界 | 采购/使用角色、标准/配置/定制、报价与验收范围 |
| 人人都是产品经理 / AI产品零度 | [项目管理平台如何接入 AI 工作流，从需求到交付形成闭环](https://www.woshipm.com/pd/6462957.html) | 业务状态与执行状态分离、上下文、产物证据及恢复 | 不将生成结束等同业务验收；AI 场景补评测、人工接管和有效结果成本 |
| 腾讯 TAPD | [敏捷研发官方介绍](https://www.tapd.cn/official/agile) | 用户故事、需求池、迭代、测试、发布、回顾与反馈 | 需求池→评审→研发/测试→上线→复盘，字段可映射协作工具 |
| 微信开放文档 | [小程序设计指南](https://developers.weixin.qq.com/miniprogram/design/) | 清晰流程、导航、反馈、异常恢复、减少输入、一致性 | 小程序场景与页面状态验收；接口能力仍按项目核查 |
| Intercom / Sean McBride | [RICE 原始说明](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/)，2018-01-05 | 触达、影响、信心、投入及例外处理 | 明确信心小数、正投入、相同单位/窗口，不把分数当硬门槛 |

## 本地设计

以下是本项目的执行约定，不是上述来源原文：

- `lean/standard` 两种交付规模；标准模式保留 `00–18` 共 19 篇 PRD。
- `E-ID → REQ-ID → BR-ID → AC-ID → 指标/版本` 追踪链。
- 国内场景路由、三类交付状态、文件结构和不覆盖初始化。
- 两种模式共用证据、需求池和验证计划。

## 既有资源与边界

已有副本来源见 [vendor-sources.md](vendor-sources.md)。本次扩展采用摘要和本地改写，未复制社区全文，也未引入新第三方子技能副本。既有 `agency-agents` 和 Jobs 视角保留历史参考来源，不是运行依赖。

后续更新核查具体页面、日期与使用条件，保留副本的许可说明。社区文章只支持方法启发，不能当统计或法律结论。平台接口、授权和资质应以执行时官方资料为准。
