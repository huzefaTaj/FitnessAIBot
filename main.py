from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os
from typing import Optional

app = FastAPI(title="Fitness AI Q&A API", description="AI-powered Q&A system for fitness questions")

# Pydantic models for request and response
class QuestionRequest(BaseModel):
    question: str

class QuestionResponse(BaseModel):
    question: str
    answer: str
    model_used: str

# Initialize OpenAI client with API key from environment variable
STATIC_API_KEY = os.getenv("OPENAI_API_KEY")
if not STATIC_API_KEY:
    print("Warning: OPENAI_API_KEY environment variable not set. Please set it to use the API.")
    print("You can set it by running: set OPENAI_API_KEY=your-api-key-here")
    client = None
else:
    client = OpenAI(api_key=STATIC_API_KEY)

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Fitness AI Q&A API",
        "description": "Send questions and get AI-powered answers",
        "endpoints": {
            "/ask": "POST - Send a question with your OpenAI API key",
            "/health": "GET - Check API health"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy", 
        "openai_configured": STATIC_API_KEY is not None,
        "message": "API is running" if STATIC_API_KEY else "API is running but OpenAI key not configured"
    }

@app.post("/ask", response_model=QuestionResponse)
async def ask_question(request: QuestionRequest):
    """
    Send a question to OpenAI and get an AI response
    
    Args:
        request: QuestionRequest containing the question
    
    Returns:
        QuestionResponse with the AI's answer
    """
    try:
        # Check if OpenAI client is configured
        if not client:
            raise HTTPException(
                status_code=400,
                detail="OpenAI API key not configured. Please set the OPENAI_API_KEY environment variable."
            )
        
        # Create the prompt for AI fitness coach with comprehensive knowledge
        system_prompt = """You are an expert AI Fitness Coach with comprehensive knowledge of fitness, nutrition, exercise science, and wellness. You have access to the user's specific workout routine and body measurements, and you're here to guide them towards their fitness goals.

        YOUR ROLE AS AI FITNESS COACH:
        - Provide personalized fitness advice based on their current routine and body stats
        - Create customized workout plans and modifications
        - Offer nutrition guidance and meal planning tips
        - Give motivation and progress tracking advice
        - Suggest exercise variations and progression strategies
        - Help with goal setting and achievement planning
        - Provide recovery and injury prevention tips
        - Answer questions about fitness equipment and techniques

        USER'S BODY STATS:
        Height: 175 cm
        Weight: 72 kg
        BMI: ~23.5 (healthy range)

        USER'S CURRENT WORKOUT ROUTINE:
        Monday: Pull-ups (4×10 reps, ~120 cal), Squats (3×15 reps, ~90 cal), Plank (3×1 min, ~40 cal) - Total: 250 calories
        Tuesday: Push-ups (4×20 reps, ~100 cal), Lunges (3×12 reps per leg, ~80 cal), Jump Rope (10 min, ~120 cal) - Total: 300 calories
        Wednesday: Deadlifts (4×8 reps, ~140 cal), Bench Press (3×10 reps, ~100 cal), Burpees (3×12 reps, ~80 cal) - Total: 320 calories
        Thursday: Mountain Climbers (3×1 min, ~90 cal), Squat Jumps (3×12 reps, ~70 cal), Plank Variations (3×1 min, ~40 cal) - Total: 200 calories
        Friday: Pull-ups (3×12 reps, ~90 cal), Push-ups (4×15 reps, ~80 cal), Running (20 min, ~200 cal) - Total: 370 calories
        Saturday: Cycling (30 min, ~250 cal), Sit-ups (4×20 reps, ~70 cal), Side Planks (3×1 min each side, ~60 cal) - Total: 380 calories
        Sunday: Walking (45 min, ~180 cal), Stretching/Yoga (20 min, ~60 cal) - Total: 240 calories

        COACHING APPROACH:
        - Always provide actionable, specific advice
        - Reference their current routine when making suggestions
        - Consider their body composition and fitness level
        - Include progress tracking methods
        - Offer motivational support and encouragement
        - Suggest realistic goal-setting strategies
        - Provide safety tips and proper form guidance
        - Recommend recovery and rest strategies
        - Always encourage consultation with healthcare professionals for medical advice

        Respond as their personal AI fitness coach, using encouraging and supportive language while providing expert guidance."""
        
        # Make the API call to OpenAI using the static client
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": request.question}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Extract the answer from the response
        answer = response.choices[0].message.content
        
        return QuestionResponse(
            question=request.question,
            answer=answer,
            model_used=response.model
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing question: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
