# SUPERMIND / SUPERSKILLS — REFACTOR & MIGRATION PLAN v1.1
## Produced by Refactor & Migration Director — Opus 4.6

**Date:** 2026-02-28
**Input Documents Reviewed:** 24 files across SUPERMIND PROJECT folder
**Scope:** Architecture review, repo proposal, skill refactor playbook, orchestrator design, memory roadmap
**Target:** Migration to new Claude MAX account + GitHub repo (`chrisflynnai-ux/Superskills`)

---

## 1. ASSUMPTIONS (Bulleted)

- The ~50 production skills (500–1500 lines XML each) will be provided in a second pass. This plan is designed to work with or without them present.
- The new Claude MAX account is a clean slate; no legacy context, projects, or memory files carry over automatically.
- The existing GitHub repo at `chrisflynnai-ux/Superskills` contains older skill versions. The new repo will be a fresh structure, not a fork.
- XML remains the primary skill format for the initial migration. XML→MD conversion is a later-stage optimization, not a blocker.
- Claude Opus 4.6 is the primary brain for strategy, writing, and orchestration. Gemini 3.1 handles visual/design. Codex 5.3 handles code debugging/refinement.
- The 4-Track model (Research → Drafts → Production → Polish) supersedes the older 3-Phase model in ZPWO v3.0.
- SSOT objects (PROJECT_BRIEF, MESSAGE_SPINE, EVIDENCE_PACK) are the canonical interchange format between tracks.
- The Lean Context Protocol (LCP) and Zero-Point Context Strategy are hard architectural constraints, not aspirational.
- "Memento" memory stack (CLAUDE.md, Context.md, Memory.md, Insights.md, Soul.md, Review.md) is the target memory model for Claude Code integration.
- Revenue model (Interscale agency, skill marketplace, Freedomation OS) is a business context constraint — the architecture must support paid skill distribution and white-labeling.
- Copy Director is the highest-priority missing skill and blocks full automated orchestration.
- Flowgrams (visual workflow diagrams via Excalidraw) are a medium-term deliverable, not a migration blocker.

---

## 2. RISKS (Bulleted with Mitigation)

- **Risk: Scope creep during migration.** The vision spans an operating system, marketplace, learning platform, and agency toolset. Mitigation: This plan treats migration as Phase 0 — get the repo clean, skills normalized, and orchestration working. Product features (Flowgrams, marketplace, Freedomation) are Phase 2+.

- **Risk: Skill naming inconsistency blocks automated routing.** Current names mix formats (e.g., `long_form_vsl_script_architect_v2.0.xml`, `mma_master_monitor_agent_v1_0.xml`, `EMAIL_COPY_GENIUS_v2_0_COMPLETE.md`). Mitigation: Define a single `skill_id` convention (Deliverable 2) and apply it to all 50 skills during normalization.

- **Risk: Monolithic skills resist decomposition.** Some skills at 1500 lines embed rules, reasoning, IO contracts, and implementation in one undifferentiated block. Mitigation: The Skill Refactor Playbook (Deliverable 3) separates these into four layers within each skill file, not across files — preserving self-containment while adding structure.

- **Risk: XML→MD conversion introduces data loss.** XML's self-describing tags, attributes, and nesting don't map 1:1 to markdown. Mitigation: Build a lossless mapping spec (XML tag → MD heading + frontmatter convention). Convert only after a validator confirms round-trip integrity.

- **Risk: Token bloat from loading orchestrator + skill + SSOTs simultaneously.** A 1500-line skill + ZPWO + MMA + 3 SSOTs could exceed comfortable context. Mitigation: Enforce the LCP tiered loading model. Skills stay out of project knowledge; they load per-conversation. Orchestrator stays lean (~500 lines).

- **Risk: Copy Director dependency blocks automated Track 2 routing.** Without it, humans manually assign skills. Mitigation: Build Copy Director v1.0 as Priority 1 post-migration (simple routing logic, not full intelligence).

- **Risk: Neo4j/Convex/Firebase infrastructure not ready.** The graph knowledge layer and real-time state backbone are dependencies for Phase 4+. Mitigation: Phase 1 uses file-based memory (CLAUDE.md stack) with no external dependencies. Infrastructure is layered in incrementally.

- **Risk: Multi-brain routing (Claude/Gemini/Codex) adds coordination overhead.** Mitigation: v1 orchestrator uses Claude-only routing. Multi-brain routing is a configuration option, not a requirement. Add Gemini/Codex routing rules only when specific track assignments demand them.

---

## 3. DELIVERABLE 1 — PROJECT CLARITY SNAPSHOT

### What Supermind/Superskills Is

Supermind is a Claude-centric agentic operating system that replaces brittle automations (n8n, Zapier, GoHighLevel) with modular, AI-operated "Superskills" — large structured files (500–1500 lines, XML or MD) that encode domain expertise, execution rules, quality gates, and knowledge components. Skills are operated by AI agents across a 4-phase production pipeline (Research → Drafts → Production → Polish) with human-in-the-loop handoffs at each gate. The system is designed for the agency brand Interscale, targeting marketers, coaches, SaaS founders, and e-commerce operators, with a path toward an autonomous agent-to-agent marketplace under the product name Freedomation.

### What It Is NOT

- NOT a chatbot or prompt library. Skills are agent operating manuals with typed I/O contracts, quality validators, and decomposition maps.
- NOT a no-code visual builder (yet). Flowgrams are a future layer; the core is code-first and file-first.
- NOT a monolithic platform. It's a composable architecture where skills, orchestrators, and memory layers can be swapped independently.
- NOT dependent on a single LLM. While Claude-optimized, the RBI architecture (Rules/Brain/Implementation) allows brain-swapping across Claude, Gemini, and Codex.
- NOT a replacement for human judgment. Every track transition requires a human gate. Autonomy is earned incrementally through learned constraints and self-repair.

### The 4-Phase Track Model

| Track | Name | Agent Fit | Purpose | Exit Gate |
|-------|------|-----------|---------|-----------|
| 1 | Research & Plan | Kimi/Manus (parallel extraction) | Extract market intelligence, build SSOTs | Human approves foundational docs |
| 2 | Drafts & Development | Claude Teams (nuanced writing) | Strategic angle selection → script/copy drafting | Human approves draft direction |
| 3 | Production & Refine | Same skill (production mode) + MMA audit | Full production build with validators | MMA PASS or human override |
| 4 | Polish & Perfect | Skeptic Avatar + HPE + NRA | Stress-test, voice polish, resonance audit | Human final publish decision |

### The RBI Model

| Component | Role | Example |
|-----------|------|---------|
| **Rules** (R) | SOPs defining what to do, in what order, with what constraints | A skill's `<ExecutionProtocol>` section specifying the 11-step VSL writing process |
| **Brain** (B) | The LLM model selected for the task based on required capability | Claude Opus for strategy/writing, Gemini for visual design, Codex for code refinement |
| **Implementation** (I) | Deterministic scripts that execute the work the LLM plans | Python validators (VT-01 through VT-10), Playwright automation scripts, data transformers |

### The Lean Context Doctrine

The system operates from a "Zero-Point" — a minimal default context (~500 tokens) containing only a skills manifest, SSOT headers, routing rules, and session state. Skills activate on-demand (loading Tier 1 descriptor, then Tier 2 execution context), execute, compress results to SSOTs, and unload. The principle: "Every always-loaded parameter schema competes with your offer, your copy voice, your SSOT objects, and your orchestration rules." Context discipline is accuracy discipline.

### Glossary (15 Key Terms)

| Term | Definition |
|------|------------|
| **Superskill** | A structured file (500–1500 lines, XML/MD) encoding domain expertise, execution rules, I/O contracts, and quality gates for agent operation |
| **Supermind** | An agentic knowledge base with a front-end (Obsidian-like) and an agent librarian, built on SQL/Neo4j |
| **Zero-Point** | The minimal default context state (~500 tokens) from which skills are activated and to which the system returns after execution |
| **SSOT** | Single Source of Truth — canonical typed objects (PROJECT_BRIEF, MESSAGE_SPINE, EVIDENCE_PACK) that persist across track transitions |
| **Track** | One of four sequential production phases (Research → Drafts → Production → Polish), each with specific agent assignments and exit gates |
| **Atom** | The smallest reusable knowledge component (a heuristic, pattern, framework, or spec) that skills assemble from |
| **RBI** | Rules-Brain-Implementation — the three-part architecture ensuring clean separation of SOPs, model selection, and execution |
| **Flowgram** | A visual workflow diagram (Excalidraw-based) showing skill chains, agent assignments, and human checkpoints |
| **LCP** | Lean Context Protocol — the specification for on-demand skill activation with minimal context consumption |
| **MMA** | Master Monitor Agent — the quality guardian that scores outputs across 7 dimensions with pass/fix/escalate verdicts |
| **ZPWO** | Zero-Point Work Orchestrator — the lean routing layer that directs tasks to skills and manages phase transitions |
| **COSM** | Contextually Organized Semantic Memory Site — a domain-specific knowledge collection in machine-friendly format with human PKM front-end |
| **Memento** | The proprietary memory stack (CLAUDE.md, Context.md, Memory.md, Insights.md, Soul.md, Review.md) for persistent agent learning |
| **Copy Director** | The missing strategic routing skill that assigns the correct execution skill (LFVA/SFVW/SPC/ACM/Email) with specific parameters |
| **Progressive Disclosure** | The L1–L4 layering system within skills: L1 routing (~500 tokens), L2 execution (~1500–3500), L3 advanced (~3000), L4 reference (~2000–6000) |

---

## 4. DELIVERABLE 2 — REPO & FILE SYSTEM PROPOSAL

### Repo Tree (GitHub-Ready)

```
supermind/
├── README.md                          # Project overview, quick start, architecture diagram
├── CLAUDE.md                          # Claude Code memory file (persistent context)
├── LICENSE                            # MIT or chosen license
├── .gitignore
│
├── skills/                            # Skills library (~50 skills)
│   ├── _schema/
│   │   ├── skill_schema_v2.xsd        # XML schema definition for validation
│   │   ├── skill_schema_v2.json       # JSON Schema equivalent
│   │   └── SKILL_TEMPLATE_V2.xml      # Canonical template
│   │
│   ├── copy/                          # Domain: copywriting & content
│   │   ├── lfva/                      # Long-Form VSL Architect
│   │   │   ├── lfva_v3.0.0.xml        # Skill file
│   │   │   ├── CHANGELOG.md           # Patch log
│   │   │   └── tests/
│   │   │       ├── golden_output_01.md # Golden trace
│   │   │       └── test_lfva.py       # Validation harness
│   │   ├── sfvw/                      # Short-Form VSL Writer
│   │   ├── spc/                       # Sales Page Copywriter
│   │   ├── acm/                       # Advertorial Copy Master
│   │   ├── ecg/                       # Email Copy Genius
│   │   ├── mwp/                       # Master Writing Partner
│   │   ├── csa/                       # Content Script Architect
│   │   └── vtd/                       # Viral Theme Developer
│   │
│   ├── strategy/                      # Domain: strategic planning & routing
│   │   ├── copy-lead/                 # Angle selection
│   │   ├── copy-director/             # Skill assignment & configuration
│   │   ├── offer-architect/           # Offer structure design
│   │   └── mis/                       # Market Intelligence Synthesizer
│   │
│   ├── research/                      # Domain: intelligence gathering
│   │   ├── market-scout/              # Reconnaissance
│   │   ├── research-ops/              # Deep extraction
│   │   └── evidence-pack-builder/     # Proof assembly
│   │
│   ├── quality/                       # Domain: validation & polish
│   │   ├── mma/                       # Master Monitor Agent
│   │   ├── hpe/                       # Human Persuasion Editor
│   │   ├── nra/                       # Neuro-Resonance Auditor
│   │   ├── skeptic-avatar/            # Red team stress test
│   │   └── vra/                       # Viral Resonance Architect
│   │
│   ├── automation/                    # Domain: technical execution
│   │   ├── browser-orchestrator/      # Playwright/scraping
│   │   ├── cold-outreach/             # Cold outreach architect
│   │   └── lead-gen/                  # Lead generation funnel
│   │
│   └── system/                        # Domain: meta/system skills
│       ├── skill-builder/             # Builds new skills
│       └── skill-auditor/             # Audits existing skills
│
├── orchestration/                     # Orchestrators & routing
│   ├── zpwo/
│   │   ├── zpwo_v4.0.0.xml           # Zero-Point Work Orchestrator (4-track)
│   │   └── CHANGELOG.md
│   ├── orchestrator-core/
│   │   ├── orchestrator_core_v5.0.yaml
│   │   └── CHANGELOG.md
│   ├── sub-agent-configs/
│   │   ├── sub_agent_configs_v3.0.yaml
│   │   └── CHANGELOG.md
│   ├── routing/
│   │   ├── routing_table.yaml         # Skill routing rules
│   │   └── track_definitions.yaml     # 4-track phase definitions
│   └── project-bases/
│       ├── vsl_production.yaml        # VSL project base template
│       └── sales_page_production.yaml # Sales page project base template
│
├── memory/                            # Memento memory stack
│   ├── CLAUDE.md                      # Core persistent memory (always loaded)
│   ├── Context.md                     # Current project/session context
│   ├── Memory.md                      # Long-term learned facts
│   ├── Insights.md                    # Patterns, discoveries, meta-learnings
│   ├── Soul.md                        # Constitutional values, voice, identity
│   ├── Review.md                      # Self-assessment, performance logs
│   └── conventions.md                 # How memory files are consumed by Claude Code
│
├── schemas/                           # Typed contracts & validators
│   ├── ssot/
│   │   ├── project_brief.schema.yaml  # PROJECT_BRIEF schema
│   │   ├── message_spine.schema.yaml  # MESSAGE_SPINE schema
│   │   ├── evidence_pack.schema.yaml  # EVIDENCE_PACK schema
│   │   ├── voice_guide.schema.yaml    # VOICE_GUIDE schema
│   │   ├── angle_set.schema.yaml      # Copy Lead output schema
│   │   └── skill_activation.schema.yaml # Copy Director output schema
│   ├── thread/
│   │   ├── thread_state.schema.json   # Minimal thread state object
│   │   └── handoff_packet.schema.json # SSOT handoff between phases
│   └── validators/
│       ├── pydantic_models.py         # Pydantic v2 models for all SSOTs
│       └── validate_ssot.py           # CLI validator script
│
├── atoms/                             # Shared knowledge components
│   ├── heuristics/
│   │   ├── sales_hook_alignment_triad_v1.md
│   │   └── ...
│   ├── patterns/
│   │   ├── sales_retention_dopamine_2hit_v1.md
│   │   └── ...
│   ├── frameworks/
│   │   ├── sales_dopamine_ladder_v1.md
│   │   └── ...
│   ├── specs/
│   │   ├── two_column_vsl_format_v1.md
│   │   └── ...
│   └── manifest.yaml                  # Atom index with versions and usage map
│
├── examples/                          # End-to-end golden traces
│   ├── vsl_production_run/
│   │   ├── 00_project_brief.yaml
│   │   ├── 01_message_spine.yaml
│   │   ├── 02_evidence_pack.yaml
│   │   ├── 03_angle_set.yaml
│   │   ├── 04_skill_activation.yaml
│   │   ├── 05_vsl_script_v1.md
│   │   ├── 06_mma_scorecard.yaml
│   │   ├── 07_vsl_script_final.md
│   │   └── README.md                  # Walkthrough of the full run
│   └── sales_page_run/
│       └── ...
│
├── docs/                              # Architecture & contributor docs
│   ├── architecture/
│   │   ├── lean_context_protocol.md   # LCP spec
│   │   ├── rbi_model.md              # Rules-Brain-Implementation
│   │   ├── 4_track_model.md          # Track system documentation
│   │   ├── neuro_resonance.md        # Persuasion architecture
│   │   └── gotcha_framework.md       # GOTCHA operational model
│   ├── contributing/
│   │   ├── CONTRIBUTING.md           # How to add/modify skills
│   │   ├── skill_style_guide.md      # Naming, structure, conventions
│   │   └── review_checklist.md       # PR review criteria
│   └── marketplace/
│       ├── marketplace_spec.md       # Skill marketplace architecture
│       └── revenue_model.md          # Revenue sharing model
│
├── tools/                             # Scripts for development & maintenance
│   ├── lint_skill.py                 # Validate skill against schema
│   ├── convert_xml_to_md.py          # XML→MD converter (lossless)
│   ├── convert_md_to_xml.py          # MD→XML converter (round-trip)
│   ├── normalize_naming.py           # Rename skills to convention
│   ├── patch_skill.py                # Apply patch to skill file
│   ├── generate_changelog.py         # Auto-generate changelog from git diff
│   ├── validate_ssot.py              # Validate SSOT against schema
│   ├── atom_usage_audit.py           # Find duplicate atoms across skills
│   └── golden_trace_runner.py        # Run golden traces and compare outputs
│
├── constitution/                      # Values & guardrails
│   ├── resonance_constitution.xml    # Neuro-resonance model
│   └── guardrails.md                 # System-level guardrails
│
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── skill_bug.md
    │   └── skill_request.md
    └── workflows/
        ├── lint_skills.yml            # CI: validate all skills on PR
        └── validate_ssots.yml         # CI: validate SSOT schemas on PR
```

### Naming Conventions

**Skill ID Format (Stable Slug):**
```
{domain}_{function}_{variant}
```
Examples:
- `copy_lfva` (Long-Form VSL Architect)
- `copy_sfvw` (Short-Form VSL Writer)
- `quality_mma` (Master Monitor Agent)
- `strategy_copy_director`
- `research_market_scout`

Rules: lowercase, underscores, no version in the ID. Version lives in metadata.

**File Naming:**
```
{skill_slug}_v{major}.{minor}.{patch}.xml
```
Examples:
- `lfva_v3.0.0.xml`
- `mma_v1.0.0.xml`
- `copy_director_v1.0.0.xml`

**Versioning (SemVer + Patch Logs):**
- MAJOR: Breaking changes to I/O contract or execution protocol
- MINOR: New capabilities, atoms, or validator additions (backwards-compatible)
- PATCH: Bug fixes, constraint updates, wording refinements

Every skill folder contains `CHANGELOG.md` with entries in this format:
```markdown
## [3.0.0] - 2026-02-15
### Changed
- Complete rebuild from atoms (not incremental patch)
- Added AtomManifest section
- Added DecompositionMap for sub-agent coordination
### Added
- Python validators VT-01 through VT-10
- Belief sequence validator
```

**Knowledge Blocks (KB) Representation:**
KBs are now called "Atoms" and live in `/atoms/` as individual files:
```
/atoms/{type}/{name}_v{version}.md
```
Types: `heuristics/`, `patterns/`, `frameworks/`, `specs/`

Each atom file has YAML frontmatter:
```yaml
---
atom_id: heuristic.sales_hook_alignment_triad
version: 1
type: heuristic
domain: sales
used_by: [copy_lfva, copy_sfvw, copy_spc]
created: 2026-01-15
---
```

**Progressive Disclosure Layers:**
Within each skill file, layers are marked with XML comments:
```xml
<!-- ===== L1: ROUTING (always loaded, ~500 tokens) ===== -->
<!-- ===== L2: EXECUTION (loaded when working, ~1500-3500 tokens) ===== -->
<!-- ===== L3: ADVANCED (loaded for complex scenarios, ~3000 tokens) ===== -->
<!-- ===== L4: REFERENCE (loaded rarely, ~2000-6000 tokens) ===== -->
```

---

## 5. DELIVERABLE 3 — SKILL REFACTOR PLAYBOOK

### Pipeline: Applied to Each of ~50 Skills

#### Step 1: CLASSIFY

Assign each skill a classification tuple:

| Dimension | Values |
|-----------|--------|
| **Domain** | `copy`, `strategy`, `research`, `quality`, `automation`, `system` |
| **Function** | `writer`, `auditor`, `router`, `builder`, `analyst`, `validator` |
| **Track Position** | `T1` (Research), `T2` (Drafts), `T3` (Production), `T4` (Polish), `TX` (Cross-track) |
| **Tier** | `system`, `meta`, `production`, `experimental` |
| **Complexity** | `A` (simple, <500 lines), `B` (standard, 500–1000), `C` (complex, 1000+) |

**Output:** A classification CSV:
```csv
skill_id, domain, function, track, tier, complexity, current_filename, line_count
copy_lfva, copy, writer, T2, production, C, long_form_vsl_script_architect_v3.0.0.xml, 1555
quality_mma, quality, validator, TX, system, B, mma_master_monitor_agent_v1_0.xml, 1066
```

**Validator:** Every skill has exactly one domain, one primary function, and one primary track.
**Evidence of success:** Classification CSV covers all 50 skills with no blanks.

#### Step 2: NORMALIZE STRUCTURE

Apply the `SKILL_TEMPLATE_V2.xml` schema to every skill. Each skill must contain these sections in this order:

```xml
<Skill skill_id="..." name="..." version="..." status="...">
  <Meta>              <!-- Identity, tier, model, sister skills -->
  <Contract>          <!-- Inputs, outputs, non-goals -->
  <Dependencies>      <!-- Upstream/downstream skills, SSOTs -->
  <AtomManifest>      <!-- Machine-readable atom dependency list -->
  <ExecutionProtocol> <!-- The actual rules/steps/SOP -->
  <OutputRules>       <!-- Deterministic formatting rules -->
  <SelfCheck>         <!-- Built-in validators and quality gates -->
  <ProgressiveDisclosure> <!-- L1-L4 layer markers -->
  <DecompositionMap>  <!-- Parallel vs sequential task breakdown -->
  <LearnedConstraints> <!-- Discovered failure modes and fixes -->
  <PatchLog>          <!-- Version history -->
</Skill>
```

**Validator:** `tools/lint_skill.py` validates every skill against `skills/_schema/skill_schema_v2.xsd`.
**Evidence of success:** `lint_skill.py` returns PASS for all 50 skills.

#### Step 3: SEPARATE CONCERNS (Within File)

For each skill, identify and tag these four layers using XML comments:

| Layer | Content | Tag Pattern |
|-------|---------|-------------|
| **(a) Rules/SOP** | Step-by-step execution protocol, ordering, constraints | `<!-- LAYER:RULES -->` |
| **(b) Reasoning Policy** | When to use which approach, conditional logic, model-selection guidance | `<!-- LAYER:REASONING -->` |
| **(c) I/O Contract** | Input schemas, output schemas, SSOT dependencies, non-goals | `<!-- LAYER:CONTRACT -->` |
| **(d) Tools/Impl Hooks** | Python validators, script references, API calls, tool integrations | `<!-- LAYER:IMPL -->` |

Important: These layers stay inside a single file. The separation is structural (tagged sections), not physical (separate files). Self-containment is preserved.

**Validator:** Each skill has all four layer tags present.
**Evidence of success:** `grep -c "LAYER:" skill.xml` returns 4 for every skill.

#### Step 4: ADD DETERMINISTIC OUTPUT RULES + SELF-CHECK

For each skill, ensure:

1. **Output Rules** section specifies exact formatting (markdown headers, YAML structure, two-column format, etc.)
2. **Self-Check** section includes at minimum:
   - A checklist the agent runs before declaring output complete
   - Scoring thresholds (if applicable to MMA)
   - Known failure modes with recovery actions

Template for Self-Check:
```xml
<SelfCheck>
  <PreSubmit>
    <Check id="SC-01">All required SSOT fields populated</Check>
    <Check id="SC-02">Output format matches OutputRules spec exactly</Check>
    <Check id="SC-03">No placeholder text remains ([BRACKETED_VALUES])</Check>
    <Check id="SC-04">Belief sequence integrity (if applicable)</Check>
    <Check id="SC-05">Evidence cited for every claim (if applicable)</Check>
  </PreSubmit>
  <MMAGate mode="M1|M2|M4" threshold="7.0|8.0|9.0"/>
  <FailureModes>
    <Mode trigger="missing_evidence" recovery="Request EVIDENCE_PACK reload"/>
    <Mode trigger="voice_drift" recovery="Re-read VOICE_GUIDE, apply HPE pass"/>
  </FailureModes>
</SelfCheck>
```

**Validator:** Every skill has `<SelfCheck>` with at least 3 `<Check>` items.
**Evidence of success:** No skill passes lint without SelfCheck section.

#### Step 5: ADD TEST HARNESS + GOLDEN OUTPUTS

For each skill:

1. Create a `tests/` subfolder inside the skill directory
2. Add at least one golden output file (the "correct" output for a known input)
3. Add a test script that:
   - Loads the skill + a known SSOT set
   - Runs the skill's Self-Check validators programmatically
   - Compares structural output (headings, sections, format) against golden trace
   - Does NOT compare creative content word-for-word (LLMs are non-deterministic)

```python
# tests/test_lfva.py
def test_output_structure():
    """Verify LFVA output has all 11 steps in two-column format."""
    output = load_output("golden_output_01.md")
    assert "## Step 1:" in output
    assert "## Step 11:" in output
    assert "| Audio |" in output  # Two-column header
    assert output.count("## Step") == 11

def test_belief_sequence():
    """Verify belief sequence is present and ordered."""
    output = load_output("golden_output_01.md")
    beliefs = extract_beliefs(output)
    assert len(beliefs) == 4
    assert beliefs[0]["type"] == "identity"  # Belief ordering

def test_self_check_all_pass():
    """Run all SC-XX checks against golden output."""
    # ...
```

**Validator:** `pytest skills/{domain}/{skill}/tests/` passes for every skill.
**Evidence of success:** CI pipeline runs all tests on PR, all green.

#### Step 6: ADD PATCH LOG

Every skill gets a `CHANGELOG.md` in its directory. Initial entry documents the refactor:

```markdown
## [X.Y.Z] - 2026-02-28
### Refactored
- Normalized to SKILL_TEMPLATE_V2 schema
- Added AtomManifest section
- Added DecompositionMap section
- Added SelfCheck validators
- Added test harness with golden outputs
- Separated concern layers (Rules/Reasoning/Contract/Impl)
- Renamed from {old_filename} to {new_filename}
```

**Validator:** `CHANGELOG.md` exists and has at least one entry.
**Evidence of success:** `ls skills/*/CHANGELOG.md` returns 50 results.

#### Step 7: XML→MD CONVERSION (When Warranted)

Conversion criteria (all must be true):
- [ ] Skill has passed Steps 1–6 in XML
- [ ] Round-trip converter (`tools/convert_xml_to_md.py` → `tools/convert_md_to_xml.py`) produces identical semantic output
- [ ] Target platform (Claude Code, Gemini, Codex) shows measurably better compliance with MD format
- [ ] No progressive disclosure functionality is lost

Lossless mapping spec:
```
XML <Skill> attributes     → MD YAML frontmatter
XML <Meta>                 → ## Meta (structured YAML block)
XML <Contract>             → ## Contract (YAML block)
XML <ExecutionProtocol>    → ## Execution Protocol (numbered markdown)
XML <SelfCheck>            → ## Self-Check (checklist)
XML comments <!-- L1: -->  → Markdown comments or H3 headers
XML CDATA                  → Fenced code blocks
```

**Validator:** `diff <(convert_to_md skill.xml | convert_to_xml) skill.xml` shows no semantic differences.
**Evidence of success:** Round-trip test passes for every converted skill.

### Refactor Execution Order

Do NOT refactor all 50 skills at once. Batch by priority:

| Batch | Skills | Rationale |
|-------|--------|-----------|
| **Batch 1** (Week 1) | LFVA, SFVW, MMA, ZPWO | Core production + orchestration. Already closest to v3 standard. |
| **Batch 2** (Week 2) | Copy Lead, Copy Director (build), SPC, ACM, ECG | Strategic layer + remaining copy skills. |
| **Batch 3** (Week 3) | HPE, NRA, Skeptic Avatar (build), VRA | Quality/polish layer. |
| **Batch 4** (Week 4) | Market Scout, Research Ops, MIS, Evidence Pack Builder | Research layer. |
| **Batch 5** (Weeks 5-6) | All remaining skills | Automation, system, and experimental. |

---

## 6. DELIVERABLE 4 — MASTER ORCHESTRATOR & ROUTING PLAN

### Orchestrator Design: ZPWO v4.0

The orchestrator is NOT a monolithic brain. It is a lean router (~500 tokens at Zero-Point) that:

1. **Selects skill** by matching task intent to routing table
2. **Runs a 4-phase track** with explicit gate conditions
3. **Enforces lean context** by loading/unloading skills per conversation
4. **Produces traceable thread logs** (JSON state objects)
5. **Supports multi-brain routing** via configurable brain assignments per track

### Routing Rules

```yaml
# orchestration/routing/routing_table.yaml

routes:
  # Track 1: Research & Plan
  - command: "/intake"
    chain: [research_market_scout, research_research_ops, research_mis]
    track: T1
    brain: claude-sonnet  # Research doesn't need Opus

  - command: "/research"
    skill: research_market_scout
    track: T1

  - command: "/synthesize"
    skill: research_mis
    track: T1

  # Track 2: Strategic Layer
  - command: "/strategy"
    chain: [strategy_copy_lead, strategy_copy_director]
    track: T2
    brain: claude-opus  # Strategy needs Opus reasoning

  # Track 2: Execution (routed by Copy Director)
  - command: "/vsl-long"
    skill: copy_lfva
    track: T2
    brain: claude-opus

  - command: "/vsl-short"
    skill: copy_sfvw
    track: T2
    brain: claude-sonnet

  - command: "/salespage"
    skill: copy_spc
    track: T2
    brain: claude-opus

  - command: "/advertorial"
    skill: copy_acm
    track: T2
    brain: claude-sonnet

  - command: "/email"
    skill: copy_ecg
    track: T2
    brain: claude-sonnet

  - command: "/content-video"
    skill: copy_csa
    track: T2
    brain: claude-sonnet

  # Track 3: Production + Validation
  - command: "/produce"
    skill: "{active_skill}"  # Same skill as Track 2
    track: T3
    brain: claude-opus
    validators: [belief_sequence, visual_coverage, proof_architecture]
    mma_mode: M2
    mma_threshold: 8.0

  # Track 4: Polish
  - command: "/skeptic"
    skill: quality_skeptic_avatar
    track: T4
    brain: claude-sonnet

  - command: "/polish"
    skill: quality_hpe
    track: T4
    brain: claude-opus

  - command: "/resonance"
    skill: quality_nra
    track: T4
    brain: claude-sonnet

  # Cross-Track
  - command: "/audit"
    skill: quality_mma
    track: TX
    brain: claude-sonnet

# Multi-Brain Routing Rules
brain_selection:
  default: claude-opus
  rules:
    - condition: "task.requires_visual_design"
      brain: gemini-3.1
      reason: "Gemini excels at visual/design tasks"
    - condition: "task.requires_code_debug"
      brain: codex-5.3
      reason: "Codex excels at code analysis and refinement"
    - condition: "task.complexity == 'simple' AND task.type == 'validation'"
      brain: claude-sonnet
      reason: "Sonnet sufficient for validation, saves Opus tokens"
    - condition: "task.complexity == 'complex' AND task.type in ['strategy', 'writing']"
      brain: claude-opus
      reason: "Opus required for nuanced strategy and long-form writing"
```

### Minimal Thread State Object (JSON)

```json
{
  "$schema": "schemas/thread/thread_state.schema.json",
  "thread_id": "THR-2026-0228-001",
  "project_id": "PRJ-2026-0228-001",
  "created_at": "2026-02-28T10:00:00Z",
  "updated_at": "2026-02-28T14:30:00Z",

  "current_track": "T2",
  "current_phase": "draft",
  "active_skill": "copy_lfva",
  "active_brain": "claude-opus",

  "track_history": [
    {
      "track": "T1",
      "started": "2026-02-28T10:00:00Z",
      "completed": "2026-02-28T11:30:00Z",
      "skills_used": ["research_market_scout", "research_mis"],
      "gate_status": "PASSED",
      "gate_approver": "human:chris"
    }
  ],

  "ssot_versions": {
    "PROJECT_BRIEF": "PB-2026-001-v2.1",
    "MESSAGE_SPINE": "MS-2026-001-v2.2",
    "EVIDENCE_PACK": "EP-2026-001-v1.1",
    "VOICE_GUIDE": "VG-2026-001-v2.1",
    "ANGLE_SET": null,
    "SKILL_ACTIVATION": null
  },

  "mma_scores": {
    "T2_draft": {
      "mode": "M1",
      "score": 7.4,
      "verdict": "PASS",
      "timestamp": "2026-02-28T13:00:00Z"
    }
  },

  "learned_constraints": [],

  "flags": {
    "human_override_used": false,
    "circuit_breaker_triggered": false,
    "fix_loop_count": 0
  }
}
```

### Standard Handoff Packet Between Phases

```json
{
  "$schema": "schemas/thread/handoff_packet.schema.json",
  "handoff_id": "HO-T1-T2-001",
  "from_track": "T1",
  "to_track": "T2",
  "timestamp": "2026-02-28T11:30:00Z",

  "gate_status": "PASSED",
  "gate_approver": "human:chris",
  "gate_notes": "Research complete. Proceed with documentary-style VSL.",

  "ssot_payload": {
    "PROJECT_BRIEF": {
      "version": "PB-2026-001-v2.1",
      "checksum": "sha256:abc123...",
      "location": "ssots/project_brief.yaml"
    },
    "MESSAGE_SPINE": {
      "version": "MS-2026-001-v2.2",
      "checksum": "sha256:def456...",
      "location": "ssots/message_spine.yaml"
    },
    "EVIDENCE_PACK": {
      "version": "EP-2026-001-v1.1",
      "checksum": "sha256:ghi789...",
      "location": "ssots/evidence_pack.yaml"
    }
  },

  "recommended_skill": "copy_lfva",
  "recommended_config": {
    "style": "S1_documentary_investigative",
    "bridge_pattern": "blind_solution",
    "target_length_minutes": 16,
    "market_sophistication": 4
  },

  "context_for_next_track": "Market sophistication level 4. Audience has seen multiple offers. Documentary/investigative style recommended to bypass skepticism. Key differentiator: proprietary mechanism (UMP) not yet seen in market."
}
```

---

## 7. DELIVERABLE 5 — MEMORY/LEARNING/REPAIR ROADMAP

### V1: Deterministic Memory Files + Manual Review Loops (Weeks 1–4)

**What ships:** The Memento file stack, consumed by Claude Code.

| File | Purpose | Update Frequency | Consumed By |
|------|---------|-----------------|-------------|
| `CLAUDE.md` | Core persistent memory — always loaded by Claude Code at session start | Every session | Claude Code (automatic) |
| `Context.md` | Current project/session context — loaded per project | Per project | Manual load |
| `Memory.md` | Long-term learned facts, preferences, patterns | Weekly review | Manual load |
| `Insights.md` | Meta-learnings, discovered heuristics, cross-project patterns | After each project | Manual load |
| `Soul.md` | Constitutional values, voice identity, philosophical grounding | Rarely (identity-level) | Loaded at project start |
| `Review.md` | Self-assessment logs, MMA score trends, skill performance data | After each production run | Manual review |

**How it's consumed in Claude Code:**
1. `CLAUDE.md` is auto-loaded (Claude Code reads it from repo root at session start)
2. Other files are referenced via `@memory/Insights.md` or loaded into conversation context
3. After each production run, the agent writes a review entry to `Review.md`
4. Human reviews `Review.md` weekly and promotes durable insights to `Memory.md` or `Insights.md`

**Validator:** `CLAUDE.md` exists in repo root. All 6 memory files present in `/memory/`.
**Evidence of success:** Claude Code loads `CLAUDE.md` automatically on session start. Human confirms context carries across sessions.

### V2: Semantic Index + Retrieval Policies (Weeks 5–12)

**What ships:** Vector search over memory + atoms, with retrieval policies.

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Vector Store** | Zilliz Cloud (Milvus) | Embed and index all atoms, memory entries, learned constraints |
| **Embedding Model** | Claude embeddings or `text-embedding-3-large` | Generate vectors for semantic search |
| **Retrieval Policy Engine** | Python + Pydantic | Rules for when to search, what to surface, how to rank |
| **Convex State Sync** | Convex Cloud | Real-time sync of `Context.md` and `Insights.md` across sessions |

**Retrieval policies:**
```yaml
policies:
  - trigger: "skill_activation"
    action: "Search atoms by skill's AtomManifest, surface any updated versions"
    priority: high

  - trigger: "error_encountered"
    action: "Search LearnedConstraints for matching failure pattern"
    priority: critical

  - trigger: "new_project_start"
    action: "Search Insights.md for patterns from similar project types"
    priority: medium

  - trigger: "mma_score_below_threshold"
    action: "Search Review.md for past fixes to similar dimension failures"
    priority: high
```

**Validator:** Semantic search returns relevant results for 10 test queries (precision > 0.7).
**Evidence of success:** Agent surfaces a relevant learned constraint when encountering a known failure mode, without human prompting.

### V3: Self-Repair + Patch Proposals + Automated Regression (Weeks 13–24)

**What ships:** Skills that diagnose their own failures and propose patches.

| Capability | Mechanism | Safety Gate |
|-----------|-----------|-------------|
| **Self-Diagnosis** | When MMA score drops below threshold, agent queries LearnedConstraints graph for root cause | Automated |
| **Patch Proposal** | Agent generates a diff-format patch to the skill file addressing the diagnosed issue | Human review required |
| **Regression Suite** | Golden traces run automatically after any skill patch to ensure no regression | Automated (CI) |
| **Constraint Learning** | New failure modes automatically added to skill's `<LearnedConstraints>` section | Automated with human review |

**Self-repair loop:**
```
MMA FAIL → Diagnose (query constraints graph)
         → Identify root cause (missing atom? drift? new failure mode?)
         → Generate patch proposal (XML diff)
         → Run regression tests against golden traces
         → IF tests pass → Present patch to human for approval
         → IF human approves → Apply patch, increment PATCH version
         → Update LearnedConstraints with new entry
         → Log to Review.md
```

**Neo4j graph structure for self-repair:**
```
(Skill:copy_lfva) --HAS_CONSTRAINT--> (Constraint:minute_8_cliff)
(Constraint:minute_8_cliff) --PREVENTS--> (Failure:viewer_dropout)
(Constraint:minute_8_cliff) --DISCOVERED_BY--> (Run:THR-2026-0315-003)
(Constraint:minute_8_cliff) --RESOLUTION--> (Patch:add_retention_hook_at_7m30s)
```

**Validator:** After 10 production runs, at least 2 new learned constraints are auto-generated and validated by human review.
**Evidence of success:** A skill that failed in run N succeeds in run N+1 due to an auto-applied (human-approved) patch.

---

## 8. NEXT ACTIONS (Checklist in Execution Order)

### Phase 0: Repo Setup (Day 1)
- [ ] Create new GitHub repo with the structure from Deliverable 2
- [ ] Add `CLAUDE.md` to repo root with core project context
- [ ] Add `README.md` with architecture overview
- [ ] Add `skills/_schema/SKILL_TEMPLATE_V2.xml` and `.xsd` validator
- [ ] Add `schemas/ssot/` with all SSOT schemas
- [ ] Add `/memory/` directory with all 6 Memento files (initial templates)
- [ ] Add `/tools/lint_skill.py` (basic XML schema validation)
- [ ] Commit and verify Claude Code auto-loads `CLAUDE.md`

### Phase 1: Batch 1 Skill Migration (Week 1)
- [ ] Run classification step on all 50 skills (produce CSV)
- [ ] Migrate LFVA v3.0 → normalize to schema, add test harness
- [ ] Migrate SFVW v3.0 → normalize to schema, add test harness
- [ ] Migrate MMA v1.0 → normalize to schema, add test harness
- [ ] Migrate ZPWO v3.0 → upgrade to v4.0 (4-track model)
- [ ] Verify lint passes on all 4 skills
- [ ] Create first golden trace (VSL production run example)

### Phase 2: Strategic Layer + Remaining Copy (Week 2)
- [ ] Build Copy Director v1.0 (routing logic + parameter assignment)
- [ ] Migrate Copy Lead → normalize
- [ ] Migrate SPC, ACM, ECG, MWP, CSA, VTD → normalize
- [ ] Update ZPWO v4.0 routing table with all new skill references
- [ ] Update SUB_AGENT_CONFIGS to v3.0

### Phase 3: Quality Layer (Week 3)
- [ ] Migrate HPE, NRA → normalize
- [ ] Build Skeptic Avatar v1.0 (from existing spec)
- [ ] Migrate VRA → normalize
- [ ] Create sales page golden trace example

### Phase 4: Research Layer (Week 4)
- [ ] Migrate Market Scout, Research Ops, MIS, Evidence Pack Builder → normalize
- [ ] SSOT template standardization (all 6 templates validated)
- [ ] End-to-end test: full 4-track run with normalized skills

### Phase 5: Remaining Skills (Weeks 5–6)
- [ ] Migrate all remaining skills (automation, system, experimental)
- [ ] `tools/atom_usage_audit.py` — identify duplicate atoms across skills
- [ ] Begin extracting shared atoms to `/atoms/` directory
- [ ] CI pipeline: lint + test on every PR

### Phase 6: Memory V2 (Weeks 7–12)
- [ ] Set up Zilliz Cloud vector store
- [ ] Build embedding pipeline for atoms + memory entries
- [ ] Implement retrieval policy engine
- [ ] Set up Convex state sync for Context.md
- [ ] Test semantic search with 10 validation queries

### Phase 7: Self-Repair V3 (Weeks 13–24)
- [ ] Set up Neo4j knowledge graph
- [ ] Migrate LearnedConstraints from all skills to graph nodes
- [ ] Build patch proposal generator
- [ ] Build regression runner (`tools/golden_trace_runner.py`)
- [ ] First self-repair cycle: diagnose → patch → test → human approve

---

*Refactor & Migration Plan v1.1*
*"Atoms are the universal interchange format. Skills are the assembly manuals. Tracks are the production line. Memory is the evolution engine."*
*Produced: 2026-02-28 by Opus 4.6*
