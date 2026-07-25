#!/usr/bin/env python3
"""Verify that game metadata, the overview table, and the public site agree."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path.cwd()
ALLOWED_STATE = {"In development", "Ready to test", "Proven", "Shelved"}


def parse_frontmatter(path: Path) -> dict[str, object] | None:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match or not re.search(r"^record_type:\s*game\s*$", match.group(1), re.M):
        return None
    data: dict[str, object] = {"path": path}
    lines = match.group(1).splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if ":" not in line:
            index += 1
            continue
        key, raw = line.split(":", 1)
        raw = raw.strip()
        if not raw:
            values: list[int] = []
            following = index + 1
            while following < len(lines):
                item = re.fullmatch(r"\s+-\s+(-?\d+)\s*", lines[following])
                if not item:
                    break
                values.append(int(item.group(1)))
                following += 1
            if values:
                data[key] = values
                index = following
                continue
            data[key] = ""
        elif raw.startswith("[") and raw.endswith("]"):
            data[key] = [int(n.strip()) for n in raw[1:-1].split(",") if n.strip()]
        elif raw in {"true", "false"}:
            data[key] = raw == "true"
        elif re.fullmatch(r"-?\d+", raw):
            data[key] = int(raw)
        else:
            data[key] = raw.strip('"')
        index += 1
    return data


records: dict[str, dict[str, object]] = {}
for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
        continue
    record = parse_frontmatter(path)
    if not record:
        continue
    name = str(record.get("game", ""))
    if not name:
        print(f"ERROR: game record has no game name: {path}")
        sys.exit(1)
    if name in records:
        print(f"ERROR: duplicate game record: {name}")
        sys.exit(1)
    records[name] = record

errors: list[str] = []
for name, record in records.items():
    if record.get("state") not in ALLOWED_STATE:
        errors.append(f"{name}: invalid state {record.get('state')!r}")
    if not isinstance(record.get("players"), list) or not record["players"]:
        errors.append(f"{name}: missing exact players list")
    else:
        if record.get("min_players") != min(record["players"]):
            errors.append(f"{name}: min_players does not match exact players")
        if record.get("max_players") != max(record["players"]):
            errors.append(f"{name}: max_players does not match exact players")
    if record.get("complexity") not in {"Light", "Medium"}:
        errors.append(f"{name}: complexity must be Light or Medium")
    if not isinstance(record.get("physically_playtested"), bool):
        errors.append(f"{name}: physically_playtested must be true or false")
    elif record.get("state") == "Proven" and not record["physically_playtested"]:
        errors.append(f"{name}: Proven requires physically_playtested: true")
    if "status" in record or "table_tested" in record or "playtest_ready" in record:
        errors.append(f"{name}: retired field present (status / table_tested / playtest_ready)")
    minimum = record.get("min_minutes")
    maximum = record.get("max_minutes")
    if (minimum is None) != (maximum is None):
        errors.append(f"{name}: min_minutes and max_minutes must be supplied together")
    elif minimum is not None and (not isinstance(minimum, int) or not isinstance(maximum, int) or minimum > maximum):
        errors.append(f"{name}: invalid numeric duration bounds")
    document = record.get("public_document")
    if not isinstance(document, str) or not document:
        errors.append(f"{name}: missing public_document")
    elif not (ROOT / document).exists():
        errors.append(f"{name}: public_document does not exist: {document}")

index_html = (ROOT / "index.html").read_text(encoding="utf-8")
html = (ROOT / "games.html").read_text(encoding="utf-8")
displayed_counts: dict[str, int | None] = {
    "README.md": (int(match.group(1)) if (match := re.search(r"\*\*(\d+) games\*\*", (ROOT / "README.md").read_text(encoding="utf-8"))) else None),
    "COLLECTION_OVERVIEW.md": (int(match.group(1)) if (match := re.search(r"\*\*(\d+) games:\*\*", (ROOT / "COLLECTION_OVERVIEW.md").read_text(encoding="utf-8"))) else None),
    "index.html": (int(match.group(1)) if (match := re.search(r'<span class="n">(\d+)</span><span class="l">Games</span>', index_html)) else None),
}
for source, count in displayed_counts.items():
    if count is None:
        errors.append(f"{source}: displayed game total not found")
    elif count != len(records):
        errors.append(f"{source}: displays {count} games but {len(records)} records exist")

index_records: dict[str, tuple[str, list[int], bool, int, int, str, str, str]] = {}
for block in re.findall(r"  \{\n    id: .*?\n  \},?", html, re.S):
    name_match = re.search(r"name: '([^']+)'", block)
    supported_match = re.search(r"supported: \[([^]]+)\]", block)
    ready_match = re.search(r"played: (true|false)", block)
    status_match = re.search(r"state: '([^']+)'", block)
    document_match = re.search(r"rulebook: '([^']+)'", block)
    pmin_match = re.search(r"pmin: (\d+)", block)
    pmax_match = re.search(r"pmax: (\d+)", block)
    duration_match = re.search(r"timeLabel: '([^']+)'", block)
    weight_match = re.search(r"weight: '([^']+)'", block)
    if not all((name_match, supported_match, ready_match, status_match, document_match, pmin_match, pmax_match, duration_match, weight_match)):
        continue
    supported = [int(n.strip()) for n in supported_match.group(1).split(",")]
    index_records[name_match.group(1)] = (
        status_match.group(1),
        supported,
        ready_match.group(1) == "true",
        int(pmin_match.group(1)),
        int(pmax_match.group(1)),
        duration_match.group(1),
        weight_match.group(1),
        document_match.group(1),
    )
    if not (ROOT / document_match.group(1)).exists():
        errors.append(f"{name_match.group(1)}: games.html document does not exist: {document_match.group(1)}")

for name in sorted(records.keys() | index_records.keys()):
    if name not in records:
        errors.append(f"{name}: in games.html but has no main game record")
        continue
    if name not in index_records:
        errors.append(f"{name}: main game record is missing from games.html")
        continue
    actual = records[name]
    expected = (
        actual["state"],
        actual["players"],
        actual["physically_playtested"],
        actual["min_players"],
        actual["max_players"],
        actual["duration"],
        actual["complexity"],
        actual["public_document"],
    )
    if index_records[name] != expected:
        errors.append(f"{name}: index {index_records[name]!r} != main record {expected!r}")

overview = (ROOT / "COLLECTION_OVERVIEW.md").read_text(encoding="utf-8")
table_match = re.search(r"## Complete catalogue\n(.*?)(?:\n---\n)", overview, re.S)
overview_records: dict[str, tuple[str, bool]] = {}
if not table_match:
    errors.append("COLLECTION_OVERVIEW.md: complete catalogue table not found")
else:
    for name, state, played in re.findall(
        r"^\| \[([^]]+)\]\([^)]+\) \| \*\*([^*]+)\*\* \| [^|]* \| [^|]* \| (Yes|No) \|",
        table_match.group(1),
        re.M,
    ):
        overview_records[name] = (state, played == "Yes")

for name in sorted(records.keys() | overview_records.keys()):
    if name not in records:
        errors.append(f"{name}: in overview table but has no main game record")
    elif name not in overview_records:
        errors.append(f"{name}: missing from overview complete catalogue")
    else:
        overview_state, overview_played = overview_records[name]
        if overview_state != records[name]["state"]:
            errors.append(f"{name}: overview state {overview_state!r} != {records[name]['state']!r}")
        if overview_played != records[name]["physically_playtested"]:
            errors.append(
                f"{name}: overview physically played {overview_played!r} "
                f"!= {records[name]['physically_playtested']!r}"
            )

state_counts = Counter(str(record["state"]) for record in records.values())
headline = re.search(r"\*\*\d+ games:\*\*(.*?)\n", overview)
if not headline:
    errors.append("COLLECTION_OVERVIEW.md: state-count headline not found")
else:
    displayed_state_counts = {
        state: int(count)
        for count, state in re.findall(
            r"(\d+) (In development|Ready to test|Proven|Shelved)",
            headline.group(1),
        )
    }
    if displayed_state_counts != dict(state_counts):
        errors.append(
            "COLLECTION_OVERVIEW.md: displayed state counts "
            f"{displayed_state_counts!r} != record counts {dict(state_counts)!r}"
        )

played_records = {
    name for name, record in records.items() if record["physically_playtested"]
}
played_headline = re.search(
    r"\*\*(\d+) have been physically played:\*\*\s*([^\n]+)",
    overview,
)
if not played_headline:
    errors.append("COLLECTION_OVERVIEW.md: physically-played headline not found")
else:
    displayed_played_count = int(played_headline.group(1))
    displayed_played_names = {
        name.strip().rstrip(".") for name in played_headline.group(2).split(",")
    }
    if displayed_played_count != len(played_records):
        errors.append(
            "COLLECTION_OVERVIEW.md: displayed physically-played count "
            f"{displayed_played_count} != {len(played_records)}"
        )
    if displayed_played_names != played_records:
        errors.append(
            "COLLECTION_OVERVIEW.md: physically-played names "
            f"{sorted(displayed_played_names)!r} != {sorted(played_records)!r}"
        )

if not records:
    errors.append("no game records found")

if errors:
    for error in errors:
        print(f"ERROR: {error}")
    print(f"\nFAIL: {len(errors)} catalogue mismatch(es).")
    sys.exit(1)

print(f"OK: {len(records)} game records match COLLECTION_OVERVIEW.md and games.html.")
