---
phase: develop
domain:
- infrastructure
- openness
- provenance
role: supporting
status: draft
actors:
- maintainers
- editors
- contributors
- testers
produces:
- public-development-space
- version-history
- issue-register
- decision-record
- contribution-history
---

## Intent

Provide the durable public infrastructure through which the standard can be developed, inspected, tested, discussed, and reproduced.

A Cardano-native version should treat this as part of the **governance infrastructure of the standard itself**.

---

# Platform Requirements

The development space should support:

### Canonical artifacts

Where is the authoritative current working version?

### Version history

What changed, when, and by whom?

### Issues

Where can ambiguities, bugs, requests, and objections be raised?

### Contributions

How can someone propose a change?

### Decisions

Where can someone discover why a substantive change was accepted or rejected?

### Tests

Where are test cases, fixtures, validators, or implementation results?

### Documentation

Where can supporting material be developed alongside the standard?

### Releases

How are stable snapshots identified?

### Archival continuity

Can the work survive the disappearance of a particular interface or maintainer?

---

# Pattern: One Development Commons, Many Interfaces

Avoid forcing all participation through one tool merely because it is convenient for developers.

The canonical repository may coexist with:

- forums;
    
- workshops;
    
- governance platforms;
    
- mailing lists;
    
- community calls;
    
- issue submission forms.
    

But contributions from those interfaces should eventually resolve into a persistent canonical record.

---

# Pattern: Preserve Provenance

For substantive changes, preserve enough information to answer:

- Who proposed this?
    
- What problem was it addressing?
    
- What alternatives were considered?
    
- What feedback was received?
    
- What decision was made?
    
- Why?
    
- In what release did it change?
