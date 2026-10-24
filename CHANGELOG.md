# Changelog

Node ids are filename slugs. Renames are listed here as old → new id so workspaces and audit records can follow them.

## Unreleased — Phases 2–4 (#1)

Added
- Phase 2 Development, Phase 3 Launch and Adoption, Phase 4 Review and Update: 26 notes, with phase gates *Development Outcomes*, *Launch and Adoption Outcomes* and *Update or Retire*, plus *Review Outcomes* inside Review.
- 28 returns-to routes wired on the main canvas from Development Phase, Development Outcomes, Launch and Adoption, Launch and Adoption Outcomes and Review Outcomes, in a *Returns-to routes* group to be tidied into the phases. Returns to "Scope and Start" point at the Scope and Start gate.
- **Lifecycle loop:** Update or Retire's labelled exits (maintain → Monitor Adoption, minor update → Develop the Standard, major update → Scope and Start gate, rescope → Frame the Opportunity), and a stub *Lifecycle Decision Record* (`lifecycle-decision-record`) that the gate produces and each re-entry node takes as its baseline.
- **Agent layer for all four phases:**
  - `toolkit/develop-gate-criteria.yaml` (32 criteria), `launch-gate-criteria.yaml` (13), and `review-gate-criteria.yaml` (Review Outcomes 10, Update or Retire 9, failure routes open).
  - Templates `development-work`, `development-outcomes-bundle`, `launch`, `launch-and-adoption-outcomes`, `review`, `lifecycle-decision-record`.
  - The effort tracker gains `cycle`, `phase` and `baselines`; the audit record names its gate, criteria file and cycle.
- **Playbooks:**
  - `guide-standard` covers every phase, with per-phase routes in `phases/`.
  - `audit-standard` audits any gate.
  - `navigate-framework` covers the whole lifecycle and says where the map is still silent.
  - `extend-framework` documents exits, decomposition and the open development targets.
  - AGENTS.md, CLAUDE.md, README, ROADMAP and the workspace README are updated to match.
- `tools/fix_canvas_paths.py` (repairs canvas links after editing in a differently rooted vault) and `tools/canvas_format.py` (writes canvas JSON in Obsidian's own layout so diffs stay small).

Changed
- **The repository root is now the Obsidian vault.** Canvas links are relative to the repository root and start with `framework/`. `framework/.obsidian/` is retired.
- **Renamed** *Accessibility and Translation* → *Inclusivity* (id `accessibility-and-translation` → `inclusivity`), to separate it from Development's *Translation and Accessibility*, and rewrote it around inclusion across development, use, governance and consequence (adds `inclusivity-intent`; the Aims template's `accessibility_intent` becomes `inclusivity_intent`).
- Notes moved into one folder per phase (`Open Standards Main Map/Phase 1 Scope and Start/`, …). No other ids changed.
- Imported notes: fenced ` ```yaml ` metadata converted to frontmatter; minimal frontmatter added to 7 notes; `gate: phase` on the three new phase gates; *Develop the Standard* `role: outcome` → `entry-point`.
- Drafted one-sentence *Intent* sections for 7 notes that had none (Decision and Provenance Record, Examples, Roles and Responsibilities, Structured Documentation, Translation and Accessibility, Key Review Questions, Review Process).
- Removed single sentences that restated outside guidance under the wrong attribution ("we should…", "Cardano governance emphasizes…", "the constitutional tenets suggest…") from Information Exchange, Provide Guidance, Shared Vocabularies, Development Phase, Development Platform, Documentation, Roles and Responsibilities, Share Progress, Team and Testing.
- Main canvas: two cards that pointed at copies inside another folder repointed; edge label typo "may generatre" fixed.
- `tools/build_index.py`: gates in lifecycle order with their next-phase edges; returns-to routes from non-gate nodes listed; quoted intents captured; canvas links checked against the repository root.

## 0.5.0 — 2026-10-21

First repository release. Framework content is the author's v0.5 vault (Phase 1: Scope and Start).

Added
- Repository structure: `framework/` (the vault), generated `map/`, `toolkit/` (gate criteria crosswalk, templates), `workspace/`, `tools/`.
- Agent support: `AGENTS.md`, `CLAUDE.md`, and four playbooks in `.claude/skills/` — navigate-framework, guide-standard, audit-standard, extend-framework.
- `tools/build_index.py` (index + CI check) and `tools/canvas_text.py`.
- Licenses (CC BY-SA 4.0 for content; MIT for code), attribution, roadmap, contributing guide, CI workflow.

Changed while importing the vault (no change to note bodies except where stated)
- Metadata written as fenced ` ```yaml ` blocks at the top of notes converted to real YAML frontmatter.
- Minimal frontmatter (`phase`, `domain`, `role`, `status`) added to the 18 notes that had none; `gate: phase` added to *Scope and Start (Phase Gate)*.
- *Actor Map* (empty) given a stub body assembled from the gate note's Actor Map component and its canvas edges; `status: stub`.
- Canvas file references re-rooted to the vault (they pointed at the author's parent folders).
- Removed the empty, unlinked note `Accessibility.md`.
- Removed a Simple Canvas card linking `General notes/Examples.md`, which is not in the vault.
- Personal Obsidian UI state (`workspace.json`) not included.
