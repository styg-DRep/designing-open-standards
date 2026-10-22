# Designing Open Standards

**A critical path for developing open standards in Cardano governance — built to be used with an AI agent, on your own machine.**

Governance runs on shared agreements: how proposals are written, what metadata travels with them, what words mean, how rationales are published, how reviews are done. When those agreements are made well, more people can take part and more tools can work together. When they are made badly — or made when they were not needed — they add cost, concentrate control, and decay.

This framework maps how to make them well. It is a network of inquiries, checkpoints and artifacts joined by typed edges, with phase gates that either let a standards effort proceed or send it back to the part of the map that needs more work. It is adapted from the Open Data Institute's open standards guidance and re-grounded in decentralized governance.

> **Status — v0.5.** Phase 1, **Scope and Start**, is mapped. Development, Launch and Adoption, and Review are next. See [ROADMAP.md](ROADMAP.md).

## What you can do with it

| | |
|---|---|
| **Guide** an effort | Walk a standards effort through scoping, node by node, and come out with a *Scope and Start Bundle*: the opportunity, the ecosystem, the case for (or against) a new standard, aims and a theory of change, a bounded scope, a development method and plan, a sustainability model, and the open questions that travel with the work. |
| **Audit** an effort | Assess an effort — or a standard already in use — against the 40 criteria of the Scope and Start gate. You get evidence-tagged findings, red flags, a recommended gate outcome, and where to go back to. |
| **Explore** the map | Ask what any node means, what feeds it, what it produces, and what a gate needs. |

Scoping can legitimately end in *reuse an existing standard*, *extend one*, *use a different intervention*, *pause* or *stop*. A process that cannot choose not to create a standard is not doing meaningful scoping.

## Quick start (with an AI agent)

1. **Get the folder.** On GitHub: **Code → Download ZIP**, then unzip. Or `git clone` it.
2. **Open it with an agent that can read local files.**
   - **Claude Code:** open a terminal in the folder and run `claude`. The repository's `CLAUDE.md` and four skills load automatically.
   - **Other coding agents** that follow the `AGENTS.md` convention: open the folder; `AGENTS.md` tells the agent where everything is and which playbook to follow.
3. **Ask.** For example:
   - *"Give me a five-minute orientation to this framework."*
   - *"Help us scope a standard for DRep voting rationales."* → guided session, files in `workspace/drep-voting-rationales/`
   - *"Audit this proposal template against the Scope and Start gate"* (attach or point to the material) → audit record in `workspace/<effort>/audits/`
   - *"Where do stakeholders come into the map, and what's the difference between a shaper and an early adopter?"*
   - *"We stopped last week at Frame the Opportunity — pick up from there."*

In Claude Code you can also call the playbooks directly: `/guide-standard`, `/audit-standard`, `/navigate-framework`, `/extend-framework`.

Your effort's files stay in your local `workspace/` folder and are git-ignored, so nothing about your effort is pushed back to this repository unless you choose to.

## Browse it in Obsidian

The framework is an [Obsidian](https://obsidian.md) vault. Open the **`framework/`** folder as a vault, then open `Open Standards Main Map/Updated Open Governance Standards Map.canvas`. The *Start and Scope* group is Phase 1; the cards on the right are the gate's inputs and its *returns-to* routes.

No Obsidian? [`map/INDEX.md`](map/INDEX.md) is a readable catalogue of every node, what it produces, and how it connects.

## The Scope and Start path

```
Simple Canvas
  → Frame the Opportunity  ⇄  Understand the Ecosystem      (consults Types of Standards)
        actors · relationships · governance data and infrastructure
        · existing standards (use instead / extend / open up) · tensions and control
        · who to work with · community stakeholders
  → Review Research and Feedback → Minimal Theory of Change → Aims and Objectives
        (core features · interoperability · adaptability · accessibility · real-world testing)
  → Development Principles
  → Choose Method → Plan Development ⇄ Think About Sustainability → Sustainability Gate → Approve
  → SCOPE AND START GATE → Development (next release)
```

The gate's question: *is there a sufficiently strong, evidence-informed, participatory and sustainable case for this standards effort to enter development?*

## What's in the repository

```
framework/        The framework itself — Markdown notes and Obsidian canvases (source of truth)
map/              Generated index: INDEX.md (readable) and graph.json (machine-readable)
toolkit/          Gate criteria crosswalk and YAML templates for every artifact and record
workspace/        Where your efforts live (git-ignored)
tools/            build_index.py (regenerate + check the map), canvas_text.py (read a canvas as text)
.claude/skills/   Playbooks: navigate-framework, guide-standard, audit-standard, extend-framework
AGENTS.md         Instructions for any AI agent
CLAUDE.md         Claude Code entry point (imports AGENTS.md)
```

## Using it without an agent

Everything an agent uses is plain text. Start at `framework/Open Standards Main Map/Simple Canvas.md`, follow the path above, and fill the templates in `toolkit/templates/`. To audit by hand, work through `toolkit/scope-gate-criteria.yaml` and record findings in `toolkit/templates/audit-record.yaml`.

## Contributing

Issues and pull requests are welcome — especially evidence from using the framework on real efforts. See [CONTRIBUTING.md](CONTRIBUTING.md). Maintainers extending the framework: the `extend-framework` playbook documents the conventions, and CI runs `python tools/build_index.py --check`.

## License and attribution

- Framework content, documentation, templates and playbooks: [CC BY-SA 4.0](LICENSE).
- Code in `tools/`: [MIT](LICENSE-CODE).

This work adapts material from the Open Data Institute's [Open Standards for Data guidebook](https://standards.theodi.org/), licensed CC BY-SA 4.0, and draws on other sources listed in [ATTRIBUTION.md](ATTRIBUTION.md).
