# 🎨 DESIGN FILES INTEGRATION GUIDE

> **Issue Reported:** Adding design files caused ULTRAMIND to close unexpectedly
> **Solution:** Safe integration protocol for design assets in Antigravity workspace

---

## 🚨 CRASH PREVENTION CHECKLIST

Before adding design files, ensure:

### **1. File Size Limits**
```
Individual file limits:
✅ < 10 MB per file (safe)
⚠️  10-50 MB (may cause slowdown)
❌ > 50 MB (likely to crash during indexing)

Total workspace limits:
✅ < 100 MB total design assets (safe)
⚠️  100-500 MB (configure exclusions)
❌ > 500 MB (must exclude from indexing)
```

### **2. Supported File Types**
```
Vector Graphics (Lightweight):
✅ .svg (always safe, text-based)
✅ .ai (check size < 10 MB)
✅ .sketch (check size)

Raster Graphics (Size-dependent):
✅ .png (if < 5 MB)
✅ .jpg/.jpeg (if < 5 MB)
⚠️  .psd (Photoshop files can be huge)
⚠️  .fig (Figma files can be large)

Design Exports (Usually safe):
✅ .pdf (exported designs, < 10 MB)
✅ .webp (optimized web graphics)
```

### **3. Workspace Indexing Configuration**

**CRITICAL:** Exclude large design assets from Antigravity indexing.

#### **Option A: Update .antigravity file**

Edit: `C:\Users\cfar7\Documents\ULTRAMIND\.antigravity`

Add this section:
```json
{
  "indexing": {
    "include": [
      "CLAUDE.md",
      ".claude/**/*.yaml",
      ".claude/**/*.json",
      ".claude/**/*.xml",
      "*.md",
      "docs/**/*",
      "ssot/**/*"
    ],
    "exclude": [
      "node_modules",
      ".git",
      "__pycache__",
      "*.pyc",
      ".DS_Store",
      "**/*.psd",
      "**/*.ai",
      "design-assets/**",
      "assets/raw/**"
    ]
  }
}
```

#### **Option B: Update .vscode/settings.json**

Edit: `C:\Users\cfar7\Documents\ULTRAMIND\.vscode\settings.json`

Add:
```json
{
  "files.watcherExclude": {
    "**/.git/objects/**": true,
    "**/.git/subtree-cache/**": true,
    "**/node_modules/*/**": true,
    "**/design-assets/**": true,
    "**/*.psd": true,
    "**/*.ai": true,
    "**/assets/raw/**": true
  },

  "search.exclude": {
    "**/node_modules": true,
    "**/bower_components": true,
    "**/*.code-search": true,
    "**/design-assets/**": true,
    "**/*.psd": true,
    "**/*.ai": true
  }
}
```

---

## 📁 RECOMMENDED DIRECTORY STRUCTURE

### **Safe Layout for Design Files:**

```
C:\Users\cfar7\Documents\ULTRAMIND\
├── CLAUDE.md                          ✅ Indexed
├── .claude/                           ✅ Indexed
│   ├── SKILLS_MANIFEST.yaml
│   ├── SESSION_STATE.json
│   └── ANTIGRAVITY_META.json
│
├── ssot/                              ✅ Indexed (text files)
│   ├── PROJECT_BRIEF.md
│   └── COPY_PLAN.md
│
├── design-assets/                     ❌ EXCLUDED from indexing
│   ├── raw/                           (Large source files)
│   │   ├── logo-source.ai
│   │   ├── mockup.psd
│   │   └── wireframes.fig
│   │
│   └── exports/                       (Optimized outputs)
│       ├── logo.svg                   (< 500 KB)
│       ├── hero-image.jpg             (< 2 MB)
│       └── icons/                     (< 100 KB each)
│
└── outputs/                           ✅ Indexed (generated content)
    ├── draft-advertorial.md
    └── sales-page.html
```

---

## 🔧 STEP-BY-STEP SAFE INTEGRATION

### **Phase 1: Prepare Workspace (DO THIS FIRST)**

1. **Update indexing exclusions** (choose one):
   ```bash
   # Option A: Edit .antigravity
   notepad "C:\Users\cfar7\Documents\ULTRAMIND\.antigravity"

   # Option B: Edit .vscode/settings.json
   notepad "C:\Users\cfar7\Documents\ULTRAMIND\.vscode\settings.json"
   ```

2. **Create design assets directory**:
   ```bash
   mkdir "C:\Users\cfar7\Documents\ULTRAMIND\design-assets"
   mkdir "C:\Users\cfar7\Documents\ULTRAMIND\design-assets\raw"
   mkdir "C:\Users\cfar7\Documents\ULTRAMIND\design-assets\exports"
   ```

3. **Close Antigravity IDE** completely.

---

### **Phase 2: Add Design Files Safely**

1. **Copy files to excluded directory**:
   ```bash
   # Move large source files to raw/
   cp /path/to/design-files/*.psd "C:\Users\cfar7\Documents\ULTRAMIND\design-assets\raw\"
   cp /path/to/design-files/*.ai "C:\Users\cfar7\Documents\ULTRAMIND\design-assets\raw\"

   # Move optimized exports to exports/
   cp /path/to/design-files/*.svg "C:\Users\cfar7\Documents\ULTRAMIND\design-assets\exports\"
   cp /path/to/design-files/*.png "C:\Users\cfar7\Documents\ULTRAMIND\design-assets\exports\"
   ```

2. **Verify file sizes**:
   ```bash
   # Check each file is under 10 MB
   du -sh "C:\Users\cfar7\Documents\ULTRAMIND\design-assets\raw\"*
   du -sh "C:\Users\cfar7\Documents\ULTRAMIND\design-assets\exports\"*
   ```

3. **Reopen Antigravity workspace**:
   ```
   File → Open Workspace
   → C:\Users\cfar7\Documents\ULTRAMIND\ULTRAMIND.code-workspace
   ```

4. **Monitor indexing**:
   - Watch status bar for indexing progress
   - Should NOT index design-assets/ folder
   - If indexing hangs, close Antigravity immediately

---

### **Phase 3: Verification**

Check that design files are accessible but not indexed:

1. **Files visible in explorer**: ✅ Yes
2. **Files appear in search**: ❌ No (excluded)
3. **Workspace loads quickly**: ✅ Yes
4. **No crash or freeze**: ✅ Yes

---

## 🚨 TROUBLESHOOTING

### **Issue: Antigravity still crashes when adding files**

**Solution 1: Use `.antigravityignore` file**

Create: `C:\Users\cfar7\Documents\ULTRAMIND\.antigravityignore`

Content:
```
# Exclude design assets from indexing
design-assets/
*.psd
*.ai
*.fig
*.sketch
assets/raw/
```

**Solution 2: Add files AFTER workspace is open**

1. Open workspace FIRST (empty or with code files only)
2. Wait for indexing to complete
3. THEN copy design files into excluded directory
4. Antigravity won't re-index excluded paths

**Solution 3: Disable auto-indexing temporarily**

```
Antigravity Settings:
→ Search: "indexing"
→ Disable "Auto Index Workspace"
→ Add design files
→ Re-enable after files are in place
```

---

### **Issue: Need to reference design files in SSOT**

**Solution: Use relative paths in markdown**

In `ssot/PROJECT_BRIEF.md`:
```markdown
## Visual Assets

Hero Image: `../design-assets/exports/hero.jpg`
Logo: `../design-assets/exports/logo.svg`

Design System:
- Colors defined in: `../design-assets/exports/color-palette.png`
- Typography: `../design-assets/exports/type-scale.svg`
```

Files are accessible via paths but not indexed by search.

---

### **Issue: Design files are essential for workflow**

**Solution: Keep lightweight reference versions**

```
ssot/
├── PROJECT_BRIEF.md              (core brief)
└── _assets/                      (lightweight refs)
    ├── logo-thumb.svg            (< 50 KB)
    ├── color-palette.png         (< 200 KB)
    └── style-guide.pdf           (< 500 KB)

design-assets/
└── raw/                          (excluded from indexing)
    ├── logo-full.ai              (15 MB - not indexed)
    ├── mockup-hires.psd          (45 MB - not indexed)
    └── design-system.fig         (20 MB - not indexed)
```

Lightweight thumbnails/references live in SSOT (indexed).
Full design sources live in excluded directory (accessible but not indexed).

---

## 📊 FILE SIZE AUDIT

Before adding design files, run audit:

```bash
# Check individual file sizes
find /path/to/design-files -type f -exec du -h {} + | sort -rh | head -20

# Check total size by file type
find /path/to/design-files -name "*.psd" -exec du -ch {} + | tail -1
find /path/to/design-files -name "*.ai" -exec du -ch {} + | tail -1
find /path/to/design-files -name "*.svg" -exec du -ch {} + | tail -1
```

**Decision Tree:**
```
File < 1 MB:        → Safe to add anywhere
File 1-10 MB:       → Add to design-assets/exports/ (excluded)
File 10-50 MB:      → Add to design-assets/raw/ (excluded)
File > 50 MB:       → Keep external, reference via path
```

---

## ✅ FINAL CHECKLIST

Before adding design files:

- [ ] Indexing exclusions configured (.antigravity or .vscode/settings.json)
- [ ] design-assets/ directory structure created
- [ ] design-assets/raw/ for large source files (> 10 MB)
- [ ] design-assets/exports/ for optimized outputs (< 10 MB)
- [ ] File size audit completed (all files < 50 MB individually)
- [ ] Antigravity closed before copying files
- [ ] Files copied to excluded directories
- [ ] Workspace reopened after files in place
- [ ] Indexing completes without hanging
- [ ] No crash or freeze during file operations

---

## 🎯 RECOMMENDED WORKFLOW

**For projects with design assets:**

1. **Create SSOT brief FIRST** (text-only, no images)
   ```
   /intake → PROJECT_BRIEF.md (no assets yet)
   ```

2. **Generate copy/content** (no visuals needed yet)
   ```
   /advertorial → draft-copy.md
   ```

3. **Add design files AFTER text is done**
   ```
   Copy design files to design-assets/exports/
   Reference in final HTML: <img src="../design-assets/exports/hero.jpg">
   ```

4. **Keep workspace lean**
   - SSOT: < 500 KB total (text files only)
   - Design assets: Excluded from indexing
   - Total workspace: < 100 MB for fast performance

---

*Design files integrated safely = No crashes, fast workspace, full access* 🎨

---

## 📞 IF CRASH PERSISTS

**Gather diagnostic info:**

1. Which files were you adding when it crashed?
   ```bash
   ls -lh /path/to/files/that/caused/crash
   ```

2. What was the total size?
   ```bash
   du -sh /path/to/files/that/caused/crash
   ```

3. Was Antigravity indexing when it crashed?
   - Check status bar for "Indexing workspace..." message

4. Error message or just closed?
   - Check Antigravity logs if available

**Then try:**
- Add files one at a time (smallest first)
- Disable indexing during file addition
- Use `.antigravityignore` file
- Keep design files external, reference by absolute path
