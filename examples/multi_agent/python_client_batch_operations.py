import os
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
        agents=[...]
    )
    responses.append(response)

