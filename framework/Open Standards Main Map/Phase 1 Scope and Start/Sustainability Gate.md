---
phase: scope
domain:
- sustainability
role: checkpoint
status: draft
---

# Sustainability Gate

A standards effort has considered sustainability sufficiently when it can answer:

1. What ongoing work will exist after initial development?
    
2. Who is expected to perform that work?
    
3. What ongoing resources does it require?
    
4. What technical dependencies could threaten continuity?
    
5. How can maintainers be replaced?
    
6. How will changes be governed?
    
7. What support will adopters require?
    
8. What is the likely implementation burden?
    
9. What knowledge needs to persist?
    
10. What components should remain stable versus evolve?
    
11. Can the scope be reduced without sacrificing the aim?
    
12. Could using or extending an existing standard produce a more sustainable outcome?
    
13. What happens if the standard eventually needs to be retired?
    

---

# Possible Outcomes

## Sustainable Enough to Proceed

The expected burden is proportionate to the expected value.

## Reduce Scope

The proposed standard creates excessive ongoing obligations.

## Simplify Governance

The stewardship mechanism is heavier than the community can support.

## Strengthen Stewardship

The standard would create ecosystem dependency without sufficient continuity.

## Reuse or Extend

An existing standard offers a more sustainable path.

## Pause

The opportunity remains valid but ongoing capacity is not credible.

---

# Lifecycle Role

Unlike most Scope nodes, Sustainability should remain active throughout the lifecycle.

```text
SCOPE
  ↓
initial sustainability model
  ↓
DEVELOP
  ↓
observe actual maintenance burden
  ↓
LAUNCH
  ↓
observe adoption/support burden
  ↓
REVIEW
  ↓
compare expected vs actual sustainability
  ↓
adapt / simplify / transfer / retire
```

This makes Sustainability both:

**a Scope checkpoint**

and

**a persistent lifecycle concern.**

---

# Relationship to Development Method

```text
          Think About Sustainability
              ↕             ↕
      Choose Method ←→ Plan Development
              \             /
               \           /
                v         v
                Approval
                   |
                   v
              Scope & Start
```

Sustainability should be capable of changing:

- the development method;
    
- the number of features;
    
- the release model;
    
- the governance model;
    
- the infrastructure;
    
- the adopter support promise.
    

Likewise, each of those choices changes the sustainability model.
