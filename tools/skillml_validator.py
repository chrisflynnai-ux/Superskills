#!/usr/bin/env python3
"""
SkillML Validator v1.0
Validates SUPERMIND skills against SkillML relaxed XML dialect.

Rules (from REFACTOR PLAN v1.4):
- Well-formed XML required
- Root element must be <Skill> with skill_id, version, status attributes
- Required sections: Meta, Contract, ExecutionProtocol, SelfCheck, PatchLog
- 4 LAYER tags required: CONTRACT, RULES, REASONING, IMPL
- SelfCheck must have >= 3 Check elements + MMAGate
- Content is free-form (no content-level schema enforcement)
- Version must be semver, skill_id must be {domain}_{function}

Usage:
    python tools/skillml_validator.py <skill.xml>
    python tools/skillml_validator.py --all
    python tools/skillml_validator.py --domain copy
"""
import sys
import re
import os
import json
import xml.etree.ElementTree as ET
from pathlib import Path


SKILLS_DIR = Path(__file__).parent.parent / ".claude" / "skills"

REQUIRED_LAYERS = ["LAYER:CONTRACT", "LAYER:RULES", "LAYER:REASONING", "LAYER:IMPL"]

REQUIRED_SECTIONS = ["Meta", "Contract", "ExecutionProtocol", "SelfCheck", "PatchLog"]


def validate_skillml(filepath: str) -> dict:
    """Validate a single skill file against SkillML rules."""
    filepath = Path(filepath)
    checks = {}
    raw_text = ""

    # Check 1: File exists
    if not filepath.exists():
        return {"passed": False, "file": str(filepath), "checks": {"file_exists": False}}

    # Check 2: Well-formed XML
    try:
        raw_text = filepath.read_text(encoding="utf-8", errors="replace")
        tree = ET.parse(filepath)
        root = tree.getroot()
        checks["well_formed_xml"] = True
    except ET.ParseError as e:
        checks["well_formed_xml"] = False
        checks["parse_error"] = str(e)
        # Can't continue without valid XML
        passed_count = sum(1 for v in checks.values() if v is True)
        total = len([v for v in checks.values() if isinstance(v, bool)])
        return {
            "passed": False,
            "file": str(filepath),
            "score": f"{passed_count}/{total}",
            "checks": checks
        }

    # Check 3: Root is <Skill>
    checks["root_is_skill"] = root.tag == "Skill"

    # Check 4: skill_id attribute
    skill_id = root.get("skill_id", "")
    checks["has_skill_id"] = bool(skill_id)
    checks["skill_id_convention"] = bool(re.match(r"^[a-z]+_[a-z_]+$", skill_id)) if skill_id else False

    # Check 5: version attribute (semver)
    version = root.get("version", "")
    checks["has_version"] = bool(version)
    checks["version_semver"] = bool(re.match(r"^\d+\.\d+\.\d+$", version)) if version else False

    # Check 6: status attribute
    checks["has_status"] = root.get("status") is not None

    # Check 7: Required sections
    for section in REQUIRED_SECTIONS:
        found = root.find(f".//{section}") is not None
        checks[f"has_{section.lower()}"] = found

    # Check 8: SelfCheck minimum (3 checks)
    selfcheck_checks = root.findall(".//Check")
    checks["selfcheck_min_3"] = len(selfcheck_checks) >= 3
    checks["selfcheck_count"] = len(selfcheck_checks)

    # Check 9: MMAGate present
    checks["has_mma_gate"] = root.find(".//MMAGate") is not None

    # Check 10: Layer tags (4 required)
    for layer in REQUIRED_LAYERS:
        checks[f"layer_{layer.split(':')[1].lower()}"] = layer in raw_text

    layer_count = sum(1 for l in REQUIRED_LAYERS if l in raw_text)
    checks["all_4_layers"] = layer_count == 4

    # Check 11: PatchLog present
    checks["has_patchlog"] = root.find(".//PatchLog") is not None

    # Calculate results
    bool_checks = {k: v for k, v in checks.items() if isinstance(v, bool)}
    passed_count = sum(1 for v in bool_checks.values() if v)
    total = len(bool_checks)
    all_passed = all(bool_checks.values())

    return {
        "passed": all_passed,
        "file": str(filepath),
        "score": f"{passed_count}/{total}",
        "skill_id": skill_id or "MISSING",
        "version": version or "MISSING",
        "checks": checks
    }


def validate_directory(domain: str = None):
    """Validate all skills or skills in a specific domain."""
    search_path = SKILLS_DIR / domain if domain else SKILLS_DIR
    results = {"passed": [], "failed": [], "errors": []}

    for xml_file in sorted(search_path.rglob("*.xml")):
        if "_template" in str(xml_file) or "_archive" in str(xml_file):
            continue
        result = validate_skillml(str(xml_file))
        if result["passed"]:
            results["passed"].append(result)
        elif "parse_error" in result.get("checks", {}):
            results["errors"].append(result)
        else:
            results["failed"].append(result)

    return results


def print_results(results: dict):
    """Print validation results in a readable format."""
    total = len(results["passed"]) + len(results["failed"]) + len(results["errors"])

    print(f"\n{'='*60}")
    print(f"SkillML Validation Report")
    print(f"{'='*60}")
    print(f"Total skills: {total}")
    print(f"  PASSED:      {len(results['passed'])}")
    print(f"  FAILED:      {len(results['failed'])}")
    print(f"  PARSE ERROR: {len(results['errors'])}")
    print()

    if results["passed"]:
        print("PASSED:")
        for r in results["passed"]:
            print(f"  [OK] {r['skill_id']} ({r['version']}) - {r['score']}")

    if results["failed"]:
        print("\nFAILED (structure issues):")
        for r in results["failed"]:
            print(f"  [FAIL] {r['skill_id']} ({r['version']}) - {r['score']}")
            failed_checks = [k for k, v in r["checks"].items() if isinstance(v, bool) and not v]
            for fc in failed_checks:
                print(f"         - {fc}")

    if results["errors"]:
        print("\nPARSE ERRORS (fix XML first):")
        for r in results["errors"]:
            err = r["checks"].get("parse_error", "unknown")
            print(f"  [ERR] {Path(r['file']).name}")
            print(f"        {err}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python tools/skillml_validator.py <skill.xml>")
        print("  python tools/skillml_validator.py --all")
        print("  python tools/skillml_validator.py --domain copy")
        sys.exit(1)

    if sys.argv[1] == "--all":
        results = validate_directory()
        print_results(results)
    elif sys.argv[1] == "--domain":
        domain = sys.argv[2] if len(sys.argv) > 2 else None
        results = validate_directory(domain)
        print_results(results)
    else:
        result = validate_skillml(sys.argv[1])
        print(json.dumps(result, indent=2, default=str))
        sys.exit(0 if result["passed"] else 1)
