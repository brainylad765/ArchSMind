from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from Durecs.core.config import settings
from Durecs.agents.requirement_decomposer import RequirementDecomposer
from Durecs.models.architecture_document import FunctionalBlock

app = FastAPI(title=settings.)

# Instantiate the agent as a reusable engine dependency
decomposer_agent = RequirementDecomposer()

class IngestionRequest(BaseModel):
    requirement: str = Field(..., min_length=10, example="Build Instagram for 50M users")

@app.get("/")
async def root_sanity_check():
    return {
        "project": settings.PROJECT_NAME,
        "status": "Operational"
    }

@app.post("/api/v1/architect/decompose", response_model=list[FunctionalBlock])
async def decompose_user_requirements(payload: IngestionRequest):
    """
    Ingests raw software specs, runs the Decomposer Agent swarm task, 
    and streams back strictly structured, validated JSON data to the UI.
    """
    try:
        functional_blocks = decomposer_agent.decompose(payload.requirement)
        return functional_blocks
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Agent Execution Core Failure: {str(e)}"
        )