# ULTRAMIND AGENTIC SWITCHOVER GUIDE v3.0.0

> **Date:** 2026-01-12
> **Strategy:** Progressive Disclosure - Light Center, Heavy Edges
> **Migration:** Chat-Era Instructions → Agentic Control Plane

---

## THE PARADIGM SHIFT

### OLD PARADIGM (Chat-Era)
```
┌────────────────────────────────────────┐
│  CLAUDE.md (12KB, 352 lines)           │
│  ├── All instructions always loaded    │
│  ├── Skills inventory embedded         │
│  ├── Full workflow descriptions        │
│  ├── Examples and templates inline     │
│  └── Result: 10K+ token baseline       │
└────────────────────────────────────────┘
```

**Problem:** Context Rot. The agent's memory is so full of instructions that it loses accuracy in execution.

### NEW PARADIGM (Agentic Era)
```
┌────────────────────────────────────────┐
│  CLAUDE.md (< 2K tokens)               │
│  ├── Identity & Core Doctrine          │
│  ├── Routing Table (commands)          │
│  ├── SSOT Requirements                 │
│  └── Skill Index (metadata only)       │
└────────────────────────────────────────┘
              ↓ (on demand)
┌────────────────────────────────────────┐
│  SKILLS_MANIFEST.yaml (< 500 tokens)   │
│  ├── Skill metadata index              │
│  ├── Routing rules                     │
│  ├── Load discipline                   │
│  └── Context budget targets            │
└────────────────────────────────────────┘
              ↓ (on command trigger)
┌────────────────────────────────────────┐
│  ZPWO Skill XML (Heavy, loaded L1→L4)  │
│  ├── L1: Quick Reference (600 tokens)  │
│  ├── L2: Core Procedure (4K tokens)    │
│  ├── L3: Advanced Patterns (3K tokens) │
│  └── L4: Output Templates (2K tokens)  │
└────────────────────────────────────────┘
```

**Result:**
- Baseline: ~2.5K tokens (CLAUDE.md + manifest)
- Active skill: +600 tokens (L1 only)
- Executing: +4K tokens (L2 loaded)
- **Total when working: ~7K tokens** (vs 10K+ always-loaded)

---

## CONTEXT MATH: WHY THIS WORKS

### Token Budget Comparison

| State | Old System | New System | Savings |
|-------|-----------|-----------|---------|
| **Idle** | 10,000 tokens | 2,500 tokens | **-75%** |
| **L1 Discovery** | 10,000 tokens | 3,100 tokens | **-69%** |
| **L2 Executing** | 10,000 tokens | 7,100 tokens | **-29%** |
| **L3 Complex** | 10,000+ tokens | 10,100 tokens | **Even** |
| **L4 Shipping** | 10,000+ tokens | 9,100 tokens | **+9%** |

**Key Insight:** You save 75% of context during discovery and 29% during execution. You only "break even" during complex multi-asset workflows, but by then you have more room because you weren't bloated from the start.

---

## FILE COMPARISON

### OLD: `.claude/CLAUDE.md/CLAUDE.md` (352 lines, 12KB)

**Structure:**
- Identity (12 lines)
- Core Principles (6 lines)
- Architecture (30 lines)
- 3-Phase Workflow (35 lines)
- Two-Brain Pod Template (10 lines)
- Skills Inventory (40 lines)
- SSOT Objects (15 lines)
- Awareness Framework (25 lines)
- Quality Standards (25 lines)
- Commands (25 lines)
- How to Work (30 lines)
- Current Project (15 lines)
- File Conventions (10 lines)
- Guardrails (30 lines)
- Tool Governance (15 lines)
- Debugging (20 lines)
- Reference Documents (10 lines)

**Total:** 352 lines, ~10K tokens always loaded

### NEW: `.claude/CLAUDE_v3.md` (180 lines, ~5KB)

**Structure:**
- Identity (5 lines)
- Neuro Box Architecture (15 lines)
- Workflow Modes (12 lines)
- Agentic Navigation (8 lines + table)
- SSOT Locking (8 lines)
- Circuit Breakers (5 lines)
- Current Focus (5 lines)
- Skill Manifest (5 lines)
- Core Doctrine (6 lines)
- Commands (10 lines)
- Guardrails (10 lines)
- How to Work (12 lines)
- Reference Documents (table)
- First Run Checklist (8 lines)

**Total:** 180 lines, ~2K tokens baseline

**Reduction:** -48% line count, -80% token usage at idle

---

## SWITCHOVER PROCEDURE

### OPTION 1: Clean Swap (Recommended)

```bash
# Backup old version
mv .claude/CLAUDE.md/CLAUDE.md .claude/CLAUDE.md/CLAUDE_v2_backup.md

# Copy new version
cp CLAUDE_v3.md .claude/CLAUDE.md

# Verify manifest exists
ls -lh .claude/SKILLS_MANIFEST.yaml

# Test with /status command
# Agent should now load minimal context
```

### OPTION 2: Side-by-Side Testing

```bash
# Keep both versions
mv .claude/CLAUDE.md/CLAUDE.md .claude/CLAUDE_v2.md
cp CLAUDE_v3.md .claude/CLAUDE.md

# Compare context usage
# Old: Check baseline token usage
# New: Should see ~75% reduction at idle
```

### OPTION 3: Gradual Migration

```bash
# Week 1: Use CLAUDE_v3.md for new projects only
# Week 2: Migrate existing projects
# Week 3: Archive CLAUDE_v2.md
# Week 4: Full commitment to v3
```

---

## VERIFICATION CHECKLIST

After switchover, verify:

- [ ] CLAUDE.md file is < 200 lines
- [ ] SKILLS_MANIFEST.yaml exists in .claude/
- [ ] Baseline context usage < 3K tokens
- [ ] `/status` command works
- [ ] `/intake` triggers market_intel skill load
- [ ] `/advertorial` triggers advertorial_master skill load
- [ ] MMA validation still runs
- [ ] Circuit breakers still enforce

---

## HOW TO USE THE NEW SYSTEM

### 1. Starting a New Project

```
User: "I want to create an advertorial for hormonal women"

Agent (ZPWO):
├── Loads: CLAUDE.md (2K tokens) + SKILLS_MANIFEST.yaml (500 tokens)
├── Reads: Command = implicit /advertorial
├── Routes: advertorial_master skill
├── Loads: L1 Quick Reference (600 tokens)
├── Responds: "Starting advertorial workflow. Run /intake first to lock SSOT?"
└── Total Context: ~3.1K tokens
```

### 2. Executing Workflow

```
User: "/intake" → Agent loads market_intel skill L1+L2 (~5K tokens)
User: "/draft" → Agent loads advertorial_master L1+L2 (~7K tokens)
User: "/produce" → Agent keeps advertorial_master L2, loads MMA (~8K tokens)
User: "/polish" → Agent swaps to human_persuasion_editor L2 (~7K tokens)
User: "/ship" → Agent loads L4 templates (~5K tokens)
```

**Max Context During Workflow:** ~8K tokens (vs 10K+ always-loaded)

### 3. Garbage Collection

```
User: "/gc" → Agent:
├── Persists SESSION_STATE.json
├── Archives completed phase artifacts
├── Generates SUMMARY_HANDOFF
├── Unloads heavy skill layers (L2-L4)
├── Keeps only L1 + CLAUDE.md + manifest
└── Context drops to ~3.1K tokens
```

---

## WHY THE "TINY FILE" IS MORE POWERFUL

### The Orchestra Analogy

**Old System (Integrated):**
```
You have 30 musicians standing on stage at all times,
even when only the strings are playing.

Result: Crowded, noisy, hard to hear the violins.
```

**New System (Orchestrated):**
```
You have a conductor with a score (CLAUDE.md).
Musicians enter when their section is needed.
Musicians exit when their part is done.

Result: Clean, focused, precise execution.
```

### The Math

```
OLD: 30 skills × 300 lines each = 9,000 lines always loaded
NEW: 1 manifest × 100 lines + 1 active skill × 300 lines = 400 lines loaded

Reduction: 95%+ context savings during most operations
```

### The Truth

**The ZPWO is not "tiny" in its logic.**

The ZPWO XML is 1,560 lines. The CLAUDE.md is 180 lines. Together they define the entire orchestration layer.

But **only the map loads by default**. The heavy machinery loads on-demand.

This is how you replace an "Integrated Master Planner" with a "Meta-Orchestrator":

1. **Master Planner:** Knows everything, always loaded, context-bloated
2. **Meta-Orchestrator:** Knows *where* everything is, loads *what* is needed, stays lean

---

## INTEGRATION WITH GEMINI 3.0 (DESIGN & MAPPING)

### Workflow Division

```
┌─────────────────────────────────────────────────────────┐
│  CLAUDE CODE (Terminal) - ZPWO Meta-Orchestrator       │
│  ├── Copy execution (advertorial, sales pages)         │
│  ├── SSOT management (locking, validation)             │
│  ├── Quality gates (MMA, circuit breakers)             │
│  └── Workflow coordination (Draft→Produce→Polish)      │
└─────────────────────────────────────────────────────────┘
              ↕ (SSOT handoff)
┌─────────────────────────────────────────────────────────┐
│  GEMINI 3.0 (Antigravity IDE) - Design & Spatial       │
│  ├── Visual wireframes (Neuro Box mapping)             │
│  ├── Skill manifest visualization                      │
│  ├── SSOT object design (PROJECT_BRIEF, MESSAGE_SPINE) │
│  └── Flow diagrams (3-phase waveform visualization)    │
└─────────────────────────────────────────────────────────┘
```

**Division of Labor:**
- **Claude Code:** Text, logic, validation, execution
- **Gemini 3.0:** Visual, spatial, design, mapping

**Shared State:**
- SSOT objects (YAML files)
- Skills Manifest (YAML index)
- Session State (JSON runtime)

---

## EXPECTED OUTCOMES

### Immediate (Week 1)
- 75% context reduction at idle
- Faster skill loading (only L1 by default)
- Clearer command routing

### Short-Term (Week 2-4)
- Fewer "confused agent" moments
- More accurate skill execution
- Better quality gate enforcement

### Long-Term (Month 2-3)
- Self-healing via PATCH_PROPOSALS
- Skill library growth without bloat
- Agentic superhighway ready for multi-agent coordination

---

## ROLLBACK PLAN

If the new system doesn't work:

```bash
# Restore old version
mv .claude/CLAUDE_v2_backup.md .claude/CLAUDE.md

# Or keep both and switch via symlink
ln -sf .claude/CLAUDE_v2.md .claude/CLAUDE.md  # Use old
ln -sf .claude/CLAUDE_v3.md .claude/CLAUDE.md  # Use new
```

No data is lost. All SSOT objects remain compatible.

---

## NEXT STEPS

1. **Review** this guide
2. **Decide** on switchover option (Clean Swap recommended)
3. **Execute** file replacement
4. **Test** with a simple /intake command
5. **Monitor** context usage
6. **Iterate** based on performance

---

*Zero-Point Context Strategy: Light Center, Heavy Edges*
*The conductor that tries to play every instrument plays none well.*
