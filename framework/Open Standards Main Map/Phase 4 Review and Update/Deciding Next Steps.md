---
phase: review
domain:
- lifecycle
- governance
- change-management
- retirement
role: checkpoint
status: draft
actors:
- stewards
- decision-makers
- adopters
- affected-participants
produces:
- lifecycle-decision
- update-scope
- maintenance-decision
- retirement-plan
- communication-plan
- transition-plan
---

---

# Deciding Next Steps

## Intent

Translate the findings of Review into a clear lifecycle decision for the standard.

This cluster asks:

> **Given the evidence, what is the responsible thing to do now?**

The available options should be broader than simply:

- update;
    
- retire.
    

A mature standard may need no substantive change.

It may require only maintenance.

It may need to return to Scope.

It may need to align with another standard.

---

# Decision Options

## Maintain

No material change to the standard is currently justified.

Continue:

- monitoring;
    
- support;
    
- routine maintenance;
    
- scheduled review.
    

---

## Minor Update

Make changes that do not materially alter the agreement or impose major migration burdens.

Examples:

- clarify wording;
    
- correct errors;
    
- improve documentation;
    
- add compatible optional fields;
    
- improve examples or tooling.
    

---

## Major Update

Make substantive or breaking changes.

This should be treated as a renewed development effort.

Potential consequences include:

- migration;
    
- incompatible implementations;
    
- multiple supported versions;
    
- updated tooling;
    
- updated documentation;
    
- renewed adoption support.
    

---

## Refine / Rescope

Return to Scope and Start when:

- adoption is low because the standard addresses the wrong problem;
    
- actual use differs fundamentally from intended use;
    
- the Theory of Change is no longer plausible;
    
- the standardization surface needs to change.
    

---

## Align / Merge / Supersede

Move toward another standard where:

- interoperability would improve;
    
- duplication is no longer justified;
    
- another standard now serves the use case better.
    

---

## Deprecate

Signal that the standard remains available but should not be used for new implementations.

Useful when transition requires time.

---

## Retire

End active maintenance.

Retirement should be deliberate and communicated.

---

# Pattern: Decide With Consequence, Not Preference

For each option assess:

- adopter impact;
    
- migration burden;
    
- interoperability;
    
- governance burden;
    
- sustainability;
    
- risk;
    
- ecosystem effect;
    
- reversibility.
    

---

# Pattern: Existing Adopters Change the Burden of Proof

During initial Development, a breaking design change may be relatively cheap.

After adoption, the same change may impose substantial costs on:

- implementers;
    
- tool builders;
    
- institutions;
    
- downstream users;
    
- policy processes;
    
- dependent standards.
    

Therefore major updates require stronger justification than equivalent changes during Development.

---

# Pattern: Classify Change Severity

A simple model:

```yaml
change:
  class:
    - patch
    - minor
    - major
    - deprecation
    - retirement
  breaking:
  affected_adopters:
  migration_required:
  governance_approval:
```

---

# Pattern: Update Means Re-enter Development

A substantive update should not create a parallel mini-lifecycle.

It should feed back into the established Development topology.

For example:

```text
Review
  ↓
Major Update
  ↓
Development
  ↓
Testing
  ↓
Documentation
  ↓
Development Outcomes
  ↓
Launch / Migration
```

The standard is mature, but the development disciplines remain the same.

---

# Pattern: Major Updates May Reopen Scope

If the proposed update changes:

- the standardization surface;
    
- target actors;
    
- primary use cases;
    
- fundamental objective;
    
- Theory of Change;
    

then return to:

**Scope and Start**

before Development.

---

# Update Planning

For an update, produce:

```yaml
update:
  rationale:
  change_class:
  scope:
  affected_components:
  breaking_changes:
  affected_adopters:
  migration_strategy:
  compatibility_strategy:
  test_requirements:
  documentation_changes:
  support_requirements:
  release_plan:
```

---

# Pattern: Preserve Version Coexistence Explicitly

When multiple versions remain supported, define:

- which versions are active;
    
- support horizon;
    
- compatibility;
    
- migration path;
    
- documentation for each;
    
- tests for each;
    
- end-of-support conditions.
    

Do not leave version support implicit.

---

# Active Retirement

Retirement should mean:

> **The standard is no longer actively maintained, but its existence, history, status, and migration context remain legible.**

Avoid passive abandonment.

---

# Retirement Triggers

Possible reasons include:

- no meaningful use;
    
- supersession;
    
- regulatory change;
    
- ecosystem change;
    
- unsustainable maintenance;
    
- insufficient stewardship;
    
- fundamental misalignment;
    
- unacceptable harm.
    

---

# Retirement Plan

A responsible retirement should address:

## Communication

Tell:

- adopters;
    
- implementers;
    
- dependent projects;
    
- relevant institutions;
    
- standards communities.
    

---

## Status

Clearly mark the standard as:

- deprecated;
    
- retired;
    
- superseded.
    

---

## Replacement

Where applicable, identify:

- successor standard;
    
- migration path;
    
- compatibility guidance.
    

---

## Archive

Preserve:

- specification;
    
- documentation;
    
- release history;
    
- issues;
    
- decisions;
    
- governance records;
    
- rationale.
    

---

## Infrastructure

Decide what happens to:

- domains;
    
- repositories;
    
- forums;
    
- registries;
    
- validators;
    
- APIs.
    

---

## Stewardship Transfer

Where appropriate, allow another group to continue maintenance.

This may include transferring:

- repository control;
    
- domain ownership;
    
- rights;
    
- archives;
    
- governance responsibility.
    

---

# Pattern: Preserve the Commons Even When Stewardship Ends

Retirement should not make an open standard disappear.

If the standard was genuinely open, its historical artifacts should remain:

- inspectable;
    
- usable;
    
- forkable where licensing allows;
    
- understandable.
