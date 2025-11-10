import os
from swarms_client import SwarmsClient
from dotenv import load_dotenv

load_dotenv()

client = SwarmsClient(
    api_key=os.getenv("SWARMS_API_KEY"),
)

# Define your task
task_description = """
Analyze the following patient symptoms and provide ICD code recommendations:
- 45-year-old female with chest pain
- Shortness of breath for 2 days
- Sharp chest pain worsening with deep breathing
- Mild fever (100.2°F) and dry cough
"""

# Create and run a swarm
response = client.swarms.run(
    name="Medical Analysis Swarm",
    description="A swarm that analyzes patient symptoms and provides ICD codes",
    swarm_type="ConcurrentWorkflow",
    task=task_description,
    agents=[
        {
            "agent_name": "Symptom Analyzer",
            "description": "Analyzes patient symptoms and identifies key indicators",
            "system_prompt": "You are a medical expert. Analyze symptoms and identify key medical indicators.",
            "model_name": "groq/openai/gpt-oss-120b",
            "role": "worker",
            "max_loops": 1,
            "max_tokens": 8192,
            "temperature": 0.3,
        },
        {
            "agent_name": "ICD Code Specialist",
            "description": "Provides appropriate ICD codes based on symptom analysis",
            "system_prompt": "You are an ICD coding specialist. Provide accurate ICD codes with explanations.",
            "model_name": "groq/openai/gpt-oss-120b",
            "role": "worker",
            "max_loops": 1,
            "max_tokens": 8192,
            "temperature": 0.2,
        }
    ],
)

print(response)

