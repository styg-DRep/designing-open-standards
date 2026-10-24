---
phase: scope
domain:
- development
- mandate
role: supporting
status: draft
---

## Cardano-native framing

“Approval” should not automatically mean:

> A single owner authorizes development.

For a decentralized governance standard, the relevant question is:

> **Does this effort possess sufficient mandate, consent, resources, and accountability to move from exploration into committed development?**

Approval may therefore take different forms.

---

# Possible Approval Forms

## Steward approval

A recognized steward or stewardship group agrees that development should proceed.

## Funder approval

Resources are released subject to an agreed scope.

## Working-group consent

The development group explicitly consents to the plan.

## Institutional mandate

A governance body authorizes development.

## Community legitimacy

No formal authority exists, but sufficient relevant actors commit to participation and adoption experiments.

## Combined approval

Several of the above may coexist.

Record which form applies.

---

# Approval Should Cover

At minimum:

- scope;
    
- aim and objectives;
    
- theory-of-change assumptions worth carrying;
    
- development method;
    
- participation model;
    
- key contributors;
    
- early adopters;
    
- core features;
    
- testing approach;
    
- interoperability commitments;
    
- major risks;
    
- resource envelope;
    
- sustainability assumptions;
    
- decision rights;
    
- development infrastructure.
    

---

# Pattern: Approval Is a Record, Not a Ceremony

Capture:

```yaml
approval_basis:
approving_parties:
decision_method:
scope_approved:
resources_committed:
conditions:
objections:
unresolved_questions:
date:
review_trigger:
```

Approval should be inspectable later.

---

# Pattern: Preserve Conditions and Objections

A qualified approval is often more informative than a simple yes.

For example:

> Proceed provided two independent implementations test the schema before candidate release.

or:

> Proceed, with unresolved concern around representation of small governance communities.

Do not erase these conditions once development begins.

They are future review inputs.
