# Roadmap

## The framework

| Phase | Status |
|---|---|
| 1. Scope and Start | Mapped (v0.5) |
| 2. Development | Mapped (v0.6) |
| 3. Launch and Adoption | Mapped (v0.6) |
| 4. Review and Update | Mapped (v0.6); lifecycle loop closed through Update or Retire's exits |

Development targets:

- **Lifecycle Decision Record** (stub) — cycle numbering, which baselines carry into the next cycle, cross-cycle comparison.
- **Update or Retire failure routes** — where the gate sends an effort when its nine criteria are not met.
- **Decompose Deciding Next Steps** — separate update, deprecation and retirement nodes, then route deprecate and retire.
- **Tidy the canvas** — move the *Returns-to routes* cards into their phase groups; label the unlabelled edges so agents can tell decomposition, family membership and sequence apart.
- A worked, clearly fictional example effort in `workspace/` to show what filled bundles and an audit look like.
- Replace references in the notes to "the attached" guides with links.

## Tooling

The playbooks already write structured, append-only records. The direction is tooling that uses them.

**Logging and tracking.** `workspace/<effort>/effort.yaml` holds the cycle and phase, node status, the baseline each gate produced, a dated log and dispositioned open questions. Next: a small command-line tool to validate a workspace against the templates, show progress across the map, and diff an effort against its Scope baseline ("changes are not failures; unrecorded changes are").

**Audit records → claim validity certificates.** An audit record already pins each finding to a stable criterion id, a framework version, specific sources with retrieval dates, an evidence tag, and named auditors with an independence statement. A certificate would be a signed, verifiable summary of such a record: *these claims about this standard were assessed against these criteria, on this evidence, by these people, on this date.* Open design questions:

- What exactly is certified — a claim, a domain, a gate outcome — and what is explicitly not.
- Who has standing to issue one, and how independence is shown.
- Expiry and revocation: certificates should lapse on the effort's review triggers, not live forever.
- Verifiability: content hashes of the record and its sources; whether and how to anchor them (for example as Cardano transaction metadata).
- The tension the framework itself names: *approval is a record, not a ceremony*. A certificate has to stay a record of evidence, not become a badge that substitutes for participation or review.
