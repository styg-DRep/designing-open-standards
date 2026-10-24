#!/usr/bin/env python3
"""Re-root canvas file links so they resolve from the repository root.

The repository folder is the Obsidian vault, and Obsidian stores canvas links relative to the
vault root, so every link should start with framework/. A canvas edited in a vault rooted
somewhere else carries different leading folders and breaks. This rewrites each link to the one
note under framework/ whose path matches its tail (falling back to a unique filename match),
and reports anything it cannot resolve.

Usage:
  python tools/fix_canvas_paths.py            # fix all canvases in framework/
  python tools/fix_canvas_paths.py --dry-run  # report only
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canvas_format import obsidian_json  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
VAULT = ROOT / "framework"


def main():
    dry = "--dry-run" in sys.argv
    notes = [p.relative_to(ROOT).as_posix() for p in VAULT.rglob("*.md") if ".obsidian" not in p.parts]
    by_name = {}
    for n in notes:
        by_name.setdefault(Path(n).name, []).append(n)
    problems = 0
    for canvas in sorted(VAULT.rglob("*.canvas")):
        data = json.loads(canvas.read_text(encoding="utf-8"))
        changed = False
        for node in data.get("nodes", []):
            old = node.get("file")
            if node.get("type") != "file" or not old or old in notes:
                continue
            cands = [n for n in notes if old.endswith("/" + n)] or by_name.get(Path(old).name, [])
            if len(cands) == 1:
                print(f"{canvas.relative_to(VAULT)}: {old} -> {cands[0]}")
                node["file"] = cands[0]
                changed = True
            else:
                problems += 1
                print(f"{canvas.relative_to(VAULT)}: UNRESOLVED {old} (candidates: {cands or 'none'})")
        if changed and not dry:
            canvas.write_text(obsidian_json(data), encoding="utf-8")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
