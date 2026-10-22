---
phase:
- scope
- develop
- launch
- review
domain:
- sustainability
- stewardship
- maintenance
- adoption
- governance
role: checkpoint
status: draft
actors:
- prospective-stewards
- maintainers
- adopters
- contributors
- funders
- infrastructure-providers
produces:
- sustainability-model
- stewardship-model
- resource-model
- maintenance-model
- support-model
- adoption-burden-assessment
- continuity-risks
- sustainability-conditions
---

---

# Think About Sustainability

## Intent

Determine whether the proposed standard can remain useful, governable, maintainable, and adoptable over a meaningful period of time.

Sustainability should be considered before development because design choices create future maintenance obligations.

The central question is:

> **If this standard succeeds, can the ecosystem actually carry it?**

---

# Sustainability Is More Than Funding

A standard can be financially funded and still be unsustainable.

Consider at least six forms of sustainability:

1. **Resource sustainability**
    
2. **Technical sustainability**
    
3. **Governance sustainability**
    
4. **Community sustainability**
    
5. **Adoption sustainability**
    
6. **Knowledge sustainability**

---
# Pattern: Prefer Existing Standards When They Are Good Enough

Reusing or extending existing standards is often the most powerful sustainability strategy.

It can reduce:

- design burden;
    
- maintenance burden;
    
- adoption burden;
    
- documentation burden;
    
- interoperability burden;
    
- community fragmentation.
    

Therefore sustainability should feed back into:

**What Could Be Used Instead?**

and:

**What Can Be Extended?**

An elegant new standard may still be the wrong choice if maintaining another ecosystem dependency creates more long-term cost than value.

---

# Pattern: Seek the Minimum Sustainable Standard

Do not ask only:

> What features could we include?

Ask:

> **What is the smallest standard that can create durable value?**

The minimum sustainable standard should be:

- useful;
    
- understandable;
    
- testable;
    
- extensible where necessary;
    
- maintainable;
    
- interoperable;
    
- governable.
    

This differs from a minimum viable prototype.

The goal is not merely to work once.

The goal is to remain worth carrying.

---

# Sustainability Model

A lightweight assessment might record:

```yaml
resource_model:
  startup:
  ongoing:
  likely_sources:
  dependency_risks:

technical_model:
  critical_dependencies:
  portability:
  reproducibility:
  continuity_plan:

stewardship_model:
  current_stewards:
  replacement_process:
  decision_process:
  escalation_path:

community_model:
  contributor_base:
  knowledge_distribution:
  onboarding:
  concentration_risks:

adoption_model:
  implementation_cost:
  support_needs:
  migration_burden:
  likely_adopter_capacity:

knowledge_model:
  documentation:
  decision_records:
  archives:
  provenance:

review_triggers:
open_questions:
```

---

# Pattern: Identify the Maintenance Surface

Every standard has a maintenance surface: the set of things that must continue to be cared for.

List them explicitly.

For example:

```text
specification
vocabulary
schemas
examples
validator
documentation
website
governance process
issue tracker
reference implementation
translations
registry
```

Then ask of every item:

> Who maintains this?

If the answer is unknown, that is a sustainability gap.

---

# Pattern: Distinguish Stable From Living Components

Not every part of a standard should change at the same rate.

Classify components as:

### Stable

Expected to change rarely.

### Living

Expected to evolve continuously.

### Generated

Derived automatically from another source.

### External

Maintained by another standard or institution.

This can dramatically reduce maintenance burden.

For example:

Do not manually copy an authoritative registry if it can be referenced safely.

---

# Pattern: Plan for Stewardship Transfer

Assume today's maintainers will eventually leave.

Ask:

- Can another group understand the standard?
    
- Can control of repositories and domains be transferred?
    
- Are permissions shared appropriately?
    
- Is licensing clear?
    
- Is institutional memory documented?
    
- Could the ecosystem fork the standard if stewardship failed?
    

A healthy open standard should be capable of surviving its founders.

---

# Pattern: Plan for Decline

Sustainability does not mean indefinite growth.

A standard may eventually:

- stabilize;
    
- merge into another standard;
    
- become obsolete;
    
- lose adoption;
    
- be replaced;
    
- be retired.
    

Therefore sustainability includes an eventual **retirement path**.

Ask:

> How would we stop maintaining this responsibly?

This will later connect directly to the Review phase.

---
