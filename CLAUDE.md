# CLAUDE.md

@AGENTS.md

## Claude Code specifics

- The four playbooks in `AGENTS.md` are project skills in `.claude/skills/` and load automatically. Users can invoke them directly: `/navigate-framework`, `/guide-standard`, `/audit-standard`, `/extend-framework`. Prefer the matching skill over improvising a process.
- On a first open with no clear request, give a three-line orientation (what Scope and Start is for, guide vs audit vs explore) and ask which they want.
- For long guided sessions, keep `workspace/<slug>/effort.yaml` current after each node so the work survives a new session; on resume, read it first.
- When a user edits notes in Obsidian while you work, re-read the note before quoting it.
- After changing anything in `framework/` or `toolkit/`, run `python tools/build_index.py` and include the regenerated `map/` in the same commit.
