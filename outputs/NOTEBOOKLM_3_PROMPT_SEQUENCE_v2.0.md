# NotebookLM 3-Prompt Sequence v2.0 — ULTRAMIND Knowledge Extraction

**Pipeline:** NotebookLM → GPT Stage-2 Synthesizer → Claude Code Skill Builder v1.2.0
**Status:** Production-ready
**Date:** 2026-01-18

---

## WORKFLOW OVERVIEW

```
Step 1: NotebookLM Prompt #1 → Compendium (source-grounded field manual)
    ↓
Step 2: NotebookLM Prompt #2 → Knowledge Base + Skill Input Pack
    ↓
Step 3: Send KB + Input Pack → GPT Stage-2 Synthesizer
    ↓
Step 4: GPT outputs → Skill Package Draft (canonical frameworks + heuristics)
    ↓
Step 5: Feed into Claude Code Skill Builder v1.2.0 → Production XML skill
    ↓
Step 6: Final pass → MMA validation + Human Persuasion Editor (if ad copy)
```

---

## NOTEBOOKLM SETUP (5 minutes)

1. **Create Notebook:** `[DOMAIN] — Knowledge Synthesis`
   - Example: "Facebook Ads — Knowledge Synthesis"
   - Example: "High-Ticket VSL — Knowledge Synthesis"

2. **Add Sources:**
   - Video transcripts (courses, trainings, masterclasses)
   - Written summaries/notes
   - Swipe files, example assets
   - Any supporting docs

3. **Add Instruction Note:** Create one source containing these 3 prompts

4. **Run in Sequence:**
   - First: Prompt #1 (Compendium Builder)
   - Second: Prompt #2 (KB + Skill Input Pack)
   - Third: Copy outputs and send to GPT Stage-2 Synthesizer

---

# PROMPT #1 — COMPENDIUM BUILDER (Source-Grounded Field Manual)

**Purpose:** Create comprehensive, source-tagged knowledge compendium
**Output:** Field manual ready for Stage-2 synthesis

---

```markdown
You are ULTRAMIND Knowledge Compendium Builder.

## MISSION
Extract grounded, source-tagged knowledge from all provided sources to create a canonical compendium for [DOMAIN].

## CRITICAL REQUIREMENTS

1. **Source Tagging (Non-Negotiable)**
   - Every framework, claim, or method MUST include: [SRC: <source_name> | <timestamp/page>]
   - If claim unsupported by sources: Mark as UNKNOWN
   - **Include direct short quotes (≤25 words) from sources for key principles**

2. **Proof Discipline**
   - Do not infer or guess
   - Ground everything in what was actually said/written
   - Quote directly when possible (≤25 words per quote)

3. **Action-Oriented**
   - Favor "how-to" over theory
   - Provide steps, decision rules, metrics
   - Include implementation details

4. **Structured for Synthesis**
   - Clear section headers
   - Consistent formatting
   - Ready for GPT Stage-2 Synthesizer

---

## OUTPUT STRUCTURE

### A. SOURCE MAP

List each source with:

```yaml
sources:
  - id: "[unique_id]"
    title: "[Full title]"
    author: "[Name/creator]"
    format: "[video/book/course/training]"
    duration: "[length if video/course]"
    primary_angle: "[Main perspective/lens used]"
    key_topics:
      - "[Topic 1]"
      - "[Topic 2]"
      - "[etc.]"
    credibility_notes: "[Credentials, results, social proof]"
    unique_contribution: "[What this source adds that others don't]"

  - id: "[source_2]"
    # ... repeat
```

**Total Sources:** [X]
**Total Duration/Pages:** [X hours or X pages]

---

### B. DOMAIN TAXONOMY (Map of Territory)

**What does this domain cover?**

```yaml
taxonomy:
  primary_categories:
    - category: "[Category 1]"
      subcategories: ["[Sub 1]", "[Sub 2]", "[Sub 3]"]

    - category: "[Category 2]"
      subcategories: ["[Sub 1]", "[Sub 2]"]

    # ... etc.

  cross_cutting_themes:
    - "[Theme 1 that appears across sources]"
    - "[Theme 2]"

  consensus_points:
    - "[What all sources agree on - point 1]"
    - "[Point 2]"

  divergence_points:
    - source_A: "[Belief X]"
      source_B: "[Contradicts with belief Y]"
      resolution: "[How to reconcile or choose]"

  knowledge_gaps:
    - "[Topic mentioned but not explained]"
    - "[Question raised but not answered]"
```

**Example for Facebook Ads:**
```yaml
primary_categories:
  - category: "Campaign Types"
    subcategories: ["ecom", "lead_gen", "local", "info_product", "webinar", "app"]
  - category: "Funnel Stages"
    subcategories: ["prospecting", "retargeting", "retention"]
  - category: "Ad Formats"
    subcategories: ["video", "image", "carousel", "UGC", "story", "reels"]
```

**Example for High-Ticket VSL:**
```yaml
primary_categories:
  - category: "Offer Types"
    subcategories: ["coaching", "consulting", "done_for_you", "certification"]
  - category: "Awareness Levels"
    subcategories: ["unaware", "problem_aware", "solution_aware", "product_aware"]
  - category: "VSL Formats"
    subcategories: ["talking_head", "slides", "hybrid", "animation"]
```

---

### C. CANONICAL FRAMEWORKS LIBRARY

**Extract 10-20 canonical frameworks** (step-by-step processes, models, blueprints)

For each framework:

```yaml
framework_name: "[Clear, Descriptive Name]"

source: "[SRC: source_id | timestamp/page]"

key_quote: "[Direct quote ≤25 words capturing core principle]"
# Example: "The first 3 seconds determine everything. Hook fails, everything else is irrelevant." [SRC: Sabri_VSL | 00:12:45]

summary: "[What problem this solves in 1-2 sentences]"

when_to_use:
  - "[Specific context 1]"
  - "[Specific context 2]"

when_NOT_to_use:
  - "[Context where this fails]"

steps:
  1. "[Specific, actionable step]"
     - inputs: "[What you need]"
     - output: "[What this produces]"
     - validation: "[How to check if done correctly]"

  2. "[Next step]"
     # ... etc.

key_metrics:
  - metric: "[Name]"
    benchmark: "[Expected range]"
    source: "[SRC: ...]"

common_failure_modes:
  - symptom: "[What goes wrong]"
    diagnosis: "[Why it happens]"
    fix: "[How to correct]"
    source: "[SRC: ...]"

examples:
  - context: "[Situation where used]"
    result: "[Outcome]"
    source: "[SRC: ...]"
```

**Example:**
```yaml
framework_name: "7-Day Campaign Launch Blueprint"

source: "[SRC: FB_Ads_Masterclass_2024 | 01:34:20]"

key_quote: "Never launch cold traffic without 7 days of warm-up data. You're flying blind otherwise." [SRC: FB_Ads_Masterclass_2024 | 01:34:35]

summary: "Structured 7-day launch sequence for new FB campaigns to gather data before scaling"

when_to_use:
  - "Launching new product with no pixel data"
  - "Testing new market/audience"
  - "Post-iOS14 attribution challenges"

when_NOT_to_use:
  - "Established campaigns with 30+ days data"
  - "Retargeting-only campaigns"

steps:
  1. "Day 1-3: Seed campaign at $50/day to 3 interest audiences"
     - inputs: "3 distinct audience hypotheses, creative variants"
     - output: "CTR, CPM, engagement data per audience"
     - validation: "At least 1000 impressions per ad set"

  2. "Day 4-5: Kill bottom 50% performers, double budget on winners"
     # ... etc.
```

---

### D. SOP PLAYBOOKS (Operational Procedures)

**Extract 10-15 SOPs** (recurring operational tasks)

For each SOP:

```yaml
sop_name: "[Clear Name]"

purpose: "[What problem this solves]"

frequency: "[daily/weekly/monthly/one-time]"

source: "[SRC: ...]"

key_quote: "[≤25 words]"

steps:
  1. "[Action]"
     - tool: "[Software/platform if applicable]"
     - duration: "[Estimated time]"
  2. "[Next action]"
     # ... etc.

quality_gates:
  - check: "[What to validate]"
    pass_criteria: "[What 'good' looks like]"

tools_required:
  - "[Tool 1]"
  - "[Tool 2]"

automation_potential: "[Can this be automated? How?]"
```

**Example SOPs for Facebook Ads:**
- Account setup + Business Manager hygiene
- Pixel/CAPI + event priority setup
- Naming conventions + UTM schema
- Campaign architecture templates (3-5 blueprints)
- Creative testing system (hooks → angles → variants)
- Budget allocation + scaling rules
- Daily optimization checklist
- Weekly performance review
- Creative iteration loop
- Retargeting logic + exclusion rules

**Example SOPs for High-Ticket VSL:**
- VSL script structure (10-part flow)
- Proof front-loading sequence
- Application funnel setup
- CTA optimization checklist
- Video production workflow
- A/B testing protocol
- Application → Call flow
- Show-up rate optimization
- Script iteration based on drop-off points

---

### E. DECISION HEURISTICS (IF-THEN RULES)

**Extract 25-50 decision rules**

Format: **IF** [condition/signal/context] **THEN** [action/priority/framework]

Group by category:

**Diagnostic Heuristics** (identifying problems):
```yaml
- IF: "[Observable signal]" THEN: "[Likely diagnosis]" [SRC: ...]
  QUOTE: "[Direct quote ≤25 words if available]"

# Example:
- IF: "CPA rises 20%+ but CTR stable" THEN: "Landing page or offer issue, not traffic quality" [SRC: FB_Ads_Bootcamp | 02:15:30]
  QUOTE: "When cost goes up but clicks don't drop, your ad is fine. The page is broken."
```

**Optimization Heuristics** (improving performance):
```yaml
- IF: "[Condition]" THEN: "[Optimization action]" [SRC: ...]
```

**Scaling Heuristics** (when/how to scale):
```yaml
- IF: "[Success metric threshold]" THEN: "[Scaling action]" [SRC: ...]
```

**Troubleshooting Heuristics** (fixing issues):
```yaml
- IF: "[Problem symptom]" THEN: "[Fix action]" [SRC: ...]
```

---

### F. METRICS + DIAGNOSTIC TABLES

**Benchmarks by Stage/Type** (if present in sources):

```yaml
benchmarks:
  - stage: "[Stage name - e.g., Prospecting]"
    metrics:
      - metric: "CTR"
        good: "[X-Y%]"
        acceptable: "[X-Y%]"
        poor: "[<X%]"
        source: "[SRC: ...]"

      - metric: "CPA"
        # ... etc.
```

**Symptom → Diagnosis → Fix Table:**

| Symptom | Likely Cause | Diagnostic Test | Fix | Source |
|---------|--------------|-----------------|-----|--------|
| [Observable issue] | [Root cause] | [How to confirm] | [Solution] | [SRC: ...] |

**Example:**
| Symptom | Likely Cause | Diagnostic Test | Fix | Source |
|---------|--------------|-----------------|-----|--------|
| High impressions, low clicks | Weak hook | Compare CTR across creative variants | Rewrite first 3 seconds, test 3 new hooks | [SRC: Creative_Testing | 00:45:12] |
| High clicks, no conversions | Offer/price misalignment | Check landing page exit rate + scroll depth | Test lower price point OR add guarantee | [SRC: Conversion_Opt | 01:22:33] |

---

### G. PATTERN LIBRARY (Tactical Patterns)

**Extract 15-25 tactical patterns**

For each pattern category:

**Hooks/Openers:**
```yaml
- pattern: "[Pattern name]"
  description: "[How it works]"
  structure: "[Template/formula]"
  example: "[Actual example from source]"
  context: "[When/where this was used]"
  result: "[Outcome if mentioned]"
  source: "[SRC: ...]"
  quote: "[≤25 words]"
```

**Pattern Categories:**
- Hooks/Openers (first 3-5 seconds/sentences)
- Authority Stacking (credibility establishment)
- Proof Structures (case studies, testimonials, data)
- Mechanism Reveals (how it works explanations)
- Offer Framing (value stack, pricing, guarantee)
- Objection Handling (pre-empting concerns)
- CTAs (call to action templates)
- Transitions (section bridges)
- Pattern Interrupts (scroll-stoppers)
- Identity Shifts ("people like you" positioning)

---

### H. FAILURE MODES + RECOVERIES

**Extract 15+ failure modes**

For each:

```yaml
failure_mode: "[Name of failure]"

symptoms:
  - "[Observable sign 1]"
  - "[Observable sign 2]"

root_cause: "[Why this happens]"

diagnosis_steps:
  1. "[How to confirm this is the issue]"
  2. "[Additional diagnostic check]"

recovery_actions:
  1. "[Immediate fix]"
  2. "[Long-term solution]"

prevention:
  - "[How to avoid in future]"

source: "[SRC: ...]"

quote: "[≤25 words if available]"
```

**Example:**
```yaml
failure_mode: "Audience Fatigue Death Spiral"

symptoms:
  - "CPM increases 30%+ over 7 days"
  - "CTR drops 20%+ from peak"
  - "Frequency >3.5 on prospecting"

root_cause: "Showing same creative to same people too many times, burning out engagement signals"

diagnosis_steps:
  1. "Check frequency metric in Ads Manager (should be <2.5 for prospecting)"
  2. "Compare CTR week-over-week (>15% drop = fatigued)"

recovery_actions:
  1. "IMMEDIATE: Pause ad set, rotate to fresh creative variant"
  2. "LONG-TERM: Implement creative rotation system (3-5 variants per campaign)"

prevention:
  - "Set frequency cap at 3.0"
  - "Rotate creatives every 5-7 days proactively"

source: "[SRC: FB_Scaling_Masterclass | 01:45:20]"

quote: "Once frequency hits 3, you're burning money. Fresh creative always beats optimization."
```

---

### I. GOLDEN RUN TEST CASES

**Extract 3-5 golden runs** (ideal scenarios to test skill against)

For each:

```yaml
golden_run_name: "[Descriptive name]"

scenario: "[Situation description]"

inputs:
  - "[Required input 1]"
  - "[Required input 2]"

expected_outputs:
  - "[What skill should produce]"
  - "[Quality criteria]"

success_criteria:
  - "[How to measure success]"
  - "[Acceptable ranges]"

source: "[SRC: ... if based on real example]"
```

**Example for Facebook Ads:**
```yaml
golden_run_name: "Cold Launch — Ecommerce Product ($50 AOV)"

scenario: "New ecommerce brand, no pixel data, $2k test budget, need to find winning audience + creative in 14 days"

inputs:
  - "Product: Ergonomic pillow, $49.99 AOV"
  - "Budget: $2000 total"
  - "Timeline: 14 days"
  - "Assets: 5 product videos, 10 lifestyle images"

expected_outputs:
  - "7-Day Launch Blueprint applied"
  - "3 audience hypotheses tested"
  - "Winner identified by Day 10"
  - "CPA <$35 by Day 14"

success_criteria:
  - "At least 1 profitable audience found (CPA <$35)"
  - "ROAS >1.5 on winning ad set"
  - "Minimum 50 purchases for pixel learning"

source: "[SRC: Ecom_Launch_Case_Study | 00:23:15]"
```

---

### J. COMPLIANCE & ETHICS

**Platform-Specific Rules:**
- Meta advertising policies
- FTC compliance (if applicable)
- Industry regulations
- Prohibited content/claims

**Safe Phrasing Patterns:**
- What to say instead of [risky claim]

**Red Flags to Avoid:**
- [Prohibited pattern 1]
- [Prohibited pattern 2]

**Sources:** [SRC: ...]

---

### K. IMPLEMENTATION CHECKLISTS

**Launch Checklist:**
- [ ] [Pre-launch task 1]
- [ ] [Pre-launch task 2]
- [ ] [etc.]

**Daily Operations:**
- [ ] [Daily task 1]
- [ ] [Daily task 2]

**Weekly Review:**
- [ ] [Weekly task 1]
- [ ] [Weekly task 2]

**Scaling Checklist:**
- [ ] [Scaling criteria 1]
- [ ] [Scaling criteria 2]

---

## FINAL OUTPUT

Deliver as **one comprehensive compendium document** with:
- ✅ All sections (A-K) populated
- ✅ Source tags on every framework/claim
- ✅ Direct quotes (≤25 words) for key principles
- ✅ 10-20 canonical frameworks
- ✅ 25-50 heuristics (IF-THEN format)
- ✅ 3-5 campaign/workflow blueprints
- ✅ Symptom → Diagnosis → Fix table
- ✅ 15+ failure modes with recoveries
- ✅ 3-5 golden run test cases
- ✅ Clear formatting for GPT Stage-2 Synthesizer

**Format:** Markdown with YAML blocks for structured data
```

---

# PROMPT #2 — KNOWLEDGE BASE + SKILL INPUT PACK

**Purpose:** Transform Compendium into structured KB + Skill Spec for GPT Stage-2 Synthesizer
**Run AFTER:** Prompt #1 (Compendium Builder) completes

---

```markdown
You are ULTRAMIND Knowledge Base Packager.

## MISSION
Using the Compendium you just created (Prompt #1 output), generate two deliverables:

1. **Knowledge Base v1.1** (canonical knowledge for skill)
2. **Skill Input Pack** (instructions for GPT Stage-2 Synthesizer)

---

## DELIVERABLE 1: KNOWLEDGE BASE v1.1

Extract and compress the Compendium into canonical knowledge structure:

```yaml
# ULTRAMIND KNOWLEDGE BASE v1.1
# Domain: [DOMAIN]
# Sources: [X sources]
# Date: [YYYY-MM-DD]

meta_topic: "[Domain name - e.g., Facebook Ads Campaign Optimization]"

## 1. CORE THESIS

core_thesis:
  primary_thesis: "[1-2 sentence synthesis of common truth across sources]"

  big_promises:
    - "[Measurable outcome 1]"
    - "[Measurable outcome 2]"
    - "[Measurable outcome 3]"

  underlying_assumptions:
    - "[Unstated belief 1 driving the frameworks]"
    - "[Unstated belief 2]"
    - "[Unstated belief 3]"

  sources: "[SRC: ... | SRC: ... | SRC: ...]"

## 2. CANONICAL MECHANISMS (How Things Really Work)

mechanisms:
  - name: "[Mechanism 1 - Canonical Name]"
    explanation: "[What it explains + why it matters]"
    signals:
      - "[Observable sign this mechanism is active]"
      - "[Observable sign 2]"
    decision_impact: "[How knowing this changes what you do]"
    sources: "[SRC: ...]"
    key_quote: "[≤25 words]"

  - name: "[Mechanism 2]"
    # ... 3-7 total mechanisms
```

**Extraction Rules for Mechanisms:**
- Limit to 3-7 canonical mechanisms
- Merge similar mechanisms with different names
- Focus on "how the system really works"
- Each must change HOW you diagnose or act

```yaml
## 3. CANONICAL FRAMEWORKS (Step-by-Step Processes)

frameworks:
  - name: "[Framework 1]"
    summary: "[Problem this solves in 1 sentence]"
    when_to_use: "[Specific context]"
    steps:
      1: "[Actionable step with inputs/outputs]"
      2: "[Next step]"
      # ... clear sequence
    inputs_required: ["[Input 1]", "[Input 2]"]
    expected_outputs: ["[Output 1]", "[Output 2]"]
    key_metrics:
      - metric: "[Name]"
        benchmark: "[Range]"
    sources: "[SRC: ...]"
    key_quote: "[≤25 words]"

  - name: "[Framework 2]"
    # ... 10-20 total frameworks
```

**Extraction Rules for Frameworks:**
- Extract 10-20 canonical frameworks (not all from Compendium, prioritize highest-impact)
- Merge redundant frameworks
- Each must be immediately actionable
- Include when_to_use decision criteria

```yaml
## 4. DECISION HEURISTICS (IF-THEN Rules)

heuristics:
  diagnostic:
    - "IF [signal] THEN [diagnosis]"
    - "IF [signal] THEN [diagnosis]"

  optimization:
    - "IF [condition] THEN [action]"
    - "IF [condition] THEN [action]"

  scaling:
    - "IF [threshold] THEN [scaling action]"

  troubleshooting:
    - "IF [symptom] THEN [fix]"

  # ... 25-50 total heuristics
```

**Extraction Rules:**
- 25-50 total heuristics (prioritize most actionable)
- Group by category
- IF-THEN format only
- Resolve conflicts with conditional pairs

```yaml
## 5. ANTI-PATTERNS (What NOT to Do)

anti_patterns:
  - label: "[Short mistake name]"
    description: "[What people do wrong]"
    why_harmful: "[Consequences]"
    instead_do: "[Correct approach]"
    sources: "[SRC: ...]"
    quote: "[≤25 words if available]"

  # ... 3-7 total anti-patterns
```

```yaml
## 6. FAILURE MODES + RECOVERIES

failure_modes:
  - name: "[Failure mode name]"
    symptoms: ["[Sign 1]", "[Sign 2]"]
    root_cause: "[Why this happens]"
    diagnosis_steps: ["[Step 1]", "[Step 2]"]
    recovery_actions: ["[Fix 1]", "[Fix 2]"]
    prevention: ["[How to avoid]"]
    sources: "[SRC: ...]"

  # ... 15+ total failure modes
```

```yaml
## 7. GOLDEN RUN TEST CASES

golden_runs:
  - name: "[Test case name]"
    scenario: "[Situation]"
    inputs: ["[Input 1]", "[Input 2]"]
    expected_outputs: ["[Output 1]"]
    success_criteria: ["[Criteria 1]"]
    source: "[SRC: ... if applicable]"

  # ... 3-5 total golden runs
```

```yaml
## 8. AGENT BEHAVIOR RULES

agent_behavior_rules:
  - "ALWAYS [behavior] when [context]"
  - "NEVER [behavior] unless [exception]"
  - "When [situation], prioritize [action] over [alternative]"

  # ... 5-10 operational rules
```

```yaml
## 9. HUMANIZING ELEMENTS

humanizing_elements:
  metaphors:
    - "[Key metaphor from sources]"

  story_arc: "[Common narrative pattern - e.g., struggle → insight → breakthrough]"

  values:
    - "[Core value 1]"
    - "[Core value 2]"

  sources: "[SRC: ...]"
```

```yaml
## 10. COMPLIANCE & ETHICS

compliance:
  platform_rules:
    - "[Meta policy 1]"
    - "[Platform rule 2]"

  safe_phrasing:
    - avoid: "[Risky claim]"
      use_instead: "[Safe alternative]"

  red_flags:
    - "[Prohibited pattern 1]"

  sources: "[SRC: ...]"
```

---

## DELIVERABLE 2: SKILL INPUT PACK

Create instructions for GPT Stage-2 Synthesizer:

```markdown
# SKILL INPUT PACK — [DOMAIN]

## FOR: GPT Stage-2 Synthesizer

## KNOWLEDGE BASE
[Paste the entire Knowledge Base v1.1 YAML from above]

---

## SKILL SPECIFICATION

skill_name: "[Domain] Master"
skill_version: "v1.0.0"
skill_category: "[Category - e.g., marketing/sales/product/operations]"

skill_purpose: |
  [1-2 sentence description of what this skill enables]

target_users:
  - "[User type 1]"
  - "[User type 2]"

use_cases:
  - use_case: "[Use case 1]"
    input: "[What user provides]"
    output: "[What skill produces]"

  - use_case: "[Use case 2]"
    # ... 3-5 total use cases

ssot_objects_required:
  - PROJECT_BRIEF (if applicable)
  - EVIDENCE_PACK (if applicable)
  - [Other SSOT objects if needed]

progressive_disclosure_layers:
  L1: |
    [Core identity, purpose, and high-level workflow]

  L2: |
    [Canonical frameworks library, decision heuristics]

  L3: |
    [Detailed SOPs, failure modes, recovery procedures]

  L4: |
    [Implementation examples, edge cases, advanced patterns]

two_brain_pod_architecture:
  left_brain_technical:
    - "[Technical/structural responsibility 1]"
    - "[Technical responsibility 2]"

  right_brain_strategic:
    - "[Strategic/experiential responsibility 1]"
    - "[Strategic responsibility 2]"

ecr_integration:
  learning_phase:
    - "[What skill learns from execution]"

  repair_phase:
    - "[What triggers self-improvement]"

mma_validation:
  critical_dimensions:
    - "[Dimension 1 that must pass]"
    - "[Dimension 2]"

  pass_criteria: |
    [Overall quality threshold]

golden_runs: |
  [Reference the 3-5 golden run test cases from Knowledge Base]

failure_modes: |
  [Reference the 15+ failure modes from Knowledge Base]

---

## INSTRUCTIONS FOR GPT STAGE-2 SYNTHESIZER

1. Use the Knowledge Base above as canonical truth
2. Generate XML skill following ULTRAMIND Skill Builder v1.2.0 format
3. Ensure all frameworks are source-grounded
4. Include progressive disclosure (L1-L4)
5. Implement Two-Brain Pod architecture
6. Add ECR self-improvement hooks
7. Integrate MMA validation gates
8. Include golden runs + failure modes
9. Output production-ready XML skill

---

## VALIDATION CHECKLIST

Before sending to Claude Code Skill Builder v1.2.0, verify:

- [ ] Knowledge Base has all 10 sections
- [ ] 10-20 canonical frameworks extracted
- [ ] 25-50 heuristics in IF-THEN format
- [ ] 15+ failure modes with recoveries
- [ ] 3-5 golden run test cases
- [ ] All claims source-tagged
- [ ] Key quotes included (≤25 words)
- [ ] Skill Input Pack complete
- [ ] Use cases defined (3-5)
- [ ] Progressive disclosure layers specified
```

---

## OUTPUT

Deliver TWO files:

1. **[domain]_knowledge_base_v1.1.yaml**
2. **[domain]_skill_input_pack.md**

These will be sent to GPT Stage-2 Synthesizer.
```

---

# PROMPT #3 — OPTIONAL PATTERN INTEGRATION

**Purpose:** Extract tactical patterns in ULTRAMIND p_XXX format for pattern library
**Run:** Only if you want to integrate tactical patterns into existing library
**Note:** This is OPTIONAL - main workflow is Compendium → KB + Input Pack → GPT → Claude

---

```markdown
You are ULTRAMIND Pattern Integration Specialist.

## MISSION
Extract tactical PATTERNS from the Compendium (Prompt #1) and format for ULTRAMIND pattern library (p_087-p_113 format).

## INPUT
The Compendium created in Prompt #1

## OUTPUT
Tactical patterns ready for `insights.md` integration

---

## PATTERN EXTRACTION FORMAT

For each tactical pattern:

```yaml
pattern_id: "p_[XXX]"  # Next available ID (check current max in pattern library)
pattern_name: "[Clear, Descriptive Name]"
category: "[hook/authority/mechanism/offer/objection/identity/transition/etc.]"

when_to_use: "[Specific contexts where effective]"

when_NOT_to_use: "[Contexts where fails or inappropriate]"

structure: |
  [Describe pattern template/formula]

examples:
  - example_1:
      source: "[SRC: ...]"
      text: "[Actual example from source with quote]"
      context: "[Where/when used]"
      result: "[Outcome if mentioned]"

  - example_2:
      source: "[SRC: ...]"
      text: "[Another example]"
      context: "[Context]"

mma_impact:
  SMART: "[+X.X predicted impact]"
  SAFE: "[+X.X]"
  SPECIAL: "[+X.X]"
  SIGNIFICANT: "[+X.X]"
  SUPPORTED: "[+X.X]"
  SUPERIOR: "[+X.X]"
  STEAL: "[+X.X]"

voice_compatibility:
  - "[Voice type 1 - e.g., irreverent, formal, empathetic, authoritative]"
  - "[Voice type 2]"

funnel_types:
  - "[Domain/funnel where effective - e.g., fb_ads, vsl, sales_page, email]"

effectiveness_rating: [X.X/10]

date_discovered: "[YYYY-MM-DD]"
```

---

## EXTRACTION TARGETS

Extract patterns for:

1. **Hooks/Openers** (first 3-5 seconds/sentences)
2. **Authority Stacking** (credibility establishment)
3. **Proof Structures** (case studies, testimonials, data)
4. **Mechanism Reveals** (how it works explanations)
5. **Offer Framing** (value stack, pricing, guarantee)
6. **Objection Handling** (pre-empting concerns)
7. **CTAs** (call to action templates)
8. **Transitions** (section bridges)
9. **Pattern Interrupts** (scroll-stoppers)
10. **Identity Shifts** ("people like you" positioning)

---

## VALIDATION RULES

For each pattern:
- [ ] Has 2+ real examples from sources
- [ ] Clear when_to_use criteria
- [ ] Clear when_NOT_to_use criteria
- [ ] MMA impact estimated
- [ ] Voice compatibility specified
- [ ] Funnel/domain compatibility specified
- [ ] Effectiveness rating justified
- [ ] Source-grounded (not invented)

---

## OUTPUT

List of 10-20 tactical patterns in YAML format, ready for insertion into `insights.md` pattern library.
```

---

## USAGE INSTRUCTIONS

### Step 1: Run Prompt #1 (Compendium Builder)
- Upload all sources to NotebookLM
- Paste Prompt #1
- Wait for complete compendium output
- Save as `[domain]_compendium.md`

### Step 2: Run Prompt #2 (KB + Skill Input Pack)
- With Compendium completed, paste Prompt #2
- Wait for both deliverables:
  - Knowledge Base v1.1 (YAML)
  - Skill Input Pack (Markdown)
- Save as separate files

### Step 3: Send to GPT Stage-2 Synthesizer
- Copy Knowledge Base + Skill Input Pack
- Send to your GPT Stage-2 Synthesizer
- GPT outputs: Skill Package Draft

### Step 4: Feed to Claude Code Skill Builder v1.2.0
- Paste Skill Package Draft into Claude Code
- Claude generates:
  - Production XML skill
  - Progressive disclosure (L1-L4)
  - Golden runs
  - Failure modes
  - MMA integration

### Step 5: Final Pass (Optional)
- MMA validation
- Human Persuasion Editor (if ad copy/resonance-critical)

### Step 6 (Optional): Run Prompt #3
- If you want tactical patterns for pattern library
- Paste Prompt #3
- Integrate outputs into `insights.md`

---

## VALIDATION CHECKLIST (Before sending to GPT)

From NotebookLM outputs, verify:

- [ ] ✅ 10-20 canonical frameworks extracted
- [ ] ✅ 25-50 heuristics in IF-THEN format
- [ ] ✅ 3-5 campaign/workflow blueprints
- [ ] ✅ Symptom → Diagnosis → Fix table populated
- [ ] ✅ 15+ failure modes with recoveries
- [ ] ✅ 3-5 golden run test cases
- [ ] ✅ All frameworks source-tagged [SRC: ...]
- [ ] ✅ Direct quotes included (≤25 words) for key principles
- [ ] ✅ Knowledge Base v1.1 has all 10 sections
- [ ] ✅ Skill Input Pack specifies use cases, progressive disclosure, Two-Brain Pod

---

## EXPECTED OUTPUTS

**From NotebookLM:**
1. `[domain]_compendium.md` (10-20 pages, comprehensive)
2. `[domain]_knowledge_base_v1.1.yaml` (canonical compressed KB)
3. `[domain]_skill_input_pack.md` (instructions for GPT)
4. `[domain]_patterns.yaml` (optional, if Prompt #3 run)

**From GPT Stage-2 Synthesizer:**
5. `[domain]_skill_package_draft.md` (synthesis ready for Claude)

**From Claude Code Skill Builder v1.2.0:**
6. `[domain]_master_v1.0.0.xml` (production XML skill)
7. Golden runs tested
8. Failure modes documented
9. MMA validation integrated

---

**Status:** Production-ready
**Version:** 2.0
**Compatible with:** ULTRAMIND Skill Builder v1.2.0
**Pipeline:** NotebookLM → GPT → Claude Code

---
