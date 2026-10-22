---
phase: scope
domain:
- development
- planning
role: supporting
status: draft
---

Once the method is chosen, turn it into an actionable development model.

The plan should explain:

> **What work will happen, in what sequence or cycles, by whom, using what infrastructure, with what tests and decisions.**

---

# Plan: Prioritize the Core

Carry forward the core-feature work from Aims and Objectives.

Separate:

- essential;
    
- desirable;
    
- optional;
    
- explicitly deferred.
    

Ask of every core feature:

> If this is absent, does the standard still solve the intended coordination problem?

Prioritize a **small robust core** over premature comprehensiveness.

---

# Plan: Define Development Units

Decide what can be developed and tested independently.

Possible units include:

- vocabulary;
    
- conceptual model;
    
- schema;
    
- protocol;
    
- API;
    
- implementation guide;
    
- validator;
    
- governance process;
    
- examples;
    
- test fixtures.
    

Smaller development units make feedback more precise.

---

# Plan: Establish Phases or Cycles

Examples might include:

```text
Discovery
→ Alpha
→ Tested Draft
→ Candidate
→ Stable Release
```

or:

```text
Explore
→ Build
→ Test
→ Integrate
→ Review
→ Repeat
```

The names matter less than making clear:

- what each stage is trying to learn or establish;
    
- what artifacts it produces;
    
- what evidence permits progression.
    

---

# Plan: Make Testing Native to Development

Testing should not be an event after drafting.

For each development phase identify:

- what is being tested;
    
- who will test it;
    
- what scenario is used;
    
- what evidence is recorded;
    
- what failure looks like;
    
- who interprets the result.
    

Different standards require different testing.

## Semantic testing

Do people interpret terms consistently?

## Exchange testing

Can independent systems exchange valid information?

## Process testing

Can participants actually follow the guidance?

## Adoption testing

Can intended users incorporate the standard without unreasonable friction?

## Governance testing

Can ambiguity, disagreement, and change be handled through the proposed governance model?

---

# Plan: Define Contribution Rules

Because the standard is being developed openly, make explicit:

- how contributions are proposed;
    
- who can contribute;
    
- where discussion occurs;
    
- how proposals are reviewed;
    
- how decisions are recorded;
    
- how dissent is preserved;
    
- how intellectual property is licensed;
    
- how contributor provenance is retained.
    

Open access to a repository is not the same as an open contribution process.

---

# Plan: Choose Development Infrastructure

Choose tools that support the development method.

Possible infrastructure includes:

- version control;
    
- issue tracking;
    
- discussion forums;
    
- decision records;
    
- documentation;
    
- test repositories;
    
- validators;
    
- reference implementations;
    
- public roadmaps;
    
- meeting archives.
    

Selection criteria should include:

- accessibility;
    
- transparency;
    
- persistence;
    
- portability;
    
- machine readability where useful;
    
- low barriers to participation.
    

---

# Plan: Define Decision Rights

Make explicit who can:

- accept changes;
    
- reject changes;
    
- request revisions;
    
- declare a release;
    
- change scope;
    
- alter the method;
    
- resolve deadlock.
    

This does not require centralized ownership.

Distributed governance makes explicit decision rights more important, not less.

---

# Pattern: Separate Contribution From Decision

A healthy open process can allow broad contribution while retaining clear responsibility for deciding whether a contribution enters a release.

Document both.
