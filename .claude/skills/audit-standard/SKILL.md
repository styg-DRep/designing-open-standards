---
name: audit-standard
description: Audit a standards effort against the Scope and Start gate of the Designing Open Standards framework, producing evidence-tagged findings per gate criterion, red flags, a recommended gate outcome with returns-to routes, and a structured audit record. Use for "audit this standard", "is this ready for development?", "review our scoping", "check this CIP / template / proposal standard against the framework", or a retroactive audit of a standard already in development or use.
---

# Audit a standard against Scope and Start

An audit reports what the evidence shows. It does not approve, authorize or certify, and it does not grade intentions. Absence of evidence is recorded as `not-evidenced`, never silently as `not-met` or `met`.

## Inputs

- The effort's materials: files the person gives you, a `workspace/<slug>/` folder, links, a repository, forum threads. You may only audit what you can actually read.
- `toolkit/scope-gate-criteria.yaml` — the 40 criteria (verbatim from the gate note) with stable ids, the nodes to consult for each, return routes, bundle components, red flags, and baseline questions.
- The framework notes those criteria point to, in `framework/Open Standards Main Map/`.
- `toolkit/templates/audit-record.yaml` — the output structure.

## 1. Frame the audit

Settle these with the person before assessing anything:

- **Effort and slug.** Output goes to `workspace/<slug>/audits/`.
- **Mode.**
  - `pre-gate` — the effort is scoping and wants to know if it is ready for development.
  - `retroactive-baseline` — the standard is already in development or use. First establish whether a Scope baseline exists at all; then assess the criteria against what was true when development began (if knowable) and answer the eight `baseline_questions` ("Changes are not failures. Unrecorded changes are.").
  - `partial` — one domain or node only.
- **Sources.** List every source as `S1…Sn` with location and retrieval date. Agree what is out of scope of the audit.
- **Independence.** If you (or this person) helped write the materials, record it as a self-assessment.

## 2. Assess each criterion

For each criterion in `toolkit/scope-gate-criteria.yaml`:

1. Read the `consult` notes' relevant section (at minimum their gate condition or the patterns that define the criterion).
2. Search the sources for evidence. Quote or locate it precisely (`S2 §3`, heading, line).
3. Assign a `status`: `met`, `partial`, `not-met`, `not-evidenced`, or `not-applicable` (with a reason).
4. Tag each piece of evidence `observed`, `reported`, `inferred`, `assumed`, `contested` or `unknown`. A claim in the effort's own document that X is true is `reported` unless it shows its evidence.
5. For anything short of `met`, set `resolve`: `before-development` or `through-development`, and the criterion's `returns_to` node.
6. Write a one- or two-sentence `finding`. Specific beats comprehensive.

Be proportionate: "readiness is sufficient, not complete". A lightweight effort can meet a criterion lightly.

## 3. Check the bundle and the patterns

- **Bundle components** — for each of the 20 in `bundle_components`, record present / partial / no, with source.
- **Red flags** — check each pattern in `red_flags`; record only the ones you can evidence, with the source.

## 4. Summarise

- Per domain (Opportunity, Ecosystem, Justification, Participation, Purpose, Design Intent, Development, Openness, Sustainability, Mandate): a status and one line of rationale. Do not average; say which criterion drives the domain.
- **Recommended outcome** — one of the ten `gate_outcomes`, with conditions if conditional. Remember that `reuse-or-extend`, `use-another-intervention`, `pause` and `stop` are legitimate, successful scoping outcomes. Recommend; the people with standing decide.
- **Returns-to routes** — the distinct nodes the failing criteria route to, each with the gate's condition text from `map/graph.json` → `returns_to`.
- **Open questions** — each with `resolve` and a disposition (development task, test hypothesis, monitoring condition, review trigger, accepted uncertainty).
- **Limitations** — sources not seen, people not heard, claims you could not verify.

## 5. Write the outputs

- `workspace/<slug>/audits/<YYYY-MM-DD>-scope-audit.yaml` — filled from `toolkit/templates/audit-record.yaml`. Every finding cites a criterion id and source ids. Set `criteria_version` from the criteria file and `framework_version` from `git rev-parse --short HEAD` (or the release tag) when available.
- `workspace/<slug>/audits/<YYYY-MM-DD>-scope-audit.md` — for people: a summary table by domain, the recommended outcome, the top findings, red flags, returns-to routes, open questions, limitations, and the record's closing statement.
- If `workspace/<slug>/effort.yaml` exists, append an `audit` log entry.

Then give the person the headline in a few lines: recommended outcome, the two or three findings that drive it, and where to return to.

## Never

- Invent or embellish evidence, or upgrade `reported` to `observed`.
- Treat a list of stakeholders as engagement, or an endorsement as consent, or silence as agreement.
- Describe the effort as certified, valid, compliant or approved. This repository does not issue certificates; the audit record is structured so that future tooling could, but it is not one.
- Audit Development, Launch and Adoption, or Review criteria. Those phases are not yet mapped; at most, note obligations the Scope bundle created and whether they appear to be honoured.
