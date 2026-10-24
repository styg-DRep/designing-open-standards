"""Write canvas JSON the way Obsidian does, so tool edits and Obsidian saves don't produce noisy diffs."""
import json


def obsidian_json(data: dict) -> str:
    parts = []
    for key, value in data.items():
        if isinstance(value, list) and value:
            body = ",\n".join("\t\t" + json.dumps(x, ensure_ascii=False, separators=(",", ":")) for x in value)
            parts.append(f'\t"{key}":[\n{body}\n\t]')
        else:
            parts.append(f'\t"{key}":' + json.dumps(value, ensure_ascii=False, separators=(",", ":")))
    return "{\n" + ",\n".join(parts) + "\n}"
