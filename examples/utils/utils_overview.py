import os
import json
from dotenv import load_dotenv
from swarms_client import SwarmsClient

# Load environment variables
load_dotenv()

# Initialize the client
client = SwarmsClient(api_key=os.getenv("SWARMS_API_KEY"))

# Check available models
print("Available Models:")
print(json.dumps(client.models.list_available(), indent=4))

# Check API health
print("\nAPI Health:")
print(json.dumps(client.health.check(), indent=4))

# Get swarm logs
print("\nSwarm Logs:")
print(json.dumps(client.swarms.get_logs(), indent=4))

# Check rate limits
print("\nRate Limits:")
print(json.dumps(client.client.rate.get_limits(), indent=4))

# Check swarm availability
print("\nSwarm Availability:")
print(json.dumps(client.swarms.check_available(), indent=4))
