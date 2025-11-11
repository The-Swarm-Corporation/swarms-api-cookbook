import os
import json
from swarms_client import SwarmsClient
from dotenv import load_dotenv

load_dotenv()

client = SwarmsClient(api_key=os.getenv("SWARMS_API_KEY"))

# Process multiple tasks
tasks = [
    "Analyze customer feedback for Q1",
    "Generate monthly report summary",
    "Review system performance metrics"
]

responses = []
for task in tasks:
    response = client.swarms.run(
        name=f"Batch Task - {task[:20]}...",
        description="Batch processing task",
        swarm_type="ConcurrentWorkflow",
        task=task,
        agents=[
            {
                "agent_name": "Task Analyst",
                "description": "Analyzes a task and extracts key points or requirements.",
                "system_prompt": (
                    "You are an analytical assistant. Read the task, extract goals, "
                    "stakeholders, constraints, and propose an outline of steps."
                ),
                "model_name": "gpt-4.1",
                "role": "worker",
                "max_loops": 1,
                "max_tokens": 2048,
                "temperature": 0.3,
            },
            {
                "agent_name": "Writer",
                "description": "Produces a concise written output based on the analyst's findings.",
                "system_prompt": (
                    "You are a professional writer. Produce a clear, concise deliverable "
                    "that addresses the task using the analyst's key points."
                ),
                "model_name": "gpt-4.1",
                "role": "worker",
                "max_loops": 1,
                "max_tokens": 2048,
                "temperature": 0.6,
            },
        ]
    )
    responses.append(response)

print(json.dumps(responses, indent=4))

