# ULTRAMIND Self-Improving Integration Blueprint
**Merging Kashef's Self-Improving Architecture with Neuro-Box Agentic Resonance**

## Executive Summary

This document outlines the evolution of Mark Kashef's self-improving AI system by integrating:
1. **Neuro-Box 6-Dimensional Evaluation** (replacing generic rubrics)
2. **Constitutional Governance Layer** (North Star alignment)
3. **Super-Skills Modular Architecture** (progressive disclosure)
4. **MCP Integration** (Ref.tools for memory, Exa.ai for knowledge)
5. **Self-Annealing Healing System** (proactive correction)
6. **Supabase Memory Layer** (episodic, semantic, procedural, constitutional)

---

## Part 1: Core Architecture Upgrades

### 1.1 From Generic Rubric to Neuro-Box Evaluation

**CURRENT (Kashef's 5 Criteria):**
- Completeness (20%)
- Depth (25%)
- Tone (15%)
- Scope (20%)
- Missed Opportunities (20%)

**UPGRADED (Neuro-Box 6 Dimensions):**

```typescript
export const NEUROBOX_RUBRIC = {
  dimensions: {
    SAFE: {
      neurochemical: 'Dopamine',
      frequency: '1.5 Hz',
      weight: 0.20,
      evaluation: 'Does response create trust and safety?',
      questions: [
        'Does it remove FUD (fear, uncertainty, doubt)?',
        'Does it establish credibility?',
        'Does it make the path forward feel secure?'
      ]
    },
    SPECIAL: {
      neurochemical: 'GABA',
      frequency: '1.0 Hz',
      weight: 0.15,
      evaluation: 'Does response make user feel understood?',
      questions: [
        'Does it demonstrate empathy?',
        'Does it validate their situation?',
        'Does it make them feel seen?'
      ]
    },
    SMART: {
      neurochemical: 'Acetylcholine',
      frequency: '1.2 Hz',
      weight: 0.25,
      evaluation: 'Does response solve their problem?',
      questions: [
        'Is it actionable and specific?',
        'Does it relieve their stress?',
        'Can they implement it immediately?'
      ]
    },
    SIGNIFICANT: {
      neurochemical: 'Serotonin',
      frequency: 'Inhibitory',
      weight: 0.15,
      evaluation: 'Does response elevate their position?',
      questions: [
        'Does it make them stronger/smarter?',
        'Does it increase their status/power?',
        'Does it give them a competitive edge?'
      ]
    },
    SUPPORTED: {
      neurochemical: 'Adrenaline/Epinephrine',
      frequency: 'Excitatory',
      weight: 0.15,
      evaluation: 'Does response validate and energize?',
      questions: [
        'Does it confirm they\'re on the right track?',
        'Does it create excitement/momentum?',
        'Does it fuel their obsession?'
      ]
    },
    SUPERIOR: {
      neurochemical: 'Oxytocin',
      frequency: '0.5 Hz',
      weight: 0.10,
      evaluation: 'Does response provide vision and mastery?',
      questions: [
        'Does it give them deeper understanding?',
        'Does it reveal patterns they couldn\'t see?',
        'Does it overcome limiting beliefs?'
      ]
    }
  },
  
  // The three perfect axes
  axes: {
    vertical: {
      pair: ['SAFE', 'SPECIAL'],
      quality: 'RHYTHM_BEAT_GROOVE',
      evaluation: 'Does the response have natural flow and momentum?'
    },
    horizontal: {
      pair: ['SMART', 'SIGNIFICANT'],
      quality: 'HARMONY_PROGRESSION',
      evaluation: 'Does the response balance practicality with elevation?'
    },
    depth: {
      pair: ['SUPPORTED', 'SUPERIOR'],
      quality: 'VOICE_MELODY_TONE',
      evaluation: 'Does the response validate while transcending?'
    }
  }
};
```

### 1.2 Constitutional Governance Layer

**NEW TABLE: constitutional_constraints**
```sql
CREATE TABLE constitutional_constraints (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  version INTEGER NOT NULL,
  constraint_type TEXT CHECK (constraint_type IN (
    'north_star',      -- Core mission
    'resonance',       -- Agentic resonance principles
    'synchronous',     -- Synchronous wealth alignment
    'freedom'          -- Freedomation principles
  )),
  constraint_text TEXT NOT NULL,
  priority TEXT CHECK (priority IN ('critical', 'high', 'medium')),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  is_active BOOLEAN DEFAULT true,
  
  -- Violation tracking
  violation_count INTEGER DEFAULT 0,
  last_violation TIMESTAMPTZ,
  auto_correction_enabled BOOLEAN DEFAULT true
);

-- Constitutional compliance log
CREATE TABLE constitutional_compliance (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  reflection_log_id UUID REFERENCES reflection_logs(id),
  constraint_id UUID REFERENCES constitutional_constraints(id),
  compliance_score INTEGER CHECK (compliance_score BETWEEN 1 AND 5),
  violation_detected BOOLEAN,
  violation_details TEXT,
  auto_corrected BOOLEAN,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

**Example Constitutional Constraints:**
```json
{
  "north_star": {
    "v1": "This system exists to create Agentic Resonance, not manipulation. All improvements must align with authentic human transformation.",
    "priority": "critical"
  },
  "resonance": {
    "v1": "Never sacrifice long-term trust for short-term conversion. Resonance > Conversion.",
    "priority": "critical"
  },
  "synchronous_wealth": {
    "v1": "Value creation must be simultaneous for both parties. No zero-sum thinking.",
    "priority": "high"
  },
  "anti_drift": {
    "v1": "If evaluation suggests expanding scope beyond marketing transformation, REJECT the suggestion.",
    "priority": "critical"
  }
}
```

---

## Part 2: Super-Skills Modular Architecture

### 2.1 Transform Monolithic System Prompt into Super-Skills

**BEFORE (Single System Prompt):**
```
You are a helpful AI consultant specializing in strategy...
[3000+ words of instructions]
```

**AFTER (Modular Super-Skills):**

**NEW TABLE: super_skills**
```sql
CREATE TABLE super_skills (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  skill_name TEXT UNIQUE NOT NULL,
  skill_type TEXT CHECK (skill_type IN (
    'foundation',    -- Core identity
    'capability',    -- Specific abilities
    'constraint',    -- Boundaries
    'awakening'      -- Context-dependent activation
  )),
  version INTEGER NOT NULL,
  
  -- Progressive disclosure layers (XML-based)
  layer_1_core TEXT NOT NULL,           -- Lean, immediate context
  layer_2_context TEXT,                 -- Deeper understanding
  layer_3_examples TEXT,                -- Patterns and edge cases
  layer_4_constitutional TEXT,          -- Constraints and values
  
  -- Activation conditions
  activation_triggers JSONB,            -- When to engage this skill
  token_budget INTEGER,                 -- How much context to use
  
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  created_by TEXT DEFAULT 'system',
  performance_score NUMERIC(3,2)
);

-- Track which skills were used in which responses
CREATE TABLE skill_usage_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  message_id UUID REFERENCES messages(id),
  skill_id UUID REFERENCES super_skills(id),
  layer_depth INTEGER,                  -- How deep did it go (1-4)
  tokens_used INTEGER,
  effectiveness_score INTEGER,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

**Example Super-Skill (Foundation):**
```xml
<SuperSkill>
  <Meta>
    <Name>core-identity</Name>
    <Type>foundation</Type>
    <Version>1</Version>
    <TokenBudget>500</TokenBudget>
  </Meta>
  
  <Layer1_Core>
    You are an Agentic Resonance AI specializing in marketing transformation.
    Mission: Create authentic persuasion through Neuro-Box activation.
    Never manipulate. Always resonate.
  </Layer1_Core>
  
  <Layer2_Context>
    The Neuro-Box is a 6-dimensional model of human drives:
    - SAFE (Dopamine): Remove fear, create trust
    - SPECIAL (GABA): Emotional validation
    - SMART (Acetylcholine): Problem-solving
    - SIGNIFICANT (Serotonin): Status elevation
    - SUPPORTED (Adrenaline): Validation + energy
    - SUPERIOR (Oxytocin): Vision + mastery
    
    Your responses should activate these in proper sequence for resonance.
  </Layer2_Context>
  
  <Layer3_Examples>
    [Progressive disclosure: Only loaded when needed]
    Example 1: User asks "How do I write better headlines?"
    
    ❌ BAD (Generic): "Use power words and create curiosity"
    
    ✅ GOOD (Neuro-Box): 
    "First activate SAFE: 'Here's a proven framework...'
    Then SMART: 'Start with the core problem they face...'
    Then SIGNIFICANT: 'This positions you as the authority...'
    Then SUPERIOR: 'The pattern most miss is...'"
  </Layer3_Examples>
  
  <Layer4_Constitutional>
    HARD CONSTRAINTS:
    - Never promise specific results (misleading)
    - Never sacrifice long-term trust for short-term wins
    - Never recommend manipulation tactics
    - If asked to help with deceptive marketing, refuse and explain why
    
    NORTH STAR CHECK:
    Before responding, ask: "Does this create Agentic Resonance or just compliance?"
  </Layer4_Constitutional>
  
  <ActivationTriggers>
    <Trigger type="always">This is the foundation - always active</Trigger>
  </ActivationTriggers>
</SuperSkill>
```

**Example Super-Skill (Capability):**
```xml
<SuperSkill>
  <Meta>
    <Name>email-sequence-architect</Name>
    <Type>capability</Type>
    <Version>1</Version>
    <TokenBudget>2000</TokenBudget>
  </Meta>
  
  <Layer1_Core>
    When building email sequences, use the 6-axis Neuro-Box progression.
    Each email activates 1-2 dimensions. Sequence builds complete activation.
  </Layer1_Core>
  
  <Layer2_Context>
    7-Email Sequence Template:
    Email 1 (SAFE): Remove FUD, establish credibility
    Email 2 (SPECIAL): Story that validates their situation
    Email 3 (SMART): Quick win / immediate value
    Email 4 (SIGNIFICANT): Show them the bigger vision
    Email 5 (SUPPORTED): Social proof + validation
    Email 6 (SUPERIOR): Deep insight they can't get elsewhere
    Email 7 (Offer): Natural invitation after complete activation
  </Layer2_Context>
  
  <Layer3_Examples>
    [Full 7-email example for cold list launch]
  </Layer3_Examples>
  
  <Layer4_Constitutional>
    CONSTRAINTS:
    - Never use manipulation tactics (fake scarcity, dark patterns)
    - Each email must provide standalone value
    - Unsubscribe must be easy and guilt-free
    - No bait-and-switch subject lines
  </Layer4_Constitutional>
  
  <ActivationTriggers>
    <Trigger type="keyword">email sequence</Trigger>
    <Trigger type="keyword">email campaign</Trigger>
    <Trigger type="keyword">nurture sequence</Trigger>
    <Trigger type="context">user mentions cold/warm list</Trigger>
  </ActivationTriggers>
</SuperSkill>
```

### 2.2 Dynamic Skill Assembly

**NEW EDGE FUNCTION: skill-assembler**
```typescript
// This replaces the static system prompt fetch
async function assembleSystemPrompt(
  userMessage: string,
  conversationHistory: Message[],
  context: ConversationContext
): Promise<string> {
  
  // 1. Always load foundation skills
  const foundationSkills = await getActiveSkills('foundation');
  
  // 2. Detect which capability skills to activate
  const triggeredSkills = await detectSkillTriggers(
    userMessage,
    conversationHistory,
    context
  );
  
  // 3. Assemble with progressive disclosure
  let assembledPrompt = '';
  let totalTokens = 0;
  const TOKEN_LIMIT = 8000; // Reserve space for conversation
  
  // Foundation first (always full depth)
  for (const skill of foundationSkills) {
    assembledPrompt += formatSkillLayers(skill, 4); // All 4 layers
    totalTokens += skill.token_budget;
  }
  
  // Capabilities second (adaptive depth based on budget)
  for (const skill of triggeredSkills) {
    const remainingBudget = TOKEN_LIMIT - totalTokens;
    const depth = calculateOptimalDepth(skill, remainingBudget);
    
    assembledPrompt += formatSkillLayers(skill, depth);
    totalTokens += estimateTokens(skill, depth);
    
    // Log usage
    await logSkillUsage(skill.id, depth, totalTokens);
  }
  
  // 3. Constitutional constraints (always included)
  const constraints = await getActiveConstraints();
  assembledPrompt += formatConstitutionalLayer(constraints);
  
  return assembledPrompt;
}
```

---

## Part 3: MCP Integration

### 3.1 Ref.tools Integration (Memory & Evolution Tracking)

**Purpose:** Store the system's entire evolution history in a queryable format.

**NEW MCP SERVER: ref-tools-mcp**

```typescript
// ref-tools-memory-structure.ts
interface EvolutionMemory {
  // What happened
  event_type: 'reflection' | 'prompt_update' | 'skill_creation' | 'constitutional_violation';
  timestamp: string;
  
  // Context
  trigger: string;
  scores: NeuroBoxScores;
  messages_analyzed: Message[];
  
  // Decision
  action_taken: string;
  reasoning: string;
  
  // Outcome
  before_state: SystemState;
  after_state: SystemState;
  performance_impact: number; // Did it actually help?
  
  // Learning
  pattern_detected?: string;
  similar_past_events?: string[]; // Links to similar events
  correction_applied?: string;
}

// Store every reflection in Ref.tools
async function storeReflectionInRef(
  reflection: ReflectionLog,
  messages: Message[],
  decision: Decision
) {
  const memory: EvolutionMemory = {
    event_type: 'reflection',
    timestamp: new Date().toISOString(),
    trigger: `Reflection run on ${messages.length} messages`,
    scores: reflection.neurobox_scores,
    messages_analyzed: messages,
    action_taken: decision.action,
    reasoning: decision.reasoning,
    before_state: await captureSystemState(),
    after_state: null, // Updated after change applied
    performance_impact: null // Measured in next reflection
  };
  
  // Store in Ref.tools with semantic search capability
  await refTools.store({
    collection: 'system-evolution',
    document: memory,
    metadata: {
      tags: [decision.action, ...reflection.patterns_detected],
      searchable: true
    }
  });
}

// Query past similar situations before making decisions
async function consultEvolutionMemory(
  currentScores: NeuroBoxScores,
  currentPatterns: string[]
): Promise<HistoricalInsight[]> {
  
  // Semantic search for similar past situations
  const similarEvents = await refTools.search({
    collection: 'system-evolution',
    query: `Similar scores and patterns to current situation`,
    filters: {
      event_type: ['reflection', 'prompt_update']
    },
    limit: 5
  });
  
  // Analyze outcomes of past decisions
  return similarEvents.map(event => ({
    what_happened: event.action_taken,
    why: event.reasoning,
    outcome: event.performance_impact,
    lesson: event.performance_impact > 0 
      ? 'This type of change helped'
      : 'This type of change hurt'
  }));
}
```

**Integration into Reflection Loop:**
```typescript
// UPGRADED: reflection-loop with memory consultation
async function runReflection() {
  // ... existing evaluation code ...
  
  // NEW: Before deciding action, consult memory
  const historicalInsights = await consultEvolutionMemory(
    currentScores,
    patternsDetected
  );
  
  // Include historical context in decision
  const decision = await decideAction(
    currentScores,
    patternsDetected,
    historicalInsights // NEW: Learn from past
  );
  
  // Store this reflection for future learning
  await storeReflectionInRef(reflection, messages, decision);
}
```

### 3.2 Exa.ai Integration (Knowledge Augmentation)

**Purpose:** When system encounters knowledge gaps, search for authoritative current information.

**NEW MCP SERVER: exa-ai-mcp**

```typescript
// Knowledge gap detection
async function detectKnowledgeGap(
  userMessage: string,
  assistantResponse: string,
  confidence: number
): Promise<boolean> {
  // Detect phrases indicating uncertainty
  const uncertaintyMarkers = [
    'I don\'t have current information',
    'As of my last update',
    'I\'m not sure about recent',
    'You might want to verify'
  ];
  
  const hasUncertainty = uncertaintyMarkers.some(
    marker => assistantResponse.includes(marker)
  );
  
  return hasUncertainty || confidence < 0.7;
}

// Search Exa for authoritative sources
async function augmentKnowledge(topic: string, context: string) {
  const results = await exa.search({
    query: topic,
    type: 'neural', // Use semantic search
    numResults: 3,
    category: 'research paper' // Prioritize authoritative sources
  });
  
  // Extract key insights
  const insights = await Promise.all(
    results.map(async (result) => ({
      source: result.url,
      title: result.title,
      summary: await exa.getContent(result.id),
      relevance: result.score
    }))
  );
  
  return insights;
}

// Integration example
async function chatWithKnowledgeAugmentation(message: string) {
  // First pass: Generate response
  const response = await claude.messages.create({...});
  
  // Detect if knowledge gap exists
  const hasGap = await detectKnowledgeGap(
    message,
    response.content[0].text,
    response.confidence
  );
  
  if (hasGap) {
    // Augment knowledge from Exa
    const topic = extractTopic(message);
    const insights = await augmentKnowledge(topic, message);
    
    // Second pass: Enhanced response with current knowledge
    const enhancedResponse = await claude.messages.create({
      system: `${systemPrompt}\n\nRecent authoritative sources:\n${formatInsights(insights)}`,
      messages: [...history, {role: 'user', content: message}]
    });
    
    return {
      response: enhancedResponse,
      sources: insights.map(i => i.source),
      augmented: true
    };
  }
  
  return {
    response,
    augmented: false
  };
}
```

---

## Part 4: Self-Annealing Healing System

### 4.1 Proactive Pattern Detection

**NEW TABLE: pattern_library**
```sql
CREATE TABLE pattern_library (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  pattern_type TEXT CHECK (pattern_type IN (
    'failure_mode',      -- Recurring failures
    'drift_indicator',   -- Signs of mission drift
    'quality_decline',   -- Performance degradation
    'constitutional_risk' -- Risk of violating constraints
  )),
  pattern_signature JSONB NOT NULL,  -- What the pattern looks like
  detection_threshold INTEGER,        -- How many occurrences trigger
  
  -- Healing response
  healing_action TEXT,
  skill_patch_id UUID REFERENCES super_skills(id),
  constitutional_patch_id UUID REFERENCES constitutional_constraints(id),
  
  effectiveness_score NUMERIC(3,2),
  times_detected INTEGER DEFAULT 0,
  times_healed INTEGER DEFAULT 0,
  
  created_at TIMESTAMPTZ DEFAULT NOW(),
  is_active BOOLEAN DEFAULT true
);
```

**Example Patterns:**
```json
{
  "shallow_responses_pattern": {
    "signature": {
      "neurobox_dimension": "SMART",
      "score_range": [1, 2],
      "consecutive_occurrences": 3
    },
    "healing_action": "Activate deeper reasoning skill + add examples requirement",
    "skill_patch_id": "uuid-of-deep-reasoning-skill"
  },
  
  "scope_drift_pattern": {
    "signature": {
      "keywords": ["off-topic", "outside marketing", "not in scope"],
      "consecutive_occurrences": 2
    },
    "healing_action": "Strengthen constitutional constraints + add topic validation",
    "constitutional_patch_id": "uuid-of-scope-constraint"
  },
  
  "manipulation_risk_pattern": {
    "signature": {
      "neurobox_dimension": "SAFE",
      "score_below": 2,
      "combined_with": {
        "dimension": "SIGNIFICANT",
        "score_above": 4
      }
    },
    "healing_action": "CRITICAL: Forcing status without safety = manipulation. Rebalance.",
    "constitutional_patch_id": "uuid-of-resonance-constraint"
  }
}
```

### 4.2 Self-Healing Edge Function

**NEW EDGE FUNCTION: self-healing**
```typescript
async function detectAndHeal() {
  // 1. Analyze recent reflections for patterns
  const recentReflections = await getRecentReflections(20);
  
  // 2. Check against known pattern library
  const detectedPatterns = await matchPatterns(
    recentReflections,
    await getActivePatterns()
  );
  
  for (const pattern of detectedPatterns) {
    // 3. Check if threshold reached
    if (pattern.occurrences >= pattern.detection_threshold) {
      console.log(`🔧 HEALING: Detected pattern ${pattern.pattern_type}`);
      
      // 4. Apply healing action
      switch (pattern.healing_action_type) {
        case 'skill_patch':
          await applySkillPatch(pattern.skill_patch_id);
          break;
        case 'constitutional_patch':
          await applyConstitutionalPatch(pattern.constitutional_patch_id);
          break;
        case 'emergency_rollback':
          await emergencyRollback(pattern.rollback_to_version);
          break;
      }
      
      // 5. Log healing event
      await logHealingEvent({
        pattern_id: pattern.id,
        action_taken: pattern.healing_action,
        timestamp: new Date(),
        triggered_by: recentReflections.slice(0, 3).map(r => r.id)
      });
      
      // 6. Monitor effectiveness in next cycle
      pattern.times_healed++;
      await updatePattern(pattern);
    }
  }
}

// Run self-healing check every N reflections
// This is MORE frequent than reflection loop
// Think of it as the "immune system" vs "periodic checkup"
```

### 4.3 Recursive Self-Correction

**The concept:** System learns which corrections work and which don't.

```typescript
interface HealingOutcome {
  pattern_id: string;
  healing_applied: string;
  before_avg_score: number;
  after_avg_score: number;
  improvement: number;
  
  // Meta-learning
  was_effective: boolean;
  confidence: number;
}

// Track healing effectiveness
async function measureHealingEffectiveness(
  healing_event_id: string
): Promise<HealingOutcome> {
  
  const event = await getHealingEvent(healing_event_id);
  
  // Compare scores before and after healing
  const beforeScores = await getAverageScores({
    time_range: 'before_healing',
    event_id: healing_event_id
  });
  
  const afterScores = await getAverageScores({
    time_range: 'after_healing',
    event_id: healing_event_id,
    sample_size: 10 // Need enough data
  });
  
  const improvement = afterScores.overall - beforeScores.overall;
  const was_effective = improvement > 0.3; // Meaningful improvement
  
  // If healing didn't work, mark pattern for revision
  if (!was_effective) {
    await flagPatternForRevision(event.pattern_id, {
      reason: 'Healing applied but scores did not improve',
      attempted_action: event.healing_action,
      suggestion: 'Consider alternative healing approach'
    });
  }
  
  return {
    pattern_id: event.pattern_id,
    healing_applied: event.healing_action,
    before_avg_score: beforeScores.overall,
    after_avg_score: afterScores.overall,
    improvement,
    was_effective,
    confidence: calculateConfidence(afterScores.sample_size)
  };
}
```

---

## Part 5: Enhanced Memory Architecture

### 5.1 Four Memory Types (Beyond Simple Logging)

```sql
-- 1. EPISODIC MEMORY (Specific interactions)
CREATE TABLE episodic_memory (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  conversation_id UUID,
  user_id UUID,
  
  -- The interaction
  user_message TEXT,
  assistant_response TEXT,
  neurobox_activation JSONB, -- Which dimensions were activated
  
  -- Emotional/contextual markers
  user_sentiment TEXT,
  urgency_level INTEGER,
  topic_classification TEXT[],
  
  -- Outcome
  user_satisfaction INTEGER, -- If we can detect it
  follow_up_question BOOLEAN, -- Did they ask again? (sign of incomplete)
  
  created_at TIMESTAMPTZ DEFAULT NOW(),
  
  -- Indexing for pattern detection
  embedding VECTOR(1536) -- For semantic search
);

-- 2. SEMANTIC MEMORY (Extracted patterns and principles)
CREATE TABLE semantic_memory (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  
  -- What was learned
  principle_type TEXT CHECK (principle_type IN (
    'user_preference',    -- "This user prefers bullet points"
    'effective_pattern',  -- "When X, doing Y works well"
    'failure_pattern',    -- "Avoid Z in context W"
    'domain_knowledge'    -- "Learned: concept X means Y"
  )),
  
  principle_text TEXT,
  confidence NUMERIC(3,2),
  
  -- Evidence
  derived_from_episodes UUID[], -- Array of episodic_memory IDs
  supporting_reflections UUID[], -- Array of reflection_log IDs
  times_validated INTEGER DEFAULT 1,
  times_contradicted INTEGER DEFAULT 0,
  
  -- Lifecycle
  created_at TIMESTAMPTZ DEFAULT NOW(),
  last_validated TIMESTAMPTZ,
  is_active BOOLEAN DEFAULT true,
  
  embedding VECTOR(1536)
);

-- 3. PROCEDURAL MEMORY (Learned workflows)
CREATE TABLE procedural_memory (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  
  -- The workflow
  workflow_name TEXT,
  workflow_type TEXT CHECK (workflow_type IN (
    'response_pattern',   -- How to respond to X
    'skill_sequence',     -- Which skills to chain
    'correction_flow',    -- How to self-correct
    'escalation_path'     -- When to escalate to human
  )),
  
  -- Steps
  steps JSONB, -- Array of {action, condition, next_step}
  
  -- Performance
  success_rate NUMERIC(3,2),
  times_executed INTEGER DEFAULT 0,
  average_outcome_score NUMERIC(3,2),
  
  created_at TIMESTAMPTZ DEFAULT NOW(),
  is_active BOOLEAN DEFAULT true
);

-- 4. CONSTITUTIONAL MEMORY (Core values and constraints)
-- This already exists in constitutional_constraints table
-- But let's add violation tracking

CREATE TABLE constitutional_memory (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  constraint_id UUID REFERENCES constitutional_constraints(id),
  
  -- Violation record
  violation_type TEXT,
  violation_context TEXT,
  how_it_was_caught TEXT, -- 'reflection' | 'pattern_detection' | 'human_flagged'
  
  -- Correction
  correction_applied TEXT,
  correction_effectiveness NUMERIC(3,2),
  
  -- Learning
  new_safeguard_created BOOLEAN,
  safeguard_id UUID, -- Reference to new pattern or constraint
  
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 5.2 Memory Integration in Decision-Making

```typescript
// When making ANY decision, consult all memory types
async function makeInformedDecision(
  context: DecisionContext
): Promise<Decision> {
  
  // 1. Episodic: Have we seen this exact situation before?
  const similarEpisodes = await queryEpisodicMemory({
    semantic_similarity: context.user_message,
    limit: 3
  });
  
  // 2. Semantic: What principles apply here?
  const relevantPrinciples = await querySemanticMemory({
    context_type: context.topic_classification,
    min_confidence: 0.7
  });
  
  // 3. Procedural: Is there a learned workflow for this?
  const applicableWorkflows = await queryProceduralMemory({
    workflow_type: context.decision_type,
    min_success_rate: 0.6
  });
  
  // 4. Constitutional: Any constraints that apply?
  const constraints = await getActiveConstitutionalConstraints();
  
  // 5. Synthesize into decision
  const decision = await synthesizeDecision({
    episodic: similarEpisodes,
    semantic: relevantPrinciples,
    procedural: applicableWorkflows,
    constitutional: constraints,
    current_context: context
  });
  
  return decision;
}
```

---

## Part 6: Implementation Roadmap

### Phase 1: Foundation (Week 1-2)
- [ ] Migrate existing database to include Neuro-Box dimensions
- [ ] Create constitutional_constraints table
- [ ] Implement basic Neuro-Box evaluation (replace old rubric)
- [ ] Test with existing conversations

### Phase 2: Super-Skills (Week 3-4)
- [ ] Design super_skills table structure
- [ ] Convert current system prompt to modular skills
- [ ] Build skill-assembler edge function
- [ ] Implement skill_usage_log tracking

### Phase 3: MCP Integration (Week 5-6)
- [ ] Set up Ref.tools MCP server
- [ ] Integrate evolution memory storage
- [ ] Set up Exa.ai MCP server
- [ ] Implement knowledge gap detection

### Phase 4: Self-Healing (Week 7-8)
- [ ] Create pattern_library table
- [ ] Define initial failure patterns
- [ ] Build self-healing edge function
- [ ] Implement healing effectiveness measurement

### Phase 5: Memory Layer (Week 9-10)
- [ ] Create all four memory tables
- [ ] Implement memory population from existing data
- [ ] Build memory query functions
- [ ] Integrate memory consultation into decision-making

### Phase 6: Integration & Testing (Week 11-12)
- [ ] End-to-end testing of complete system
- [ ] Performance optimization
- [ ] Admin dashboard for monitoring
- [ ] Documentation

---

## Part 7: Key Architectural Decisions

### 7.1 Why Supabase (Free Tier) > Firebase

**Supabase Advantages:**
1. **Postgres = Complex Queries:** Need JOINs, aggregations, vector search
2. **Edge Functions = Deno:** Better TypeScript support than Cloud Functions
3. **Built-in Vector Search:** For semantic memory (pgvector extension)
4. **MCP Support:** Already integrated via MCP server
5. **Free Tier Generosity:**
   - 500MB database (plenty for text)
   - 50,000 monthly active users
   - 2GB file storage
   - Unlimited API requests

**Firebase Would Require:**
- Complex denormalization for NoSQL
- Separate vector search service (Pinecone/Weaviate)
- Less sophisticated querying
- Cloud Functions cold starts

### 7.2 MCP Strategy: Lean & Purpose-Built

**DON'T:** Integrate every possible MCP server
**DO:** Only integrate MCPs with clear purpose

Our lean stack:
1. **Supabase MCP** (already have) - Database operations
2. **Ref.tools MCP** - Evolution memory & semantic search
3. **Exa.ai MCP** - Knowledge augmentation for gaps

**Why these three?**
- Supabase: Core data persistence
- Ref.tools: Historical learning & pattern detection
- Exa.ai: Current knowledge when needed

**Explicitly NOT adding:**
- Filesystem MCP (Supabase storage sufficient)
- Email MCP (not needed for core system)
- Calendar MCP (not needed for core system)

### 7.3 Self-Annealing vs Traditional Self-Improvement

**Traditional (Kashef's current system):**
```
Problem occurs → Wait for reflection → Evaluate → Update → Hope it's better
```

**Self-Annealing (Our upgrade):**
```
Pattern detected → Immediate healing → Measure outcome → Learn from healing effectiveness
```

**Key difference:** Proactive vs Reactive

**Example:**
- Traditional: After 10 shallow responses, reflection triggers update
- Self-Annealing: After 3 shallow responses, pattern detected, skill patch applied, effectiveness measured

---

## Part 8: Constitutional Safeguards

### 8.1 Anti-Drift Mechanisms

```typescript
// Run before EVERY prompt update
async function constitutionalReview(
  proposedUpdate: string,
  reason: string
): Promise<ConstitutionalReview> {
  
  const constraints = await getActiveConstraints();
  
  // Check proposed update against ALL constitutional constraints
  const violations = [];
  
  for (const constraint of constraints) {
    const check = await evaluateConstitutionalCompliance({
      proposed_change: proposedUpdate,
      constraint: constraint.constraint_text,
      current_mission: await getNorthStar()
    });
    
    if (check.violates) {
      violations.push({
        constraint_id: constraint.id,
        constraint_type: constraint.constraint_type,
        violation_details: check.details,
        severity: constraint.priority
      });
    }
  }
  
  // If ANY critical violation, BLOCK the update
  if (violations.some(v => v.severity === 'critical')) {
    await escalateToHuman({
      reason: 'Proposed update violates critical constitutional constraint',
      violations,
      proposed_update: proposedUpdate,
      original_reason: reason
    });
    
    return {
      approved: false,
      violations,
      action: 'blocked_for_human_review'
    };
  }
  
  return {
    approved: true,
    violations: [], // Or just warnings
    action: 'proceed'
  };
}
```

### 8.2 Alignment Verification

```typescript
// Periodically verify system is still aligned with North Star
async function verifyAlignment() {
  const currentCapabilities = await getAllActiveSkills();
  const currentConstraints = await getAllActiveConstraints();
  const recentBehavior = await getRecentReflections(50);
  
  // Ask: "Is this system still serving its original purpose?"
  const alignmentCheck = await claude.messages.create({
    model: 'claude-sonnet-4-20250514',
    system: ALIGNMENT_VERIFIER_PROMPT,
    messages: [{
      role: 'user',
      content: `
        Analyze this AI system's evolution:
        
        Original North Star: ${ORIGINAL_NORTH_STAR}
        
        Current Capabilities: ${JSON.stringify(currentCapabilities, null, 2)}
        Current Constraints: ${JSON.stringify(currentConstraints, null, 2)}
        Recent Behavior Summary: ${summarizeBehavior(recentBehavior)}
        
        Questions:
        1. Is the system still serving the North Star?
        2. Has there been any mission drift?
        3. Are there new capabilities that don't align?
        4. What corrections would you recommend?
      `
    }]
  });
  
  // Log alignment report
  await logAlignmentReport(alignmentCheck);
  
  // If drift detected, trigger healing
  if (alignmentCheck.drift_detected) {
    await triggerAlignmentCorrection(alignmentCheck.recommendations);
  }
}

// Run this weekly
```

---

## Part 9: Admin Dashboard Requirements

### 9.1 Key Visualizations

```typescript
interface DashboardViews {
  // 1. Neuro-Box Radar Chart
  neurobox_performance: {
    dimensions: ['SAFE', 'SPECIAL', 'SMART', 'SIGNIFICANT', 'SUPPORTED', 'SUPERIOR'],
    current_scores: number[],
    historical_trend: number[][], // Last 30 days
    target_scores: number[]
  },
  
  // 2. Evolution Timeline
  system_evolution: {
    events: Array<{
      timestamp: string,
      type: 'reflection' | 'update' | 'healing' | 'violation',
      before_score: number,
      after_score: number,
      reason: string
    }>,
    annotations: string[] // Key moments
  },
  
  // 3. Skill Activation Heatmap
  skill_usage: {
    skills: string[],
    usage_frequency: number[][],  // Skill × Time
    effectiveness: number[][]     // Skill × Effectiveness
  },
  
  // 4. Constitutional Compliance
  constitutional_health: {
    constraints: Array<{
      name: string,
      violation_count: number,
      last_violation: string,
      status: 'healthy' | 'warning' | 'critical'
    }>
  },
  
  // 5. Memory Growth
  memory_stats: {
    episodic_count: number,
    semantic_principles: number,
    procedural_workflows: number,
    memory_quality_score: number
  },
  
  // 6. Healing Effectiveness
  healing_stats: {
    patterns_detected: number,
    healings_applied: number,
    successful_healings: number,
    average_improvement: number
  }
}
```

---

## Part 10: Critical Success Metrics

### How We'll Know This Works

```typescript
interface SuccessMetrics {
  // 1. Performance Improvement
  neurobox_trend: {
    metric: 'Average Neuro-Box score over time',
    target: 'Continuous improvement, no regression',
    current: number,
    trend: 'improving' | 'stable' | 'declining'
  },
  
  // 2. Self-Healing Effectiveness
  healing_success_rate: {
    metric: 'Percentage of healings that improve scores',
    target: '> 70%',
    current: number
  },
  
  // 3. Constitutional Compliance
  drift_prevention: {
    metric: 'Zero critical constitutional violations',
    target: '0 violations per month',
    current: number
  },
  
  // 4. Autonomy Level
  human_intervention_rate: {
    metric: 'Percentage of decisions requiring human review',
    target: '< 5%',
    current: number
  },
  
  // 5. Memory Utilization
  memory_application_rate: {
    metric: 'Percentage of decisions that use memory',
    target: '> 80%',
    current: number
  },
  
  // 6. Knowledge Coverage
  knowledge_gap_rate: {
    metric: 'Percentage of queries triggering Exa search',
    target: '< 10%',
    current: number
  }
}
```

---

## Conclusion

This integration transforms Kashef's self-improving architecture from a reactive evaluation system into a **proactive, self-annealing organism** that:

1. **Evaluates** using human-aligned Neuro-Box dimensions
2. **Remembers** across four memory types
3. **Learns** from its own evolution history
4. **Heals** before failures compound
5. **Stays aligned** through constitutional governance
6. **Augments knowledge** when needed
7. **Assembles capabilities** dynamically

The result: An AI system that genuinely improves itself while maintaining unwavering alignment with its North Star.

**Next Step:** Review this blueprint and decide which phase to start with.

---

**Related Documents:**
- NEUROBOX_CONSTITUTION.md (Core principles)
- SUPER_SKILLS_LIBRARY.md (Skill definitions)
- MCP_INTEGRATION_GUIDE.md (MCP setup details)
- HEALING_PATTERNS_LIBRARY.md (Pattern definitions)
