---
phase: launch
domain:
- release
- communication
- adoption
role: supporting
status: draft
actors:
- stewards
- editors
- ecosystem-liaisons
- early-adopters
produces:
- launch-plan
- stable-release
- launch-materials
- adoption-entry-points
- public-release-record
---

## Intent

Make the standard publicly legible, discoverable, accessible, and ready for use by audiences beyond the development group.

The launch should answer:

- What is being released?
    
- Why should anyone care?
    
- Who is it for?
    
- What can someone do with it?
    
- Where can they find it?
    
- How can they get support?
    
- How can they contribute feedback?
    
- What remains experimental or limited?
    

---

# Pattern: Launch the Capability, Not Just the Artifact

Do not launch only:

> Version 1.0 is available.

Launch:

> Here is the coordination capability this standard makes possible, who can use it, and how to begin.

The standard itself is only part of the launch surface.

Include:

- stable specification;
    
- documentation;
    
- examples;
    
- validators or tooling;
    
- implementation guidance;
    
- migration guidance where needed;
    
- support channels;
    
- known limitations;
    
- contribution pathways.
    

---

# Pattern: Make the Stable Boundary Visible

Clearly distinguish:

- stable;
    
- experimental;
    
- deprecated;
    
- draft extensions;
    
- optional profiles.
    

Adopters should not have to infer which parts they can safely depend on.

---

# Pattern: Launch Is an Adoption Invitation

A successful launch should create identifiable next actions for different audiences.

For example:

**Implementers**

> Build against the specification.

**Existing infrastructure providers**

> Integrate or map to the standard.

**Governance communities**

> Test whether the standard represents your use cases.

**Researchers**

> Evaluate use and impact.

**Tool builders**

> Build validators, interfaces, visualizations, or adapters.

**Policy / institutional actors**

> Consider adoption or recognition.

---

# Pattern: Use Early-Adopter Evidence

Launch communication should privilege demonstrated experience over abstract claims.

Useful materials include:

- case studies;
    
- implementation stories;
    
- test results;
    
- before/after examples;
    
- interoperability demonstrations;
    
- lessons from early adopters.
    

The strongest launch story is:

> **Here is what someone was able to do that was previously difficult.**

---

# Pattern: Expand the Stakeholder Horizon

Launch exposes the standard to actors not visible during Scope.

Actively look for:

- downstream users;
    
- infrastructure providers;
    
- adjacent standards communities;
    
- institutional adopters;
    
- auditors;
    
- educators;
    
- policy communities;
    
- tool builders;
    
- critics;
    
- unintended users.
    

Feed them back into the ecosystem map.

---

# Launch Artifact

```yaml
release:
  version:
  stable_components:
  experimental_components:
  release_date:

audiences:
adoption_entry_points:
support_channels:
known_limitations:

launch_channels:
case_studies:
demonstrations:

feedback_paths:
review_triggers:
```
