import os
from swarms_client import SwarmsClient
from dotenv import load_dotenv

load_dotenv()

client = SwarmsClient(api_key=os.getenv("SWARMS_API_KEY"))

analysis_pipeline = client.swarms.run(
    name="Data Analysis Pipeline",
    description="Comprehensive data analysis workflow",
    swarm_type="SequentialWorkflow",
    task="Analyze quarterly sales data and provide insights",
    agents=[
        {
            "agent_name": "Data Validator",
            "description": "Validates and cleans input data",
            "system_prompt": "You are a data validation expert. Check data quality and format.",
            "model_name": "groq/openai/gpt-oss-120b",
            "role": "validator",
            "max_loops": 1,
            "max_tokens": 4096,
            "temperature": 0.1,
        },
        {
            "agent_name": "Statistical Analyst",
            "description": "Performs statistical analysis on the data",
            "system_prompt": "You are a statistical analyst. Perform comprehensive data analysis.",
            "model_name": "groq/openai/gpt-oss-120b",
            "role": "analyst",
            "max_loops": 1,
            "max_tokens": 8192,
            "temperature": 0.2,
        },
        {
            "agent_name": "Insight Generator",
            "description": "Generates actionable insights from analysis",
            "system_prompt": "You are a business analyst. Generate actionable insights.",
            "model_name": "groq/openai/gpt-oss-120b",
            "role": "insights",
            "max_loops": 1,
            "max_tokens": 4096,
            "temperature": 0.5,
        }
    ],
)

