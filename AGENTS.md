# AGENTS.md

Instructions for AI agents working in this repository. People: see `README.md`.

## What this is

**Designing Open Standards** is a critical-path framework for developing open standards in Cardano governance — proposal templates, metadata schemas, shared vocabularies, rationale formats, review practices and the like. It is a map of nodes (inquiries, checkpoints, artifacts) joined by typed edges, with phase gates that either let an effort proceed or route it back.

All four phases are mapped: **Scope and Start**, **Development**, **Launch and Adoption**, and **Review and Update**. Each ends in a gate; returns-to routes send an effort back when a condition fails; *Update or Retire* closes the lifecycle into a loop.

People use this repository with an agent to do one of two things:

- **Guide** an effort through any phase, keeping its records and the bundle each gate produces.
- **Audit** an effort, or a standard already in use, against any gate.

## Layout

| Path | What | Edit? |
|---|---|---|
| `framework/` | The framework: Markdown notes + Obsidian canvases. **Source of truth.** | Only when asked to change the framework (see `extend-framework`) |
| `map/INDEX.md`, `map/graph.json` | Generated catalogue of every node, edge, returns-to route and artifact | Never by hand — `python tools/build_index.py` |
| `toolkit/<phase>-gate-criteria.yaml` | One per phase (`scope` 40, `develop` 32, `launch` 13, `review` 10 + 9): gate criteria (verbatim) with stable ids, nodes to consult, return routes, bundle components, red flags, baseline questions | When a gate changes |
| `toolkit/templates/` | YAML templates for every phase's artifacts, bundles and decision records, the effort tracker, and the audit record | Copy into a workspace; do not fill in place |
| `workspace/<effort-slug>/` | A user's effort: tracker, artifacts, audits | Yes — this is where work goes |
| `tools/` | `build_index.py` (map + checks), `canvas_text.py` (read a canvas as text), `fix_canvas_paths.py`, `canvas_format.py` | — |
| `.claude/skills/` | The playbooks below | — |

## Playbooks

Each is a `SKILL.md`. Claude Code loads them as skills. Other agents: read the file and follow it when the request matches.

| Playbook | Use when |
|---|---|
| `.claude/skills/navigate-framework/SKILL.md` | Someone asks what a node or concept means, where it lives, what connects to what, what a gate needs |
| `.claude/skills/guide-standard/SKILL.md` | Someone wants to start, scope, develop, launch, review or continue an effort (per-phase routes in `phases/`) |
| `.claude/skills/audit-standard/SKILL.md` | Someone wants an effort or existing standard assessed against a gate |
| `.claude/skills/extend-framework/SKILL.md` | Someone is changing the framework itself, adding a phase, or the map check fails |

If the request is unclear, ask which of *guide*, *audit* or *explore* they want. Most first-time users want a short orientation (the four phases, where their work sits, what the next gate asks) and then one of those.

## Ground rules

1. **The framework is the authority.** Answer from `framework/` and cite note paths. Do not substitute general knowledge of ODI, OpenStand, Theory of Change methods or Cardano governance for what the framework says. If it is silent, say so.
2. **Separate the framework from the interpretation layer.** The `toolkit/*-gate-criteria.yaml` files add ids, consult lists and routes that are not in the notes; say so when you rely on them.
3. **Tag evidence.** Claims about an effort or its ecosystem carry one of `observed`, `reported`, `inferred`, `assumed`, `contested`, `unknown`, and a source.
4. **Do not invent the ecosystem.** Never present actors, positions, adoption figures, tool behaviour or control relationships from memory as fact. Research only with a cited source, tag it `reported`, and have people confirm.
5. **Never decide for people.** Agents draft approval and readiness records; the people with standing make and record the decision. Do not mark gates passed, consent given, or standards certified.
6. **Preserve disagreement and uncertainty.** Competing frames, objections and unknowns are artifacts, not noise. Every open question gets a disposition.
7. **Keep "no new standard" live.** Reuse, extend, open up, another intervention, pause and stop are successful outcomes.
8. **Say where the map is silent.** Deprecate and retire are not routed, Update or Retire has no failure routes yet, and *Lifecycle Decision Record* is a stub (see `navigate-framework`). Do not fill those gaps with invented content.
9. **Keep returns and exits apart.** A returns-to route means a condition was not met. Update or Retire's exits (maintain, minor update, major update, rescope) mean a decision was made and a new cycle starts.

## Workspaces

One folder per effort: `workspace/<effort-slug>/`, starting from `toolkit/templates/effort.yaml`. The tracker holds the cycle and phase, node statuses, the baseline each gate produced, an append-only log, and open questions; artifacts sit beside it; audits go in `audits/`. Record the framework version (tag or `git rev-parse --short HEAD`) the effort used. Workspace contents are git-ignored by default so efforts are not accidentally pushed upstream.

## Commands

```bash
python tools/build_index.py            # regenerate map/ after any change in framework/ or toolkit/
python tools/build_index.py --check    # CI check: stale map, frontmatter, canvas links, toolkit ids
python tools/fix_canvas_paths.py       # repair canvas links after editing in a differently rooted vault
python tools/canvas_text.py "<canvas>" # print a canvas's cards in reading order (add --edges)
```

Requires Python 3.9+ and PyYAML (`pip install pyyaml`). Nothing else is needed to *use* the framework — agents can read `framework/` and `map/` directly.

## Style

Plain language with participants; precise language in records. Short questions, a few at a time. Use the framework's own terms (opportunity frame, standardization surface, coordination need, bundle, returns-to) and explain them the first time.
