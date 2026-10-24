---
name: navigate-framework
description: Find, explain and trace concepts anywhere in the Designing Open Standards framework map — all four phases (Scope and Start, Development, Launch and Adoption, Review and Update), their gates, returns-to routes and lifecycle loop. Use when someone asks what a node or concept means, where something lives, what feeds into or follows a node, what a gate requires, which node produces an artifact, where a route leads back to, or how two parts of the map connect, e.g. "where do stakeholders come in?", "what does the Development Outcomes gate need?", "what happens after a standard is retired?", "what is a standardization surface?".
---

# Navigate the framework

Answer questions about the map from the map itself. The framework is the authority; you are a guide to it.

## Sources, in order of authority

1. **`framework/`** — the notes and canvases (an Obsidian vault). Authoritative. Quote and cite these.
2. **`map/INDEX.md`** and **`map/graph.json`** — generated from `framework/` by `tools/build_index.py`. Use them to find things and trace edges fast; confirm meaning in the note itself.
3. **`toolkit/*-gate-criteria.yaml`** — one per phase; an interpretation layer (criterion ids, which nodes to consult, return routes). Say so when you lean on it.

Do not answer from general knowledge of ODI, OpenStand, Theory of Change methods or Cardano governance when the question is about what *this framework* says. If the framework is silent, say it is silent.

## Procedure

1. **Resolve the concept.** Match it against node titles in `map/INDEX.md`, then the *Artifacts → producing nodes* table, then the concept locator below. If nothing matches, search the notes: `grep -ril "<term>" framework/ --include=*.md`.
2. **Read the note(s)** in full. Most checkpoint notes follow: Intent → Inputs → Core principle → Patterns → artifact template → Gate condition (numbered questions) → Possible outcomes → topology.
3. **Trace connections** from `map/graph.json`: `edges` (with the canvas label as `label` and a slugged `relation`), `returns_to` (routes back when a condition fails), `placeholders` (unmapped next steps). Use the edge labels verbatim — *Feeds*, *Informs*, *Produces*, *Checks*, *Enables us to*, *returns to*. Unlabelled edges appear as `connects`; describe them as a plain connection, not a typed one.
4. **Answer** briefly, citing note paths. When the question is "what next?", give the next node(s) by edge *and* the gate question that decides whether you are ready to move.

If `map/` looks out of date relative to `framework/`, run `python tools/build_index.py`.

## The lifecycle

Four phases joined by gates. It is a map with reciprocal loops and returns-to routes, not a pipeline, and Update or Retire closes it into a cycle.

```
PHASE 1  SCOPE AND START
Simple Canvas → Frame the Opportunity ⇄ Understand Ecosystem (consults Types of Standards)
   ecosystem cluster: Identify People and Groups → Actor Map → Understand Relationships · Governance Data and
   Infrastructure · Identify Current Ecosystem Standards (Used Instead / Extended / Opened Up) → Ecosystem Map
   → Surface Ecosystem Tensions · Decide Who To Work With → Identify Community Stakeholders
→ Review Research and Feedback → Minimal Theory of Change → Decide On Aims and Objectives
   (Core Features · Interoperability Intent · Adaptability and Extensibility · Inclusivity · Real-World Testnet)
→ Development Principles → 1 Choose Method → 2 Plan ⇄ Think about sustainability → Sustainability Gate
→ 3 Approve → The Development Method → SCOPE AND START GATE ──moves to next phase──▶

PHASE 2  DEVELOPMENT
Develop the Standard ◀─supports─ Team (← Roles and Responsibilities) · Development Platform · Share Progress · Testing
   Documentation ◀ Structured Documentation · Examples · Decision and Provenance Record · Translation and Accessibility
Develop the Standard ─is the main work of─▶ Development Phase (the loop) → DEVELOPMENT OUTCOMES GATE ──▶

PHASE 3  LAUNCH AND ADOPTION
Launch and Adoption ─requires─▶ Plan and Launch · Support Adoption · Monitor Adoption
→ LAUNCH AND ADOPTION OUTCOMES GATE ──▶

PHASE 4  REVIEW AND UPDATE
Review · Deciding To Review · Review Process · Key Review Questions → Reviewing the Standard
→ REVIEW OUTCOMES (gate) → Deciding Next Steps → UPDATE OR RETIRE GATE ─produces─▶ Lifecycle Decision Record
   exits: maintain → Monitor Adoption · minor update → Develop the Standard
          major update → Scope and Start gate · rescope → Frame the Opportunity
```

**Returns-to routes.** Each phase has routes back to earlier nodes when a condition fails. They are listed under every gate in `map/INDEX.md`, and from non-gate nodes (Testing, Development Phase, Launch and Adoption) under *Other returns-to routes*. On the canvas they sit in the *Returns-to routes* group.

Two kinds of backward edge need keeping apart:

- **Returns-to:** a gate or node is *not passed*, so the effort goes back.
- **Update or Retire's exits:** the gate *is* passed, and the decision re-enters the map, starting a new cycle with the Lifecycle Decision Record as its baseline.

**Baselines.** Each gate's bundle is the baseline for what follows: the Scope bundle for Development, the Development Outcomes bundle for Launch, and all three for Review.

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
| Inclusion across development, use, governance and consequence; inclusion is not uniformity; exclusion through success | Inclusivity |
| Design → express → implement → test → share → learn; the development loop; development can reopen scope | Development Phase |
| Develop claims, not just text; traceability chain; normative vs informative vs example vs experimental | Develop the Standard |
| Roles are functions, not offices; editor as custodian; implementer as instrument of inquiry | Team; Roles and Responsibilities |
| One development commons, many interfaces; preserve provenance | Development Platform |
| Share for response; milestones are invitations; report disagreement | Share Progress |
| Testing subtypes; every important failure becomes information; confidence, not proof | Testing |
| Documentation as interface; one source of normative truth; four documentation modes; tested examples | Documentation; Structured Documentation; Examples |
| Confidence gate; evidence gate; stable core, explicit edge; failures must resolve somewhere; known unknowns become launch conditions; scope drift record; launch baseline | Development Outcomes (Phase Gate) |
| Launch the capability, not the artifact; make the stable boundary visible; launch is an adoption invitation | Plan and Launch |
| Adoption journey; support requests as evidence; community capacity, not dependence | Support Adoption |
| Behavior not reach; watch the forks; adoption vs impact success; map the standard back into the ecosystem; longitudinal snapshots | Monitor Adoption |
| Review triggers; review readiness; review is triggered by learning, not completion | Launch and Adoption Outcomes (Phase Gate); Deciding To Review |
| Compare expectation with reality; separate reviewing from deciding; fitness classes; review produces options | Review; Review Process; Review Outcomes (Gate) |
| Change severity; existing adopters change the burden of proof; version coexistence; active retirement; preserve the commons | Deciding Next Steps |
| Lifecycle routes; retirement is a successful outcome; review closes the learning loop | Update or Retire (Phase Gate); Lifecycle Decision Record |

## Canvases

- `framework/Open Standards Main Map/Updated Open Governance Standards Map.canvas` is the map. It has one group per phase (*Start and Scope*, *Development*, *Launch and Adoption*, *Review*), plus the *Returns-to routes* group.
- `framework/Open Standards Simple Canvas/Simple Canvas For Open Standards.canvas` is the fill-in canvas (START / WHY / WHO / HOW, 12 steps), with examples.
- `framework/Theory of Change/Theory of change - Four principles of Change.canvas` is a text-only systems-change explorer: tension; What? / So what? / Now what?; coherence and simple rules. Read it with `python tools/canvas_text.py "<path>"`.

Canvas links are relative to the repository root, which is the Obsidian vault.

## Not yet defined in the framework

Say so plainly when a question lands here. Do not fill the gap:

- **Deprecate and retire are not routed.** Their content lives inside *Deciding Next Steps*, which is due to be split into finer nodes.
- **Unmet Update or Retire criteria have no failure routes yet.**
- ***Lifecycle Decision Record* is a stub.** Its open questions — cycle numbering, which baselines carry forward, cross-cycle comparison — are development targets.
