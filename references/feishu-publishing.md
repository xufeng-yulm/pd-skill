# 飞书发布说明

本技能不会默认把 PRD 发布到飞书。先完成本地多文档产物，然后显式询问用户是否要通过飞书 CLI 发布。

只有用户明确说“要发布到飞书”，才进入本页流程。

## 已验证的 CLI 基础命令

以下命令基于本地执行过的 `@larksuite/cli` 帮助信息整理：

- CLI 包：`@larksuite/cli`
- 已确认版本：`1.0.25`
- 文档命令：`docs`
- 云盘命令：`drive`
- 知识库命令：`wiki`

## 决策门

先问用户：

> 是否要通过飞书 CLI 直接发布到飞书？

分支如下：

- 不需要：停在本地多文档交付；可选生成 `publish-plan.md`
- 需要：先跑预检查，再确认目标发布位置，最后进入发布流程

## 发布前预检查

先运行：

```bash
python3 scripts/feishu_preflight.py
```

如果目标是飞书知识库，应改为：

```bash
python3 scripts/feishu_preflight.py --wiki
```

这个脚本会检查：

- 是否能找到 `lark-cli`
- 当前是否已授权
- 当前 token 是否具备基础写入 scopes
- 当传入 `--wiki` 时，是否具备知识库读取与节点创建 scopes

## 目标路径确认

发布到飞书前，必须先让用户确认目标位置。

### 如果发到 Drive 目录

必须让用户提供或确认目标父目录 token。不要默认发到任意目录。

### 如果发到 Wiki

1. 读取知识库列表：

```bash
python3 scripts/feishu_wiki_targets.py
```

2. 把返回结果中的 `name` 和 `space_id` 展示给用户，明确询问：

> 发布到哪个知识库？

3. 用户确认 `space_id` 后，如果还需要确认知识库内路径，读取该空间下的一级节点：

```bash
python3 scripts/feishu_wiki_targets.py --space-id "<space_id>"
```

4. 如果用户要挂到某个节点下，再继续读取对应父节点的子节点：

```bash
python3 scripts/feishu_wiki_targets.py --space-id "<space_id>" --parent-node-token "<node_token>"
```

5. 只有在 `space_id` 与可选的 `parent_node_token` 都经用户确认后，才允许执行写操作。

如果检查失败，不应继续发文档，而应等待用户完成授权。

## 推荐发布路径

### 方案 A：发布到 Drive 目录

1. 创建文件夹：

```bash
npx -y @larksuite/cli@latest drive files create_folder \
  --data '{"name":"PRD - <项目名>","folder_token":"<父目录token>"}' \
  --yes
```

2. 逐篇创建文档：

```bash
npx -y @larksuite/cli@latest docs +create \
  --title "<文档标题>" \
  --markdown @<本地markdown文件> \
  --folder-token "<新目录token>"
```

这个方案最贴合“新建目录，多文档展示 PRD”的要求。

### 方案 B：发布到 Wiki

当用户明确要求进知识库，并且已经确认 `space_id` 与可选父节点后，先建 wiki 节点：

```bash
npx -y @larksuite/cli@latest wiki +node-create \
  --space-id "<space_id>" \
  --title "<项目名>"
```

如果要挂到知识库内指定路径：

```bash
npx -y @larksuite/cli@latest wiki +node-create \
  --space-id "<space_id>" \
  --parent-node-token "<parent_node_token>" \
  --title "<项目名>"
```

如果本地先创建的是 Drive 文档，也可以后续用 `wiki +move` 把文档纳入知识库结构。

## 发布顺序

按 `feishu/manifest.json` 的 `documents` 顺序逐篇发布，默认顺序应为：

1. 项目背景
2. 执行摘要
3. 问题与目标
4. 用户角色与场景
5. 方案总览
6. 用户流程
7. 功能需求
8. 业务规则与验收
9. 功能架构
10. 技术架构
11. 指标、风险、依赖
12. 里程碑

## 发布前检查

- 用户已明确要求发布到飞书
- 飞书 CLI 已登录
- `scripts/feishu_preflight.py` 已通过
- 目标知识库或目标目录已经过用户确认
- 目标目录或空间权限可写
- 本地 markdown 内容已定稿
- mermaid 代码已经过基本语法检查
- 核心图形内容使用的是飞书可编辑文本格式（优先 Mermaid / Markdown 表格 / 编号结构块）
- 未把封面图、旅程图、循环图、信息架构图、漏斗图做成 SVG 或静态图片主稿
- `manifest.json` 中文档路径存在

## 图形格式要求

面向飞书发布时，核心图形默认采用以下顺序：

1. Mermaid
2. Markdown 表格
3. 编号列表 / 分层清单 / 文本卡片

默认不要用：

- SVG
- PNG / JPG 截图式图示
- 只能查看、不能在飞书正文内继续编辑的嵌入图

只有在用户明确要求导出静态图，或者某种结构确实无法用文本格式表达时，才允许把静态图作为补充材料，而不是主稿。

## 发布失败时的处理

不要回滚前面的文档生产工作。改为：

1. 记录失败命令和错误信息到 `feishu/publish-plan.md`
2. 写清楚缺少的是登录、scope、权限、目标 token 还是网络
3. 如果知识库或父节点路径尚未确认，把候选 `space_id` / `parent_node_token` 一并写入
4. 明确告知用户“等待你完成飞书授权并确认发布目标后再继续发布”
5. 保留所有本地 PRD 文档，等待下一次继续发布
