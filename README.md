## swarms-api-client-cookbook
Practical cookbook examples for the Swarms API Client.

### Install

```bash
pip install swarms-client python-dotenv
```

### Set your API Key

Use an environment variable:

```bash
export SWARMS_API_KEY="your_api_key_here"
```

Or create a `.env` file in your project root:

```bash
echo 'SWARMS_API_KEY=your_api_key_here' > .env
```

### Quickstart

```python
import os
from dotenv import load_dotenv
from swarms_client import SwarmsClient

load_dotenv()

client = SwarmsClient(api_key=os.getenv("SWARMS_API_KEY"))

response = client.swarms.run(
    name="Hello Swarm",
    description="Simple demo swarm",
    swarm_type="SequentialWorkflow",
    task="Write a concise haiku about collaborative AI.",
    agents=[
        {
            "agent_name": "Haiku Writer",
            "description": "Creates short poetic outputs",
            "system_prompt": "Write a haiku that is vivid and clear.",
            "model_name": "groq/openai/gpt-oss-120b",
            "role": "worker",
            "max_loops": 1,
            "max_tokens": 256,
            "temperature": 0.5,
        }
    ],
)

print(response)
```

### Explore the Examples

- See [examples/README.md](examples/README.md) for a full index of every example and what each script does.
- Categories:
  - [examples/multi_agent/](examples/multi_agent/): multi-agent workflows (hierarchical, concurrent, sequential).
  - [examples/single_agent/](examples/single_agent/): single-agent runs and batch requests.
  - [examples/utils/](examples/utils/): health checks, model listings, async usage, and swarm management helpers.
