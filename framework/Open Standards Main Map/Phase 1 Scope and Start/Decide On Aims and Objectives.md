---
phase: scope
domain:
- purpose
- impact
- design-intent
role: checkpoint
status: draft
actors:
- prospective-stewards
- affected-participants
- ecosystem-researchers
- domain-experts
- prospective-adopters
produces:
- aim
- objectives
- theory-of-change
- core-feature-hypotheses
- interoperability-intent
- adaptability-intent
- accessibility-intent
- initial-test-intent
- development-principles
- success-hypotheses
---

---

# Decide on Aims and Objectives

## Intent

Translate the framed opportunity and ecosystem understanding into a clear statement of what the standards effort intends to accomplish.

This node answers:

> **If this standards effort succeeds, what should become different, and what must the effort accomplish to contribute to that change?**

The aim establishes direction.

The objectives describe the important changes, capabilities, or conditions the work must create in order to move in that direction.

They should be specific enough to guide development without prematurely locking the effort into a particular implementation.

---

# Inputs

This node should draw directly from:

- **Simple Canvas**
    
- **Frame the Opportunity**
    
- **Understand the Ecosystem**
    
- **Actor Map**
    
- **Existing Standards**
    
- **Types of Standards**
    
- research and stakeholder feedback
    

The aims should therefore emerge from scoping evidence rather than simply formalising the intentions of the initiating group.

---

# Distinguish Aim, Objective, Feature, and Measure

These concepts should not be collapsed.

## Aim

The broad change the standards effort seeks to contribute toward.

> _Make governance proposals easier to interpret, compare, exchange, and build upon across the Cardano ecosystem._

## Objectives

Conditions or capabilities that must become true to meaningfully advance that aim.

> _Establish a shared model for describing proposal purpose, assumptions, impacts, and status._

> _Enable governance tools to exchange proposal records consistently._

## Features

Properties of the standard intended to enable those objectives.

> machine-readable schema  
> shared identifiers  
> extensible vocabulary

## Measures

Evidence used later to determine whether those objectives are actually being achieved.

> number of interoperable implementations  
> successful validation rate  
> participant comprehension

This distinction prevents the project from confusing **what it builds** with **what it changes**.

---

# Pattern: Aim at Change, Not Delivery

Avoid aims such as:

> Publish version 1 of the standard.

That is an output.

Prefer:

> Enable governance participants and tools to exchange comparable governance information with substantially less bespoke translation.

The standard itself is an intervention.

The aim describes the condition the intervention is intended to help produce.

---

# Pattern: Objectives Describe Necessary Progress

Objectives should identify meaningful intermediate accomplishments between producing the standard and realizing the broader aim.

Ask:

- What must participants be able to do?
    
- What must become easier?
    
- What must become more consistent?
    
- What must become interoperable?
    
- What must become understandable?
    
- What capabilities must exist?
    
- What coordination friction must diminish?
    

Objectives should make the underlying causal logic visible.

---
# Pattern: Objectives Need Evidence, Not Just SMARTness

SMART can be useful for operational planning, but it should not become the primary test of a standards objective.

The attached Theory of Change guide makes a useful caution: specifying numerical targets too early can distract from understanding the underlying causal logic, and performance measurement should follow rather than substitute for that reasoning.

For this framework, objectives should first be:

- **meaningful** — connected to the intended change;
    
- **traceable** — connected to evidence and the opportunity;
    
- **plausible** — supported by a credible causal path;
    
- **bounded** — clear about what the standards effort can contribute;
    
- **testable** — capable eventually of being evaluated;
    
- **revisable** — capable of changing as the ecosystem learns.
    

SMART criteria may then help operationalize particular objectives where appropriate.

---

# Pattern: Distinguish Contribution From Control

Standards efforts rarely control ecosystem outcomes.

Use language such as:

> contribute to

> enable

> make possible

> reduce barriers to

> increase likelihood of

rather than:

> cause

> guarantee

> ensure

unless the causal relationship genuinely supports such language.

This is especially important in decentralized governance.

---

# Aim and Objectives Artifact

A useful output structure is:

```yaml
aim:

objectives:
  - objective:
    intended_change:
    affected_actors:
    evidence:
    mechanism:
    required_capabilities:
    success_signal:
    assumptions:

theory_of_change:
  current_pattern:
  intervention:
  mechanisms:
  outcomes:
  intended_impact:
  enabling_conditions:
  assumptions:
  unintended_effects:

core_features:
interoperability_intent:
adaptability_intent:
accessibility_intent:
test_intent:
development_principles:
open_questions:
```

---

# Gate Condition

Aims and objectives are sufficiently developed when participants can answer:

1. What broad change is this effort trying to contribute toward?
    
2. What objectives must be achieved for that change to become more likely?
    
3. How does each objective relate to the framed opportunity?
    
4. Who must experience a changed condition?
    
5. What mechanism plausibly connects the standard to those changes?
    
6. What capabilities must the standard therefore possess?
    
7. What must interoperate with existing ecosystem infrastructure?
    
8. What must remain stable and what should be extensible?
    
9. Who could be excluded if accessibility is ignored?
    
10. How might the major claims eventually be tested?
    
11. What assumptions make the causal logic vulnerable?
    
12. What procedural principles govern development?
    

---

# Possible Gate Outcomes

## Proceed

A coherent and appropriately bounded set of aims and objectives exists.

## Refine

The direction is broadly sound but objectives remain vague, untraceable, or overly implementation-specific.

## Return to Opportunity

The ToC exposes that the proposed objectives do not adequately address the framed opportunity.

**returns-to → Frame the Opportunity**

## Return to Ecosystem

Important actors, dependencies, or enabling conditions are missing.

**returns-to → Understand the Ecosystem**

## Reconsider the Intervention

The causal model suggests that a standard is unlikely to meaningfully affect the desired outcome.

This may redirect the effort toward another intervention.

---

# Initial topology

```text
                  Frame the Opportunity
                          |
                          | feeds
                          v
               Research & Feedback
                          |
                          v
                Theory of Change
                          |
                          | informs
                          v
              DECIDE AIMS & OBJECTIVES
                 /    /   |   \    \
                /    /    |    \    \
               v    v     v     v    v
            Core  Interop Adapt Access Test
          Features        /Extend
                \          |          /
                 \         |         /
                  └────────┼────────┘
                           |
                           v
                 Development Principles
                           |
                           v
                 Scope & Start outcomes
```

Several of these relationships are reciprocal.

In particular:

**Theory of Change —informs→ Aims and Objectives**

but also:

**Aims and Objectives —returns-to→ Theory of Change**

when stating the objectives exposes an implausible or missing causal mechanism.

Similarly:

**Interoperability —returns-to→ Existing Standards**

when a required dependency reveals standards that were not previously mapped.

The cluster should therefore be understood as **convergence around purpose**, not as a linear mini-process.
