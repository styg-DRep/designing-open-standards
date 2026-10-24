---
phase: scope
domain:
- ecosystem
- actors
role: supporting
status: draft
---

This node asks:

**Who must interact with governance systems, tools, procedures, interfaces, and institutions in order to participate?**

A “user” is broader than an end user of software. It includes anyone whose governance activity is mediated by infrastructure.

Infrastructure might include voting systems, wallets, governance portals, metadata standards, repositories, forums, APIs, identity systems, delegation systems, dashboards, constitutional processes, registries, proposal templates, meeting structures, and even recurring human workflows.

Useful groups to look for include voters, DReps, SPOs, Constitutional Committee members, proposers, treasury applicants, developers, delegates, reviewers, observers, researchers, community organizers, educators, journalists, auditors, ecosystem institutions, and people consuming governance records historically.

A useful discovery method is to trace **tasks**:

> What does someone have to do in order to participate in this governance activity?

Then ask which infrastructure mediates each step.

For example:

`understand proposal → discover it → read it → contextualize it → discuss it → evaluate it → vote`

Each transition may reveal different users and different infrastructure.

Another useful working pattern is:

**Actor → task → interface/infrastructure → dependency**

For example:

`DRep → evaluate proposal → governance portal + metadata → depends on discoverable, legible information`

`proposer → submit action → transaction tooling + schema → depends on valid formatting and wallet support`

#### Things to capture

For each user group, record:

- what they are trying to accomplish;
- what infrastructure they must use;
- whether use is mandatory or optional;
- what knowledge or access is required;
- where friction appears;
- what workarounds exist;
- whether the infrastructure behaves differently for different users;
- whether exclusion is technical, economic, linguistic, institutional, social, or informational.

Two especially useful questions are:

> **Who is expected to use this infrastructure but struggles to?**

and

> **Who is affected by the infrastructure without ever directly touching it?**

Those often reveal the most important design constraints for an open standard.
