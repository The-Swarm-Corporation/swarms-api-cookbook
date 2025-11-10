import os
from swarms_client import SwarmsClient
from dotenv import load_dotenv

load_dotenv()

client = SwarmsClient(api_key=os.getenv("SWARMS_API_KEY"))

content_swarm = client.swarms.run(
    name="Content Generation Swarm",
    description="Creates engaging content for social media",
    swarm_type="SequentialWorkflow",
    task="Create a blog post about AI trends in 2024",
    agents=[
        {
            "agent_name": "Research Agent",
            "description": "Researches current AI trends and statistics",
            "system_prompt": "You are a research specialist. Gather current information about AI trends.",
            "model_name": "groq/openai/gpt-oss-120b",
            "role": "researcher",
            "max_loops": 1,
            "max_tokens": 4096,
            "temperature": 0.3,
        },
        {
            "agent_name": "Writer Agent",
            "description": "Writes engaging blog content based on research",
            "system_prompt": "You are a professional writer. Create engaging blog content.",
            "model_name": "groq/openai/gpt-oss-120b",
            "role": "writer",
            "max_loops": 1,
            "max_tokens": 8192,
            "temperature": 0.7,
        }
    ],
)

