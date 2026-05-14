---
name: scripts
description: "Skill for the Scripts area of pd-skill. 21 symbols across 5 files."
---

# Scripts

21 symbols | 5 files | Cohesion: 95%

## When to Use

- Working with code in `subskills/`
- Understanding how slugify, write_if_missing, main work
- Modifying scripts-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `subskills/brainstorming/scripts/server.cjs` | isFullDocument, wrapInFrame, getNewestScreen, handleRequest, handleMessage (+6) |
| `scripts/init_pm_case.py` | slugify, write_if_missing, main |
| `scripts/feishu_wiki_targets.py` | build_base_cmd, run_json, main |
| `scripts/feishu_preflight.py` | run, main |
| `subskills/brainstorming/scripts/helper.js` | sendEvent, choice |

## Entry Points

Start here when exploring this area:

- **`slugify`** (Function) — `scripts/init_pm_case.py:498`
- **`write_if_missing`** (Function) — `scripts/init_pm_case.py:507`
- **`main`** (Function) — `scripts/init_pm_case.py:513`
- **`build_base_cmd`** (Function) — `scripts/feishu_wiki_targets.py:8`
- **`run_json`** (Function) — `scripts/feishu_wiki_targets.py:18`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `slugify` | Function | `scripts/init_pm_case.py` | 498 |
| `write_if_missing` | Function | `scripts/init_pm_case.py` | 507 |
| `main` | Function | `scripts/init_pm_case.py` | 513 |
| `build_base_cmd` | Function | `scripts/feishu_wiki_targets.py` | 8 |
| `run_json` | Function | `scripts/feishu_wiki_targets.py` | 18 |
| `main` | Function | `scripts/feishu_wiki_targets.py` | 30 |
| `run` | Function | `scripts/feishu_preflight.py` | 30 |
| `main` | Function | `scripts/feishu_preflight.py` | 40 |
| `isFullDocument` | Function | `subskills/brainstorming/scripts/server.cjs` | 106 |
| `wrapInFrame` | Function | `subskills/brainstorming/scripts/server.cjs` | 111 |
| `getNewestScreen` | Function | `subskills/brainstorming/scripts/server.cjs` | 115 |
| `handleRequest` | Function | `subskills/brainstorming/scripts/server.cjs` | 128 |
| `handleMessage` | Function | `subskills/brainstorming/scripts/server.cjs` | 223 |
| `touchActivity` | Function | `subskills/brainstorming/scripts/server.cjs` | 251 |
| `computeAcceptKey` | Function | `subskills/brainstorming/scripts/server.cjs` | 10 |
| `encodeFrame` | Function | `subskills/brainstorming/scripts/server.cjs` | 14 |
| `decodeFrame` | Function | `subskills/brainstorming/scripts/server.cjs` | 38 |
| `handleUpgrade` | Function | `subskills/brainstorming/scripts/server.cjs` | 166 |
| `broadcast` | Function | `subskills/brainstorming/scripts/server.cjs` | 239 |
| `sendEvent` | Function | `subskills/brainstorming/scripts/helper.js` | 25 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `HandleUpgrade → TouchActivity` | cross_community | 3 |

## How to Explore

1. `gitnexus_context({name: "slugify"})` — see callers and callees
2. `gitnexus_query({query: "scripts"})` — find related execution flows
3. Read key files listed above for implementation details
