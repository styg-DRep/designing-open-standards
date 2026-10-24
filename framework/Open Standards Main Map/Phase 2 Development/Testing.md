---
phase: develop
domain:
- testing
- validation
- implementation
role: checkpoint
status: draft
actors:
- testers
- implementers
- early-adopters
- editors
produces:
- test-suite
- implementation-evidence
- interoperability-evidence
- failure-register
- conformance-criteria
- test-results
---

## Intent

Expose the developing standard to enough independent reality that confidence rests on evidence rather than internal agreement.

---

# Testing Subtypes

## Semantic Testing

Ask:

> Do independent participants interpret the same requirement in materially the same way?

Useful for:

- terminology;
    
- classifications;
    
- guidance;
    
- ambiguous normative language.
    

---

## Conformance Testing

Ask:

> Does an artifact or implementation satisfy the stated requirements?

Produces:

- valid examples;
    
- invalid examples;
    
- validation rules.
    

---

## Interoperability Testing

Ask:

> Can independent implementations interact without bespoke coordination?

This is one of the strongest tests of an open standard.

Prefer multiple independent implementations where practical.

---

## Use-Case Testing

Ask:

> Does the standard actually support the use cases that justified it?

A specification can be internally consistent while failing the original purpose.

---

## Implementation Testing

Ask:

> Can an implementer build against the standard using only the available specification and supporting materials?

Watch for:

- undocumented assumptions;
    
- reliance on editor knowledge;
    
- unclear requirements;
    
- impractical complexity.
    

---

## Adoption / Usability Testing

Ask:

> Can intended adopters understand and integrate the standard at a reasonable cost?

This exposes barriers that pure conformance tests cannot.

---

## Governance Testing

For process or governance standards ask:

> What happens when participants disagree, fail, abstain, arrive late, or encounter an unanticipated case?

Test the **exception path**, not only the happy path.

---

## Regression Testing

When the standard changes:

> Did fixing one problem break something that previously worked?

---

## Adversarial and Edge-Case Testing

Ask:

- What happens at minimum and maximum values?
    
- What happens when information is missing?
    
- What happens when participants behave strategically?
    
- What happens when inputs conflict?
    
- What happens when infrastructure fails?
    
- What happens when an implementation follows the letter but violates the intention?
    

Particularly important for governance standards.

---

# Pattern: Every Important Failure Becomes Information

Record:

```yaml
test:
expected:
observed:
classification:
  - specification-defect
  - implementation-defect
  - documentation-defect
  - use-case-defect
  - assumption-defect
severity:
resolution:
```

A failed test is not automatically evidence that an implementation is wrong.

It may reveal that the **standard itself is wrong**.

---

# Testing Return Edges

Testing should be capable of:

**returns-to → Develop the Standard**

for specification defects.

**returns-to → Documentation**

for comprehension or implementation guidance defects.

**returns-to → Aims and Objectives**

if evidence reveals the standard cannot plausibly achieve an objective.

**returns-to → Frame the Opportunity**

in exceptional cases where implementation evidence exposes a faulty original premise.

---

# Pattern: Testing Produces Confidence, Not Proof

Passing a test suite establishes evidence about known scenarios.

It does not prove universal correctness.

Preserve:

- untested areas;
    
- known limitations;
    
- environmental assumptions;
    
- implementation diversity.
