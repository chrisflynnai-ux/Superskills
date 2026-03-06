#!/usr/bin/env python3
"""
Manifest Builder v1.0
Scans .claude/skills/ and generates SKILLS_MANIFEST.yaml
with validation status from SkillML validator.

Per REFACTOR PLAN v1.4:
- Auto-discovers all .xml skills
- Validates each against SkillML rules
- Generates manifest with domain grouping + health status
- Outputs to .claude/SKILLS_MANIFEST.yaml

Usage:
    python tools/manifest_builder.py
    python tools/manifest_builder.py --output custom_path.yaml
    python tools/manifest_builder.py --json
"""
import sys
import os
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

# Import the validator
sys.path.insert(0, str(Path(__file__).parent))
from skillml_validator import validate_skillml

ROOT = Path(__file__).parent.parent
SKILLS_DIR = ROOT / ".claude" / "skills"
DEFAULT_OUTPUT = ROOT / ".claude" / "SKILLS_MANIFEST.yaml"


def extract_skill_meta(filepath: Path) -> dict:
    """Extract metadata from a skill XML file."""
    meta = {
        "file": filepath.name,
        "domain": filepath.parent.name,
        "path": str(filepath.relative_to(ROOT)),
    }

    try:
        raw = filepath.read_text(encoding="utf-8", errors="replace")
        tree = ET.parse(filepath)
        root = tree.getroot()

        # Root attributes
        meta["skill_id"] = root.get("skill_id", "")
        meta["name"] = root.get("name", "")
        meta["version"] = root.get("version", "")
        meta["status"] = root.get("status", "")
        meta["tier"] = root.get("tier", "")
        meta["model"] = root.get("model", "")

        # Try to get name from Meta section if not in root
        if not meta["name"]:
            name_el = root.find(".//Meta/Name")
            if name_el is None:
                name_el = root.find(".//Meta/n")
            if name_el is not None and name_el.text:
                meta["name"] = name_el.text.strip()

        # Try to get description
        desc_el = root.find(".//Meta/Description")
        if desc_el is None:
            desc_el = root.find(".//Description")
        if desc_el is not None and desc_el.text:
            meta["description"] = desc_el.text.strip()[:200]
        else:
            meta["description"] = ""

        # Count layers
        layer_count = sum(1 for layer in ["LAYER:CONTRACT", "LAYER:RULES", "LAYER:REASONING", "LAYER:IMPL"]
                         if layer in raw)
        meta["layers"] = layer_count

        # Count checks
        checks = root.findall(".//Check")
        meta["selfcheck_count"] = len(checks)

        # Has MMAGate?
        meta["has_mma_gate"] = root.find(".//MMAGate") is not None

        # Has PatchLog?
        meta["has_patchlog"] = root.find(".//PatchLog") is not None

        # File size
        meta["size_kb"] = round(filepath.stat().st_size / 1024, 1)

    except ET.ParseError as e:
        meta["parse_error"] = str(e)
        meta["skill_id"] = ""
        meta["name"] = filepath.stem
        meta["version"] = ""
        meta["status"] = "parse_error"

    return meta


def build_manifest() -> dict:
    """Build the full skills manifest."""
    manifest = {
        "version": "3.0.0",
        "generated": datetime.now().isoformat(),
        "generator": "manifest_builder v1.0",
        "skills_dir": str(SKILLS_DIR.relative_to(ROOT)),
        "domains": {},
        "summary": {
            "total": 0,
            "healthy": 0,
            "parse_errors": 0,
            "validation_failures": 0,
            "domains": 0,
        }
    }

    # Scan all XML files
    for xml_file in sorted(SKILLS_DIR.rglob("*.xml")):
        # Skip templates, archives, and non-skill files
        rel = str(xml_file.relative_to(SKILLS_DIR))
        if any(skip in rel for skip in ["_template", "_archive", "SKILL_TEMPLATE", "xml_skill_template"]):
            continue

        domain = xml_file.parent.name
        if domain in ("_template", "_archive", "styles"):
            continue

        # Extract metadata
        meta = extract_skill_meta(xml_file)

        # Run validation
        validation = validate_skillml(str(xml_file))
        meta["validation"] = {
            "passed": validation["passed"],
            "score": validation.get("score", "0/0"),
        }

        if "parse_error" in meta:
            meta["health"] = "ERROR"
            manifest["summary"]["parse_errors"] += 1
        elif validation["passed"]:
            meta["health"] = "HEALTHY"
            manifest["summary"]["healthy"] += 1
        else:
            meta["health"] = "NEEDS_FIX"
            meta["validation"]["failed_checks"] = [
                k for k, v in validation.get("checks", {}).items()
                if isinstance(v, bool) and not v
            ]
            manifest["summary"]["validation_failures"] += 1

        # Add to domain group
        if domain not in manifest["domains"]:
            manifest["domains"][domain] = {
                "skills": [],
                "count": 0,
                "healthy": 0,
            }

        manifest["domains"][domain]["skills"].append(meta)
        manifest["domains"][domain]["count"] += 1
        if meta["health"] == "HEALTHY":
            manifest["domains"][domain]["healthy"] += 1

        manifest["summary"]["total"] += 1

    manifest["summary"]["domains"] = len(manifest["domains"])
    return manifest


def to_yaml_string(manifest: dict) -> str:
    """Convert manifest dict to YAML string (without PyYAML dependency)."""
    lines = []
    lines.append("# SUPERMIND Skills Manifest")
    lines.append(f"# Generated: {manifest['generated']}")
    lines.append(f"# Generator: {manifest['generator']}")
    lines.append("")
    lines.append(f"version: \"{manifest['version']}\"")
    lines.append(f"generated: \"{manifest['generated']}\"")
    lines.append(f"skills_dir: \"{manifest['skills_dir']}\"")
    lines.append("")

    # Summary
    s = manifest["summary"]
    lines.append("summary:")
    lines.append(f"  total: {s['total']}")
    lines.append(f"  healthy: {s['healthy']}")
    lines.append(f"  parse_errors: {s['parse_errors']}")
    lines.append(f"  validation_failures: {s['validation_failures']}")
    lines.append(f"  domains: {s['domains']}")
    lines.append("")

    # Domains
    lines.append("domains:")
    for domain_name, domain_data in sorted(manifest["domains"].items()):
        lines.append(f"  {domain_name}:")
        lines.append(f"    count: {domain_data['count']}")
        lines.append(f"    healthy: {domain_data['healthy']}")
        lines.append(f"    skills:")

        for skill in domain_data["skills"]:
            lines.append(f"      - skill_id: \"{skill.get('skill_id', '')}\"")
            lines.append(f"        name: \"{skill.get('name', '')}\"")
            lines.append(f"        file: \"{skill.get('file', '')}\"")
            lines.append(f"        version: \"{skill.get('version', '')}\"")
            lines.append(f"        status: \"{skill.get('status', '')}\"")
            lines.append(f"        health: \"{skill['health']}\"")
            lines.append(f"        size_kb: {skill.get('size_kb', 0)}")

            if skill.get("description"):
                desc = skill["description"].replace('"', '\\"')[:120]
                lines.append(f"        description: \"{desc}\"")

            if skill.get("layers"):
                lines.append(f"        layers: {skill['layers']}")
            if skill.get("selfcheck_count"):
                lines.append(f"        selfcheck_count: {skill['selfcheck_count']}")

            val = skill.get("validation", {})
            lines.append(f"        validation_score: \"{val.get('score', '?')}\"")

            if val.get("failed_checks"):
                lines.append(f"        failed_checks:")
                for fc in val["failed_checks"]:
                    lines.append(f"          - \"{fc}\"")

            if skill.get("parse_error"):
                err = skill["parse_error"].replace('"', '\\"')[:100]
                lines.append(f"        parse_error: \"{err}\"")

            lines.append("")

    return "\n".join(lines)


def print_summary(manifest: dict):
    """Print a human-readable summary."""
    s = manifest["summary"]
    print(f"\n{'='*60}")
    print(f"SUPERMIND Skills Manifest — Build Report")
    print(f"{'='*60}")
    print(f"Total skills:          {s['total']}")
    print(f"  HEALTHY:             {s['healthy']}")
    print(f"  NEEDS_FIX:           {s['validation_failures']}")
    print(f"  PARSE_ERROR:         {s['parse_errors']}")
    print(f"Domains:               {s['domains']}")
    print()

    for domain, data in sorted(manifest["domains"].items()):
        health_pct = round(data["healthy"] / data["count"] * 100) if data["count"] else 0
        bar = "█" * (health_pct // 10) + "░" * (10 - health_pct // 10)
        print(f"  {domain:15s} {data['healthy']:2d}/{data['count']:2d} {bar} {health_pct}%")

    print()


if __name__ == "__main__":
    output_path = DEFAULT_OUTPUT
    output_json = False

    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_path = Path(sys.argv[idx + 1])

    if "--json" in sys.argv:
        output_json = True

    # Build manifest
    manifest = build_manifest()

    if output_json:
        print(json.dumps(manifest, indent=2, default=str))
    else:
        # Write YAML
        yaml_content = to_yaml_string(manifest)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(yaml_content, encoding="utf-8")
        print(f"Manifest written to: {output_path}")
        print_summary(manifest)
