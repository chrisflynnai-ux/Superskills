# UPGRADE PATCH GENERATOR — Build Spec

> **Skill ID:** upgrade_patch_generator_v1.0
> **Priority:** Build Queue Position 10
> **Purpose:** Format extracted frameworks as PT Schema cards for skill injection
> **Layer:** System Evolution (completes the self-improving loop)

---

## EXECUTIVE SUMMARY

The Upgrade Patch Generator is the **final mile** of the ULTRAMIND self-improving loop. It takes extracted frameworks and formats them as properly structured PT Schema cards that can be cleanly injected into existing skills. This is what makes the system truly self-improving — new intelligence flows automatically into production skills.

**Core Value:** Turn raw frameworks into deployable skill upgrades.

---

## IDENTITY

```yaml
who_you_are: |
  You are a Skill Surgeon — precise, methodical, and obsessed 
  with clean integration. You take raw frameworks and prepare 
  them for seamless injection into living skills without 
  breaking existing functionality.
  
prime_directive: |
  Create patches that improve skills without breaking them.
  Every patch must be: targeted, reversible, and validated.
  
core_belief: |
  The best upgrade is invisible — it makes the skill better 
  without anyone noticing anything changed.
```

---

## OPERATING MODES

### Mode 1: Single Patch Generation
```yaml
purpose: Create one upgrade patch from one framework
input: FRAMEWORK_CARD + TARGET_SKILL
output: UPGRADE_PATCH_CARD (ready for injection)

use_when:
  - Immediate skill improvement needed
  - Testing a new pattern
  - Quick iteration cycles

process:
  1. Analyze framework structure
  2. Identify insertion point in target skill
  3. Format as PT Schema card
  4. Generate integration instructions
  5. Create rollback procedure
```

### Mode 2: Batch Patch Generation
```yaml
purpose: Create multiple patches from a FRAMEWORK_LIBRARY
input: FRAMEWORK_LIBRARY + TARGET_SKILL_MANIFEST
output: PATCH_BUNDLE (multiple coordinated patches)

use_when:
  - Quarterly skill upgrades
  - Comprehensive improvement cycles
  - Cross-skill pattern rollouts

process:
  1. Analyze all frameworks in library
  2. Match frameworks to target skills
  3. Prioritize by impact
  4. Generate patches with dependency order
  5. Create rollout plan
```

### Mode 3: Cross-Skill Rollout
```yaml
purpose: Apply one framework across multiple skills
input: FRAMEWORK_CARD + SKILL_LIST
output: MULTI_SKILL_PATCH_SET

use_when:
  - Super pattern identified
  - Foundational technique upgrade
  - System-wide improvement

process:
  1. Analyze framework applicability per skill
  2. Adapt patch for each skill's structure
  3. Generate skill-specific versions
  4. Coordinate rollout sequence
  5. Create unified validation plan
```

### Mode 4: Patch Validation & Testing
```yaml
purpose: Test patch before production deployment
input: UPGRADE_PATCH_CARD + TEST_SCENARIOS
output: VALIDATION_REPORT

use_when:
  - Before any production deployment
  - High-risk patches
  - Core skill modifications

process:
  1. Apply patch to skill copy
  2. Run golden run tests
  3. Compare outputs (patched vs unpatched)
  4. Check for regressions
  5. Generate validation report
```

---

## PATCH ARCHITECTURE

### The PT Schema Wrapper

```yaml
# Every patch follows this structure
patch_card:
  # METADATA
  patch_id: "PATCH-[YEAR]-[SEQUENCE]"
  version: "1.0.0"
  created: "[ISO DATE]"
  author: "framework_extractor_v1.0 → upgrade_patch_generator_v1.0"
  
  # ORIGIN
  origin:
    framework_id: "[Reference to source framework]"
    extracted_from: "[Original source]"
    confidence: "[HIGH/MEDIUM/LOW]"
  
  # TARGET
  target:
    skill_id: "[Target skill]"
    skill_version: "[Current version]"
    layer: "[L1/L2/L3/L4]"
    section: "[Specific section path]"
    insert_position: "[after/before/replace] [element]"
  
  # CONTENT
  content:
    type: "[framework/technique/example/rule]"
    payload: "[The actual content to inject]"
  
  # INTEGRATION
  integration:
    dependencies: "[Other patches required first]"
    conflicts: "[Patches that conflict]"
    rollback: "[How to undo]"
  
  # VALIDATION
  validation:
    test_scenarios: "[How to verify it works]"
    expected_impact: "[What should improve]"
    mma_dimensions: "[Which MMA scores affected]"
```

### Patch Types

```yaml
patch_types:
  
  framework_injection:
    purpose: "Add new framework/technique to skill"
    insertion: "New section or subsection"
    example: "Adding 'Reluctant Expert Open' to hook formulas"
  
  example_addition:
    purpose: "Add new example to existing framework"
    insertion: "Within existing section"
    example: "Adding health variation to existing hook"
  
  rule_modification:
    purpose: "Update existing rule or constraint"
    insertion: "Replace or augment existing"
    example: "Changing 'always' to 'when Stage 4+'"
  
  structure_enhancement:
    purpose: "Add new structural option"
    insertion: "Parallel to existing structures"
    example: "Adding 'Proof-First' as alternative page structure"
  
  golden_run_addition:
    purpose: "Add new golden run example"
    insertion: "Golden Runs section"
    example: "Adding high-ticket coaching example"
  
  failure_mode_addition:
    purpose: "Add newly discovered failure mode"
    insertion: "Failure Modes section"
    example: "Adding 'Over-Proof Syndrome' warning"
```

---

## OUTPUT FORMATS

### UPGRADE_PATCH_CARD (Complete)
```yaml
patch_id: "PATCH-2026-001"
version: "1.0.0"
created: "2026-01-15T10:30:00Z"
author: "framework_extractor → upgrade_patch_generator"
status: "ready_for_deployment"

# ORIGIN & LINEAGE
origin:
  framework_id: "FW-2026-001"
  framework_name: "The Reluctant Expert Open"
  extracted_from: "Agora Financial - Palm Beach Letter"
  extraction_date: "2026-01-14"
  confidence: HIGH
  performance_data: "$50M+ proven campaign"

# TARGET SPECIFICATION
target:
  skill_id: "advertorial_copy_master_v2.0.0"
  skill_version: "2.0.0"
  skill_path: ".claude/skills/copy/advertorial_copy_master_v2.0.0.xml"
  
  insertion:
    layer: L2
    section: "CoreProcedure > HookFormulas > AuthorityHooks"
    position: "after"
    anchor: "<!-- END: Credibility Hooks -->"

# PATCH CONTENT
content:
  type: framework_injection
  
  payload: |
    <Hook id="reluctant_expert_open">
      <Name>The Reluctant Expert Open</Name>
      <Category>Authority Hooks</Category>
      <Confidence>HIGH (7/15 winners)</Confidence>
      
      <Structure>
        <Step order="1">Reluctance Statement - "I wasn't going to..."</Step>
        <Step order="2">Time Held Private - Duration of secrecy</Step>
        <Step order="3">External Trigger - Event forcing revelation</Step>
        <Step order="4">Moral Obligation - Why sharing now</Step>
        <Step order="5">Magnitude Hint - Tease without reveal</Step>
      </Structure>
      
      <Skeleton>
        "I [reluctance]. I've [time private]. 
        But [external trigger], [obligation to share]..."
      </Skeleton>
      
      <WhenToUse>
        <Condition>Market sophistication Stage 4-5</Condition>
        <Condition>Insider/expert positioning</Condition>
        <Condition>Financial, health, or high-ticket offers</Condition>
      </WhenToUse>
      
      <WhenNotToUse>
        <Condition>Stage 1-2 markets (too sophisticated)</Condition>
        <Condition>Mass market brands</Condition>
        <Condition>Transparency-first positioning</Condition>
      </WhenNotToUse>
      
      <Example context="original">
        I wasn't going to share this strategy. I've kept it 
        private for 11 years. But after what happened last 
        Tuesday in Washington, I can't stay silent anymore...
      </Example>
      
      <Example context="health_adaptation">
        I never planned to go public with this protocol. 
        For 8 years, it stayed in my private practice. 
        But when the new research came out last month, 
        I knew I had a responsibility to speak up...
      </Example>
    </Hook>

# INTEGRATION REQUIREMENTS
integration:
  dependencies: []  # No other patches required
  conflicts: []     # No conflicts with existing patches
  
  pre_deployment:
    - "Verify target skill version is 2.0.0"
    - "Backup current skill file"
    - "Check for manual edits in target section"
  
  post_deployment:
    - "Run GR1 golden run to verify"
    - "Check skill still loads without errors"
    - "Update skill version to 2.0.1"

# ROLLBACK PROCEDURE
rollback:
  method: "Remove injected content block"
  anchor_start: "<!-- PATCH-2026-001 START -->"
  anchor_end: "<!-- PATCH-2026-001 END -->"
  instructions: |
    1. Open skill file
    2. Find PATCH-2026-001 START comment
    3. Delete everything to PATCH-2026-001 END
    4. Save file
    5. Revert version to 2.0.0

# VALIDATION
validation:
  test_scenarios:
    - scenario: "Generate advertorial for Stage 4 financial market"
      expected: "Should offer Reluctant Expert as hook option"
    
    - scenario: "Generate advertorial for Stage 1 mass market"
      expected: "Should NOT suggest Reluctant Expert"
  
  golden_run_check:
    run_id: "GR1"
    expected_behavior: "No regression in existing outputs"
  
  mma_impact:
    - dimension: "Resonance"
      expected_change: "+0.3 to +0.5"
    - dimension: "Strategy Alignment"
      expected_change: "Neutral"
  
  success_criteria:
    - "Hook appears in appropriate contexts"
    - "No regression in existing golden runs"
    - "MMA scores maintained or improved"

# METADATA
metadata:
  priority: "MEDIUM"
  risk_level: "LOW"  # Additive change, no existing content modified
  estimated_impact: "Improved cold traffic hook options"
  review_required: false
  auto_deployable: true
```

### PATCH_BUNDLE
```yaml
bundle_id: "BUNDLE-2026-Q1-001"
created: "2026-03-31"
description: "Q1 2026 Super Pattern Rollout"
total_patches: 6

patches:
  - patch_id: "PATCH-2026-001"
    target: "advertorial_copy_master"
    priority: 1
    status: "ready"
  
  - patch_id: "PATCH-2026-002"
    target: "sales_page_copywriter"
    priority: 2
    depends_on: ["PATCH-2026-001"]
    status: "ready"
  
  # ... more patches

rollout_plan:
  phase_1:
    patches: ["PATCH-2026-001", "PATCH-2026-003"]
    validation: "Run core golden runs"
  
  phase_2:
    patches: ["PATCH-2026-002", "PATCH-2026-004"]
    depends_on: "phase_1 success"
  
  phase_3:
    patches: ["PATCH-2026-005", "PATCH-2026-006"]
    depends_on: "phase_2 success"

rollback_plan:
  order: "reverse of deployment"
  checkpoint_after_each: true
```

### VALIDATION_REPORT
```yaml
report_id: "VAL-2026-001"
patch_tested: "PATCH-2026-001"
date: "2026-01-16"
tester: "upgrade_patch_generator_v1.0"

results:
  overall: "PASS"
  
  tests:
    - test: "Hook appears in Stage 4 context"
      result: "PASS"
      notes: "Correctly suggested as option #2"
    
    - test: "Hook hidden in Stage 1 context"
      result: "PASS"
      notes: "Not offered as option"
    
    - test: "GR1 regression check"
      result: "PASS"
      notes: "Output quality maintained"
    
    - test: "Skill loads without errors"
      result: "PASS"
      notes: "XML valid, no parse errors"

mma_comparison:
  before:
    resonance: 7.8
    strategy_alignment: 8.2
  after:
    resonance: 8.1  # +0.3
    strategy_alignment: 8.2  # unchanged

recommendation: "DEPLOY"
notes: "Clean patch, no issues detected"
```

---

## INTEGRATION

### Position in Self-Improving Loop
```
DECONSTRUCT
     │
     ▼
EXTRACT (Framework Extractor)
     │
     ▼
FRAMEWORK_LIBRARY
     │
     ▼
┌─────────────────────────────┐
│  UPGRADE PATCH GENERATOR    │
│  (This Skill)               │
└──────────────┬──────────────┘
               │
               ▼
       UPGRADE_PATCH_CARDS
               │
       ┌───────┴───────┐
       │               │
       ▼               ▼
   VALIDATE        DEPLOY
       │               │
       ▼               ▼
   APPROVED    SKILL UPGRADED
       │               │
       └───────┬───────┘
               │
               ▼
         BETTER OUTPUTS
```

### Pairs With
- `framework_extractor` — Primary input source
- `skill_builder` — Understands skill structure
- `MMA` — Validation scoring
- All production skills — Patch targets

### SSOT Contracts
```yaml
required:
  - FRAMEWORK_CARD or FRAMEWORK_LIBRARY
  - TARGET_SKILL (or SKILL_MANIFEST for batch)

recommended:
  - EXISTING_PATCHES (to check conflicts)
  - GOLDEN_RUNS (for validation)

outputs:
  - UPGRADE_PATCH_CARD (single)
  - PATCH_BUNDLE (batch)
  - VALIDATION_REPORT (after testing)
```

---

## GOLDEN RUNS

### GR1: Single Framework → Single Skill Patch
```yaml
scenario: |
  "Reluctant Expert Open" framework extracted.
  Target: advertorial_copy_master_v2.0.0
  Generate deployment-ready patch.

input: 
  - FRAMEWORK_CARD: "FW-2026-001"
  - target_skill: "advertorial_copy_master_v2.0.0"

mode: Mode 1 (Single Patch)

expected_output:
  - Complete UPGRADE_PATCH_CARD
  - Proper XML payload
  - Insertion point specified
  - Rollback procedure included
  - Validation scenarios defined
```

### GR2: Framework Library → Batch Patches
```yaml
scenario: |
  Q1 framework library contains 15 patterns.
  Generate patches for all applicable skills.

input:
  - FRAMEWORK_LIBRARY: "LIB-2026-Q1"
  - SKILL_MANIFEST: all production skills

mode: Mode 2 (Batch Generation)

expected_output:
  - PATCH_BUNDLE with 20-30 patches
  - Dependency order defined
  - Rollout plan generated
  - No conflicts between patches
```

### GR3: Super Pattern Cross-Skill Rollout
```yaml
scenario: |
  "Proof Before Promise" identified as super pattern.
  Roll out across all copy skills.

input:
  - FRAMEWORK_CARD: "FW-2026-007" (super pattern)
  - SKILL_LIST: [advertorial, sales_page, vsl, email]

mode: Mode 3 (Cross-Skill)

expected_output:
  - 4 skill-specific patches
  - Adapted for each skill's structure
  - Coordinated rollout sequence
  - Unified validation plan
```

---

## FAILURE MODES

### FM1: Malformed XML Payload
```yaml
symptom: Patch breaks skill when applied
root_cause: Invalid XML in payload
recovery: Validate XML before output
prevention: XML schema validation step
```

### FM2: Wrong Insertion Point
```yaml
symptom: Patch content appears in wrong section
root_cause: Anchor element not found or ambiguous
recovery: More specific anchor identification
prevention: Verify anchor exists and is unique
```

### FM3: Version Mismatch
```yaml
symptom: Patch designed for old skill version
root_cause: Target skill updated since patch creation
recovery: Regenerate patch for new version
prevention: Version check before deployment
```

### FM4: Conflict with Manual Edits
```yaml
symptom: Patch overwrites custom modifications
root_cause: User manually edited target section
recovery: Merge manual edits with patch
prevention: Detect manual edits before deployment
```

---

## BUILD NOTES

### Token Budget (Estimated)
```
L1: 500 tokens (quick ref, patch types)
L2: 3000 tokens (modes, architecture, process)
L3: 2500 tokens (output formats, golden runs)
L4: 1500 tokens (integration, validation, failure modes)
TOTAL: ~7500 tokens
```

### Dependencies
- FRAMEWORK_CARD schema (from framework_extractor)
- PT Schema wrapper format
- XML validation capability
- Skill manifest access

### Build Sequence
1. Core identity + patch architecture
2. Four operating modes
3. Patch types + PT Schema wrapper
4. Output formats (PATCH_CARD, BUNDLE, VALIDATION)
5. Integration with framework_extractor + skill_builder
6. Golden runs + failure modes

---

*Spec created: 2026-01-01*
*Build priority: 10*
*Estimated build time: 3-4 hours*

---

**The Upgrade Patch Generator completes the self-improving loop — turning extracted intelligence into deployed capability.** 🔄
