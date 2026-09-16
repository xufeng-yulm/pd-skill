# 第三方子技能来源

本页记录仓库已有副本及历史参考；本次升级的新方法与中国社区来源见 [pm-source-map.md](pm-source-map.md)。子技能中的方法按任务取用，交付规模与授权以主入口及用户要求为准。

## brainstorming

- 来源仓库：<https://github.com/obra/superpowers>
- 子目录：`skills/brainstorming`
- 用途：需求发散、问题澄清、备选方案与推荐方案整理

## frontend-design

- 来源仓库：<https://github.com/anthropics/skills>
- 子目录：`skills/frontend-design`
- 用途：前端原型和高质量界面方案

## deliver-prd

- 来源仓库：<https://github.com/product-on-purpose/pm-skills>
- 子目录：`skills/deliver-prd`
- 用途：PRD 主结构与写作框架

## utility-mermaid-diagrams

- 来源仓库：<https://github.com/product-on-purpose/pm-skills>
- 子目录：`skills/utility-mermaid-diagrams`
- 用途：流程图、架构图、状态图等 mermaid 图表

## utility-slideshow-creator

- 来源仓库：<https://github.com/product-on-purpose/pm-skills>
- 子目录：`skills/utility-slideshow-creator`
- 用途：汇报 PPT 的 deck 结构、逐页内容和 JSON 规格

## steve-jobs-perspective

- 来源对齐：<https://github.com/alchaincyf/nuwa-skill>
- 历史参考，未随本仓库分发，也不是运行依赖。
- 用途：聚焦、取舍、端到端体验和一句话产品定义；主入口已包含可独立执行的判断问题。

## agency-agents

- 历史参考：<https://github.com/msitarzewski/agency-agents>
- 用途：产品与战略方法的早期整理来源；现按具体场景重写，不把经验阈值当作统一规则。

## 更新副本

`scripts/bootstrap_subskills.sh` 会联网替换已有 `subskills/`，包括本地定制。普通调用不需要执行。更新前保存改动、核对来源与许可，更新后审查与主入口的兼容性。
