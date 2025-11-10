import asyncio
import os
from swarms_client import AsyncSwarmsClient
from dotenv import load_dotenv

load_dotenv()

async def main():
    client = AsyncSwarmsClient(api_key=os.getenv("SWARMS_API_KEY"))
    
    # Run multiple operations concurrently
    tasks = [
        client.swarms.run(name="Task 1", ...),
        client.swarms.run(name="Task 2", ...),
        client.models.list_available()
    ]
    
    results = await asyncio.gather(*tasks)
    return results

# Run the async function
results = asyncio.run(main())

