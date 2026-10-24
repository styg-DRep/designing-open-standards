---
phase: launch
domain:
- adoption
- support
- education
role: supporting
status: draft
actors:
- adopters
- implementers
- educators
- support-providers
- stewards
produces:
- adopter-guidance
- training
- support-record
- adoption-tools
- recurring-adopter-issues
---

## Intent

Reduce the practical distance between:

> **“The standard exists”**

and:

> **“An independent actor can use it competently.”**

Support should be tailored to the needs of different adopter roles.

---

# Pattern: Support the Adoption Journey

Think of adoption as a sequence:

```text
discover
  ↓
understand
  ↓
evaluate
  ↓
experiment
  ↓
implement
  ↓
validate
  ↓
integrate
  ↓
operate
  ↓
update
```

Different support is needed at each stage.

---

# Discovery Support

Help actors answer:

- What is this?
    
- Is it relevant to me?
    
- What problem does it address?
    
- Where do I start?
    

Useful artifacts:

- overview;
    
- examples;
    
- comparison with existing practice;
    
- adoption stories.
    

---

# Evaluation Support

Help actors determine:

- Does this fit our needs?
    
- What will adoption cost?
    
- What dependencies exist?
    
- What changes will we need to make?
    

Useful artifacts:

- conformance overview;
    
- migration guide;
    
- compatibility information;
    
- implementation checklist;
    
- risk and limitation summary.
    

---

# Implementation Support

Help adopters actually use the standard.

Possible support:

- tutorials;
    
- how-to guides;
    
- schemas;
    
- validators;
    
- libraries;
    
- reference implementations;
    
- examples;
    
- office hours;
    
- helpdesk;
    
- forums.
    

---

# Operational Support

Once adopted, help users deal with:

- errors;
    
- updates;
    
- interpretation;
    
- version changes;
    
- interoperability issues;
    
- migration;
    
- edge cases.
    

---

# Pattern: Support the Whole Adoption System

The direct adopter may not be the only actor who needs help.

For governance standards, adoption may involve:

- decision-makers;
    
- policy teams;
    
- operational staff;
    
- developers;
    
- analysts;
    
- governance participants;
    
- legal or compliance reviewers;
    
- community facilitators.
    

The standard may fail because one of these surrounding roles cannot support adoption.

---

# Pattern: Treat Support Requests as Evidence

A support channel is not merely a service function.

Repeated questions expose:

- unclear specification;
    
- missing documentation;
    
- difficult concepts;
    
- unrealistic assumptions;
    
- adoption friction;
    
- recurring edge cases.
    

Classify support requests where useful:

```yaml
support_issue:
category:
  - documentation
  - specification
  - tooling
  - interoperability
  - governance
  - education
  - adoption-cost
frequency:
severity:
resolution:
feeds:
```

Frequent support issues should feed back into Development or Review.

---

# Pattern: Build Community Capacity, Not Permanent Dependence

Support should progressively help the ecosystem answer its own questions.

Encourage:

- peer support;
    
- implementer communities;
    
- shared examples;
    
- community-maintained tools;
    
- independent training;
    
- third-party documentation.
    

A standard is healthier when adoption knowledge is distributed.
