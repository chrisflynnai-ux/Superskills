# SkillML Specification v1.0

> **Per:** REFACTOR PLAN v1.4
> **Dialect:** Relaxed XML (well-formed, not strict XSD)
> **Validator:** `tools/skillml_validator.py`
> **Linter:** `tools/lint_skill.py`

---

## 1. Overview

SkillML is a relaxed XML dialect for defining SUPERMIND skills. It enforces structural conventions (root element, required sections, layer tags) while allowing free-form content within sections.

**Key principle:** Structure is validated, content is not. The XML must be well-formed and contain required sections, but what goes inside those sections is up to the skill author.

---

## 2. Root Element

```xml
<Skill
  skill_id="{domain}_{function}"
  version="{major}.{minor}.{patch}"
  status="{draft|beta|active|deprecated}"
>
```

### Required Attributes

| Attribute | Format | Example | Rule |
|-----------|--------|---------|------|
| `skill_id` | `{domain}_{function}` | `copy_advertorial` | Lowercase, underscores, no dots |
| `version` | Semver | `2.0.0` | `\d+\.\d+\.\d+` |
| `status` | Enum | `active` | `draft\|beta\|active\|deprecated` |

### Optional Attributes

| Attribute | Purpose |
|-----------|---------|
| `name` | Human-readable name |
| `tier` | `system\|meta\|production\|experimental` |
| `model` | `sonnet\|opus\|haiku` |

---

## 3. Required Sections (5)

Every skill must contain these 5 sections as descendants of `<Skill>`:

### 3.1 Meta
```xml
<Meta>
  <Name>...</Name>
  <Description>...</Description>
  <!-- Free-form metadata -->
</Meta>
```

### 3.2 Contract
```xml
<Contract>
  <InputsRequired>...</InputsRequired>
  <OutputsPrimary>...</OutputsPrimary>
  <!-- I/O specification -->
</Contract>
```

### 3.3 ExecutionProtocol
```xml
<ExecutionProtocol>
  <Rules>...</Rules>
  <ReasoningFramework>...</ReasoningFramework>
  <Implementation>...</Implementation>
</ExecutionProtocol>
```

### 3.4 SelfCheck
```xml
<SelfCheck>
  <Check id="SC-01" type="structural">...</Check>
  <Check id="SC-02" type="content">...</Check>
  <Check id="SC-03" type="compliance">...</Check>
  <!-- Minimum 3 Check elements -->
  <MMAGate>...</MMAGate>
</SelfCheck>
```

### 3.5 PatchLog
```xml
<PatchLog>
  <Entry version="1.0.0" date="YYYY-MM-DD" author="agent|human">
    Description of changes.
  </Entry>
</PatchLog>
```

---

## 4. Layer Tags (4 Required)

Four layer markers must appear somewhere in the XML content (as comments or element names):

| Tag | Purpose | Typical Location |
|-----|---------|-----------------|
| `LAYER:CONTRACT` | I/O specification | Above or inside `<Contract>` |
| `LAYER:RULES` | Governing rules | Above or inside `<ExecutionProtocol>` |
| `LAYER:REASONING` | Reasoning framework | Inside `<ExecutionProtocol>` |
| `LAYER:IMPL` | Implementation details | Inside `<ExecutionProtocol>` |

Layer tags can appear in comments (`<!-- LAYER:CONTRACT -->`) or as text content. The validator checks for string presence in the raw XML.

---

## 5. SelfCheck Requirements

### Minimum 3 Check Elements

```xml
<Check id="SC-01" type="structural">
  <Name>Check name</Name>
  <Condition>What must be true</Condition>
  <OnFail>What to do on failure</OnFail>
</Check>
```

Check types: `structural`, `content`, `compliance`, `proof`, `resonance`

### MMAGate (Required)

```xml
<MMAGate>
  <Trigger>When to invoke MMA scoring</Trigger>
  <MinScore>8.0</MinScore>
  <OnFail>Route to FIX loop (max 3 iterations)</OnFail>
</MMAGate>
```

### FailureModes (Recommended)

```xml
<FailureModes>
  <Mode name="failure_type">
    <Symptom>How it manifests</Symptom>
    <Cause>Why it happens</Cause>
    <Fix>How to resolve</Fix>
  </Mode>
</FailureModes>
```

---

## 6. Naming Conventions

### skill_id Format
```
{domain}_{function}
```

| Domain | Examples |
|--------|----------|
| `copy` | `copy_advertorial`, `copy_lfva`, `copy_sfvw` |
| `research` | `research_market_intel`, `research_deconstructor` |
| `meta` | `meta_mma`, `meta_zpwo`, `meta_skill_builder` |
| `design` | `design_master`, `design_wireframe` |
| `product` | `product_offer_architect`, `product_quick_builder` |
| `ads` | `ads_generator`, `ads_andromeda_engine` |
| `email` | `email_architecture`, `email_launch_sequence` |
| `leadgen` | `leadgen_funnel`, `leadgen_cold_outreach` |

### Legacy ID Migration

Old format: `skill.copy.long_form_vsl_script_architect.v3_0_0`
New format: `copy_lfva`

Use `tools/alias_resolver.py` for backward compatibility. Old IDs are mapped in `orchestration/routing/aliases.yaml`.

### File Naming
```
{skill_slug}_v{major}_{minor}_{patch}.xml
```
Example: `advertorial_copy_master_v2_0_0.xml`

---

## 7. Validation Rules

The `skillml_validator.py` checks 19 conditions:

| # | Check | Required |
|---|-------|----------|
| 1 | Well-formed XML | Yes |
| 2 | Root element is `<Skill>` | Yes |
| 3 | `skill_id` attribute present | Yes |
| 4 | `skill_id` matches `{domain}_{function}` | Yes |
| 5 | `version` attribute present | Yes |
| 6 | `version` is semver | Yes |
| 7 | `status` attribute present | Yes |
| 8 | `<Meta>` section exists | Yes |
| 9 | `<Contract>` section exists | Yes |
| 10 | `<ExecutionProtocol>` section exists | Yes |
| 11 | `<SelfCheck>` section exists | Yes |
| 12 | `<PatchLog>` section exists | Yes |
| 13 | >= 3 `<Check>` elements in SelfCheck | Yes |
| 14 | `<MMAGate>` present | Yes |
| 15 | `LAYER:CONTRACT` tag present | Yes |
| 16 | `LAYER:RULES` tag present | Yes |
| 17 | `LAYER:REASONING` tag present | Yes |
| 18 | `LAYER:IMPL` tag present | Yes |
| 19 | All 4 layers present | Yes |

---

## 8. Migration Scoring

The `lint_skill.py` migration report scores skills on 10 criteria:

| Criterion | Weight |
|-----------|--------|
| Has all 4 V1.4 layer tags | 10% |
| Has all 5 required sections | 10% |
| Has 3+ SelfCheck checks | 10% |
| Has MMAGate | 10% |
| Has PatchLog | 10% |
| skill_id in V1.4 format | 10% |
| Version is semver | 10% |
| Has Contract section | 10% |
| Has ExecutionProtocol | 10% |
| Has circuit breaker reference | 10% |

**Migration ready:** Score >= 80%

---

## 9. Tooling Quick Reference

```bash
# Validate single skill
python tools/skillml_validator.py path/to/skill.xml

# Validate all skills
python tools/skillml_validator.py --all

# Validate by domain
python tools/skillml_validator.py --domain copy

# Lint with migration scoring
python tools/lint_skill.py path/to/skill.xml

# Full migration readiness report
python tools/lint_skill.py --migration-report

# Generate manifest
python tools/manifest_builder.py

# Resolve skill alias
python tools/alias_resolver.py /advertorial
python tools/alias_resolver.py copy_advertorial

# Run acceptance tests
python tools/acceptance_tests.py
```

---

*SkillML Spec v1.0 — 2026-03-05*
*Per REFACTOR PLAN v1.4*
