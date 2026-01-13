# Design Assets Directory

**Purpose:** Store design files separate from indexed workspace files to prevent crashes.

## Structure

```
design-assets/
├── raw/                  (Large source files > 10 MB)
│   ├── *.psd            (Photoshop)
│   ├── *.ai             (Illustrator)
│   ├── *.fig            (Figma)
│   └── *.sketch         (Sketch)
│
└── exports/             (Optimized outputs < 10 MB)
    ├── *.svg            (Vector graphics)
    ├── *.png            (Raster images)
    ├── *.jpg            (Photos)
    └── icons/           (Icon sets)
```

## Important Notes

⚠️ **This directory is EXCLUDED from Antigravity indexing**
- Files here won't appear in workspace search
- Prevents crashes from large design files
- Keeps workspace fast and responsive

✅ **Files are still accessible**
- Browse via file explorer in IDE
- Reference via relative paths: `../design-assets/exports/logo.svg`
- Use in HTML/markdown as needed

## Usage

**Add large source files:**
```bash
cp /path/to/mockup.psd design-assets/raw/
```

**Add optimized exports:**
```bash
cp /path/to/logo.svg design-assets/exports/
```

**Reference in SSOT:**
```markdown
Hero Image: `../design-assets/exports/hero.jpg`
```

See: `DESIGN_FILES_GUIDE.md` for full integration instructions.
