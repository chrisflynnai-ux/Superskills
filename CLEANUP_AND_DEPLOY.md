# ULTRAMIND CLEANUP & DEPLOYMENT SCRIPT

> **Date:** 2026-01-12
> **Purpose:** Final cleanup and Antigravity-ready deployment
> **Status:** Ready to execute

---

## CURRENT STATE ANALYSIS

### Files Found:
```
✅ .claude/CLAUDE.md/CLAUDE_v3.md          (New control plane - in subdirectory)
✅ .claude/SKILLS_MANIFEST.yaml            (New manifest - correct location)
✅ .claude/skills/meta/zpwo_v3_MICRO.xml   (New ZPWO - correct location)

❓ .claude/CLAUDE.md/                      (Directory, should be file)
📁 skills manifest/SKILLS_MANIFEST_v2.1.yaml (Old location - keep as reference)
```

---

## ISSUES TO RESOLVE

### 1. CLAUDE.md Structure Problem
**Current:** `.claude/CLAUDE.md/` is a **directory** containing `CLAUDE_v3.md`
**Should Be:** `.claude/CLAUDE.md` as a **file** (not directory)

**Why:** Claude Code looks for `.claude/CLAUDE.md` as a file, not a subdirectory

---

### 2. Skills Manifest Duplication
**Current:**
- `.claude/SKILLS_MANIFEST.yaml` (New, lightweight, Antigravity-ready)
- `skills manifest/SKILLS_MANIFEST_v2.1.yaml` (Old, detailed inventory)

**Decision Needed:** Keep both or consolidate?

---

## RECOMMENDED CLEANUP STEPS

### STEP 1: Backup Original Files

```bash
# Create backup directory
mkdir -p .archive/v2_backup_2026-01-12

# Backup original CLAUDE.md directory
cp -r .claude/CLAUDE.md .archive/v2_backup_2026-01-12/CLAUDE.md_original

# Backup old manifest (if consolidating)
cp "skills manifest/SKILLS_MANIFEST_v2.1.yaml" .archive/v2_backup_2026-01-12/
```

---

### STEP 2: Deploy New CLAUDE.md

```bash
# Remove old CLAUDE.md directory structure
rm -rf .claude/CLAUDE.md

# Move CLAUDE_v3.md to proper location as file
cp CLAUDE_v3.md .claude/CLAUDE.md

# Verify
ls -lh .claude/CLAUDE.md
# Should show: -rw-r--r-- ... CLAUDE.md (file, not directory)
```

---

### STEP 3: Consolidate Skills Manifests (OPTION A - Recommended)

**Keep both for different purposes:**

```bash
# .claude/SKILLS_MANIFEST.yaml = Runtime index (lightweight, always loaded)
# Keep as-is (169 lines, ~500 tokens)

# skills manifest/SKILLS_MANIFEST_v2.1.yaml = Reference documentation (detailed)
# Keep in skills manifest/ directory for human reference
```

**Rationale:**
- `.claude/SKILLS_MANIFEST.yaml` → Agent uses this (lean, Antigravity-ready)
- `skills manifest/SKILLS_MANIFEST_v2.1.yaml` → Humans reference this (detailed inventory)

---

### STEP 3: Consolidate Skills Manifests (OPTION B - Single Source)

**Merge into one Antigravity-ready manifest:**

```bash
# Create enhanced Antigravity-ready manifest
# Combine lightweight structure with detailed metadata
# Output to: .claude/SKILLS_MANIFEST_ANTIGRAVITY_v3.yaml

# Archive old manifests
mv .claude/SKILLS_MANIFEST.yaml .archive/v2_backup_2026-01-12/
mv "skills manifest/SKILLS_MANIFEST_v2.1.yaml" .archive/v2_backup_2026-01-12/
```

---

### STEP 4: Verify ZPWO Deployment

```bash
# Check that new ZPWO is in place
ls -lh .claude/skills/meta/zpwo_v3_MICRO.xml

# Should show: zpwo_v3_MICRO.xml (~21KB, 542 lines)

# Verify old ZPWO is removed/archived
ls -lh .claude/skills/meta/zpwo_v1_0_0_updated.xml
# Should show: No such file (if you removed it)
```

---

## ANTIGRAVITY-READY REQUIREMENTS

Based on your mention of "Antigravity-ready manifest," here's what that likely means:

### Key Features for Antigravity IDE Integration:

1. **Structured Metadata** ✅
   - YAML format (machine-readable)
   - Clear skill taxonomy
   - Load cost indicators
   - Axis alignments (6D + center)

2. **Visual Mapping Support** ✅
   - Neuro Box coordinates for each skill
   - Routing table (command → skill)
   - Dependency graph data

3. **Progressive Disclosure Markers** ✅
   - L1-L4 layer indicators
   - Token budget targets
   - Load rules

4. **Real-time State Integration** 🔄
   - SESSION_STATE.json compatibility
   - SSOT object references
   - Context usage tracking

---

## PROPOSED ANTIGRAVITY-READY MANIFEST ENHANCEMENTS

If you want to "revamp" the manifest for Antigravity, add these sections:

### Additional Metadata for Visual IDE:

```yaml
# Add to SKILLS_MANIFEST.yaml

visual_mapping:
  neuro_box_coordinates:
    zpwo:
      position: "CENTER"
      dimension: 7
      color: "#FFFFFF"

    advertorial_master:
      position: "X_AXIS"
      dimensions: [MIND, SPIRIT]
      color: "#4A90E2"

    market_intel:
      position: "PSYCH"
      dimension: "BACK"
      color: "#7B68EE"

dependency_graph:
  zpwo:
    depends_on: []
    consumed_by: [advertorial_master, sales_page_lite, email_genius]

  advertorial_master:
    depends_on: [market_intel, zpwo]
    consumed_by: [sales_page_lite]

realtime_integration:
  session_state_path: "ssot/{project_id}/SESSION_STATE.json"
  context_monitor: "enabled"
  auto_gc_threshold: 70
```

---

## FINAL DIRECTORY STRUCTURE (After Cleanup)

```
ULTRAMIND/
├── .claude/
│   ├── CLAUDE.md                          ← FILE (not directory) ✅
│   ├── SKILLS_MANIFEST.yaml               ← Runtime index ✅
│   ├── settings.local.json
│   ├── skills/
│   │   ├── meta/
│   │   │   ├── zpwo_v3_MICRO.xml         ← New ZPWO ✅
│   │   │   ├── skill_builder_v1.2.0.xml
│   │   │   └── ...
│   │   ├── copy/
│   │   │   ├── advertorial_copy_master_v2.0.0.xml
│   │   │   └── ...
│   │   └── ...
│   └── schemas/
│       └── SSOT_SCHEMAS_v2_2.yaml
│
├── skills manifest/
│   └── SKILLS_MANIFEST_v2.1.yaml          ← Reference doc (detailed)
│
├── .archive/
│   └── v2_backup_2026-01-12/
│       ├── CLAUDE.md_original/            ← Backup
│       └── ...
│
└── [New files created]
    ├── CLAUDE_v3.md                       ← Source (can delete after deployed)
    ├── SWITCHOVER_GUIDE.md
    ├── ARCHITECTURE_COMPARISON.md
    └── ...
```

---

## EXECUTION COMMANDS

### Quick Deploy (All-in-One)

```bash
# Navigate to ULTRAMIND directory
cd /c/Users/cfar7/OneDrive/Desktop/ULTRAMIND

# Create backup
mkdir -p .archive/v2_backup_2026-01-12
cp -r .claude/CLAUDE.md .archive/v2_backup_2026-01-12/CLAUDE.md_original

# Deploy new CLAUDE.md
rm -rf .claude/CLAUDE.md
cp CLAUDE_v3.md .claude/CLAUDE.md

# Verify
echo "=== VERIFICATION ==="
echo "CLAUDE.md is now:"
ls -lh .claude/CLAUDE.md

echo ""
echo "SKILLS_MANIFEST.yaml:"
ls -lh .claude/SKILLS_MANIFEST.yaml

echo ""
echo "ZPWO v3 MICRO:"
ls -lh .claude/skills/meta/zpwo_v3_MICRO.xml

echo ""
echo "✅ Deployment complete!"
```

---

## VERIFICATION CHECKLIST

After running cleanup:

- [ ] `.claude/CLAUDE.md` is a **file** (not directory)
- [ ] `.claude/CLAUDE.md` contains ULTRAMIND AGENTIC CONTROL PLANE v3.0.0
- [ ] `.claude/SKILLS_MANIFEST.yaml` exists and is ~169 lines
- [ ] `.claude/skills/meta/zpwo_v3_MICRO.xml` exists and is ~542 lines
- [ ] Original files backed up in `.archive/v2_backup_2026-01-12/`
- [ ] `skills manifest/SKILLS_MANIFEST_v2.1.yaml` preserved (reference doc)

---

## NEXT STEPS AFTER CLEANUP

1. **Test the deployment:**
   ```
   Start new conversation
   Agent should load CLAUDE.md v3.0.0
   Check baseline context (should be ~2.5K tokens)
   ```

2. **Verify routing:**
   ```
   User: "/status"
   Agent: Should display ZPWO status report
   ```

3. **Test skill loading:**
   ```
   User: "Create an advertorial"
   Agent: Should route to advertorial_master
   Context should jump to ~3.1K tokens (L1 loaded)
   ```

4. **Decide on Antigravity enhancements:**
   - Do you want visual_mapping additions?
   - Do you want dependency_graph metadata?
   - Should we merge both manifests into one Antigravity-optimized version?

---

## QUESTIONS FOR YOU

Before I execute cleanup:

1. **CLAUDE.md deployment:** Ready to replace directory with file?
   - ✅ Yes, proceed
   - ⏸️ No, wait

2. **Skills Manifest strategy:**
   - Option A: Keep both (lightweight + detailed) ✅ Recommended
   - Option B: Merge into single Antigravity-optimized manifest
   - Option C: Other approach?

3. **Antigravity enhancements needed:**
   - Add visual_mapping metadata? (for IDE visualization)
   - Add dependency_graph? (for skill relationship mapping)
   - Add real-time state hooks? (for context monitoring)

---

*Ready for cleanup on your command.*
