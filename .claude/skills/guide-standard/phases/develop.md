# Route: Phase 2 — Development

Notes are in `framework/Open Standards Main Map/Phase 2 Development/`. Baseline: this cycle's Scope and Start Bundle.

Development is a learning cycle (design → express → implement → test → share → learn), not a writing phase. The route below is the set of clusters the loop passes through; most efforts go round several times before the gate. Read **Development Phase** first — it holds the loop, the traceability checks against Scope, and the twelve readiness questions.

| # | Node(s) to read | Write to | Exit check |
|---|---|---|---|
| 0 | Development Phase | `effort.yaml` (`phase: develop`, Scope baseline recorded) | They can name the bounded development problem for this cycle of the loop |
| 1 | Team; Roles and Responsibilities | `development-work.yaml` → `team` | Necessary responsibilities are visible, decision rights are explicit, missing capabilities named. Roles are functions, not offices |
| 2 | Development Platform | where each platform requirement lives, in `development-work.yaml` notes | Canonical artifacts, version history, issues, contributions, decisions, tests, documentation, releases, archival continuity — each has an answer |
| 3 | Develop the Standard | `development-work.yaml` → `decisions`, `component_maturity` | Important requirements have an intelligible reason (traceability chain); normative, informative, example and experimental material are marked |
| 4 | Testing | `development-work.yaml` → `test_records` | Relevant test subtypes chosen; every material failure resolves somewhere (the note's returns-to routes) |
| 5 | Documentation; Structured Documentation; Examples; Decision and Provenance Record; Translation and Accessibility | documentation set (pointers), `decisions` | The *Documentation Readiness Questions* in the gate note; one source of normative truth |
| 6 | Share Progress | `development-work.yaml` → `progress_updates` | Updates say what changed, why, what is unresolved and what feedback is needed by when; disagreement is reported |
| ↺ | Development Phase → *Development Loop* | `effort.yaml` log | Scope traceability questions checked each pass; material changes recorded rather than drifting |
| 7 | Development Outcomes (Phase Gate) | `development-outcomes-bundle.yaml`, draft `release_readiness_record` | Self-assessment with **audit-standard** (`toolkit/develop-gate-criteria.yaml`); the people decide |

Prompts worth reaching for: "can someone who did not author this use it from the available materials?", "is that a specification defect or an implementation defect?", "which objective does this requirement serve?", "what would the strongest implementer object to?", "are we still building the standard that was justified in Scope?".

Development can reopen Scope — that is the phase doing its epistemic job, not failing. Use the wired returns-to routes. At the gate, unresolved questions are classified `blocking`, `launch-condition`, `monitor`, `review-trigger` or `deferred`. Record the bundle as the cycle's Development baseline. Progression moves to **Launch and Adoption**.
