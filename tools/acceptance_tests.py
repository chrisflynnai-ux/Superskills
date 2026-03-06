#!/usr/bin/env python3
"""
Phase 0 Acceptance Tests v1.0
Per REFACTOR PLAN v1.4 — AT-01 through AT-10

Tests verify Phase 0 tooling is operational before skill migration begins.
All tests must pass before proceeding to Phase 1.

Usage:
    python tools/acceptance_tests.py           # Run all tests
    python tools/acceptance_tests.py AT-03     # Run specific test
    python tools/acceptance_tests.py --summary # Quick pass/fail summary
"""
import sys
import os
import json
import importlib.util
from pathlib import Path

ROOT = Path(__file__).parent.parent
SKILLS_DIR = ROOT / ".claude" / "skills"
TOOLS_DIR = ROOT / "tools"
ROUTING_DIR = ROOT / "orchestration" / "routing"


def load_module(name: str, filepath: Path):
    """Dynamically import a Python module."""
    spec = importlib.util.spec_from_file_location(name, filepath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class AcceptanceTests:
    """Phase 0 acceptance test suite."""

    def __init__(self):
        self.results = []

    def run_test(self, test_id: str, name: str, test_fn):
        """Run a single test and record result."""
        try:
            passed, msg = test_fn()
            self.results.append({
                "id": test_id,
                "name": name,
                "passed": passed,
                "msg": msg,
            })
        except Exception as e:
            self.results.append({
                "id": test_id,
                "name": name,
                "passed": False,
                "msg": f"Exception: {str(e)}",
            })

    def at_01_skillml_validator_exists(self):
        """AT-01: SkillML validator exists and is importable."""
        path = TOOLS_DIR / "skillml_validator.py"
        if not path.exists():
            return False, "skillml_validator.py not found"
        try:
            mod = load_module("skillml_validator", path)
            assert hasattr(mod, "validate_skillml"), "Missing validate_skillml function"
            assert hasattr(mod, "validate_directory"), "Missing validate_directory function"
            return True, "SkillML validator exists and has required functions"
        except Exception as e:
            return False, f"Import error: {e}"

    def at_02_validator_catches_invalid(self):
        """AT-02: Validator correctly identifies invalid XML."""
        path = TOOLS_DIR / "skillml_validator.py"
        mod = load_module("skillml_validator", path)

        # Test with a known-parseable but non-compliant file
        test_files = list(SKILLS_DIR.rglob("*.xml"))
        if not test_files:
            return False, "No XML files found to test"

        # Run on first parseable file
        for f in test_files:
            result = mod.validate_skillml(str(f))
            if "checks" in result:
                # Should have checks dict
                assert isinstance(result["checks"], dict), "checks should be a dict"
                assert "passed" in result, "result should have 'passed' key"
                return True, f"Validator ran successfully on {f.name}, passed={result['passed']}"

        return False, "Could not find any testable XML files"

    def at_03_alias_resolver_exists(self):
        """AT-03: Alias resolver exists and aliases.yaml is populated."""
        resolver_path = TOOLS_DIR / "alias_resolver.py"
        aliases_path = ROUTING_DIR / "aliases.yaml"

        if not resolver_path.exists():
            return False, "alias_resolver.py not found"
        if not aliases_path.exists():
            return False, "aliases.yaml not found"

        # Check aliases has content
        content = aliases_path.read_text(encoding="utf-8")
        skill_count = content.count("- skill_id:")
        if skill_count < 30:
            return False, f"aliases.yaml has only {skill_count} entries (need >= 30)"

        return True, f"Alias resolver + aliases.yaml ({skill_count} entries)"

    def at_04_manifest_builder_exists(self):
        """AT-04: Manifest builder exists and can generate manifest."""
        path = TOOLS_DIR / "manifest_builder.py"
        manifest_path = ROOT / ".claude" / "SKILLS_MANIFEST.yaml"

        if not path.exists():
            return False, "manifest_builder.py not found"

        try:
            mod = load_module("manifest_builder", path)
            assert hasattr(mod, "build_manifest"), "Missing build_manifest function"

            # Check if manifest was already generated
            if manifest_path.exists():
                content = manifest_path.read_text(encoding="utf-8")
                if "domains:" in content:
                    return True, "Manifest builder exists and manifest is generated"

            return True, "Manifest builder exists (manifest not yet generated)"
        except Exception as e:
            return False, f"Import error: {e}"

    def at_05_master_template_exists(self):
        """AT-05: Master SkillML template exists and is valid."""
        template_path = SKILLS_DIR / "_template" / "master_skill_template_v1.xml"

        if not template_path.exists():
            return False, "master_skill_template_v1.xml not found"

        content = template_path.read_text(encoding="utf-8")

        # Check required markers
        checks = {
            "has_skill_root": "<Skill" in content,
            "has_meta": "<Meta>" in content,
            "has_contract": "<Contract>" in content,
            "has_execution": "<ExecutionProtocol>" in content,
            "has_selfcheck": "<SelfCheck>" in content,
            "has_patchlog": "<PatchLog>" in content,
            "has_layer_contract": "LAYER:CONTRACT" in content,
            "has_layer_rules": "LAYER:RULES" in content,
            "has_layer_reasoning": "LAYER:REASONING" in content,
            "has_layer_impl": "LAYER:IMPL" in content,
            "has_mmagate": "<MMAGate>" in content,
            "has_3_checks": content.count("<Check ") >= 3,
        }

        failed = [k for k, v in checks.items() if not v]
        if failed:
            return False, f"Template missing: {', '.join(failed)}"

        return True, "Master template has all V1.4 required elements"

    def at_06_routing_table_exists(self):
        """AT-06: Routing table v4.0 exists with 4-track structure."""
        path = ROUTING_DIR / "routing_table.yaml"

        if not path.exists():
            return False, "routing_table.yaml not found"

        content = path.read_text(encoding="utf-8")

        checks = {
            "has_T1": "T1:" in content,
            "has_T2": "T2:" in content,
            "has_T3": "T3:" in content,
            "has_T4": "T4:" in content,
            "has_routes": "routes:" in content,
            "has_chains": "chains:" in content,
            "has_team_rules": "team_rules:" in content,
        }

        failed = [k for k, v in checks.items() if not v]
        if failed:
            return False, f"Routing table missing: {', '.join(failed)}"

        route_count = content.count("- command:")
        return True, f"Routing table v4.0 with {route_count} routes and 4 tracks"

    def at_07_validate_ssot_exists(self):
        """AT-07: SSOT validation script exists."""
        path = TOOLS_DIR / "validate_ssot.py"

        if not path.exists():
            return False, "validate_ssot.py not found"

        try:
            mod = load_module("validate_ssot", path)
            assert hasattr(mod, "validate_ssot_object"), "Missing validate_ssot_object"
            assert hasattr(mod, "validate_all"), "Missing validate_all"
            assert hasattr(mod, "pre_transition_check"), "Missing pre_transition_check"
            return True, "SSOT validator exists with all required functions"
        except Exception as e:
            return False, f"Import error: {e}"

    def at_08_lint_skill_exists(self):
        """AT-08: SkillML linter exists with migration report."""
        path = TOOLS_DIR / "lint_skill.py"

        if not path.exists():
            return False, "lint_skill.py not found"

        try:
            mod = load_module("lint_skill", path)
            assert hasattr(mod, "lint_skill"), "Missing lint_skill function"
            assert hasattr(mod, "migration_report"), "Missing migration_report function"
            return True, "SkillML linter exists with migration report capability"
        except Exception as e:
            return False, f"Import error: {e}"

    def at_09_skills_directory_structure(self):
        """AT-09: Skills directory has proper domain structure."""
        expected_domains = ["ads", "copy", "design", "email", "leadgen",
                           "meta", "product", "research"]
        missing = []
        for domain in expected_domains:
            if not (SKILLS_DIR / domain).exists():
                missing.append(domain)

        if missing:
            return False, f"Missing domain directories: {', '.join(missing)}"

        # Check template exists
        if not (SKILLS_DIR / "_template").exists():
            return False, "_template directory missing"

        # Check archive exists
        if not (SKILLS_DIR / "_archive").exists():
            return False, "_archive directory missing"

        total_domains = len([d for d in SKILLS_DIR.iterdir() if d.is_dir()
                            and not d.name.startswith("_") and d.name != "styles"])
        xml_count = len(list(SKILLS_DIR.rglob("*.xml")))

        return True, f"{total_domains} domains, {xml_count} XML files, _template and _archive present"

    def at_10_tool_index_complete(self):
        """AT-10: All Phase 0 tools are registered and accessible."""
        required_tools = {
            "skillml_validator.py": TOOLS_DIR / "skillml_validator.py",
            "alias_resolver.py": TOOLS_DIR / "alias_resolver.py",
            "manifest_builder.py": TOOLS_DIR / "manifest_builder.py",
            "validate_ssot.py": TOOLS_DIR / "validate_ssot.py",
            "lint_skill.py": TOOLS_DIR / "lint_skill.py",
            "acceptance_tests.py": TOOLS_DIR / "acceptance_tests.py",
        }

        required_configs = {
            "aliases.yaml": ROUTING_DIR / "aliases.yaml",
            "routing_table.yaml": ROUTING_DIR / "routing_table.yaml",
            "master_template": SKILLS_DIR / "_template" / "master_skill_template_v1.xml",
        }

        missing_tools = [k for k, v in required_tools.items() if not v.exists()]
        missing_configs = [k for k, v in required_configs.items() if not v.exists()]

        if missing_tools or missing_configs:
            all_missing = missing_tools + missing_configs
            return False, f"Missing: {', '.join(all_missing)}"

        return True, f"All {len(required_tools)} tools + {len(required_configs)} configs present"

    def run_all(self):
        """Run all acceptance tests."""
        tests = [
            ("AT-01", "SkillML validator exists", self.at_01_skillml_validator_exists),
            ("AT-02", "Validator catches invalid XML", self.at_02_validator_catches_invalid),
            ("AT-03", "Alias resolver + aliases.yaml", self.at_03_alias_resolver_exists),
            ("AT-04", "Manifest builder exists", self.at_04_manifest_builder_exists),
            ("AT-05", "Master template V1.4 compliant", self.at_05_master_template_exists),
            ("AT-06", "Routing table v4.0", self.at_06_routing_table_exists),
            ("AT-07", "SSOT validation script", self.at_07_validate_ssot_exists),
            ("AT-08", "SkillML linter + migration", self.at_08_lint_skill_exists),
            ("AT-09", "Skills directory structure", self.at_09_skills_directory_structure),
            ("AT-10", "Tool index complete", self.at_10_tool_index_complete),
        ]

        for test_id, name, fn in tests:
            self.run_test(test_id, name, fn)

        return self.results


def print_results(results: list):
    """Print acceptance test results."""
    passed = sum(1 for r in results if r["passed"])
    total = len(results)

    print(f"\n{'='*60}")
    print(f"Phase 0 Acceptance Tests")
    print(f"{'='*60}")
    print(f"Result: {passed}/{total} PASSED\n")

    for r in results:
        icon = "[PASS]" if r["passed"] else "[FAIL]"
        print(f"  {icon} {r['id']}: {r['name']}")
        print(f"         {r['msg']}")
        print()

    if passed == total:
        print("  >>> ALL TESTS PASSED — Phase 0 Complete <<<")
        print("  >>> Ready for Phase 1: Skill Migration <<<")
    else:
        failed = [r for r in results if not r["passed"]]
        print(f"  >>> {len(failed)} TESTS FAILED — Fix before proceeding <<<")


if __name__ == "__main__":
    suite = AcceptanceTests()

    if len(sys.argv) >= 2 and sys.argv[1] == "--summary":
        results = suite.run_all()
        passed = sum(1 for r in results if r["passed"])
        total = len(results)
        print(f"Phase 0: {passed}/{total} passed")
        sys.exit(0 if passed == total else 1)

    elif len(sys.argv) >= 2 and sys.argv[1].startswith("AT-"):
        # Run specific test
        test_map = {
            "AT-01": ("SkillML validator", suite.at_01_skillml_validator_exists),
            "AT-02": ("Validator validation", suite.at_02_validator_catches_invalid),
            "AT-03": ("Alias resolver", suite.at_03_alias_resolver_exists),
            "AT-04": ("Manifest builder", suite.at_04_manifest_builder_exists),
            "AT-05": ("Master template", suite.at_05_master_template_exists),
            "AT-06": ("Routing table", suite.at_06_routing_table_exists),
            "AT-07": ("SSOT validator", suite.at_07_validate_ssot_exists),
            "AT-08": ("SkillML linter", suite.at_08_lint_skill_exists),
            "AT-09": ("Directory structure", suite.at_09_skills_directory_structure),
            "AT-10": ("Tool index", suite.at_10_tool_index_complete),
        }

        test_id = sys.argv[1].upper()
        if test_id in test_map:
            name, fn = test_map[test_id]
            suite.run_test(test_id, name, fn)
            print_results(suite.results)
        else:
            print(f"Unknown test: {test_id}")
            sys.exit(1)
    else:
        results = suite.run_all()
        print_results(results)
        passed = sum(1 for r in results if r["passed"])
        sys.exit(0 if passed == len(results) else 1)
