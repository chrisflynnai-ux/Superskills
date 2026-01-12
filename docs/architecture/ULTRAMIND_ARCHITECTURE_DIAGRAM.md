# ULTRAMIND Self-Annealing Architecture
## Visual System Diagram

```mermaid
graph TB
    subgraph "User Interaction Layer"
        U[User Message] --> CA[Chat Handler]
        CA --> UR[User Response]
    end
    
    subgraph "Dynamic Skill Assembly"
        CA --> SA[Skill Assembler]
        SA --> FS[Foundation Skills<br/>Always Active]
        SA --> CS[Capability Skills<br/>Context-Triggered]
        SA --> CC[Constitutional<br/>Constraints]
        FS --> AP[Assembled Prompt]
        CS --> AP
        CC --> AP
        AP --> CLAUDE[Claude 4.5 Haiku]
    end
    
    subgraph "Memory Consultation Layer"
        CLAUDE -.Consult Before Response.-> EM[Episodic Memory<br/>Similar Past Cases]
        CLAUDE -.Consult Before Response.-> SM[Semantic Memory<br/>Learned Principles]
        CLAUDE -.Consult Before Response.-> PM[Procedural Memory<br/>Proven Workflows]
        CLAUDE -.Consult Before Response.-> CM[Constitutional Memory<br/>Violation History]
    end
    
    subgraph "MCP Knowledge Layer"
        CLAUDE -.Knowledge Gap?.-> EXA[Exa.ai MCP<br/>Current Information]
        EXA -.Augmented Knowledge.-> CLAUDE
    end
    
    subgraph "Response Storage"
        CLAUDE --> MSG[Messages Table<br/>+Skill Usage Log]
        MSG --> SB[(Supabase<br/>PostgreSQL)]
    end
    
    subgraph "Reflection Loop - Every 12hrs"
        SB --> RL[Reflection Loop]
        RL --> NBE[Neuro-Box Evaluator]
        NBE --> S1[SAFE: Trust?]
        NBE --> S2[SPECIAL: Validated?]
        NBE --> S3[SMART: Solved?]
        NBE --> S4[SIGNIFICANT: Elevated?]
        NBE --> S5[SUPPORTED: Energized?]
        NBE --> S6[SUPERIOR: Vision?]
        S1 & S2 & S3 & S4 & S5 & S6 --> SCORES[Aggregate Scores]
    end
    
    subgraph "Decision Layer with Memory"
        SCORES --> HI[Historical Insights<br/>via Ref.tools MCP]
        REF[Ref.tools<br/>Evolution Memory] --> HI
        HI --> DM[Decision Matrix]
        DM -->|Score >= 4.0| NONE[No Action]
        DM -->|3.0-3.9| SUG[Create Suggestion]
        DM -->|2.0-2.9| UPD[Auto Update]
        DM -->|< 2.0| ESC[Escalate]
    end
    
    subgraph "Self-Healing Layer - Every 2hrs"
        SB --> SH[Self-Healing Loop]
        SH --> PD[Pattern Detection]
        PD --> PL[Pattern Library<br/>Known Failure Modes]
        PL -->|Pattern Match| HA[Healing Action]
        HA --> SP[Skill Patch]
        HA --> CP[Constitutional Patch]
        HA --> RB[Emergency Rollback]
    end
    
    subgraph "Constitutional Governance"
        UPD --> CR[Constitutional Review]
        CR --> NS[North Star Check]
        NS -->|Aligned| APPLY[Apply Update]
        NS -->|Drift Detected| BLOCK[Block & Escalate]
        APPLY --> SKT[Update Skills Table]
        SKT --> SB
    end
    
    subgraph "Effectiveness Tracking"
        APPLY --> EFF[Measure Effectiveness]
        SP --> EFF
        CP --> EFF
        EFF -->|Store Outcome| REF
        EFF -->|Update Pattern| PL
    end
    
    subgraph "Memory Population"
        MSG -.Extract.-> EM
        SCORES -.Extract Principles.-> SM
        HA -.Record Workflow.-> PM
        CR -.Record Violations.-> CM
    end
    
    style CLAUDE fill:#4A90E2,stroke:#2E5C8A,color:#fff
    style NBE fill:#E24A4A,stroke:#8A2E2E,color:#fff
    style SA fill:#4AE290,stroke:#2E8A5C,color:#fff
    style SH fill:#E2B44A,stroke:#8A6E2E,color:#fff
    style CR fill:#B44AE2,stroke:#6E2E8A,color:#fff
    style REF fill:#4AE2E2,stroke:#2E8A8A,color:#fff
    style EXA fill:#E2E24A,stroke:#8A8A2E,color:#000
```

## Data Flow Sequence

### Normal Operation
```
1. User sends message
2. Skill Assembler queries:
   - Foundation skills (always)
   - Triggered capability skills
   - Constitutional constraints
3. Assembled prompt sent to Claude
4. Claude consults 4 memory types
5. If knowledge gap: Query Exa.ai
6. Response generated
7. Stored with skill usage log
```

### Reflection Cycle (Every 12 hours)
```
1. Fetch last 20 conversations
2. Evaluate each on 6 Neuro-Box dimensions
3. Calculate aggregate scores
4. Consult Ref.tools for similar past situations
5. Make decision:
   - None (score >= 4.0)
   - Suggestion (3.0-3.9)
   - Auto-update (2.0-2.9)
   - Escalate (< 2.0)
6. If update: Constitutional review
7. Store reflection in Ref.tools
8. Measure effectiveness in next cycle
```

### Self-Healing Cycle (Every 2 hours, OR after 3 similar patterns)
```
1. Analyze recent reflections
2. Match against pattern library
3. If pattern threshold reached:
   a. Apply skill patch, OR
   b. Apply constitutional patch, OR
   c. Emergency rollback
4. Measure healing effectiveness
5. Update pattern library
6. Store workflow in procedural memory
```

## Memory Integration Points

### Episodic Memory
- **Populated:** Every user interaction
- **Queried:** Before generating response to find similar past cases
- **Updated:** Never (append-only historical record)

### Semantic Memory
- **Populated:** After each reflection (extract principles)
- **Queried:** Before making decisions ("What have we learned about X?")
- **Updated:** Confidence adjusted when validated/contradicted

### Procedural Memory
- **Populated:** When healing actions succeed
- **Queried:** Before applying corrections ("Has this workflow worked before?")
- **Updated:** Success rate after each execution

### Constitutional Memory
- **Populated:** When violations detected
- **Queried:** Before prompt updates ("Has this caused problems before?")
- **Updated:** When new safeguards created

## MCP Usage Patterns

### Ref.tools MCP
```
STORES:
- Every reflection log
- Every prompt update (before/after)
- Every healing event
- Every constitutional decision

QUERIES:
- "Similar situations to current scores/patterns"
- "Outcomes of past updates like this one"
- "Historical effectiveness of healing action X"
```

### Exa.ai MCP
```
TRIGGERS:
- Low confidence response detected
- Uncertainty markers in response
- Topic outside training data
- User asks about recent events

QUERIES:
- Semantic search for authoritative sources
- Filter to research papers, official docs
- Limit to 3 most relevant results

STORES:
- Sources in episodic memory
- New knowledge in semantic memory
```

### Supabase MCP
```
MANAGES:
- All tables (users, sessions, messages, etc.)
- Vector embeddings for semantic search
- Real-time subscriptions for UI
- Edge function deployments
```

## Key Architectural Principles

### 1. Progressive Disclosure
- Layer 1: Immediate core (500 tokens)
- Layer 2: Deeper context (1500 tokens)
- Layer 3: Examples (3000 tokens)
- Layer 4: Constitutional (1000 tokens)
- Total budget: ~8000 tokens for prompt

### 2. Proactive Healing
- Don't wait for critical failure
- Detect patterns early (3 occurrences)
- Apply corrections immediately
- Measure effectiveness

### 3. Constitutional Supremacy
- North Star cannot be compromised
- Critical constraints block auto-updates
- Weekly alignment verification
- Drift triggers immediate correction

### 4. Memory-Informed Decisions
- Every decision consults all 4 memory types
- Historical outcomes weigh heavily
- Patterns override individual cases
- Learning compounds over time

### 5. Lean MCP Integration
- Only 3 MCPs: Supabase, Ref.tools, Exa.ai
- Each has clear, non-overlapping purpose
- No "nice to have" integrations
- Minimize external dependencies
