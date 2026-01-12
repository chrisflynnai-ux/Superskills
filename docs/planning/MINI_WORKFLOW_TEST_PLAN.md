# MINI-WORKFLOW TEST PLAN
## ZPWO Orchestration Proof-of-Concept

**Date:** 2026-01-11
**Objective:** Test ZPWO orchestration from /intake through /draft phase
**Scope:** Minimal advertorial angle generation for Sleep Energy Breakthrough

---

## 🎯 TEST OBJECTIVES

### Primary Goal
Verify that ZPWO can successfully orchestrate a multi-skill workflow with:
- Proper routing to specialized skills
- Phase context maintenance
- SSOT locking
- Two-Brain Pod coordination
- MMA validation

### Success Criteria
- ✅ ZPWO routes `/draft --asset=advertorial` to `advertorial_copy_master` skill
- ✅ Phase context set to "draft" in SESSION_STATE
- ✅ PROJECT_BRIEF and MESSAGE_SPINE loaded and locked
- ✅ 3-5 viable advertorial angles generated
- ✅ MMA strategy alignment score ≥7.0
- ✅ SESSION_STATE properly updated with results

---

## 📋 PRE-REQUISITES (✅ COMPLETED)

### Test Files Created
- ✅ `ssot/test_workflow/SESSION_STATE.json` — Initial workflow state
- ✅ `ssot/test_workflow/PROJECT_BRIEF.yaml` — Minimal Sleep Energy brief
- ✅ `ssot/test_workflow/MESSAGE_SPINE.yaml` — Minimal cortisol-melatonin spine

### ZPWO Understanding
- ✅ Orchestrator skill loaded and analyzed
- ✅ Routing table mapped (lines 259-270)
- ✅ 3-phase workflow logic extracted
- ✅ SESSION_STATE schema understood
- ✅ Intake procedure documented

---

## 🔄 WORKFLOW STEPS

### STEP 1: /intake (Simulated)
**Goal:** Lock SSOT objects and prepare for draft phase

**Actions:**
1. Load PROJECT_BRIEF.yaml
2. Load MESSAGE_SPINE.yaml
3. Generate checksums for each object
4. Set `locked: true` in SESSION_STATE
5. Update `active_phase` to "draft"
6. Mark intake phase as complete

**Expected Outputs:**
```json
{
  "ssot_versions": {
    "PROJECT_BRIEF": {
      "version": "1.0",
      "checksum": "sha256_hash_here",
      "locked": true
    },
    "MESSAGE_SPINE": {
      "version": "1.0",
      "checksum": "sha256_hash_here",
      "locked": true
    }
  },
  "active_phase": "draft",
  "phase_history": [
    {"phase": "intake", "status": "complete", "exited_at": "..."}
  ]
}
```

---

### STEP 2: /draft --asset=advertorial
**Goal:** Generate 3-5 viable advertorial angles

**ZPWO Orchestration:**
1. **Recognize command:** `/draft` with asset type `advertorial`
2. **Route to skill:** `advertorial_copy_master` (from routing table line 260)
3. **Load context:**
   - Locked PROJECT_BRIEF
   - Locked MESSAGE_SPINE
   - Phase = "draft"
4. **Activate Two-Brain Pod:**
   - LEFT (Technical): Schema Guardian, Routing Planner
   - RIGHT (Strategic): Angle Finder, Story Architect
5. **Execute Draft Logic:**
   - Generate 3-5 angles with rationale
   - Each angle should:
     - Hook (opening question/statement)
     - Angle (unique approach to the problem)
     - Bridge (connection to mechanism)
     - Rationale (why this works for cold traffic)
6. **Light MMA Validation:**
   - Strategy Alignment check only
   - Threshold: ≥7.0
7. **Update SESSION_STATE:**
   - Add asset to queue
   - Record draft status
   - Track angles generated

**Expected Outputs:**
```markdown
# ADVERTORIAL DRAFT ANGLES - Sleep Energy Breakthrough

## Angle 1: The Backwards Sleep Problem
**Hook:** "What if your sleep problem isn't about falling asleep... but about what's keeping you awake at 3am?"

**Angle:** Frame the problem as cortisol being HIGH when it should be LOW (reversed rhythm), not about sleep hygiene failures.

**Bridge:** "That's why sleep hygiene doesn't work. You're trying to force sleep while cortisol is blocking melatonin production."

**Rationale:** Reframes failure ("I've tried everything") as wrong diagnosis, not personal inadequacy. Opens door to mechanism.

---

## Angle 2: The Energy-Sleep Connection
**Hook:** "Why do sleep supplements work for some women... but make others feel MORE exhausted?"

**Angle:** It's not about the sleep quality alone - it's about the cortisol rhythm controlling BOTH sleep AND energy.

**Bridge:** "Fix cortisol timing, and you get both deep sleep AND daytime energy back."

**Rationale:** Expands promise beyond just sleep to include energy (bigger pain point for target avatar).

---

## Angle 3: The Hormonal Shift Nobody Talks About
**Hook:** "After 40, your sleep changed. Not because you're getting older... but because your hormones are."

**Angle:** Position cortisol-melatonin reversal as a hormonal shift specific to women over 40, not aging or stress.

**Bridge:** "This is why what worked in your 30s doesn't work now. Your biology changed."

**Rationale:** Validates experience, removes shame, introduces mechanism as age-appropriate solution.

---

**MMA Strategy Alignment:** 8.2/10
**Recommendation:** All 3 angles viable for cold traffic. Angle 3 strongest for avatar resonance.
```

---

### STEP 3: User Selection (Simulated)
**Action:** Select Angle 3 for production

**SESSION_STATE Update:**
```json
{
  "asset_queue": [
    {
      "asset_id": "adv-test-001",
      "type": "advertorial",
      "status": "draft_complete",
      "current_phase": "draft",
      "selected_angle": {
        "id": "angle_3",
        "name": "The Hormonal Shift Nobody Talks About",
        "selected_at": "2026-01-11T02:30:00Z"
      },
      "fix_count": {},
      "mma_scores": [
        {"timestamp": "...", "dimension": "strategy_alignment", "score": 8.2, "verdict": "PASS"}
      ]
    }
  ]
}
```

---

## 🧪 TESTING APPROACHES

### Approach A: Manual ZPWO Simulation (Recommended First)
**Method:** Manually execute ZPWO logic without building slash commands yet

**Steps:**
1. Read ZPWO orchestration logic from skill XML
2. Manually route to advertorial_copy_master skill
3. Load skill with PROJECT_BRIEF + MESSAGE_SPINE context
4. Execute draft angle generation
5. Validate output manually against MMA criteria
6. Update SESSION_STATE by hand
7. Document what worked and what didn't

**Pros:**
- Fast to test
- Helps understand orchestration flow
- Identifies gaps before building automation

**Cons:**
- Manual, not automated
- Doesn't test actual command invocation

---

### Approach B: Build /draft Slash Command
**Method:** Create actual slash command that invokes ZPWO orchestration

**Steps:**
1. Check if `.claude/commands/` directory exists
2. Create `/draft` command file (markdown or YAML)
3. Command should:
   - Parse arguments (--asset=advertorial)
   - Load SESSION_STATE
   - Invoke ZPWO routing logic
   - Call appropriate skill
   - Update SESSION_STATE
   - Return results

**Pros:**
- Real workflow automation
- Reusable for future runs
- Tests actual command system

**Cons:**
- More setup required
- Need to understand Claude Code command format

---

### Approach C: Task Tool Sub-Agent
**Method:** Use Claude Code's Task tool to spawn advertorial_copy_master as sub-agent

**Steps:**
1. Load PROJECT_BRIEF + MESSAGE_SPINE
2. Use Task tool with prompt:
   ```
   You are the advertorial_copy_master skill.
   Load ssot/test_workflow/PROJECT_BRIEF.yaml and MESSAGE_SPINE.yaml.
   Generate 3-5 draft angles for a cold-traffic advertorial.
   Follow Draft Phase (P1) logic: volume over perfection, strategy alignment only.
   ```
3. Receive angles from sub-agent
4. Validate with MMA logic
5. Update SESSION_STATE

**Pros:**
- Uses Claude Code's built-in sub-agent system
- Parallel execution possible
- Tests skill invocation pattern

**Cons:**
- Task tool interface (not slash commands)
- Still need orchestration wrapper

---

## 📊 OBSERVATION CHECKLIST

### During Test Execution

**ZPWO Routing:**
- [ ] Does ZPWO correctly identify asset type from command?
- [ ] Does routing table mapping work (advertorial → advertorial_copy_master)?
- [ ] Is correct model selected (opus for advertorial)?

**Phase Context:**
- [ ] Is `active_phase` set to "draft"?
- [ ] Is phase recorded in `phase_history`?
- [ ] Are phase-specific constraints applied?

**SSOT Loading:**
- [ ] Are PROJECT_BRIEF and MESSAGE_SPINE loaded?
- [ ] Are they marked as `locked: true`?
- [ ] Are checksums verified?

**Two-Brain Pod:**
- [ ] Is LEFT brain engaged (schema validation)?
- [ ] Is RIGHT brain engaged (angle generation)?
- [ ] Are both perspectives reflected in output?

**MMA Validation:**
- [ ] Is strategy alignment checked?
- [ ] Is threshold ≥7.0 enforced?
- [ ] Are other dimensions skipped (draft phase = light validation)?

**SESSION_STATE Maintenance:**
- [ ] Is asset added to `asset_queue`?
- [ ] Is `fix_count` initialized?
- [ ] Are `mma_scores` recorded?
- [ ] Is `updated_at` timestamp current?

**Output Quality:**
- [ ] Are 3-5 angles generated?
- [ ] Does each angle have hook, angle, bridge, rationale?
- [ ] Are angles aligned with MESSAGE_SPINE mechanism?
- [ ] Are angles appropriate for cold traffic?

---

## 🎯 SUCCESS METRICS

### Minimum Viable Success
- ✅ At least 3 angles generated
- ✅ Angles reference cortisol-melatonin mechanism
- ✅ Strategy alignment ≥7.0
- ✅ SESSION_STATE updated

### Full Success
- ✅ All minimum criteria PLUS:
- ✅ ZPWO routing works automatically
- ✅ Two-Brain Pod coordination evident
- ✅ SSOT locking verified
- ✅ MMA validation integrated
- ✅ Phase transitions tracked

### Stretch Success
- ✅ All full success criteria PLUS:
- ✅ Slash command automation working
- ✅ Sub-agent spawning functional
- ✅ Full P1 → P2 workflow tested
- ✅ Circuit breakers tested

---

## 🚨 FAILURE MODES TO WATCH FOR

### Routing Failures
- ❌ ZPWO doesn't recognize asset type
- ❌ Wrong skill invoked
- ❌ Skill file not found

**Recovery:** Verify routing table, check skill file paths

### Context Failures
- ❌ SSOT objects not loaded
- ❌ MESSAGE_SPINE not available to skill
- ❌ Phase context not set

**Recovery:** Check SSOT file paths, verify locking mechanism

### Validation Failures
- ❌ MMA not invoked
- ❌ Strategy alignment not checked
- ❌ Angles don't align with mechanism

**Recovery:** Review MMA integration points, check validation logic

### State Management Failures
- ❌ SESSION_STATE not updated
- ❌ Asset not added to queue
- ❌ Phase history not tracked

**Recovery:** Verify SESSION_STATE schema, check update logic

---

## 📝 DOCUMENTATION REQUIREMENTS

### During Test
Document in real-time:
1. What command/action was taken
2. What was expected to happen
3. What actually happened
4. Any errors or issues
5. How issues were resolved

### After Test
Create summary report:
1. What worked well
2. What didn't work
3. Gaps identified
4. Skills needed (evidence_pack_builder, etc.)
5. Next steps

---

## 🔄 NEXT ITERATION PLANNING

### If Test Succeeds
**Next Steps:**
1. Build `/produce` phase test
2. Add MMA deep validation
3. Test FIX loop mechanism
4. Verify circuit breakers

### If Test Partially Succeeds
**Next Steps:**
1. Fix identified issues
2. Re-run with improvements
3. Document workarounds
4. Identify systemic vs. one-off problems

### If Test Fails
**Next Steps:**
1. Identify root cause
2. Simplify test scope
3. Build missing infrastructure
4. Re-attempt with minimal viable test

---

## 🎬 RECOMMENDED EXECUTION

### Step 1: Manual Simulation (15-30 min)
Test Approach A to understand flow

### Step 2: Document Learnings (15 min)
Capture what worked and what didn't

### Step 3: Decide Next Step (5 min)
Choose: Build slash command, use Task tool, or refine simulation

### Step 4: Execute Next Step (30-60 min)
Implement chosen approach

### Step 5: Final Documentation (15 min)
Update session log with complete findings

---

## 📦 DELIVERABLES

### From This Test
1. ✅ Test SSOT objects (PROJECT_BRIEF, MESSAGE_SPINE, SESSION_STATE)
2. ✅ Test plan (this document)
3. 📋 Generated advertorial angles (pending execution)
4. 📋 MMA validation report (pending execution)
5. 📋 Updated SESSION_STATE (pending execution)
6. 📋 Session learnings log (pending execution)

### For Future Use
- Reusable test workflow pattern
- ZPWO orchestration template
- Slash command structure (if built)
- Sub-agent invocation pattern

---

**Status:** Test plan complete. Ready for execution.

**Recommended Start:** Approach A (Manual Simulation) to quickly test orchestration logic.

**Next Session:** Execute test, document results, plan P2 (Production) phase test.
