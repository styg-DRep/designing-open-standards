# Route: Phase 4 — Review and Update

Notes are in `framework/Open Standards Main Map/Phase 4 Review and Update/`. Baselines: this cycle's Scope and Start, Development Outcomes, and Launch and Adoption Outcomes bundles.

Review compares expectation with reality. Its purpose is to understand what the standard has become, not to defend it. Review produces options; the decision comes after.

| # | Node(s) to read | Write to | Exit check |
|---|---|---|---|
| 1 | Deciding To Review | `review.yaml` → `review` (trigger, scope) | The trigger, who invoked it, urgency, and an explicit review scope — including what is out of scope |
| 2 | Review; Review Process; Key Review Questions | `review.yaml` → roles, `baselines` | Reviewing separated from deciding where possible; all three baselines revisited; questions prioritized, not an open backlog |
| 3 | Reviewing the Standard | `review.yaml` → `findings`, `theory_of_change`, `evidence`, `confidence`, `dissent` | Findings with evidence basis and confidence; "was the causal theory broadly correct?" answered |
| 4 | Review Outcomes (Gate) | `review.yaml` → `options`, `fitness`, `review_outcome` | Its ten criteria (`toolkit/review-gate-criteria.yaml`); outcomes include return to Review Process, to monitoring, or to Scope |
| 5 | Deciding Next Steps | `lifecycle-decision-record.yaml` → `change`, `update`, `versions`, `retirement` | Each option assessed by consequence; existing adopters raise the burden of proof for breaking change |
| 6 | Update or Retire (Phase Gate) | `lifecycle-decision-record.yaml` (decision record, `carried_forward`) | Its nine criteria; the destination path is explicit; responsible actors have accepted the obligations |

## Crossing Update or Retire: starting a new cycle

Update or Retire's routes are exits, not failures:

- **maintain** → Monitor Adoption
- **minor update** → Develop the Standard
- **major update** → Scope and Start (Phase Gate) — when the change materially alters the development case
- **rescope** → Frame the Opportunity

When people make the decision:

1. Record the decision in `lifecycle-decision-record.yaml` (decided and recorded by them).
2. In `effort.yaml`: add the Review baseline, increment `cycle`, set `phase` and `current_node` to the re-entry node, and copy `carried_forward` open questions, conditions and objections into `open_questions`.
3. At the re-entry node, the Lifecycle Decision Record is the baseline: compare the new cycle against the previous one rather than starting from blank.

**Not yet defined in the framework — say so if you reach them:**

- **Deprecate and retire** are not routed. Use the *Retirement Plan* and *Active Retirement* content in Deciding Next Steps, and do not invent nodes.
- **Unmet Update or Retire criteria** have no failure routes yet. Name the unmet criterion, and let the people choose where to continue (usually Deciding Next Steps or Review Outcomes). Record it as an open question.
