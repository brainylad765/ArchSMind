# This would be used to VALIDATE THE ARCHITECUTURE DOCUMENTATION, THATS WHY ONLY SCHEMAS ARE DEFINED HERE, NOT THE ACTUAL MODELS.
from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from enum import Enum

class DatabaseType(str, Enum):
    POSTGRESQL = "PostgreSQL"
    MYSQL = "MySQL"
    MONGODB = "MongoDB"
    CASSANDRA = "Cassandra"
    DYNAMODB = "DynamoDB"
    NEO4J = "Neo4j"
    REDIS = "Redis"

class DatabaseChoice(BaseModel):
    db_type: DatabaseType
    justification: str
    trade_offs: List[str]
    scaling_strategy: str

class FunctionalBlock(BaseModel):
    name: str
    description: str
    sub_components: List[str] = Field(default_factory=list)
    dependencies: List[str] = Field(default_factory=list)
    data_flow: str = ""

class APIDesign(BaseModel):
    style: str  
    endpoints: List[Dict[str, Any]] = Field(default_factory=list)
    authentication: str
    rate_limiting: str

class SecurityRecommendation(BaseModel):
    area: str
    recommendation: str
    severity: str  

class ArchitectureDocument(BaseModel):
    project_name: str
    functional_decomposition: List[FunctionalBlock] = Field(default_factory=list)
    backend_architecture: str = ""
    database_choices: List[DatabaseChoice] = Field(default_factory=list)
    api_design: Optional[APIDesign] = None
    security_recommendations: List[SecurityRecommendation] = Field(default_factory=list)
    cloud_architecture: Optional[str] = None
    scalability_analysis: Optional[str] = None
    cost_estimation: Optional[str] = None