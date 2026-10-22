# Contributing

This repository applies its own framework to itself where it can.

## Ways to contribute

- **Use it and report back.** The most valuable contribution is evidence: where the map helped, where a node's questions did not fit a real effort, where a gate was too heavy or too light. Open an issue describing the effort (as much as you can share), the node, and what happened.
- **Propose changes to the framework.** Open an issue first for anything beyond a typo, so the change can be discussed before it is drafted. Then a pull request.
- **Improve the playbooks or tools.** Pull requests welcome.

## Making a change

1. Edit notes and canvases in `framework/` (Obsidian is easiest). Follow the conventions in `.claude/skills/extend-framework/SKILL.md` — an agent can apply them for you.
2. If the Scope and Start gate criteria change, update `toolkit/scope-gate-criteria.yaml` (never renumber ids).
3. Run `python tools/build_index.py` and commit the regenerated `map/` with your change.
4. Add a line to `CHANGELOG.md`, including any note renames (old → new id).

CI runs `python tools/build_index.py --check` on every push and pull request.

## Contribution and decision

Anyone can propose. For now the repository is at the *named steward* stage of the progression described in *Governance Sustainability*: the maintainer decides what is merged, records the reason on the pull request or issue, and keeps objections visible. As contributors and adopters grow, that should move toward a small maintainer group and an open change process.

## Licensing of contributions

By contributing you agree that your contribution is licensed under the repository's licenses: CC BY-SA 4.0 for framework content, documentation, templates and playbooks; MIT for code in `tools/`. Contributors are credited in the git history; substantial contributions can be named in `ATTRIBUTION.md`.
