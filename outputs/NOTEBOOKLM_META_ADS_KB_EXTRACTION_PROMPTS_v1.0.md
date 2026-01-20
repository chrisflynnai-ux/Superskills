# NotebookLM Meta Ads KB Module Extraction Prompts v1.0

**Purpose:** Extract granular frameworks, methods, patterns, and strategy cards for 7 Meta Ads KB modules
**Workflow:** NotebookLM extraction → GPT Stage-2 synthesis → Claude KB module builder
**Date:** 2026-01-19

---

## SETUP INSTRUCTIONS (2 minutes per module)

**For each KB module:**
1. Create new Notebook: `[KB Module Name] - Meta Ads Knowledge Extraction`
2. Upload source materials: training videos, masterclasses, transcripts, swipe files, case studies
3. Run the corresponding prompt below (7 prompts total, one per KB module)
4. Save output as: `KB_[MODULE_NAME]_COMPENDIUM_RAW.md`
5. Send all 7 raw compendiums to GPT Stage-2 Synthesizer
6. GPT outputs KB drafts → Claude builds final XML modules

---

## PROMPT #1 — KB-CAMPAIGN-ARCHITECTURE (M3 Swim Lanes & Structure)

**Notebook Name:** `Campaign Architecture - Meta Ads Knowledge Extraction`

**Upload Sources:** Campaign structure guides, M3 swim lane tutorials, budget allocation frameworks, learning phase mechanics

**Paste this into NotebookLM:**

```
You are ULTRAMIND Knowledge Extractor for META ADS CAMPAIGN ARCHITECTURE.

Extract grounded, source-tagged knowledge about campaign structure, M3 swim lanes, budget allocation, and learning phase mechanics.

FOCUS AREAS:
- M3 Swim Lane Architecture (Prospecting/Retargeting/Retention separation)
- Campaign structure frameworks (3:2:2, 5x5 testing matrices)
- Budget allocation formulas (learning phase minimums, scaling increments)
- Audience exclusion logic (preventing overlap between swim lanes)
- Placement strategy (Automatic vs Manual)
- Campaign naming conventions
- Platform architecture (Pixel, Conversion API, attribution windows)

REQUIREMENTS:
- Tag every claim: [SRC: source_name | timestamp]
- Include direct quotes (≤25 words) for key principles
- Favor "how-to" over theory (actionable steps, not concepts)

OUTPUT STRUCTURE:

A) SOURCE MAP
List each source: ID, title, author, key topics covered, unique contribution

B) TAXONOMY
Categories: M3 Architecture, Budget Management, Learning Phase, Exclusions, Platform Setup
Subcategories: Prospecting setup, Retargeting setup, Retention setup, Budget formulas, Scaling rules
Consensus points: What do all sources agree on?
Divergences: Where do sources contradict or offer different approaches?
Gaps: What's missing from the source material?

C) FRAMEWORKS (8-15)
For each framework:
- Name: [Clear descriptive name]
- Source tag: [SRC: ...]
- Key quote: [≤25 words, verbatim from source]
- Summary: [What this framework does, 2-3 sentences]
- When to use: [Specific contexts, conditions, triggers]
- When NOT to use: [Exclusions, anti-patterns, wrong contexts]
- Steps: [Actionable sequence, numbered, clear]
- Key metrics: [What to measure, success thresholds]
- Failure modes: [What goes wrong, how to detect]

Example frameworks to extract:
1. M3 Swim Lane Architecture
2. 3:2:2 Flexible Ad System
3. 5x5 Testing Matrix
4. Learning Phase Optimization
5. Budget Allocation Formula
6. Audience Exclusion Protocol
7. Campaign Consolidation Framework
8. Placement Strategy Decision Tree
9. Pixel + Conversion API Setup
10. Attribution Window Configuration

D) SOPs (Standard Operating Procedures) (5-10)
Operational procedures with frequency, steps, quality gates:
- Campaign launch checklist (pre-launch validation)
- Daily monitoring SOP (what to check, when to intervene)
- Weekly performance review SOP
- Budget scaling protocol (when/how to increase spend)
- Campaign consolidation SOP (when to merge ad sets)

E) HEURISTICS (20-40 IF-THEN rules)
Group by category:

1. DIAGNOSTIC (Identifying problems):
   - IF learning limited 7+ days THEN consolidate campaigns or increase budget
   - IF budget unspent 50%+ THEN increase audience size or bid cap too low
   - IF frequency >3.5 in prospecting THEN audience too narrow

2. OPTIMIZATION (Improving performance):
   - IF profitable CPA achieved THEN scale budget 20% every 3-5 days max
   - IF campaign spending <50% budget THEN expand audience or reduce bid cap
   - IF multiple ad sets in same swim lane THEN consolidate for faster learning

3. SCALING (Growth decisions):
   - IF spending <$10k/month THEN use 3:2:2 framework
   - IF spending $20k+/month THEN use 5x5 framework
   - IF spending $50k+/month THEN build 3-5 prospecting campaigns (avoid single campaign ceiling)

4. TROUBLESHOOTING (Fixing issues):
   - IF retargeting outperforms prospecting 3x+ THEN prospecting creative weak
   - IF all ad sets learning limited THEN budget too low or audience too narrow
   - IF exclusions not working THEN check custom audience refresh rate

F) METRICS TABLE
| Metric | Purpose | Threshold | Action Trigger | Source |
|--------|---------|-----------|----------------|--------|
| Learning Phase Status | Campaign optimization | "Learning" >7 days | Consolidate or increase budget | [SRC] |
| Budget Delivery % | Spend pacing | <50% spent | Expand audience or reduce bid cap | [SRC] |
| Frequency | Audience saturation | >3.5 | Audience too narrow, expand | [SRC] |
| Ad Set Count per Campaign | Learning efficiency | >5 ad sets | Consolidate for faster learning | [SRC] |

G) PATTERNS (10-20)
Campaign structure patterns, naming conventions, setup sequences:
- Campaign naming pattern: [LANE]_[OBJECTIVE]_[CREATIVE_ANGLE]_[DATE]
- M3 setup sequence: Prospecting first → validate → add Retargeting → add Retention
- Exclusion chain: Prospecting excludes (Retargeting + Retention), Retargeting excludes Retention

H) FAILURE MODES (8-12)
For each failure mode:
- Name: [Short descriptive label]
- Symptoms: [Observable signals, metrics, delivery status]
- Root cause: [Why it happens, mechanism breakdown]
- Diagnosis steps: [How to confirm, specific checks]
- Recovery: [Step-by-step fix, prioritized actions]
- Prevention: [Proactive monitoring, process changes]

Example failure modes:
1. Learning Limited Loop
2. Budget Unspent
3. Audience Fragmentation
4. Exclusion Logic Failure
5. Retargeting Pool Exhaustion
6. Over-Segmentation
7. Campaign Sprawl
8. Attribution Drift (M3 lanes bleeding)

I) GOLDEN RUNS (2-4)
Test scenarios with inputs, expected outputs, success criteria:
- Scenario 1: New campaign launch (Ecom DTC, $10k/month budget)
  - Inputs: Offer, budget, target ncROAS
  - Expected outputs: M3 campaign structure, budget allocation, exclusions set
  - Success criteria: Learning phase starts within 24h, budget spends 80%+, no exclusion errors

J) COMPLIANCE & GUARDRAILS
- Platform rules: Meta Advertising Policies compliance
- Budget constraints: Minimum spend for learning phase (50 conversions/week)
- Exclusion requirements: No audience overlap between M3 lanes
- Scaling limits: 20% max budget increase per adjustment

K) CHECKLISTS
- Pre-launch: Campaign structure validated, exclusions set, budgets allocated, naming convention followed
- Daily ops: Budget delivery %, learning phase status, frequency check, spend pacing
- Weekly review: ncROAS by swim lane, consolidation opportunities, scaling readiness
- Scaling checklist: ncROAS >1.5x for 14+ days, MER stable, creative flywheel active

Deliver as structured markdown with YAML blocks for frameworks, metrics, and heuristics.
```

---

## PROMPT #2 — KB-ANDROMEDA-CREATIVE-ENGINE (Hooks, Frameworks, Concept Testing)

**Notebook Name:** `Andromeda Creative Engine - Meta Ads Knowledge Extraction`

**Upload Sources:** Creative testing case studies, hook frameworks, Andromeda algorithm guides, concept-over-variation research

**Paste this into NotebookLM:**

```
You are ULTRAMIND Knowledge Extractor for META ADS ANDROMEDA CREATIVE ENGINE.

Extract grounded, source-tagged knowledge about creative-as-targeting paradigm, hook generation frameworks, concept testing, and creative flywheel systems.

FOCUS AREAS:
- Andromeda Retrieval Engine (creative IS targeting, not demographics)
- 12 Creative Frameworks (Founder VSL, Hero vs Villain, Lazy Statics, Scam Hook, etc.)
- Concept Over Variation principle (test different stories, not color swaps)
- Creative Flywheel (Rule of 1:10k - ship 1 new creative per $10k monthly spend)
- Visual Hook Architecture (first 3 seconds determine success)
- Hook Rate optimization (>30% target)
- Self-selecting ICP hooks (psychographic targeting via creative)

REQUIREMENTS:
- Tag every claim: [SRC: source_name | timestamp]
- Include direct quotes (≤25 words) for key principles
- Favor "how-to" over theory

OUTPUT STRUCTURE:

A) SOURCE MAP
List each source: ID, title, author, key topics, unique contribution

B) TAXONOMY
Categories: Andromeda Paradigm, Hook Frameworks, Concept Testing, Creative Production, Performance Metrics
Subcategories: Hook types (curiosity, scam, founder story), Format types (static, video, carousel), Testing frameworks
Consensus points: What all sources agree on (e.g., creative IS targeting)
Divergences: Different approaches to hook generation or testing
Gaps: Missing creative frameworks or formats

C) FRAMEWORKS (12-20)
For each creative framework:
- Name
- Source tag: [SRC: ...]
- Key quote (≤25 words)
- Summary: What this framework produces
- When to use: Niche, offer type, awareness level
- When NOT to use: Wrong contexts, prerequisites
- Steps: How to create this creative type
- Key metrics: Hook Rate target, Hold Rate target, CTR target
- Failure modes: What goes wrong (hook-body mismatch, low Hook Rate)

CRITICAL FRAMEWORKS TO EXTRACT:
1. Andromeda Retrieval Engine (paradigm shift)
2. Concept Over Variation (testing philosophy)
3. Visual Hook Architecture (first 3 seconds structure)
4. 3-Step Viral Hook (Visual + Text + Audio)
5. Founder-Led VSL (Hook → Promise → Proof → Pivot → CTA)
6. Hero vs Villain Story (villain identification, stakes, plan)
7. Lazy Static Headlines (authentic images + text overlays)
8. Scam Hook Formula (contrarian positioning)
9. Nano Banana AI Static Machine (AI-accelerated scaling)
10. Post ID Harvesting (social proof preservation)
11. Creative Flywheel System (Rule of 1:10k production)
12. Hook-Body Alignment (ICP self-selection)
13. Native Format Matching (blend with feed, avoid "ad-like")
14. Visual Hook Audit (diagnostic for low Hook Rate)

D) SOPs (5-10)
- Weekly creative production sprint (how to ship 5-10 concepts)
- Concept diversity validation (ensure testing concepts not variations)
- Hook Rate baseline testing (first 48 hours)
- Creative rotation protocol (before fatigue hits, 14-day max)
- Creative bench building (maintain 3-5 concepts in queue)

E) HEURISTICS (25-50 IF-THEN rules)

DIAGNOSTIC:
- IF Hook Rate <25% THEN audit visual hook using Visual Hook Audit
- IF Hook Rate >35% but CPA high THEN hook-body mismatch (attracts wrong audience)
- IF all creatives perform within 10% THEN testing variations not concepts
- IF creative fatigue cycle <14 days THEN audience saturation or poor concept diversity

OPTIMIZATION:
- IF Hook Rate >35% and profitable CPA THEN scale candidate (create variants)
- IF Hold Rate >50% but low CTR THEN weak CTA or offer-creative mismatch
- IF high engagement but low conversion THEN awareness-stage traffic (wrong funnel stage)

SCALING:
- IF spending $10k+/month THEN ship 1+ new concept weekly (Rule of 1:10k)
- IF spending $50k+/month THEN ship 5+ concepts weekly
- IF winner identified THEN create 10-20 variants using Nano Banana framework

TROUBLESHOOTING:
- IF Hook Rate declining 30%+ from baseline THEN creative fatigue detected
- IF frequency >3.5 on winning creative THEN rotate before fatigue kills performance
- IF compliance flags received THEN audit hooks for sensationalism

F) METRICS TABLE
| Metric | Purpose | Threshold | Action Trigger | Source |
|--------|---------|-----------|----------------|--------|
| Hook Rate (3-sec) | Stop-scroll effectiveness | >30% good, >35% excellent | <25% = audit visual hook | [SRC] |
| Hold Rate (15-sec+) | Engagement depth | >50% good | <40% = weak story/proof | [SRC] |
| Click-Through Rate | Trust conversion | >2% good | <1% = weak CTA or offer mismatch | [SRC] |
| Concept Diversity Ratio | Variation vs concept testing | >70% unique hooks | <50% = testing variations | [SRC] |
| Creative Fatigue Cycle | Winner lifespan | 14-21 days typical | <14 days = audience saturation | [SRC] |

G) PATTERNS (15-25)
Hook patterns, creative structures, production workflows:
- Curiosity hook pattern: "The #1 mistake [avatar] make with [problem]..."
- Self-selecting hook: "If you're [ICP descriptor], watch this..."
- Contrarian hook: "Stop [common practice] — it's keeping you stuck"
- Benefit-driven hook: "[Outcome] in [timeframe] without [objection]"
- Founder VSL structure: 0-3sec hook → 3-15sec promise → 15-45sec proof → 45-60sec pivot → 60-90sec CTA
- Lazy Static production: Authentic image + bold text overlay + 2-3 sentence primary text

H) FAILURE MODES (10-15)
- Creative Fatigue (Hook Rate drops 30%+, frequency >3.5)
- Hook-Body Mismatch (high Hook Rate, low conversion)
- Variable Testing Trap (testing color swaps instead of concepts)
- Native Format Misfit (too polished, feels like "ad")
- Creative Starvation (no weekly fresh concepts)
- Hook Rate Plateau (<25% and not improving)
- Concept Diversity Failure (all concepts similar)
- Self-Selection Failure (hook doesn't filter for ICP)
- Compliance Flag from Hooks (sensationalism, prohibited content)
- Creative-Avatar Misalignment (attracts wrong demographic)

I) GOLDEN RUNS (3-5)
Test scenarios:
- Scenario 1: Weekly creative sprint for Ecom DTC (ship 5 Lazy Static concepts in <2 hours)
- Scenario 2: Scale winning Founder VSL (create 10 variants using Nano Banana)
- Scenario 3: Fix low Hook Rate creative (apply Visual Hook Audit, retest)

J) COMPLIANCE & GUARDRAILS
- No clickbait hooks (must deliver on promise)
- No sensationalist language without proof
- Authentic/ugly beats polished (native format requirement)
- Self-selecting hooks required (ICP filtering)

K) CHECKLISTS
- Creative production sprint: 5-10 concepts, concept diversity validated, Hook Rate predictions made
- Creative QA: Visual hook present, text overlay clear, self-selecting for ICP, compliant
- Creative rotation: Winners rotated every 14 days, bench has 3-5 concepts ready

Deliver as structured markdown with YAML blocks.
```

---

## PROMPT #3 — KB-IMAGE-GENERATOR (Niche-Specific Visual Production)

**Notebook Name:** `Image Generator - Meta Ads Knowledge Extraction`

**Upload Sources:** Visual creative guides, niche-specific swipe files (Ecom, SaaS, Lead Gen, Info Product), AI image generation tutorials

**Paste this into NotebookLM:**

```
You are ULTRAMIND Knowledge Extractor for META ADS IMAGE GENERATOR.

Extract grounded, source-tagged knowledge about visual creative production across niches, styles, formats, and AI-accelerated workflows.

FOCUS AREAS:
- Niche-specific visual strategies (Ecom/DTC, Lead Gen/Local Service, SaaS/B2B, Info Product/Coaching, Health/Wellness)
- Style frameworks (Lazy Statics, Authentic Chaos, Data Viz, Testimonial Graphics, Founder Authority)
- Format optimization (Feed 1:1, Stories/Reels 9:16, Carousels)
- Text overlay frameworks (curiosity hooks, self-selecting questions, contrarian statements, benefit-driven)
- AI-accelerated production (Nano Banana workflow, Midjourney prompts, Canva AI, ChatGPT variants)
- Production workflows (weekly sprints, batch production, quality gates)

REQUIREMENTS:
- Tag every claim: [SRC: source_name | timestamp]
- Include direct quotes (≤25 words) for visual principles
- Include visual examples where possible (describe in detail)
- Favor "how-to" over theory

OUTPUT STRUCTURE:

A) SOURCE MAP
List each source: ID, title, author, key topics (niche focus, style focus), unique contribution

B) TAXONOMY
Categories: Niche Strategies, Style Frameworks, Format Types, Text Overlays, AI Tools
Subcategories:
- Niches: Ecom, Lead Gen, SaaS, Info Product, Health/Wellness
- Styles: Lazy Statics, Authentic Chaos, Data Viz, Testimonials, Founder Authority
- Formats: 1:1 Feed, 9:16 Stories/Reels, Carousels
Consensus points: What works across all niches (e.g., authentic beats polished)
Divergences: Niche-specific visual requirements (e.g., SaaS needs dashboards, Ecom needs product-in-context)
Gaps: Missing niches or visual styles

C) FRAMEWORKS (10-20)

NICHE-SPECIFIC VISUAL STRATEGIES (5 frameworks):
1. Ecom/DTC Visual Strategy
   - Product in context (not white background)
   - Lifestyle shots (product in use)
   - Before/after (compliant, disclaimed)
   - Unboxing/authenticity signals
2. Lead Gen/Local Service Visual Strategy
   - Founder face (trust signal)
   - Local landmarks (geographic relevance)
   - Review screenshots (social proof)
   - "Ugly" authentic (not corporate stock photos)
3. SaaS/B2B Visual Strategy
   - Dashboard screenshots (product in action)
   - Data visualizations (results proof)
   - Founder authority (speaking, teaching)
   - Workflow diagrams (how it works)
4. Info Product/Coaching Visual Strategy
   - Founder selfies (personal connection)
   - Whiteboard frameworks (teaching authority)
   - Testimonial graphics (transformation proof)
   - Behind-the-scenes (authenticity)
5. Health/Wellness Visual Strategy
   - Authentic settings (not clinical)
   - Relatable scenarios (daily life context)
   - No medical claims (compliance)
   - Founder journey (personal story)

STYLE FRAMEWORKS (5-8):
6. Lazy Static Headlines
   - Authentic image source: Founder selfie, messy desk, product in real context
   - Text overlay: Bold, contrasting color, curiosity hook or self-selecting question
   - Primary text: 2-3 sentence story or pattern interrupt
   - Headline: Promise + mechanism or objection handle
   - Production time: <15 min per creative
7. Authentic Chaos Style
   - Messy/real workspace (not staged)
   - iPhone footage quality (not professional camera)
   - Imperfect lighting/framing (relatable, not polished)
   - Movement/action (not static posed shots)
8. Data Visualization Style
   - Charts/graphs showing results
   - Before/after metrics (compliant)
   - Statistical proof (authority signal)
   - Clean, readable design (not cluttered)
9. Testimonial Graphics Style
   - Customer quote + photo
   - Result highlight (quantified outcome)
   - Authentic headshot (not stock photo)
   - Source attribution (name, location, context)
10. Founder Authority Style
    - Speaking on stage/teaching
    - Whiteboard/framework visuals
    - Professional setting (but not stuffy)
    - Expertise signals (credentials, media features)

TEXT OVERLAY FRAMEWORKS (4):
11. Curiosity Hook Overlays
    - Pattern: "The #1 mistake [avatar] make with [problem]..."
    - Pattern: "Why [common belief] is keeping you stuck..."
    - Pattern: "What [authority figure] won't tell you about [topic]..."
12. Self-Selecting Question Overlays
    - Pattern: "If you're [ICP descriptor], watch this..."
    - Pattern: "Are you [pain point]? Here's why..."
    - Pattern: "[Avatar type]? Stop [wrong action] immediately..."
13. Contrarian Statement Overlays
    - Pattern: "Stop [common practice] — it's a scam"
    - Pattern: "[Industry norm] doesn't work. Try this instead..."
    - Pattern: "Forget [old method]. Do this..."
14. Benefit-Driven Overlays
    - Pattern: "[Outcome] in [timeframe] without [objection]"
    - Pattern: "How to [achieve goal] even if [obstacle]"
    - Pattern: "[Result] using [unique mechanism]"

FORMAT OPTIMIZATION FRAMEWORK:
15. Feed (1:1 Square) Optimization
16. Stories/Reels (9:16 Vertical) Optimization
17. Carousel (Multi-Image) Optimization

AI-ACCELERATED PRODUCTION FRAMEWORKS:
18. Nano Banana Workflow (10-20 variants from winners)
19. Midjourney Prompt Engineering (niche-specific visuals)
20. Canva AI Template Batch Production

D) SOPs (5-8)
- Weekly creative production sprint (5-10 concepts in <2 hours)
- Batch production workflow (20-50 variants from proven winners)
- AI image generation SOP (Midjourney → editing → upload)
- Text overlay creation SOP (ChatGPT variants → Canva → export)
- Quality gate checklist (mobile-first test, compliance scan, format validation)

E) HEURISTICS (20-35 IF-THEN rules)

DIAGNOSTIC:
- IF Hook Rate <25% on static image THEN audit text overlay clarity and visual contrast
- IF niche is Ecom/DTC THEN use product-in-context (not white background)
- IF niche is SaaS/B2B THEN use dashboard screenshots or data viz (not generic stock)
- IF niche is Lead Gen/Local Service THEN use founder face + local trust signals

OPTIMIZATION:
- IF Hook Rate >35% THEN scale via Nano Banana (create 10-20 variants)
- IF authentic/ugly style outperforms polished THEN double down on iPhone footage
- IF text overlay too long THEN reduce to <10 words for mobile readability

PRODUCTION:
- IF spending <$10k/month THEN produce 3-5 concepts weekly (manual creation)
- IF spending $20k+/month THEN use AI acceleration (Nano Banana, 10-20 concepts weekly)
- IF winner identified (Hook Rate >35%, profitable CPA) THEN batch produce 20-50 variants

COMPLIANCE:
- IF niche is Health/Wellness THEN no before/after without disclaimers
- IF text overlay makes income claim THEN add disclosure
- IF using testimonial THEN verify authenticity and get permission

F) METRICS TABLE
| Metric | Purpose | Threshold | Action Trigger | Source |
|--------|---------|-----------|----------------|--------|
| Production Time per Creative | Efficiency | <15 min for Lazy Statics | >30 min = simplify workflow | [SRC] |
| Concept Diversity Score | Avoid variations | >70% unique visuals | <50% = using same image templates | [SRC] |
| Mobile Readability Score | Text overlay clarity | 100% readable on phone | <80% = text too small/dense | [SRC] |
| Compliance Flag Rate | Policy violations | <5% rejection rate | >10% = audit text overlays/images | [SRC] |

G) PATTERNS (15-25)
Visual patterns, production workflows, niche-specific templates:
- Ecom product-in-context pattern: Product + lifestyle setting + text overlay
- Lead Gen founder trust pattern: Founder face + local landmark + review screenshot
- SaaS dashboard proof pattern: Dashboard screenshot + data highlight + benefit overlay
- Info Product teaching pattern: Whiteboard framework + founder pointing + curiosity hook
- Lazy Static production pattern: iPhone selfie → Canva text overlay → export 1:1 and 9:16

H) FAILURE MODES (8-12)
- Text Overlay Unreadable (too small, low contrast, cluttered)
- Niche-Visual Mismatch (generic stock photo for SaaS, polished corporate for Lead Gen)
- Format Mismatch (1:1 image used in 9:16 Stories, cropping cuts off text)
- Compliance Violation (before/after without disclaimer, income claim without disclosure)
- Over-Polished (stock photo feel, too professional, doesn't blend with feed)
- Under-Resourced Production (can't ship weekly, bottlenecked, manual workflow)
- AI Artifact Errors (Midjourney hands, text misspellings, unrealistic elements)
- Brand Inconsistency (different visual styles across creatives, no cohesive look)

I) GOLDEN RUNS (3-5)
- Scenario 1: Weekly Lazy Static sprint for Ecom DTC (produce 5 concepts in 1 hour)
- Scenario 2: Nano Banana scaling for SaaS winner (create 20 dashboard variants in 2 hours)
- Scenario 3: Niche-specific visual strategy for Lead Gen local service (founder face + local trust)

J) COMPLIANCE & GUARDRAILS
- No before/after in health/beauty without disclaimers
- No income claims without disclosures
- Authentic visuals preferred (stock photos only if strategically justified)
- Mobile-first testing (view on phone before uploading)
- Platform policy compliance (Meta Advertising Policies)

K) CHECKLISTS
- Creative production sprint: Niche strategy selected, style framework chosen, format optimized, text overlay created, compliance validated
- AI production workflow: Winner identified, Midjourney prompts generated, variants created, text overlays applied, batch exported
- Quality gates: Mobile readability test, compliance scan, format validation (1:1, 9:16), Hook Rate prediction

Deliver as structured markdown with YAML blocks and detailed visual descriptions.
```

---

## PROMPT #4 — KB-IMAGE-ANALYZER (Hook Rate Diagnostics & Competitive Research)

**Notebook Name:** `Image Analyzer - Meta Ads Knowledge Extraction`

**Upload Sources:** Hook Rate analysis guides, Visual Hook Audit frameworks, competitive research methodologies, Meta Ads Library tutorials

**Paste this into NotebookLM:**

```
You are ULTRAMIND Knowledge Extractor for META ADS IMAGE ANALYZER.

Extract grounded, source-tagged knowledge about visual creative performance analysis, Hook Rate diagnostics, competitive visual research, and creative fatigue detection.

FOCUS AREAS:
- Visual Hook Audit framework (diagnostic for Hook Rate <25%)
- Hook Rate diagnostics (trend analysis, fatigue detection)
- Hold Rate analysis (15-sec+ engagement depth)
- Competitive visual research (Meta Ads Library scraping, pattern extraction)
- Native format analysis (blend with feed vs "ad-like")
- Creative fatigue detection (Hook Rate decline, frequency spike)
- A/B test design for visual variants

REQUIREMENTS:
- Tag every claim: [SRC: source_name | timestamp]
- Include direct quotes (≤25 words) for diagnostic principles
- Favor "how-to" over theory

OUTPUT STRUCTURE:

A) SOURCE MAP
List each source: ID, title, author, key topics, unique contribution

B) TAXONOMY
Categories: Visual Diagnostics, Hook Rate Analysis, Competitive Research, Fatigue Detection, A/B Testing
Subcategories: Visual audit elements (interrupt, text, movement, audio, contrast), Research methods, Performance metrics
Consensus points: Hook Rate >30% = good, Visual interrupt beats polish
Divergences: Different diagnostic frameworks or competitive research methods
Gaps: Missing diagnostic criteria or research tools

C) FRAMEWORKS (8-15)

VISUAL DIAGNOSTICS (5 frameworks):
1. Visual Hook Audit Framework
   - Visual interrupt check: Is first frame chaotic/surprising/ugly (not polished)?
   - Text overlay validation: Does hook self-select ICP or create curiosity gap?
   - Movement detection: Is there motion in first 3sec (not static)?
   - Audio presence: Is there voice/sound in first 3sec (not just music)?
   - Feed contrast: Does creative stand out (pattern interrupt vs blends in)?
   - Scoring: 5 elements, 0-10 each, 40+ = strong visual hook
2. Hook Rate Trend Analysis
   - Baseline: First 7 days Hook Rate average
   - Decline detection: >30% drop from baseline = fatigue signal
   - Plateau detection: Hook Rate flat <25% for 7+ days = weak hook
   - Spike detection: Hook Rate >40% = strong concept or hook-body mismatch
3. Hold Rate Analysis (15-sec+ Engagement)
   - Target: >50% Hold Rate = good story/proof
   - <40% Hold Rate = weak body, story doesn't deliver on hook
   - High Hook Rate + Low Hold Rate = hook promises more than body delivers
4. Native Format Analysis Framework
   - Feed aesthetic matching: Does it blend or scream "ad"?
   - Authenticity score: Polished vs raw/ugly (0-10 scale)
   - Scroll-stopping elements: Movement, chaos, contrast present?
   - "Ad-like" signals: Corporate polish, stock photo feel, branding too prominent
5. Creative Fatigue Detection Framework
   - Hook Rate decline: >30% drop from week 1 baseline
   - Frequency spike: >3.5 = audience saturation
   - CPA increase: >40% increase from baseline
   - Delivery slowdown: Budget unspent despite availability

COMPETITIVE RESEARCH (3 frameworks):
6. Meta Ads Library Scraping Protocol
   - Search: Competitor brand names, keywords, product categories
   - Filter: Active ads only, date range (last 30 days)
   - Capture: Screenshot, ad copy, hook type, visual style, format
   - Categorize: Hook type (curiosity, scam, benefit), Visual style (lazy static, founder, testimonial), Format (1:1, 9:16, carousel)
7. Competitor Hook Pattern Extraction
   - Identify: Recurring hook structures, common curiosity gaps, contrarian angles
   - Extract: Template patterns (e.g., "The #1 mistake [avatar] make...")
   - Test: Apply extracted patterns to your niche/offer
8. Swipe File Building & Categorization
   - Categories: Niche (Ecom, SaaS, Lead Gen), Hook type, Visual style, Format
   - Tagging: Estimated Hook Rate (high/medium/low), Compliance level, Authenticity score
   - Usage: Inspiration for weekly creative sprints, competitive gap analysis

PERFORMANCE ANALYSIS (2 frameworks):
9. Hook Rate Benchmarking Framework
   - <25% = weak visual hook (audit required)
   - 25-35% = acceptable (proceed)
   - >35% = strong hook (scale candidate)
   - >40% but low conversion = hook-body mismatch (attracts wrong audience)
10. Engagement Rate Analysis
    - Shares/comments/saves = emotional resonance
    - High engagement + low conversion = awareness-stage traffic (wrong funnel)
    - Low engagement + high conversion = direct response working (scale)

A/B TESTING DESIGN (3 frameworks):
11. Visual Variant Testing Framework
    - Test: Different backgrounds (authentic vs polished, indoor vs outdoor)
    - Test: Text overlay positions (top vs center vs bottom)
    - Test: Color schemes (contrasting vs monochrome)
    - Control: Hook text stays same, visual elements change
12. Text Overlay Split Test Framework
    - Test: Hook phrasing (curiosity vs benefit vs contrarian)
    - Test: Word count (5 words vs 10 words vs 15 words)
    - Test: Question vs statement format
    - Control: Visual stays same, text overlay changes
13. Format Testing Framework
    - Test: 1:1 square vs 9:16 vertical (same creative, different aspect ratio)
    - Test: Static vs carousel (single image vs 3-5 image sequence)
    - Test: Image vs short video (static with text vs 5-sec video loop)

D) SOPs (5-8)
- Weekly Hook Rate review (compare to baseline, detect fatigue)
- Daily creative fatigue monitoring (frequency check, Hook Rate trend)
- Monthly competitive research sprint (Meta Ads Library scraping, pattern extraction)
- Visual Hook Audit protocol (for creatives with Hook Rate <25%)
- A/B test launch SOP (setup, monitoring, winner declaration)

E) HEURISTICS (20-35 IF-THEN rules)

DIAGNOSTIC:
- IF Hook Rate <25% for 7+ days THEN run Visual Hook Audit
- IF Hook Rate >40% but CPA high THEN hook-body mismatch (attracts wrong audience)
- IF Hook Rate declining 30%+ from baseline THEN creative fatigue detected
- IF frequency >3.5 THEN audience saturation (expand audience or rotate creative)
- IF Hold Rate <40% THEN weak story/proof (body doesn't deliver on hook)

OPTIMIZATION:
- IF Visual Hook Audit score <30/50 THEN fix weakest element first
- IF Hook Rate improving after audit THEN winning element identified (scale)
- IF native format analysis shows "ad-like" THEN de-polish creative (authentic/ugly)
- IF competitive research reveals gap THEN test unexplored hook angle

COMPETITIVE RESEARCH:
- IF competitor Hook Rate estimated >40% THEN extract hook pattern, apply to your offer
- IF swipe file lacks examples in your niche THEN expand research to adjacent niches
- IF competitor visual style new to you THEN test variant in your creative mix

A/B TESTING:
- IF visual variant wins by 20%+ Hook Rate THEN scale winner, kill loser
- IF text overlay split test inconclusive (within 10%) THEN increase sample size
- IF format test shows 9:16 outperforms 1:1 THEN shift production to vertical

F) METRICS TABLE
| Metric | Purpose | Threshold | Action Trigger | Source |
|--------|---------|-----------|----------------|--------|
| Hook Rate Baseline | Fatigue detection reference | Established in first 7 days | 30%+ decline = fatigue | [SRC] |
| Visual Hook Audit Score | Diagnostic quality | 40+/50 = strong | <30/50 = fix weakest element | [SRC] |
| Hold Rate (15-sec+) | Engagement depth | >50% good | <40% = weak story/proof | [SRC] |
| Frequency | Audience saturation | <3.5 healthy | >3.5 = saturated, rotate | [SRC] |
| Native Format Score | "Ad-like" detection | 7+/10 = native | <5/10 = too polished | [SRC] |

G) PATTERNS (10-20)
Diagnostic patterns, competitive research patterns, A/B test structures:
- Hook Rate decline pattern: Week 1 (35%) → Week 2 (30%) → Week 3 (24%) = fatigue trajectory
- Visual Hook Audit checklist pattern: Interrupt (Y/N) → Text (Y/N) → Movement (Y/N) → Audio (Y/N) → Contrast (Y/N)
- Competitive research workflow: Search → Filter → Capture → Categorize → Extract → Test
- A/B test design pattern: Hypothesis → Control + Variant → Launch → Monitor (48h minimum) → Declare winner

H) FAILURE MODES (8-12)
- Hook Rate Plateau (flat <25% for 7+ days, audit shows no clear fix)
- False Positive Hook (Hook Rate >40% but attracts wrong audience, CPA too high)
- Creative Fatigue Missed (Hook Rate declining but not caught early, performance tanks)
- Over-Polished Detection Failure (visual looks "ad-like" but not flagged as native format misfit)
- Competitive Research Overwhelm (too many swipe files, no actionable patterns extracted)
- A/B Test Inconclusive (variants perform within 10%, no clear winner)
- Visual Hook Audit Misdiagnosis (fix wrong element first, no Hook Rate improvement)
- Native Format Score Inaccurate (score says native but Hook Rate still low)

I) GOLDEN RUNS (3-5)
- Scenario 1: Visual Hook Audit for creative with Hook Rate 18% (diagnose, fix, retest to 32%)
- Scenario 2: Competitive research sprint (scrape Meta Ads Library, extract 10 hook patterns, test in creative)
- Scenario 3: Creative fatigue detection and recovery (Hook Rate drops from 35% to 24%, rotate creative, new concept ships within 24h)

J) COMPLIANCE & GUARDRAILS
- No gaming metrics (buying engagement to inflate Hook Rate)
- Transparent competitive research (don't steal verbatim, extract patterns only)
- Respect privacy (no personal data scraping from competitor ads)

K) CHECKLISTS
- Weekly Hook Rate review: Compare to baseline, flag 30%+ declines, audit creatives <25%
- Visual Hook Audit: 5 elements checked (interrupt, text, movement, audio, contrast), score calculated, weakest element identified
- Competitive research sprint: 10+ competitor ads captured, patterns extracted, swipe file updated, test concepts generated

Deliver as structured markdown with YAML blocks.
```

---

## PROMPT #5 — KB-MEASUREMENT-ATTRIBUTION (ncROAS, Tracking, Incrementality)

**Notebook Name:** `Measurement & Attribution - Meta Ads Knowledge Extraction`

**Upload Sources:** ncROAS calculation guides, incrementality testing case studies, tracking setup tutorials, attribution window research

**Paste this into NotebookLM:**

```
You are ULTRAMIND Knowledge Extractor for META ADS MEASUREMENT & ATTRIBUTION.

Extract grounded, source-tagged knowledge about ncROAS calculation, incrementality testing, attribution validation, tracking integrity, and MER monitoring.

FOCUS AREAS:
- ncROAS (New Customer ROAS) vs Blended ROAS (attribution inflation detection)
- Incremental attribution methods (Holdout Tests, Conversion Lift Studies, ncROAS tracking)
- Tracking validation (Pixel, Conversion API, Event Match Quality)
- MER (Marketing Efficiency Ratio) as health check metric
- Lead Gen Lag-Time Optimization (optimize for backend conversion, not just lead capture)
- Attribution window configuration (7-day click / 1-day view)
- Platform vs actual lift measurement

REQUIREMENTS:
- Tag every claim: [SRC: source_name | timestamp]
- Include direct quotes (≤25 words) for key principles
- Favor "how-to" over theory

OUTPUT STRUCTURE:

A) SOURCE MAP
List each source: ID, title, author, key topics, unique contribution

B) TAXONOMY
Categories: ncROAS Framework, Incrementality Testing, Tracking Validation, MER Monitoring, Lead Gen Optimization
Subcategories: Holdout tests, Conversion Lift Studies, Pixel setup, Conversion API, Event Match Quality
Consensus points: ncROAS >1.5x for scaling, Platform ROAS inflated by repeats
Divergences: Different incrementality testing methods (Holdout vs Lift Studies)
Gaps: Missing tracking validation steps or attribution models

C) FRAMEWORKS (8-12)

ncROAS FRAMEWORKS (3):
1. ncROAS Calculation Framework
   - Formula: New customer revenue / ad spend = ncROAS
   - New customer definition: First purchase within attribution window, exclude repeats
   - Comparison: ncROAS vs Blended ROAS (gap >1.5x = attribution hallucination)
   - Target: ncROAS >1.5x for sustainable scaling, >2.0x = highly profitable
   - Use case: Scale decisions based on ncROAS, not platform ROAS
2. Attribution Inflation Detection Framework
   - Symptom: Platform ROAS looks great (3.0x+) but MER flat or declining
   - Diagnosis: Blended ROAS - ncROAS gap (>1.5x = inflation likely)
   - Cause: Platform attributes repeat customers to ads (would've bought anyway)
   - Recovery: Calculate ncROAS, use for scale decisions, run holdout test for validation
3. ncROAS Tracking Setup
   - Segment reporting: New customers vs repeat customers in analytics
   - Tag first-time buyers: UTM parameter, custom conversion event, or CRM flag
   - Calculate weekly/monthly: Track trend, detect attribution drift

INCREMENTALITY TESTING FRAMEWORKS (3):
4. Holdout Test Framework
   - Step 1: Baseline period (14-30 days ads on, measure MER and conversion volume)
   - Step 2: Holdout period (14-30 days ads off, measure organic revenue)
   - Step 3: Calculate lift: (baseline revenue - organic revenue) / ad spend = true incremental ROAS
   - Step 4: Compare platform ROAS to holdout lift (validate attribution accuracy)
   - When to use: Annually for validation, before major budget jumps, when stakeholders question effectiveness
5. Conversion Lift Study Framework
   - Meta runs controlled experiment: Test group (sees ads) vs Control group (no ads)
   - Measures: Conversion difference between groups (incremental conversions attributed to ads)
   - Output: Incremental conversion count, incremental CPA, true incremental ROAS
   - Requirements: $50k+/month spend for statistical validity, 2-4 week test duration
   - When to use: Need statistically valid incrementality data, annual validation
6. MER (Marketing Efficiency Ratio) Framework
   - Formula: Total revenue / total marketing spend (all channels)
   - Purpose: Health check metric, should align with platform ROAS trends
   - Red flag: MER flat while ad spend increases = attribution hallucination or channel cannibalization
   - Use case: Track weekly/monthly, compare to platform ROAS to detect drift

TRACKING VALIDATION FRAMEWORKS (3):
7. Pixel Firing Verification Framework
   - Tool: Meta Pixel Helper (Chrome extension)
   - Check: Pixel fires on every funnel page (landing, checkout, thank-you)
   - Validate: Event parameters correct (value, currency, content_ids)
   - Test purchase: Complete transaction, verify event shows in Events Manager within 20min
   - Frequency: Pre-launch (required), weekly spot-check (recommended)
8. Conversion API Setup Framework
   - Purpose: Server-side tracking backup (browser-based pixel can be blocked)
   - Setup: Send conversion events from server to Meta API
   - Validate: Event Match Quality score >7.0 (good), >8.0 (excellent)
   - Deduplication: Use event_id to prevent double-counting (Pixel + API same event)
9. Attribution Window Configuration Framework
   - Default: 7-day click / 1-day view attribution window
   - Adjustment: Extend to 28-day click if longer sales cycle (high-ticket, B2B)
   - Shorten: 1-day click if short impulse buy cycle (low-ticket Ecom)
   - Impact: Longer window = more conversions attributed (inflates ROAS), shorter = conservative

LEAD GEN OPTIMIZATION FRAMEWORK:
10. Lead Gen Lag-Time Optimization Framework
    - Problem: Optimizing for lead capture = low-quality leads (junk form fills)
    - Solution: Optimize for backend conversion (call booked, sale made), not lead form submit
    - Setup: Primary event = backend action, secondary event = lead capture (for learning phase)
    - Transition: After 50 backend conversions, switch to backend-only optimization
    - Result: Higher quality leads, improved lead-to-sale conversion rate (10%+ improvement)

FAILURE MODE FRAMEWORKS (2):
11. Pixel Malnutrition Diagnosis & Recovery
12. Attribution Hallucination Diagnosis & Recovery

D) SOPs (5-8)
- Weekly ncROAS calculation (segment new vs repeat customers, calculate ratio)
- Monthly MER monitoring (compare to platform ROAS, detect drift)
- Quarterly holdout test (validate incrementality, adjust scale targets)
- Pre-launch tracking validation (pixel firing, Conversion API, test purchase)
- Daily Events Manager check (conversion volume, event match quality, tracking breaks)

E) HEURISTICS (20-30 IF-THEN rules)

DIAGNOSTIC:
- IF platform ROAS >3.0 but MER <2.5 THEN attribution hallucination likely (calculate ncROAS)
- IF blended ROAS - ncROAS gap >1.5x THEN repeat customers inflating platform attribution
- IF pixel firing but no conversions attributed THEN check Conversion API or attribution window
- IF Event Match Quality <7.0 THEN improve server-side data quality (email hash, phone, address)

OPTIMIZATION:
- IF ncROAS >1.5x consistently for 14+ days THEN scale candidate (increase budget 20%)
- IF ncROAS <1.0 THEN unprofitable for new customer acquisition (fix creative or offer)
- IF MER declining while spend increases THEN channel cannibalization or attribution drift

INCREMENTALITY TESTING:
- IF spending $50k+/month THEN run Conversion Lift Study annually
- IF MER flat despite platform ROAS growth THEN run holdout test to validate true lift
- IF holdout test shows 50%+ of attributed revenue is organic THEN scale back ad spend

TRACKING:
- IF Events Manager shows no conversions but sales confirmed THEN pixel malnutrition (fix immediately)
- IF Event Match Quality <7.0 THEN add server-side data (email, phone, Conversion API)
- IF attribution window too short (<7 days) for sales cycle THEN extend to 28 days

F) METRICS TABLE
| Metric | Purpose | Threshold | Action Trigger | Source |
|--------|---------|-----------|----------------|--------|
| ncROAS | Incremental revenue scale decisions | >1.5x scalable, >2.0x highly profitable | <1.0 = unprofitable new CAC | [SRC] |
| Blended ROAS - ncROAS Gap | Attribution inflation detection | <1.0x = healthy | >1.5x = inflation likely | [SRC] |
| MER (Marketing Efficiency Ratio) | Multi-channel health check | Should trend with platform ROAS | MER flat while ROAS grows = drift | [SRC] |
| Event Match Quality | Server-side tracking accuracy | >7.0 good, >8.0 excellent | <7.0 = improve data quality | [SRC] |
| Pixel Firing Rate | Browser-side tracking health | 100% on all funnel pages | <95% = tracking breaks exist | [SRC] |

G) PATTERNS (10-15)
Calculation patterns, testing workflows, tracking validation sequences:
- ncROAS calculation pattern: Segment new vs repeat → Calculate new customer revenue → Divide by ad spend → Compare to blended ROAS
- Holdout test workflow: Baseline (ads on) → Holdout (ads off) → Lift calculation → Platform validation
- Tracking validation sequence: Pixel Helper check → Test purchase → Events Manager verification → Event Match Quality review

H) FAILURE MODES (6-10)
- Attribution Hallucination (platform ROAS great, MER flat, repeat customers inflate)
- Pixel Malnutrition (no conversions tracked, sales confirmed in CRM/Stripe, tracking broken)
- Event Match Quality Low (<7.0, Conversion API data incomplete)
- Attribution Window Mismatch (too short for sales cycle, conversions missed)
- ncROAS Miscalculation (repeat customers not excluded, inflated new CAC)
- MER Misread (cutting profitable channels due to platform attribution gaps)
- Holdout Test Execution Error (baseline period too short, seasonal variance not controlled)
- Conversion Lift Study Misinterpretation (ignoring confidence intervals, declaring false positive)

I) GOLDEN RUNS (3-5)
- Scenario 1: ncROAS calculation for Ecom DTC (segment new vs repeat, detect 1.8x gap with blended ROAS)
- Scenario 2: Holdout test for SaaS ($75k/month spend, validate 30% true lift vs 2.5x platform ROAS)
- Scenario 3: Pixel malnutrition diagnosis and recovery (no conversions tracked, fix Conversion API, restore tracking)

J) COMPLIANCE & GUARDRAILS
- Transparent attribution (acknowledge platform vs actual lift to clients/stakeholders)
- No false ROAS claims (use ncROAS for client reporting, not blended)
- Data privacy compliance (hash PII for Conversion API, GDPR/CCPA compliant)

K) CHECKLISTS
- Weekly ncROAS review: Calculate ratio, compare to blended, flag >1.5x gap
- Pre-launch tracking validation: Pixel firing verified, Conversion API configured, test purchase complete, Events Manager shows attribution
- Quarterly incrementality test: Holdout or Lift Study scheduled, baseline measured, lift calculated, scale targets adjusted

Deliver as structured markdown with YAML blocks.
```

---

## PROMPT #6 — KB-PERFORMANCE-DIAGNOSTICS (15 Failure Modes + Troubleshooting)

**Notebook Name:** `Performance Diagnostics - Meta Ads Knowledge Extraction`

**Upload Sources:** Troubleshooting guides, failure mode case studies, Meta ads optimization tutorials, diagnostic frameworks

**Paste this into NotebookLM:**

```
You are ULTRAMIND Knowledge Extractor for META ADS PERFORMANCE DIAGNOSTICS.

Extract grounded, source-tagged knowledge about 15 failure modes, 7 anti-patterns, troubleshooting playbooks, and diagnostic heuristics.

FOCUS AREAS:
- 15 Failure Modes with full playbooks (Symptoms → Root Cause → Diagnosis → Recovery → Prevention)
- 7 Anti-Patterns (behaviors to avoid: Variable Testing, Frequent Pausing, Front-End Obsession, etc.)
- Diagnostic heuristics (25-50 IF-THEN rules for identifying and fixing issues)
- Troubleshooting workflows (step-by-step diagnostic sequences)
- Circuit breakers (when to stop optimizing and restart)

REQUIREMENTS:
- Tag every claim: [SRC: source_name | timestamp]
- Include direct quotes (≤25 words) for diagnostic principles
- Favor "how-to" over theory (actionable recovery steps)

OUTPUT STRUCTURE:

A) SOURCE MAP
List each source: ID, title, author, key topics, unique contribution

B) TAXONOMY
Categories: Failure Modes, Anti-Patterns, Diagnostic Heuristics, Troubleshooting Workflows
Subcategories:
- Failure Mode types: Creative (fatigue, hook mismatch), Technical (pixel, attribution), Strategic (scaling, budget)
- Anti-Pattern types: Testing, Optimization, Structural
Consensus points: What all sources agree causes failures
Divergences: Different recovery approaches or diagnostic methods
Gaps: Missing failure modes or troubleshooting steps

C) FRAMEWORKS (15 Failure Modes + 7 Anti-Patterns = 22)

15 FAILURE MODES (full playbooks):

1. CREATIVE FATIGUE
   - Symptoms: Hook Rate drops 30%+ from baseline, frequency >3.5, CPA increases 40%+, delivery slowing
   - Root Cause: Same creative shown to same audience repeatedly, novelty worn off
   - Diagnosis Steps:
     1. Check frequency metric (>3.5 = fatigued)
     2. Compare current Hook Rate to first 7 days (30%+ drop = fatigued)
     3. Check delivery: If reaching same users repeatedly, audience too narrow
   - Recovery:
     1. Ship replacement concept immediately (same offer, different hook/angle)
     2. Pause fatigued creative
     3. Expand audience if frequency was issue
   - Prevention:
     1. Follow Rule of 1:10k (ship fresh concepts weekly)
     2. Rotate winners before fatigue (14-day max lifespan)
     3. Build creative bench (always have 3-5 concepts in testing)

2. ATTRIBUTION HALLUCINATION
   - Symptoms: Platform ROAS looks great (3.0x+) but MER flat or declining
   - Root Cause: Platform attributing sales that would've happened anyway (existing customers, organic traffic)
   - Diagnosis Steps:
     1. Calculate MER: total revenue / total ad spend across all channels
     2. Compare platform ROAS to MER (>1.5x gap = hallucination likely)
     3. Check new customer percentage (if <30%, attribution inflated by repeats)
   - Recovery:
     1. Run holdout test: pause ads for 2 weeks, measure organic revenue baseline
     2. Calculate ncROAS: (total revenue - organic baseline) / ad spend
     3. Use ncROAS for scale decisions, not platform ROAS
   - Prevention:
     1. Track ncROAS from day 1
     2. Use Conversion Lift Studies for accurate incrementality measurement
     3. Segment reporting: new customers vs repeat customers

3. LEARNING LIMITED LOOP
   - Symptoms: Ad set stuck in "Learning Limited" for 7+ days, poor delivery
   - Root Cause: Not enough conversions per week (need 50 minimum), budget too low or audience too narrow
   - Diagnosis Steps:
     1. Check conversion volume: <50/week = learning limited
     2. Check audience size: <500k = likely too narrow
     3. Check budget: if <$50/day for conversions, may be too low
   - Recovery:
     1. Consolidate campaigns (combine ad sets to pool conversions)
     2. Increase budget to hit 50 conversions/week minimum
     3. Expand audience (remove narrow interest/behavior layers)
   - Prevention:
     1. Start with broad targeting (M3 swim lanes only)
     2. Budget formula: (target CPA × 50) / 7 days = minimum daily budget
     3. Avoid fragmentation (fewer campaigns with higher budgets)

4. HOOK-BODY MISMATCH
5. OFFER-CHANNEL MISMATCH
6. PIXEL MALNUTRITION
7. CREATIVE-AVATAR MISALIGNMENT
8. RETARGETING SATURATION
9. COMPLIANCE FLAGS FROM HOOKS
10. NATIVE FORMAT MISFIT
11. UNDER-RESOURCED CREATIVE PIPELINE
12. BUDGET CLIFF
13. MISREAD MER
14. AUDIENCE FRAGMENTATION BY PLACEMENT
15. FUNNEL BLINDNESS

(Extract full playbooks for all 15 following same structure as #1-3)

7 ANTI-PATTERNS:

1. VARIABLE TESTING
   - Description: Testing minor variations (color swaps, font changes, small text edits) instead of distinct concepts
   - Why Harmful: Wastes learning budget, algorithm sees variations as duplicates, spreads data thin
   - Instead Do: Test concepts (different hooks/angles/stories), different mechanisms, different proof types

2. FREQUENT PAUSING
3. FRONT-END OBSESSION
4. AVATAR SPRAWL
5. RETARGETING CRUTCH
6. CREATIVE STARVATION
7. OVER-SEGMENTATION

(Extract full anti-pattern descriptions for all 7)

D) SOPs (5-8)
- Daily diagnostic check (frequency, delivery %, learning phase status)
- Weekly failure mode scan (Hook Rate trends, ncROAS vs MER, creative fatigue signals)
- Monthly deep diagnostic (holdout test planning, campaign consolidation review)
- Failure mode recovery protocol (diagnose → recover → prevent → document)

E) HEURISTICS (25-50 IF-THEN rules)

DIAGNOSTIC:
- IF Hook Rate <25% for 7+ days THEN audit visual hook (Creative Fatigue or weak hook)
- IF Hook Rate >35% but CPA high THEN hook-body mismatch (attracts wrong audience)
- IF learning limited 7+ days THEN consolidate campaigns or increase budget
- IF all creatives perform within 10% THEN testing variations not concepts
- IF MER flat while spend increases THEN attribution hallucination (check ncROAS)
- IF retargeting outperforms prospecting 3x+ THEN prospecting creative weak
- IF creative fatigue cycle <14 days THEN audience saturation or poor concept diversity

OPTIMIZATION:
- IF profitable CPA achieved THEN scale budget 20% every 3-5 days max
- IF winner emerges (CPA 30%+ better) THEN kill bottom 50%, reallocate budget
- IF creative fatigue detected THEN ship replacement concept same day
- IF Hold Rate >50% but low CTR THEN weak CTA or offer-creative mismatch
- IF high engagement but low conversion THEN awareness-stage traffic (wrong funnel)
- IF ncROAS >2.0 THEN profitable for scaling (ignore blended ROAS)

SCALING:
- IF spending <$10k/month THEN use 3:2:2 framework (low variance)
- IF spending $20k+/month THEN use 5x5 framework (high variance)
- IF spending $50k+/month THEN ship 5+ new concepts weekly (Rule of 1:10k)
- IF scaling past $100k/month THEN add new prospecting campaigns (avoid single campaign ceiling)
- IF scaling plateaus THEN audit creative flywheel (need weekly fresh concepts)

TROUBLESHOOTING:
- IF compliance flags received THEN audit hooks for sensationalism
- IF pixel firing but no conversions attributed THEN check Conversion API setup
- IF budget unspent 50%+ THEN increase audience size or bid cap too low
- IF audience fragmentation detected THEN consolidate to M3 lanes only
- IF retargeting saturated (frequency >5) THEN expand retargeting window or reduce budget

F) METRICS TABLE
| Failure Mode | Key Signal Metric | Threshold | Diagnostic Test | Source |
|--------------|------------------|-----------|-----------------|--------|
| Creative Fatigue | Hook Rate decline | >30% drop from baseline | Compare week 1 vs current | [SRC] |
| Attribution Hallucination | Blended ROAS - ncROAS gap | >1.5x | Calculate ncROAS, compare | [SRC] |
| Learning Limited Loop | Conversions per week | <50 | Check ad set status | [SRC] |
| Hook-Body Mismatch | Hook Rate vs Conversion Rate | Hook >35%, Conv <2% | Analyze landing page bounce rate | [SRC] |
| Pixel Malnutrition | Events Manager conversions | 0 despite sales | Test purchase, check Pixel Helper | [SRC] |

G) PATTERNS (15-25)
Diagnostic patterns, troubleshooting workflows, recovery sequences:
- Creative Fatigue detection pattern: Week 1 Hook Rate → Week 2 (declining) → Week 3 (30%+ drop) → Rotate creative
- Attribution Hallucination detection: Platform ROAS up → MER flat → Calculate ncROAS → Confirm inflation → Adjust scale targets
- Learning Limited recovery: Check conversion volume → Consolidate ad sets → Increase budget → Monitor exit from Learning Limited
- Troubleshooting workflow: Observe symptom → Run diagnostic test → Confirm root cause → Execute recovery → Monitor improvement → Document prevention

H) FAILURE MODES (Already covered in section C, but extract additional ones if found)

I) GOLDEN RUNS (3-5)
- Scenario 1: Diagnose and recover from Creative Fatigue (Hook Rate 35% → 24%, frequency 4.2, ship replacement within 24h, restore to 32%)
- Scenario 2: Detect Attribution Hallucination (platform ROAS 3.2x, MER 2.1x, run holdout test, discover 1.4x true ncROAS, adjust scale targets)
- Scenario 3: Fix Learning Limited Loop (3 ad sets stuck, <30 conv/week each, consolidate to 1 ad set, 90 conv/week, exit Learning Limited in 3 days)

J) COMPLIANCE & GUARDRAILS
- No black-hat workarounds (platform violations)
- Transparent troubleshooting (acknowledge when issues are unfixable without restart)
- Document all failure mode recoveries (for ECR LEARNING phase)

K) CHECKLISTS
- Daily diagnostic: Frequency check, delivery %, learning phase status, Events Manager conversions
- Weekly failure mode scan: Hook Rate trends, ncROAS vs MER, creative fatigue signals, compliance flags
- Monthly deep diagnostic: Holdout test planning, campaign consolidation review, creative pipeline audit

Deliver as structured markdown with YAML blocks. Ensure all 15 failure modes have complete playbooks (Symptoms → Root Cause → Diagnosis → Recovery → Prevention).
```

---

## PROMPT #7 — KB-SCALING-STRATEGIST (Growth Phases & Budget Optimization)

**Notebook Name:** `Scaling Strategist - Meta Ads Knowledge Extraction`

**Upload Sources:** Scaling case studies, budget optimization guides, multi-campaign strategies, geographic expansion frameworks

**Paste this into NotebookLM:**

```
You are ULTRAMIND Knowledge Extractor for META ADS SCALING STRATEGIST.

Extract grounded, source-tagged knowledge about 3-phase scaling system, budget optimization, incrementality validation, multi-campaign strategies, and geographic expansion.

FOCUS AREAS:
- 3-Phase Scaling System (Validation → Growth → Scale)
- ncROAS-based scale decisions (when to increase budget, when to plateau)
- Budget Cliff detection (audience ceiling identification)
- Multi-campaign scaling (avoid single campaign ceiling)
- Geographic expansion strategies (Tier 1/2/3 markets)
- Incrementality validation (holdout tests, Conversion Lift Studies)
- Scaling metrics dashboard (what to monitor daily/weekly/monthly)

REQUIREMENTS:
- Tag every claim: [SRC: source_name | timestamp]
- Include direct quotes (≤25 words) for scaling principles
- Favor "how-to" over theory (actionable scaling steps)

OUTPUT STRUCTURE:

A) SOURCE MAP
List each source: ID, title, author, key topics, unique contribution

B) TAXONOMY
Categories: Scaling Phases, Budget Optimization, Multi-Campaign Strategy, Geographic Expansion, Incrementality Testing
Subcategories:
- Phases: Validation ($0-10k), Growth ($10k-50k), Scale ($50k-200k+)
- Budget tactics: Incremental scaling (20% per adjustment), Audience expansion, Campaign multiplication
- Geo tiers: Tier 1 (US/UK/CA/AU), Tier 2 (EU/NZ/SG), Tier 3 (LATAM/SEA/Eastern EU)
Consensus points: ncROAS >1.5x required for scaling, 20% max budget increase per adjustment
Divergences: Different scaling speeds (conservative vs aggressive)
Gaps: Missing scaling tactics or market expansion strategies

C) FRAMEWORKS (8-12)

3-PHASE SCALING SYSTEM (3 frameworks):

1. PHASE 1: VALIDATION ($0-10k/month)
   - Goal: Achieve ncROAS >1.5x consistently for 14+ days
   - Framework: 3:2:2 testing (low variance, stable campaigns)
   - Creative volume: 3-5 concepts/week
   - Structure: Single M3 swim lane setup (Prospecting/Retargeting/Retention)
   - Exit criteria:
     - ncROAS >1.5x for 14+ days
     - MER stable (not declining)
     - Hook Rate >30% on winning creatives
     - Creative flywheel established (weekly production)
   - Key metrics: ncROAS trend, MER, CPA stability, Hook Rate
   - Circuit breaker: If ncROAS <1.0 after 30 days, fix offer or creative before scaling

2. PHASE 2: GROWTH ($10k-50k/month)
   - Goal: Scale budget 20% weekly while maintaining ncROAS >1.5x
   - Framework: 5x5 testing for prospecting (high variance, winner identification)
   - Creative volume: 5-7 concepts/week
   - Structure: Add 2nd prospecting campaign (different creative angles to unlock new audience segments)
   - Scaling protocol:
     1. Week 1: Increase budget 20% ($10k → $12k)
     2. Monitor: ncROAS, MER, frequency, Hook Rate (48-72h)
     3. If metrics stable: Week 2 increase 20% ($12k → $14.4k)
     4. If ncROAS drops >20%: Pause scaling, diagnose issue (creative fatigue, audience ceiling)
     5. Repeat until $50k/month or plateau detected
   - Exit criteria:
     - MER >3.0 (healthy multi-channel efficiency)
     - ncROAS >1.5x at $50k/month spend
     - 2+ prospecting campaigns active (avoiding single campaign ceiling)
     - Creative flywheel scaling (5-7 concepts/week shipped consistently)

3. PHASE 3: SCALE ($50k-200k+/month)
   - Goal: Expand to new markets/products while maintaining MER >3.0
   - Framework: Creative Flywheel (Rule of 1:10k = 5-20 concepts/week)
   - Creative volume: 10-20 concepts/week (or 1 per $10k spend)
   - Structure:
     - 3-5 prospecting campaigns (different creative angles)
     - Geographic expansion (new countries/regions)
     - Product line expansion (cross-sell, upsell, new offers)
   - Scaling tactics:
     - Multi-campaign strategy (avoid audience ceiling per campaign)
     - Geographic testing (Tier 2/3 markets for volume, Tier 1 for profit)
     - Audience segmentation by intent (bottom-funnel vs top-funnel campaigns)
   - Exit criteria: None (continuous optimization and expansion)
   - Key metrics: ncROAS by campaign/geo, MER by channel, creative production rate

BUDGET OPTIMIZATION FRAMEWORKS (3):

4. Budget Scaling Protocol Framework
   - Rule: 20% max increase per adjustment (avoid algorithm shock)
   - Frequency: 3-5 day intervals between increases (let learning stabilize)
   - Monitoring: ncROAS, MER, frequency, Hook Rate, CPA trend
   - Circuit breaker: If ncROAS drops >20%, pause scaling, diagnose issue (creative fatigue, audience ceiling, offer-market mismatch)
   - Recovery: Fix root cause before resuming scale

5. Budget Cliff Detection Framework
   - Symptoms: Profitable at $X spend, unprofitable when scaling to $1.5X+ (CPA spikes, frequency rises, ncROAS drops)
   - Diagnosis:
     1. Audience size vs daily spend ratio (need 100x minimum, e.g., 1M audience for $10k/day spend)
     2. Frequency trend: If rising fast during scale (>3.5), hitting audience ceiling
     3. CPA trend: If increases 30%+ during scale, losing efficiency
   - Root Cause: Algorithm exhausted available users interested in this creative angle
   - Recovery:
     1. Add new prospecting campaign with different creative angles (unlock different audience segments)
     2. Expand to new geographic markets (if applicable)
     3. Test new creative concepts to access different psychographic triggers
   - Prevention:
     1. Build 3-5 prospecting campaigns BEFORE hitting ceiling
     2. Diversify creative angles (test different hooks/stories/mechanisms)
     3. Monitor frequency daily (pause scaling if >3.5)

6. Multi-Campaign Scaling Framework
   - Problem: Single campaign ceiling (algorithm hits audience limit at $X spend)
   - Solution: Build multiple prospecting campaigns with different creative angles
   - Structure:
     - Campaign 1: Founder-led VSL angle (authority + trust)
     - Campaign 2: Scam Hook angle (contrarian positioning)
     - Campaign 3: Hero vs Villain story angle (narrative-driven)
     - Campaign 4: Data/proof angle (logical persuasion)
     - Campaign 5: Testimonial/social proof angle (peer validation)
   - Each campaign unlocks different audience psychographics
   - Budget allocation: Distribute evenly initially, then reallocate to winners
   - Retargeting: Separate retargeting campaign for each prospecting campaign (clean attribution)

GEOGRAPHIC EXPANSION FRAMEWORKS (2):

7. Geographic Expansion Strategy Framework
   - Tier 1 Markets: US, UK, CA, AU
     - Characteristics: Highest ROAS potential, highest CPA, most competitive
     - Strategy: Profit focus, premium positioning, high-quality creative
   - Tier 2 Markets: EU (DE, FR, ES, IT), NZ, SG
     - Characteristics: Moderate ROAS, moderate CPA, less competitive
     - Strategy: Volume + profit balance, localized creative (language/culture)
   - Tier 3 Markets: LATAM, SEA, Eastern EU
     - Characteristics: Lower ROAS, lower CPA, high volume potential
     - Strategy: Volume focus, cost-efficient creative, test viability
   - Expansion sequence: Validate Tier 1 → Test Tier 2 → Scale Tier 3 (if profitable)

8. Localization Requirements Framework
   - Language: Native language copy (not Google Translate, hire native speaker)
   - Currency: Local currency pricing (not USD conversion)
   - Cultural hooks: Local references, slang, pain points (not US-centric)
   - Compliance: Local advertising regulations (GDPR in EU, etc.)
   - Creative adaptation: Visual styles matching local norms

INCREMENTALITY VALIDATION FRAMEWORKS (2):

9. Holdout Test Planning Framework
   - When to run: Annually for validation, before major budget jumps ($50k → $100k+), when stakeholders question effectiveness
   - Baseline period: 14-30 days with ads on, measure MER and conversion volume
   - Holdout period: 14-30 days with ads off, measure organic revenue
   - Lift calculation: (baseline revenue - organic revenue) / ad spend = true incremental ROAS
   - Interpretation: Use lift data to set realistic scale targets, adjust budget allocation

10. Conversion Lift Study Framework
    - Requirements: $50k+/month spend for statistical validity, 2-4 week test duration
    - Meta runs controlled experiment: Test group (sees ads) vs Control group (no ads)
    - Output: Incremental conversion count, incremental CPA, confidence intervals
    - Use case: Need statistically valid incrementality data for board/investors

SCALING DASHBOARD FRAMEWORK:

11. Scaling Metrics Dashboard Framework
    - Daily monitoring: Spend vs target, delivery %, frequency by campaign, compliance flags
    - Weekly monitoring: ncROAS trend, MER trend, creative production rate (concepts shipped), Hook Rate by creative
    - Monthly monitoring: Geographic performance (ncROAS by market), holdout test planning, audience ceiling indicators (frequency spikes, CPA trends)

D) SOPs (5-8)
- Weekly scaling review (ncROAS trend, budget adjustment decision, creative volume check)
- Monthly incrementality validation (MER vs platform ROAS comparison, holdout test planning)
- Quarterly geographic expansion test (Tier 2 market launch, performance review)
- Budget scaling SOP (20% increase protocol, monitoring checklist, circuit breaker triggers)
- Multi-campaign launch SOP (creative angle selection, budget distribution, retargeting setup)

E) HEURISTICS (20-35 IF-THEN rules)

DIAGNOSTIC:
- IF ncROAS >1.5x for 14+ days THEN ready to scale (increase budget 20%)
- IF ncROAS drops >20% after budget increase THEN pause scaling, diagnose issue
- IF frequency rising during scale (>3.5) THEN hitting audience ceiling (add new campaign or geo)
- IF CPA increasing 30%+ during scale THEN losing efficiency (audit creative fatigue or audience saturation)

OPTIMIZATION:
- IF ncROAS >2.0 THEN highly profitable (aggressive scaling opportunity)
- IF MER declining during scale THEN channel cannibalization or attribution drift
- IF creative production can't keep up with spend THEN pause scaling, build creative bench

SCALING:
- IF spending <$10k/month THEN use 3:2:2 framework (Validation Phase)
- IF spending $10k-50k/month THEN use 5x5 framework (Growth Phase)
- IF spending $50k+/month THEN use Creative Flywheel (Scale Phase, 5-20 concepts/week)
- IF spending $100k+/month THEN build 3-5 prospecting campaigns (avoid single campaign ceiling)
- IF scaling plateaus THEN test geographic expansion (Tier 2 markets)

GEOGRAPHIC EXPANSION:
- IF Tier 1 markets validated (ncROAS >1.5x) THEN test Tier 2 (EU, NZ, SG)
- IF Tier 2 profitable THEN scale volume in Tier 3 (LATAM, SEA)
- IF new geo underperforms (<1.0 ncROAS) for 30 days THEN pause, reallocate to proven markets

INCREMENTALITY:
- IF spending $50k+/month THEN run Conversion Lift Study annually
- IF MER flat despite platform ROAS growth THEN run holdout test to validate true lift
- IF holdout test shows <50% incremental lift THEN scale back ad spend or fix attribution

F) METRICS TABLE
| Metric | Purpose | Threshold | Action Trigger | Source |
|--------|---------|-----------|----------------|--------|
| ncROAS Trend | Scale decision readiness | >1.5x for 14+ days | <1.5x = not ready to scale | [SRC] |
| MER Trend | Multi-channel health | Should trend with platform ROAS | MER flat while ROAS grows = attribution drift | [SRC] |
| Budget Delivery % | Spend pacing | 80-100% daily | <70% = increase bid or expand audience | [SRC] |
| Frequency by Campaign | Audience ceiling indicator | <3.5 healthy | >3.5 = hitting ceiling, add new campaign | [SRC] |
| Creative Production Rate | Flywheel health | 1 concept per $10k monthly spend | Behind pace = bottleneck, pause scaling | [SRC] |

G) PATTERNS (10-20)
Scaling patterns, budget adjustment sequences, expansion workflows:
- Validation → Growth → Scale progression: $0-10k (validate) → $10k-50k (grow) → $50k+ (scale)
- Budget scaling pattern: Current spend × 1.2 = new budget, monitor 48-72h, repeat if stable
- Multi-campaign build pattern: Campaign 1 validated → Add Campaign 2 (different angle) → Add Campaign 3 → Distribute budget to winners
- Geographic expansion: Tier 1 (validate) → Tier 2 (test) → Tier 3 (scale volume)

H) FAILURE MODES (6-10)
- Budget Cliff (profitable at $X, unprofitable at $1.5X+, audience ceiling hit)
- Creative Production Bottleneck (can't ship weekly, scaling stalled, manual workflow)
- Geographic Expansion Failure (new market underperforms, localization insufficient)
- Multi-Campaign Dilution (too many campaigns, learning spread thin, none exit learning phase)
- Over-Scaling (ncROAS drops below 1.0, unprofitable growth, ego-driven spending)
- Incrementality Validation Ignored (scaling based on platform ROAS, true lift unknown, waste discovered later)

I) GOLDEN RUNS (3-5)
- Scenario 1: Validation → Growth scaling (start $5k/month, validate ncROAS 1.8x, scale to $30k/month in 8 weeks)
- Scenario 2: Budget Cliff detection and recovery (hit ceiling at $40k/month, add 2nd campaign, break through to $75k/month)
- Scenario 3: Geographic expansion (US validated 2.1x ncROAS, test EU markets, DE/FR profitable at 1.6x, scale to 30% of total spend)

J) COMPLIANCE & GUARDRAILS
- No fake growth claims (incremental ROAS only, not blended)
- Transparent about plateau risks (audience ceilings exist, communicate to stakeholders)
- Responsible scaling (don't sacrifice profitability for vanity metrics)

K) CHECKLISTS
- Weekly scaling review: ncROAS trend check, budget adjustment decision, creative volume validation, frequency monitoring
- Monthly incrementality validation: MER vs platform ROAS comparison, holdout test planning, geographic expansion opportunities
- Quarterly deep review: Multi-campaign structure audit, creative production capacity review, geographic portfolio optimization

Deliver as structured markdown with YAML blocks. Ensure 3-phase scaling system is detailed with clear exit criteria and circuit breakers.
```

---

## WORKFLOW SUMMARY

### For Each KB Module:

1. **Create Notebook** in NotebookLM with module name
2. **Upload sources** (training videos, transcripts, case studies, swipe files)
3. **Run the corresponding prompt** (Prompt #1 for Campaign Architecture, etc.)
4. **Save raw output** as: `KB_[MODULE_NAME]_COMPENDIUM_RAW.md`
5. **Repeat for all 7 modules**

### After All 7 Compendiums Extracted:

6. **Send all 7 raw compendiums to GPT Stage-2 Synthesizer**
7. **GPT synthesizes** into KB draft XML files (7 files)
8. **Send KB drafts to Claude Code**
9. **Claude builds final production KB modules** with:
   - Constitutional compliance sections
   - Consciousness profiles (Neuro-Box 6D mapping)
   - Explicit dependencies
   - YAML-formatted frameworks and metrics
   - Full failure mode playbooks

---

## VALIDATION CHECKLIST (Before Sending to GPT)

For each raw compendium, verify:

- [ ] 8-20 frameworks extracted (with source tags, quotes, steps, metrics)
- [ ] 20-50 heuristics in IF-THEN format (Diagnostic, Optimization, Scaling, Troubleshooting)
- [ ] 5-10 SOPs with frequency and quality gates
- [ ] 8-15 failure modes with full playbooks (Symptoms → Root Cause → Diagnosis → Recovery → Prevention)
- [ ] 10-25 patterns extracted (templates, workflows, sequences)
- [ ] 3-5 golden runs (test scenarios with inputs, outputs, success criteria)
- [ ] All claims source-tagged: [SRC: source_name | timestamp]
- [ ] Direct quotes included (≤25 words) for key principles
- [ ] Metrics table with thresholds and action triggers
- [ ] Compliance & guardrails section present
- [ ] Checklists for daily/weekly/monthly operations

---

## EXPECTED OUTPUT SIZES

| KB Module | Expected Compendium Size | Expected Final XML Size |
|-----------|-------------------------|------------------------|
| Campaign Architecture | 8-12 pages | 60KB |
| Andromeda Creative Engine | 10-15 pages | 55KB |
| Image Generator | 8-12 pages | 50KB |
| Image Analyzer | 7-10 pages | 45KB |
| Measurement & Attribution | 8-12 pages | 55KB |
| Performance Diagnostics | 12-18 pages | 60KB |
| Scaling Strategist | 8-12 pages | 50KB |

**Total:** ~60-90 pages of raw compendiums → ~375KB of final XML KB modules

---

## NEXT STEPS

1. **Upload sources to NotebookLM** (videos, transcripts, case studies)
2. **Run all 7 prompts** (extract compendiums)
3. **Send compendiums to me** (I'll review and pass to GPT Stage-2)
4. **GPT synthesizes KB drafts**
5. **I build final production KB modules** with constitutional compliance and dependencies

**Timeline:**
- NotebookLM extraction: 1-2 hours (7 prompts × 10-15 min each)
- Your review: 2-3 hours
- GPT Stage-2 synthesis: 1-2 hours
- Claude KB module building: 3-4 days (7 modules × 4-6 hours each)

**Total:** ~1 week from extraction to production-ready KB suite

---

**Version:** 1.0
**Date:** 2026-01-19
**Status:** Ready for NotebookLM extraction

*These prompts are optimized for NotebookLM's context limits (~200-300 tokens per prompt) while extracting maximum granular detail for each KB module.*
