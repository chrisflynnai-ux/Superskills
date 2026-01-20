# Pipeline Comparison & NotebookLM Extraction Prompt

**Date:** 2026-01-18
**Purpose:** Compare Knowledge Skill Synthesis Pipeline to existing ULTRAMIND pattern extraction, create NotebookLM prompt

---

## 1. PIPELINE COMPARISON

### **Current ULTRAMIND Pattern Extraction Pipeline**

**Location:** `.claude/skills/research/` + `outputs/` analysis files

**Flow:**
```
Raw Asset (Sales Page, VSL, etc.)
    ↓
Sales Page Deconstructor v2.1.0 OR VSL Script Analyzer v1.0.0
    ↓
6-Dimension Analysis:
1. Structure Extraction
2. Mechanism Analysis
3. Offer Architecture
4. Voice Signature
5. 7S/7F Coverage (with Neuro-Box mapping)
6. Neuro-Box 6D (neurochemical activation)
    ↓
Pattern Extraction (p_087-p_113)
- Pattern ID, name, category
- When_to_use / When_NOT_to_use
- MMA impact predictions
- Examples from source
    ↓
Pattern Library (insights.md)
- 24 validated patterns
- Cross-referenced to skills
- Patch proposals generated
    ↓
Skill Enhancement (Patches applied to existing skills)
```

**Characteristics:**
- ✅ **Automated extraction** (Python tools + LLM analysis)
- ✅ **Quantitative validation** (MMA scoring, neurochemical balance)
- ✅ **Pattern-centric** (patterns = reusable building blocks)
- ✅ **Skill-focused** (output = skill patches)
- ⚠️ **Single-source** (analyzes one asset at a time)
- ⚠️ **Marketing-specific** (sales pages, VSLs, email copy)

---

### **Knowledge Skill Synthesis Pipeline (3-Stage)**

**Location:** `.claude/skills/knowledge/Knowledge Skill Synthesis Pipeline/`

**Flow:**
```
Stage 1: Masterclass Summarization (NotebookLM or manual)
    ↓
Raw Content (Course, Book, Training, etc.)
    ↓
Masterclass Summary Document:
- Big picture / thesis
- Modules
- Frameworks / processes
- Principles & heuristics
- Mistakes / anti-patterns
- Implementation ideas
- Style / teaching flavor
    ↓
Stage 2: Meta Knowledge Synthesizer (Merge 2-5 masterclasses)
    ↓
XML Patch (Unified Conceptual Model):
- Core thesis (2-5 points)
- Mechanisms (3-7 canonical)
- Frameworks (3-7 step-by-step)
- Heuristics (5-10 decision rules)
- Anti-patterns (3-7 warnings)
- Agent behavior rules (5-10 SOPs)
- Humanizing elements (1-5 metaphors/values)
    ↓
Stage 3: Skill Formation (XML → Agentic Skill)
    ↓
Production-Ready Skill with:
- L1-L4 progressive disclosure
- Two-Brain Pod architecture
- ECR self-improvement
- MMA validation
```

**Characteristics:**
- ✅ **Multi-source synthesis** (merges 2-5 sources on same topic)
- ✅ **Knowledge-centric** (mechanisms, frameworks, heuristics)
- ✅ **Canonical extraction** (finds shared truth across sources)
- ✅ **Agent behavior focus** (how to think, not just what to do)
- ✅ **Domain-agnostic** (works for ANY topic)
- ⚠️ **Manual Stage 1** (requires human-curated masterclass summaries)
- ⚠️ **No quantitative validation** (relies on conceptual merging)

---

## 2. KEY DIFFERENCES

| Dimension | ULTRAMIND Pattern Extraction | Knowledge Skill Synthesis |
|-----------|------------------------------|---------------------------|
| **Input** | Single asset (sales page, VSL) | 2-5 masterclasses on same topic |
| **Extraction Focus** | Patterns (reusable tactics) | Mechanisms + Frameworks (mental models) |
| **Validation** | Quantitative (MMA, Neuro-Box scores) | Conceptual (canonical truth across sources) |
| **Output** | Pattern library → Skill patches | XML patch → Full skill |
| **Automation** | High (Python tools + LLM) | Medium (Stage 1 manual, Stages 2-3 automated) |
| **Domain** | Marketing/Copy-specific | Domain-agnostic |
| **Granularity** | Micro (sentence-level patterns) | Macro (worldview, mental models) |
| **Integration** | Incremental (patch existing skills) | Generative (build new skill from scratch) |

---

## 3. SYNTHESIS OPPORTUNITIES

### **Option 1: Use BOTH Pipelines (Complementary)**

**When to use Pattern Extraction:**
- Analyzing high-performing marketing assets
- Extracting tactical patterns (hooks, CTAs, proof structures)
- Validating copy quality (MMA, Neuro-Box)
- Patching existing copy skills

**When to use Knowledge Synthesis:**
- Building new skills in non-marketing domains
- Synthesizing knowledge from courses/books/trainings
- Creating mental model-based skills
- Merging multiple expert perspectives

**Example:**
- Use **Pattern Extraction** for: "Analyze top 10 VSLs → extract tactical patterns"
- Use **Knowledge Synthesis** for: "Merge 3 sleep optimization courses → build Sleep Coach skill"

---

### **Option 2: Hybrid Pipeline (Best of Both)**

**Proposed Unified Flow:**
```
Stage 0: Source Ingestion
├── Marketing Assets → Pattern Extraction Pipeline
└── Courses/Books/Trainings → Knowledge Synthesis Pipeline
    ↓
Stage 1: Extraction
├── Pattern Extraction → Tactical patterns (p_XXX format)
└── Masterclass Synthesis → Mechanisms, frameworks, heuristics
    ↓
Stage 2: Canonical Merging
- Merge patterns + mechanisms into unified model
- Validate patterns against frameworks
- Resolve conflicts (pattern vs mechanism)
- Generate canonical truth
    ↓
Stage 3: Skill Formation
- Combine tactical patterns + mental models
- Build Two-Brain Pod (Left = patterns/tactics, Right = frameworks/strategy)
- Add ECR self-improvement
- Apply MMA validation
    ↓
Production Skill (Pattern-Enhanced + Knowledge-Grounded)
```

---

## 4. NOTEBOOKLM EXTRACTION PROMPT

**Purpose:** Extract frameworks, patterns, methods, systems, and strategies from courses/trainings for Stage 1 Masterclass Synthesis

---

### **NotebookLM Prompt Template v1.0**

```markdown
# MASTERCLASS SYNTHESIS EXTRACTION

You are a Stage-1 Knowledge Synthesizer. Your role is to extract actionable, decision-changing knowledge from training content.

---

## EXTRACTION FRAMEWORK

Analyze the provided training content and extract the following 7 layers:

---

### **1. CORE THESIS (Big Picture Truth)**

What does this training claim is TRUE about [topic]?

Extract:
- **Primary Thesis** (1-2 sentences): The core belief or worldview
- **Big Promises** (2-3 bullet points): What outcomes does this enable?
- **Underlying Assumptions** (2-3 bullet points): What must be true for this to work?

Example:
```yaml
primary_thesis: "Sleep optimization requires addressing cortisol-melatonin balance, not just sleep hygiene."
big_promises:
  - "Restore deep sleep within 7-14 days"
  - "Eliminate 3pm energy crashes"
  - "Improve metabolic health markers"
underlying_assumptions:
  - "Most sleep issues are hormone-driven, not behavioral"
  - "Sleep supplements without rhythm reset fail"
  - "Morning light exposure is more critical than evening routine"
```

---

### **2. MECHANISMS (How Things Really Work)**

What are the KEY LENSES or MENTAL MODELS for understanding [topic]?

Extract 3-7 canonical mechanisms:

For each mechanism:
- **Name** (short, clear, descriptive)
- **Explanation** (what it explains, why it matters)
- **Signals** (when to apply this lens)
- **Decision Impact** (how it changes what you do)

Example:
```yaml
mechanisms:
  - name: "Cortisol-Melatonin Rhythm Reset"
    explanation: "Body's stress hormone (cortisol) and sleep hormone (melatonin) must follow opposing curves. When cortisol stays elevated at night, melatonin can't rise."
    signals:
      - "Can't fall asleep despite being tired"
      - "Wake up feeling wired at 2-3am"
      - "Need stimulants to function in morning"
    decision_impact: "Prioritize cortisol reduction (magnesium, ashwagandha, cold exposure) over sleep aids."

  - name: "Deep Sleep Deficiency Loop"
    explanation: "Missing deep sleep → poor glucose metabolism → cortisol spike → worse sleep → repeat"
    signals:
      - "Wake up after 8 hours still exhausted"
      - "Sugar cravings intensify"
      - "Weight gain despite no diet change"
    decision_impact: "Must address deep sleep architecture (temperature, timing) before optimizing REM."
```

---

### **3. FRAMEWORKS (Step-by-Step Processes)**

What are the ACTIONABLE PROCESSES taught in this training?

Extract 3-7 frameworks:

For each framework:
- **Name**
- **Summary** (what problem it solves)
- **When_to_use** (specific contexts)
- **Steps** (clear, actionable sequence)

Example:
```yaml
frameworks:
  - name: "7-Day Rhythm Reset Protocol"
    summary: "Re-sync circadian rhythm in 7 days without medication"
    when_to_use: "When sleep onset is delayed (can't fall asleep before midnight) or wake times are inconsistent"
    steps:
      1. "Day 1-3: Wake at same time (6am) regardless of sleep quality. No naps."
      2. "Day 1-7: Get 10+ min direct sunlight within 30 min of waking."
      3. "Day 1-7: No caffeine after 12pm. No screens after 8pm."
      4. "Day 3-7: Add cold exposure (2 min cold shower) at 6pm to drop core temp."
      5. "Day 5-7: Introduce magnesium glycinate (400mg) + L-theanine (200mg) at 8pm."
      6. "Day 7: Evaluate. If sleep onset < 11pm, continue. If not, add melatonin (0.3mg) for next 7 days."
```

---

### **4. HEURISTICS (Decision Rules)**

What RULES-OF-THUMB guide decisions in [topic]?

Extract 5-10 heuristics in IF-THEN format:

Example:
```yaml
heuristics:
  - "IF wake time is inconsistent (varies >1 hour) THEN fix wake time BEFORE optimizing sleep onset."
  - "IF caffeine after 2pm → poor sleep THEN eliminate all caffeine for 14 days, then reintroduce only before 10am."
  - "IF waking at 2-3am consistently THEN suspect blood sugar crash → add protein/fat snack at 9pm."
  - "IF sleep supplements aren't working THEN check magnesium status first (90% deficient)."
  - "IF stress/anxiety prevents sleep THEN prioritize cortisol management (breathwork, cold exposure) over sedatives."
```

---

### **5. ANTI-PATTERNS (What NOT to Do)**

What MISTAKES does this training warn against?

Extract 3-7 anti-patterns:

For each:
- **Label** (short name for the mistake)
- **Description** (what people do wrong)
- **Why Harmful** (consequences)
- **Instead Do** (correct approach)

Example:
```yaml
anti_patterns:
  - label: "Melatonin Megadosing"
    description: "Taking 5-10mg melatonin nightly without addressing root cause"
    why_harmful: "Downregulates natural melatonin production, creates dependency, disrupts hormone balance"
    instead_do: "Use 0.3mg melatonin (physiological dose) only for rhythm reset, not long-term"

  - label: "Sleep Hygiene Theater"
    description: "Focusing only on behavioral tips (dark room, cool temp) while ignoring metabolic/hormonal issues"
    why_harmful: "Works for 20% of people, fails for those with hormone dysregulation"
    instead_do: "Test cortisol rhythm first, then layer behavioral changes"
```

---

### **6. AGENT BEHAVIOR RULES (How to Apply)**

If an AI agent were teaching [topic], how should it ALWAYS behave?

Extract 5-10 operational rules:

Example:
```yaml
agent_behavior_rules:
  - "ALWAYS start by asking about wake consistency before recommending sleep aids."
  - "ALWAYS validate hormone status (cortisol, thyroid) before attributing issues to 'stress' or 'poor habits'."
  - "When presenting frameworks, start with simplest (wake time fixing) before advanced (supplement stacking)."
  - "Never recommend melatonin >0.5mg without explaining dependency risk."
  - "If user reports 'tried everything', probe for blood sugar, magnesium, or thyroid issues."
  - "Present options as experiments, not prescriptions (e.g., 'Let's test this for 7 days')."
```

---

### **7. HUMANIZING ELEMENTS (Tone & Feel)**

What METAPHORS, STORY PATTERNS, or VALUES define this training's style?

Extract 1-5 elements:

Example:
```yaml
humanizing_elements:
  - metaphor: "Treat sleep like a lab experiment, not a battleground. Test, measure, adjust."
  - story_arc: "Struggle (exhaustion) → Insight (cortisol rhythm broken) → Experiment (7-day protocol) → Breakthrough (first deep sleep in years)"
  - values:
      - "Curiosity over compliance (explore what works for YOUR body)"
      - "Data-driven compassion (measure objectively, adapt with kindness)"
      - "Simplicity first (fix one thing at a time)"
```

---

## OUTPUT FORMAT

Deliver as structured YAML with all 7 layers:

```yaml
meta_topic: "[Topic Name - e.g., Sleep Optimization, Email Campaigns, etc.]"

core_thesis:
  primary_thesis: "..."
  big_promises: [...]
  underlying_assumptions: [...]

mechanisms:
  - name: "..."
    explanation: "..."
    signals: [...]
    decision_impact: "..."

frameworks:
  - name: "..."
    summary: "..."
    when_to_use: "..."
    steps: [...]

heuristics:
  - "IF [...] THEN [...]"

anti_patterns:
  - label: "..."
    description: "..."
    why_harmful: "..."
    instead_do: "..."

agent_behavior_rules:
  - "..."

humanizing_elements:
  - metaphor: "..."
  - story_arc: "..."
  - values: [...]
```

---

## EXTRACTION PRIORITIES

**Less but better:**
- Extract ONLY decision-changing knowledge
- Ignore nice-to-have trivia
- Focus on what changes behavior

**Canonical over comprehensive:**
- Choose ONE clear name for mechanisms (not 3 similar ones)
- Merge redundant frameworks
- Resolve conflicts with IF-THEN conditionals

**Action-oriented:**
- Every extracted element should enable an agent to:
  - Diagnose situations
  - Choose frameworks
  - Avoid mistakes
  - Explain clearly

---

## USAGE INSTRUCTIONS FOR NOTEBOOKLM

1. Upload training content (video transcript, PDF, course notes)
2. Paste this entire prompt into NotebookLM
3. Ask: "Using the MASTERCLASS SYNTHESIS EXTRACTION framework above, analyze the uploaded training content and output structured YAML."
4. Review output for completeness (all 7 layers extracted)
5. Refine as needed (add missing mechanisms, clarify heuristics)
6. Save output as `[topic]_masterclass_stage1.yaml`
7. Repeat for 2-5 related trainings on same topic
8. Feed all Stage-1 outputs into Stage-2 Meta Synthesizer

---

## VALIDATION CHECKLIST

Before submitting Stage-1 output, verify:

- [ ] Core thesis is 1-2 sentences (not a paragraph)
- [ ] 3-7 mechanisms extracted (not 15)
- [ ] Each mechanism has clear decision_impact
- [ ] 3-7 frameworks with actionable steps
- [ ] Heuristics are IF-THEN format
- [ ] Anti-patterns have "instead_do" alternatives
- [ ] Agent behavior rules are operational (not abstract)
- [ ] Humanizing elements capture unique training flavor

---

**END OF NOTEBOOKLM PROMPT**
```

---

## 5. INTEGRATION RECOMMENDATION

### **Immediate Action:**

1. **Test NotebookLM Prompt** on existing training content (e.g., Fernando Oliver's Direct Response Ecommerce Masterclass)
   - Upload transcript/notes
   - Run extraction prompt
   - Validate output quality

2. **Compare outputs:**
   - Pattern Extraction (existing): Tactical patterns from VSL analysis
   - Knowledge Synthesis (new): Frameworks/mechanisms from course content
   - Identify overlap and gaps

3. **Decide on pipeline strategy:**
   - **Option A:** Keep separate (use each for different content types)
   - **Option B:** Merge into hybrid pipeline (best of both)

---

## 6. NEXT SESSION PRIORITIES

**Updated based on this analysis:**

1. **Test NotebookLM Extraction:**
   - Run prompt on 1-2 existing course materials
   - Validate YAML output quality
   - Refine prompt if needed

2. **VSL Skill Enhancements (as planned):**
   - Apply HIGH priority patches to sales_page_copywriter_lite
   - Apply patches to advertorial_copy_master
   - Build High-Ticket VSL Script Writer v1.0.0

3. **Framework Gathering (as planned):**
   - Collect frameworks user provided in previous message
   - Organize into pattern library
   - Map to existing skills

---

**Status:** Pipeline comparison complete, NotebookLM prompt ready for testing
**Deliverable:** PIPELINE_COMPARISON_AND_NOTEBOOKLM_PROMPT_2026-01-18.md

---
