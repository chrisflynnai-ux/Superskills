#!/usr/bin/env python3
"""
SSOT Validator v1.0
Validates Single Source of Truth objects against schemas.

Per REFACTOR PLAN v1.4:
- PROJECT_BRIEF.yaml: Goal, Avatar, Offer (required fields)
- MESSAGE_SPINE.yaml: Promise, Mechanism, Proof (required fields)
- EVIDENCE_PACK.yaml: Claims, Citations, Gaps (required fields)
- SESSION_STATE.json: Active phase, FIX counts, token stats

Usage:
    python tools/validate_ssot.py                    # Validate all SSOT files
    python tools/validate_ssot.py PROJECT_BRIEF      # Validate specific object
    python tools/validate_ssot.py --check-locks       # Verify lock integrity
    python tools/validate_ssot.py --pre-transition T3 # Pre-phase-transition check
"""
import sys
import os
import json
import hashlib
from pathlib import Path

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


ROOT = Path(__file__).parent.parent
SSOT_DIR = ROOT / "ssot"
SCHEMAS_DIR = ROOT / ".claude" / "schemas"


# ============================================================
# SSOT SCHEMAS (embedded for zero-dependency operation)
# ============================================================

SSOT_SCHEMAS = {
    "PROJECT_BRIEF": {
        "required_fields": [
            "project_name",
            "goal",
            "avatar",
            "offer",
        ],
        "recommended_fields": [
            "avatar.age_range",
            "avatar.pain_points",
            "avatar.desires",
            "avatar.awareness_level",
            "offer.name",
            "offer.price",
            "offer.mechanism",
            "acquisition_channel",
            "target_audience",
        ],
        "file_patterns": ["PROJECT_BRIEF.yaml", "PROJECT_BRIEF.yml", "project_brief.yaml"],
    },
    "MESSAGE_SPINE": {
        "required_fields": [
            "promise",
            "mechanism",
            "proof",
        ],
        "recommended_fields": [
            "promise.headline",
            "promise.subheadline",
            "mechanism.name",
            "mechanism.description",
            "mechanism.uniqueness",
            "proof.statistics",
            "proof.testimonials",
            "proof.credentials",
            "belief_shifts",
            "objections",
        ],
        "file_patterns": ["MESSAGE_SPINE.yaml", "MESSAGE_SPINE.yml", "message_spine.yaml"],
    },
    "EVIDENCE_PACK": {
        "required_fields": [
            "claims",
        ],
        "recommended_fields": [
            "claims",
            "citations",
            "gaps",
            "proof_strength",
        ],
        "file_patterns": ["EVIDENCE_PACK.yaml", "EVIDENCE_PACK.yml", "evidence_pack.yaml"],
    },
    "SESSION_STATE": {
        "required_fields": [
            "active_phase",
        ],
        "recommended_fields": [
            "active_phase",
            "fix_counts",
            "token_stats",
            "current_track",
            "last_mma_score",
        ],
        "file_patterns": ["SESSION_STATE.json", "session_state.json"],
    },
}


def find_ssot_file(object_name: str) -> Path:
    """Find the SSOT file for a given object name."""
    schema = SSOT_SCHEMAS.get(object_name)
    if not schema:
        return None

    for pattern in schema["file_patterns"]:
        # Check ssot/ directory first
        path = SSOT_DIR / pattern
        if path.exists():
            return path
        # Check root
        path = ROOT / pattern
        if path.exists():
            return path

    return None


def load_ssot_file(filepath: Path) -> dict:
    """Load a SSOT file (YAML or JSON)."""
    content = filepath.read_text(encoding="utf-8")

    if filepath.suffix in (".yaml", ".yml"):
        if HAS_YAML:
            return yaml.safe_load(content) or {}
        else:
            # Minimal YAML parser for flat structures
            return _parse_flat_yaml(content)
    elif filepath.suffix == ".json":
        return json.loads(content)

    return {}


def _parse_flat_yaml(content: str) -> dict:
    """Minimal flat YAML parser."""
    data = {}
    for line in content.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if value:
                data[key] = value
    return data


def check_nested_field(data: dict, field_path: str) -> bool:
    """Check if a nested field exists (e.g., 'avatar.pain_points')."""
    parts = field_path.split(".")
    current = data

    for part in parts:
        if isinstance(current, dict):
            if part in current:
                current = current[part]
            else:
                return False
        else:
            return False

    # Field exists — check it has content
    if current is None:
        return False
    if isinstance(current, str) and not current.strip():
        return False
    if isinstance(current, (list, dict)) and len(current) == 0:
        return False

    return True


def compute_checksum(filepath: Path) -> str:
    """Compute SHA-256 checksum for lock verification."""
    content = filepath.read_bytes()
    return hashlib.sha256(content).hexdigest()[:16]


def validate_ssot_object(object_name: str) -> dict:
    """Validate a single SSOT object."""
    result = {
        "object": object_name,
        "passed": False,
        "file": None,
        "checks": [],
    }

    schema = SSOT_SCHEMAS.get(object_name)
    if not schema:
        result["checks"].append({
            "name": "schema_exists",
            "passed": False,
            "msg": f"No schema defined for '{object_name}'",
        })
        return result

    # Find file
    filepath = find_ssot_file(object_name)
    if not filepath:
        result["checks"].append({
            "name": "file_exists",
            "passed": False,
            "msg": f"SSOT file not found. Expected one of: {schema['file_patterns']}",
        })
        return result

    result["file"] = str(filepath)
    result["checks"].append({
        "name": "file_exists",
        "passed": True,
        "msg": f"Found at {filepath}",
    })

    # Load data
    try:
        data = load_ssot_file(filepath)
        result["checks"].append({
            "name": "parseable",
            "passed": True,
            "msg": "File parsed successfully",
        })
    except Exception as e:
        result["checks"].append({
            "name": "parseable",
            "passed": False,
            "msg": f"Parse error: {str(e)}",
        })
        return result

    # Check non-empty
    if not data:
        result["checks"].append({
            "name": "non_empty",
            "passed": False,
            "msg": "File is empty or contains no data",
        })
        return result

    result["checks"].append({
        "name": "non_empty",
        "passed": True,
        "msg": f"Contains {len(data)} top-level keys",
    })

    # Check required fields
    required_count = 0
    required_total = len(schema["required_fields"])
    for field in schema["required_fields"]:
        found = check_nested_field(data, field)
        result["checks"].append({
            "name": f"required_{field}",
            "passed": found,
            "msg": f"Required field '{field}': {'FOUND' if found else 'MISSING'}",
        })
        if found:
            required_count += 1

    result["checks"].append({
        "name": "required_fields_coverage",
        "passed": required_count == required_total,
        "msg": f"Required: {required_count}/{required_total}",
    })

    # Check recommended fields
    recommended_count = 0
    recommended_total = len(schema["recommended_fields"])
    for field in schema["recommended_fields"]:
        found = check_nested_field(data, field)
        if not found:
            result["checks"].append({
                "name": f"recommended_{field}",
                "passed": True,  # Recommended = warning, not failure
                "msg": f"Recommended field '{field}': MISSING (optional)",
                "level": "warning",
            })
        else:
            recommended_count += 1

    result["recommended_coverage"] = f"{recommended_count}/{recommended_total}"

    # Compute checksum
    result["checksum"] = compute_checksum(filepath)

    # Overall pass
    required_checks = [c for c in result["checks"] if c["name"].startswith("required_") or
                       c["name"] in ("file_exists", "parseable", "non_empty", "required_fields_coverage")]
    result["passed"] = all(c["passed"] for c in required_checks)

    return result


def validate_all() -> dict:
    """Validate all SSOT objects."""
    results = {
        "objects": {},
        "summary": {
            "total": len(SSOT_SCHEMAS),
            "passed": 0,
            "failed": 0,
            "missing": 0,
        }
    }

    for object_name in SSOT_SCHEMAS:
        result = validate_ssot_object(object_name)
        results["objects"][object_name] = result

        if result["file"] is None:
            results["summary"]["missing"] += 1
        elif result["passed"]:
            results["summary"]["passed"] += 1
        else:
            results["summary"]["failed"] += 1

    return results


def check_locks() -> dict:
    """Verify SSOT lock integrity — checksums match locked state."""
    lock_file = SSOT_DIR / ".ssot_locks.json"
    if not lock_file.exists():
        return {"locked": False, "msg": "No lock file found. Run /intake to create SSOT locks."}

    try:
        locks = json.loads(lock_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"locked": False, "msg": "Lock file is corrupted."}

    results = {"locked": True, "objects": {}}

    for object_name, lock_info in locks.items():
        filepath = find_ssot_file(object_name)
        if not filepath:
            results["objects"][object_name] = {"status": "MISSING", "msg": "File not found"}
            results["locked"] = False
            continue

        current_checksum = compute_checksum(filepath)
        locked_checksum = lock_info.get("checksum", "")

        if current_checksum == locked_checksum:
            results["objects"][object_name] = {
                "status": "LOCKED",
                "checksum": current_checksum,
            }
        else:
            results["objects"][object_name] = {
                "status": "DRIFT_DETECTED",
                "expected": locked_checksum,
                "actual": current_checksum,
                "msg": "File has been modified since lock!",
            }
            results["locked"] = False

    return results


def pre_transition_check(target_track: str) -> dict:
    """Run pre-phase-transition validation."""
    result = {
        "target_track": target_track,
        "passed": True,
        "checks": [],
    }

    # T1→T2: PROJECT_BRIEF and MESSAGE_SPINE must exist and be valid
    if target_track in ("T2", "T3", "T4"):
        for obj in ["PROJECT_BRIEF", "MESSAGE_SPINE"]:
            validation = validate_ssot_object(obj)
            passed = validation["passed"]
            result["checks"].append({
                "name": f"{obj}_valid",
                "passed": passed,
                "msg": f"{obj}: {'VALID' if passed else 'INVALID or MISSING'}",
            })
            if not passed:
                result["passed"] = False

    # T2→T3: EVIDENCE_PACK must exist
    if target_track in ("T3", "T4"):
        validation = validate_ssot_object("EVIDENCE_PACK")
        passed = validation["passed"]
        result["checks"].append({
            "name": "EVIDENCE_PACK_valid",
            "passed": passed,
            "msg": f"EVIDENCE_PACK: {'VALID' if passed else 'INVALID or MISSING'}",
        })
        if not passed:
            result["passed"] = False

    # T3→T4: MMA score check (from SESSION_STATE)
    if target_track == "T4":
        state_file = find_ssot_file("SESSION_STATE")
        if state_file:
            try:
                state = load_ssot_file(state_file)
                mma_score = state.get("last_mma_score", 0)
                passed = float(mma_score) >= 8.0 if mma_score else False
                result["checks"].append({
                    "name": "mma_production_gate",
                    "passed": passed,
                    "msg": f"MMA Score: {mma_score} (need >= 8.0 for T4)",
                })
                if not passed:
                    result["passed"] = False
            except (ValueError, TypeError):
                result["checks"].append({
                    "name": "mma_production_gate",
                    "passed": False,
                    "msg": "Could not read MMA score from SESSION_STATE",
                })
                result["passed"] = False

    # Lock integrity check
    lock_result = check_locks()
    if lock_result.get("locked") is False:
        result["checks"].append({
            "name": "ssot_lock_integrity",
            "passed": False,
            "msg": "SSOT lock integrity check failed — possible drift",
            "level": "warning",
        })

    return result


def print_results(results: dict):
    """Print validation results."""
    s = results["summary"]
    print(f"\n{'='*60}")
    print(f"SSOT Validation Report")
    print(f"{'='*60}")
    print(f"Total objects:  {s['total']}")
    print(f"  PASSED:       {s['passed']}")
    print(f"  FAILED:       {s['failed']}")
    print(f"  MISSING:      {s['missing']}")
    print()

    for obj_name, result in results["objects"].items():
        status = "OK" if result["passed"] else ("MISSING" if result["file"] is None else "FAIL")
        icon = {"OK": "[OK]", "FAIL": "[FAIL]", "MISSING": "[---]"}[status]
        print(f"  {icon} {obj_name}")

        if result["file"]:
            print(f"       File: {result['file']}")
            if result.get("checksum"):
                print(f"       Checksum: {result['checksum']}")
            if result.get("recommended_coverage"):
                print(f"       Recommended coverage: {result['recommended_coverage']}")

        failed_checks = [c for c in result.get("checks", []) if not c["passed"]]
        for fc in failed_checks:
            level = fc.get("level", "error")
            prefix = "WARNING" if level == "warning" else "ERROR"
            print(f"       [{prefix}] {fc['msg']}")

    print()


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "--check-locks":
        result = check_locks()
        print(json.dumps(result, indent=2, default=str))
        sys.exit(0 if result.get("locked") else 1)

    elif len(sys.argv) >= 3 and sys.argv[1] == "--pre-transition":
        target = sys.argv[2].upper()
        result = pre_transition_check(target)
        print(json.dumps(result, indent=2, default=str))
        sys.exit(0 if result["passed"] else 1)

    elif len(sys.argv) >= 2 and sys.argv[1] not in ("--check-locks", "--pre-transition"):
        # Validate specific object
        obj = sys.argv[1].upper()
        result = validate_ssot_object(obj)
        print(json.dumps(result, indent=2, default=str))
        sys.exit(0 if result["passed"] else 1)

    else:
        # Validate all
        results = validate_all()
        print_results(results)
        sys.exit(0 if results["summary"]["failed"] == 0 else 1)
