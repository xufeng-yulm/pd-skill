# 产品与商业思维框架

本文件蒸馏自 `msitarzewski/agency-agents` 的产品与战略线（`product/*`、`strategy/*`），挑出能直接加强 pd-skill 的高价值框架。每条框架给出「是什么 → 何时用 → 怎么用 → 在 pd-skill 哪一步落地」。

> 使用方式：本文件是参考，不是模板。PM 在对应步骤主动选用其中一两个，而不是堆砌全部。

---

## 1. PM 八条铁律

来源：`product/product-manager.md`。可直接作为 `prd-skill` 工作原则的补强。

1. **先说问题，再说方案。** Stakeholders 带着方案来，PM 的工作是先还原背后的用户痛点或业务目标，再评估方案。
2. **PRD 之前先写 Press Release。** 一段话说不清用户为什么在乎，就还没准备好写需求或开设计。
3. **没有 owner / 成功指标 / 时间窗的需求，不进路线图。** 「我们改天做一下」不是路线图项。
4. **经常说 No。** 保护团队焦点是最被低估的 PM 能力。每说一个 Yes，就是对其他事情的 No；让取舍显式。
5. **构建前验证，上线后衡量。** 所有功能想法都是假设，重大范围不拿证据不立项。
6. **对齐 ≠ 共识。** 共识是奢侈品，清晰是必需品。每个人要理解决策、决策理由、自己要执行的环节。
7. **惊喜 = 失败。** 延期、范围变更、未达指标都不能让 stakeholders 突然知道。要主动沟通两次以上。
8. **范围蠕变会杀死产品。** 每个变更请求都要被记录、对照目标、明确接受 / 延后 / 拒绝，绝不静默吸收。

**在 pd-skill 落地：**

- 第 1-2 步（接收需求 + 头脑风暴）必须产出「问题陈述」和「Press Release 草稿」，再写 PRD
- 头脑风暴结果必须显式记录「我们不做的事项」
- 12 / 16 阶段必须给出每个里程碑的 owner + 指标 + 时间窗

---

## 2. Press Release 之前

「如果用户不在乎，那我们就不该做。」

模板（中文版骨架）：

```text
【标题】一句话卖点
【副标题】谁 + 在什么场景下 + 得到什么结果

今天我们为 [角色] 推出 [产品 / 功能]，解决 [具体痛点]。
和现有方案不同，[本方案] 让 [用户] 可以 [关键动作]，从而 [可衡量结果]。

首发场景：
- [场景 1]
- [场景 2]

为什么现在做：[市场 / 用户行为 / 竞争态势] 让我们必须抓住这个窗口。
我们不会做：[明确不做的诱惑项]。

—— 完 ——
```

**何时用：** 头脑风暴收敛之后、PRD 撰写之前；尤其是 V1 / 重大新方向。

**在 pd-skill 落地：** `analysis/02-jobs-product-lens.md` 之后、`prd/01` 撰写之前。要求 1 段以内，不超过 200 字。

---

## 3. Why Now? 机会窗口

每个产品决策都要回答：**为什么是现在？** 否则就是「想做的事」而不是「必须做的事」。

四个常见 Why Now：

| 触发类型     | 典型信号                               | 反问                       |
| ------------ | -------------------------------------- | -------------------------- |
| 市场窗口     | TAM 拐点、新政策、平台更迭             | 不做 6 个月会怎样？        |
| 用户行为拐点 | 留存阈值被跨过、行为数据异常、NPS 信号 | 现有方案开始不可忍受？     |
| 竞争压力     | 直接竞品上线、间接替代品规模化         | 落后半年还有窗口？         |
| 内部能力成熟 | 自研技术 / 数据资产 / 团队到位         | 现在能打平过去的成本曲线？ |

**何时用：** 任何 V1 / 新方向的「机会评估」环节；路线图改版的论证段。

**在 pd-skill 落地：** `prd/00-business-blueprint.md` 的「为什么是现在」段、`prd/12-scope-and-release-plan.md` 的「版本切分依据」段。

---

## 4. Opportunity Assessment 机会评估

来源：`product/product-manager.md`。用于替代「凭感觉立项」。

标准结构：

1. **Why Now?**（用上面第 3 节的信号）
2. **用户证据**：访谈（n≥5）、行为数据、客服信号、竞品信号各占一段
3. **商业论证**：营收影响、成本影响、战略契合（接 OKR）、市场 sizing
4. **RICE 评分**（见第 5 节）
5. **方案选项表**：自建完整版 / MVP / 采购集成 / 延后两季度，各列优劣与投入
6. **推荐与回滚条件**：Build / Explore / Defer / Kill；附信心度

**何时用：** 任何超过 2 周投入的立项；季度路线图排序。

**在 pd-skill 落地：** 在 `analysis/02-jobs-product-lens.md` 末尾或 `prd/00-business-blueprint.md` 末尾追加「机会评估」段（视重要性二选一）。

---

## 5. RICE 评分

来源：`product/product-sprint-prioritizer.md`。RICE = Reach × Impact × Confidence ÷ Effort。

| 因子       | 含义               | 取值 / 单位                |
| ---------- | ------------------ | -------------------------- |
| Reach      | 季度内受影响用户数 | 数字 + 区间（保守 / 乐观） |
| Impact     | 对业务目标的贡献   | 0.25 / 0.5 / 1 / 2 / 3     |
| Confidence | 信心度             | 百分比 + 依据              |
| Effort     | 投入               | 人月 / t-shirt size        |

**使用约束：**

- RICE 是排序工具，不是真理。分数接近的项（< 10% 差距）让战略 / 风险判断决胜负
- Confidence < 50% 的项应该走 Explore 而非 Build
- Effort 必须包含「联调 + 测试 + 上线」的真实成本，不能只算 happy path

**何时用：** 季度 / 双周路线图排序；机会评估的方案选项排序。

**在 pd-skill 落地：** `prd/12-scope-and-release-plan.md` 的「版本切分依据」段、`analysis/02-jobs-product-lens.md` 的「推荐方案」段。

---

## 6. 价值 - 投入矩阵 + Kano 模型

来源：`product/product-sprint-prioritizer.md`。两个框架互补，用来快速判断一个想法值不值得做。

### 价值-投入矩阵

|            | 低投入              | 高投入               |
| ---------- | ------------------- | -------------------- |
| **高价值** | 立即做（Quick Win） | 战略项目，分阶段投入 |
| **低价值** | 容量补位            | 砍掉 / 重设目标      |

### Kano 模型

| 类型        | 含义                 | 处置                         |
| ----------- | -------------------- | ---------------------------- |
| Must-Have   | 缺失会被骂           | 必做，但不构成差异化         |
| Performance | 越多越好，有递减     | 看竞争水位决定水位           |
| Delighters  | 超出预期，能形成口碑 | 投放型资源，宁可不做也不摊薄 |
| Indifferent | 用户不在乎           | 砍 / 重新定位                |
| Reverse     | 做了反而被骂         | 删除                         |

**何时用：** 评审单个功能 / 一组功能；处理 backlog 里的「历史包袱」。

**在 pd-skill 落地：** `prd/07-functional-requirements.md` 的「需求优先级」表与「需求降级 / 删除」说明。

---

## 7. Now / Next / Later 路线图

来源：`product/product-manager.md`。比 Gantt 图更适合在多变环境里沟通。

| 桶                  | 含义        | 入桶要求                                         |
| ------------------- | ----------- | ------------------------------------------------ |
| **🟢 Now**          | 本季度交付  | 工程、设计、PM 全部对齐，owner / 指标 / ETA 明确 |
| **🟡 Next**         | 下 1-2 季度 | 方向已定，需要开工前细化                         |
| **🔵 Later**        | 3-6 月视野  | 战略押注，需要信号才能进 Next                    |
| **❌ Not Building** | 公开说不做  | 写明「为什么不做」和「什么条件下重新评估」       |

**使用约束：**

- Now 不要超过 3-5 个，超过即代表焦点失守
- 每个 Not Building 必须有理由 + 重新评估条件，否则 stakeholder 会反复问
- Later 不写「何时交付」，只写「什么信号能让我们把它推到 Next」

**何时用：** 季度路线图沟通会；面对 sales / 客户做需求排期时。

**在 pd-skill 落地：** `prd/16-milestones.md` 增加「Now / Next / Later」结构；`prd/12-scope-and-release-plan.md` 增加「Not Building」表。

---

## 8. TAM / SAM / SOM 与趋势生命周期

来源：`product/product-trend-researcher.md`。用于在「业务蓝图」阶段判断市场体量与时机。

### 三层市场 sizing

| 层      | 含义       | 计算方法                                                               |
| ------- | ---------- | ---------------------------------------------------------------------- |
| **TAM** | 总潜在市场 | 自上而下：行业总盘 × 我们的可触达比例；或自下而上：客单价 × 潜在客户数 |
| **SAM** | 可服务市场 | 我们产品形态 / 渠道 / 地域能覆盖的子集                                 |
| **SOM** | 可获取市场 | 1-3 年内能拿下的份额，依赖销售 / 渠道 / 品牌能力                       |

**约束：** SOM 必须小于 SAM 的 30%，否则说明估算过于乐观。

### 趋势生命周期

```
萌芽期 → 高速增长 → 成熟期 → 衰退期
  |          |          |         |
 强信号    押注期     优化期    退出期
  0-3%     3-30%     30-70%    >70%
 渗透率    渗透率     渗透率    渗透率
```

**何时用：** 业务蓝图（`prd/00`）的市场体量段；新方向立项的「为什么是现在」段。

**在 pd-skill 落地：** `prd/00-business-blueprint.md` 增加「TAM / SAM / SOM」与「市场时机」两段；机会评估的「商业论证」段。

---

## 9. 多阶段质量门（Pipeline Integrity）

来源：`strategy/nexus-strategy.md`。pd-skill 现有的「完成定义 / DoD」已经接近这个概念，但 NEXUS 把它显式拆成「阶段-门-证据」三件套。

**三件套模板：**

| 维度 | 内容                                         |
| ---- | -------------------------------------------- |
| 阶段 | 当前阶段名 + 时长范围                        |
| 门   | 通过/不通过的判定人 + 判定标准               |
| 证据 | 必须提交的具体产物（日志、截图、报告、数据） |

**关键原则：**

- **Evidence Over Claims**：所有质量判断都要有证据，不能「我觉得挺好的」
- **Fail Fast, Fix Fast**：单任务最多 3 次重试，超过就升级而不是无限重试
- **Single Source of Truth**：一个规范、一个任务列表、一个架构文档，避免 N 个版本互相对齐
- **Context Continuity**：跨阶段交接必须把上下文全量带上，下游不能冷启动

**在 pd-skill 落地：**

- 「完成定义 / DoD」表重写为「阶段-门-证据」三列结构
- 阶段交接必须明确「交付物 + 接受人 + 移交清单」，写到 `analysis/01` 与 `prd/01` 顶部

---

## 10. 用户反馈五通道

来源：`product/product-feedback-synthesizer.md`。把零散反馈汇成可行动洞察。

| 通道                 | 性质                     | 适用          |
| -------------------- | ------------------------ | ------------- |
| **Proactive** 主动   | 调研、问卷、内测         | 验证假设      |
| **Reactive** 被动    | 工单、差评、客诉         | 找问题        |
| **Passive** 被动     | 行为数据、热图、会话回放 | 找摩擦        |
| **Community** 半主动 | 论坛、Discord、用户群    | 找趋势 / 机会 |
| **Competitive** 主动 | 竞品评论、行业论坛       | 找差异 / 空白 |

**使用约束：**

- 任何优先级结论必须引用至少 2 个通道的证据
- 反馈主题要先做信度检查（≥3 个独立用户、≥2 个通道），再进入路线图
- 抱怨频率 ≠ 优先级，× 影响的用户数才是优先级

**在 pd-skill 落地：** `prd/04-user-segments-and-scenarios.md` 的「角色边界」段；机会评估的「用户证据」段。

---

## 11. 行为激励（Nudge）

来源：`product/product-behavioral-nudge-engine.md`。偏交互设计，但 PRD 写「状态与文案」「通知策略」时直接可用。

四条原则：

1. **不要把 50 个待办砸给用户。** 永远只给 1 个最低成本的 next step
2. **尊重专注时段。** 不要在用户工作时间打断；选择用户偏好的通道（SMS / Email / In-App）
3. **提供 opt-out 收口。** 每次「继续冲刺」都要配「先到这」按钮
4. **用 default bias 替用户做决定。** 预填草稿 → 询问「发还是改」远比「请写一封感谢信」转化高

**何时用：** 写通知、提醒、引导、首次体验、激励文案时。

**在 pd-skill 落地：** `prd/13-interaction-and-content-spec.md` 的「状态与提示文案」段与「通知 / 引导策略」段。

---

## 在 pd-skill 中的引用入口

- `analysis/01-brainstorm.md` 末尾：补「Why Now?」与「Press Release 草稿」
- `analysis/02-jobs-product-lens.md`：用 PM 八条铁律作为收敛检查清单
- `prd/00-business-blueprint.md`：嵌入 TAM/SAM/SOM、市场时机、机会评估
- `prd/04-user-segments-and-scenarios.md`：嵌入五通道反馈证据
- `prd/07-functional-requirements.md`：嵌入 RICE + Kano
- `prd/12-scope-and-release-plan.md`：嵌入 RICE 排序依据 + Not Building 表
- `prd/13-interaction-and-content-spec.md`：嵌入 Nudge 四原则
- `prd/16-milestones.md`：改用 Now / Next / Later + 阶段-门-证据表
- 完成定义 / DoD：改用「阶段-门-证据」三列结构

---

## 来源

- `msitarzewski/agency-agents` 仓库
  - `product/product-manager.md`
  - `product/product-sprint-prioritizer.md`
  - `product/product-trend-researcher.md`
  - `product/product-feedback-synthesizer.md`
  - `product/product-behavioral-nudge-engine.md`
  - `strategy/nexus-strategy.md`
  - `strategy/playbooks/phase-0-discovery.md`
  - `strategy/EXECUTIVE-BRIEF.md`
