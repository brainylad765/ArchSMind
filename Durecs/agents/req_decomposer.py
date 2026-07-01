import os
import json
from openai import OpenAI
from Durecs.models.architecture_document import FunctionalBlock

class RequirementDecomposer:
    """Breaks down raw application text specifications into validated structured Functional Blocks."""

    def __init__(self):
        # Gracefully fallbacks to an environment variable read
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "mock-key-if-missing"))

    def decompose(self, requirement: str) -> list[FunctionalBlock]:
        system_prompt = (
            "You are an expert systems engineer. Analyze the requirements and output a raw JSON "
            "object with a top-level key 'blocks' containing an array of functional components. "
            "Each block must have: name, description, sub_components (list), dependencies (list), data_flow."
        )
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": requirement}
            ],
            response_format={"type": "json_object"},
            temperature=0.2,
        )
        
        raw_output = response.choices[0].message.content
        data = json.loads(raw_output)
        
        blocks_data = data.get("blocks", data if isinstance(data, list) else [])
        return [FunctionalBlock(**block) for block in blocks_data]