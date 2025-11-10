import os
from swarms_client import SwarmsClient
from dotenv import load_dotenv

load_dotenv()

client = SwarmsClient(api_key=os.getenv("SWARMS_API_KEY"))

# Create and run a swarm
swarm_response = client.swarms.run(
    name="Data Analysis Swarm",
    description="Analyzes complex datasets",
    swarm_type="SequentialWorkflow",
    task="Analyze the sales data for Q4",
    agents=[...]
)

# Get swarm logs
logs = client.swarms.get_logs()

# Check available swarms
available = client.swarms.check_available()

