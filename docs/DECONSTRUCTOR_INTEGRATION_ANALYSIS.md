# SALES PAGE DECONSTRUCTOR — Integration Analysis
**Date:** 2026-01-11
**Purpose:** Merge existing 79KB Deconstructor SKILL with orchestration-aligned spec

---

## 🎯 OBJECTIVE

Create a unified **Sales Page Deconstructor Analyst v1.0.0** XML skill that:
1. Preserves all 7 operating modes from existing SKILL
2. Integrates with ZPWO Phase 4 (Learning) orchestration
3. Adds pattern extraction → library updates → patch proposals
4. Maintains both FULL and LITE modes for flexibility
5. Aligns with Strategic Copy Director 7S/7F and Neuro-Box 6D frameworks

---

## 📊 EXISTING DECONSTRUCTOR ANALYSIS

### What Exists (79KB SKILL.md)

**7 Operating Modes:**
1. **Quick Audit** — 10-20 bullets, top fixes, framework ID (DM/consultation use)
2. **Deep Deconstruction** — Full analysis, section-by-section, mechanism mapping
3. **Comparative Analysis** — Current vs. competitor/benchmark
4. **Framework Extraction** — Blueprint templates for reuse
5. **Revision Roadmap** — Keep/Improve/Replace/Add with priorities
6. **Skill Feedback** — Pattern observations for skill improvements
7. **Rewrite Brief Generation** — Complete rebuild briefs (7A/7B/7C sub-modes)

**Core Strengths:**
- ✅ Comprehensive analysis frameworks (10 sections)
- ✅ Proof/credibility/compliance mapping
- ✅ Drop-off hypothesis generation
- ✅ Testing recommendations with A/B structures
- ✅ Framework extraction templates (e.g., "2 AM Revelation")
- ✅ Value stack + CTA analysis
- ✅ Avatar/emotion/messaging deep-dive
- ✅ Compliance risk assessment by platform

**Analysis Frameworks (Sections 4-10):**
- Section 4: Structure + Flow Mapping
- Section 5: Avatar, Emotion & Messaging
- Section 6: Proof, Credibility & Compliance
- Section 7: Offer, Value Stack & CTA
- Section 8: Drop-Off Hypotheses & Friction Points
- Section 9: Revision Roadmap (KEEP/IMPROVE/REPLACE/ADD)
- Section 10: Framework Extraction & Template

---

## 🆕 NEW ORCHESTRATION SPEC (From Phase 4 Design)

### What's New:

**Phase 4 Integration:**
- ZPWO activates Deconstructor post-deployment
- Pattern Library updates (new patterns discovered)
- Patch Proposal generation (skill improvements)
- Human approval checkpoints
- TWE applies approved patches
- Improvement validation (before/after MMA scoring)

**7 Extraction Frameworks:**
1. Structure Extraction
2. Mechanism Analysis
3. Offer Deconstruction
4. Voice Signature
5. 7S/7F Coverage Audit
6. Pattern Recognition
7. Patch Proposal Generation

**Integration with 5-Pillar Architecture:**
- **ZPWO:** Triggers P4 learning phase
- **TWA:** Routes high/low performers to Deconstructor
- **TWE:** Receives and applies patch proposals
- **MMA:** Provides quality scores as input
- **Skills:** Updated via approved patches

---

## 🔗 INTEGRATION STRATEGY

### Option A: Full Merge (Recommended)

**Create Single Skill with Dual Modes:**

```xml
<Skill skill_id="skill.sales_page_deconstructor_analyst.v1_0_0">

  <!-- Mode Selection -->
  <Modes>
    <Mode1>Quick Audit (LITE)</Mode1>
    <Mode2>Deep Deconstruction (FULL)</Mode2>
    <Mode3>Comparative Analysis</Mode3>
    <Mode4>Framework Extraction</Mode4>
    <Mode5>Revision Roadmap</Mode5>
    <Mode6>Skill Feedback</Mode6>
    <Mode7>Rewrite Brief Generation (7A/7B/7C)</Mode7>
    <Mode8>Learning Loop (NEW - P4 Integration)</Mode8>
  </Modes>

  <!-- L1: Core Identity + Mode Router -->
  <!-- L2: Analysis Frameworks (10 sections) -->
  <!-- L3: Pattern Extraction + Patch Generation -->
  <!-- L4: Templates + Examples -->

</Skill>
```

**Benefits:**
- All analysis capabilities in one place
- ZPWO can activate any mode via parameters
- Maintains existing functionality
- Adds orchestration learning loop

**Challenges:**
- Large skill file (will exceed current sizes)
- Need strict token budgeting per layer

---

### Option B: Split Skill Family

**Create 2 Skills:**

1. **Sales Page Deconstructor (Analyst)** — Modes 1-5 + 8
   - Quick Audit, Deep Analysis, Comparative, Framework Extraction, Revision
   - Pattern Library integration
   - ~40KB XML

2. **Sales Page Deconstructor (Architect)** — Modes 6-7
   - Skill Feedback
   - Rewrite Brief Generation (7A/7B/7C)
   - Patch Proposal system
   - ~30KB XML

**Benefits:**
- Cleaner separation of concerns
- Smaller individual skills
- Easier to activate specific capabilities

**Challenges:**
- ZPWO needs to know which to activate when
- Potential duplication of frameworks

---

### Option C: LITE + FULL Versions (Like Copywriter)

**Create 2 Versions:**

1. **Sales Page Deconstructor LITE v1.0.0**
   - Mode 1: Quick Audit only
   - Mode 4: Framework Extraction
   - Mode 8: Learning Loop (basic pattern recognition)
   - Target: ~15KB XML
   - Use case: Fast analysis, DM audits, initial scans

2. **Sales Page Deconstructor FULL v1.0.0**
   - All 8 modes
   - Complete analysis frameworks
   - Full pattern extraction
   - Patch proposal generation
   - Target: ~60-70KB XML
   - Use case: Deep analysis, major revisions, template extraction

**Benefits:**
- Follows existing pattern (sales_page_copywriter_lite vs. full)
- Speed option for common use cases
- Complete option for deep work
- Easier token management

**Challenges:**
- Need to maintain both
- Some duplication

---

## 🎯 RECOMMENDATION: Option C (LITE + FULL)

**Rationale:**
- Matches existing architecture pattern
- Provides speed option for high-frequency use (quick audits, DM outreach)
- Preserves all capability in FULL version
- Easier for ZPWO to route (LITE for P4 quick scans, FULL for deep learning)

---

## 📐 PROPOSED STRUCTURE

### LITE Version Structure:

```xml
<Skill skill_id="skill.sales_page_deconstructor_lite.v1_0_0">

  <L1_core_identity> (≤600 tokens)
    - Identity: Master analyst, framework extractor
    - Prime directive: First do no harm
    - Operating modes: Quick Audit (M1), Framework Extraction (M4), Learning Loop (M8)
    - Non-negotiables
  </L1_core_identity>

  <L2_quick_audit_framework> (≤4000 tokens)
    - 10-20 bullet format
    - Strengths/weaknesses scanner
    - Priority fixes ranker
    - Framework identifier
    - Test suggestions
  </L2_quick_audit_framework>

  <L3_pattern_recognition> (≤3000 tokens)
    - Pattern Library matching
    - New pattern detection
    - Anti-pattern flagging
    - Basic patch proposals
  </L3_pattern_recognition>

  <L4_outputs_examples> (≤2000 tokens)
    - Quick Audit output template
    - Pattern extraction format
    - Patch proposal format
    - Golden runs (3 scenarios)
  </L4_outputs_examples>

  Total Target: ~10,000 tokens (~40KB XML)
</Skill>
```

---

### FULL Version Structure:

```xml
<Skill skill_id="skill.sales_page_deconstructor_analyst.v1_0_0">

  <L1_core_identity> (≤800 tokens)
    - Full identity + philosophy
    - All 8 operating modes
    - Mode selection logic
    - Integration points (ZPWO/TWA/TWE/MMA)
  </L1_core_identity>

  <L2_analysis_frameworks> (≤8000 tokens)
    - Structure + Flow Mapping
    - Avatar, Emotion & Messaging
    - Proof, Credibility & Compliance
    - Offer, Value Stack & CTA
    - Drop-Off Hypotheses & Friction Points
    - 7S/7F Coverage Audit
    - Mechanism Analysis (UMP/UMS)
  </L2_analysis_frameworks>

  <L3_pattern_extraction_patches> (≤6000 tokens)
    - Framework Extraction (Mode 4)
    - Pattern Library integration
    - Patch Proposal Generation (Mode 6 + M8)
    - Skill feedback system
    - Testing recommendation engine
  </L3_pattern_extraction_patches>

  <L4_rewrite_brief_generation> (≤4000 tokens)
    - Mode 7A: Complete Rewrite
    - Mode 7B: New Angle Test
    - Mode 7C: Template Application
    - Section-by-section brief templates
    - Success criteria checklists
  </L4_rewrite_brief_generation>

  <L5_templates_examples> (≤3000 tokens)
    - Framework templates (e.g., "2 AM Revelation")
    - Golden runs (5 scenarios)
    - Revision roadmap examples
    - Comparative analysis examples
  </L5_templates_examples>

  Total Target: ~22,000 tokens (~85KB XML)
</Skill>
```

---

## 🔄 ORCHESTRATION INTEGRATION POINTS

### ZPWO Activation Patterns:

**Phase 4 (Learning) — LITE Version:**
```
ZPWO → TWA routes → Deconstructor LITE (M8: Learning Loop)
Input: Completed asset + MMA scores
Output: Pattern extraction + basic patch proposals
Duration: 2-3 minutes
```

**Deep Analysis — FULL Version:**
```
ZPWO → TWA routes → Deconstructor FULL (M2: Deep Deconstruction)
Input: Asset + performance data + context
Output: Complete analysis + framework extraction + patch proposals
Duration: 10-15 minutes
```

**Competitor Research — FULL Version:**
```
User request → TWA routes → Deconstructor FULL (M3: Comparative Analysis)
Input: Your page + competitor page
Output: Gap analysis + framework extraction
Duration: 8-12 minutes
```

---

### Integration with Other Pillars:

**TWA (Router):**
- High-performing asset (MMA ≥8.5) → Deconstructor LITE (quick pattern extraction)
- Underperforming asset (MMA <7.0) → Deconstructor FULL (deep diagnosis)
- A/B test complete → Deconstructor FULL (comparative analysis)

**TWE (Tools Engineer):**
- Receives patch proposals from Deconstructor
- Applies approved patches to skills
- Versions skills (v[X] → v[X+1])

**MMA (Quality Monitor):**
- Provides scores as input for analysis
- Validates improvements after patch application

**Skills (Production):**
- Receive updates via TWE
- Improve over time based on Deconstructor learnings

---

## 🎨 NEW MODE 8: LEARNING LOOP SPECIFICATION

### Mode 8 Inputs:
- Completed asset (advertorial, sales page, email, VSL)
- MMA scores (7D validation results)
- Performance data (optional: CVR, CTR, engagement)
- Asset metadata (avatar, mechanism, offer type)

### Mode 8 Outputs:

**1. PATTERN_LIBRARY_UPDATE**
```yaml
patterns_discovered:
  - pattern_id: P087
    name: "Reversed System Framework"
    description: "Your system isn't broken, it's running backwards"
    effectiveness: 9.5/10
    context: "Mechanism explanation in advertorials"
    example: "Cortisol rhythm reversed - high at night, low in morning"

  - pattern_id: P088
    name: "Failed Alternative as Proof"
    description: "Validate why X failed → Proves Y is the answer"
    effectiveness: 8.8/10
    context: "Objection handling, paradigm shift"
    example: "Sleep hygiene can't work if cortisol blocks melatonin"

confirmed_patterns:
  - pattern_id: P042
    frequency_increased: 5 → 6
    effectiveness_confirmed: 8.9/10
```

**2. PATCH_PROPOSALS**
```yaml
patches:
  - patch_id: PATCH_027
    priority: HIGH
    target_skill: advertorial_copy_master
    target_section: L3_mechanism_intro
    description: "Add 'Reversed System Framework' template"
    rationale: "Used in high-performing angle (9.5/10), creates strong 'aha' moment"
    implementation:
      add_template: |
        "Your [system] isn't broken, it's running [backwards/upside-down].
        [Normal state] → [Reversed state] → [Consequence]"
    estimated_effort: 30 minutes

  - patch_id: PATCH_028
    priority: MEDIUM
    target_skill: advertorial_copy_master
    target_section: L3_offer_templates
    description: "Strengthen SUPERIOR dimension (belonging language)"
    rationale: "7S audit showed SUPERIOR at 6.9/10 (below threshold)"
    implementation:
      add_examples: ["You're not alone in this", "Join thousands who've...", "Welcome to the..."]
    estimated_effort: 20 minutes
```

**3. DECONSTRUCTION_REPORT** (summary for human review)
- Asset performance summary
- 7S/7F coverage scores
- New patterns discovered
- Patch recommendations
- Next steps

---

## ✅ NEXT STEPS

### Build Order (Recommended):

**Step 1: Build LITE Version (Priority 1)**
- Faster to build (~2-3 hours)
- Immediate value for P4 learning loops
- Test orchestration integration
- File: `sales_page_deconstructor_lite_v1.0.0.xml`

**Step 2: Build FULL Version (Priority 2)**
- Complete all 8 modes
- Integrate all existing frameworks from SKILL.md
- Add Mode 8 (Learning Loop)
- File: `sales_page_deconstructor_analyst_v1.0.0.xml`

**Step 3: Build Pattern Library Manager (Priority 3)**
- YAML/JSON storage for patterns
- Version control
- Pattern matching engine
- File: `pattern_library_manager.py` (Python tool)

**Step 4: Test Complete Learning Cycle (Priority 4)**
- Run P1 → P2 → P3 → P4 workflow
- Validate pattern extraction
- Test patch application
- Measure improvement

---

## 📦 FILES TO CREATE

### Skills:
1. `.claude/skills/copy/sales_page_deconstructor_lite_v1.0.0.xml` (~40KB)
2. `.claude/skills/copy/sales_page_deconstructor_analyst_v1.0.0.xml` (~85KB)

### Supporting Tools:
3. `tools/pattern_library_manager.py` (pattern storage/matching)
4. `tools/patch_applicator.py` (skill update automation)

### Documentation:
5. `docs/skills/SALES_PAGE_DECONSTRUCTOR_USAGE_GUIDE.md` (how to use all modes)
6. `docs/patterns/PATTERN_LIBRARY_v1.0.yaml` (validated patterns storage)

---

## 💡 KEY INSIGHTS

### What Makes This Integration Powerful:

1. **Preserves Existing Work:** All 79KB of analysis frameworks retained
2. **Adds Learning Loop:** Closes self-healing architecture
3. **Flexible Activation:** LITE for speed, FULL for depth
4. **Pattern Compounding:** Each success improves future runs
5. **Human-in-Loop:** All patches require approval (quality control)
6. **Measurable Improvement:** MMA before/after comparison

### Integration with Your Discovery:

> "Initial sales pages came out very nice when we gave comprehensive research."

**The Loop:**
1. Comprehensive research → "Very nice" page
2. Deconstructor extracts what worked (patterns)
3. Patterns added to library
4. Future pages benefit WITHOUT comprehensive research every time
5. System compounds learning

---

## 🎯 READY TO BUILD

**Recommendation:** Start with LITE version (Step 1)

**Why:**
- Quick build (2-3 hours)
- Tests orchestration integration
- Immediate value for learning loops
- Can build FULL version while LITE is being tested

**Shall I proceed to build the Sales Page Deconstructor LITE v1.0.0 XML?**
