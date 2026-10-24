---
phase: develop
domain:
- standards-development
role: entry-point
status: draft
actors:
- editors
- domain-experts
- implementers
- contributors
- stewards
produces:
- working-drafts
- candidate-specifications
- vocabularies
- schemas
- protocols
- guidance
- models
- implementation-artifacts
---

## Intent

Transform the approved scope, use cases, objectives, and core-feature hypotheses into a concrete reusable agreement.

What gets developed depends upon the standard type.

Possible products include:

- vocabulary;
    
- taxonomy;
    
- ontology;
    
- register;
    
- specification;
    
- schema;
    
- exchange format;
    
- API contract;
    
- protocol;
    
- process;
    
- method;
    
- code of practice;
    
- governance model;
    
- implementation profile.
    

Development may mean creating guidance, vocabularies, schemas, models, or exchange formats depending upon the type of standard.

## Pattern: Develop Claims, Not Just Text

Treat each important part of the emerging standard as a claim:

> **If implementers follow this agreement, some desired form of consistency or interoperability will result.**

Each such claim should eventually connect to:

- a use case;
    
- an objective;
    
- implementation evidence;
    
- a test;
    
- or an explicit rationale.
    

---

# Pattern: Maintain Traceability

Where practical, preserve:

```text
Opportunity
   ↓
Objective
   ↓
Use Case
   ↓
Requirement
   ↓
Standard Feature
   ↓
Implementation
   ↓
Test
```

Not every contribution requires a bureaucratic trace.

But important normative requirements should have an intelligible reason for existing.

---

# Pattern: Normative vs Informative

Explicitly distinguish material that participants **must follow** from material intended to help them understand or implement the standard.

Use categories such as:

- `normative`
    
- `informative`
    
- `example`
    
- `experimental`
    

This becomes especially important as documentation grows.
