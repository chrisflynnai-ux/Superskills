# NotebookLM Prompts (Condensed for Token Limits) v2.1

**Pipeline:** NotebookLM → GPT Stage-2 Synthesizer → Claude Code Skill Builder v1.2.0
**Status:** Production-ready, token-optimized
**Date:** 2026-01-18

---

## SETUP (2 minutes)

1. Create Notebook: `[DOMAIN] Knowledge Synthesis`
2. Upload sources (transcripts, videos, notes)
3. Run prompts in sequence

---

# PROMPT #1 — COMPENDIUM (Grounded Knowledge Extraction)

Paste this into NotebookLM:

```
You are ULTRAMIND Compendium Builder for [DOMAIN].

Extract grounded, source-tagged knowledge from all sources.

REQUIREMENTS:
- Tag every claim: [SRC: source_name | timestamp]
- Include direct quotes (≤25 words) for key principles
- Favor "how-to" over theory

OUTPUT STRUCTURE:

A) SOURCE MAP
List each source: ID, title, author, key topics, unique contribution

B) TAXONOMY
Categories, subcategories, consensus points, divergences, gaps

C) FRAMEWORKS (10-20)
For each:
- Name, source tag, key quote (≤25 words)
- Summary, when to use, when NOT to use
- Steps (actionable sequence)
- Key metrics, failure modes

D) SOPs (10-15)
Operational procedures: name, frequency, steps, quality gates

E) HEURISTICS (25-50)
IF-THEN format grouped by:
- Diagnostic (identifying problems)
- Optimization (improving)
- Scaling (when/how)
- Troubleshooting (fixing)

F) METRICS TABLE
Symptom | Cause | Diagnostic Test | Fix | Source

G) PATTERNS (15-25)
Hooks, authority, proof, mechanisms, offers, objections, CTAs

H) FAILURE MODES (15+)
Name, symptoms, root cause, diagnosis steps, recovery, prevention

I) GOLDEN RUNS (3-5)
Test case: scenario, inputs, expected outputs, success criteria

J) COMPLIANCE
Platform rules, safe phrasing, red flags

K) CHECKLISTS
Launch, daily ops, weekly review, scaling

Deliver as structured markdown with YAML blocks.
```

---

# PROMPT #2 — KNOWLEDGE BASE + SKILL PACK

Paste this AFTER Prompt #1 completes:

```
Using the Compendium above, create:

1) KNOWLEDGE BASE v1.1 (YAML format):

meta_topic: "[Domain]"

core_thesis:
  primary_thesis: "[1-2 sentences]"
  big_promises: [3 outcomes]
  underlying_assumptions: [3 beliefs]
  sources: [SRC: ...]

mechanisms: [3-7 with name, explanation, signals, decision_impact, quote]

frameworks: [10-20 with name, summary, when_to_use, steps, metrics, quote]

heuristics:
  diagnostic: [IF-THEN rules]
  optimization: [IF-THEN rules]
  scaling: [IF-THEN rules]
  troubleshooting: [IF-THEN rules]

anti_patterns: [3-7 with label, description, why_harmful, instead_do]

failure_modes: [15+ with symptoms, cause, diagnosis, recovery, prevention]

golden_runs: [3-5 test cases]

agent_behavior_rules: [5-10 operational rules]

humanizing_elements:
  metaphors: [...]
  story_arc: "[pattern]"
  values: [...]

compliance: [rules, safe phrasing, red flags]

2) SKILL INPUT PACK:

skill_name: "[Domain] Master v1.0.0"
skill_purpose: "[1-2 sentences]"
target_users: [...]
use_cases: [3-5 with input/output]
ssot_objects_required: [...]

progressive_disclosure_layers:
  L1: [Core identity, high-level workflow]
  L2: [Frameworks, heuristics]
  L3: [SOPs, failure modes]
  L4: [Examples, edge cases]

two_brain_pod:
  left_brain: [technical responsibilities]
  right_brain: [strategic responsibilities]

Output both as separate files ready for GPT Stage-2 Synthesizer.
```

---

# PROMPT #3 — PATTERN LIBRARY (Optional)

Paste this if you want tactical patterns for insights.md:

```
Extract tactical patterns from Compendium in ULTRAMIND format:

For each pattern:

pattern_id: "p_[XXX]"
pattern_name: "[Name]"
category: "[hook/authority/mechanism/offer/objection/etc.]"
when_to_use: "[contexts]"
when_NOT_to_use: "[contexts]"
structure: "[template]"
examples: [2+ with source, text, context]
mma_impact: [SMART/SAFE/SPECIAL/etc. predictions]
voice_compatibility: [voice types]
funnel_types: [domains]
effectiveness_rating: [X.X/10]

Extract 10-20 patterns total.

Categories:
- Hooks, Authority, Proof, Mechanisms, Offers, Objections, CTAs, Transitions, Pattern Interrupts, Identity Shifts

Output as YAML list.
```

---

## CONDENSED WORKFLOW

**Step 1:** Run Prompt #1 → Get Compendium
**Step 2:** Run Prompt #2 → Get KB + Skill Pack
**Step 3:** Send KB + Skill Pack to GPT Stage-2 Synthesizer
**Step 4:** GPT outputs Skill Package Draft
**Step 5:** Feed to Claude Code Skill Builder v1.2.0
**Step 6:** (Optional) Run Prompt #3 for patterns

---

## VALIDATION CHECKLIST

Before sending to GPT, verify:
- [ ] 10-20 frameworks
- [ ] 25-50 heuristics (IF-THEN)
- [ ] 15+ failure modes
- [ ] 3-5 golden runs
- [ ] All source-tagged [SRC: ...]
- [ ] Direct quotes included (≤25 words)

---

**Token-Optimized:** Each prompt ~200-300 tokens
**Output:** Compendium (~5-10 pages), KB (~3-5 pages), Patterns (~2-3 pages)
