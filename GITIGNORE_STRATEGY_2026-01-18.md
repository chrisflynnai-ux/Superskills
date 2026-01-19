# .gitignore Strategy for ULTRAMIND System Development

**Date:** 2026-01-18
**Purpose:** Exclude temporary project files, keep system development work

---

## EXCLUSION PHILOSOPHY

**Core Principle:** Backup system development work (skills, frameworks, docs), NOT dynamic client project files.

**What Gets Backed Up:**
- `.claude/skills/` - All skill XML files (the system itself)
- `docs/` - Architecture, constitution, handoffs
- `skills manifest/` - Skill inventory and tracking
- `ssot/` - SSOT schema templates
- `tools/` - Python validation tools
- Root-level system docs (CLAUDE.md, README.md, ARCHITECTURE_*.md, etc.)
- System development outputs (FRAMEWORK_*.md, BUILD_LOG_*.md, SPDC_*.md)

**What Gets Excluded:**
- `tmpclaude-*` files (16+ temporary Claude Code session files)
- `assets/` - Temporary images/media for client projects
- `specs/` - Client project specifications (PDFs, PPTs, sales decks)
- `outputs/deconstruction_reports/` - Specific sales page analyses
- `outputs/test_simulation/` - Test runs
- All image files (*.png, *.jpg, etc.) EXCEPT docs/

---

## CHANGES MADE TO .gitignore

### 1. Enhanced tmpclaude Exclusion
```gitignore
# Claude Code temporary files (16+ tmp files from sessions)
tmpclaude-*
tmpclaude*.cwd
```

**Before:** `tmpclaude-*` (line 76)
**After:** Added explicit `.cwd` pattern for clarity
**Impact:** Excludes all 16 tmpclaude files found in root

---

### 2. Dynamic Project Directories
```gitignore
# Assets directory - temporary images/media for projects
assets/
!assets/.gitkeep

# Specs directory - client project specifications (PDFs, PPTs, etc.)
specs/
!specs/.gitkeep
```

**Rationale:**
- `assets/` contains 24 temporary PNG images (~43MB) from design work
- `specs/` contains client sales decks (QRX NEW SALES DECK 20.pdf/pptx ~38MB)
- These are dynamic, project-specific, and should NOT be version controlled
- `.gitkeep` files ensure empty directories remain in repo structure

---

### 3. Selective Outputs Exclusion
```gitignore
# Outputs directory structure - keep framework/docs, exclude project outputs
outputs/deconstruction_reports/
outputs/test_simulation/

# Keep system development outputs like framework guides, build logs
!outputs/FRAMEWORK_*.md
!outputs/BUILD_LOG_*.md
!outputs/SPDC_*.md
```

**Rationale:**
- `outputs/` contains BOTH system dev work AND project-specific outputs
- **KEEP:** Framework guides, build logs, skill upgrade summaries (system development)
- **EXCLUDE:** Deconstruction reports for specific sales pages (client work)

---

### 4. Image File Blanket Exclusion (with Exception)
```gitignore
# Image files (temporary project assets)
*.png
*.jpg
*.jpeg
*.gif
*.webp

# Exception: Keep system architecture diagrams if needed
!docs/**/*.png
!docs/**/*.jpg
```

**Rationale:**
- 24 temporary PNG files in `assets/` are project work (sales page screenshots, design mockups)
- These should NOT be backed up
- **Exception:** If architecture diagrams are added to `docs/`, they WILL be kept

---

## CURRENT FILE INVENTORY

### Excluded by New Rules:

**tmpclaude files (16 files, ~500 bytes each):**
```
tmpclaude-8785-cwd
tmpclaude-74d5-cwd
tmpclaude-3194-cwd
tmpclaude-12d4-cwd
tmpclaude-2521-cwd
tmpclaude-13b3-cwd
tmpclaude-2631-cwd
tmpclaude-8ab0-cwd
tmpclaude-f55e-cwd
tmpclaude-e7ee-cwd
tmpclaude-b08e-cwd
tmpclaude-87fc-cwd
tmpclaude-7a53-cwd
tmpclaude-fff3-cwd
tmpclaude-5b45-cwd
tmpclaude-454b-cwd
```

**assets/ (24 PNG files, ~43MB total):**
- image_14b1943e-e426-4b24-8333-8d65fde6780a.png
- image_1bb59120-5e15-45ed-8bc7-dbe751e1eaae.png
- ... (22 more)
- Miising image number 24 of 23.png

**specs/ (2 files, ~38MB total):**
- QRX NEW SALES DECK 20.pdf (2.4MB)
- QRX NEW SALES DECK 20.pptx (36MB)

**outputs/deconstruction_reports/ (subdirectory with sales page analyses)**
**outputs/test_simulation/ (subdirectory with test runs)**

---

### Included (System Development Work):

**Root-level system docs:**
- CLAUDE.md (control plane instructions)
- README.md (project overview)
- ULTRAMIND_AGENTIC_OS_INTEGRATION_PLAN.md ✅ (user's vision doc)
- ARCHITECTURE_*.md (system design docs)
- ANTIGRAVITY_*.md (Google AI integration docs)
- *.md files (all system documentation)

**.claude/ directory (entire skill library):**
- .claude/skills/ (all XML skill files)
- .claude/settings.local.json (modified, will be committed)

**outputs/ (selective):**
- ✅ FRAMEWORK_GATHERING_GUIDE_2026-01-15.md
- ✅ BUILD_LOG_VSL_ANALYZER_2026-01-15.md
- ✅ SPDC_V2.1_UPGRADE_SUMMARY.md (if created in outputs/)
- ❌ outputs/deconstruction_reports/
- ❌ outputs/test_simulation/

**skills manifest/, docs/, ssot/, tools/, web/** (all included)

---

## VERIFICATION COMMANDS

After committing with new .gitignore, verify exclusions:

```bash
# Check what will be committed
git status

# Should NOT see:
# - tmpclaude-* files
# - assets/*.png
# - specs/*.pdf or specs/*.pptx
# - outputs/deconstruction_reports/
# - outputs/test_simulation/

# Should see (if modified):
# - .gitignore (the updated file itself)
# - .claude/skills/*.xml
# - outputs/FRAMEWORK_*.md
# - outputs/BUILD_LOG_*.md
# - All root-level .md files
```

---

## CLEANUP RECOMMENDATION

Before first commit with new .gitignore, remove tracked files that should now be ignored:

```bash
# Remove tmpclaude files from repo (if they were previously committed)
git rm --cached tmpclaude-*

# Remove assets from repo (if previously committed)
git rm --cached -r assets/

# Remove specs from repo (if previously committed)
git rm --cached -r specs/

# Remove specific outputs subdirectories (if previously committed)
git rm --cached -r outputs/deconstruction_reports/
git rm --cached -r outputs/test_simulation/

# Commit the cleanup
git add .gitignore
git commit -m "Update .gitignore: exclude dynamic project files, keep system development

- Exclude 16+ tmpclaude session files
- Exclude assets/ (temporary project images)
- Exclude specs/ (client project specifications)
- Exclude outputs/deconstruction_reports/ and test_simulation/
- Keep all system development work (skills, docs, frameworks)
- Keep selective outputs (FRAMEWORK_*.md, BUILD_LOG_*.md, SPDC_*.md)"
```

---

## LONG-TERM MAINTENANCE

### When to Add New Exclusions:

1. **New client projects create temp directories** → Add to .gitignore
2. **New asset types accumulate** → Add pattern (e.g., `*.mp4` for video)
3. **New output categories emerge** → Add selective exclusion rules

### When to Include Files:

1. **New skill built** → Automatically included (in .claude/skills/)
2. **New framework guide** → Automatically included (FRAMEWORK_*.md pattern)
3. **New architecture doc** → Automatically included (docs/ or root .md files)

### Quick Test:

```bash
# Before committing, always check git status
git status

# Ask: "Would I want this file in the repo 6 months from now?"
# - Yes → Make sure it's NOT in .gitignore
# - No → Make sure it IS in .gitignore
```

---

## ULTRAMIND_AGENTIC_OS_INTEGRATION_PLAN.md

**Location:** `C:\Users\cfar7\Desktop\ULTRAMIND\ULTRAMIND_AGENTIC_OS_INTEGRATION_PLAN.md`
**Status:** ✅ CONFIRMED - This file is in the root directory and will be included in backups
**Purpose:** Long-term vision document for Antigravity/Google AI integration

This file is correctly positioned. It's a root-level .md file, so it will be tracked by git and backed up with all system development work.

---

**Next Steps:**
1. Review this strategy
2. Run `git status` to see current state
3. Run cleanup commands if tmpclaude/assets/specs were previously committed
4. Commit .gitignore changes
5. Future commits will automatically exclude dynamic project files

---

**Status:** ✅ .gitignore updated and documented
**Impact:** ~81MB of temporary files excluded, system development work preserved
