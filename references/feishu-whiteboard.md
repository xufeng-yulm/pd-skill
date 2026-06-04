# 飞书画板与图表发布

本技能在把 PRD 发布到飞书时，不是简单地把 mermaid 源码塞进飞书文档就完事，而是按图表类型路由到飞书可继续编辑的画板，让关键图“好看、可改、可评审”。

默认原则：

- PRD 本地多文档中，**mermaid / 表格 / 编号结构块仍是主稿**。它是 PRD 单一事实源，可 diff、可版本化。
- 进入飞书后，按下面决策树把“关键图”升级为画板。
- 不要把 SVG / PNG / 截图图作为 PRD 核心结构信息的默认承载。

## 与 `lark-doc` / `lark-whiteboard` 的关系

| Skill | 职责 | 本 skill 的使用方式 |
| --- | --- | --- |
| `lark-doc` | 飞书云文档创建/读写/插入媒体 | 把 mermaid 图表直接以 `<whiteboard type="mermaid">…</whiteboard>` 插入到已创建的飞书文档中 |
| `lark-whiteboard` | 飞书画板查询 / 创建 / 编辑 / 复杂图表生成 | 复杂图（架构、泳道、漏斗、里程碑等）走它的 Mermaid / SVG / DSL 路由，由它把画板写到飞书 |
| 本 skill | 编排 | 在 `第 5 步` 写完多文档 PRD 之后，调度 `lark-doc` / `lark-whiteboard`，把关键图升级为画板 |

## 图表格式决策树

每张准备发到飞书的图都按下面顺序判断，命中哪一条就走哪条：

```
这张图是否要进飞书？
  └─ 否 → 留在 PRD 本地 mermaid，不动
  └─ 是 → 它是哪种图？
        ├─ 思维导图 / 时序图 / 类图 / 饼图 / 甘特图 / 状态图 / 简单 flowchart
        │     → 走 [Mermaid 内嵌模式](#mermaid-内嵌模式)
        └─ 架构图 / 业务架构 / 组织架构 / 泳道 / 漏斗 / 里程碑 / 鱼骨图 / 金字塔 / 柱状图 / 折线图 / 飞轮 / 对比矩阵 / 其它
              ├─ 已有画板要改字 / 换色 / 调布局
              │     → 走 [修改已有画板](#修改已有画板)
              └─ 全新图
                    → 走 [复杂画板模式](#复杂画板模式)
```

## Mermaid 内嵌模式

适用：思维导图、时序图、类图、饼图、甘特图、状态图、简单流程图。

写法（直接在 `lark-doc` 的 `docs +create` / `+update` 文档正文中插入）：

```xml
<whiteboard type="mermaid">
mindmap
  root((第一版开发交付))
    范围
      业务蓝图
      核心链路
    角色
      任务方
      学生 / 团队
      高校
      运营
    风险
      合规
      数据
      联调
</whiteboard>
```

要点：

- 必须用 `<whiteboard type="mermaid">…</whiteboard>` 包裹整段 mermaid 代码
- 标签完整闭合，不留未配对 `<whiteboard>`
- mermaid 语法自检：变量先声明后引用、label 含空格或括号必须双引号包裹
- 不支持 mermaid 表达的子图，先拆成多张独立图表，每张单独画板

如果图是“复杂 flowchart 但仍然想 mermaid 内嵌”，在写 mermaid 时就要规划好节点上限（mermaid 在大图下阅读性会崩）。

## 复杂画板模式

适用：架构图、业务架构、组织架构、泳道、漏斗、里程碑、鱼骨图、金字塔、柱状图、折线图、飞轮、对比矩阵等 mermaid 难以撑住的图形。

流程：

1. **准备产物目录**

   ```text
   .pd/diagrams/<YYYY-MM-DDTHHMMSS>/
   ├── diagram.mmd   # 或 diagram.svg / diagram.json（按路由决定）
   ├── diagram.json  # 渲染脚本导出
   ├── diagram.png   # 渲染结果预览
   └── source.cjs    # 坐标计算脚本（仅 DSL 路由）
   ```

   目录命名严格按 `lark-whiteboard` 的产物规范：本地时间，格式 `YYYY-MM-DDTHHMMSS`，不含冒号与时区。

2. **读 `lark-whiteboard` 完整 SKILL.md**

   包含认证、全局参数、SVG 失败硬兜底、产物文件命名等强制约束，**必须先读再动手**。

3. **自报身份 + 选路由**

   读 `lark-whiteboard/SKILL.md` 的「渲染路由」段，按「身份（Claude / Gemini / GPT / GLM / Doubao / Seed / Other）× 图表类型」选 Mermaid / SVG / DSL。

4. **渲染 & 视觉自检**

   - 导出 PNG 预览
   - 目视确认：无文字溢出、节点压字、布局整体崩溃
   - SVG 路径两轮改写仍不收敛 → **丢弃当前 SVG，改走 DSL 从零重画**（硬兜底）
   - 不要逐行修补 SVG 源码，常常越补越乱

5. **写入飞书画板**

   ```bash
   npx -y @larksuite/whiteboard-cli@^0.2.11 -i diagram.mmd --to openapi --format json \
     | lark-cli whiteboard +update \
       --whiteboard-token <Token> \
       --source - --input_format raw \
       --idempotent-token <10+字符唯一串> \
       --as user \
       --overwrite
   ```

   - `--overwrite` 必须带，否则旧内容会和新内容重叠
   - `--idempotent-token` 至少 10 字符，建议用 `时间戳-board-<序号>`，避免重试导致重复
   - `--as user` 切应用身份时改为 `--as bot`

6. **在飞书文档里挂画板**

   在 `lark-doc` 创建 / 更新文档时，用 `<whiteboard>` 组件挂上画板：

   ```xml
   <whiteboard token="wbcnXXXXXXXX"/>
   ```

   或者用 lark-doc 的 `media insert` 能力把画板 token 作为插入元素写进文档。

7. **回填产物**

   把 `whiteboard_token` 与画板 URL 写回 `feishu/publish-result.md`，并保留 `.pd/diagrams/...` 目录作为本地可重发布产物。

## 修改已有画板

适用：评审会上画板被点过、需要改文字、换颜色、调整布局。

流程：

1. **取 board_token**

   - 用户直接给：`wbcnXXX`
   - 文档 URL / doc_id 中提取：`lark-cli docs +fetch --api-version v2 --doc <URL> --as user`，从返回的 `<whiteboard token="…"/>` 提取

2. **判断修改策略**

   ```bash
   lark-cli whiteboard +query --whiteboard-token <Token> --output_as code
   ```

   - 返回 mermaid / plantuml 代码 → 在原代码上改 → `+update --input_format mermaid/plantuml`
   - 没有代码（DSL 或原生画板）：
     - 只改文字 / 颜色 → `+query --output_as raw` → 手动改 JSON → `+update --input_format raw --overwrite`
     - 结构调整 / 重绘 → `+query --output_as image` 看图后进入「复杂画板模式」从零重画

3. **加 `--overwrite`**，避免叠加

## 与 mermaid 文档的关系

发布到飞书后，本地 PRD 文档保持 mermaid / 表格 / 编号结构块不变，二者并存：

- **PRD 文档**：可 diff、可版本化、可二次编辑 mermaid 源码；评审会前快速更新靠这一层
- **飞书画板**：发布后用于演示 / 高频评审 / 视觉呈现；本地 PRD 改了，发布前再同步一次

不要因为有画板就放弃 mermaid 主稿。两者是“文档源 ↔ 演示画”的关系。

## 失败回退

发布画板失败时：

1. 不要回滚已经写好的 PRD 文档
2. 把失败命令、错误信息写到 `feishu/publish-plan.md`
3. 写清楚缺的是：登录、scope、目标父节点 token，还是网络 / 渲染管线
4. `.pd/diagrams/...` 目录必须保留本地，授权恢复后可以重试
5. 告诉用户“等待你完成飞书授权 / 确认发布目标后再继续画板发布”

## 校验清单

每次画板发布完成后，逐条检查：

- [ ] 画板 token 已写入 `feishu/publish-result.md`，并能直接在飞书打开
- [ ] 文档正文中能正常加载画板，无“画板加载失败”占位
- [ ] 画板 PNG 预览无文字溢出、无节点压字、无严重重叠
- [ ] 本地 `.pd/diagrams/<时间戳>/` 目录存在，源码 / 渲染产物 / 预览图齐全
- [ ] 如果是替换原画板，确认旧画板内容已被覆盖
- [ ] 如果是修改字 / 色，diff 后只动了目标字段，没动其他节点

## 与现有产物目录的关系

`scripts/init_pm_case.py` 默认会创建 `.pd/diagrams/` 目录，作为本次产物的画板产物根。`lark-whiteboard` 规范要求每次画图用 `YYYY-MM-DDTHHMMSS/` 子目录区分多次迭代。

详细目录结构见 `references/artifact-structure.md`。
