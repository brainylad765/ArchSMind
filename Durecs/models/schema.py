from pydantic import BaseModel, Field, field_validator
from typing import Optional, List, Dict

class UserRequirementPayload(BaseModel):
    """
    The immutable contract ingestion model for ArchMind.
    Validates user constraints before passing them to the agent swarm.
    """
    prompt: str = Field(..., description="Raw architecture requirements from the user.")
    target_scale_users: int = Field(default=100000, description="Target concurrent or active user base.")
    budget_constraints_usd: Optional[float] = Field(default=None, description="Optional monthly cloud spend cap.")
    preferred_cloud_providers: List[str] = Field(default_factory=list, description="AWS, GCP, Azure, etc.")
    
    @field_validator('target_scale_users')
    @classmethod
    def validate_scale(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("Target scale users must be a positive integer.")
        return v