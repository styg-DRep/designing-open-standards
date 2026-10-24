---
phase: review
domain:
  - lifecycle
  - provenance
role: artifact
status: stub
produces:
  - lifecycle-decision-record
---

## Intent

Carry the decision made at *Update or Retire* into the next cycle as an explicit baseline, so the part of the framework the standard re-enters can see what was decided, on what evidence, and what it inherits.

> Stub. A development target for the next stage of the framework.

## Where it sits

Produced by **Update or Retire (Phase Gate)**. It is the baseline for the node each lifecycle route re-enters:

| Decision | Re-enters at |
|---|---|
| maintain | Monitor Adoption |
| minor update | Develop the Standard |
| major update | Scope and Start (Phase Gate) |
| rescope | Frame the Opportunity |

Deprecate and retire are not yet routed; their content currently lives in *Deciding Next Steps*.

## What it records

From the *Lifecycle Decision Record* in Update or Retire:

```yaml
decision:
  outcome:
    - maintain
    - minor-update
    - major-update
    - rescope
    - align
    - deprecate
    - retire
basis:
review_findings:
decision_participants:
decision_method:
affected_adopters:
migration_required:
transition_conditions:
next_phase:
responsible_stewards:
communication_plan:
objections:
review_trigger:
```

## Why it exists

Each phase ends by fixing a baseline for what follows: the Scope and Start Bundle is the first audit boundary, and the Development Outcomes Bundle is the baseline against which Launch and Review are evaluated. Review then closes the learning loop. Without a record that travels into the next cycle, the loop closes only in prose, and the next cycle has nothing to compare itself against.

## Open questions

- How is a cycle identified, and how are cycles numbered?
- Which earlier bundles does each re-entry point inherit as baselines — every prior one, or the most recent per phase?
- How does a re-entered node compare the new cycle with the old one (scope drift across cycles)?
- What happens to the open questions, conditions and objections carried by the previous cycle's records?
- Where does Update or Retire route when its own gate criteria are not met?
