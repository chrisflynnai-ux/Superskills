# ZPWO ORCHESTRATION TEST SESSION

**Date:** 2026-01-11
**Objective:** Load ZPWO, map routing, understand orchestration architecture
**Status:** In Progress

---

## ✅ ZPWO LOADED SUCCESSFULLY

**File:** `.claude/skills/meta/zpwo_v1_0_0_updated.xml`
**Version:** 1.0.0
**Status:** Active
**Created:** 2026-01-06
**Model:** Sonnet

---

## 🎯 CORE ORCHESTRATION PRINCIPLES

### Prime Directive (Line 185-188)
> "Coordinate production across 3 phases using locked SSOT, tool-first state, Two-Brain Pod teams, and self-healing loops—keeping the Zero-Point light while sub-agents handle heavy execution at the edges."

### Core Belief (Line 191-194)
> "The orchestrator that tries to do everything does nothing well. ZPWO routes, tracks, and validates—it does not generate content. Generation happens at the edges through specialized skills."

### Non-Negotiables (Lines 224-230)
1. ❌ Never generate content directly—route to specialized skills
2. ❌ Never allow SSOT drift—objects are locked after Stage A
3. ❌ Never exceed 3 FIX loops for same MMA dimension—escalate to human
4. ❌ Never bloat context—garbage collect at phase transitions
5. ✅ Always track state—SESSION_STATE is truth, chat is ephemeral
6. ✅ Always run MMA validation before phase transitions

---

## 📊 ROUTING TABLE MAPPED

### Command → Skill → Model Routing (Lines 259-270)

| Command | Skill | Model | File Location |
|---------|-------|-------|---------------|
| `/advertorial` | advertorial_copy_master | opus | `.claude/skills/copy/advertorial_copy_master_v2.0.0.xml` |
| `/salespage` | sales_page_copywriter | opus | `.claude/skills/copy/sales_page_copywriter_*.xml` |
| `/salespage-lite` | sales_page_copywriter_lite | sonnet | `.claude/skills/copy/sales_page_copywriter_lite_v2.0.0.xml` |
| `/vsl` | vsl_script_writer_long_form | opus | `.claude/skills/copy/long_form_vsl_script_architect_v2.0.xml` |
| `/email` | email_campaign_copy_genius | opus | `.claude/skills/email/KB-EMAIL-*.xml` |
| `/infoproduct` | quick_info_product_builder_lite | sonnet | `.claude/skills/product/*.xml` |
| `/design` | strategic_design_master | opus | `.claude/skills/design/strategic_design_master_v1.0.0.xml` |
| `/deconstruct` | sales_page_deconstructor | opus | (needs verification) |
| `/polish` | human_persuasion_editor | opus | (needs verification) |
| `/copy-check` | sales_copy_consistency_contract | sonnet | (needs verification) |

### Meta Commands (Lines 240-248)

| Command | Purpose | Phase |
|---------|---------|-------|
| `/intake` | Initialize project, lock SSOT | Stage 0-2 |
| `/draft` | Fast exploration (P1) | Draft |
| `/produce` | Looped refinement (P2) | Production |
| `/polish` | Voice + UX finish (P3) | Polish |
| `/validate` | MMA quality check | Any |
| `/ship` | Package deliverables | Final |
| `/status` | Display workflow state | Any |
| `/handoff` | Session summary | Any |
| `/gc` | Garbage collection | Any |

---

## 🔄 3-PHASE WORKFLOW LOGIC

### PHASE 1: DRAFT (P1) — Filter & Frame
**Lines 565-606**

**Goal:** Generate 3-10 viable angles/approaches quickly
**Mode:** Creative, experimental, low-validation
**Tools:** Minimal (don't over-validate early ideas)
**Exit Criteria:** Strategy-aligned angles ready for Production

**Two-Brain Pod (P1):**
```
LEFT BRAIN (Technical):
├── Schema Guardian: SSOT compliance
└── Routing Planner: Skill selection

RIGHT BRAIN (Strategic):
├── Angle Finder: Hook/theme generation
└── Story Architect: Narrative frames
```

**Workflow:**
1. Load PROJECT_BRIEF + MESSAGE_SPINE (locked)
2. Route to appropriate Draft sub-agent
3. Generate 3-10 angles with rationale
4. Light MMA check (strategy alignment only, threshold ≥7.0)
5. Human selects angle(s) to advance
6. Lock ANGLE_SET for Production

**MMA Gates (Soft):**
- Strategy Alignment: ≥7.0 (must match MESSAGE_SPINE)
- Other dimensions: Not evaluated (too early)

---

### PHASE 2: PRODUCTION (P2) — Focus & Form
**Lines 608-664**

**Goal:** Publishable assets with grounded proof
**Mode:** Iterative, validation-heavy
**Tools:** Heavy (Python validators, proof checkers)
**Exit Criteria:** MMA PASS (all dimensions ≥7.0, average ≥8.0, critical ≥9.0)

**Two-Brain Pod (P2):**
```
LEFT BRAIN (Technical):
├── Proof Verifier: EP reference check
├── Schema Guardian: SSOT compliance
└── MMA Validator: 7D scoring

RIGHT BRAIN (Strategic):
├── Content Builder: Draft expansion
├── Voice Editor: Consistency check
└── UX Pacer: Flow optimization
```

**Production Loop:**
1. Load locked SSOT + selected ANGLE_SET
2. Route to Production builder
3. Generate full draft with proof discipline
4. Run MMA 7D validation (continuous)
5. IF MMA PASS → advance to Polish
6. IF MMA FIX → run correction loop
7. IF MMA ESCALATE → human decision

**FIX LOOP PROTOCOL:**
1. Identify failing dimension(s)
2. Generate CORRECTION_LOG with specific fixes
3. Route back to appropriate builder
4. Increment fix_count for dimension
5. Re-run MMA

**Circuit Breaker Rules:**
- fix_count for any dimension ≥ 3 → escalate
- Same dimension fails consecutively 2x → PATCH_REQUEST
- Human can: approve as-is, force another loop, or stop

**MMA Gates (Hard):**
- Strategy Alignment: ≥8.0 (Critical)
- Proof Discipline: ≥9.0 (Critical)
- CTA Integrity: ≥9.0 (Critical)
- Ethical Guardrails: ≥9.0 (Critical)
- Voice Consistency: ≥8.0 (High)
- Clarity + Structure: ≥8.0 (High)
- Resonance: ≥8.0 (High)
- Average: ≥8.0
- No dimension < 7.0

---

### PHASE 3: POLISH (P3) — Fixate & Forge
**Lines 667-712**

**Goal:** Voice consistency, UX optimization, ship-ready
**Mode:** Selective refinement, human-like finish
**Tools:** AI detox, rhythm analysis, Kitchen Table Test
**Exit Criteria:** Final pack ready for deployment

**Two-Brain Pod (P3):**
```
LEFT BRAIN (Technical):
├── Final QA: Compliance check
└── Format Validator: Mobile-first

RIGHT BRAIN (Strategic):
├── Voice Editor: AI detox, rhythm
├── HPE: Human Persuasion Editor
└── UX Pacer: Final flow polish
```

**Polish Workflow:**
1. Load P2-approved asset
2. Route to Human Persuasion Editor:
   - 5-pass surgical procedure
   - AI detox (banned words)
   - Cardiac rhythm (sentence variation)
   - Sensory injection (metaphors)
   - Open loop architecture
   - "You" scan (reader focus)
3. Run Kitchen Table Test
4. Final MMA validation
5. Package for deployment

**Quality Checks:**
- Bar Test: Would you say this at a bar? (voice)
- Kitchen Table Test: Natural conversation? (human-like)
- Scan Test: Readable on mobile in 3 seconds? (UX)
- Flow Test: Can't stop reading? (slippery slope)

---

## 📦 SESSION_STATE SCHEMA

**Lines 484-521**

```json
{
  "run_id": "uuid-v4",
  "project_id": "project-slug",
  "created_at": "ISO-8601",
  "updated_at": "ISO-8601",

  "active_phase": "intake|draft|production|polish|complete",
  "phase_history": [
    {"phase": "intake", "entered_at": "...", "exited_at": "...", "status": "complete"}
  ],

  "ssot_versions": {
    "PROJECT_BRIEF": {"version": "1.0", "checksum": "sha256", "locked": true},
    "MESSAGE_SPINE": {"version": "1.0", "checksum": "sha256", "locked": true},
    "EVIDENCE_PACK": {"version": "1.0", "checksum": "sha256", "locked": false}
  },

  "asset_queue": [
    {
      "asset_id": "adv-001",
      "type": "advertorial",
      "status": "in_progress|complete|blocked",
      "current_phase": "production",
      "fix_count": {"proof_discipline": 1, "voice_consistency": 0},
      "mma_scores": [{"timestamp": "...", "scores": {...}, "verdict": "FIX"}]
    }
  ],

  "context_stats": {
    "estimated_tokens": 12500,
    "capacity_percent": 62,
    "last_gc": "ISO-8601"
  },

  "patches_proposed": [],
  "escalations": []
}
```

---

## 🔒 INTAKE PROCEDURE (Stage 0-2)

**Lines 525-562**

### STAGE 0: RAW CAPTURE
- **Input:** Research bundle, avatar notes, constraints
- **Output:** INTAKE_PACKET (structured raw data)
- **Skill:** market_intelligence_synthesizer
- **Rule:** Flag missing data, don't guess

### STAGE 1: EVIDENCE CANONICALIZATION
- **Input:** PDFs, links, screenshots, testimonials
- **Output:** EVIDENCE_PACK (grounded claims)
- **Skill:** evidence_pack_builder (TO BUILD)
- **Rule:** No claim without source pointer

### STAGE 2: STRATEGY SYNTHESIS
- **Input:** INTAKE_PACKET + EVIDENCE_PACK
- **Output:** MESSAGE_SPINE + OFFER_ARCHITECTURE
- **Skills:** strategic_copy_director + offer_architect
- **Rule:** Lock before downstream execution

### LOCKING PROTOCOL:
1. Human confirms SSOT objects are correct
2. Generate checksum for each object
3. Set locked: true in SESSION_STATE
4. Any future change requires PATCH_REQUEST with:
   - Justification (why change needed)
   - Impact analysis (what assets affected)
   - Human approval

### POST-INTAKE STATE:
- PROJECT_BRIEF: LOCKED ✅
- MESSAGE_SPINE: LOCKED ✅
- EVIDENCE_PACK: LOCKED (or flagged gaps) ✅
- active_phase: "draft"
- Ready for /draft

---

## 🎨 TWO-BRAIN POD COORDINATION

### Left Brain (Technical/Structural)
**Role:** Schema validation, proof checking, routing decisions, MMA validation

**Responsibilities:**
- Ensure SSOT compliance
- Validate claims against EVIDENCE_PACK
- Run MMA 7D scoring
- Track fix_count per dimension
- Enforce circuit breakers
- Maintain SESSION_STATE

### Right Brain (Strategic/Experiential)
**Role:** Angle generation, storytelling, voice editing, UX pacing

**Responsibilities:**
- Generate creative angles
- Build narrative arcs
- Ensure voice consistency
- Optimize emotional flow
- Test Kitchen Table readability
- Inject sensory language

### Balance Requirement
**Every phase must engage BOTH brains.** Imbalance detection:
- If only analytical agents engaged → route to missing creative brain
- If only creative agents engaged → route to missing validation brain
- Dual review required before phase exit

---

## 🚨 CIRCUIT BREAKERS & ESCALATION

### Max FIX Loops: 3 per asset
If any dimension reaches 3 FIX attempts:
1. Trip circuit breaker
2. Generate ESCALATION_PACKET
3. Present options to human:
   - approve_as_is (accept risk)
   - force_loop (one more try)
   - patch_skill (skill improvement needed)
   - stop (abort asset)

### Same Dimension Fails 2x Consecutively
Triggers:
1. PATCH_REQUEST generation
2. Automatic escalation to human
3. Skill gap identified

### Human Decision Capture
- Log decision with timestamp and rationale
- If patch approved, generate PATCH_PROPOSAL
- If override approved, log risk acceptance
- Continue or stop based on decision

---

## 📋 SSOT REQUIREMENTS

### Required (Must Have)
- ✅ PROJECT_BRIEF: Goal, avatar, offer, constraints, CTA, timeline, budget
- ✅ MESSAGE_SPINE: Promise, mechanism, proof pillars, objection handlers, belief shifts

### Recommended (Should Have)
- 📋 EVIDENCE_PACK: Claims grounding, citations, proof gaps, hypothesis flags
- 📋 VOICE_GUIDE: Tone dials, taboos, rhythm, personality, Kitchen Table Test criteria
- 📋 OFFER_ARCHITECTURE: Value Equation, tier structure, pricing logic, bonuses

### Generated (By ZPWO)
- SESSION_STATE: Run tracking, phase history, SSOT versions, asset queue
- LOCKED_OBJECTS: Versioned + checksummed SSOT snapshots
- MMA_REPORT: 7-dimension quality scorecard
- CORRECTION_LOG: What changed, why, which MMA dimension triggered
- PATCH_PROPOSALS: Skill improvement suggestions
- SUMMARY_HANDOFF: Session summary for continuity

---

## 🔧 HOW TO ACTIVATE ZPWO

### Current Understanding

**ZPWO is a meta-orchestrator that:**
1. **Routes** commands to appropriate skills
2. **Manages** SESSION_STATE across phases
3. **Locks** SSOT objects to prevent drift
4. **Coordinates** Two-Brain Pods
5. **Validates** via MMA at phase gates
6. **Enforces** circuit breakers and escalations

### Activation Methods

**Option A: Via Slash Commands** (Recommended)
```bash
/intake --project=sleep_energy
/draft --asset=advertorial
/produce --asset=advertorial
/polish --asset=advertorial
/ship
```

**Option B: Direct Invocation**
Claude Code can invoke ZPWO directly by referencing the skill and providing context.

**Option C: Sub-Agent Spawning** (Advanced)
ZPWO spawns specialized sub-agents for each phase/skill, managing their coordination.

---

## 🧪 TEST WORKFLOW DESIGN

### Mini-Test: Advertorial Draft Generation

**Objective:** Test ZPWO orchestration from /intake through /draft

**Prerequisites:**
1. Create minimal PROJECT_BRIEF for Sleep Energy Breakthrough
2. Create minimal MESSAGE_SPINE with cortisol-melatonin mechanism

**Steps:**
1. `/intake` → Lock SSOT objects
2. `/draft --asset=advertorial` → Generate 3-5 angles
3. Observe:
   - Does ZPWO route to advertorial_copy_master?
   - Is phase context set to "draft"?
   - Are Two-Brain Pods coordinated?
   - Is MMA validation triggered?
   - Is SESSION_STATE maintained?

**Success Criteria:**
- ZPWO successfully routes request
- advertorial_copy_master skill activates
- 3-5 viable angles generated
- MMA strategy alignment ≥7.0
- SESSION_STATE tracks progress

---

## 📝 FINDINGS & INSIGHTS

### Key Discovery 1: ZPWO is Already Built & Complete
✅ Comprehensive orchestration logic
✅ 3-phase workflow defined
✅ Two-Brain Pod coordination
✅ Circuit breakers implemented
✅ MMA integration points specified
✅ SESSION_STATE schema defined

### Key Discovery 2: Routing Table is Clear
The routing table (lines 259-270) shows exactly which command triggers which skill. This makes implementation straightforward.

### Key Discovery 3: SSOT Locking is Well-Defined
The locking protocol (lines 547-554) provides clear checksumming and drift prevention. This prevents the multi-project inconsistency issue you experienced.

### Key Discovery 4: Missing Skills Identified
Some routed skills need verification:
- ❓ sales_page_deconstructor (referenced but file needs verification)
- ❓ human_persuasion_editor (referenced but file needs verification)
- ❓ sales_copy_consistency_contract (referenced but file needs verification)
- ❓ evidence_pack_builder (needed for Stage 1, marked TO BUILD)
- ❓ offer_architect (needed for Stage 2, file needs verification)

### Key Discovery 5: Sub-Agent Pattern Emerges
ZPWO doesn't execute work—it coordinates sub-agents (skills) that do the work. This is the "Light Center, Heavy Edges" principle in action.

---

## 🚀 NEXT STEPS

### Immediate (This Session)
1. ✅ ZPWO loaded and analyzed
2. ✅ Routing table mapped
3. ✅ 3-phase workflow understood
4. 📋 **NEXT:** Create test SESSION_STATE
5. 📋 **NEXT:** Design mini-workflow test
6. 📋 **NEXT:** Document activation approach

### Short-Term (Next Session)
7. Build `/intake` slash command
8. Create minimal PROJECT_BRIEF for Sleep Energy
9. Create minimal MESSAGE_SPINE for Sleep Energy
10. Test /intake → /draft flow

### Medium-Term (This Week)
11. Verify all routed skills exist
12. Build missing skills (evidence_pack_builder, etc.)
13. Complete full P1 → P2 → P3 workflow test
14. Document learnings and refine

---

## 🎯 ACTIVATION STRATEGY

### Recommendation: Build Slash Commands First

**Rationale:**
- Slash commands provide clean invocation interface
- ZPWO expects command-based routing
- Easier to test and debug
- Matches ZPWO's design (lines 240-248)

**Build Order:**
1. `/intake` — Foundation (locks SSOT)
2. `/draft` — First workflow phase
3. `/validate` — Quality check (MMA integration)
4. `/produce` — Core production loop
5. `/polish` — Final refinement
6. `/ship` — Deliverable packaging

---

## 💡 CLARIFICATION ON SUB-AGENTS

**From your input:**
> "we will build slash commands and run the skills inside sub-agents as you see fit"

**Understanding:**
- ZPWO is the **orchestrator/conductor**
- Skills (advertorial_copy_master, etc.) are the **sub-agents**
- Slash commands are the **invocation interface**
- Claude Code can spawn Task agents as **sub-processes** for parallel execution

**Architecture:**
```
User types: /draft --asset=advertorial
    ↓
/draft slash command invoked
    ↓
ZPWO orchestrator activates
    ↓
ZPWO routes to advertorial_copy_master skill
    ↓
Skill loads (progressive disclosure L1-L4)
    ↓
Skill executes in sub-agent context
    ↓
Output validated by MMA
    ↓
Results returned to ZPWO
    ↓
SESSION_STATE updated
    ↓
User sees result
```

---

**Status:** ZPWO orchestration logic fully understood. Ready to build activation interface.

**Next Task:** Create test SESSION_STATE object for mini-workflow.
