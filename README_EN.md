<div align="center">

<img src="assets/logo.svg" alt="pd-skill logo" width="96" height="96" />

# pd-skill

<p><strong>AI-native product documentation system for visual PRDs, Feishu publishing, prototype briefs, and launch-ready planning.</strong></p>

<p>
  <img src="https://img.shields.io/badge/PRD-18%20Docs-2563EB?style=flat-square" alt="18 doc PRD" />
  <img src="https://img.shields.io/badge/Publishing-Feishu%20Wiki-0F766E?style=flat-square" alt="Feishu Wiki" />
  <img src="https://img.shields.io/badge/Visuals-Mermaid%20Native-7C3AED?style=flat-square" alt="Mermaid Native" />
  <img src="https://img.shields.io/badge/Lens-Jobs%20Product%20Review-F59E0B?style=flat-square" alt="Jobs Lens" />
</p>

<p>
  English · <a href="./README.md">中文</a>
</p>

<p>
  <a href="#overview">Overview</a> ·
  <a href="#what-it-produces">What It Produces</a> ·
  <a href="#workflow">Workflow</a> ·
  <a href="#quick-start">Quick Start</a> ·
  <a href="#feishu-publishing">Feishu Publishing</a>
</p>

<img src="assets/banner.svg" alt="pd-skill banner" width="100%" />

</div>

---

## Overview

`pd-skill` is not a single PRD prompt. It is a full delivery system for turning one product request into a structured artifact set:

- requirement analysis
- Jobs-style product judgment
- multi-document PRD
- editable visual diagrams
- prototype brief and handoff
- Feishu wiki publishing
- deck outline and ops brief

The default output is designed for real review meetings, not just markdown storage. The documents are meant to be readable by product, design, engineering, operations, and management without rewriting the same context in five different places.

## Why It Exists

Most AI-generated PRDs fail in predictable ways:

- they are too short
- they are too generic
- they collapse strategy, UX, and execution into one page
- they look finished, but they are not reviewable
- they publish poorly into Feishu because diagrams become static

`pd-skill` solves that by forcing:

1. structured brainstorming
2. a Jobs-style product lens
3. multi-document separation by audience and concern
4. editable visuals first
5. explicit publishing rules for Feishu wiki delivery

## What It Produces

### Core Analysis

| Artifact | Purpose |
| --- | --- |
| `analysis/01-brainstorm.md` | Problem framing, assumptions, solution options, recommendation |
| `analysis/02-jobs-product-lens.md` | One-line definition, focus decisions, experience principles, what to cut |

### PRD System

The PRD is intentionally split into 18 documents so each page can stay focused and still feel complete:

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

### Supporting Deliverables

| Directory | Purpose |
| --- | --- |
| `prototype/` | Prototype brief, screen flow, page coverage checklist |
| `deck/` | Deck outline and JSON presentation spec |
| `ops/` | Ops brief and creative matrix |
| `feishu/` | Manifest, publishing plan, publishing result |

## Design Standards

This skill ships PRDs with a stronger visual and editorial standard than plain markdown notes.

### Visual Language

- Mermaid-first diagrams
- summary cards and review boards
- comparison matrices
- milestone swimlanes
- hierarchy tables
- screenshot / reference-image slots with captions

### Feishu-first Rules

Core diagrams must remain editable after publishing. The default order of preference is:

1. `Mermaid`
2. Markdown tables
3. numbered structure blocks

Static graphics are allowed as support material, not as the primary source of structure. That is why PRD-level architecture, journey, funnel, and IA content should not depend on `SVG`, `PNG`, or screenshots alone.

## Workflow

```mermaid
flowchart LR
    A["User request"] --> B["Init workspace"]
    B --> C["Brainstorm"]
    C --> D["Jobs product lens"]
    D --> E["18-doc PRD generation"]
    E --> F["Feishu publish decision"]
    F --> G["Prototype brief / prototype"]
    G --> H["Deck + ops outputs"]
```

### Standard Execution Order

1. initialize the working directory
2. generate brainstorming output
3. generate the Jobs review layer
4. generate the multi-document PRD
5. ask whether to publish to Feishu
6. publish to wiki or drive if requested
7. continue to prototype / deck / ops outputs as needed

## What Makes It Different

| Area | Typical PRD prompt | `pd-skill` |
| --- | --- | --- |
| Scope | Single markdown page | 18-document system |
| Product judgment | Usually absent | Explicit Jobs-style filter |
| Visual quality | Mostly text | diagrams, tables, review cards, reference slots |
| Feishu publishing | Ad hoc | explicit wiki path rules |
| Editing after publish | Often poor | Feishu-native structures first |
| Handoff quality | Generic | product, design, eng, ops-ready split |

## Example Output Tree

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

## Quick Start

Create a working case in the current project:

```bash
python3 scripts/init_pm_case.py --title "需求标题"
```

Create a nested case directory:

```bash
python3 scripts/init_pm_case.py --title "需求标题" --nested
```

## Feishu Publishing

This skill does not auto-publish by default. Publishing starts only after the user explicitly asks for it.

### Default Wiki Structure

The recommended publishing path is:

```text
知识库 -> 产品部门 -> 产品名
```

Example:

```text
知识库 -> 产品部门 -> 产品1
```

Then the skill writes the full multi-document PRD into `产品1`.

### Publish Flow

1. run `scripts/feishu_preflight.py`
2. confirm wiki target, usually `知识库 -> 产品部门`
3. locate the `产品部门` node
4. create the product node, for example `产品1`
5. publish all PRD docs from `feishu/manifest.json` into that node

### Preflight Checks

- Feishu CLI is available
- auth and scopes are valid
- wiki path is confirmed
- product department node is confirmed
- product name is confirmed
- core diagrams remain editable after publish

## Capability Matrix

| Capability | Included |
| --- | --- |
| Brainstorming | Yes |
| Jobs-style product review | Yes |
| Visual PRD structure | Yes |
| Editable Mermaid diagrams | Yes |
| Feishu wiki publishing | Yes |
| Prototype brief | Yes |
| Deck output | Yes |
| Ops creative brief | Yes |

## Repository Layout

| Path | Role |
| --- | --- |
| [SKILL.md](./SKILL.md) | Master orchestration contract |
| [references/artifact-structure.md](./references/artifact-structure.md) | Output tree and minimum delivery structure |
| [references/feishu-publishing.md](./references/feishu-publishing.md) | Feishu publishing workflow |
| [subskills/deliver-prd/references/TEMPLATE.md](./subskills/deliver-prd/references/TEMPLATE.md) | PRD template reference |
| [scripts/init_pm_case.py](./scripts/init_pm_case.py) | Workspace scaffold generator |

## Notes

- The PRD system is intentionally verbose enough to feel like a real internal launch document, not a note dump.
- Visual richness is constrained by editability. Feishu-native structures win over pretty but static output.
- Images are allowed, but captions are required and the structure cannot depend on the image alone.
