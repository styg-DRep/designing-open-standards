---
name: navigate-framework
description: Find, explain and trace concepts in the Designing Open Standards framework map. Use when someone asks what a node or concept means, where something lives in the map, what feeds into or follows a node, what a gate requires, which node produces an artifact, or how two parts of the map connect, e.g. "where do stakeholders come in?", "what does the Scope and Start gate need?", "what is a standardization surface?", "what happens after Frame the Opportunity?".
---

# Navigate the framework

Answer questions about the map from the map itself. The framework is the authority; you are a guide to it.

## Sources, in order of authority

1. **`framework/`** — the notes and canvases (an Obsidian vault). Authoritative. Quote and cite these.
2. **`map/INDEX.md`** and **`map/graph.json`** — generated from `framework/` by `tools/build_index.py`. Use them to find things and trace edges fast; confirm meaning in the note itself.
3. **`toolkit/scope-gate-criteria.yaml`** — an interpretation layer (criterion ids, which nodes to consult, return routes). Say so when you lean on it.

Do not answer from general knowledge of ODI, OpenStand, Theory of Change methods or Cardano governance when the question is about what *this framework* says. If the framework is silent, say it is silent.

## Procedure

1. **Resolve the concept.** Match it against node titles in `map/INDEX.md`, then the *Artifacts → producing nodes* table, then the concept locator below. If nothing matches, search the notes: `grep -ril "<term>" framework/ --include=*.md`.
2. **Read the note(s)** in full. Most checkpoint notes follow: Intent → Inputs → Core principle → Patterns → artifact template → Gate condition (numbered questions) → Possible outcomes → topology.
3. **Trace connections** from `map/graph.json`: `edges` (with the canvas label as `label` and a slugged `relation`), `returns_to` (gate routes when a condition fails), `placeholders` (unmapped next steps). Use the edge labels verbatim — *Feeds*, *Informs*, *Produces*, *Checks*, *Enables us to*, *returns to*. Unlabelled edges appear as `connects`; describe them as a plain connection, not a typed one.
4. **Answer** briefly, citing note paths. When the question is "what next?", give the next node(s) by edge *and* the gate question that decides whether you are ready to move.

If `map/` looks out of date relative to `framework/`, run `python tools/build_index.py`.

## The critical path (Scope and Start)

From the gate note's *Initial Macro Topology*. It is a map with reciprocal loops, not a pipeline.

```
Simple Canvas
  → Frame the Opportunity  ⇄  Understand Ecosystem        (consults Types of Standards)
        ecosystem cluster: Identify People and Groups (producers / users / exchangers) → Actor Map
          → Understand Relationships · Understand Governance Data and Infrastructure
          · Identify Current Ecosystem Standards (Used Instead / Extended / Opened Up) → Ecosystem Map
          → Surface Ecosystem Tensions · Decide Who To Work With → Identify Community Stakeholders
  → Review Research and Feedback → Minimal Theory of Change → Decide On Aims and Objectives
        (Core Features · Interoperability Intent · Adaptability and Extensibility
         · Accessibility and Translation · Real-World Testnet)
  → Development Principles
  → 1 Choose the Development Method → 2 Plan the Development ⇄ Think about sustainability (six forms)
        (the six sustainability forms also feed Operational Guidance for Producers)
  → Sustainability Gate → 3 Approve Development → The Development Method (checkpoint)
  → Scope and Start (Phase Gate) → [Development: not yet mapped]
```

Note when it matters: on the canvas, the ecosystem cluster reaches the rest of the path through *Understand Ecosystem —Updates→ Simple Canvas* and the reciprocal loop with *Frame the Opportunity*; the gate note's topology also draws Ecosystem → Aims & Objectives.

## Concept locator

| Concept | Where |
|---|---|
| Opportunity frame, coordination need, need vs demand, counterfactual, competing frames, frame at the right scale | Frame the Opportunity |
| Standardization surface, three families, strength of standardization, minimum necessary surface | Types of Standards (+ Shared Vocabularies, Information Exchange, Provide Guidance) |
| Evidence tags `observed / reported / inferred / assumed / contested / unknown` | Frame the Opportunity; Ecosystem Map |
| Earn the right to create; "no new standard" as success | What Can Be Used Instead; Scope and Start gate |
| Standards archaeology; de facto conventions | Identify Current Ecosystem Standards |
| Invention vs enclosure | What Can Be Opened Up |
| Actor → activity → object; object → activity → actor; actor → task → interface → dependency | Identify People and Groups; Producers…; Users… |
| Follow the transformations; where information "ceases to be the same thing" | Exchanging of Governance Information |
| Trace one governance object | Understand Governance Data and Infrastructure |
| Follow the dependency | Understand Relationships Between People and Groups |
| Locate the veto and the exit; syndicating actors; control as a relationship | Surface Ecosystem Tensions |
| Representation is not participation; participation states | Identify Community Stakeholders |
| Shapers / testers / advocates; cohort, not audience | Decide Who To Work With |
| Aim vs objective vs feature vs measure; contribution vs control | Decide On Aims and Objectives |
| Minimal ToC chain; mechanisms; escalate to full ToC | Minimal Theory of Change (+ Theory of Change canvas) |
| Aim → objective → capability → feature traceability | Identify Core Features |
| Stable core and open edge | Adaptability and Extensibility |
| Interoperable with what, for what purpose | Interoperability Intent |
| Method spectrum; least heavy process | 1- Choose the Development Method |
| Development units; testing types; contribution vs decision | 2- Plan the Development |
| Approval forms; approval is a record | 3- Approve Development |
| Six forms of sustainability; minimum sustainable standard; maintenance surface; stable/living/generated/external; retirement path | Think about sustainability and its six sub-notes |
| Heroic maintenance; survive its website; price the future; adopter's cost | Community / Technical / Resource / Adoption Sustainability |
| Scope and Start Bundle; development case; readiness record; ten gate outcomes; first audit boundary; crossing the gate creates obligations | Scope and Start (Phase Gate) |

## Canvases

- `framework/Open Standards Main Map/Updated Open Governance Standards Map.canvas` — the map. Group *Start and Scope*; returns-to routes; *Development* placeholder.
- `framework/Open Standards Simple Canvas/Simple Canvas For Open Standards.canvas` — the fill-in canvas (START / WHY / WHO / HOW, 12 steps) with examples.
- `framework/Theory of Change/Theory of change - Four principles of Change.canvas` — text-only systems-change explorer (tension, What? / So what? / Now what?, coherence and simple rules). Read it with `python tools/canvas_text.py "<path>"`.

## Phase boundary

Only **Scope and Start** is mapped. Development, Launch and Adoption, and Review are not. When asked about them, say so, then point to the forward hooks already in the Scope notes:

- *Think about sustainability* / *Sustainability Gate* — sustainability as a lifecycle concern through Develop, Launch, Review.
- *Minimal Theory of Change* — Review —returns-to→ Theory of Change.
- *Types of Standards*, *Shared Vocabularies*, *Information Exchange*, *Provide Guidance* — tagged for develop and review.
- *Scope and Start (Phase Gate)* — "The Bundle Is the First Audit Boundary" and "Crossing the Gate Creates Obligations".

Do not invent content for unmapped phases.
