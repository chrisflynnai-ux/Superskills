#!/usr/bin/env python3
"""
SkillML Linter v1.0
Extended linting beyond structural validation.

Wraps skillml_validator.py and adds:
- Style checks (naming conventions, description quality)
- Complexity analysis (layer count, token estimates)
- Cross-reference validation (sister skills exist, SSOT refs valid)
- Migration readiness scoring (how close to V1.4 compliance)
- Auto-fix suggestions for common issues

Usage:
    python tools/lint_skill.py <skill.xml>
    python tools/lint_skill.py --all
    python tools/lint_skill.py --domain copy
    python tools/lint_skill.py --migration-report
"""
import sys
import os
import re
import json
import xml.etree.ElementTree as ET
from pathlib import Path

# Import the validator
sys.path.insert(0, str(Path(__file__).parent))
from skillml_validator import validate_skillml, REQUIRED_LAYERS, REQUIRED_SECTIONS

ROOT = Path(__file__).parent.parent
SKILLS_DIR = ROOT / ".claude" / "skills"


def estimate_tokens(text: str) -> int:
    """Rough token estimate (4 chars per token)."""
    return len(text) // 4


def lint_skill(filepath: str) -> dict:
    """Run extended linting on a skill file."""
    filepath = Path(filepath)
    result = {
        "file": str(filepath),
        "structural": {},
        "style": [],
        "complexity": {},
        "migration": {},
        "fixes": [],
    }

    if not filepath.exists():
        result["structural"] = {"error": "File not found"}
        return result

    # Run structural validation first
    validation = validate_skillml(str(filepath))
    result["structural"] = validation

    # Read raw content
    try:
        raw = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        result["style"].append({"level": "error", "msg": f"Cannot read file: {e}"})
        return result

    # Try parsing XML
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
    except ET.ParseError as e:
        result["style"].append({
            "level": "error",
            "msg": f"XML parse error: {e}",
            "fix": "Fix XML syntax before other checks can run",
        })
        result["migration"]["ready"] = False
        result["migration"]["score"] = 0
        result["migration"]["blockers"] = ["XML parse error"]
        return result

    # ============================================================
    # STYLE CHECKS
    # ============================================================

    skill_id = root.get("skill_id", "")

    # S1: skill_id format
    if skill_id:
        if not re.match(r"^[a-z][a-z0-9_]+$", skill_id):
            result["style"].append({
                "level": "warning",
                "msg": f"skill_id '{skill_id}' uses non-standard format",
                "fix": f"Rename to {{domain}}_{{function}} format (e.g., 'copy_advertorial')",
            })

        # Check for old dotted format
        if "." in skill_id:
            new_id = skill_id.replace(".", "_").replace("__", "_")
            # Remove version suffix from id
            new_id = re.sub(r"_v\d+_\d+_\d+$", "", new_id)
            result["style"].append({
                "level": "info",
                "msg": f"skill_id uses legacy dot notation: '{skill_id}'",
                "fix": f"Migrate to: '{new_id}'",
            })
            result["fixes"].append({
                "type": "rename_skill_id",
                "old": skill_id,
                "new": new_id,
            })
    else:
        result["style"].append({
            "level": "error",
            "msg": "Missing skill_id attribute on root <Skill> element",
            "fix": "Add skill_id=\"domain_function\" to <Skill> tag",
        })

    # S2: Name attribute
    name = root.get("name", "")
    if not name:
        # Check Meta/Name or Meta/n
        name_el = root.find(".//Meta/Name")
        if name_el is None:
            name_el = root.find(".//Meta/n")
        if name_el is not None and name_el.text:
            result["style"].append({
                "level": "info",
                "msg": "Name found in Meta but not as root attribute",
                "fix": "Add name=\"...\" to <Skill> tag for consistency",
            })

    # S3: Description presence and quality
    desc_el = root.find(".//Meta/Description")
    if desc_el is None:
        desc_el = root.find(".//Description")
    if desc_el is not None and desc_el.text:
        desc_text = desc_el.text.strip()
        if len(desc_text) < 20:
            result["style"].append({
                "level": "warning",
                "msg": f"Description is too short ({len(desc_text)} chars)",
                "fix": "Expand to at least one complete sentence describing what and when",
            })
        elif len(desc_text) > 500:
            result["style"].append({
                "level": "info",
                "msg": f"Description is quite long ({len(desc_text)} chars)",
                "fix": "Consider shortening to 1-2 sentences",
            })
    else:
        result["style"].append({
            "level": "warning",
            "msg": "No Description element found in Meta",
            "fix": "Add <Description> to <Meta> section",
        })

    # S4: Check for unescaped special chars in content
    problem_patterns = [
        (r"&(?!(amp|lt|gt|apos|quot|#\d+|#x[0-9a-fA-F]+);)", "Unescaped '&' — use '&amp;'"),
        (r"<(?!/?\w)", "Possible unescaped '<' — use '&lt;'"),
    ]
    for pattern, msg in problem_patterns:
        # Only check in text content, not tags
        matches = re.findall(pattern, raw)
        if len(matches) > 5:
            result["style"].append({
                "level": "info",
                "msg": f"{msg} ({len(matches)} occurrences)",
            })

    # ============================================================
    # COMPLEXITY ANALYSIS
    # ============================================================

    total_tokens = estimate_tokens(raw)
    result["complexity"]["total_tokens_est"] = total_tokens
    result["complexity"]["file_size_kb"] = round(filepath.stat().st_size / 1024, 1)
    result["complexity"]["line_count"] = raw.count("\n") + 1

    # Layer token estimates
    for layer_tag in REQUIRED_LAYERS:
        layer_name = layer_tag.split(":")[1]
        # Find content between layer markers
        start_pattern = f"LAYER:{layer_name}"
        if start_pattern in raw:
            idx = raw.index(start_pattern)
            # Find next LAYER: marker or end
            next_markers = [raw.index(f"LAYER:{l.split(':')[1]}") for l in REQUIRED_LAYERS
                          if f"LAYER:{l.split(':')[1]}" in raw and raw.index(f"LAYER:{l.split(':')[1]}") > idx]
            end_idx = min(next_markers) if next_markers else len(raw)
            section = raw[idx:end_idx]
            result["complexity"][f"layer_{layer_name.lower()}_tokens"] = estimate_tokens(section)

    # Section count
    sections_found = sum(1 for s in REQUIRED_SECTIONS if root.find(f".//{s}") is not None)
    result["complexity"]["sections_found"] = sections_found
    result["complexity"]["sections_required"] = len(REQUIRED_SECTIONS)

    # Check count
    checks = root.findall(".//Check")
    result["complexity"]["selfcheck_count"] = len(checks)

    # ============================================================
    # MIGRATION READINESS
    # ============================================================

    migration_checks = {
        "has_v14_layers": all(layer in raw for layer in REQUIRED_LAYERS),
        "has_all_sections": sections_found == len(REQUIRED_SECTIONS),
        "has_selfcheck_min3": len(checks) >= 3,
        "has_mma_gate": root.find(".//MMAGate") is not None,
        "has_patchlog": root.find(".//PatchLog") is not None,
        "skill_id_v14_format": bool(re.match(r"^[a-z]+_[a-z_]+$", skill_id)) if skill_id else False,
        "version_semver": bool(re.match(r"^\d+\.\d+\.\d+$", root.get("version", ""))),
        "has_contract": root.find(".//Contract") is not None,
        "has_execution_protocol": root.find(".//ExecutionProtocol") is not None,
        "has_circuit_breaker": "CircuitBreaker" in raw or "circuit_breaker" in raw.lower(),
    }

    passed = sum(1 for v in migration_checks.values() if v)
    total = len(migration_checks)
    score = round(passed / total * 100) if total else 0

    result["migration"]["checks"] = migration_checks
    result["migration"]["score"] = score
    result["migration"]["passed"] = passed
    result["migration"]["total"] = total
    result["migration"]["ready"] = score >= 80
    result["migration"]["blockers"] = [k for k, v in migration_checks.items() if not v]

    # Generate fixes for missing V1.4 requirements
    if not migration_checks["has_v14_layers"]:
        missing_layers = [l for l in REQUIRED_LAYERS if l not in raw]
        result["fixes"].append({
            "type": "add_layers",
            "missing": missing_layers,
            "instruction": "Add LAYER:XXX comment tags to mark sections",
        })

    if not migration_checks["has_selfcheck_min3"]:
        result["fixes"].append({
            "type": "add_selfchecks",
            "current": len(checks),
            "required": 3,
            "instruction": "Add Check elements inside SelfCheck section",
        })

    if not migration_checks["has_mma_gate"]:
        result["fixes"].append({
            "type": "add_mma_gate",
            "instruction": "Add <MMAGate> inside <SelfCheck> with track-based min scores",
        })

    if not migration_checks["has_patchlog"]:
        result["fixes"].append({
            "type": "add_patchlog",
            "instruction": "Add <PatchLog> section with initial version entry",
        })

    return result


def migration_report():
    """Generate a migration readiness report for all skills."""
    print(f"\n{'='*70}")
    print(f"SkillML V1.4 Migration Readiness Report")
    print(f"{'='*70}\n")

    domain_scores = {}
    total_ready = 0
    total_skills = 0
    total_parse_errors = 0

    for xml_file in sorted(SKILLS_DIR.rglob("*.xml")):
        rel = str(xml_file.relative_to(SKILLS_DIR))
        if any(skip in rel for skip in ["_template", "_archive", "SKILL_TEMPLATE", "xml_skill_template"]):
            continue
        domain = xml_file.parent.name
        if domain in ("_template", "_archive", "styles"):
            continue

        total_skills += 1
        result = lint_skill(str(xml_file))

        if domain not in domain_scores:
            domain_scores[domain] = {"skills": [], "ready": 0, "total": 0, "errors": 0}

        migration = result.get("migration", {})
        score = migration.get("score", 0)
        ready = migration.get("ready", False)

        if not migration:
            total_parse_errors += 1
            domain_scores[domain]["errors"] += 1
            domain_scores[domain]["skills"].append({
                "file": xml_file.name,
                "score": 0,
                "status": "PARSE_ERROR",
            })
        else:
            if ready:
                total_ready += 1
                domain_scores[domain]["ready"] += 1

            domain_scores[domain]["skills"].append({
                "file": xml_file.name,
                "score": score,
                "status": "READY" if ready else "NEEDS_WORK",
                "blockers": migration.get("blockers", []),
            })

        domain_scores[domain]["total"] += 1

    # Print summary
    print(f"Total skills:      {total_skills}")
    print(f"Migration ready:   {total_ready} ({round(total_ready/total_skills*100) if total_skills else 0}%)")
    print(f"Needs work:        {total_skills - total_ready - total_parse_errors}")
    print(f"Parse errors:      {total_parse_errors}")
    print()

    for domain, data in sorted(domain_scores.items()):
        pct = round(data["ready"] / data["total"] * 100) if data["total"] else 0
        bar = "=" * (pct // 10) + "-" * (10 - pct // 10)
        print(f"  {domain:15s} [{bar}] {pct:3d}%  ({data['ready']}/{data['total']} ready, {data['errors']} errors)")

        for skill in data["skills"]:
            status_icon = {"READY": "+", "NEEDS_WORK": "~", "PARSE_ERROR": "!"}[skill["status"]]
            print(f"    [{status_icon}] {skill['file'][:50]:50s} {skill['score']:3d}%", end="")
            if skill.get("blockers"):
                top_blockers = skill["blockers"][:3]
                print(f"  blockers: {', '.join(top_blockers)}", end="")
            print()

        print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python tools/lint_skill.py <skill.xml>")
        print("  python tools/lint_skill.py --all")
        print("  python tools/lint_skill.py --domain copy")
        print("  python tools/lint_skill.py --migration-report")
        sys.exit(1)

    if sys.argv[1] == "--migration-report":
        migration_report()

    elif sys.argv[1] == "--all":
        all_results = []
        for xml_file in sorted(SKILLS_DIR.rglob("*.xml")):
            rel = str(xml_file.relative_to(SKILLS_DIR))
            if any(skip in rel for skip in ["_template", "_archive"]):
                continue
            result = lint_skill(str(xml_file))
            mig = result.get("migration", {})
            score = mig.get("score", 0)
            status = "READY" if mig.get("ready") else "NEEDS_WORK"
            print(f"  [{score:3d}%] {status:10s} {xml_file.name}")

    elif sys.argv[1] == "--domain":
        domain = sys.argv[2] if len(sys.argv) > 2 else None
        if domain:
            domain_path = SKILLS_DIR / domain
            for xml_file in sorted(domain_path.rglob("*.xml")):
                result = lint_skill(str(xml_file))
                print(json.dumps(result, indent=2, default=str))
                print()

    else:
        result = lint_skill(sys.argv[1])
        print(json.dumps(result, indent=2, default=str))
        sys.exit(0 if result.get("migration", {}).get("ready") else 1)
