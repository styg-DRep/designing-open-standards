---
phase: develop
domain:
- standards-development
- implementation
- testing
- collaboration
role: checkpoint
status: draft
actors:
- stewards
- editors
- implementers
- testers
- contributors
- reviewers
- adopters
produces:
- development-outcomes-bundle
- candidate-standard
- test-evidence
- implementation-evidence
- documentation-set
- development-record
---

## Intent

Turn the justified development case produced during **Scope and Start** into a tested, documented, implementable open governance standard.

Development is not simply the writing phase.

It is the period in which the standards effort repeatedly asks:

> **Can the agreement we imagined actually be expressed clearly, implemented independently, used by real participants, challenged openly, and improved without losing coherence?**

Development therefore operates as a learning cycle:

```text
DESIGN
  ↓
EXPRESS
  ↓
IMPLEMENT
  ↓
TEST
  ↓
SHARE
  ↓
LEARN
  ↺
```

The standard becomes progressively more trustworthy through repeated encounters with:

- implementers;
    
- users;
    
- affected communities;
    
- existing infrastructure;
    
- other standards;
    
- edge cases;
    
- disagreements;
    
- actual governance practice.

---
# Development Phase Feedback Topology

```text
                       SCOPE & START
                            |
                          gates
                            v
                   DEVELOP THE STANDARD
                    ↗      ↑       ↖
                   /       |        \
               TEAM     PLATFORM   DOCUMENTATION
                |          |          ↑
                |          |          |
                └──────┐   |   ┌──────┘
                       v   v
                   WORKING DRAFT
                       |
                       v
                    TESTING
                    /  |  \
                   /   |   \
                  v    v    v
             defects evidence experience
                  \    |    /
                   \   |   /
                    v  v  v
                 SHARE PROGRESS
                       |
                       v
                 COMMUNITY INPUT
                       |
                       └──── returns-to ────┐
                                           |
                                      WORKING DRAFT
```

This should not be interpreted as one exact execution order.

The important feature is the **recurrence**.

---

# Development Loop

A healthy Development cycle might look like:

```text
1. Select a bounded development problem
2. Draft or modify the standard
3. Update implementation artifacts
4. Update documentation
5. Run tests
6. Attempt real implementation
7. Share the change and evidence
8. Gather review
9. Resolve issues and objections
10. Record decisions
11. Repeat
```

---

# What Should Remain Traceable From Scope?

Development inherits commitments from the Scope and Start Bundle.

Continuously check:

- Is this still the same opportunity?
    
- Are we still pursuing the same objectives?
    
- Are the original use cases still served?
    
- Has scope expanded?
    
- Are new actors affected?
    
- Are sustainability assumptions changing?
    
- Are interoperability commitments being honored?
    
- Are development principles still being followed?
    

Material changes should be recorded rather than allowed to become silent scope drift.

---

# Pattern: Development Can Reopen Scope

Development generates evidence that Scope could not.

Therefore the boundary must be permeable.

Examples:

**Testing reveals the intended use case is impossible**

→ `returns-to: Aims and Objectives`

**Implementers reveal another existing standard solves the issue**

→ `returns-to: Existing Standards`

**A new affected group becomes visible**

→ `returns-to: Understand the Ecosystem`

**The standard's adoption burden becomes unsustainable**

→ `returns-to: Think About Sustainability`

This does not mean Development failed.

It means Development performed its epistemic function.

---

# Emerging Development Outcomes

The five clusters should collectively generate at least:

## Working Standard

Stable enough to evaluate as a candidate for launch.

## Implementation Evidence

Evidence that independent participants can use or implement it.

## Test Suite and Results

Including valid, invalid, edge, and interoperability cases where appropriate.

## Documentation Set

Including:

- tutorial;
    
- how-to;
    
- reference;
    
- explanation;
    
- examples;
    
- normative specification;
    
- decision history.
    

## Development Infrastructure

A durable public development and issue-management environment.

## Participation Record

Who contributed, reviewed, tested, implemented, or objected.

## Early-Adopter Experience

Concrete evidence about actual use.

## Open Issues and Known Limitations

What remains unresolved.

## Release / Change History

How the candidate evolved.

---

# Development Readiness for the Next Phase

Development should eventually be able to answer:

1. Is there a coherent candidate standard?
    
2. Can independent participants understand it?
    
3. Can intended adopters implement or use it?
    
4. Have important use cases been demonstrated?
    
5. Have interoperability claims been tested?
    
6. Are normative requirements sufficiently unambiguous?
    
7. Are known failures and limitations documented?
    
8. Are supporting documentation and examples adequate?
    
9. Is development history inspectable?
    
10. Have meaningful external participants reviewed or tested it?
    
11. Are unresolved objections visible?
    
12. Is the artifact sufficiently stable to expose to wider adoption?
    

Those questions can later become the basis of the aggregate **Development Outcomes** gate.
