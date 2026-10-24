---
name: extend-framework
description: Maintain and extend the Designing Open Standards framework itself — add, revise, split or rename nodes in any of the four phases, wire canvas edges, returns-to routes and lifecycle exits, keep the toolkit gate crosswalks and skills in step, and regenerate the map index. Use when editing anything under framework/ or toolkit/, decomposing a node, working a development target, preparing a release, or when the map check fails.
---

# Extend the framework

The repository root is the Obsidian vault; `framework/` is the source of truth. Everything in `map/` is generated from it. `toolkit/` is derived from it by hand.

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
- Label edges. The index records labels verbatim and slugs them into relations. In use: *Starts and Supports, Feeds, Informs, Informs and updates, Updates, Produces, Checks, Supports, Describes, References, References/Consults, Enables us to, Follows through, Checkpoint for, Delivers, returns to*. Several dozen current edges are unlabelled (they index as `connects`) — mostly parent→lens decompositions and the Types of Standards families; labelling them (e.g. *Decomposes into*, *Is a family of*) would sharpen agent navigation.
- **Returns-to routes** (a node or gate is *not passed*): source note → a hub text card (`returns-to instances`) → one text card per condition → edge labelled `returns to` → the node to return to. `tools/build_index.py` walks text-only hops back from each `returns to` edge to find the source, so keep condition cards as text, not notes. Cards wired for navigation but not yet laid out sit in the *Returns-to routes* group; moving them into their phase groups changes nothing for the index.
- **Phase transitions**: a labelled edge from a phase gate to the next phase's entry node (*moves to next phase*). The index lists every labelled out-edge of a gate under that gate.
- **Lifecycle exits** (Update or Retire *is* passed and the decision re-enters the map): labelled edges from the gate to the re-entry node (*maintain*, *minor update*, *major update*, *rescope*), plus the gate *produces* the *Lifecycle Decision Record*, which *is the baseline for* each re-entry node. Never model these as returns-to.

Edit canvases in Obsidian where possible; moving or renaming files there updates canvas references. If you edit canvas JSON directly, keep node ids unique 16-hex strings, keep `file` paths relative to the repository root (they start with `framework/`), and write the file with `tools/canvas_format.py` so diffs stay small. If links break after editing in another vault, run `python tools/fix_canvas_paths.py`, and validate JSON.

## Revising a phase

1. Notes live in one folder per phase under `framework/Open Standards Main Map/` (`Phase 1 Scope and Start/` … `Phase 4 Review and Update/`) with the matching `phase:` key. Any folder under `framework/` is indexed.
2. Place new notes in the phase's canvas group and draw labelled edges.
3. A new gate: `role: checkpoint`; add `gate: phase` only to the gate that ends the phase. Give it criteria, outcomes, and returns-to cards.
4. Keep the phase's crosswalk in step: `toolkit/<phase>-gate-criteria.yaml` (`scope`, `develop`, `launch`, `review`). Criteria are quoted verbatim from the gate note; ids, `consult` and `returns_to` are the interpretation layer and should follow the wired routes. A file may hold several gates under `gates:` (the review file does).
5. New artifact templates go in `toolkit/templates/`, built from the note's own YAML blocks, with a `# source:` line.
6. Update the skills where the phase is described: `guide-standard/phases/<phase>.md`, the gate table in `audit-standard`, the lifecycle sketch and concept locator in `navigate-framework`, and `AGENTS.md`.

## Decomposing a node

Large nodes can be split (e.g. *Deciding Next Steps* → separate update, deprecation and retirement nodes). Keep the original as the cluster's checkpoint or orientation note, move sections into new notes, wire them, then:

- move any returns-to or exit edges to the more specific node;
- update `consult` lists in the crosswalk;
- record the change in `CHANGELOG.md` — a decomposition adds ids, it should not remove one that audit records cite.

## Open development targets

- *Lifecycle Decision Record* (stub): cycle numbering, which baselines carry forward, cross-cycle comparison.
- Update or Retire: failure routes when its own criteria are not met (`returns_to: null` in `toolkit/review-gate-criteria.yaml`).
- Deprecate and retire routes, pending the decomposition of *Deciding Next Steps*.

## Changing gate criteria

Each `toolkit/*-gate-criteria.yaml` quotes its gate's criteria verbatim. If you change the criteria in a note, change them there. Never renumber or reuse an id — audit records cite them, and the index check rejects duplicates across files. Deprecate with `deprecated: true`, add a new id, and bump `version`.

## Before committing

```bash
python tools/build_index.py          # regenerate map/
python tools/build_index.py --check  # what CI runs: stale map, bad frontmatter, broken canvas links, unknown or duplicate ids in the toolkit
```

Commit `map/` with the change that caused it. Add a `CHANGELOG.md` entry. Tag releases (`v0.6.0`, …) so workspaces and audit records can cite the framework version they used.
