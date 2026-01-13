# ULTRAMIND ARCHITECTURE COMPARISON
## Chat-Era vs Agentic-Era Control Planes

> **Date:** 2026-01-12
> **Transition:** v2.0 (Integrated) → v3.0 (Orchestrated)

---

## VISUAL ARCHITECTURE

### OLD (v2.0): Integrated Master Planner

```
┌─────────────────────────────────────────────────────────────┐
│                    CLAUDE.md (12KB)                         │
│                  ALWAYS LOADED (10K tokens)                 │
├─────────────────────────────────────────────────────────────┤
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │
│ │  Identity   │ │ Principles  │ │Architecture │           │
│ └─────────────┘ └─────────────┘ └─────────────┘           │
│                                                             │
│ ┌─────────────────────────────────────────────────────┐   │
│ │          Skills Inventory (embedded)                │   │
│ │  - Advertorial Copy Master                          │   │
│ │  - Sales Page Copywriter                            │   │
│ │  - Email Campaign Genius                            │   │
│ │  - (27 more skills listed with descriptions)        │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ ┌─────────────────────────────────────────────────────┐   │
│ │          Workflow Instructions (embedded)           │   │
│ │  - Draft Phase (35 lines)                           │   │
│ │  - Production Phase (40 lines)                      │   │
│ │  - Polish Phase (30 lines)                          │   │
│ └─────────────────────────────────────────────────────┘   │
│                                                             │
│ ┌─────────────────────────────────────────────────────┐   │
│ │          Examples & Templates (embedded)            │   │
│ │  - MMA scoring examples                             │   │
│ │  - SSOT object samples                              │   │
│ │  - Command usage patterns                           │   │
│ └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            ↓
              🎯 AGENT READS ALL OF THIS FIRST
                   (Every single invocation)
```

**Problem:**
- Agent drowns in instructions before doing anything
- 30+ skills described, but only 1 will be used
- Workflow steps repeated even when not needed
- Context bloat from examples never referenced

---

### NEW (v3.0): Zero-Point Meta-Orchestrator

```
┌───────────────────────────────────────────────────────────┐
│               CLAUDE.md (5KB, 2K tokens)                  │
│                   ALWAYS LOADED                           │
├───────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐               │
│  │ Identity │  │ 6D Box   │  │ Doctrine │               │
│  │ (5 lines)│  │ (15 lines│  │ (6 lines)│               │
│  └──────────┘  └──────────┘  └──────────┘               │
│                                                           │
│  ┌─────────────────────────────────────────────┐         │
│  │    Routing Table (command → skill)          │         │
│  │    /advertorial → advertorial_master        │         │
│  │    /salespage → sales_page_lite             │         │
│  │    /intake → market_intel                   │         │
│  └─────────────────────────────────────────────┘         │
│                                                           │
│  ┌─────────────────────────────────────────────┐         │
│  │    SSOT Requirements (8 lines)              │         │
│  │    - PROJECT_BRIEF, MESSAGE_SPINE           │         │
│  │    - EVIDENCE_PACK, VOICE_GUIDE             │         │
│  └─────────────────────────────────────────────┘         │
│                                                           │
│  ┌─────────────────────────────────────────────┐         │
│  │    Circuit Breakers (5 lines)               │         │
│  │    - Max 3 FIX loops → HALT                 │         │
│  │    - Context >70% → /gc                     │         │
│  └─────────────────────────────────────────────┘         │
└───────────────────────────────────────────────────────────┘
                            ↓
                   🎯 AGENT READS THIS
              (Quick map, knows where to go)
                            ↓
              ┌─────────────────────────┐
              │ SKILLS_MANIFEST.yaml    │
              │ (500 tokens, metadata)  │
              ├─────────────────────────┤
              │ advertorial_master:     │
              │   file: skills/copy/... │
              │   load_cost: high       │
              │   axis: MIND-SPIRIT     │
              │                         │
              │ sales_page_lite:        │
              │   file: skills/copy/... │
              │   load_cost: high       │
              │   axis: MIND-SPIRIT     │
              └─────────────────────────┘
                            ↓
              (On /advertorial command)
                            ↓
        ┌───────────────────────────────────────┐
        │  advertorial_copy_master_v2.0.0.xml   │
        │  (Loaded progressively)               │
        ├───────────────────────────────────────┤
        │  L1: Quick Reference (600 tokens)     │
        │  ├── Core identity                    │
        │  ├── When to use                      │
        │  └── Quick decision tree              │
        │                                       │
        │  L2: Core Procedure (4K tokens)       │
        │  ├── Belief ladder construction       │
        │  ├── Bridge protocols                 │
        │  └── Proof discipline rules           │
        │                                       │
        │  L3: Advanced Patterns (3K tokens)    │
        │  ├── Multi-mechanism handling         │
        │  ├── Avatar segmentation              │
        │  └── Objection weaving                │
        │                                       │
        │  L4: Output Templates (2K tokens)     │
        │  ├── Section templates                │
        │  ├── Example outputs                  │
        │  └── Quality checklists               │
        └───────────────────────────────────────┘
```

**Solution:**
- Agent reads 2K token map first
- Loads 600 token L1 only when skill triggered
- Loads 4K token L2 only when executing
- Loads 3K token L3 only when complex scenario detected
- Loads 2K token L4 only when generating deliverable

**Total Context Budget:**
- Idle: 2.5K tokens (CLAUDE.md + manifest)
- Discovery: 3.1K tokens (+ L1)
- Executing: 7.1K tokens (+ L2)
- Complex: 10.1K tokens (+ L3)
- Shipping: 9.1K tokens (+ L4)

---

## TOKEN FLOW COMPARISON

### OLD SYSTEM (Always-Loaded)

```
Session Start
    ↓
Load CLAUDE.md (10,000 tokens)
    ↓
User: "Create an advertorial"
    ↓
Agent: Reads all 10K tokens again
       Finds advertorial section
       Executes
    ↓
Context: 10,000 tokens + conversation
```

**Context Growth:**
```
Start:    10,000 tokens
+ User:   10,100 tokens (+100)
+ Agent:  10,500 tokens (+400)
+ User:   10,600 tokens (+100)
+ Agent:  11,200 tokens (+600)

After 10 exchanges: 15,000 tokens
Garbage collection needed every 20 exchanges
```

---

### NEW SYSTEM (Progressive Disclosure)

```
Session Start
    ↓
Load CLAUDE.md (2,000 tokens)
Load SKILLS_MANIFEST.yaml (500 tokens)
    ↓
User: "Create an advertorial"
    ↓
Agent: Reads routing table
       Routes to advertorial_master
       Loads L1 only (600 tokens)
    ↓
Context: 3,100 tokens
    ↓
User: "/draft"
    ↓
Agent: Loads L2 (4,000 tokens)
    ↓
Context: 7,100 tokens + conversation
    ↓
User: "/produce"
    ↓
Agent: Keeps L2, loads MMA
    ↓
Context: 8,000 tokens + conversation
    ↓
User: "/gc" (after produce complete)
    ↓
Agent: Unloads L2, keeps L1
    ↓
Context: 3,100 tokens (back to baseline)
```

**Context Growth:**
```
Start:     2,500 tokens (CLAUDE.md + manifest)
+ Command: 3,100 tokens (+ L1)
+ Execute: 7,100 tokens (+ L2)
+ Complex: 10,100 tokens (+ L3)
+ GC:      3,100 tokens (unload L2-L4)

After 10 exchanges with GC: 8,000 tokens
Garbage collection needed every 50+ exchanges
```

---

## SKILL LOADING VISUALIZATION

### OLD: Everything In Memory

```
┌─────────────────────────────────────────────────────────┐
│                    AGENT MEMORY                         │
├─────────────────────────────────────────────────────────┤
│ [LOADED] CLAUDE.md (full)                               │
│ [LOADED] Skills Inventory (all 30 skills described)     │
│ [LOADED] Workflow instructions (all phases)             │
│ [LOADED] Examples (all templates)                       │
│ [LOADED] Quality standards (all dimensions)             │
│ [LOADED] Commands (all 20+ commands)                    │
│ [LOADED] Guardrails (all rules)                         │
│ [LOADED] Tool governance (all tools)                    │
│                                                         │
│ Total: 10,000 tokens                                    │
│                                                         │
│ ⚠️ Problem: Only 1 skill will be used,                  │
│            but all 30 are loaded                        │
└─────────────────────────────────────────────────────────┘
```

---

### NEW: Progressive Disclosure

```
┌─────────────────────────────────────────────────────────┐
│                    AGENT MEMORY (Idle)                  │
├─────────────────────────────────────────────────────────┤
│ [LOADED] CLAUDE.md (map only)              2,000 tokens │
│ [LOADED] SKILLS_MANIFEST.yaml (metadata)     500 tokens │
│ [UNLOADED] All skill XMLs (not in memory)              │
│                                                         │
│ Total: 2,500 tokens                                     │
│                                                         │
│ ✅ Benefit: 75% context savings at idle                 │
└─────────────────────────────────────────────────────────┘

                            ↓
              (User: "/advertorial")
                            ↓

┌─────────────────────────────────────────────────────────┐
│                AGENT MEMORY (Discovery)                 │
├─────────────────────────────────────────────────────────┤
│ [LOADED] CLAUDE.md                         2,000 tokens │
│ [LOADED] SKILLS_MANIFEST.yaml                500 tokens │
│ [LOADED] advertorial_master (L1 only)        600 tokens │
│ [UNLOADED] advertorial_master (L2-L4)                  │
│                                                         │
│ Total: 3,100 tokens                                     │
│                                                         │
│ ✅ Benefit: Agent knows what skill does,                │
│            but not full execution details yet           │
└─────────────────────────────────────────────────────────┘

                            ↓
                    (User: "/draft")
                            ↓

┌─────────────────────────────────────────────────────────┐
│                AGENT MEMORY (Executing)                 │
├─────────────────────────────────────────────────────────┤
│ [LOADED] CLAUDE.md                         2,000 tokens │
│ [LOADED] SKILLS_MANIFEST.yaml                500 tokens │
│ [LOADED] advertorial_master (L1+L2)       4,600 tokens │
│ [UNLOADED] advertorial_master (L3-L4)                  │
│                                                         │
│ Total: 7,100 tokens                                     │
│                                                         │
│ ✅ Benefit: Full execution procedures loaded,           │
│            but advanced patterns still cached           │
└─────────────────────────────────────────────────────────┘

                            ↓
            (Complex scenario detected)
                            ↓

┌─────────────────────────────────────────────────────────┐
│                AGENT MEMORY (Complex)                   │
├─────────────────────────────────────────────────────────┤
│ [LOADED] CLAUDE.md                         2,000 tokens │
│ [LOADED] SKILLS_MANIFEST.yaml                500 tokens │
│ [LOADED] advertorial_master (L1+L2+L3)    7,600 tokens │
│ [UNLOADED] advertorial_master (L4)                     │
│                                                         │
│ Total: 10,100 tokens                                    │
│                                                         │
│ ✅ Benefit: Now equals old system's baseline,           │
│            but ONLY when complexity requires it         │
└─────────────────────────────────────────────────────────┘

                            ↓
                    (User: "/gc")
                            ↓

┌─────────────────────────────────────────────────────────┐
│            AGENT MEMORY (Post-GC, Ready)                │
├─────────────────────────────────────────────────────────┤
│ [LOADED] CLAUDE.md                         2,000 tokens │
│ [LOADED] SKILLS_MANIFEST.yaml                500 tokens │
│ [LOADED] advertorial_master (L1 only)        600 tokens │
│ [LOADED] SESSION_STATE.json                  200 tokens │
│ [UNLOADED] advertorial_master (L2-L4)                  │
│                                                         │
│ Total: 3,300 tokens                                     │
│                                                         │
│ ✅ Benefit: Back to near-baseline,                      │
│            with session continuity preserved            │
└─────────────────────────────────────────────────────────┘
```

---

## ORCHESTRATION FLOW

### OLD: Monolithic Execution

```
User Request
    ↓
┌───────────────────────────────────┐
│  Read entire CLAUDE.md            │
│  ├── Find relevant section        │
│  ├── Execute inline               │
│  └── Keep all context loaded      │
└───────────────────────────────────┘
    ↓
Response
```

**Issues:**
- All 30 skills compete for attention
- Workflow instructions repeated unnecessarily
- Examples loaded but rarely used
- No clear separation of concerns

---

### NEW: Orchestrated Execution

```
User Request
    ↓
┌───────────────────────────────────┐
│  Read CLAUDE.md (routing table)   │
│  ├── Identify command             │
│  ├── Route to skill               │
│  └── Load minimal skill layer     │
└───────────────────────────────────┘
    ↓
┌───────────────────────────────────┐
│  Load Skill L1 (Quick Reference)  │
│  ├── Identity check               │
│  ├── Scope validation             │
│  └── Decision tree                │
└───────────────────────────────────┘
    ↓
(If executing)
    ↓
┌───────────────────────────────────┐
│  Load Skill L2 (Core Procedure)   │
│  ├── Execution steps              │
│  ├── Validation rules             │
│  └── Quality gates                │
└───────────────────────────────────┘
    ↓
(If complex)
    ↓
┌───────────────────────────────────┐
│  Load Skill L3 (Advanced Patterns)│
│  ├── Edge cases                   │
│  ├── Multi-asset coordination     │
│  └── Escalation handling          │
└───────────────────────────────────┘
    ↓
(If generating deliverable)
    ↓
┌───────────────────────────────────┐
│  Load Skill L4 (Output Templates) │
│  ├── Section templates            │
│  ├── Example outputs              │
│  └── Quality checklists           │
└───────────────────────────────────┘
    ↓
Response
    ↓
(If phase complete)
    ↓
┌───────────────────────────────────┐
│  Garbage Collection               │
│  ├── Persist SESSION_STATE        │
│  ├── Unload L2-L4                 │
│  └── Keep L1 + CLAUDE.md          │
└───────────────────────────────────┘
```

**Benefits:**
- Single skill in focus
- Progressive detail loading
- Automatic cleanup
- Clear separation of concerns

---

## THE MATH: WHY "LIGHT CENTER" WINS

### Context Utilization Efficiency

```
OLD SYSTEM:
──────────────────────────────────────────────
10,000 tokens loaded
     30 tokens relevant (1 skill needed)
 9,970 tokens wasted (other 29 skills)

Efficiency: 0.3% (30/10,000)
──────────────────────────────────────────────

NEW SYSTEM (Idle):
──────────────────────────────────────────────
2,500 tokens loaded
 2,500 tokens relevant (map + manifest)
     0 tokens wasted

Efficiency: 100% (2,500/2,500)
──────────────────────────────────────────────

NEW SYSTEM (Executing):
──────────────────────────────────────────────
7,100 tokens loaded
 7,100 tokens relevant (map + manifest + skill L1+L2)
     0 tokens wasted

Efficiency: 100% (7,100/7,100)
──────────────────────────────────────────────
```

**Key Insight:** The new system maintains 100% context efficiency by only loading what's needed, when it's needed.

---

## MIGRATION BENEFITS SUMMARY

| Metric | Old (v2.0) | New (v3.0) | Improvement |
|--------|-----------|-----------|-------------|
| **Baseline Context** | 10,000 tokens | 2,500 tokens | **-75%** |
| **Discovery Context** | 10,000 tokens | 3,100 tokens | **-69%** |
| **Execution Context** | 10,000 tokens | 7,100 tokens | **-29%** |
| **Context Efficiency** | 0.3% | 100% | **+333x** |
| **Skills in Memory** | 30 (always) | 1 (when needed) | **-97%** |
| **GC Frequency** | Every 20 exchanges | Every 50+ exchanges | **+150%** |
| **CLAUDE.md Size** | 352 lines | 180 lines | **-49%** |
| **Skill Load Time** | Instant (always loaded) | On-demand (L1→L4) | **Trade-off** |

**Net Result:** 75% context savings with no loss of capability.

---

*Zero-Point Context Strategy: Only load what you need, when you need it.*
