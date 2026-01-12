# ULTRAMIND COORDINATION GUIDE
## For Claude Code Runs

**Version:** 1.0.0
**Date:** 2026-01-11
**Purpose:** Understanding the orchestrated workflow and why individual skills need coordination

---

## THE CORE PROBLEM YOU DISCOVERED

### What You Built
- **Large, comprehensive skill files** (1,000-1,500 lines each)
- Each skill is designed to act as a **sub-agent** with deep expertise
- Skills contain progressive disclosure (L1-L4 layers)
- Skills pair into **Two-Brain Pods** (Technical + Strategic)

### What Didn't Work
- **Running skills in isolation** (one at a time)
- Skills were designed to be **orchestrated**, not invoked individually
- Without ZPWO coordination, skills lacked:
  - Phase context (Draft/Production/Polish)
  - SSOT locking discipline
  - Cross-skill handoffs
  - Quality gates (MMA)
  - Circuit breakers

### The Missing Piece
**ZPWO (Zero-Point Workflow Orchestrator)** — Already built at:
`.claude/skills/meta/zpwo_v1_0_0_updated.xml`

---

## THE ORCHESTRATION MODEL

### Zero-Point Philosophy

```
     HEAVY EDGE                LIGHT CENTER               HEAVY EDGE
   (Copy Skills)              (ZPWO Routes)            (Design Skills)
        │                           │                         │
        │                           │                         │
    ┌───▼───┐                  ┌────▼────┐              ┌────▼────┐
    │ Draft │                  │  ZPWO   │              │ Design  │
    │ Prod  │◄─────────────────┤  State  │─────────────►│ Review  │
    │Polish │                  │ Manager │              │Validate │
    └───────┘                  └────┬────┘              └─────────┘
                                    │
                                    │
                               ┌────▼────┐
                               │   MMA   │
                               │Validate │
                               └─────────┘
```

**Principle:** Keep the center (ZPWO) light with minimal context. Activate heavy skills at the edges on-demand.

---

## THE 3-PHASE WORKFLOW

### PHASE 1: DRAFT (P1) — Filter & Frame
**Goal:** Volume, novelty, angles
**Tool Usage:** Minimal
**MMA Gates:** Strategy alignment only
**Exit:** 3-10 viable angles selected

**Two-Brain Pod:**
- **LEFT (Technical):** Schema Guardian, Routing Planner
- **RIGHT (Strategic):** Angle Finder, Story Architect

**Skills Activated:**
- `strategic_copy_director_v2_1_0.xml` (light mode)
- Relevant copy skill in "draft mode"

### PHASE 2: PRODUCTION (P2) — Focus & Form
**Goal:** Publishable assets with proof
**Tool Usage:** Heavy (validation, proof grounding)
**MMA Gates:** Continuous 7D validation
**Exit:** MMA PASS (max 3 FIX loops)

**Two-Brain Pod:**
- **LEFT (Technical):** Proof Verifier, Schema Guardian, MMA Validator
- **RIGHT (Strategic):** Content Builder, Voice Editor, UX Pacer

**Skills Activated:**
- Copy execution skill (advertorial, sales page, etc.)
- `mma_master_monitor_agent_v1_0_0.xml`
- Evidence pack validation tools

### PHASE 3: POLISH (P3) — Fixate & Forge
**Goal:** Resonance, voice, ship-ready
**Tool Usage:** Selective (AI detox, compliance)
**MMA Gates:** Final quality gate
**Exit:** Final pack ready for deployment

**Two-Brain Pod:**
- **LEFT (Technical):** Final QA, Format Validator
- **RIGHT (Strategic):** Voice Editor, HPE, UX Pacer

**Skills Activated:**
- `master_writing_partner_v2.0.0.xml`
- Voice consistency tools
- Kitchen Table Test

---

## HOW ORCHESTRATION WORKS

### Stage A/B SSOT Locking

**Stage A: Creation** (Upstream)
- PROJECT_BRIEF created
- MESSAGE_SPINE created
- EVIDENCE_PACK created
- Objects are **checksummed and locked**

**Stage B: Consumption** (Downstream)
- Copy skills read locked objects
- No modifications allowed without PATCH_REQUEST
- Prevents drift across assets

### The Handoff Chain

```
/intake (ZPWO Stage 0-2)
   │
   ├─► Lock PROJECT_BRIEF
   ├─► Lock MESSAGE_SPINE
   └─► Lock EVIDENCE_PACK
       │
       ▼
/draft (ZPWO P1)
   │
   ├─► Strategic Copy Director → Generate angles
   └─► User selects angle → Lock ANGLE_SET
       │
       ▼
/produce (ZPWO P2)
   │
   ├─► Copy Skill → Generate asset
   ├─► MMA → Validate (7D scoring)
   ├─► IF FIX: Correction loop (max 3)
   └─► IF PASS: Lock ASSET_V1
       │
       ▼
/polish (ZPWO P3)
   │
   ├─► Master Writing Partner → AI detox, voice
   ├─► MMA → Final validation
   └─► IF PASS: Lock FINAL_ASSET
       │
       ▼
/ship
   │
   └─► Package deliverables
```

---

## WHY INDIVIDUAL SKILLS DIDN'T WORK

### Without ZPWO Coordination:

1. **No Phase Context**
   - Skill doesn't know if it's drafting, producing, or polishing
   - Quality bar unclear (draft = loose, production = strict)

2. **No SSOT Locking**
   - MESSAGE_SPINE can drift between sessions
   - Cross-asset inconsistency (advertorial says one thing, sales page says another)

3. **No Circuit Breakers**
   - Infinite FIX loops possible
   - Same failures repeat without escalation

4. **No Two-Brain Coordination**
   - Technical validation without strategic creativity
   - Or vice versa — imbalanced output

5. **No Quality Gates**
   - MMA not called automatically
   - Proof discipline missed
   - Voice inconsistency undetected

---

## THE LEAN STACK DOCTRINE

### Skills > MCPs

**Why:**
- MCPs load full schemas **always** (bloats context)
- Skills load progressively (L1 always, L2-L4 on-demand)
- Token discipline = accuracy discipline

**Replacement Map:**

| Old (MCP) | New (Skill + Script) |
|-----------|---------------------|
| Browser MCP | `dev_browser` skill + CLI fetch |
| GitHub MCP | `repo_ops` skill + `gh` CLI |
| Exa MCP | `web_intelligence` skill |
| Terminal MCP | `script_runner` skill + bash |

### Tool Index (Zero-Point Friendly)

Store **only capability descriptors** in default context:

```yaml
TOOL_INDEX:
  web_intelligence:
    capability: "search + fetch + extract + cite"
    activation: "/web-intel"
    latency: "2-5s"

  repo_ops:
    capability: "branch + PR + diff + review"
    activation: "/repo"
    latency: "1-3s"
```

Full schemas loaded **only when activated**.

---

## MMA (MASTER MONITOR AGENT)

### The 7 Dimensions (7D)

| Dimension | Weight | Threshold | Priority |
|-----------|--------|-----------|----------|
| Strategy Alignment | 0.15 | 8.0 | CRITICAL |
| Proof Discipline | 0.20 | 9.0 | CRITICAL |
| CTA Integrity | 0.15 | 9.0 | CRITICAL |
| Voice Consistency | 0.15 | 8.0 | HIGH |
| Clarity + Structure | 0.10 | 8.0 | HIGH |
| Resonance | 0.15 | 8.0 | HIGH |
| Ethical Guardrails | 0.10 | 9.0 | CRITICAL |

### Pass Rules
- Weighted average ≥ 8.0
- No dimension < 7.0
- All CRITICAL dimensions ≥ threshold

### Circuit Breaker
- Max 3 FIX loops per asset
- Same dimension fails 2x → PATCH_REQUEST + escalate
- Ethical failures → immediate human escalation

### 5 Operating Modes

1. **M1: Quick Score** — Standard phase gate (2-3 min)
2. **M2: Deep Audit** — Pre-launch comprehensive (10-15 min)
3. **M3: Multi-Asset Consistency** — Funnel drift detection (15-20 min)
4. **M4: Compliance Gate** — Binary pass/block (1-2 min)
5. **M5: Comparative Scoring** — A/B variant selection (5-10 min)

---

## THE 7S/7F FRAMEWORK

### 7 Dimensions (Neuro-Box Integration)

| S | Name | Neuro | Question | Threshold |
|---|------|-------|----------|-----------|
| 1 | SAFE | BODY | Am I safe here? | 8.0 |
| 2 | SPECIAL | HEART | Is this unique? | 7.5 |
| 3 | SMART | MIND | Does this make sense? | 9.0 ⚠️ CRITICAL |
| 4 | SIGNIFICANT | SPIRIT | Do others want this? | 7.5 |
| 5 | SUPPORTED | PSYCHE | Can I act NOW? | 8.0 |
| 6 | SUPERIOR | CONSCIENCE | Am I supported? | 7.0 |
| 7 | STEAL | SOUL | Is this a great deal? | 7.0 |

### Coverage Requirements by Asset Type

**Advertorial:**
- Primary (9.0): SAFE, SPECIAL
- Secondary (7.5): SMART (tease only)

**Sales Page:**
- Primary (9.0): SMART, SIGNIFICANT, SUPPORTED
- Secondary (8.0): SAFE, STEAL
- Tertiary (7.0): SPECIAL, SUPERIOR

**VSL:**
- Primary (9.0): SAFE, SPECIAL, SMART
- Secondary (8.0): SIGNIFICANT, SUPPORTED
- Tertiary (7.0): SUPERIOR, STEAL

---

## RECOMMENDED RUN PATTERNS

### Pattern 1: Full Funnel Build

```bash
# Session 1: Intake & Lock SSOT
/intake
# → Creates PROJECT_BRIEF, MESSAGE_SPINE, EVIDENCE_PACK
# → Human reviews and confirms
# → Objects are checksummed and locked

# Session 2: Advertorial (Cold Traffic)
/draft --asset=advertorial
# → Generate 5-7 angles
# → Human selects 1-2

/produce --asset=advertorial --angle=selected
# → Build full advertorial
# → MMA validates (may loop 1-3x)

/polish --asset=advertorial
# → AI detox, voice consistency
# → Final MMA check

# Session 3: Sales Page (Warm Traffic)
/draft --asset=salespage
/produce --asset=salespage
/polish --asset=salespage

# Session 4: Email Sequence
/draft --asset=email-sequence
/produce --asset=email-sequence
/polish --asset=email-sequence

# Session 5: Ship
/ship --funnel=complete
# → Package all assets
# → QA report
# → Deployment notes
```

### Pattern 2: Quick Info Product

```bash
/intake --mode=light
/produce --asset=infoproduct --speed=fast
/validate --mode=M1
/ship
```

### Pattern 3: Sales Page Revision

```bash
/deconstruct --asset=existing-sales-page.md
# → Analyze current performance
# → Identify weaknesses

/intake --update-from=analysis
/produce --asset=salespage --version=v2
/polish --asset=salespage
/ship --include-ab-test-plan
```

---

## CURRENT STATE ASSESSMENT

### ✅ Built & Production-Ready

**Meta Skills:**
- ✅ Skill Builder v1.2.0
- ✅ XML Template v2.1
- ✅ ZPWO v1.0.0 (just verified)
- ✅ MMA v1.0.0 (just verified)

**Copy Skills:**
- ✅ Strategic Copy Director (Full + Light)
- ✅ Advertorial Copy Master v2.0.0
- ✅ Sales Page Copywriter LITE v2.0.0
- ✅ Quick Info Product Builder LITE v2.0.0
- ✅ Master Writing Partner v2.0.0
- ✅ Email Campaign Genius v2.0.0
- ✅ VSL Script Writer (Long Form) v1.0

**Design Skills:**
- ✅ Strategic Design Master v1.0.0

**Total:** ~15-20 production skills

### 🔨 To Build (Priority Order)

1. **Evidence Pack Builder** — Stage 1 intake synthesizer
2. **Offer Architect** — Value Equation + positioning
3. **Human Persuasion Editor** — Final polish specialist
4. **Sales Copy Consistency Contract** — Mechanism drift detection
5. **Neuro-Resonance Auditor** — Deep 7S/7F analysis

### 📋 Infrastructure Needs

1. **SSOT Templates** — Already exist in `ssot/Templates/`
2. **/commands** — Need to create slash commands
3. **Python Tools** — Validation scripts
4. **Hooks** — Pre/post execution

---

## RECOMMENDED NEXT STEPS

### Immediate (This Session)

1. **Test ZPWO** — Verify it can orchestrate
2. **Create /intake command** — First workflow entry point
3. **Test on mini-project** — Sleep Energy Breakthrough outline

### Short-term (This Week)

4. **Build missing synthesizers** — Evidence Pack Builder, Offer Architect
5. **Create remaining /commands** — /draft, /produce, /polish, /validate, /ship
6. **Document workflow** — Step-by-step guide for Sleep project

### Medium-term (This Month)

7. **Full Sleep project** — Advertorial + Sales Page + Email Sequence
8. **Validate with MMA** — Real quality gate testing
9. **Refine orchestration** — Based on lessons learned
10. **Build Python tools** — Deterministic validation

---

## KEY INSIGHTS FROM ARCHITECTURE DOCS

### From LEAN STACK:
- **Zero-Point Context Strategy** — Default state ≤500 tokens
- **Skills + Scripts > MCPs** — Token discipline = accuracy discipline
- **Activate → Execute → Compress → Unload** — Temporary power, not permanent bloat

### From 3-AXIS:
- **All axes meet at FLOW** — Zero-Point coordination center
- **Self-correcting geometry** — Misalignment creates tension toward center
- **Recursive scaling** — Same architecture at every level

### From MMA:
- **Quality is continuous** — Not a phase, a state
- **PASS / FIX / ESCALATE** — Three verdicts only
- **7D + 7S = Complete picture** — Technical quality + resonance coverage

### From HANDOFF:
- **State > Chat** — SSOT is memory, conversation is UI
- **Generate Last** — Tools first, LLM generation second
- **Light Center, Heavy Edges** — ZPWO routes, skills execute

---

## DEBUGGING FUTURE RUNS

### If Skills Don't Produce Quality Output:

**Check:**
1. Is ZPWO coordinating? (Phase context set?)
2. Are SSOT objects locked? (Checksums verified?)
3. Is MMA validating? (7D scoring happening?)
4. Is the Two-Brain Pod balanced? (Left + Right engaged?)
5. Are circuit breakers enforced? (Max 3 loops?)

### If Context Bloats:

**Solutions:**
1. Trigger /gc (garbage collection)
2. Load only L1 layers by default
3. Reference SSOT by checksum, not full content
4. Archive completed phases

### If Assets Drift Across Funnel:

**Solutions:**
1. Run /validate --mode=M3 (Multi-Asset Consistency)
2. Check MESSAGE_SPINE locking
3. Verify mechanism language matches exactly
4. Use Sales Copy Consistency Contract skill

---

## PHILOSOPHY RECAP

### The Core Thesis

> "At the heart of infinitely intelligent adaptive systems is radical simplicity."

**Translation:**
- Don't build complexity for complexity's sake
- Orchestration at center, execution at edges
- State-driven, not conversation-driven
- Self-healing through geometry, not rules

### The Business Model

**Convection > Conversion**
- Thrilled customers become advocates
- Word-of-mouth engine, not ad dependency

**Transformation > Information**
- Action and results, not content consumption
- Done-for-you at done-with-you pricing

**Sublime Intervention > Manipulation**
- Genuine value creation
- Ethical guardrails non-negotiable

---

## FINAL NOTES

### What Makes ULTRAMIND Different

1. **AI-First from Day 1** — Not AI bolted onto human process
2. **Agentic Architecture** — Skills as sub-agents, not templates
3. **SSOT Discipline** — State machines, not chat threads
4. **Two-Brain Pods** — Technical + Strategic always paired
5. **Zero-Point Orchestration** — Light center, heavy edges
6. **Self-Healing** — Circuit breakers, patch proposals, MMA gates
7. **Fractal Scaling** — Same geometry at every level

### The Vision

Build the world's first AI-first university:
- Cloud supermind for every member
- Collective evolution, private data
- Newverity University launch Q1 2026
- The Agentic Superhighway

---

**You're not building a writing tool.**
**You're building an intelligence orchestration system.**

**The skills work.**
**The architecture is sound.**
**The orchestration is the unlock.**

---

*Document created: 2026-01-11*
*For: ULTRAMIND Claude Code Sessions*
*Next: Test ZPWO orchestration*
