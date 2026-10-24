---
phase:
- scope
- develop
- review
domain:
- standards
- classification
- design
role: supporting
status: stable
actors:
- standards-developers
- ecosystem-researchers
- prospective-stewards
- reviewers
produces:
- standard-type-classification
- candidate-standard-form
- comparison-language
- specification-options
---

# Types of Standards

## Intent

Provide a shared reference for recognizing, comparing, and designing the kinds of reusable agreements that may function as open governance standards.

The cluster helps participants answer:

> **What kind of thing are we actually trying to standardize?**

It should be consulted when:

- identifying existing standards in the ecosystem;
    
- framing an opportunity;
    
- determining whether a standard is an appropriate response;
    
- choosing the form of a proposed standard;
    
- comparing candidate approaches;
    
- combining multiple standard types;
    
- reviewing whether an existing standard still matches its intended purpose.
    

Unlike most development nodes, this cluster is primarily **classificatory infrastructure**.

Its contents should change rarely, but its classifications should be referenced often.

---

# Principle

**Classify by purpose before classifying by artifact.**

Do not begin with:

> We need a schema.

Begin with:

> What kind of coordination needs to become reusable and consistent?

The artifact should follow from the coordination problem.

---

# Three primary families

This framework identifies three broad purposes:

1. **Shared Vocabulary**

2. **Exchange**

3. **Guidance**


A governance standard may serve one family primarily or combine several.

---
# Standards Can Be Composite

Most meaningful governance standards will combine types.

For example, a governance proposal standard could contain:

**Vocabulary**

- defined proposal types
    
- status terms
    
- identifiers
    

**Exchange**

- machine-readable metadata schema
    
- API representation
    

**Guidance**

- recommendations for documenting evidence
    
- publication practices
    
- review procedures
    

Therefore classify standards using:

```yaml
primary_type:
secondary_types:
```

rather than requiring a single exclusive category.

---

# Pattern: Separate Purpose From Product

The same artifact can serve different purposes.

A “model,” for example, might:

- define shared concepts;
    
- guide a process;
    
- support an exchange specification.
    

Therefore do not classify a standard solely from the name of its artifact.

Ask:

> **What coordination function does this artifact perform?**

---

# Pattern: Identify the Standardization Surface

Before choosing a standard type, ask exactly what is being made consistent.

Possible standardization surfaces include:

### Meaning

What concepts, classifications, or relationships should mean the same thing?

→ likely **Shared Vocabulary**

### Representation

What information must be structured consistently?

→ likely **Exchange**

### Transfer

How should information move between systems or actors?

→ likely **Exchange**

### Practice

What activity should be performed consistently?

→ likely **Guidance**

### Evaluation

What criteria should be used consistently?

→ often **Guidance + Vocabulary**

### Identity

How should entities be recognized consistently?

→ often **Vocabulary + Exchange**

### Record

What information should persist about governance activity?

→ often **Vocabulary + Exchange**

### Process

What sequence, method, or protocol should participants follow?

→ likely **Guidance**

---

# Pattern: Match Strength of Standardization to Need

Not every coordination problem requires the same strength of agreement.

A spectrum might run:

```text
shared suggestion
      ↓
recommended practice
      ↓
common vocabulary
      ↓
structured template
      ↓
formal specification
      ↓
machine-validatable rule
      ↓
protocol requirement
```

Ask:

> **How much consistency does the problem actually require?**

Over-standardization can suppress legitimate variation.

Under-standardization can leave interoperability problems unresolved.

---

# Pattern: Standardize the Minimum Necessary Surface

Prefer the smallest agreement that enables the desired coordination.

Do not standardize:

- implementation details that can safely vary;
    
- terminology that does not affect interoperability;
    
- practices whose diversity is beneficial;
    
- local decisions that do not require ecosystem-wide consistency.
    

A good open standard creates **shared constraint where shared constraint is valuable**, while preserving freedom elsewhere.

---

# Pattern: Reuse Before Reinvention

Types of Standards should directly inform the ecosystem inquiry.

Once the likely standardization surface is identified, search specifically for:

- existing vocabularies;
    
- existing identifiers;
    
- existing schemas;
    
- existing protocols;
    
- existing APIs;
    
- existing codes of practice;
    
- existing models;
    
- existing governance procedures.
    

This makes the reference cluster an input to:

**Identify Current Ecosystem Standards**

rather than merely a design reference used later.

---

# Classification output

When the cluster is consulted for a standards effort, produce a lightweight classification:

```yaml
coordination_need:
standardization_surface:
primary_type:
secondary_types:
possible_products:
required_strength:
existing_reference_points:
open_questions:
```

This output should remain provisional during scoping.

---

# Relationship to the broader map

```text
                     TYPES OF STANDARDS
                       [REFERENCE]
                      /     |      \
                     /      |       \
                    v       v        v
          Shared Vocabulary Exchange Guidance
                    \       |       /
                     \      |      /
                      \     |     /
                       classification
                            |
       ┌────────────────────┼────────────────────┐
       |                    |                    |
       v                    v                    v
Frame the Opportunity   Identify Existing    Develop Standard
                        Standards
       ^                    |                    |
       |                    |                    |
       └──── informs ───────┴──── informs ──────┘
                            |
                            v
                          Review
```

This cluster should therefore have many **informs** relationships and relatively few sequential edges.

It behaves more like a shared conceptual library than a stage in the lifecycle.
