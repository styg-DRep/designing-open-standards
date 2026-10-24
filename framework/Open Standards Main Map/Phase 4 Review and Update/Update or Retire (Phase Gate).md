---
phase: review
domain:
- lifecycle
- transition
role: checkpoint
status: draft
actors:
- stewards
- decision-makers
- adopters
- affected-participants
produces:
- lifecycle-decision
- next-phase-route
- update-mandate
- retirement-record
- transition-conditions
- lifecycle-decision-record
gate: phase
---

## Intent

Commit the standard to its next lifecycle state.

This is the final decision gate in the planned lifecycle.

It asks:

> **Given the Review findings and community consequences, what lifecycle path should the standard now enter?**

---

# Gate Routes

## Maintain

```text
Update or Retire
      ↓
Maintain
      ↓
Launch / Adoption Monitoring
```

No major lifecycle reset is required.

---

## Minor Update

```text
Update or Retire
      ↓
Development
```

Potentially using an abbreviated Scope check where the underlying development case remains unchanged.

---

## Major Update

```text
Update or Retire
      ↓
Scope and Start
      ↓
Development
```

Use when the changes materially alter the original development case.

---

## Refine / Rescope

```text
Update or Retire
      ↓
Frame the Opportunity
      ↓
Scope and Start
```

---

## Deprecate

```text
Update or Retire
      ↓
Transition Support
      ↓
Retirement
```

---

## Retire

```text
Update or Retire
      ↓
Active Retirement
      ↓
Archive / Preserve
```

---

# Gate Criteria

A lifecycle decision is ready when:

1. Review findings are sufficiently clear;
    
2. consequences for current adopters are understood;
    
3. the decision aligns with the standard's governance process;
    
4. material objections are documented;
    
5. sustainability implications are understood;
    
6. migration consequences are assessed;
    
7. communication requirements are known;
    
8. the destination lifecycle path is explicit;
    
9. responsible actors have accepted the next-step obligations.
    

---

# Lifecycle Decision Record

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

---

# Pattern: A Lifecycle, Not a Line

The complete standards process should now be understood as a loop:

```text
SCOPE & START
      ↓
DEVELOPMENT
      ↓
LAUNCH & ADOPTION
      ↓
REVIEW
      ↓
DECIDE NEXT STEPS
   ↙   ↓    ↓    ↘
scope develop monitor retire
```

The standard can move backward, forward, stabilize, or end.

That flexibility is a feature.

---

# Pattern: Retirement Is a Successful Outcome

A standard that once created value may later cease to be the best coordination mechanism.

Retirement may indicate:

- another standard succeeded;
    
- ecosystem conditions improved;
    
- technology changed;
    
- the problem disappeared;
    
- the standard fulfilled its purpose.
    

Therefore retirement should not automatically be interpreted as failure.

The relevant question is whether the transition is responsible.

---

# Pattern: Review Closes the Learning Loop

The lifecycle begins with hypotheses:

> We believe this coordination problem exists.

> We believe this standard can help.

It ends each cycle with evidence:

> Here is what actually happened.

That evidence can then revise:

- the opportunity;
    
- ecosystem understanding;
    
- aims;
    
- Theory of Change;
    
- development method;
    
- sustainability assumptions.
    

Review therefore completes the epistemic loop of the entire framework.
