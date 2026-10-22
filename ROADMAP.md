# Roadmap

## The framework

| Phase | Status |
|---|---|
| 1. Scope and Start | Mapped (v0.5) |
| 2. Development | Next. The Scope notes already carry hooks for it: phases or cycles, testing types and decision rights in *2- Plan the Development*; sustainability as a lifecycle concern; obligations created by crossing the gate. |
| 3. Launch and Adoption | Planned. Adoption sustainability, operational guidance for producers, engagement channels. |
| 4. Review | Planned. Loop topology still being worked out — Review returns to Theory of Change, to the Scope bundle as the first audit boundary, and to sustainability (adapt / simplify / transfer / retire). |

Smaller items:

- Label the 30 unlabelled canvas edges so agents can distinguish decomposition, family membership and sequence.
- A worked, clearly fictional example effort in `workspace/` to show what a filled bundle and an audit look like.
- Replace references in the notes to "the attached" guides with links.
- Confirm the source and license of the Theory of Change canvas (see ATTRIBUTION.md).

## Tooling

The playbooks already write structured, append-only records. The direction is tooling that uses them.

**Logging and tracking.** `workspace/<effort>/effort.yaml` holds node status, a dated log and dispositioned open questions. Next: a small command-line tool to validate a workspace against the templates, show progress across the map, and diff an effort against its Scope baseline ("changes are not failures; unrecorded changes are").

**Audit records → claim validity certificates.** An audit record already pins each finding to a stable criterion id, a framework version, specific sources with retrieval dates, an evidence tag, and named auditors with an independence statement. A certificate would be a signed, verifiable summary of such a record: *these claims about this standard were assessed against these criteria, on this evidence, by these people, on this date.* Open design questions:

- What exactly is certified — a claim, a domain, a gate outcome — and what is explicitly not.
- Who has standing to issue one, and how independence is shown.
- Expiry and revocation: certificates should lapse on the effort's review triggers, not live forever.
- Verifiability: content hashes of the record and its sources; whether and how to anchor them (for example as Cardano transaction metadata).
- The tension the framework itself names: *approval is a record, not a ceremony*. A certificate has to stay a record of evidence, not become a badge that substitutes for participation or review.
