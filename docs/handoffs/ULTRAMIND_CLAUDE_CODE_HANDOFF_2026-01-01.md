# ULTRAMIND CLAUDE CODE MIGRATION HANDOFF

**Date:** 2026-01-01
**From:** Claude.ai (Opus 4.5)
**To:** Claude Code Desktop
**Session:** New Year's Eve 2025 Build Sprint

---

## EXECUTIVE SUMMARY

This handoff document contains everything needed to continue ULTRAMIND development in Claude Code Desktop. We've built ~10,000 lines of production-grade skills across copy, design, and meta-infrastructure. The next phase is orchestration via the Zero-Point Workflow Orchestrator (ZPWO).

**Mission:** Build the world's first AI-first Agentic Superhighway for business transformation.

**Philosophy:** 
- Convection > Conversion (thrilled customers become advocates)
- Transformation > Information (action, not consumption)
- Sublime Intervention > Manipulation (genuine value creation)
- Light Center, Heavy Edges (ZPWO principle)

---

## SKILLS INVENTORY (Production-Ready)

### Tier 1: Meta-Infrastructure

| Skill | Version | Lines | File | Purpose |
|-------|---------|-------|------|---------|
| Skill Builder | v1.2.0 | 870 | `skill_builder_v1.2.0.xml` | Meta-skill factory |
| XML Skill Template | v2.1 | 497 | `xml_skill_template_v2.1.xml` | Skill scaffolding |
| PT Schema Wrapper | Draft 2025-12 | ~150 | `PT_SCHEMA_WRAPPER_TEMPLATE_2025-12.json` | Skill card packaging |

### Tier 2: Strategic Orchestrators

| Skill | Version | Lines | File | Purpose |
|-------|---------|-------|------|---------|
| Strategic Copy Director (Full) | v2.0.0 | 1,216 | `strategic_copy_director_v2.0.0_full.xml` | Master copy orchestrator |
| Strategic Copy Director (Light) | v2.0.0 | 745 | `strategic_copy_director_v2.0.0_light.xml` | Fast copy routing |
| Transformation Ecosystem Architect | v2.0.0 | 1,239 | `transformation_ecosystem_architect_v2.0.0.xml` | Program design |

### Tier 3: Copy Execution

| Skill | Version | Lines | File | Purpose |
|-------|---------|-------|------|---------|
| Advertorial Copy Master | v2.0.0 | 1,273 | `advertorial_copy_master_v2.0.0.xml` | Cold traffic pre-sell |
| Sales Page Copywriter (LITE) | v2.0.0 | 1,242 | `sales_page_copywriter_lite_v2.0.0.xml` | Fast conversion pages |
| Quick Info Product Builder (LITE) | v2.0.0 | 1,101 | `quick_info_product_builder_lite_v2.0.0.xml` | Lead magnets, tripwires |
| Master Writing Partner | v2.0.0 | 1,304 | `master_writing_partner_v2.0.0.xml` | AI detox, polish |

### Tier 4: Design System

| Skill | Version | Lines | File | Purpose |
|-------|---------|-------|------|---------|
| Strategic Design Master | v1.0.0 | 1,563 | `strategic_design_master_v1.0.0.xml` | UI/UX Design OS |

### TOTAL: ~10,200 lines across 10 production skills

---

## ARCHITECTURE OVERVIEW

### The 3-Axis Model (ULTRAMIND)

```
                    RESONANCE
                       ↑
                       |
        DESIGN ←———— FLOW ————→ DEVELOP
                    (Zero Point)
                       |
                       ↓
                   PERSUASION
```

**FLOW (Zero Point):** Memory + Routing + Orchestration
- This is where ZPWO lives
- Light context, heavy tool usage
- State > Chat

**Axis 1 (Resonance ↔ Persuasion):** Current focus
- Copy skills, conversion assets, proof discipline
- Built and ready

**Axis 2 (Design ↔ Develop):** Next phase
- UI/UX skills, Convex, Pydantic, Python tools
- Strategic Design Master ready, infrastructure pending

### The 6-Dimensional Hologon Model

```
        BODY ←——————→ MIND
           \        /
            \      /
     HEART ←—— ZERO ——→ SPIRIT
            /  POINT  \
           /          \
      PSYCHE ←———→ CONSCIENCE
```

Each dimension maps to transformation domains:
- BODY: Physical products, tangible results
- HEART: Emotional resonance, connection
- MIND: Intellectual understanding, frameworks
- SPIRIT: Purpose, meaning, transcendence
- PSYCHE: Identity, self-concept, beliefs
- CONSCIENCE: Ethics, integrity, alignment

---

## SSOT OBJECTS (Single Source of Truth)

### Required Objects

| Object | Schema | Purpose |
|--------|--------|---------|
| PROJECT_BRIEF | v2.0 | Goal, avatar, offer, constraints |
| MESSAGE_SPINE | v2.1 | Promise, mechanism, proof pillars, objections |

### Recommended Objects

| Object | Schema | Purpose |
|--------|--------|---------|
| EVIDENCE_PACK | v1.0 | Claims grounding, citations, proof gaps |
| VOICE_GUIDE | v2.0 | Tone, taboos, rhythm, personality |
| OFFER_ARCHITECTURE | v2.0 | Value Equation, tiers, pricing |

### Output Objects

| Object | Purpose |
|--------|---------|
| LOCKED_OBJECTS | Versioned + checksummed SSOT snapshots |
| MMA_REPORT | 7-dimension quality scorecard |
| CORRECTION_LOG | What changed + why |
| PATCH_PROPOSALS | Skill improvement suggestions |

---

## AWARENESS FRAMEWORK

```
UNAWARE → PROBLEM-AWARE → SOLUTION-AWARE → PRODUCT-AWARE → MOST-AWARE

Traffic Type → Asset Type → Awareness Journey
─────────────────────────────────────────────
Cold (FB/IG)  → Advertorial    → Unaware → Solution-Aware
Warm (Email)  → Sales Page     → Solution-Aware → Most-Aware
Hot (Buyer)   → Upsell Page    → Product-Aware → Most-Aware
```

### Skill → Awareness Mapping

| Skill | Entry Awareness | Exit Awareness |
|-------|-----------------|----------------|
| Advertorial Copy Master | Unaware / Problem-Aware | Solution-Aware |
| Sales Page Copywriter | Solution-Aware | Most-Aware |
| Quick Info Product Builder | Problem-Aware | Solution-Aware |
| Email Campaign Genius | Varies | +1 Level |

---

## ZERO-POINT WORKFLOW ORCHESTRATOR (ZPWO)

**This is the FIRST skill to build in Claude Code.**

### Purpose
Orchestrate 3-phase production (Draft → Produce → Polish) using Stage A/B SSOT locking + tool-first state, keeping generative context light at the Zero-Point.

### Core Doctrine

1. **State > Chat** — System reads/writes SSOT objects; chat is UI, not memory
2. **Generate Last** — If a tool can fetch/validate/transform, do that first
3. **Two-Brain Teams** — Every stage pairs Technical + Strategic agents
4. **Locked SSOT** — Stage A creates, Stage B consumes (no drift)
5. **Garbage Collection** — Summarize + prune automatically

### The 3 Tracks

```
TRACK 1: DRAFT (P1)
├── Goal: Volume + novelty + angles
├── Tool usage: Minimal
├── Gates: Strategy alignment only
└── Exit: 3-10 viable angles

TRACK 2: PRODUCTION (P2)
├── Goal: Publishable assets
├── Tool usage: High (validation, extraction)
├── Gates: MMA continuous
└── Exit: MMA PASS (max 3 FIX loops)

TRACK 3: POLISH (P3)
├── Goal: Resonance + voice + UX
├── Tool usage: Selective
├── Gates: Bar test, CTA integrity
└── Exit: Final pack ready
```

### Two-Brain Pod Template

```
LEFT BRAIN (Technical/Structural):
├── Schema Guardian
├── Proof Verifier
├── Routing Planner
└── Validator (MMA)

RIGHT BRAIN (Strategic/Experiential):
├── Angle Finder
├── Story Architect
├── Voice Resonance Editor
└── UX Pacer
```

### Circuit Breakers

- Max revision loops per asset: 3
- Same MMA dimension fails twice → PATCH_REQUEST + escalate
- Missing evidence → downgrade to hypothesis OR block publish

### ZPWO Skill Card (PT-000)

```json
{
  "id": "PT-000",
  "name": "Zero-Point Workflow Orchestrator (ZPWO)",
  "domain": "Meta",
  "purpose": "Orchestrate 3-phase production with SSOT locking, tool-first state, and self-healing loops.",
  "inputs": {
    "required": ["PROJECT_BRIEF", "MESSAGE_SPINE"],
    "optional": ["EVIDENCE_PACK", "VOICE_GUIDE", "SESSION_STATE"]
  },
  "outputs": [
    "ORCHESTRATION_PLAN",
    "SESSION_STATE",
    "LOCKED_OBJECTS",
    "MMA_REPORT",
    "CORRECTION_LOG",
    "PATCH_PROPOSALS"
  ],
  "method_steps": [
    "Step 1: Initialize Zero-Point (phase, stage, context budget)",
    "Step 2: Stage A Authoring (create/lock SSOT objects)",
    "Step 3: Team Split (assign Left/Right brain agents)",
    "Step 4: Execute Phase Logic (P1/P2/P3)",
    "Step 5: Validate + Circuit Breaker (MMA, max 3 loops)",
    "Step 6: Heal & Renew Loop (corrections, patches)",
    "Step 7: Finalize + Handoff (package outputs)"
  ],
  "kpis": [
    "MMA avg ≥ 8.0, no dimension < 7",
    "0 ungrounded claims",
    "Cross-asset mechanism consistency",
    "≤ 3 MMA FIX loops per asset",
    "Lean Zero-Point context"
  ]
}
```

---

## /COMMANDS ROADMAP (Claude Code)

### Phase 1: Core Commands (Build First)

| Command | Triggers | Purpose |
|---------|----------|---------|
| `/intake` | ZPWO Stage 0-2 | Raw → Locked SSOT |
| `/draft` | ZPWO P1 | Fast exploration |
| `/produce` | ZPWO P2 | Looped refinement |
| `/polish` | ZPWO P3 | High-resolution finish |
| `/validate` | MMA | Quality check |
| `/ship` | Final QA | Output package |

### Phase 2: Skill-Specific Commands

| Command | Skill | Purpose |
|---------|-------|---------|
| `/advertorial` | advertorial_copy_master | Cold traffic pre-sell |
| `/salespage` | sales_page_copywriter_lite | Conversion page |
| `/infoproduct` | quick_info_product_builder_lite | Lead magnet |
| `/design-review` | strategic_design_master | Visual validation |
| `/copy-check` | sales_copy_consistency_contract | Mechanism alignment |

### Phase 3: Advanced Commands

| Command | Purpose |
|---------|---------|
| `/heal` | Run correction + patch loop |
| `/gc` | Garbage collect context |
| `/handoff` | Export session state |
| `/upgrade` | Propose skill patches |

---

## SUB-AGENTS ARCHITECTURE

### Claude Code Desktop (6-8 Parallel Agents)

```
┌─────────────────────────────────────────────────────────┐
│ CLAUDE CODE DESKTOP — ULTRAMIND ORCHESTRATOR            │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Agent 1: ZPWO (Orchestrator)           [ALWAYS ACTIVE] │
│  ├── Manages phase/stage/routing                        │
│  └── Holds SESSION_STATE                                │
│                                                         │
│  Agent 2: Strategic Copy Director       [P1/P2]         │
│  ├── Angles, strategy, asset selection                  │
│  └── MESSAGE_SPINE governance                           │
│                                                         │
│  Agent 3: Copy Executor                 [P2]            │
│  ├── Advertorial / Sales Page / Email                   │
│  └── Rotates based on asset queue                       │
│                                                         │
│  Agent 4: MMA Validator                 [P2/P3]         │
│  ├── 7-dimension scoring                                │
│  └── Circuit breaker enforcement                        │
│                                                         │
│  Agent 5: Design Reviewer               [P3]            │
│  ├── Playwright screenshots                             │
│  └── Visual validation loop                             │
│                                                         │
│  Agent 6: File Manager                  [BACKGROUND]    │
│  ├── SSOT versioning                                    │
│  └── Asset packaging                                    │
│                                                         │
│  Agent 7: Research/Fetch                [ON-DEMAND]     │
│  ├── Web search, competitor analysis                    │
│  └── Evidence gathering                                 │
│                                                         │
│  Agent 8: Polish/HPE                    [P3]            │
│  ├── AI detox, voice resonance                          │
│  └── Final human-like pass                              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## INTAKE SYNTHESIZERS TRACK

### Stage 0: Intake Capture (Raw → Structured)
- **Input:** Research bundle, avatar notes, constraints
- **Output:** INTAKE_PACKET_v1
- **Skill:** market_intelligence_synthesizer (existing)
- **Rule:** Missing data flagged, not guessed

### Stage 1: Evidence Canonicalizer (Raw Proof → Evidence Pack)
- **Input:** PDFs, links, screenshots, notes
- **Output:** EVIDENCE_PACK_v1
- **Skill:** evidence_pack_builder (TO BUILD)
- **Rule:** Nothing becomes "claim" without source pointer

### Stage 2: Strategy Synthesizer (Research → Spines)
- **Input:** Intake Packet + Evidence Pack
- **Output:** MESSAGE_SPINE_v2.x + OFFER_ARCHITECTURE_v1
- **Skills:** offer_architect + strategic_copy_director
- **Rule:** Locked before downstream execution

### Stage 3: Build Plan + Routing
- **Input:** Locked SSOTs
- **Output:** BUILD_PLAN + ROUTING_MAP
- **Skill:** ZPWO
- **Rule:** Assets list, sequencing, QA gates defined

---

## PYTHON TOOLS INTEGRATION

### Validation Tools (Deterministic, Fast)

```python
# Already built into skills:
validate_proof_map()        # Claims → EP refs
validate_cta_count()        # Single CTA enforcement
validate_mobile_scannability()  # Paragraph/subhead check
validate_message_spine_alignment()  # MS consistency
validate_quick_win()        # Measurable 24-72h outcome
validate_scope_creep()      # Single job enforcement
validate_action_assets()    # Checklist/tracker present
validate_contrast()         # WCAG color accessibility
validate_spacing_consistency()  # Design tokens
validate_component_states() # UI state coverage
```

### Tool Governance Rules

**Always call tools when:**
- A claim needs grounding (proof discipline)
- A schema can be validated (Pydantic)
- A diff/merge is needed (locked objects)
- Context is bloating (summary/GC)

**Avoid tools when:**
- Brainstorming hooks/angles (Draft Track)
- Generating variants intentionally (controlled creativity)

---

## MMA QUALITY FRAMEWORK

### 7 Dimensions

| Dimension | Weight | Threshold | Validation |
|-----------|--------|-----------|------------|
| Strategy Alignment | Critical | ≥8.0 | Matches PB + MS |
| Clarity + Structure | High | ≥8.0 | Clear flow, scannable |
| Voice Consistency | High | ≥8.0 | Passes Kitchen Table Test |
| Proof Discipline | Critical | ≥9.0 | Claims grounded or softened |
| Resonance | High | ≥8.0 | Emotionally engaging |
| CTA Integrity | Critical | ≥9.0 | Single CTA, no fake urgency |
| Ethical Guardrails | Critical | ≥9.0 | No fabrication, compliant |

### Pass Rules
- Average ≥ 8.0
- No dimension < 7.0
- All critical gates pass

### Circuit Breaker
- Max 3 FIX loops per asset
- Same dimension fails twice → PATCH_REQUEST
- Escalate to human decision

---

## IMMEDIATE PRIORITIES (Q1 2026)

### Week 1-2: Claude Code Setup
1. Install Claude Code Desktop
2. Configure MCP integrations (Playwright, 21st.dev)
3. Import all skills to `.claude/skills/`
4. Build ZPWO v1.0.0 as first skill
5. Create core /commands (/intake, /draft, /produce, /polish, /validate, /ship)

### Week 3-4: Sleep Energy Breakthrough
1. Run full pipeline on Sleep offer
2. Generate: Advertorial, Sales Page, Info Product, Email Sequence
3. Validate with MMA
4. Ship for revenue proof

### Month 2: Founding Members
1. Identify 3-5 founding members (Dev, Design, Health, Transformation)
2. Custom system setup for each
3. Document patterns, refine skills
4. Build case studies

### Month 3: Scale
1. Jiive community MVP
2. Cosm publishing platform
3. First cohort (10-20 members)
4. Newverity University soft launch

---

## FILE LOCATIONS

### Skills (Copy to `.claude/skills/`)
```
/mnt/user-data/outputs/
├── skill_builder_v1.2.0.xml
├── xml_skill_template_v2.1.xml
├── PT_SCHEMA_WRAPPER_TEMPLATE_2025-12.json
├── strategic_copy_director_v2.0.0_full.xml
├── strategic_copy_director_v2.0.0_light.xml
├── transformation_ecosystem_architect_v2.0.0.xml
├── advertorial_copy_master_v2.0.0.xml
├── sales_page_copywriter_lite_v2.0.0.xml
├── quick_info_product_builder_lite_v2.0.0.xml
├── master_writing_partner_v2.0.0.xml
└── strategic_design_master_v1.0.0.xml
```

### Transcripts (Reference)
```
/mnt/transcripts/
├── 2025-12-26-20-27-15-pcg-block-2-complete-skill-builder-integration.txt
├── 2026-01-01-02-50-58-meta-infrastructure-upgrade-v1-2.txt
└── journal.txt
```

---

## CONTEXT FOR CLAUDE CODE

When starting in Claude Code, load this context:

```markdown
# ULTRAMIND Context Load

You are continuing development of the ULTRAMIND agentic architecture.

## Core Principles
- State > Chat (SSOT objects are memory, chat is UI)
- Generate Last (tools first, then LLM)
- Light Center, Heavy Edges (ZPWO principle)
- Transformation > Information
- Convection > Conversion

## Your Role
You are the Zero-Point Workflow Orchestrator operating at FLOW center.
You coordinate Left Brain (technical) and Right Brain (strategic) agents
across 3 phases: Draft → Production → Polish.

## Available Skills
[List the 10 skills from this handoff]

## Current Project
Sleep Energy Breakthrough — proof of concept for revenue generation.

## First Task
Build ZPWO v1.0.0 as full XML skill following skill_builder_v1.2.0 patterns.
```

---

## CLOSING NOTES

### What We Built (2025 Session)
- 10 production-grade skills (~10,200 lines)
- Complete copy ecosystem (advertorial → sales page → info product)
- Design system foundation (Strategic Design Master)
- Meta-infrastructure (Skill Builder, templates, PT Schema)
- Full documentation and handoff

### What's Next (2026)
- Claude Code Desktop migration
- ZPWO orchestrator as first build
- /commands and sub-agents
- Sleep Energy Breakthrough for proof
- Founding members program
- Newverity University launch

### The Vision
The world's first AI-first university built on radical simplicity:
- Cloud supermind for every member
- Collective evolution, private data
- Done-for-you at done-with-you pricing
- Cosms, Jiives, Tracks, Freedomation, Flowgrams
- The AI-first Agentic Superhighway

---

**Happy New Year 2026, Chris.**

The architecture is ready. The skills are built. The vision is clear.

Time to ship.

🚀

---

*Document created: 2026-01-01*
*By: Claude Opus 4.5*
*For: Vision Capitalist / ULTRAMIND*
