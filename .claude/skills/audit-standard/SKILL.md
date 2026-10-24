---
name: audit-standard
description: Audit a standards effort or an existing standard against any gate of the Designing Open Standards framework — Scope and Start, Development Outcomes, Launch and Adoption Outcomes, Review Outcomes, or Update or Retire. It produces evidence-tagged findings per gate criterion, red flags, a recommended outcome with returns-to routes, and a structured audit record. Use for "audit this standard", "is this ready for development / launch / review?", "review our scoping", "check this CIP / template / proposal standard against the framework", or a retroactive audit of a standard already in development or use.
---

# Audit a standard against a gate

An audit reports what the evidence shows. It does not approve, authorize or certify, and it does not grade intentions. Absence of evidence is recorded as `not-evidenced`, never silently as `not-met` or `met`.

## Inputs

- The effort's materials: files the person gives you, a `workspace/<slug>/` folder, links, a repository, forum threads. You can only audit what you can actually read.
- The criteria file for the gate. The criteria are verbatim from the gate notes, with stable ids, the nodes to consult, return routes, bundle components, red flags, and baseline questions.

  | Gate | Criteria file | Baseline it compares against |
  |---|---|---|
  | Scope and Start | `toolkit/scope-gate-criteria.yaml` (40) | — (it *creates* the first baseline) |
  | Development Outcomes | `toolkit/develop-gate-criteria.yaml` (32) | Scope and Start Bundle |
  | Launch and Adoption Outcomes | `toolkit/launch-gate-criteria.yaml` (13, sufficiency judgment) | Development Outcomes Bundle |
  | Review Outcomes; Update or Retire | `toolkit/review-gate-criteria.yaml` (10 + 9, under `gates:`) | all three earlier bundles |

- The framework notes those criteria point to, in `framework/Open Standards Main Map/<phase folder>/`.
- `toolkit/templates/audit-record.yaml` — the output structure.

## 1. Frame the audit

Settle these with the person before assessing anything:

- **Effort, slug and cycle.** Output goes to `workspace/<slug>/audits/`. Take the cycle from `effort.yaml` if there is one.
- **Which gate.** If unclear, place the effort by where its work actually is (see **guide-standard**, step 4) and confirm.
- **Mode.**
  - `pre-gate` — the effort is approaching this gate and wants to know whether it is ready.
  - `retroactive-baseline` — the effort is past this gate, or skipped it. First establish whether the earlier baselines exist at all. Then assess against what was true when the gate was (or should have been) crossed, and answer the earlier phase's `baseline_questions`. "Changes are not failures. Unrecorded changes are."
  - `partial` — one domain or node only.
- **Sources.** List every source as `S1…Sn` with location and retrieval date. Agree what is out of scope.
- **Independence.** If you (or this person) helped write the materials, record it as a self-assessment.

## 2. Assess each criterion

For each criterion in the file (for the review file, for each gate under `gates:` in scope):

1. Read the relevant part of each `consult` note — at least its gate condition, readiness questions, or the patterns that define the criterion.
2. Search the sources for evidence. Locate it precisely (`S2 §3`, heading, line).
3. Assign a `status`: `met`, `partial`, `not-met`, `not-evidenced`, or `not-applicable` with a reason. Some domains carry an `applies_when`; respect it.
4. Tag each piece of evidence `observed`, `reported`, `inferred`, `assumed`, `contested` or `unknown`. A claim in the effort's own document that X is true is `reported` unless it shows its evidence.
5. For anything short of `met`:
   - Set the disposition from the file: `resolve` (Scope: before- or through-development), or the file's `open_question_dispositions` (Development: blocking, launch-condition, monitor, review-trigger, deferred).
   - Set the criterion's `returns_to`.
   - Where `returns_to` is `null` (Update or Retire), say that the framework has not defined a route yet.
6. Write a one- or two-sentence `finding`. Specific beats comprehensive.

Be proportionate. Every gate in this framework asks whether things are sufficiently true for the next phase to be the right source of learning, not whether they are perfect.

## 3. Check the bundle, the patterns and the baseline

- **Bundle components:** record each of the file's `bundle_components` as present, partial or missing, with its source.
- **Red flags:** check each pattern in `red_flags`, and record only the ones you can evidence.
- **Baseline:** for gates after Scope, compare against the baseline bundle in the table above. Record material drift, and whether it was reviewed.

## 4. Summarise

- **Per domain:** a status and one line of rationale. Do not average; name the criterion that drives the domain.
- **Recommended outcome:** one of the file's `gate_outcomes`, with conditions if it is conditional.
  - Remember the successful non-progressions: reuse or extend, another intervention, pause and stop (Scope); continue adoption monitoring (Launch); maintain, deprecate and retire (Update or Retire).
  - You recommend; the people with standing decide.
- **Returns-to routes:** the distinct nodes the failing criteria route to, with the condition text from `map/graph.json` → `returns_to` where a wired route matches.
- **Open questions:** each with its disposition.
- **Limitations:** sources not seen, people not heard, claims you could not verify.

## 5. Write the outputs

- `workspace/<slug>/audits/<YYYY-MM-DD>-<phase>-audit.yaml`, filled from `toolkit/templates/audit-record.yaml`.
  - Every finding cites a criterion id and source ids.
  - Set `gate_node`, `criteria_file`, `criteria_version` and `cycle`.
  - Set `framework_version` from `git rev-parse --short HEAD` (or the release tag) when available.
- `workspace/<slug>/audits/<YYYY-MM-DD>-<phase>-audit.md`, for people: a summary table by domain, the recommended outcome, the top findings, red flags, returns-to routes, open questions, limitations, and the record's closing statement.
- If `workspace/<slug>/effort.yaml` exists, append an `audit` log entry.

Then give the person the headline in a few lines: the recommended outcome, the two or three findings that drive it, and where to return to.

## Never

- Invent or embellish evidence, or upgrade `reported` to `observed`.
- Treat a list of stakeholders or adopters as engagement, adoption depth or consent. Treat an endorsement as agreement, or silence as either.
- Describe the effort as certified, valid, compliant or approved. This repository does not issue certificates; the audit record is structured so that future tooling could, but it is not one.
- Invent return routes the framework does not define. Say it is silent.
