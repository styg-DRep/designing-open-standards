---
phase: scope
domain:
  - requirements
  - design-intent
role: supporting
status: draft
produces:
  - core-feature-hypotheses
  - optional-feature-hypotheses
  - feature-rationale
---

## Intent

Identify the smallest capabilities the standard must possess for its objectives to remain plausible.

Ask:

> **What must be true of this standard for it to have any reasonable chance of accomplishing its objectives?**

Core features may include:

- shared definitions;
    
- validation;
    
- identifiers;
    
- provenance;
    
- machine readability;
    
- human readability;
    
- versioning;
    
- extensibility;
    
- discovery;
    
- governance;
    
- portability.
    

Do not design the implementation yet.

Describe the needed capability.

---

# Pattern: Derive Features From Objectives

For every proposed feature ask:

> Which objective does this enable?

If no objective depends upon it, the feature may not be core.

Likewise, for every objective ask:

> What capabilities must the standard possess for this objective to be achievable?

This creates traceability:

```text
Aim
 ↓
Objective
 ↓
Required capability
 ↓
Feature
```
