#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


DOCS = [
    ("01-project-background.md", "项目背景"),
    ("02-executive-summary.md", "执行摘要"),
    ("03-problem-and-goals.md", "问题与目标"),
    ("04-user-segments-and-scenarios.md", "用户角色与场景"),
    ("05-solution-overview.md", "方案总览"),
    ("06-user-flows.md", "用户流程"),
    ("07-functional-requirements.md", "功能需求"),
    ("08-business-rules-and-acceptance.md", "业务规则与验收"),
    ("09-information-architecture.md", "功能架构"),
    ("10-technical-architecture.md", "技术架构"),
    ("11-metrics-risks-dependencies.md", "指标、风险、依赖"),
    ("12-milestones.md", "里程碑"),
]

DOC_TEMPLATES = {
    "01-project-background.md": "# 项目背景\n\n> **一句话产品定义：** 待补充\n>\n> **Why now：** 待补充\n>\n> **这次不做什么：** 待补充\n\n## 发起背景\n\n## 行业 / 业务环境\n\n## 现状与机会窗口\n\n## 为什么是现在\n\n## 不做的代价\n\n## 决策者速览\n\n| 维度 | 结论 |\n| --- | --- |\n| 用户价值 | 待补充 |\n| 商业价值 | 待补充 |\n| 核心下注 | 待补充 |\n| 关键取舍 | 待补充 |\n\n",
    "02-executive-summary.md": "# 执行摘要\n\n> 默认使用飞书可编辑格式。不要把本页核心图形做成 SVG 或静态图片。\n\n## 项目概述\n\n## 为什么现在做\n\n## 本期交付范围\n\n## 预期业务结果\n\n## 封面型总览图\n\n```mermaid\nmindmap\n  root((产品总览))\n    用户价值\n      待补充\n    核心流程\n      待补充\n    商业结果\n      待补充\n```\n\n## 体验旅程图\n\n```mermaid\njourney\n    title 待补充\n    section 发现\n      用户进入场景: 3: 用户\n    section 完成任务\n      用户完成关键动作: 4: 用户, 产品\n    section 得到反馈\n      用户获得结果与下一步: 5: 产品\n```\n\n## 本期重点卡片\n\n| 模块 | 要解决的问题 | 价值 |\n| --- | --- | --- |\n| 待补充 | 待补充 | 待补充 |\n\n",
    "03-problem-and-goals.md": "# 问题与目标\n\n## 当前核心问题\n\n## 目标\n\n## 非目标\n\n## 成功指标\n\n| 指标 | 当前值 | 目标值 | 时间窗 |\n| --- | --- | --- | --- |\n| 待补充 | 待补充 | 待补充 | 待补充 |\n\n## Focus / Say No\n\n- 要坚持做的：待补充\n- 本期明确不做的：待补充\n- 容易分散焦点的诱惑项：待补充\n\n",
    "04-user-segments-and-scenarios.md": "# 用户角色与场景\n\n## 核心角色\n\n## 次级角色\n\n## 典型使用场景\n\n## 高频任务\n\n## 关键痛点\n\n",
    "05-solution-overview.md": "# 方案总览\n\n## 方案摘要\n\n## 用户价值\n\n## 平台价值\n\n## 体验原则\n\n1. 待补充\n2. 待补充\n3. 待补充\n\n## 产品循环图\n\n```mermaid\nflowchart LR\n    A[\"触发\"] --> B[\"激活\"]\n    B --> C[\"获得价值\"]\n    C --> D[\"留存 / 复用\"]\n    D --> E[\"传播 / 扩张\"]\n    E --> A\n```\n\n## 方案结构图\n\n```mermaid\nflowchart TB\n    A[\"用户入口\"] --> B[\"核心体验层\"]\n    B --> C[\"关键工作流\"]\n    C --> D[\"支撑能力\"]\n    D --> E[\"反馈与增长\"]\n```\n\n## 模块清单\n\n| 模块 | 目标 | 主要用户 | 优先级 |\n| --- | --- | --- | --- |\n| 待补充 | 待补充 | 待补充 | P0 |\n\n## 范围边界\n\n### In Scope\n\n### Out of Scope\n\n### Later\n\n",
    "06-user-flows.md": """# 用户流程

## 角色说明

1. 任务方 / 需求方
2. 平台运营
3. 学生个人 / 团队负责人
4. 高校管理员

## 核心流程 1：任务发布到完成

```mermaid
flowchart TD
    A["需求方创建任务"] --> B["平台审核任务信息"]
    B --> C["任务发布到前台"]
    C --> D["学生/团队浏览并报名"]
    D --> E["需求方筛选团队"]
    E --> F["项目立项并进入执行"]
    F --> G["团队提交阶段性交付物"]
    G --> H{"是否验收通过"}
    H -- "否" --> I["退回并补充反馈"]
    I --> G
    H -- "是" --> J["记录结项与后续动作"]
```

## 核心流程 2：高校组织入驻

```mermaid
flowchart TD
    A["高校提交入驻申请"] --> B["平台审核学校资料"]
    B --> C["创建高校账号与管理员"]
    C --> D["邀请学生/团队加入"]
    D --> E["完成资料认证后参与项目"]
```

## 体验要求

1. 前台任务信息要清楚说明目标、报酬、时间和交付标准。
2. 报名和筛选链路应短，避免复杂配置。
3. 项目执行页需要同时支持进度、交付物和反馈记录。

""",
    "07-functional-requirements.md": "# 功能需求\n\n## 模块总表\n\n| 模块 | 关键能力 | 用户价值 | 优先级 |\n| --- | --- | --- | --- |\n| 待补充 | 待补充 | 待补充 | P0 |\n\n## 用户端\n\n## 任务方端\n\n## 高校管理端\n\n## 运营后台\n\n## 优先级\n\n",
    "08-business-rules-and-acceptance.md": "# 业务规则与验收\n\n## 核心业务规则\n\n## 状态流转规则\n\n## 权限规则\n\n## 验收标准\n\n## 边界与异常处理\n\n",
    "09-information-architecture.md": """# 功能架构

## 功能架构图

```mermaid
flowchart TD
    A["平台产品"] --> B["前台门户"]
    A --> C["学生/团队端"]
    A --> D["高校管理端"]
    A --> E["运营后台"]

    B --> B1["首页 / 品牌叙事"]
    B --> B2["任务广场"]
    B --> B3["案例 / 成果"]

    C --> C1["注册与认证"]
    C --> C2["任务报名"]
    C --> C3["项目执行"]
    C --> C4["成长档案"]

    D --> D1["高校入驻"]
    D --> D2["团队管理"]
    D --> D3["校内成果统计"]

    E --> E1["任务治理"]
    E --> E2["审核合规"]
    E --> E3["项目验收"]
    E --> E4["运营配置"]
```

## 信息架构说明

> 如果发布到飞书，本节应保持 Mermaid + 分层清单双份表达，避免只留静态图。

## 信息架构层级表

| 一级导航 / 角色 | 二级页面 / 模块 | 三级页面 / 操作 | 主要任务 | 备注 |
| --- | --- | --- | --- | --- |
| 前台门户 | 待补充 | 待补充 | 待补充 | 待补充 |
| 学生 / 团队端 | 待补充 | 待补充 | 待补充 | 待补充 |
| 高校管理端 | 待补充 | 待补充 | 待补充 | 待补充 |
| 运营后台 | 待补充 | 待补充 | 待补充 | 待补充 |

### 前台门户

1. 首页
2. 任务广场
3. 任务详情
4. 案例中心

### 学生 / 团队端

1. 我的报名
2. 我的项目
3. 成长档案

### 运营后台

1. 任务管理
2. 团队管理
3. 项目验收
4. 数据统计

""",
    "10-technical-architecture.md": """# 技术架构

## 技术架构图

```mermaid
flowchart LR
    A["Web 门户"] --> D["应用服务层"]
    B["小程序 / H5"] --> D
    C["管理后台"] --> D

    D --> E["身份与权限服务"]
    D --> F["任务与项目服务"]
    D --> G["团队与报名服务"]
    D --> H["验收与通知服务"]

    E --> I["关系型数据库"]
    F --> I
    G --> I
    H --> J["消息通道"]
    D --> K["文件存储"]
    D --> L["审计日志"]
```

## 架构原则

1. 首版优先保证任务、团队、项目三条主链路清晰。
2. 扩展能力通过独立服务或接口预留，不提前复杂化。
3. 用户、项目、验收、通知的数据边界要明确。

## 核心数据对象

1. 用户
2. 团队
3. 任务
4. 项目
5. 交付物
6. 验收记录

## 分层说明

| 层级 | 职责 | 关键接口 / 对象 |
| --- | --- | --- |
| 终端层 | 待补充 | 待补充 |
| 应用层 | 待补充 | 待补充 |
| 领域层 | 待补充 | 待补充 |
| 基础设施层 | 待补充 | 待补充 |

""",
    "11-metrics-risks-dependencies.md": "# 指标、风险、依赖\n\n## 北极星指标\n\n## 过程指标\n\n## 指标漏斗图\n\n| 漏斗阶段 | 定义 | 当前值 | 目标值 | Owner |\n| --- | --- | --- | --- | --- |\n| 曝光 / 触达 | 待补充 | 待补充 | 待补充 | 待补充 |\n| 访问 / 激活 | 待补充 | 待补充 | 待补充 | 待补充 |\n| 核心行为完成 | 待补充 | 待补充 | 待补充 | 待补充 |\n| 留存 / 复购 / 复用 | 待补充 | 待补充 | 待补充 | 待补充 |\n\n## 风险清单\n\n| 风险 | 概率 | 影响 | 缓解方式 |\n| --- | --- | --- | --- |\n| 待补充 | 中 | 高 | 待补充 |\n\n## 外部依赖\n\n| 依赖 | Owner | 状态 | 延误影响 |\n| --- | --- | --- | --- |\n| 待补充 | 待补充 | 待补充 | 待补充 |\n\n## 假设\n\n",
    "12-milestones.md": "# 里程碑\n\n## 阶段划分\n\n## 每阶段交付物\n\n## 风险缓冲\n\n",
}

PROTOTYPE_BRIEF = """# 原型 Brief

## 目标用户

1. 平台运营
2. 任务发布方
3. 学生个人 / 团队负责人
4. 高校管理员

## 页面目标

定义全量原型集的页面集合、信息层级和关键任务流，便于继续进入设计或前端实现。

## 原型范围原则

1. 默认交付全量原型集，不只覆盖主链路首页
2. 所有一级导航页面都应有原型
3. 所有核心业务对象都应覆盖列表页、详情页、创建/编辑页
4. 关键状态必须覆盖空态、加载态、失败态、无权限态
5. 不同角色的关键工作台必须分开呈现

## 页面覆盖清单

### 门户 / 品牌入口

1. 门户首页
2. 任务广场
3. 任务详情
4. 案例 / 成果页
5. 高校合作 / 入驻页

### 学生 / 团队端

1. 注册 / 认证页
2. 我的报名列表页
3. 我的项目列表页
4. 项目详情 / 执行页
5. 交付物提交页
6. 成长档案 / 认证页

### 任务方端

1. 任务方工作台
2. 新建任务页
3. 任务详情与报名筛选页
4. 立项确认页
5. 验收与归档页

### 高校管理端

1. 高校工作台
2. 学生 / 团队管理页
3. 校内项目看板
4. 成果统计页

### 运营后台

1. 运营总览页
2. 任务管理页
3. 高校管理页
4. 团队管理页
5. 项目验收页
6. 结算 / 记录页
7. 内容 / 案例运营页
8. 配置 / 权限页

## 信息层级

### 门户首页

1. 平台定位
2. 核心任务
3. 案例与成果
4. 入驻 / 报名入口

### 任务详情

1. 任务目标
2. 时间与报酬
3. 交付标准
4. 报名条件

### 工作台页面

1. 概览指标
2. 待办事项
3. 列表与筛选
4. 操作入口
5. 风险 / 异常提醒

## 关键流程

1. 浏览任务并报名
2. 审核报名并立项
3. 提交交付物并验收
4. 高校组织入驻与团队管理
5. 运营审核、配置与归档

## 风格方向

1. 专业可信
2. 年轻但克制
3. 适合高频信息浏览

## 组件清单

1. 顶部导航
2. 任务卡片
3. 进度时间轴
4. 状态标签
5. 数据看板
6. 列表筛选条
7. 审核抽屉 / 侧栏
8. 多角色工作台模块

## 响应式要求

1. 门户优先桌面端
2. 学生端兼顾移动端
3. 后台以桌面端为主

"""

PROTOTYPE_FLOW = """# 原型页面流转

## 页面关系图

```mermaid
flowchart LR
    A["门户首页"] --> B["任务广场"]
    B --> C["任务详情"]
    C --> D["报名表单 / 报名动作"]
    D --> E["我的项目"]
    E --> F["交付物提交 / 验收反馈"]
    G["任务方工作台"] --> H["新建任务"]
    H --> I["报名筛选"]
    I --> J["立项 / 项目跟进"]
    K["高校工作台"] --> L["学生 / 团队管理"]
    L --> M["校内项目看板"]
    N["运营后台"] --> O["任务管理"]
    O --> P["验收 / 结算"]
    N --> Q["高校 / 团队治理"]
```

## 页面清单

1. 门户首页：平台定位、任务入口、案例展示
2. 任务广场：筛选、排序、任务卡片
3. 任务详情：任务目标、要求、报名入口
4. 学生 / 团队端：报名、项目、交付、成长档案
5. 任务方端：新建任务、报名筛选、立项、验收
6. 高校端：组织管理、校内项目看板、成果统计
7. 运营后台：任务治理、高校治理、验收结算、配置权限

"""

WIREFRAME_NOTES = """# 低保真原型说明

## 首页线框要点

- 顶部导航
- 首屏价值主张
- 任务推荐区
- 合作案例区
- 底部 CTA

## 任务广场线框要点

- 搜索与筛选区
- 任务列表
- 状态 / 报酬 / 时间标签

## 后台页线框要点

- 统计概览
- 任务表格
- 报名侧栏
- 验收操作区

"""

PAGE_COVERAGE = """# 原型页面覆盖清单

## 交付要求

- [ ] 门户首页
- [ ] 任务广场
- [ ] 任务详情
- [ ] 案例 / 成果页
- [ ] 高校合作 / 入驻页
- [ ] 注册 / 认证页
- [ ] 我的报名列表页
- [ ] 我的项目列表页
- [ ] 项目详情 / 执行页
- [ ] 交付物提交页
- [ ] 成长档案 / 认证页
- [ ] 任务方工作台
- [ ] 新建任务页
- [ ] 任务详情与报名筛选页
- [ ] 立项确认页
- [ ] 验收与归档页
- [ ] 高校工作台
- [ ] 学生 / 团队管理页
- [ ] 校内项目看板
- [ ] 成果统计页
- [ ] 运营总览页
- [ ] 任务管理页
- [ ] 高校管理页
- [ ] 团队管理页
- [ ] 项目验收页
- [ ] 结算 / 记录页
- [ ] 内容 / 案例运营页
- [ ] 配置 / 权限页

## 状态覆盖

- [ ] 空态
- [ ] 加载态
- [ ] 失败态
- [ ] 无权限态

## 角色闭环

- [ ] 学生 / 团队主流程闭环
- [ ] 任务方主流程闭环
- [ ] 高校管理员主流程闭环
- [ ] 平台运营主流程闭环

"""


def slugify(value: str) -> str:
    text = value.strip().lower()
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    if not text:
        return "pm-case"
    return text


def write_if_missing(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="初始化产品经理交付工作目录")
    parser.add_argument("--title", required=True, help="项目或需求标题")
    parser.add_argument("--slug", help="目录 slug，默认由 title 派生")
    parser.add_argument(
        "--base-dir",
        default=".pd",
        help="工作目录路径，默认是当前目录下的 .pd/",
    )
    parser.add_argument(
        "--nested",
        action="store_true",
        help="在 base-dir 下追加 slug 子目录；默认直接写入 base-dir",
    )
    args = parser.parse_args()

    slug = args.slug or slugify(args.title)
    base_dir = Path(args.base_dir).expanduser().resolve()
    root = base_dir / slug if args.nested else base_dir

    write_if_missing(
        root / "brief/00-request.md",
        f"# 原始需求\n\n- 标题：{args.title}\n- 来源：待补充\n- 原始输入：待补充\n",
    )
    write_if_missing(
        root / "analysis/01-brainstorm.md",
        "# 头脑风暴\n\n## 需求摘要\n\n## 用户与场景\n\n## 方案备选\n\n## 推荐方案\n\n## 假设与待确认项\n",
    )
    write_if_missing(
        root / "analysis/02-jobs-product-lens.md",
        "# Jobs 产品判断\n\n## 一句话产品定义\n\n## Focus / Say No\n\n## End-to-end 体验原则\n\n## 用户真正会记住的瞬间\n\n## 哪些内容必须砍掉\n\n## 对 PRD 的写作指令\n\n",
    )

    for file_name, title in DOCS:
        write_if_missing(
            root / "prd" / file_name,
            DOC_TEMPLATES.get(file_name, f"# {title}\n\n"),
        )

    write_if_missing(
        root / "prototype/01-prototype-brief.md",
        PROTOTYPE_BRIEF,
    )
    write_if_missing(root / "prototype/02-screen-flow.md", PROTOTYPE_FLOW)
    write_if_missing(root / "prototype/03-wireframe-notes.md", WIREFRAME_NOTES)
    write_if_missing(root / "prototype/04-page-coverage-checklist.md", PAGE_COVERAGE)
    write_if_missing(
        root / "deck/01-deck-outline.md",
        "# 汇报 Deck 大纲\n\n## 受众\n\n## 核心信息\n\n## 逐页结构\n",
    )
    write_if_missing(
        root / "deck/02-deck-spec.json",
        json.dumps(
            {
                "title": args.title,
                "author": "Product Manager Skill",
                "footerText": "Generated by product-manager",
                "slides": [],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
    )
    write_if_missing(
        root / "ops/01-campaign-brief.md",
        "# 运营素材 Brief\n\n## 渠道\n\n## 目标受众\n\n## 卖点\n\n## 文案钩子\n\n## 视觉方向\n",
    )
    write_if_missing(
        root / "ops/02-creative-matrix.md",
        "# 创意矩阵\n\n| 渠道 | 受众 | 卖点 | 视觉方向 | 变体 |\n| --- | --- | --- | --- | --- |\n",
    )
    write_if_missing(root / "feishu/publish-plan.md", "# 飞书发布计划\n\n")
    write_if_missing(root / "feishu/publish-result.md", "# 飞书发布结果\n\n")

    manifest = {
        "project_title": args.title,
        "slug": slug,
        "folder_name": f"PRD - {args.title}",
        "documents": [
            {
                "title": title,
                "path": str((root / "prd" / file_name).resolve()),
            }
            for file_name, title in DOCS
        ],
    }
    (root / "feishu").mkdir(parents=True, exist_ok=True)
    (root / "feishu/manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(root)


if __name__ == "__main__":
    main()
