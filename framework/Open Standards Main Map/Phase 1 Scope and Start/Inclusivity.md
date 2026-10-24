---
phase: scope
domain:
  - inclusivity
  - accessibility
  - participation
role: supporting
status: draft
produces:
  - inclusivity-intent
  - accessibility-intent
  - translation-intent
  - participation-barriers
---

## Intent

Identify who could be excluded from shaping, using, governing, or benefiting from the standard, and what the standard must therefore make room for.

Inclusivity is broader than access. It asks whether the standard can hold the range of people, practices, languages, capacities and contexts in the ecosystem it intends to serve, without requiring them to become alike in order to take part.

Ask:

> **Who could theoretically use, shape, or be served by this standard but practically cannot?**

This may materially change the objectives themselves.

---

# Where Exclusion Happens

Look at each point where people meet the standard:

- **Development** — who can take part in shaping it: language, time, funding, tooling, expertise, the cost of participating at all;
- **Use** — who can adopt or implement it: technical complexity, infrastructure, bandwidth, implementation cost;
- **Governance** — who can propose changes, raise objections, or become a steward;
- **Consequence** — who is affected by the standard without ever touching it.

The same group may be included at one point and excluded at another.

---

# Translation, Understood Broadly

Many exclusions are failures of translation.

Translation may include:

- spoken language;
- technical ↔ nontechnical language;
- human ↔ machine representation;
- expert ↔ newcomer communication;
- visual accessibility;
- low-bandwidth access;
- cultural or institutional context.

---

# Pattern: Inclusion Is Not Uniformity

A standard can exclude by requiring everyone to work the same way.

Distinguish:

- **variation the standard should accommodate** — legitimate differences in governance practice, language, capacity or context;
- **variation that would destroy interoperability.**

Where legitimate variation exists, prefer extension points, profiles or guidance over a single required form. This is the participatory side of the stable core and open edge in *Adaptability and Extensibility*.

---

# Pattern: Name the Cost of Taking Part

Participation is not free.

Record who bears the cost of contributing, reviewing, testing and adopting.

A process that depends on unpaid time, a dominant language, specialist tooling or a particular time zone will tend to select for the people who already have them — and the resulting standard will encode their assumptions.

---

# Pattern: Look for Exclusion Through Success

A standard that works exactly as intended can still narrow who takes part, by making some forms of governance information visible, comparable or required, and leaving others out.

Ask:

> **Who becomes less legible if this standard succeeds?**

---

# Inclusivity Intent

```yaml
inclusivity_intent:
  excluded_from_development:
  excluded_from_use:
  excluded_from_governance:
  affected_without_access:
  translation_needs:
  accessibility_requirements:
  legitimate_variation:
  participation_costs:
  success_exclusion_risks:
```
