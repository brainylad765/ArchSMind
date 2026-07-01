import os
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Global System Settings for ArchMind Core Engine.
    Loads variables from environment or .env file securely.
    """
    PROJECT_NAME: str = "ArchMind Reasoning Engine"
    ENVIRONMENT: str = Field(default="development", alias="ENV")
    
    # LLM Provider Configuration
    OPENAI_API_KEY: str = Field(default="mock-key-for-now", alias="OPENAI_API_KEY")
    DEFAULT_MODEL: str = "gpt-4o"
    TEMPERATURE: float = 0.2
    
    # System Architecture Boundaries
    MAX_AGENT_LOOPS: int = 10
    
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"
    )

# Instantiate a global singleton for runtime reuse
settings = Settings()