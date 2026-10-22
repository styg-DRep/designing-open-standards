#!/usr/bin/env python3
"""Print an Obsidian canvas as readable text: groups, cards in reading order, and labelled edges.

Useful for text-only canvases (e.g. the Theory of Change explorer) that the map index does not expand.

Usage:
  python tools/canvas_text.py "framework/Theory of Change/Theory of change - Four principles of Change.canvas"
  python tools/canvas_text.py <canvas> --edges     # also list edges
"""
import json
import sys
from pathlib import Path


def label(n):
    if n["type"] == "file":
        return f"[note] {Path(n['file']).stem}"
    if n["type"] == "group":
        return f"[group] {n.get('label', '')}"
    if n["type"] == "link":
        return f"[link] {n.get('url', '')}"
    return " ".join(n.get("text", "").split())


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    nodes = {n["id"]: n for n in data.get("nodes", [])}
    groups = [n for n in nodes.values() if n["type"] == "group"]
    for g in groups:
        print(f"## group: {g.get('label', '(unlabelled)')}")
    print()
    # reading order: top-to-bottom bands, left-to-right within a band
    for n in sorted((n for n in nodes.values() if n["type"] != "group"),
                    key=lambda n: (round(n.get("y", 0) / 150), n.get("x", 0))):
        print(f"- {label(n)}")
    if "--edges" in sys.argv:
        print("\n## edges")
        for e in data.get("edges", []):
            a, b = nodes.get(e["fromNode"]), nodes.get(e["toNode"])
            if a and b:
                print(f"- {label(a)[:70]}  --{e.get('label', '') or ''}-->  {label(b)[:70]}")


if __name__ == "__main__":
    main()
