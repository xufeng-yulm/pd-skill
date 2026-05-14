---
name: deliver-prd
description: Creates a comprehensive Product Requirements Document that aligns stakeholders on what to build, why, and how success will be measured. Use when specifying features, epics, or product initiatives for engineering handoff.
phase: deliver
version: "2.0.0"
updated: 2026-01-26
license: Apache-2.0
metadata:
  category: specification
  frameworks: [triple-diamond, lean-startup, design-thinking]
  author: product-on-purpose
---
<!-- PM-Skills | https://github.com/product-on-purpose/pm-skills | Apache 2.0 -->
# Product Requirements Document (PRD)

A Product Requirements Document is the primary specification artifact that communicates what to build and why. It bridges the gap between problem understanding and engineering implementation by providing clear requirements, success criteria, and scope boundaries. A good PRD enables engineering to build the right thing while maintaining flexibility on implementation details.

In this workspace, the PRD is expected to be presentation-grade rather than a plain wall of text. It should be easy to scan in a review meeting, with deliberate use of diagrams, summary blocks, structured tables, and visual hierarchy.

In this workspace, "presentation-grade" is still not enough by itself. The target quality bar is implementation-ready for V1 delivery: the downstream product, design, engineering, QA, and ops teams should be able to start real work from the PRD without translating it again.

## When to Use

- After problem and solution alignment, before engineering work begins
- When specifying features, epics, or product initiatives for handoff
- When multiple teams need to coordinate on a shared deliverable
- When stakeholders need to approve scope before investment
- As reference documentation during development and QA

## Instructions

When asked to create a PRD, follow these steps:

1. **Summarize the Problem**
   Start with a brief recap of the problem being solved. Link to the problem statement if available. Ensure readers understand *why* this work matters before diving into *what* to build.

2. **Define Goals and Success Metrics**
   Articulate what success looks like. Include specific, measurable metrics with baselines and targets. These metrics should connect directly to the problem being solved.

3. **Outline the Solution**
   Describe the proposed solution at a high level. Focus on user-facing functionality and key capabilities. Include enough detail for stakeholders to evaluate the approach without over-specifying implementation.

4. **Detail Functional Requirements**
   Break down what the system must do. Use user stories or requirement statements. Each requirement should be testable . someone should be able to verify if it's met.

5. **Define Scope Boundaries**
   Explicitly state what's in scope, out of scope, and deferred to future iterations. Clear scope prevents scope creep and sets realistic expectations.

6. **Address Technical Considerations**
   Note any technical constraints, architectural decisions, or integration requirements. Don't design the system, but surface considerations engineering needs to know.

7. **Identify Dependencies and Risks**
   List external dependencies, assumptions, and risks that could impact delivery. Include mitigation strategies where applicable.

8. **Propose Timeline and Milestones**
   Outline key phases and checkpoints. This helps stakeholders understand the delivery plan without committing to specific dates prematurely.

9. **Make It Visually Legible**
   Add the minimum visual scaffolding needed for fast comprehension:
   - an executive summary block
   - at least one system/experience diagram when the topic benefits from it
   - comparison or prioritization tables where tradeoffs matter
   - concise callouts for critical decisions, risks, or constraints
   - prefer editable text-native formats that can survive a Feishu publish flow; avoid SVG or screenshot-style diagrams as the default artifact
10. **Make It Implementation-Ready**
   For the core PRD set, strengthen each page so it can directly support execution:
   - keep `01-04` minimal and only preserve background required to understand the work
   - make `05-18` the real handoff surface for product, design, engineering, QA, and ops
   - add requirement-to-rule-to-service-to-test traceability where relevant
   - include direct next actions, owners, and release gates instead of abstract discussion prompts
   - add upstream/downstream chapter pointers when the document is part of a multi-file PRD

## Output Format

Use the template in `references/TEMPLATE.md` to structure the output.

## Quality Checklist

Before finalizing, verify:

- [ ] Problem and "why now" are clearly articulated
- [ ] Success metrics are specific and measurable
- [ ] Scope boundaries are explicit (in/out/future)
- [ ] Requirements are testable and unambiguous
- [ ] Technical considerations are surfaced without over-specifying
- [ ] Dependencies and risks are documented with owners
- [ ] Document is readable in under 15 minutes
- [ ] The document has enough visual structure that a stakeholder can scan it quickly
- [ ] Diagrams clarify the product or system rather than repeat prose
- [ ] The doc can support direct execution: design, engineering, QA, data, or ops can pick up work from it
- [ ] V1 scope is broken down deeply enough that engineering can estimate and split work

## Examples

See `references/EXAMPLE.md` for a completed example.
