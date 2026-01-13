# 🚨 ULTRAMIND CRASH TROUBLESHOOTING

**Issue:** "When I load a design project files, Ultramind vanishes"

**Root Cause:** Large design files trigger Antigravity's file indexer, which can crash or freeze when processing binary files (PSD, AI, FIG, etc.)

---

## ✅ FIXES APPLIED

### **1. Sleep Energy Breakthrough Removed**
- `ssot/sleep_energy/` folder deleted from both Desktop and Documents
- SESSION_STATE.json reset to `project_id: null` (no longer obsessed with one project)
- System now ready for ANY project

### **2. Design File Crash Prevention Configured**

**Desktop location:** `C:\Users\cfar7\OneDrive\Desktop\ULTRAMIND\`

Files added:
- ✅ `.antigravity` - Excludes design files from indexing
- ✅ `.vscode/settings.json` - Prevents file watcher from monitoring large files
- ✅ `.project` - IDE descriptor for Antigravity
- ✅ `ULTRAMIND.code-workspace` - Workspace definition
- ✅ `design-assets/` directory - Safe location for design files

**Excluded from indexing:**
```
design-assets/**
**/*.psd
**/*.ai
**/*.fig
**/*.sketch
assets/raw/**
```

---

## 🎯 HOW TO ADD DESIGN FILES NOW

### **IMPORTANT: Use the design-assets directory**

Instead of dropping files anywhere in ULTRAMIND:

```bash
# 1. Copy design files to excluded directory
cp /path/to/mockup.psd "C:/Users/cfar7/OneDrive/Desktop/ULTRAMIND/design-assets/raw/"
cp /path/to/logo.ai "C:/Users/cfar7/OneDrive/Desktop/ULTRAMIND/design-assets/raw/"
cp /path/to/icon.svg "C:/Users/cfar7/OneDrive/Desktop/ULTRAMIND/design-assets/exports/"
```

Files will be:
- ✅ Accessible in file explorer
- ✅ NOT indexed by Antigravity
- ✅ Won't cause crashes

---

## 🔧 STEP-BY-STEP RECOVERY

If Antigravity crashes or "vanishes":

### **1. Close Antigravity completely**
```
Task Manager → Find Antigravity process → End Task
Or just close the window if it's frozen
```

### **2. Reopen workspace**
```
Option A: Double-click ULTRAMIND.code-workspace
Option B: File → Open Workspace → ULTRAMIND.code-workspace
```

### **3. Wait for indexing to complete**
- Check status bar for "Indexing workspace..." message
- DO NOT add files while indexing
- Wait until it shows "Ready" or similar

### **4. Add design files ONLY to design-assets/**
```bash
# Safe location - won't be indexed
cp /path/to/designs/* design-assets/raw/
```

---

## 🎨 WORKING WITH DESIGN PROJECTS

### **Before adding ANY design files:**

1. **Check file sizes**
   ```bash
   ls -lh /path/to/design/files
   ```
   - If any file > 50 MB, keep it external (don't copy to ULTRAMIND)
   - If 10-50 MB, put in `design-assets/raw/`
   - If < 10 MB, put in `design-assets/exports/`

2. **Copy to correct location**
   ```
   Large files (PSD, AI, FIG): design-assets/raw/
   Optimized (SVG, PNG, JPG): design-assets/exports/
   ```

3. **Reference from SSOT**
   ```markdown
   ## Design Assets

   Hero mockup: `../design-assets/raw/hero-mockup.psd`
   Logo: `../design-assets/exports/logo.svg`
   ```

---

## 📋 NEW PROJECT WORKFLOW

When starting a new design project:

### **1. Start with text FIRST (no designs yet)**
```
/intake
→ Creates ssot/{project-name}/PROJECT_BRIEF.yaml
→ No design files involved yet
```

### **2. Generate content (still no designs)**
```
/advertorial
→ Drafts copy angles
→ All text-based
```

### **3. THEN add design files**
```bash
# After text is done, add visuals
cp /path/to/designs/* design-assets/raw/
```

### **4. Reference in final output**
```html
<img src="../design-assets/exports/hero.jpg">
```

**Key:** Text first, designs last. This prevents crashes during intake/copy phases.

---

## ⚠️ WARNING SIGNS

If you see these, **STOP and close Antigravity**:

1. **Indexing stuck** - Status bar shows "Indexing..." for > 2 minutes
2. **High CPU usage** - Task Manager shows Antigravity using > 50% CPU continuously
3. **UI freezing** - Workspace stops responding to clicks
4. **Memory spike** - Antigravity using > 2 GB RAM

**Action:**
```
1. Close Antigravity immediately
2. Find the large file you just added
3. Move it to design-assets/raw/
4. Reopen workspace
```

---

## 🔍 DIAGNOSTIC COMMANDS

### **Check what's being indexed:**
```bash
# From ULTRAMIND directory
find . -type f -name "*.psd" -o -name "*.ai" -o -name "*.fig"
```

If this returns files OUTSIDE `design-assets/`, move them:
```bash
mv path/to/mockup.psd design-assets/raw/
```

### **Check workspace size:**
```bash
du -sh .
du -sh design-assets/
```

Target:
- Total workspace: < 100 MB (fast)
- design-assets/: Can be larger (excluded from indexing)

### **Verify exclusions are active:**
```bash
cat .antigravity | grep -A 10 exclude
cat .vscode/settings.json | grep -A 10 watcherExclude
```

Should show design file patterns excluded.

---

## 🚀 CLEAN STATE VERIFICATION

Your workspace is now in clean state:

✅ **Desktop:** `C:\Users\cfar7\OneDrive\Desktop\ULTRAMIND\`
- SESSION_STATE.json: `project_id: null` (no project locked in)
- ssot/sleep_energy/: REMOVED
- .antigravity: Design files excluded
- design-assets/: Ready for safe file storage

✅ **Documents (backup):** `C:\Users\cfar7\Documents\ULTRAMIND\`
- Same clean configuration
- Same crash prevention
- OneDrive-free (if you prefer local-only)

---

## 📖 REFERENCE GUIDES

- `DESIGN_FILES_GUIDE.md` - Comprehensive design file integration
- `WORKSPACE_ACTIVATION.md` - How to activate workspace in Antigravity
- `STARTUP_CHECKLIST.md` - Quick verification checklist

---

## 🎯 RECOMMENDED WORKFLOW

**For any new project:**

1. ✅ Open ULTRAMIND workspace (via `.code-workspace` file)
2. ✅ Wait for indexing to complete
3. ✅ Run `/intake` to start project (creates SSOT)
4. ✅ Generate copy/content (all text-based)
5. ✅ THEN add design files to `design-assets/`
6. ✅ Reference designs in final HTML/output

**Never:**
- ❌ Add design files before text is done
- ❌ Drop large files directly into ssot/ or root
- ❌ Add files while Antigravity is indexing
- ❌ Ignore high CPU/memory warnings

---

*Clean slate restored. Design crash prevention active. Ready for new projects.* 🚀
