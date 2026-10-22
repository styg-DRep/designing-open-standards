# AGENTS.md

Instructions for AI agents working in this repository. People: see `README.md`.

## What this is

**Designing Open Standards** is a critical-path framework for developing open standards in Cardano governance — proposal templates, metadata schemas, shared vocabularies, rationale formats, review practices and the like. It is a map of nodes (inquiries, checkpoints, artifacts) joined by typed edges, with phase gates that either let an effort proceed or route it back.

This release maps **Phase 1: Scope and Start** only. Development, Launch and Adoption, and Review are not yet mapped.

People use this repository with an agent to do one of two things:

- **Guide** an effort through scoping, producing a *Scope and Start Bundle*.
- **Audit** an effort (or an existing standard) against the Scope and Start gate.

## Layout

| Path | What | Edit? |
|---|---|---|
| `framework/` | The framework: Markdown notes + Obsidian canvases. **Source of truth.** | Only when asked to change the framework (see `extend-framework`) |
| `map/INDEX.md`, `map/graph.json` | Generated catalogue of every node, edge, returns-to route and artifact | Never by hand — `python tools/build_index.py` |
| `toolkit/scope-gate-criteria.yaml` | The gate's 40 criteria (verbatim) with stable ids, nodes to consult, return routes, bundle components, red flags | When the gate changes |
| `toolkit/templates/` | YAML templates for each artifact, the effort tracker, the readiness record and the audit record | Copy into a workspace; do not fill in place |
| `workspace/<effort-slug>/` | A user's effort: tracker, artifacts, audits | Yes — this is where work goes |
| `tools/` | `build_index.py` (map + checks), `canvas_text.py` (read a canvas as text) | — |
| `.claude/skills/` | The playbooks below | — |

## Playbooks

Each is a `SKILL.md`. Claude Code loads them as skills. Other agents: read the file and follow it when the request matches.

| Playbook | Use when |
|---|---|
| `.claude/skills/navigate-framework/SKILL.md` | Someone asks what a node or concept means, where it lives, what connects to what, what a gate needs |
| `.claude/skills/guide-standard/SKILL.md` | Someone wants to start, scope or continue an effort |
| `.claude/skills/audit-standard/SKILL.md` | Someone wants an effort or existing standard assessed against the gate |
| `.claude/skills/extend-framework/SKILL.md` | Someone is changing the framework itself, adding a phase, or the map check fails |

If the request is unclear, ask which of *guide*, *audit* or *explore* they want. Most first-time users want a short orientation (what the phase is for, the route, the gate) and then one of those.

## Ground rules

1. **The framework is the authority.** Answer from `framework/` and cite note paths. Do not substitute general knowledge of ODI, OpenStand, Theory of Change methods or Cardano governance for what the framework says. If it is silent, say so.
2. **Separate the framework from the interpretation layer.** `toolkit/scope-gate-criteria.yaml` adds ids, consult lists and routes that are not in the notes; say so when you rely on them.
3. **Tag evidence.** Claims about an effort or its ecosystem carry one of `observed`, `reported`, `inferred`, `assumed`, `contested`, `unknown`, and a source.
4. **Do not invent the ecosystem.** Never present actors, positions, adoption figures, tool behaviour or control relationships from memory as fact. Research only with a cited source, tag it `reported`, and have people confirm.
5. **Never decide for people.** Agents draft approval and readiness records; the people with standing make and record the decision. Do not mark gates passed, consent given, or standards certified.
6. **Preserve disagreement and uncertainty.** Competing frames, objections and unknowns are artifacts, not noise. Every open question gets a disposition.
7. **Keep "no new standard" live.** Reuse, extend, open up, another intervention, pause and stop are successful outcomes.
8. **Stay inside the mapped phase.** Do not improvise Development, Launch or Review content. Point to the forward hooks listed in `navigate-framework`.

## Workspaces

One folder per effort: `workspace/<effort-slug>/`, starting from `toolkit/templates/effort.yaml`. The tracker holds node statuses, an append-only log, and open questions; artifacts sit beside it; audits go in `audits/`. Record the framework version (tag or `git rev-parse --short HEAD`) the effort used. Workspace contents are git-ignored by default so efforts are not accidentally pushed upstream.

## Commands

```bash
python tools/build_index.py            # regenerate map/ after any change in framework/ or toolkit/
python tools/build_index.py --check    # CI check: stale map, frontmatter, canvas links, toolkit ids
python tools/canvas_text.py "<canvas>" # print a canvas's cards in reading order (add --edges)
```

Requires Python 3.9+ and PyYAML (`pip install pyyaml`). Nothing else is needed to *use* the framework — agents can read `framework/` and `map/` directly.

## Style

Plain language with participants; precise language in records. Short questions, a few at a time. Use the framework's own terms (opportunity frame, standardization surface, coordination need, bundle, returns-to) and explain them the first time.
