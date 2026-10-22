#!/usr/bin/env python3
"""Build the machine- and agent-readable map of the framework.

Reads every note (frontmatter + intent) and every Obsidian canvas under
framework/, and writes:

  map/graph.json   nodes, typed edges, returns-to routes, artifact producers
  map/INDEX.md     the same, as a readable catalogue for people and agents

Usage:
  python tools/build_index.py           # regenerate map/
  python tools/build_index.py --check   # fail if map/ is stale or the vault has errors (CI)

Requires PyYAML (pip install pyyaml).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
VAULT = ROOT / "framework"
OUT = ROOT / "map"

PHASES = [
    ("scope", "Scope and Start"),
    ("develop", "Development"),
    ("launch", "Launch and Adoption"),
    ("review", "Review"),
]
ROLE_ORDER = ["entry-point", "orientation", "checkpoint", "supporting", "artifact"]
FEEDBACK = {"returns-to", "updates", "informs-and-updates"}

FM = re.compile(r"\A---\s*\n(.*?)\n---[ \t]*\n", re.S)


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def relation(label: str | None) -> str:
    label = (label or "").strip()
    return slug(label) if label else "connects"


def listify(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def intent_of(body: str) -> str:
    """First paragraph under '## Intent', else the first prose paragraph."""
    lines = body.splitlines()
    start = 0
    for i, line in enumerate(lines):
        if re.match(r"#+\s*Intent\b", line.strip()):
            start = i + 1
            break
    para = []
    for line in lines[start:]:
        s = line.strip()
        if not s:
            if para:
                break
            continue
        if s.startswith(("#", "```", "---", ">")) and not para:
            continue
        if s.startswith(("#", "```")):
            break
        para.append(s.lstrip("-* ").strip())
    text = " ".join(para)
    text = re.sub(r"\*\*|__", "", text)
    return (text[:237] + "...") if len(text) > 240 else text


def load_notes(errors: list[str]):
    notes = {}
    for path in sorted(VAULT.rglob("*.md")):
        if ".obsidian" in path.parts:
            continue
        rel = path.relative_to(VAULT).as_posix()
        raw = path.read_text(encoding="utf-8")
        meta, body = {}, raw
        m = FM.match(raw)
        if m:
            try:
                meta = yaml.safe_load(m.group(1)) or {}
            except yaml.YAMLError as exc:
                errors.append(f"{rel}: frontmatter does not parse ({exc.__class__.__name__})")
            body = raw[m.end():]
        else:
            errors.append(f"{rel}: no frontmatter (add phase/role/status)")
        nid = slug(path.stem)
        if nid in {n["id"] for n in notes.values()}:
            errors.append(f"{rel}: duplicate note id '{nid}' (rename the file)")
        notes[rel] = {
            "id": nid,
            "title": path.stem,
            "path": f"framework/{rel}",
            "phase": listify(meta.get("phase")),
            "role": meta.get("role", "unspecified"),
            "status": meta.get("status", "unspecified"),
            "gate": meta.get("gate"),
            "domain": listify(meta.get("domain")),
            "actors": listify(meta.get("actors")),
            "produces": listify(meta.get("produces")),
            "intent": intent_of(body),
            "empty_body": not body.strip(),
            "canvases": [],
            "groups": [],
        }
    return notes


def inside(n, g):
    return (g["x"] <= n["x"] and n["x"] + n["width"] <= g["x"] + g["width"]
            and g["y"] <= n["y"] and n["y"] + n["height"] <= g["y"] + g["height"])


def load_canvases(notes, errors: list[str]):
    edges, returns_to, placeholders, canvases = [], [], [], []
    for cpath in sorted(VAULT.rglob("*.canvas")):
        crel = cpath.relative_to(VAULT).as_posix()
        data = json.loads(cpath.read_text(encoding="utf-8"))
        nodes = {n["id"]: n for n in data.get("nodes", [])}
        groups = [n for n in nodes.values() if n["type"] == "group"]
        file_count = 0
        for n in nodes.values():
            if n["type"] == "file":
                if n["file"] not in notes:
                    if not (VAULT / n["file"]).exists():
                        errors.append(f"{crel}: links missing file '{n['file']}'")
                    continue
                file_count += 1
                note = notes[n["file"]]
                if f"framework/{crel}" not in note["canvases"]:
                    note["canvases"].append(f"framework/{crel}")
                for g in groups:
                    if g.get("label") and inside(n, g) and g["label"] not in note["groups"]:
                        note["groups"].append(g["label"])
        canvases.append({"path": f"framework/{crel}", "nodes": len(nodes), "notes": file_count,
                         "edges": len(data.get("edges", []))})
        if file_count == 0:
            continue  # pure text canvas (e.g. a reference explorer): no graph edges to extract

        def ref(nid):
            n = nodes.get(nid)
            if not n:
                return None
            if n["type"] == "file" and n["file"] in notes:
                return ("note", notes[n["file"]]["id"])
            if n["type"] == "text":
                return ("text", n["text"].strip())
            return None

        incoming = defaultdict(list)
        for e in data.get("edges", []):
            incoming[e["toNode"]].append(e)

        def file_sources(nid, seen=None):
            """Notes that reach this text node through text-only hops."""
            seen = seen or set()
            out = []
            for e in incoming[nid]:
                src = e["fromNode"]
                if src in seen:
                    continue
                seen.add(src)
                r = ref(src)
                if r and r[0] == "note":
                    out.append(r[1])
                elif r and r[0] == "text":
                    out += file_sources(src, seen)
            return out

        for e in data.get("edges", []):
            a, b = ref(e["fromNode"]), ref(e["toNode"])
            rel = relation(e.get("label"))
            if not a or not b:
                continue
            if a[0] == "note" and b[0] == "note":
                edges.append({"from": a[1], "to": b[1], "relation": rel,
                              "label": (e.get("label") or "").strip(), "canvas": f"framework/{crel}"})
            elif a[0] == "text" and b[0] == "note" and rel == "returns-to":
                for gate in file_sources(e["fromNode"]):
                    returns_to.append({"from": gate, "condition": a[1], "to": b[1]})
            elif a[0] == "note" and b[0] == "text" and not outgoing_any(data, e["toNode"]):
                placeholders.append({"from": a[1], "to_text": b[1], "relation": rel,
                                     "canvas": f"framework/{crel}"})
    # de-duplicate (notes can appear more than once on a canvas)
    edges = list({(e["from"], e["to"], e["relation"]): e for e in edges}.values())
    returns_to = list({(r["from"], r["to"], r["condition"]): r for r in returns_to}.values())
    return edges, returns_to, placeholders, canvases


def outgoing_any(data, nid):
    return any(e["fromNode"] == nid for e in data.get("edges", []))


def build():
    errors: list[str] = []
    notes = load_notes(errors)
    edges, returns_to, placeholders, canvases = load_canvases(notes, errors)
    nodes = sorted(notes.values(), key=lambda n: (ROLE_ORDER.index(n["role"]) if n["role"] in ROLE_ORDER
                                                  else len(ROLE_ORDER), n["title"].lower()))
    producers = defaultdict(list)
    for n in nodes:
        for p in n["produces"]:
            producers[str(p)].append(n["id"])
    warnings = []
    for n in nodes:
        if n["empty_body"]:
            warnings.append(f"{n['path']}: note has no body")
        if not n["canvases"]:
            warnings.append(f"{n['path']}: not placed on any canvas")
    ids = {n["id"] for n in nodes}
    crosswalk = ROOT / "toolkit" / "scope-gate-criteria.yaml"
    if crosswalk.exists():
        cw = yaml.safe_load(crosswalk.read_text(encoding="utf-8"))
        refs = [cw.get("gate_node")]
        seen_ids = set()
        for d in cw.get("domains", []):
            for c in d.get("criteria", []):
                if c["id"] in seen_ids:
                    errors.append(f"toolkit/scope-gate-criteria.yaml: duplicate criterion id {c['id']}")
                seen_ids.add(c["id"])
                refs += c.get("consult", []) + [c.get("returns_to")]
        for b in cw.get("bundle_components", []):
            refs += b.get("nodes", [])
            if not (ROOT / "toolkit" / "templates" / b["template"]).exists():
                errors.append(f"toolkit/scope-gate-criteria.yaml: missing template {b['template']}")
        refs += [f["source"] for f in cw.get("red_flags", [])]
        for r in sorted({r for r in refs if r} - ids):
            errors.append(f"toolkit/scope-gate-criteria.yaml: unknown node id '{r}'")
    unlabeled = sum(1 for e in edges if e["relation"] == "connects")
    if unlabeled:
        warnings.append(f"{unlabeled} canvas edges between notes have no label (indexed as 'connects')")
    phases_present = {p for n in nodes for p in n["phase"]}
    graph = {
        "generated_by": "tools/build_index.py",
        "phases": [{"key": k, "name": name,
                    "mapped": any(k in n["phase"] and n["gate"] == "phase" for n in nodes),
                    "referenced": k in phases_present} for k, name in PHASES],
        "nodes": [{k: v for k, v in n.items() if k != "empty_body"} for n in nodes],
        "edges": sorted(edges, key=lambda e: (e["from"], e["to"])),
        "returns_to": sorted(returns_to, key=lambda r: (r["from"], r["to"])),
        "placeholders": placeholders,
        "artifacts": dict(sorted(producers.items())),
        "canvases": canvases,
        "warnings": warnings,
    }
    return graph, errors


def link(n):
    return f"[{n['title']}](<../{n['path']}>)"


def render(graph) -> str:
    by_id = {n["id"]: n for n in graph["nodes"]}
    out_e, in_e = defaultdict(list), defaultdict(list)
    for e in graph["edges"]:
        out_e[e["from"]].append(e)
        in_e[e["to"]].append(e)
    L = []
    w = L.append
    w("<!-- GENERATED by tools/build_index.py from framework/. Do not edit by hand. -->")
    w("# Framework Map Index\n")
    w("Every note in the framework, what it is for, what it produces, and how it connects. "
      "Edges come from the Obsidian canvases; metadata comes from each note's frontmatter. "
      "Machine-readable twin: [`graph.json`](graph.json).\n")
    w("## Phases\n")
    w("| Phase | Key | Status |")
    w("|---|---|---|")
    for p in graph["phases"]:
        status = "mapped (phase gate present)" if p["mapped"] else (
            "referenced by notes, not yet mapped" if p["referenced"] else "not yet mapped")
        w(f"| {p['name']} | `{p['key']}` | {status} |")
    w("")
    gates = [n for n in graph["nodes"] if n.get("gate") == "phase"]
    for g in gates:
        w(f"### Phase gate: {link(g)}\n")
        routes = [r for r in graph["returns_to"] if r["from"] == g["id"]]
        if routes:
            w("When the gate is not passed, it **returns to**:\n")
            w("| Condition | Returns to |")
            w("|---|---|")
            for r in routes:
                w(f"| {r['condition']} | {link(by_id[r['to']])} |")
            w("")
        nxt = [p for p in graph["placeholders"] if p["from"] == g["id"]]
        for p in nxt:
            w(f"Next: **{p['to_text']}** (placeholder on the canvas; not yet mapped).\n")
    w("## Nodes\n")
    w("Roles: `entry-point` start here · `orientation` context · `checkpoint` has a gate condition and "
      "possible outcomes · `supporting` a lens or sub-inquiry feeding a checkpoint · `artifact` an output other nodes consume.\n")
    current = None
    for n in graph["nodes"]:
        if n["role"] != current:
            current = n["role"]
            w(f"### {current}\n")
        meta = [f"phase: {', '.join(n['phase']) or '—'}", f"status: {n['status']}"]
        if n.get("gate"):
            meta.append(f"gate: {n['gate']}")
        w(f"#### {link(n)}")
        w(f"`{n['id']}` · " + " · ".join(meta) + "\n")
        if n["intent"]:
            w(f"{n['intent']}\n")
        if n["produces"]:
            w("- **Produces:** " + ", ".join(f"`{p}`" for p in n["produces"]))
        if n["domain"]:
            w("- **Domains:** " + ", ".join(n["domain"]))
        if out_e[n["id"]]:
            w("- **Out:** " + "; ".join(f"{e['label'] or 'connects'} → {by_id[e['to']]['title']}"
                                        for e in out_e[n["id"]]))
        if in_e[n["id"]]:
            w("- **In:** " + "; ".join(f"{by_id[e['from']]['title']} ({e['label'] or 'connects'})"
                                       for e in in_e[n["id"]]))
        w("")
    w("## Artifacts → producing nodes\n")
    w("| Artifact | Produced by |")
    w("|---|---|")
    for art, ids in graph["artifacts"].items():
        w(f"| `{art}` | " + ", ".join(by_id[i]["title"] for i in ids) + " |")
    w("")
    w("## Canvases\n")
    for c in graph["canvases"]:
        w(f"- [{Path(c['path']).stem}](<../{c['path']}>) — {c['notes']} note links, {c['nodes']} nodes, {c['edges']} edges")
    w("")
    if graph["warnings"]:
        w("## Maintenance warnings\n")
        for x in graph["warnings"]:
            w(f"- {x}")
        w("")
    return "\n".join(L).rstrip() + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="fail if map/ is stale or the vault has errors")
    args = ap.parse_args()
    graph, errors = build()
    gj = json.dumps(graph, indent=2, ensure_ascii=False) + "\n"
    md = render(graph)
    if args.check:
        stale = [p for p, s in ((OUT / "graph.json", gj), (OUT / "INDEX.md", md))
                 if not p.exists() or p.read_text(encoding="utf-8") != s]
        for e in errors:
            print(f"ERROR {e}")
        for p in stale:
            print(f"STALE {p.relative_to(ROOT)} — run: python tools/build_index.py")
        for x in graph["warnings"]:
            print(f"warn  {x}")
        sys.exit(1 if errors or stale else 0)
    OUT.mkdir(exist_ok=True)
    (OUT / "graph.json").write_text(gj, encoding="utf-8")
    (OUT / "INDEX.md").write_text(md, encoding="utf-8")
    print(f"wrote map/ — {len(graph['nodes'])} nodes, {len(graph['edges'])} edges, "
          f"{len(graph['returns_to'])} returns-to routes")
    for e in errors:
        print(f"ERROR {e}")
    for x in graph["warnings"]:
        print(f"warn  {x}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
