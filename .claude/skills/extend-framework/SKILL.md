---
name: extend-framework
description: Maintain and extend the Designing Open Standards framework itself — add or revise nodes, add the Development, Launch and Adoption, or Review phases, wire canvas edges and returns-to routes, keep the toolkit crosswalk in step, and regenerate the map index. Use when editing anything under framework/ or toolkit/, adding a phase, renaming or moving notes, preparing a release, or when the map check fails.
---

# Extend the framework

`framework/` is an Obsidian vault and the source of truth. Everything in `map/` is generated from it. `toolkit/` is derived from it by hand.

## Conventions

**One note per node.** The filename is the node title; its slug (lowercase, non-alphanumerics → `-`) is the node id used in `map/`, the toolkit, workspaces and audit records. Renaming a note changes its id — record renames in `CHANGELOG.md` with old → new id.

**Frontmatter** — real YAML at the top of every note (not a fenced code block):

```yaml
---
phase: scope            # scope | develop | launch | review — or a list when a node spans phases
domain: [framing, ecosystem]
role: checkpoint        # entry-point | orientation | checkpoint | supporting | artifact
status: draft           # stub | draft | stable
actors: [prospective-stewards, affected-participants]
produces: [opportunity-frame, evidence-gaps]   # kebab-case artifact names
gate: phase             # only on a phase gate note
---
```

- `checkpoint` — has a gate condition and possible outcomes. `supporting` — a lens or sub-inquiry feeding a checkpoint. `artifact` — an output other nodes consume (e.g. Actor Map, Ecosystem Map). `entry-point` — where a phase starts. `orientation` — context.
- `produces` names feed the artifact index; reuse existing names where the artifact is the same thing.

**Node anatomy** — the strongest existing notes (Frame the Opportunity, Decide On Aims and Objectives, Think about sustainability, the gate) share a shape worth keeping: *Intent* (first paragraph is extracted into the index — make it a sentence that stands alone) → *Inputs* → *Core principle* → *Pattern: …* sections → an artifact YAML block → *Gate condition* as numbered questions → *Possible gate outcomes* (including returns) → a small topology sketch.

**Canvas** — the main map is `framework/Open Standards Main Map/Updated Open Governance Standards Map.canvas`.
- One **group** per phase, labelled with the phase name (Scope's is *Start and Scope*).
- Label edges. The index records labels verbatim and slugs them into relations. In use: *Starts and Supports, Feeds, Informs, Informs and updates, Updates, Produces, Checks, Supports, Describes, References, References/Consults, Enables us to, Follows through, Checkpoint for, Delivers, returns to*. Thirty current edges are unlabelled (they index as `connects`) — mostly parent→lens decompositions and the Types of Standards families; labelling them (e.g. *Decomposes into*, *Is a family of*) would sharpen agent navigation.
- **Returns-to routes**: gate note → a hub text card (`returns-to instances`) → one text card per condition → edge labelled `returns to` → the node to return to. `tools/build_index.py` walks text-only hops back from each `returns to` edge to find the gate, so keep the condition cards as text, not notes.
- **Next phase placeholder**: a text card the gate points at, with no outgoing edges (currently *Development*). The index lists it as a placeholder.

Edit canvases in Obsidian where possible; moving or renaming files there updates canvas references. If you edit canvas JSON directly, keep node ids unique 16-hex strings, keep `file` paths relative to `framework/`, and validate JSON.

## Adding a phase (Development, Launch and Adoption, Review)

1. Create the phase's notes in `framework/Open Standards Main Map/` (or a sibling folder — any folder under `framework/` is indexed) with `phase: develop` etc.
2. Add a group for the phase on the main canvas, place the notes, and draw labelled edges.
3. Create the phase gate note with `role: checkpoint` and `gate: phase`, its criteria, outcomes, and returns-to cards on the canvas.
4. Replace the previous phase's placeholder: edge from the previous gate to the new phase's entry node, delete the placeholder card, add a new placeholder after your gate if the next phase is still unmapped.
5. Pick up the forward hooks already in the Scope notes:
   - Think about sustainability / Sustainability Gate — sustainability across Develop, Launch, Review (observe actual maintenance burden, adoption/support burden, compare expected vs actual, adapt / simplify / transfer / retire).
   - Minimal Theory of Change — *Review —returns-to→ Theory of Change* when outcomes diverge.
   - Scope and Start gate — *The Bundle Is the First Audit Boundary* (the baseline questions) and *Crossing the Gate Creates Obligations*.
   - Types of Standards, Shared Vocabularies, Information Exchange, Provide Guidance — already tagged `develop`/`review`.
   - 2- Plan the Development — phases or cycles, testing types, decision rights: the Development phase should inherit rather than restate them.
6. Add `toolkit/<phase>-gate-criteria.yaml` mirroring `scope-gate-criteria.yaml` (verbatim criteria, stable ids, consult, returns_to), plus templates the phase needs.
7. Extend the skills: the route table in `guide-standard`, the mode list in `audit-standard`, the phase boundary in `navigate-framework`, and `AGENTS.md`.
8. Update `tools/build_index.py` only if the phase introduces a structure it cannot read.

## Changing the Scope gate criteria

`toolkit/scope-gate-criteria.yaml` quotes the gate's criteria verbatim. If you change the criteria in the note, change them there. Never renumber or reuse an id — audit records cite them. Deprecate with `deprecated: true` and add a new id. Bump `version`.

## Before committing

```bash
python tools/build_index.py          # regenerate map/
python tools/build_index.py --check  # what CI runs: stale map, bad frontmatter, broken canvas links, unknown ids in the toolkit
```

Commit `map/` with the change that caused it. Add a `CHANGELOG.md` entry. Tag releases (`v0.6.0`, …) so workspaces and audit records can cite the framework version they used.
