# Changelog

Node ids are filename slugs. Renames are listed here as old → new id so workspaces and audit records can follow them.

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
