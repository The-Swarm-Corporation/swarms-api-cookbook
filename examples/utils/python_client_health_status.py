import os
from swarms_client import SwarmsClient
from dotenv import load_dotenv

load_dotenv()

client = SwarmsClient(api_key=os.getenv("SWARMS_API_KEY"))

# Check API health
health_status = client.health.check()

# Get rate limits
rate_limits = client.client.rate.get_limits()

print(health_status)
print(rate_limits)

