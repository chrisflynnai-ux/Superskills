# SSOT TEMPLATES — Single Source of Truth Objects
## ULTRAMIND Claude Code Foundation

**Version:** 1.0  
**Date:** January 2026  
**Purpose:** Foundational templates for copy consistency and quality

---

## WHAT ARE SSOT OBJECTS?

SSOT = Single Source of Truth

These are **locked documents** that all copy assets reference. They ensure:

- **Consistency** — Same mechanism language everywhere
- **Alignment** — All assets tell the same story
- **Quality** — MMA validates against these contracts
- **Speed** — No reinventing the wheel each asset

---

## THE FIVE CORE TEMPLATES

| Template | Version | Purpose | Required? |
|----------|---------|---------|-----------|
| `PROJECT_BRIEF_template.yaml` | v2.0 | Goal, avatar, offer, constraints, CTA | ✅ Yes |
| `MESSAGE_SPINE_template.yaml` | v2.1 | Promise, mechanism, proof, objections | ✅ Yes |
| `EVIDENCE_PACK_template.yaml` | v1.0 | Claims grounding, proof discipline | 🟡 Recommended |
| `VOICE_GUIDE_template.yaml` | v2.0 | Tone, vocabulary, style patterns | 🟡 Recommended |
| `OFFER_ARCHITECTURE_template.yaml` | v2.0 | Value Equation, pricing, bonuses | 🟡 For sales |

---

## HOW TO USE

### 1. Create Project Folder

```
/ssot/
  /sleep_energy_breakthrough/
    ├── PROJECT_BRIEF.yaml
    ├── MESSAGE_SPINE.yaml
    ├── EVIDENCE_PACK.yaml
    ├── VOICE_GUIDE.yaml
    └── OFFER_ARCHITECTURE.yaml
```

### 2. Copy Templates

```bash
cp ssot_templates/PROJECT_BRIEF_template.yaml ssot/[project]/PROJECT_BRIEF.yaml
cp ssot_templates/MESSAGE_SPINE_template.yaml ssot/[project]/MESSAGE_SPINE.yaml
# etc.
```

### 3. Fill In & Lock

1. Complete all required fields
2. Run validation checklist at bottom of each template
3. Change status to "locked"
4. Generate checksum for MESSAGE_SPINE (mechanism paragraph)

### 4. Reference in Skills

All copy skills read from locked SSOT objects:

```yaml
context:
  required:
    - PROJECT_BRIEF
    - MESSAGE_SPINE
  optional:
    - EVIDENCE_PACK
    - VOICE_GUIDE
```

---

## DEPENDENCY CHAIN

```
PROJECT_BRIEF (created first)
      │
      ▼
MESSAGE_SPINE (references avatar, offer from PROJECT_BRIEF)
      │
      ├──► EVIDENCE_PACK (maps claims from MESSAGE_SPINE)
      │
      └──► OFFER_ARCHITECTURE (structures offer from PROJECT_BRIEF)
      
VOICE_GUIDE (can be created independently)
```

---

## MMA VALIDATION

MMA checks copy against SSOT objects:

| MMA Dimension | SSOT Reference |
|---------------|----------------|
| Strategy Alignment | MESSAGE_SPINE (promise, mechanism) |
| Voice Consistency | VOICE_GUIDE (tone, vocabulary) |
| Proof Discipline | EVIDENCE_PACK (claims grounding) |
| CTA Integrity | PROJECT_BRIEF (single CTA rule) |

**If copy drifts from SSOT → MMA fails that dimension**

---

## LOCK PROTOCOL

### When to Lock

- **PROJECT_BRIEF:** After stakeholder approval
- **MESSAGE_SPINE:** After mechanism tested/validated
- **EVIDENCE_PACK:** After all claims verified
- **VOICE_GUIDE:** After voice samples confirmed
- **OFFER_ARCHITECTURE:** After pricing approved

### Lock Means

- No changes without version increment
- All downstream assets reference this version
- Checksum validates no tampering

### To Update Locked SSOT

1. Create new version (v1.1, v2.0, etc.)
2. Document what changed
3. Re-lock
4. Update all affected assets
5. Re-validate with MMA

---

## QUICK START

**Minimum viable SSOT for any project:**

1. `PROJECT_BRIEF.yaml` — Who, what, why
2. `MESSAGE_SPINE.yaml` — Promise + mechanism

**Add for production quality:**

3. `EVIDENCE_PACK.yaml` — Proof discipline
4. `VOICE_GUIDE.yaml` — Consistency

**Add for sales assets:**

5. `OFFER_ARCHITECTURE.yaml` — Value equation

---

## FILE NAMING

```
SSOT files:     [OBJECT_NAME].yaml (uppercase)
Templates:      [OBJECT_NAME]_template.yaml
Locked:         [OBJECT_NAME]_v[X.Y].yaml (versioned)
```

---

## GUARDRAILS

### Non-Negotiables in SSOT

- **No fabricated evidence** — All EVIDENCE_PACK entries must be real
- **No fake urgency** — All deadlines in OFFER_ARCHITECTURE must be TRUE
- **Mechanism consistency** — MESSAGE_SPINE.canonical_paragraph is verbatim everywhere
- **Single CTA** — PROJECT_BRIEF.cta.primary_action is THE action

### If Violated

- MMA will flag
- Copy cannot ship
- Fix SSOT or fix copy to match

---

*SSOT Templates v1.0 — The foundation for copy consistency*

*"State > Chat" — These objects ARE the memory*
