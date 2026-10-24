# Designing Open Standards

**A critical path for developing open standards in Cardano governance — built to be used with an AI agent, on your own machine.**

Governance runs on shared agreements: how proposals are written, what metadata travels with them, what words mean, how rationales are published, how reviews are done. When those agreements are made well, more people can take part and more tools can work together. When they are made badly — or made when they were not needed — they add cost, concentrate control, and decay.

This framework maps how to make them well. It is a network of inquiries, checkpoints and artifacts joined by typed edges, with phase gates that either let a standards effort proceed or send it back to the part of the map that needs more work. It is adapted from the Open Data Institute's open standards guidance and re-grounded in decentralized governance.

> **Status — v0.6 (in progress).** All four phases are mapped: **Scope and Start**, **Development**, **Launch and Adoption**, **Review and Update**. Some routes are still open (see [ROADMAP.md](ROADMAP.md)).

## What you can do with it

| | |
|---|---|
| **Guide** an effort | Walk a standards effort through whichever phase it is in, node by node. Each phase ends in a bundle that becomes the next phase's baseline: the *Scope and Start Bundle* (the case for — or against — a new standard), the *Development Outcomes Bundle* (a tested, documented candidate), the *Launch and Adoption Outcomes Bundle* (what real use showed), and a *Lifecycle Decision Record* (maintain, update, rescope, deprecate or retire). |
| **Audit** an effort | Assess an effort — or a standard already in use — against any gate. You get evidence-tagged findings, red flags, a recommended outcome, and where to go back to. |
| **Explore** the map | Ask what any node means, what feeds it, what it produces, and what a gate needs. |

Scoping can legitimately end in *reuse an existing standard*, *extend one*, *use a different intervention*, *pause* or *stop*. A process that cannot choose not to create a standard is not doing meaningful scoping. Later, retiring a standard can be just as much a success.

## Quick start (with an AI agent)

1. **Get the folder.** On GitHub: **Code → Download ZIP**, then unzip. Or `git clone` it.
2. **Open it with an agent that can read local files.**
   - **Claude Code:** open a terminal in the folder and run `claude`. The repository's `CLAUDE.md` and four skills load automatically.
   - **Other coding agents** that follow the `AGENTS.md` convention: open the folder; `AGENTS.md` tells the agent where everything is and which playbook to follow.
3. **Ask.** For example:
   - *"Give me a five-minute orientation to this framework."*
   - *"Help us scope a standard for DRep voting rationales."* → guided session, files in `workspace/drep-voting-rationales/`
   - *"Audit this proposal template against the Scope and Start gate"* (attach or point to the material) → audit record in `workspace/<effort>/audits/`
   - *"Our schema has two implementations — are we ready to launch?"* → Development Outcomes gate
   - *"This standard has been in use for a year. Should we review it?"*
   - *"Where do stakeholders come into the map, and what's the difference between a shaper and an early adopter?"*
   - *"We stopped last week at Frame the Opportunity — pick up from there."*

In Claude Code you can also call the playbooks directly: `/guide-standard`, `/audit-standard`, `/navigate-framework`, `/extend-framework`.

Your effort's files stay in your local `workspace/` folder and are git-ignored, so nothing about your effort is pushed back to this repository unless you choose to.

## Browse it in Obsidian

The repository is an [Obsidian](https://obsidian.md) vault. Open the **repository folder itself** as a vault (*Open folder as vault*), then open `framework/Open Standards Main Map/Updated Open Governance Standards Map.canvas`. Each phase has its own group; the *Returns-to routes* group on the right holds the conditions under which a node sends an effort back to an earlier part of the map. Opening the vault at the repository root also puts your `workspace/` efforts and the generated `map/INDEX.md` beside the framework.

No Obsidian? [`map/INDEX.md`](map/INDEX.md) is a readable catalogue of every node, what it produces, and how it connects.

## The lifecycle

```
SCOPE AND START ──▶ DEVELOPMENT ──▶ LAUNCH AND ADOPTION ──▶ REVIEW AND UPDATE ──┐
       ▲                 ▲                    ▲                                 │
       │                 │                    └──────── maintain ───────────────┤
       │                 └───────────────────────────── minor update ───────────┤
       └─────────────────────────────────────────────── major update / rescope ─┘
```

*Update or Retire*, the last gate, re-enters the map: **maintain** → Monitor Adoption, **minor update** → Develop the Standard, **major update** → the Scope and Start gate, **rescope** → Frame the Opportunity. Every phase also has *returns-to* routes back to earlier nodes when a condition is not met.

Each phase ends in a gate:

| Gate | Asks |
|---|---|
| Scope and Start | Is there a sufficiently strong, evidence-informed, participatory and sustainable case for this standards effort to enter development? |
| Development Outcomes | Has the effort produced a sufficiently stable, tested, documented, implementable and inspectable agreement to justify wider exposure and adoption? |
| Launch and Adoption Outcomes | Has the standard encountered enough reality that we can meaningfully evaluate what should happen next? |
| Review Outcomes → Update or Retire | Do we understand the standard's present fitness well enough to decide — and what lifecycle path should it now enter? |

## What's in the repository

```
framework/        The framework itself — Markdown notes and Obsidian canvases (source of truth)
map/              Generated index: INDEX.md (readable) and graph.json (machine-readable)
toolkit/          Gate criteria for each phase and YAML templates for every artifact and record
workspace/        Where your efforts live (git-ignored)
tools/            build_index.py (regenerate + check the map), canvas_text.py, fix_canvas_paths.py, canvas_format.py
.claude/skills/   Playbooks: navigate-framework, guide-standard, audit-standard, extend-framework
AGENTS.md         Instructions for any AI agent
CLAUDE.md         Claude Code entry point (imports AGENTS.md)
```

## Using it without an agent

Everything an agent uses is plain text. Start at `framework/Open Standards Main Map/Phase 1 Scope and Start/Simple Canvas.md` (or the entry node of the phase you are in), use [`map/INDEX.md`](map/INDEX.md) to follow the edges, and fill the templates in `toolkit/templates/`. To audit by hand, work through the gate's file in `toolkit/` (`scope-`, `develop-`, `launch-` or `review-gate-criteria.yaml`) and record findings in `toolkit/templates/audit-record.yaml`.

## Contributing

Issues and pull requests are welcome — especially evidence from using the framework on real efforts. See [CONTRIBUTING.md](CONTRIBUTING.md). Maintainers extending the framework: the `extend-framework` playbook documents the conventions, and CI runs `python tools/build_index.py --check`.

## License and attribution

- Framework content, documentation, templates and playbooks: [CC BY-SA 4.0](LICENSE).
- Code in `tools/`: [MIT](LICENSE-CODE).

This work adapts material from the Open Data Institute's [Open Standards for Data guidebook](https://standards.theodi.org/), licensed CC BY-SA 4.0, and draws on other sources listed in [ATTRIBUTION.md](ATTRIBUTION.md).
