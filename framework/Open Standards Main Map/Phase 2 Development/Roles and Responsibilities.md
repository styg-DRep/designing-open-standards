---
phase: develop
domain:
- collaboration
- governance
role: supporting
status: draft
---

## Intent

Define the functions Development needs — process stewardship, editing, implementation, testing, domain expertise, review, liaison and evidence stewardship — and what each may and may not decide.

## Process Steward / Facilitator

Replaces the assumption that every group requires a singular authoritative “Chair.”

Responsibilities:

- keep development aligned with scope and objectives;
    
- facilitate decisions;
    
- surface unresolved disagreement;
    
- protect meaningful participation;
    
- ensure decision procedures are followed;
    
- prevent schedule pressure from silently replacing deliberation;
    
- preserve objections and minority positions where relevant.
    

Does **not** automatically own the standard or possess unilateral technical authority.

---

## Editors

Responsibilities:

- translate decisions into clear normative language;
    
- maintain consistency across the specification;
    
- distinguish normative and informative material;
    
- maintain terminology;
    
- publish drafts;
    
- incorporate accepted changes;
    
- connect changes with decisions and rationale.
    

### Pattern: Editor as Custodian

Editors should not quietly turn editorial discretion into policy-making.

Where a change affects meaning, requirements, or compatibility, return it to the appropriate decision process.

---

## Implementers

Responsibilities:

- attempt real implementations;
    
- expose ambiguity;
    
- identify hidden assumptions;
    
- evaluate implementation cost;
    
- test integration with existing infrastructure;
    
- provide concrete feedback about feasibility.
    

An implementation is not merely adoption.

During Development it is an **instrument of inquiry**.

---

## Testers

Responsibilities:

- turn requirements and claims into tests;
    
- maintain test fixtures;
    
- identify edge cases;
    
- test interoperability;
    
- document failure;
    
- distinguish specification defects from implementation defects.
    

Implementer and tester may overlap, but preserving the conceptual distinction is useful:

> Implementers ask, **“Can I build this?”**

> Testers ask, **“How do we know independent implementations behave consistently?”**

---

## Domain Experts

Responsibilities:

- challenge technical abstractions against governance reality;
    
- identify domain-specific constraints;
    
- validate terminology;
    
- identify missing cases and actors;
    
- prevent technical elegance from replacing domain fitness.
    

---

## Contributors and Reviewers

Responsibilities:

- propose improvements;
    
- review drafts;
    
- identify missing use cases;
    
- challenge assumptions;
    
- provide editorial or substantive comments;
    
- bring evidence from wider communities.
    

---

## Community / Ecosystem Liaison

Responsibilities:

- maintain contact with relevant stakeholder communities;
    
- surface emerging concerns;
    
- communicate review opportunities;
    
- identify participation gaps;
    
- bring ecosystem feedback back into development.
    

This role prevents “sharing progress” from becoming one-directional communications work.

---

## Evidence / Research Steward

Responsibilities:

- maintain continuity with Scope research;
    
- track claims requiring evidence;
    
- record implementation findings;
    
- distinguish anecdote from recurring patterns;
    
- identify questions requiring additional investigation.
    

---

# Team Artifact

```yaml
roles:
  - role:
    responsibilities:
    current_holders:
    authority:
    required_inputs:
    produces:
    unresolved_capacity:

decision_rights:
participation_paths:
missing_capabilities:
```
