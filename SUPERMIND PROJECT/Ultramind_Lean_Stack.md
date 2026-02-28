# ULTRAMIND LEAN STACK v2.0
## The Zero-Point Technical Architecture

**"Skills + Scripts > MCPs"**

*Minimal context, maximum capability. Token discipline is accuracy discipline.*

---

Version: 2.0.0  
Updated: 2026-01-07  
Codename: Operation Deep Ultra  
Doctrine: Zero-Point Context Strategy

---

## EXECUTIVE SUMMARY

The ULTRAMIND Lean Stack is built on one core principle:

> **Every always-loaded parameter schema competes with your offer, your copy voice, your SSOT objects, and your orchestration rules.**

We achieve powerful agentic capabilities by:
1. **Keeping context light at Zero-Point** (default state)
2. **Activating skills on-demand** (temporary power)
3. **Returning to Zero-Point** after each operation
4. **Replacing 80% of MCPs** with Skills + Scripts

---

## THE ZERO-POINT CONTEXT STRATEGY

### Default State (Always Loaded) — ~500 tokens max

```yaml
ZERO_POINT_CONTEXT:
  # MOD/MMA Quick Refs (L1 only)
  orchestration:
    - ZPWO routing rules
    - MMA dimension thresholds
    - Current phase (Draft/Produce/Polish)
  
  # SSOT Headers Only (not full objects)
  ssot_index:
    - PROJECT_BRIEF: "PB-2026-001 v2.1"
    - MESSAGE_SPINE: "MS-2026-001 v2.2"
    - EVIDENCE_PACK: "EP-2026-001 v1.1"
    - VOICE_GUIDE: "VG-2026-001 v2.1"
  
  # Tool Index (capabilities list, not schemas)
  tool_capabilities:
    - web_intelligence: "search + fetch + extract + cite"
    - repo_ops: "branch + PR + diff + review"
    - script_runner: "python + bash + validate"
    - knowledge_graph: "extract + store + query"
  
  # Session State
  session:
    phase: "P2_Production"
    active_deliverable: "advertorial_v1"
    active_skill: null  # Nothing loaded by default
```

### Activated State (Temporary)

```
ZERO_POINT ──► ACTIVATE SKILL ──► RUN TOOLS ──► COMPRESS TO SSOT ──► UNLOAD ──► ZERO_POINT
     │                                                                              │
     └──────────────────────────────────────────────────────────────────────────────┘
```

**Rule:** Never keep full tool schemas or script bodies in default context.

---

## THE STACK ARCHITECTURE

### Layer 0: Infrastructure (Cloud + Local)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           INFRASTRUCTURE LAYER                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │    SUPABASE     │  │    FIREBASE     │  │     CONVEX      │             │
│  │   (Current)     │  │   (Migration)   │  │  (Real-time)    │             │
│  ├─────────────────┤  ├─────────────────┤  ├─────────────────┤             │
│  │ PostgreSQL      │  │ Firestore       │  │ Real-time DB    │             │
│  │ pgvector        │  │ Auth            │  │ Functions       │             │
│  │ Auth            │  │ Storage         │  │ Subscriptions   │             │
│  │ Edge Functions  │  │ Functions       │  │ ACID txns       │             │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘             │
│                                                                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │  ZILLIZ/MILVUS  │  │     NEO4J       │  │   CLOUDFLARE    │             │
│  │  (Vectors)      │  │  (Knowledge)    │  │   (Edge/CDN)    │             │
│  ├─────────────────┤  ├─────────────────┤  ├─────────────────┤             │
│  │ Vector search   │  │ Graphiti        │  │ Workers         │             │
│  │ Similarity      │  │ Node/Edge store │  │ KV Store        │             │
│  │ Semantic index  │  │ Cypher queries  │  │ R2 Storage      │             │
│  │ Clustering      │  │ Path traversal  │  │ AI Gateway      │             │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘             │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Layer 1: Database Strategy

```yaml
DATABASE_STRATEGY:
  
  # Primary Relational + Vector (Current)
  supabase:
    role: "Primary data store (migration path open)"
    use_for:
      - User accounts + auth
      - Project metadata
      - SSOT object storage (JSON columns)
      - Audit logs
    postgres_extensions:
      - pgvector: "Embedding storage + similarity search"
      - pg_trgm: "Fuzzy text search"
    migration_to: "Firebase or Convex (evaluate Q2 2026)"
  
  # Real-time + Functions (Future Primary)
  convex:
    role: "Real-time collaboration + compute"
    use_for:
      - Live document editing
      - Real-time agent state
      - Subscription-based updates
      - ACID transactions for SSOT locks
    advantages:
      - TypeScript-native
      - Built-in reactivity
      - No cold starts
      - Automatic scaling
  
  # Alternative Auth + Storage (Evaluate)
  firebase:
    role: "Auth + file storage option"
    use_for:
      - Authentication (if leaving Supabase)
      - Large file storage (videos, PDFs)
      - Mobile SDK needs
    evaluate: "Compare with Supabase for total cost"
  
  # Vector Search (Dedicated)
  zilliz_milvus:
    role: "Production vector search"
    use_for:
      - Semantic similarity (embeddings)
      - Knowledge retrieval
      - Content deduplication
      - Clustering similar content
    why_separate:
      - Specialized for vector ops
      - Better performance than pgvector at scale
      - Managed cloud option (Zilliz)
  
  # Knowledge Graph (Semantic Relationships)
  neo4j:
    role: "Knowledge graph + relationship store"
    use_for:
      - Entity relationships
      - Concept hierarchies
      - Proof → Claim mappings
      - Avatar → Pain → Solution paths
    integration: "Graphiti for agent memory"
    output_format: "JSON nodes + edges"
```

### Layer 2: AI/Agent Framework

```yaml
AI_AGENT_LAYER:
  
  # Orchestration
  pydantic_ai:
    role: "Type-safe agent definitions"
    use_for:
      - Agent class definitions
      - Tool schemas (strict)
      - Result validation
      - Structured outputs
  
  langgraph:
    role: "Workflow orchestration"
    use_for:
      - Multi-step workflows
      - State machines
      - HITL breakpoints
      - Conditional routing
  
  # Human-in-the-Loop
  copilotkit:
    role: "HITL interface"
    components:
      - useAgent: "Subscribe to agent state"
      - useApproval: "Human approval gates"
      - AG-UI: "Generative UI components"
    ag_ui_components:
      - MMAScorecard: "7D quality visualization"
      - SevenSCoverage: "Dimension heatmap"
      - DriftReport: "Cross-asset consistency"
  
  # Model Routing
  model_router:
    default: "claude-sonnet-4-20250514"
    fast: "claude-haiku"
    reasoning: "claude-sonnet-4-20250514"
    fallback: "gemini-2.0-flash"
    routing_rules:
      - "Draft phase → Sonnet (creativity)"
      - "Validation → Haiku (speed)"
      - "Complex reasoning → Sonnet"
      - "Cost optimization → Gemini fallback"
```

### Layer 3: Document Processing Pipeline

```yaml
DOCUMENT_PROCESSING:
  
  # Layout-Aware Parsing
  docling:
    role: "Layout-aware markdown extraction"
    capabilities:
      - PDF → Structured Markdown
      - Table extraction with context
      - Image + caption linking
      - Header hierarchy preservation
      - Code block detection
    output: "Layout-aware markdown with metadata"
  
  # Semantic Extraction
  langextract:
    role: "Semantic relationship extraction"
    capabilities:
      - Entity extraction (people, orgs, concepts)
      - Relationship identification
      - Claim detection
      - Evidence linking
    output: "JSON with entities + relationships"
  
  # Knowledge Graph Pipeline
  knowledge_pipeline:
    flow: |
      Document 
        → Docling (layout-aware parse)
        → LangExtract (semantic extraction)
        → Entity Resolution
        → Neo4j (nodes + edges)
        → Zilliz (embeddings)
    
    output_format:
      nodes:
        - id: "uuid"
          type: "Concept | Entity | Claim | Evidence"
          properties: {}
          embedding_ref: "zilliz_id"
      edges:
        - source: "node_id"
          target: "node_id"
          type: "SUPPORTS | CONTRADICTS | RELATED_TO | CAUSES"
          properties: {}
```

### Layer 4: LSP Integration (Code Intelligence)

```yaml
LSP_INTEGRATION:
  
  purpose: "Code intelligence for skill/script development"
  
  # Language Servers
  language_servers:
    python:
      server: "pylsp or pyright"
      features:
        - Autocomplete for SSOT schemas
        - Type checking for Pydantic models
        - Validation script linting
    typescript:
      server: "typescript-language-server"
      features:
        - Convex function types
        - React component props
        - API type safety
    yaml:
      server: "yaml-language-server"
      features:
        - SSOT schema validation
        - Skill definition linting
        - Config file checking
  
  # Cloud LSP (Remote Development)
  cloud_lsp:
    providers:
      - "Gitpod (full cloud IDE)"
      - "GitHub Codespaces"
      - "Cursor (AI-native)"
    benefits:
      - Consistent environment
      - No local setup
      - Shared configurations
      - AI assistance built-in
  
  # Integration Points
  integration:
    cursor_ide:
      role: "Primary development environment"
      features:
        - Agent layout mode
        - AI autocomplete
        - Skill file editing
    claude_code:
      role: "Agentic coding"
      features:
        - CLI execution
        - File operations
        - Git workflows
```

---

## SKILLS > MCPs DOCTRINE

### The Core Principle

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│   MCPs: Full schemas ALWAYS in context → Bloat + cognitive load             │
│                                                                              │
│   Skills: Thin descriptors + ON-DEMAND activation → Minimal until needed    │
│                                                                              │
│   TOKEN DISCIPLINE = ACCURACY DISCIPLINE                                     │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### MCP Replacement Map

| Old (MCP) | New (Skill + Script) | When to Escalate to MCP |
|-----------|---------------------|------------------------|
| Browser MCP | `dev_browser` skill + CLI fetch | Heavy automation + self-healing tests |
| GitHub MCP | `repo_ops` skill + `gh` CLI | Complex multi-repo orchestration |
| Exa MCP | `web_intelligence` skill | Never (skill is sufficient) |
| Terminal MCP | `script_runner` skill + bash | Never (skill is sufficient) |
| Filesystem MCP | `file_ops` skill + native | Never (skill is sufficient) |
| Database MCP | Typed client + skill wrapper | Complex migrations only |

### The Skill Package Pattern

Every tool skill ships with:

```yaml
SKILL_PACKAGE:
  
  # L1: Micro Descriptor (90-200 tokens) — Always available
  l1_descriptor:
    capability: "Web fetch + extract + cite"
    inputs: ["url", "extraction_schema"]
    outputs: ["content", "citations", "evidence_items"]
    safety: "Respects robots.txt, rate limits"
    escalation: "MCP only for JS-heavy sites"
  
  # L2: Procedure (loaded on activation)
  l2_procedure:
    steps:
      - "Fetch URL with headers"
      - "Parse HTML/JSON response"
      - "Extract per schema"
      - "Generate citations"
      - "Store in EVIDENCE_PACK"
    branching:
      - "If 403 → retry with different UA"
      - "If JS-required → escalate to browser"
  
  # L3: Helper Scripts (loaded only when needed)
  l3_scripts:
    - "fetch_with_retry.py"
    - "html_extractor.py"
    - "citation_formatter.py"
    validators:
      - "output_schema_validator.py"
  
  # L4: SSOT Contracts
  l4_contracts:
    stores_to: ["EVIDENCE_PACK.evidence_items"]
    locked_fields: ["source_url", "fetch_date"]
    logging: "ACTION_LOG + CORRECTION_LOG"
    patch_hooks: true
```

### Tool Index (Zero-Point Friendly)

```yaml
# TOOL_INDEX.yaml — Single canonical registry
# Total context cost: ~200 tokens

TOOL_INDEX:
  version: "1.0"
  updated: "2026-01-07"
  
  skills:
    - id: "web_intelligence"
      capability: "search + fetch + extract + cite"
      inputs: ["query | url", "extraction_schema"]
      outputs: ["content", "citations", "EP_items"]
      activation: "/web-intel"
      escalation: "browser_mcp (JS-heavy only)"
      latency: "2-5s"
      cost: "low"
    
    - id: "repo_ops"
      capability: "branch + PR + diff + review + merge"
      inputs: ["repo", "action", "params"]
      outputs: ["result", "diff", "status"]
      activation: "/repo"
      escalation: "github_mcp (multi-repo orchestration)"
      latency: "1-3s"
      cost: "free"
    
    - id: "script_runner"
      capability: "python + bash + node execution"
      inputs: ["script_ref", "args"]
      outputs: ["stdout", "stderr", "artifacts"]
      activation: "/run"
      escalation: "never"
      latency: "<1s"
      cost: "free"
    
    - id: "knowledge_graph"
      capability: "extract + store + query entities"
      inputs: ["document | query"]
      outputs: ["nodes", "edges", "subgraph"]
      activation: "/kg"
      escalation: "never"
      latency: "3-10s"
      cost: "medium"
    
    - id: "file_ops"
      capability: "read + write + search + transform"
      inputs: ["path", "operation", "content"]
      outputs: ["result", "file_ref"]
      activation: "/file"
      escalation: "never"
      latency: "<1s"
      cost: "free"
    
    - id: "validator"
      capability: "schema + proof + compliance checks"
      inputs: ["content", "validation_type"]
      outputs: ["valid", "errors", "suggestions"]
      activation: "/validate"
      escalation: "never"
      latency: "<1s"
      cost: "free"
```

---

## KNOWLEDGE GRAPH PIPELINE

### Document → Graph Flow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   DOCUMENT  │────►│   DOCLING   │────►│ LANGEXTRACT │────►│   NEO4J     │
│  (PDF/MD)   │     │  (Layout)   │     │ (Semantic)  │     │  (Graph)    │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
                           │                   │                   │
                           ▼                   ▼                   ▼
                    ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
                    │  Markdown   │     │   Entities  │     │   Nodes +   │
                    │  + Layout   │     │   + Rels    │     │   Edges     │
                    │  Metadata   │     │   JSON      │     │   JSON      │
                    └─────────────┘     └─────────────┘     └─────────────┘
                                               │
                                               ▼
                                        ┌─────────────┐
                                        │   ZILLIZ    │
                                        │ (Embeddings)│
                                        └─────────────┘
```

### Output Schema (Neo4j JSON)

```json
{
  "document_id": "doc_2026_001",
  "extraction_date": "2026-01-07",
  "pipeline_version": "1.0",
  
  "nodes": [
    {
      "id": "n_001",
      "type": "Concept",
      "label": "Cortisol Reset Protocol",
      "properties": {
        "category": "mechanism",
        "source_doc": "doc_2026_001",
        "confidence": 0.92
      },
      "embedding_ref": "zilliz_emb_001"
    },
    {
      "id": "n_002",
      "type": "Claim",
      "label": "Reduces cortisol within 7 days",
      "properties": {
        "claim_type": "outcome",
        "strength": "medium",
        "evidence_refs": ["E01", "E02"]
      },
      "embedding_ref": "zilliz_emb_002"
    },
    {
      "id": "n_003",
      "type": "Evidence",
      "label": "Smith et al. 2024 Study",
      "properties": {
        "source_type": "peer_reviewed",
        "url": "https://...",
        "reliability": "high"
      },
      "embedding_ref": "zilliz_emb_003"
    }
  ],
  
  "edges": [
    {
      "id": "e_001",
      "source": "n_001",
      "target": "n_002",
      "type": "ENABLES",
      "properties": {
        "confidence": 0.85,
        "extracted_from": "paragraph_14"
      }
    },
    {
      "id": "e_002",
      "source": "n_003",
      "target": "n_002",
      "type": "SUPPORTS",
      "properties": {
        "strength": "strong",
        "citation_context": "..."
      }
    }
  ],
  
  "metadata": {
    "total_nodes": 3,
    "total_edges": 2,
    "node_types": ["Concept", "Claim", "Evidence"],
    "edge_types": ["ENABLES", "SUPPORTS"]
  }
}
```

### Graphiti Integration (Agent Memory)

```yaml
GRAPHITI_CONFIG:
  
  purpose: "Persistent agent memory as knowledge graph"
  
  node_types:
    - Entity: "People, companies, products"
    - Concept: "Ideas, mechanisms, frameworks"
    - Claim: "Statements that need proof"
    - Evidence: "Proof items"
    - Avatar: "Customer profiles"
    - Offer: "Products/services"
    - Session: "Conversation contexts"
  
  edge_types:
    - SUPPORTS: "Evidence → Claim"
    - CONTRADICTS: "Evidence → Claim"
    - RELATED_TO: "Concept → Concept"
    - CAUSES: "Mechanism → Outcome"
    - EXPERIENCES: "Avatar → Pain"
    - DESIRES: "Avatar → Outcome"
    - SOLVES: "Offer → Pain"
    - DISCUSSED_IN: "Entity → Session"
  
  queries:
    # Find proof gaps
    proof_gaps: |
      MATCH (c:Claim)
      WHERE NOT (c)<-[:SUPPORTS]-(:Evidence)
      RETURN c.label, c.id
    
    # Avatar pain-solution mapping
    avatar_journey: |
      MATCH (a:Avatar)-[:EXPERIENCES]->(p:Pain)<-[:SOLVES]-(o:Offer)
      RETURN a, p, o
    
    # Evidence chain
    evidence_chain: |
      MATCH path = (e:Evidence)-[:SUPPORTS*1..3]->(c:Claim)
      WHERE c.id = $claim_id
      RETURN path
```

---

## 3-PHASE TOOLING ALIGNMENT

### Phase 1: Drafting / Exploration

```yaml
P1_DRAFT:
  goal: "Speed, creativity, breadth"
  
  tool_stance:
    active_skills: ["minimal"]
    search: "light (quick lookups only)"
    automation: "none"
  
  allowed:
    - Basic web search (no deep extraction)
    - File read/write
    - SSOT object creation
  
  not_allowed:
    - Heavy scraping
    - Multi-step automation
    - Database writes (except drafts)
  
  output: "3-10 viable angles in SSOT"
```

### Phase 2: Production / Refinement

```yaml
P2_PRODUCTION:
  goal: "Build assets with grounded proof"
  
  tool_stance:
    active_skills: ["web_intelligence", "knowledge_graph", "validator"]
    search: "deep (full extraction)"
    automation: "validation only"
  
  allowed:
    - Full web intelligence pipeline
    - Knowledge graph population
    - Evidence extraction
    - MMA continuous validation
  
  pipeline:
    - Activate retrieval skills
    - Fetch evidence + competitor refs
    - Populate EVIDENCE_PACK
    - Tighten MESSAGE_SPINE
    - Run validators
  
  output: "Publishable assets, MMA PASS"
```

### Phase 3: Polish / Perfect

```yaml
P3_POLISH:
  goal: "Resonance, compliance, final QA"
  
  tool_stance:
    active_skills: ["validator", "compliance"]
    search: "none (use cached)"
    automation: "compliance scans"
  
  allowed:
    - MMA 7D scoring
    - Compliance scanning
    - Human persuasion editor pass
    - Patch logging
  
  pipeline:
    - MMA deep audit
    - Compliance gate
    - Voice consistency check
    - Kitchen table test
    - Generate CORRECTION_LOG
    - Propose PATCH_CANDIDATES
  
  output: "Final assets + patch proposals"
```

---

## LOGGING, LEARNING, PATCHING (Heal & Renew)

### Every Tool Skill Emits:

```yaml
SKILL_OUTPUTS:
  
  # What it did
  ACTION_LOG:
    skill_id: "web_intelligence"
    timestamp: "2026-01-07T14:30:00Z"
    commands:
      - "fetch https://example.com"
      - "extract per schema"
    produced:
      - type: "evidence_item"
        ref: "E01"
    stored_to:
      - "EVIDENCE_PACK.evidence_items"
    duration_ms: 2340
    success: true
  
  # What went wrong (from MMA/Human)
  CORRECTION_LOG:
    skill_id: "web_intelligence"
    timestamp: "2026-01-07T15:00:00Z"
    failure_type: "extraction_incomplete"
    signature: "missing_author_field"
    context: "Academic papers often have author in different location"
    recommended_fix: "Add fallback extraction pattern for academic sources"
  
  # Proposed improvements
  PATCH_CANDIDATE:
    skill_id: "web_intelligence"
    proposed_by: "mma_validator"
    timestamp: "2026-01-07T15:05:00Z"
    change_type: "add_heuristic"
    description: "Add academic source detection + alternate extraction"
    priority: "medium"
    confidence: 0.78
    code_diff: |
      + if is_academic_source(url):
      +     return extract_academic_pattern(html)
```

---

## THE FULL STACK (Summary)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        ULTRAMIND LEAN STACK v2.0                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  FRONTEND                                                                    │
│  ├── Next.js 14+ (App Router)                                               │
│  ├── React 18+ (Server Components)                                          │
│  ├── Tailwind CSS v4                                                        │
│  ├── Shadcn/ui (Components)                                                 │
│  ├── Framer Motion (Animation)                                              │
│  └── CopilotKit + AG-UI (Agent Interface)                                   │
│                                                                              │
│  AI/AGENT LAYER                                                              │
│  ├── Claude Sonnet (Primary reasoning)                                      │
│  ├── Claude Haiku (Fast validation)                                         │
│  ├── Gemini Flash (Fallback)                                                │
│  ├── Pydantic AI (Type-safe agents)                                         │
│  ├── LangGraph (Workflow orchestration)                                     │
│  └── Skills + Scripts (NOT MCPs)                                            │
│                                                                              │
│  DOCUMENT PROCESSING                                                         │
│  ├── Docling (Layout-aware markdown)                                        │
│  ├── LangExtract (Semantic relationships)                                   │
│  └── Custom parsers (domain-specific)                                       │
│                                                                              │
│  DATA LAYER                                                                  │
│  ├── Supabase (PostgreSQL + pgvector) — Current                            │
│  ├── Convex (Real-time + Functions) — Migration target                     │
│  ├── Firebase (Auth + Storage) — Evaluate                                   │
│  ├── Zilliz/Milvus (Vector search) — Dedicated                             │
│  └── Neo4j + Graphiti (Knowledge graph)                                     │
│                                                                              │
│  DEVELOPMENT                                                                 │
│  ├── Cursor IDE (AI-native)                                                 │
│  ├── Claude Code (Agentic coding)                                           │
│  ├── LSP (Python, TypeScript, YAML)                                         │
│  ├── GitHub + gh CLI                                                        │
│  └── Cloud LSP (Gitpod/Codespaces)                                          │
│                                                                              │
│  INFRASTRUCTURE                                                              │
│  ├── Vercel (Frontend hosting)                                              │
│  ├── Railway/Render (Backend)                                               │
│  ├── Cloudflare (CDN + Workers + AI Gateway)                                │
│  └── GitHub Actions (CI/CD)                                                 │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## WHAT TO BUILD NEXT (Priority Order)

### Immediate (This Week)
1. **TOOL_INDEX.yaml** — Single canonical registry
2. **MOD Routing Rules** — Which skill activates when
3. **Web Intelligence Skill** — Search → Fetch → Extract → Cite → EP

### Short-term (This Month)
4. **Repo Ops Skill** — gh + git workflows
5. **Script Runner Skill** — Python/bash kit + validators
6. **Knowledge Graph Skill** — Docling + LangExtract → Neo4j

### Medium-term (Q1 2026)
7. **Convex Migration** — Real-time SSOT
8. **Zilliz Integration** — Production vector search
9. **Patch Refiner** — Reads logs → proposes skill upgrades

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 2026-01-07 | Complete rewrite: Skills > MCPs doctrine, multi-database strategy, LSP integration, knowledge graph pipeline, Docling + LangExtract |
| 1.0.0 | 2025-12-26 | Initial lean stack definition |

---

**Token Discipline = Accuracy Discipline**

**Skills + Scripts > MCPs**

**Zero-Point Context Strategy**

---

*ULTRAMIND Lean Stack v2.0 — Operation Deep Ultra*

