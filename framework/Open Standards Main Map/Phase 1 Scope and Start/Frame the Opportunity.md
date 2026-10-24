---
phase: scope
domain:
  - framing
  - opportunity
  - standards-landscape
role: checkpoint
status: draft
actors:
  - initiators
  - ecosystem-researchers
  - prospective-stewards
  - affected-participants
  - domain-experts
produces:
  - opportunity-frame
  - coordination-need
  - affected-participant-frame
  - benefit-hypotheses
  - candidate-interventions
  - candidate-standard-type
  - framing-assumptions
  - evidence-gaps
  - proceed-reframe-exit-decision
---

## Intent

Develop a shared, evidence-informed understanding of the condition the standards effort may attempt to change.

The opportunity frame should explain:

- what is happening now;
    
- why it matters;
    
- who experiences the condition;
    
- what improved state is sought;
    
- what coordination failure or opportunity appears present;
    
- whether standardization could plausibly help;
    
- what other responses might exist.
    

The objective is not to justify a predetermined standard.

The objective is to understand the situation well enough to decide **whether and where standardization belongs in the response**.

---

# Inputs

Frame the Opportunity is fed by several earlier and reciprocal sources.

## Simple Canvas

Provides:

- initial vision;
    
- opportunity hypothesis;
    
- asset hypothesis;
    
- use cases;
    
- participant assumptions;
    
- expected impacts;
    
- initial risks.
    

## Actor Map

Provides:

- relevant actors;
    
- activities;
    
- governance objects;
    
- infrastructure pointers;
    
- possible dependencies;
    
- actor gaps.
    

## Understand the Ecosystem

Provides:

- ecosystem map;
    
- relationships;
    
- infrastructure;
    
- existing standards;
    
- power and control observations;
    
- stakeholder understanding;
    
- alternatives.
    

## Types of Standards

Provides:

- language for identifying the coordination need;
    
- possible standardization surfaces;
    
- candidate forms of agreement.
    

---

# Core principle

**Frame the condition before framing the intervention.**

A useful opportunity frame should remain understandable if every reference to the proposed standard is removed.

If the description only makes sense in terms of the proposed solution, the opportunity has not yet been adequately framed.

---

# Pattern: Describe the Present Condition

Begin with what is happening now.

Avoid:

> We lack a standard for X.

Prefer:

> Participants currently encounter X condition, which produces Y consequence under Z circumstances.

For example:

> Governance participants cannot reliably compare the assumptions and expected impacts of materially different proposals because those claims are expressed inconsistently across tools and processes.

This describes a condition that can later be investigated.

---

# Pattern: Locate the Coordination Need

Ask:

> **What specifically needs to become more consistent, comparable, repeatable, interoperable, or mutually understandable?**

Possible coordination needs include:

- shared meaning;
    
- comparable information;
    
- interoperable records;
    
- repeatable process;
    
- common identifiers;
    
- transparent provenance;
    
- consistent evaluation;
    
- reusable governance practices.
    

This inquiry connects directly to **Types of Standards**.

---

# Pattern: Identify Who Experiences It

Describe whose activity is constrained by the current condition.

Distinguish:

- people directly experiencing the difficulty;
    
- downstream people affected by its consequences;
    
- people whose behavior contributes to it;
    
- infrastructure maintainers;
    
- institutions affected by changing it.
    

Use the Actor Map and Ecosystem Map rather than relying solely on intuition.

---

# Pattern: Describe the Desired Difference

Do not jump immediately to an artifact.

Ask:

> **What would become meaningfully different if this opportunity were realized?**

Examples:

- proposals become easier to compare;
    
- governance histories become easier to inspect;
    
- multiple tools can exchange records;
    
- participants can use consistent terminology;
    
- deliberation becomes more transparent;
    
- decisions become easier to audit.
    

The desired state should describe capability or condition, not merely the existence of a standard.

---

# Pattern: Surface the Benefit Hypothesis

For each important participant ask:

> What becomes better for them?

Then ask:

> What must be true for that benefit to occur?

This produces an explicit chain:

```text
standardized capability
        ↓
changed behavior or interoperability
        ↓
participant benefit
        ↓
ecosystem effect
```

Each arrow is an assumption that can later be tested.

---

# Pattern: Separate Need From Demand

A standards effort may identify a genuine coordination need without evidence that participants want the proposed intervention.

Record separately:

- observed need;
    
- expressed demand;
    
- predicted benefit;
    
- willingness to participate;
    
- willingness to adopt.
    

This distinction helps prevent a technically elegant standard from being mistaken for an adoptable one.

---

# Pattern: Generate Multiple Intervention Classes

Before deciding that standardization is the answer, identify plausible alternative interventions.

These might include:

- documentation;
    
- education;
    
- interface improvement;
    
- tooling;
    
- policy change;
    
- process change;
    
- institutional reform;
    
- coordination practice;
    
- adoption of an existing standard;
    
- extension of an existing standard;
    
- opening an existing convention;
    
- creation of a new standard.
    

A healthy opportunity frame allows several of these to coexist.

---

# Pattern: Identify the Standardization Surface

If standardization appears useful, ask:

**What exactly would be standardized?**

Examples:

- terms;
    
- concepts;
    
- identifiers;
    
- classifications;
    
- metadata;
    
- records;
    
- interfaces;
    
- exchange formats;
    
- evaluation criteria;
    
- practices;
    
- protocols;
    
- procedures.
    

Then consult **Types of Standards**.

---

# Pattern: Test the Counterfactual

Ask:

> **What happens if we do not create a standard?**

Possible answers:

- the problem remains;
    
- another intervention solves it;
    
- existing convergence continues organically;
    
- competing standards emerge;
    
- infrastructure providers define the de facto standard;
    
- the opportunity is not important enough to justify intervention.
    

This helps estimate both urgency and necessity.

---

# Pattern: Look for Existing Coordination

Many ecosystems already contain partial standards.

Look for:

- repeated terminology;
    
- common templates;
    
- shared tooling assumptions;
    
- de facto schemas;
    
- habitual processes;
    
- dominant interfaces;
    
- recurring community norms.
    

The opportunity may therefore be:

> formalize what already works,

rather than:

> invent something new.

---

# Pattern: Capture Competing Frames

Different actors may understand the same situation differently.

Do not force premature consensus.

Record competing frames explicitly.

For example:

**Frame A**

> Proposal information is inconsistent.

**Frame B**

> Proposal information is adequate, but discovery tools are poor.

**Frame C**

> The real problem is insufficient deliberation, not information structure.

These competing explanations are valuable.

They identify where evidence is required.

---

# Pattern: Evidence Before Resolution

For each major claim mark:

- `observed`
    
- `reported`
    
- `inferred`
    
- `assumed`
    
- `contested`
    
- `unknown`
    

Important assumptions should become explicit research questions.

---

# Pattern: Frame at the Right Scale

Avoid frames so broad they cannot guide action:

> Governance is confusing.

Avoid frames so narrow they already encode a preferred solution:

> Governance actions lack field X in schema Y.

Look for the level at which:

- the condition is concrete;
    
- actors can be identified;
    
- consequences can be observed;
    
- several interventions remain possible.
    

---

# Working template

A useful opportunity statement might take the form:

> **[Actors] encounter [condition] when [context], resulting in [consequence]. Improving [coordination capability] could enable [desired difference], but we still need to determine whether [standardization or alternatives] provide the most appropriate intervention.**

---

# Opportunity frame artifact

```yaml
current_condition:
affected_actors:
context:
consequences:
coordination_need:
desired_difference:
benefit_hypotheses:
existing_coordination:
possible_interventions:
candidate_standardization_surface:
candidate_standard_types:
existing_standards:
competing_frames:
evidence:
assumptions:
open_questions:
```

---

# Gate condition

The opportunity is framed well enough to proceed when participants can answer:

1. What condition currently exists?
    
2. Who experiences or contributes to it?
    
3. Why does it matter?
    
4. What coordination need appears underneath it?
    
5. What improved condition is sought?
    
6. What evidence supports the frame?
    
7. What important assumptions remain?
    
8. What existing coordination already exists?
    
9. What plausible interventions could address it?
    
10. Why might standardization be appropriate?
    
11. What kind of standardization might be involved?
    
12. What evidence could cause us to abandon or materially reframe the effort?
    

---

# Possible gate outcomes

This checkpoint should allow several legitimate outcomes.

## Proceed

The opportunity is sufficiently understood and standards work appears justified.

## Reframe

The condition is real, but the current opportunity frame is inaccurate or incomplete.

Return to:

- ecosystem mapping;
    
- stakeholder inquiry;
    
- Simple Canvas;
    
- additional research.
    

## Adopt or extend

An existing standard appears capable of addressing the opportunity.

Redirect toward adoption or extension.

## Use another intervention

The opportunity is valid, but a standard is not the most appropriate response.

## Stop

Evidence no longer supports the original premise strongly enough to justify continued work.

Stopping is a successful scoping outcome when it prevents unnecessary standards development.

---

# Reciprocal relationship with Understand the Ecosystem

These nodes should continually correct one another.

```text
              SIMPLE CANVAS
                    |
                    | feeds
                    v
          FRAME THE OPPORTUNITY
               ↕           \
       returns-to / informs  \ consults
             ↕               \
   UNDERSTAND THE ECOSYSTEM    TYPES OF STANDARDS
             ↕                       |
             |                       |
             └──── existing standards
```

**Frame the Opportunity → informs → Understand the Ecosystem**

because framing establishes what portion of the ecosystem deserves investigation.

**Understand the Ecosystem → returns-to → Frame the Opportunity**

because ecosystem research may reveal that:

- different actors experience the problem;
    
- the apparent problem is caused elsewhere;
    
- existing standards already apply;
    
- the proposed intervention would redistribute power;
    
- the opportunity is broader or narrower than assumed.
    

This reciprocal loop should continue until both descriptions are mutually coherent.

---

# Relationship to Types of Standards

Types of Standards should **inform**, not gate, Frame the Opportunity.

Its purpose is to help participants recognize whether the coordination need appears related to:

- shared meaning;
    
- exchange/interoperability;
    
- repeatable practice;
    
- or some combination.
    

The opportunity should never be reshaped merely to fit one of the available categories.

If the situation does not fit cleanly, the classification should bend before the evidence does.
