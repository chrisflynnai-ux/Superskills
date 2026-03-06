#!/usr/bin/env python3
"""
Alias Resolver v1.0
Resolves legacy skill filenames, slash commands, and nicknames
to canonical skill_ids per REFACTOR PLAN v1.4.

Reads from: orchestration/routing/aliases.yaml
Returns:     canonical skill_id + file path

Usage:
    python tools/alias_resolver.py /advertorial
    python tools/alias_resolver.py advertorial_copy_master_v2.0.0
    python tools/alias_resolver.py copy_advertorial
    python tools/alias_resolver.py --list
    python tools/alias_resolver.py --validate
"""
import sys
import os
import json
from pathlib import Path

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


ROOT = Path(__file__).parent.parent
ALIASES_PATH = ROOT / "orchestration" / "routing" / "aliases.yaml"
SKILLS_DIR = ROOT / ".claude" / "skills"


def load_aliases() -> dict:
    """Load the aliases.yaml file."""
    if not ALIASES_PATH.exists():
        print(f"ERROR: aliases.yaml not found at {ALIASES_PATH}")
        sys.exit(1)

    if HAS_YAML:
        with open(ALIASES_PATH, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    else:
        # Fallback: simple YAML parser for flat structure
        data = _parse_simple_yaml(ALIASES_PATH)

    return data


def _parse_simple_yaml(filepath: Path) -> dict:
    """Minimal YAML parser for aliases.yaml structure."""
    data = {"skills": []}
    current_skill = None
    current_key = None
    in_aliases = False

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue

            # Top-level list item under skills:
            if stripped.startswith("- skill_id:"):
                if current_skill:
                    data["skills"].append(current_skill)
                current_skill = {"skill_id": stripped.split(":", 1)[1].strip().strip('"')}
                in_aliases = False
                continue

            if current_skill is None:
                continue

            if stripped.startswith("domain:"):
                current_skill["domain"] = stripped.split(":", 1)[1].strip().strip('"')
            elif stripped.startswith("file:"):
                current_skill["file"] = stripped.split(":", 1)[1].strip().strip('"')
            elif stripped.startswith("command:"):
                current_skill["command"] = stripped.split(":", 1)[1].strip().strip('"')
            elif stripped.startswith("aliases:"):
                current_skill["aliases"] = []
                in_aliases = True
            elif in_aliases and stripped.startswith("- "):
                alias_val = stripped[2:].strip().strip('"')
                current_skill.setdefault("aliases", []).append(alias_val)
            else:
                in_aliases = False

    if current_skill:
        data["skills"].append(current_skill)

    return data


def build_lookup(data: dict) -> dict:
    """Build a reverse lookup from any alias/command/filename → skill entry."""
    lookup = {}
    skills = data.get("skills", [])

    for skill in skills:
        skill_id = skill.get("skill_id", "")
        entry = {
            "skill_id": skill_id,
            "domain": skill.get("domain", ""),
            "file": skill.get("file", ""),
            "command": skill.get("command", ""),
        }

        # Map canonical skill_id
        lookup[skill_id] = entry

        # Map command (with and without slash)
        cmd = skill.get("command", "")
        if cmd:
            lookup[cmd] = entry
            lookup[cmd.lstrip("/")] = entry

        # Map filename (with and without extension)
        filename = skill.get("file", "")
        if filename:
            lookup[filename] = entry
            stem = Path(filename).stem
            lookup[stem] = entry
            # Also without version suffix
            parts = stem.rsplit("_v", 1)
            if len(parts) == 2:
                lookup[parts[0]] = entry

        # Map all aliases
        for alias in skill.get("aliases", []):
            lookup[alias] = entry
            lookup[alias.lstrip("/")] = entry

    return lookup


def resolve(query: str) -> dict:
    """Resolve a query to canonical skill entry."""
    data = load_aliases()
    lookup = build_lookup(data)

    # Normalize query
    normalized = query.strip().lower()

    # Try exact match first
    if normalized in lookup:
        return lookup[normalized]

    # Try case-insensitive
    lower_lookup = {k.lower(): v for k, v in lookup.items()}
    if normalized in lower_lookup:
        return lower_lookup[normalized]

    # Try partial match
    matches = [v for k, v in lower_lookup.items() if normalized in k]
    if len(matches) == 1:
        return matches[0]
    elif len(matches) > 1:
        # Deduplicate by skill_id
        seen = set()
        unique = []
        for m in matches:
            if m["skill_id"] not in seen:
                seen.add(m["skill_id"])
                unique.append(m)
        if len(unique) == 1:
            return unique[0]
        return {"error": "ambiguous", "matches": unique}

    return {"error": "not_found", "query": query}


def find_skill_file(entry: dict) -> str:
    """Find the actual file path for a resolved skill entry."""
    if "error" in entry:
        return None

    domain = entry.get("domain", "")
    filename = entry.get("file", "")

    if domain and filename:
        path = SKILLS_DIR / domain / filename
        if path.exists():
            return str(path)

    # Fallback: search all domains
    if filename:
        for xml_file in SKILLS_DIR.rglob(filename):
            return str(xml_file)

    return None


def list_all():
    """List all registered skills and their aliases."""
    data = load_aliases()
    skills = data.get("skills", [])

    print(f"\n{'='*70}")
    print(f"Registered Skills ({len(skills)} total)")
    print(f"{'='*70}\n")

    for skill in sorted(skills, key=lambda s: s.get("domain", "") + s.get("skill_id", "")):
        sid = skill.get("skill_id", "?")
        domain = skill.get("domain", "?")
        cmd = skill.get("command", "-")
        aliases = skill.get("aliases", [])
        filename = skill.get("file", "?")

        print(f"  [{domain}] {sid}")
        print(f"    file:    {filename}")
        print(f"    command: {cmd}")
        if aliases:
            print(f"    aliases: {', '.join(aliases)}")
        print()


def validate_aliases():
    """Validate that all alias entries point to existing files."""
    data = load_aliases()
    skills = data.get("skills", [])
    errors = []
    warnings = []

    for skill in skills:
        sid = skill.get("skill_id", "MISSING")
        domain = skill.get("domain", "")
        filename = skill.get("file", "")

        # Check file exists
        if filename and domain:
            path = SKILLS_DIR / domain / filename
            if not path.exists():
                errors.append(f"  [MISSING FILE] {sid} → {domain}/{filename}")

        # Check skill_id convention
        if not sid or "_" not in sid:
            warnings.append(f"  [BAD ID] {sid} — should be {{domain}}_{{function}}")

    print(f"\nAlias Validation Report")
    print(f"{'='*50}")
    print(f"Total skills: {len(skills)}")
    print(f"Errors:       {len(errors)}")
    print(f"Warnings:     {len(warnings)}")

    if errors:
        print(f"\nERRORS:")
        for e in errors:
            print(e)

    if warnings:
        print(f"\nWARNINGS:")
        for w in warnings:
            print(w)

    if not errors and not warnings:
        print("\n  All aliases valid!")

    return len(errors) == 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python tools/alias_resolver.py <query>")
        print("  python tools/alias_resolver.py --list")
        print("  python tools/alias_resolver.py --validate")
        sys.exit(1)

    if sys.argv[1] == "--list":
        list_all()
    elif sys.argv[1] == "--validate":
        valid = validate_aliases()
        sys.exit(0 if valid else 1)
    else:
        query = sys.argv[1]
        result = resolve(query)

        if "error" in result:
            print(json.dumps(result, indent=2))
            sys.exit(1)
        else:
            filepath = find_skill_file(result)
            result["resolved_path"] = filepath or "NOT_FOUND"
            print(json.dumps(result, indent=2))
            sys.exit(0)
