# ULTRAMIND TECHNICAL PATTERNS
## XML → Pydantic → Production Integration Guide

**Version:** 1.0.0  
**Updated:** 2026-01-07  
**Purpose:** Bridge XML skill definitions to production Pydantic AI implementations

---

## THE PATTERN STACK

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ULTRAMIND PATTERN STACK                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  LAYER 4: KNOWLEDGE ENGINE                                                  │
│  ├── Knowledge Graph (Neo4j + Graphiti)                                    │
│  ├── Vector Store (Zilliz/Milvus)                                          │
│  ├── AI Synthesizer (automatic organization)                               │
│  └── Intent-Based Execution (autonomy > automation)                        │
│                                                                              │
│  LAYER 3: PRODUCTION CODE                                                   │
│  ├── Pydantic AI Agents                                                    │
│  ├── Type-Safe Schemas (BaseModel)                                         │
│  ├── Field Validators (@field_validator)                                   │
│  ├── Self-Annealing Workflows                                              │
│  └── MMA Integration (quality loops)                                       │
│                                                                              │
│  LAYER 2: SKILL DEFINITIONS                                                 │
│  ├── XML Skill Files (L1-L4 progressive disclosure)                        │
│  ├── SSOT Contracts (inputs/outputs)                                       │
│  ├── Python Tools (deterministic validation)                               │
│  ├── MMA Quality Gates                                                     │
│  └── Golden Runs (test cases)                                              │
│                                                                              │
│  LAYER 1: ARCHITECTURE                                                      │
│  ├── Constitution v2.1 (principles)                                        │
│  ├── Lean Stack v2.0 (infrastructure)                                      │
│  ├── 6D Super-Resonance Model                                              │
│  ├── 7S/7F Chain                                                           │
│  └── SSOT Schemas v2.2                                                     │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## PART 1: XML SKILL TEMPLATE PATTERNS

### Token Budgets (Strict)

```yaml
L1_QuickReference:
  budget: "≤600 tokens"
  load: "always"
  purpose: "Instant orientation for 80% of tasks"
  
L2_CoreProcedure:
  budget: "≤4000 tokens"
  load: "when_executing"
  purpose: "Complete step-by-step instructions"
  
L3_AdvancedUsage:
  budget: "≤3000 tokens"
  load: "when_complexity_high"
  purpose: "Edge cases, failure modes, optimization"
  
L4_OutputTemplates:
  budget: "≤2000 tokens"
  load: "when_generating_deliverables"
  purpose: "Formal output specifications"
```

### Required Sections (Every Skill)

```xml
<Skill skill_id="skill.[domain].[name].v[X_Y_Z]">
  
  <!-- IDENTITY -->
  <Meta>...</Meta>
  <Purpose>...</Purpose>
  <Identity>...</Identity>
  <Scope>...</Scope>
  
  <!-- CONTRACTS -->
  <SSOT>...</SSOT>
  <Contract>...</Contract>
  <Dependencies>...</Dependencies>
  
  <!-- GUARDRAILS -->
  <Guardrails>...</Guardrails>
  <ConstitutionalCompliance>...</ConstitutionalCompliance>
  
  <!-- KNOWLEDGE (Progressive Disclosure) -->
  <ProgressiveDisclosure>
    <Layer id="L1">...</Layer>
    <Layer id="L2">...</Layer>
    <Layer id="L3">...</Layer>
    <Layer id="L4">...</Layer>
  </ProgressiveDisclosure>
  
  <!-- VALIDATION -->
  <PythonTools>...</PythonTools>      <!-- CRITICAL: Often missing! -->
  <MMAIntegration>...</MMAIntegration>
  <QAGates>...</QAGates>
  
  <!-- TESTING -->
  <GoldenRuns>...</GoldenRuns>
  
  <!-- COMPOSITION -->
  <Recipes>...</Recipes>
  
  <!-- HISTORY -->
  <VersionHistory>...</VersionHistory>
  
</Skill>
```

### Python Tools Section (Must Include!)

```xml
<PythonTools>
  <Tool name="validate_output_schema" execution_time="10ms">
    <Purpose>Validate output matches expected schema</Purpose>
    <Code><![CDATA[
def validate_output_schema(output: dict, schema_name: str) -> dict:
    """Validate output against SSOT schema"""
    from pydantic import ValidationError
    
    schemas = {
        "MESSAGE_SPINE": MessageSpineSchema,
        "PROJECT_BRIEF": ProjectBriefSchema,
        "EVIDENCE_PACK": EvidencePackSchema,
        "VOICE_GUIDE": VoiceGuideSchema
    }
    
    issues = []
    try:
        schema = schemas.get(schema_name)
        if schema:
            schema.model_validate(output)
    except ValidationError as e:
        issues = [str(err) for err in e.errors()]
    
    return {
        "passed": len(issues) == 0,
        "schema": schema_name,
        "issues": issues
    }
    ]]></Code>
  </Tool>
  
  <Tool name="validate_seven_s_coverage" execution_time="5ms">
    <Purpose>Check 7S dimension coverage</Purpose>
    <Code><![CDATA[
def validate_seven_s_coverage(content: str) -> dict:
    """Check which 7S dimensions are activated"""
    
    seven_s_markers = {
        "SAFE": ["guarantee", "protected", "risk-free", "secure"],
        "SPECIAL": ["unique", "exclusive", "different", "special"],
        "SMART": ["how", "works", "science", "step-by-step"],
        "SIGNIFICANT": ["proven", "results", "testimonial", "case study"],
        "SUPPORTED": ["click", "start", "begin", "next step"],
        "SUPERIOR": ["community", "support", "together", "family"],
        "STEAL": ["value", "bonus", "worth", "included"]
    }
    
    content_lower = content.lower()
    coverage = {}
    
    for dimension, markers in seven_s_markers.items():
        score = sum(1 for m in markers if m in content_lower)
        coverage[dimension] = min(score * 2, 10)  # Cap at 10
    
    weak_dimensions = [d for d, s in coverage.items() if s < 5]
    
    return {
        "passed": len(weak_dimensions) <= 2,
        "coverage": coverage,
        "weak_dimensions": weak_dimensions,
        "average_score": sum(coverage.values()) / len(coverage)
    }
    ]]></Code>
  </Tool>
</PythonTools>
```

---

## PART 2: PYDANTIC AI PRODUCTION PATTERNS

### Schema Design Pattern

```python
from pydantic import BaseModel, Field, field_validator
from typing import List, Literal, Dict
from enum import Enum

# ─────────────────────────────────────────────────────────────────────────────
# INPUT SCHEMA (Prevents hallucination)
# ─────────────────────────────────────────────────────────────────────────────

class SkillInput(BaseModel):
    """Type-safe input - prevents hallucination"""
    
    # Required fields with validation
    primary_input: str = Field(
        description="Main content to process",
        min_length=10,
        max_length=5000
    )
    
    # Constrained choices
    mode: Literal["draft", "production", "polish"] = Field(
        default="production",
        description="Processing mode"
    )
    
    # Optional context
    ssot_refs: Dict[str, str] | None = Field(
        default=None,
        description="References to SSOT objects"
    )
    
    @field_validator('primary_input')
    @classmethod
    def validate_input_quality(cls, v: str) -> str:
        """Custom validation logic"""
        if len(v.split()) < 5:
            raise ValueError("Input must be at least 5 words")
        return v


# ─────────────────────────────────────────────────────────────────────────────
# NEURO-BOX ACTIVATION (6D + 7S Assessment)
# ─────────────────────────────────────────────────────────────────────────────

class NeuroBoxActivation(BaseModel):
    """6D axis activation assessment"""
    
    # AXIS A: BODY ↔ HEART
    body_safe: Literal["none", "weak", "moderate", "strong"] = Field(
        description="BODY/Dopamine/SAFE activation"
    )
    heart_special: Literal["none", "weak", "moderate", "strong"] = Field(
        description="HEART/GABA/SPECIAL activation"
    )
    
    # AXIS B: MIND ↔ SPIRIT
    mind_smart: Literal["none", "weak", "moderate", "strong"] = Field(
        description="MIND/Acetylcholine/SMART activation"
    )
    spirit_significant: Literal["none", "weak", "moderate", "strong"] = Field(
        description="SPIRIT/Serotonin/SIGNIFICANT activation"
    )
    
    # AXIS C: PSYCHE ↔ CONSCIENCE
    psyche_supported: Literal["none", "weak", "moderate", "strong"] = Field(
        description="PSYCHE/Adrenaline/SUPPORTED activation"
    )
    conscience_superior: Literal["none", "weak", "moderate", "strong"] = Field(
        description="CONSCIENCE/Oxytocin/SUPERIOR activation"
    )
    
    # CENTER: SOUL
    soul_steal: Literal["none", "weak", "moderate", "strong"] = Field(
        description="SOUL/Zero-Point/STEAL activation"
    )


class SevenSCoverage(BaseModel):
    """7S Chain coverage map"""
    
    safe: int = Field(ge=0, le=10, description="SAFE dimension score")
    special: int = Field(ge=0, le=10, description="SPECIAL dimension score")
    smart: int = Field(ge=0, le=10, description="SMART dimension score")
    significant: int = Field(ge=0, le=10, description="SIGNIFICANT dimension score")
    supported: int = Field(ge=0, le=10, description="SUPPORTED dimension score")
    superior: int = Field(ge=0, le=10, description="SUPERIOR dimension score")
    steal: int = Field(ge=0, le=10, description="STEAL dimension score")
    
    @property
    def average(self) -> float:
        return sum([
            self.safe, self.special, self.smart, 
            self.significant, self.supported, self.superior, self.steal
        ]) / 7
    
    @property
    def weak_dimensions(self) -> List[str]:
        dims = {
            "SAFE": self.safe, "SPECIAL": self.special, "SMART": self.smart,
            "SIGNIFICANT": self.significant, "SUPPORTED": self.supported,
            "SUPERIOR": self.superior, "STEAL": self.steal
        }
        return [d for d, s in dims.items() if s < 7]


# ─────────────────────────────────────────────────────────────────────────────
# OUTPUT SCHEMA (Validated at runtime)
# ─────────────────────────────────────────────────────────────────────────────

class SkillOutput(BaseModel):
    """Type-safe output with quality metadata"""
    
    # Primary output
    content: str = Field(description="Generated content")
    
    # Quality assessment
    neurobox_activation: NeuroBoxActivation
    seven_s_coverage: SevenSCoverage
    
    # Self-assessment
    self_critique: str = Field(description="Agent's quality assessment")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score")
    
    # MMA readiness
    ready_for_mma: bool = Field(default=True)
    mma_expected_score: float = Field(ge=0.0, le=10.0)
    
    @field_validator('content')
    @classmethod
    def validate_content(cls, v: str) -> str:
        """Ensure content meets minimum quality"""
        if len(v) < 100:
            raise ValueError("Content too short for production")
        return v
```

### Self-Annealing Pattern

```python
async def generate_with_annealing(
    input_data: SkillInput,
    skill_agent: Agent,
    max_attempts: int = 3,
    quality_threshold: float = 8.0
) -> tuple[SkillOutput, MMAReview, int]:
    """
    Generate output with self-annealing quality loop
    
    Pattern:
    1. Generate output
    2. MMA validates
    3. If FAIL: Regenerate with critique
    4. Max N attempts, then escalate
    """
    
    for attempt in range(1, max_attempts + 1):
        print(f"🔄 Attempt {attempt}/{max_attempts}")
        
        # Generate
        result = await skill_agent.run(input_data.model_dump_json())
        output = result.data
        
        # MMA Review
        review = await mma_review(output, quality_threshold)
        
        print(f"🎯 MMA Score: {review.overall_score:.1f}/10")
        print(f"⚖️  Verdict: {review.verdict}")
        
        # Check quality
        if review.verdict == "PASS":
            print(f"✨ Quality achieved in {attempt} attempt(s)")
            return output, review, attempt
        
        elif review.verdict == "FIX" and attempt < max_attempts:
            print(f"🔧 Issues: {review.revision_instructions}")
            print("🔄 Self-annealing: Regenerating with critique...")
            
            # Add critique to context for next attempt
            input_data = input_data.model_copy(update={
                "previous_critique": review.critique,
                "fix_instructions": review.revision_instructions
            })
            continue
        
        else:
            print(f"⚠️  Max attempts reached")
            return output, review, attempt
    
    return output, review, max_attempts


# MMA Review Schema
class MMAReview(BaseModel):
    """MMA quality assessment"""
    
    overall_score: float = Field(ge=0.0, le=10.0)
    
    dimensions: Dict[str, float] = Field(
        description="7D scorecard"
    )
    
    verdict: Literal["PASS", "FIX", "ESCALATE"]
    
    critique: str | None = None
    revision_instructions: List[str] = Field(default_factory=list)
```

---

## PART 3: KNOWLEDGE ENGINE INTEGRATION

### Knowledge Graph Schema (Pydantic)

```python
from enum import Enum
from typing import List, Dict, Any

class NodeType(str, Enum):
    CONCEPT = "concept"       # Ideas, frameworks
    SKILL = "skill"           # ULTRAMIND skills
    CLAIM = "claim"           # Statements needing proof
    EVIDENCE = "evidence"     # Proof items
    AVATAR = "avatar"         # Customer profiles
    OFFER = "offer"           # Products/services
    MEMORY = "memory"         # Episodic memories
    PATTERN = "pattern"       # Detected patterns
    INSIGHT = "insight"       # AI-generated insights

class RelationType(str, Enum):
    SUPPORTS = "supports"         # Evidence → Claim
    CONTRADICTS = "contradicts"   # Evidence → Claim
    ENABLES = "enables"           # A enables B
    REQUIRES = "requires"         # A requires B
    EVOLVES = "evolves"           # A evolves into B
    RELATED_TO = "related_to"     # Loose association
    CAUSES = "causes"             # Mechanism → Outcome
    EXPERIENCES = "experiences"   # Avatar → Pain
    SOLVES = "solves"             # Offer → Pain

class KnowledgeNode(BaseModel):
    """Core knowledge unit"""
    
    id: str
    type: NodeType
    title: str
    content: str
    
    # AI-generated metadata
    embedding_ref: str | None = None  # Reference to vector in Zilliz
    summary: str | None = None
    key_insights: List[str] = Field(default_factory=list)
    
    # Tags (flexible categorization)
    tags: List[str] = Field(default_factory=list)
    properties: Dict[str, Any] = Field(default_factory=dict)
    
    # 7S mapping
    seven_s_target: str | None = None  # Which dimension this serves
    
    # Evolution tracking
    version: int = 1
    evolved_from: str | None = None
    
    # AI confidence
    ai_confidence: float = Field(ge=0.0, le=1.0, default=0.8)
    validation_status: Literal["validated", "hypothesis", "deprecated"] = "hypothesis"


class KnowledgeEdge(BaseModel):
    """Relationship between nodes"""
    
    id: str
    source: str  # Node ID
    target: str  # Node ID
    type: RelationType
    
    # Context
    properties: Dict[str, Any] = Field(default_factory=dict)
    confidence: float = Field(ge=0.0, le=1.0, default=0.8)
    
    # Extraction metadata
    extracted_from: str | None = None  # Document/conversation source


class KnowledgeGraphOutput(BaseModel):
    """Output format for Neo4j import (JSON)"""
    
    document_id: str
    extraction_date: str
    pipeline_version: str = "1.0"
    
    nodes: List[KnowledgeNode]
    edges: List[KnowledgeEdge]
    
    metadata: Dict[str, Any] = Field(default_factory=dict)
```

### Knowledge → SSOT Pipeline

```
Document/Conversation
        │
        ▼
┌───────────────┐
│    Docling    │  (Layout-aware parsing)
│  (Parser)     │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│  LangExtract  │  (Semantic extraction)
│  (Extractor)  │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│   Pydantic    │  (Type-safe validation)
│   Schemas     │
└───────┬───────┘
        │
   ┌────┴────┐
   │         │
   ▼         ▼
┌──────┐  ┌──────┐
│Neo4j │  │Zilliz│
│(Graph)│  │(Vecs)│
└──────┘  └──────┘
        │
        ▼
┌───────────────┐
│  SSOT Objects │
│ (Populated)   │
│ EP, MS, PB    │
└───────────────┘
```

---

## PART 4: AUTONOMY > AUTOMATION PRINCIPLE

### The Critical Distinction

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        AUTOMATION vs AUTONOMY                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  AUTOMATION (N8N, Zapier, Make) ❌                                          │
│  ─────────────────────────────────                                          │
│  "When email arrives → extract data → add to sheet → send Slack"           │
│                                                                              │
│  Problems:                                                                   │
│  • Breaks when format changes                                               │
│  • Breaks when API updates                                                  │
│  • No learning, no adaptation                                               │
│  • Rigid, brittle, maintenance nightmare                                    │
│                                                                              │
│  ──────────────────────────────────────────────────────────────────────────│
│                                                                              │
│  AUTONOMY (ULTRAMIND Agents) ✅                                             │
│  ─────────────────────────────────                                          │
│  "Keep track of important client communications and surface insights"       │
│                                                                              │
│  Advantages:                                                                 │
│  • Understands intent (not just steps)                                     │
│  • Adapts to format changes                                                 │
│  • Handles edge cases intelligently                                         │
│  • Learns what's "important" over time                                     │
│  • Self-heals when things break                                            │
│  • Gets smarter with use                                                    │
│                                                                              │
│  ──────────────────────────────────────────────────────────────────────────│
│                                                                              │
│  THE DIFFERENCE:                                                            │
│  • Automation: "Do this exact sequence" (fragile)                          │
│  • Autonomy: "Achieve this outcome" (adaptive)                             │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Intent-Based Execution Pattern

```python
class Intent(BaseModel):
    """What the user wants to achieve (not steps to do)"""
    
    description: str
    success_criteria: List[str]
    context: Dict[str, Any] = Field(default_factory=dict)
    constraints: List[str] = Field(default_factory=list)


class IntentExecutor:
    """
    NOT: Fixed workflow
    BUT: Dynamic plan based on intent + current knowledge
    """
    
    async def execute(self, intent: Intent) -> ExecutionResult:
        
        # 1. Understand intent (not parse steps)
        understanding = await self.understand_intent(intent)
        
        # 2. Query knowledge graph for relevant context
        knowledge = await self.query_knowledge(understanding)
        
        # 3. Generate plan dynamically (not fixed workflow)
        plan = await self.generate_plan(understanding, knowledge)
        
        # 4. Execute with adaptation
        for step in plan.steps:
            result = await self.execute_step(step)
            
            # Adapt if needed (self-healing)
            if result.needs_adaptation:
                plan = await self.adapt_plan(plan, result)
        
        # 5. Learn from execution
        await self.learn_from_execution(intent, plan, result)
        
        return result
```

---

## PART 5: SELF-IMPROVEMENT HOOKS

### Skill Self-Improvement Protocol

```xml
<SelfImprovement>
  <AfterEachRun>
    <Action>Store: Input type, output quality, MMA score</Action>
    <Action>Track: Which patterns worked</Action>
    <Action>Track: Which failures occurred</Action>
  </AfterEachRun>
  
  <AfterNRuns count="20">
    <Action>Analyze: Which input types score highest</Action>
    <Action>Analyze: Common failure patterns</Action>
    <Action>Analyze: Token budget accuracy</Action>
    <Action>Propose: Template adjustments</Action>
  </AfterNRuns>
  
  <QuarterlyReview>
    <Action>Review: All runs this quarter</Action>
    <Action>Identify: Emerging patterns in requests</Action>
    <Action>Update: Procedure to handle new patterns</Action>
    <Action>Calibrate: Quality thresholds</Action>
  </QuarterlyReview>
  
  <EvolutionTriggers>
    <Trigger>If >30% of outputs need revision → update templates</Trigger>
    <Trigger>If new request type 5+ times → add specialized handler</Trigger>
    <Trigger>If constitutional violations → strengthen guardrails</Trigger>
  </EvolutionTriggers>
</SelfImprovement>
```

### Pydantic Self-Improvement Tracking

```python
class SkillExecution(BaseModel):
    """Track each skill execution for learning"""
    
    skill_id: str
    timestamp: str
    
    # Input characteristics
    input_type: str
    input_tokens: int
    input_complexity: Literal["simple", "moderate", "complex"]
    
    # Output quality
    mma_score: float
    mma_verdict: Literal["PASS", "FIX", "ESCALATE"]
    weak_dimensions: List[str]
    
    # Performance
    attempts_needed: int
    total_tokens_used: int
    latency_ms: int
    
    # Human feedback (if available)
    human_satisfaction: float | None = None
    human_edits_needed: bool | None = None


class SkillLearningLog(BaseModel):
    """Aggregated learning from executions"""
    
    skill_id: str
    period_start: str
    period_end: str
    
    # Aggregate stats
    total_executions: int
    average_mma_score: float
    pass_rate: float
    
    # Pattern analysis
    common_failure_modes: List[str]
    high_performing_input_types: List[str]
    weak_dimensions_trend: Dict[str, int]
    
    # Recommendations
    suggested_improvements: List[str]
    template_updates_needed: bool
    guardrail_updates_needed: bool
```

---

## PART 6: FILE INTEGRATION MAP

### Where Each Pattern Lives

| Pattern | Source File | Integration Point |
|---------|-------------|-------------------|
| L1-L4 Progressive Disclosure | `xml_skill_template_v2.1.xml` | All skill XMLs |
| PythonTools validators | `xml_skill_template_v2.1.xml` | All skill XMLs |
| Pydantic schemas | `transformational_writer_pydantic.py` | Production code |
| Self-annealing | `transformational_writer_pydantic.py` | MMA loops |
| Knowledge Graph | `ULTRAMIND_KNOWLEDGE_ENGINE.md` | Neo4j + Graphiti |
| Intent-based execution | `ULTRAMIND_KNOWLEDGE_ENGINE.md` | TWA routing |
| Self-improvement hooks | `SKILL_ARCHITECT_v2_ENHANCED.md` | All skills |
| Value Equation | `xml_skill_template_v2.1.xml` | Offer/sales skills |
| Awareness Framework | `xml_skill_template_v2.1.xml` | Copy skills |
| Belief Ladder | `xml_skill_template_v2.1.xml` | Persuasion skills |

---

## PART 7: CHECKLIST FOR PRODUCTION SKILLS

### XML Skill File Checklist

```markdown
## SKILL FILE QUALITY CHECKLIST

### Structure
- [ ] L1-L4 layers present
- [ ] Token budgets respected
- [ ] Progressive disclosure correct

### Identity
- [ ] Meta complete (id, version, tier, status)
- [ ] Purpose clear
- [ ] Scope defined
- [ ] Non-negotiables listed

### Contracts
- [ ] SSOT inputs specified
- [ ] Outputs defined
- [ ] Dependencies mapped

### Validation
- [ ] PythonTools section present
- [ ] At least 2 validators included
- [ ] MMAIntegration configured
- [ ] QAGates by domain
- [ ] GoldenRuns (1-3 test cases)

### Integration
- [ ] Recipes for workflow composition
- [ ] Constitutional compliance
- [ ] Self-improvement hooks

### Quality
- [ ] 7S coverage addressed
- [ ] Neuro-Box activation specified
- [ ] Value Equation (if offer/sales)
- [ ] Awareness Framework (if copy)
```

### Pydantic Implementation Checklist

```markdown
## PYDANTIC IMPLEMENTATION CHECKLIST

### Schemas
- [ ] Input schema with validation
- [ ] Output schema with NeuroBoxActivation
- [ ] SevenSCoverage in output
- [ ] Field validators for critical fields

### Agent
- [ ] System prompt from L1-L4
- [ ] Structured output enabled
- [ ] Model specified

### Quality Loop
- [ ] MMA review function
- [ ] Self-annealing workflow
- [ ] Max attempts configured
- [ ] Escalation path defined

### Learning
- [ ] Execution tracking
- [ ] Learning log aggregation
- [ ] Improvement recommendations
```

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-07 | Initial synthesis from xml_skill_template, transformational_writer_pydantic, ULTRAMIND_KNOWLEDGE_ENGINE, SKILL_ARCHITECT_v2 |

---

*ULTRAMIND Technical Patterns v1.0*
*XML → Pydantic → Production*
*Knowledge → Intelligence → Autonomy*
