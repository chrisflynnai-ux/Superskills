# Freedomation Full-Stack Integration
# FastAPI Backend + Next.js/CopilotKit Frontend

# ============================================================================
# BACKEND: FastAPI Server (backend/main.py)
# ============================================================================

"""
FastAPI backend serving ULTRAMIND Pydantic AI agents
Connects to Freedomation/Flowgrams frontend via CopilotKit
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import asyncio

# Import our Transformational Writer agent
from transformational_writer_pydantic import (
    generate_carousel_with_annealing,
    TransformationalWriterOutput,
    MMAReview
)

# Initialize FastAPI
app = FastAPI(
    title="Freedomation AI Backend",
    description="ULTRAMIND Agents powered by Pydantic AI",
    version="1.0.0"
)

# CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://freedomation.ai"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# REQUEST/RESPONSE MODELS
# ============================================================================

class CarouselRequest(BaseModel):
    """Request to generate carousel"""
    hook: str
    platform: str = "LinkedIn"
    voice_tone: str = "visionary"
    num_slides: int = 10
    brand_context: str | None = "Vision Capitalist"

class CarouselResponse(BaseModel):
    """Response with carousel and quality metrics"""
    success: bool
    carousel: TransformationalWriterOutput
    mma_review: MMAReview
    attempts: int
    message: str

class SkillExecutionRequest(BaseModel):
    """Generic skill execution request (for Flowgrams)"""
    skill_id: str
    inputs: Dict[str, Any]
    quality_threshold: float = 8.0
    max_attempts: int = 3

# ============================================================================
# API ROUTES
# ============================================================================

@app.get("/")
async def root():
    """Health check"""
    return {
        "status": "online",
        "service": "Freedomation AI Backend",
        "skills_available": [
            "transformational_writer",
            "strategic_mentor",
            "product_creator"
        ]
    }

@app.post("/api/carousel/generate", response_model=CarouselResponse)
async def generate_carousel_endpoint(request: CarouselRequest):
    """
    Generate carousel with self-annealing quality loop
    
    Example:
    ```
    POST /api/carousel/generate
    {
        "hook": "Without Vision the programmers perish",
        "platform": "LinkedIn",
        "num_slides": 10
    }
    ```
    """
    try:
        # Execute with self-annealing
        output, review, attempts = await generate_carousel_with_annealing(
            hook=request.hook,
            max_attempts=3,
            quality_threshold=8.0
        )
        
        return CarouselResponse(
            success=True,
            carousel=output,
            mma_review=review,
            attempts=attempts,
            message=f"Carousel generated in {attempts} attempt(s) with score {review.overall_score:.1f}/10"
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Carousel generation failed: {str(e)}"
        )

@app.post("/api/skills/execute")
async def execute_skill(request: SkillExecutionRequest):
    """
    Generic skill execution endpoint (for Flowgrams visual workflows)
    
    This is called when user executes a node in Flowgrams
    """
    try:
        skill_id = request.skill_id
        inputs = request.inputs
        
        # Route to appropriate skill
        if skill_id == "transformational_writer":
            output, review, attempts = await generate_carousel_with_annealing(
                hook=inputs.get("hook", ""),
                max_attempts=request.max_attempts,
                quality_threshold=request.quality_threshold
            )
            
            return {
                "success": True,
                "skill_id": skill_id,
                "output": output.model_dump(),
                "quality": {
                    "score": review.overall_score,
                    "verdict": review.verdict,
                    "attempts": attempts
                }
            }
        
        elif skill_id == "strategic_mentor":
            # TODO: Implement Strategic Mentor agent
            return {
                "success": False,
                "error": "Strategic Mentor not yet implemented"
            }
        
        else:
            raise HTTPException(
                status_code=404,
                detail=f"Skill '{skill_id}' not found"
            )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Skill execution failed: {str(e)}"
        )

@app.get("/api/skills/list")
async def list_skills():
    """List all available ULTRAMIND skills"""
    return {
        "skills": [
            {
                "id": "transformational_writer",
                "name": "Transformational Writer",
                "description": "Generate viral carousels from hooks",
                "status": "active",
                "inputs": ["hook", "platform", "num_slides"],
                "outputs": ["carousel_slides", "quality_scores"]
            },
            {
                "id": "strategic_mentor",
                "name": "Strategic Business Mentor",
                "description": "Strategic coaching and guidance",
                "status": "coming_soon",
                "inputs": ["situation", "goal"],
                "outputs": ["strategy", "action_steps"]
            },
            {
                "id": "product_creator",
                "name": "Product Creation Genius",
                "description": "End-to-end product development",
                "status": "coming_soon",
                "inputs": ["market", "audience", "value_prop"],
                "outputs": ["product_spec", "positioning", "pricing"]
            }
        ]
    }

# ============================================================================
# COPILOTKIT INTEGRATION ENDPOINT
# ============================================================================

@app.post("/api/copilotkit")
async def copilotkit_endpoint(request: Dict[str, Any]):
    """
    CopilotKit backend endpoint
    Handles streaming AI interactions from frontend
    """
    message = request.get("message", "")
    agent = request.get("agent", "transformational_writer")
    context = request.get("context", {})
    
    # Route based on agent type
    if agent == "transformational_writer":
        # Extract hook from message
        hook = message
        
        # Generate carousel
        output, review, attempts = await generate_carousel_with_annealing(
            hook=hook,
            max_attempts=3,
            quality_threshold=8.0
        )
        
        return {
            "response": {
                "type": "carousel",
                "data": output.model_dump(),
                "quality": review.model_dump(),
                "attempts": attempts
            },
            "status": "complete"
        }
    
    else:
        return {
            "response": {
                "type": "text",
                "data": f"Agent '{agent}' not yet implemented"
            },
            "status": "error"
        }

# ============================================================================
# FRONTEND: Next.js + CopilotKit (frontend/app/page.tsx)
# ============================================================================

"""
TypeScript/React frontend for Freedomation
Uses CopilotKit for AI interaction layer
"""

FRONTEND_CODE = '''
// frontend/app/page.tsx

"use client";

import { CopilotKit } from "@copilotkit/react-core";
import { CopilotSidebar } from "@copilotkit/react-ui";
import "@copilotkit/react-ui/styles.css";
import { useState } from "react";

interface Slide {
  slide_number: number;
  sound_bite: string;
  supporting_insight: string;
}

interface CarouselOutput {
  carousel_slides: Slide[];
  viral_potential: string;
  hook_strength: number;
}

export default function FreedomationHome() {
  const [hook, setHook] = useState("");
  const [carousel, setCarousel] = useState<CarouselOutput | null>(null);
  const [loading, setLoading] = useState(false);
  const [quality, setQuality] = useState<any>(null);

  const generateCarousel = async () => {
    setLoading(true);
    
    try {
      const response = await fetch("http://localhost:8000/api/carousel/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          hook,
          platform: "LinkedIn",
          num_slides: 10,
          brand_context: "Vision Capitalist"
        })
      });
      
      const data = await response.json();
      
      if (data.success) {
        setCarousel(data.carousel);
        setQuality(data.mma_review);
      }
    } catch (error) {
      console.error("Generation failed:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <CopilotKit
      runtimeUrl="/api/copilotkit"
      agent="transformational_writer"
    >
      <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
        
        {/* Header */}
        <header className="p-6 border-b border-purple-500/30">
          <h1 className="text-4xl font-bold text-white">
            🧠 Freedomation
          </h1>
          <p className="text-purple-300 mt-2">
            Visual Agentic Workflows powered by ULTRAMIND
          </p>
        </header>

        <div className="flex">
          
          {/* Main Canvas */}
          <main className="flex-1 p-8">
            
            {/* Input Section */}
            <div className="bg-white/10 backdrop-blur-lg rounded-xl p-6 mb-6">
              <h2 className="text-2xl text-white mb-4">
                Transformational Writer
              </h2>
              
              <textarea
                value={hook}
                onChange={(e) => setHook(e.target.value)}
                placeholder="Enter your ultimate hook... (e.g., 'Without Vision the programmers perish')"
                className="w-full h-32 bg-white/5 border border-purple-500/30 rounded-lg p-4 text-white placeholder-purple-300/50"
              />
              
              <button
                onClick={generateCarousel}
                disabled={loading || !hook}
                className="mt-4 px-6 py-3 bg-purple-600 hover:bg-purple-700 disabled:bg-gray-600 text-white rounded-lg font-semibold transition-colors"
              >
                {loading ? "🔄 Generating..." : "✨ Generate Carousel"}
              </button>
            </div>

            {/* Quality Metrics */}
            {quality && (
              <div className="bg-white/10 backdrop-blur-lg rounded-xl p-6 mb-6">
                <h3 className="text-xl text-white mb-4">Quality Metrics</h3>
                <div className="grid grid-cols-3 gap-4">
                  <div className="text-center">
                    <div className="text-3xl font-bold text-purple-400">
                      {quality.overall_score.toFixed(1)}/10
                    </div>
                    <div className="text-sm text-purple-300">Overall Score</div>
                  </div>
                  <div className="text-center">
                    <div className="text-3xl font-bold text-green-400">
                      {quality.verdict}
                    </div>
                    <div className="text-sm text-purple-300">Verdict</div>
                  </div>
                  <div className="text-center">
                    <div className="text-3xl font-bold text-blue-400">
                      {carousel?.viral_potential}
                    </div>
                    <div className="text-sm text-purple-300">Viral Potential</div>
                  </div>
                </div>
              </div>
            )}

            {/* Carousel Preview */}
            {carousel && (
              <div className="bg-white/10 backdrop-blur-lg rounded-xl p-6">
                <h3 className="text-xl text-white mb-4">
                  📱 Carousel Preview ({carousel.carousel_slides.length} slides)
                </h3>
                
                <div className="grid grid-cols-2 gap-4">
                  {carousel.carousel_slides.map((slide) => (
                    <div
                      key={slide.slide_number}
                      className="bg-gradient-to-br from-purple-600/20 to-blue-600/20 border border-purple-500/30 rounded-lg p-4"
                    >
                      <div className="text-sm text-purple-300 mb-2">
                        Slide {slide.slide_number}
                      </div>
                      <div className="text-lg font-bold text-white mb-2">
                        {slide.sound_bite}
                      </div>
                      <div className="text-sm text-purple-200">
                        {slide.supporting_insight}
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

          </main>

          {/* CopilotKit Sidebar */}
          <CopilotSidebar
            labels={{
              title: "ULTRAMIND Assistant",
              initial: "Ready to transform your ideas...",
            }}
            defaultOpen={true}
            className="w-96"
          >
            <div className="p-4 text-white">
              <p className="text-sm text-purple-300">
                Talk to ULTRAMIND to generate carousels, get strategic advice, 
                or create products. Type your hook or question.
              </p>
            </div>
          </CopilotSidebar>

        </div>
      </div>
    </CopilotKit>
  );
}
'''

# ============================================================================
# DEPLOYMENT INSTRUCTIONS
# ============================================================================

DEPLOYMENT_README = """
# Freedomation Deployment Guide

## Backend Setup

1. Install dependencies:
```bash
cd backend
pip install fastapi uvicorn pydantic-ai anthropic
```

2. Set environment variables:
```bash
export ANTHROPIC_API_KEY="your-api-key"
```

3. Run FastAPI server:
```bash
uvicorn main:app --reload --port 8000
```

Backend runs at: http://localhost:8000

## Frontend Setup

1. Create Next.js app:
```bash
npx create-next-app@latest freedomation-frontend
cd freedomation-frontend
```

2. Install CopilotKit:
```bash
npm install @copilotkit/react-core @copilotkit/react-ui
```

3. Copy frontend code to app/page.tsx

4. Run Next.js:
```bash
npm run dev
```

Frontend runs at: http://localhost:3000

## Testing

1. Open http://localhost:3000
2. Enter hook: "Without Vision the programmers perish"
3. Click "Generate Carousel"
4. Watch self-annealing in action
5. See quality scores and carousel preview

## Production Deployment

Backend (FastAPI):
- Deploy to Railway, Render, or Fly.io
- Set ANTHROPIC_API_KEY in environment
- Update CORS origins

Frontend (Next.js):
- Deploy to Vercel
- Update API_URL to production backend
- Configure CopilotKit runtime URL

## Environment Variables

Backend (.env):
```
ANTHROPIC_API_KEY=sk-ant-...
ALLOWED_ORIGINS=https://freedomation.ai
```

Frontend (.env.local):
```
NEXT_PUBLIC_API_URL=https://api.freedomation.ai
```
"""

# ============================================================================
# RUN THE SERVER
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    print("=" * 60)
    print("🚀 FREEDOMATION AI BACKEND")
    print("=" * 60)
    print()
    print("Starting FastAPI server...")
    print("Backend: http://localhost:8000")
    print("Docs: http://localhost:8000/docs")
    print()
    print("Available endpoints:")
    print("  POST /api/carousel/generate")
    print("  POST /api/skills/execute")
    print("  GET  /api/skills/list")
    print("  POST /api/copilotkit")
    print()
    print("=" * 60)
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
