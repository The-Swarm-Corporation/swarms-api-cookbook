# Swarms API Cookbook

<p align="left">
  <!-- Main Navigation Links -->
  <a href="https://swarms.ai">🏠 Swarms Website</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://docs.swarms.ai">📙 Documentation</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://swarms.world/platform/api-keys">🔑 API Key Management</a>
</p>


Practical cookbook examples for the Swarms API Client. This repository is a hands-on guide to building with Swarms, showcasing single-agent and multi-agent workflows, concurrent and sequential pipelines, content generation, data analysis, health and rate checks, and more. Each example is designed to be minimal yet illustrative, so you can quickly adapt patterns to your own use cases.

What you’ll find here:

- Clear, runnable examples for common tasks
- Patterns for hierarchical, concurrent, and sequential workflows
- Utilities for health checks, model discovery, logs, and rate limits
- Async usage with `AsyncSwarmsClient` for higher throughput workloads

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

### Why Swarms
- Compose specialized agents to collaborate on end-to-end tasks.
- Mix and match workflow types (hierarchical leadership, concurrent workers, sequential pipelines).
- Keep observability with logs, health checks, and rate limit endpoints.
- Scale via async execution and batch operations.

### How to run an example

```bash
python examples/path/to/script.py
```

Replace `path/to/script.py` with any script listed below.

### Examples

#### `multi_agent/`
Multi-agent workflows where several agents collaborate either concurrently or in sequence.

| File | Description | Run |
|---|---|---|
| [`hospital_team.py`](examples/multi_agent/hospital_team.py) | Simulates a hierarchical medical unit swarm (attending physician as leader, nurses, and a medical assistant) collaborating on diagnosis and care planning from patient symptoms. Prints a structured JSON result. | `python examples/multi_agent/hospital_team.py` |
| [`icd_ten_analysis.py`](examples/multi_agent/icd_ten_analysis.py) | Concurrent ICD code analysis with three agents (an analyzer and two explainers) producing detailed ICD insights from patient symptoms. | `python examples/multi_agent/icd_ten_analysis.py` |
| [`python_client_batch_operations.py`](examples/multi_agent/python_client_batch_operations.py) | Pattern for processing a list of tasks in batch by looping and running `client.swarms.run` for each task. Good for bulk workloads. | `python examples/multi_agent/python_client_batch_operations.py` |
| [`python_client_content_generation.py`](examples/multi_agent/python_client_content_generation.py) | Sequential content generation workflow with a Research agent and a Writer agent to produce a blog post from current AI trends. | `python examples/multi_agent/python_client_content_generation.py` |
| [`python_client_data_analysis_pipeline.py`](examples/multi_agent/python_client_data_analysis_pipeline.py) | Sequential data analysis pipeline featuring Data Validator, Statistical Analyst, and Insight Generator agents. | `python examples/multi_agent/python_client_data_analysis_pipeline.py` |
| [`python_client_first_swarm.py`](examples/multi_agent/python_client_first_swarm.py) | Minimal multi-agent medical analysis swarm (Symptom Analyzer and ICD Code Specialist) returning a response for given symptoms. | `python examples/multi_agent/python_client_first_swarm.py` |

#### `single_agent/`
Single-agent operations and batch runs using individual agents.

| File | Description | Run |
|---|---|---|
| [`agent_overview.py`](examples/single_agent/agent_overview.py) | Run a single expert agent (“Bloodwork Diagnosis Expert”) on a diagnostic task and print a formatted JSON response. | `python examples/single_agent/agent_overview.py` |
| [`batch_example.py`](examples/single_agent/batch_example.py) | Submit multiple independent single-agent tasks in one batch using `client.agent.batch.run` (e.g., bloodwork interpretation and radiology summarization). | `python examples/single_agent/batch_example.py` |

#### `utils/`
Utility scripts for quick checks, model and health endpoints, async patterns, and swarm management.

| File | Description | Run |
|---|---|---|
| [`client_example.py`](examples/utils/client_example.py) | Quick tour of client endpoints: lists available models, checks health, fetches swarm logs, prints rate limits, and checks available swarms. | `python examples/utils/client_example.py` |
| [`python_client_async_example.py`](examples/utils/python_client_async_example.py) | Demonstrates `AsyncSwarmsClient` to run multiple operations concurrently (multiple swarm runs and a model list) using `asyncio.gather`. | `python examples/utils/python_client_async_example.py` |
| [`python_client_health_status.py`](examples/utils/python_client_health_status.py) | Checks API health and retrieves current rate limits; prints results. | `python examples/utils/python_client_health_status.py` |
| [`python_client_model_info.py`](examples/utils/python_client_model_info.py) | Lists available models from the API. | `python examples/utils/python_client_model_info.py` |
| [`python_client_quickstart.py`](examples/utils/python_client_quickstart.py) | Minimal client bootstrap showing how to instantiate `SwarmsClient` with an API key (starting point for your own scripts). | `python examples/utils/python_client_quickstart.py` |
| [`python_client_swarm_management.py`](examples/utils/python_client_swarm_management.py) | Create and run a swarm, then retrieve logs and inspect which swarms are available. | `python examples/utils/python_client_swarm_management.py` |
| [`rate_limits.py`](examples/utils/rate_limits.py) | Retrieves and prints current rate limits and health status for quick diagnostics. | `python examples/utils/rate_limits.py` |

----

### Resources

| Resource | Link |
|---|---|
| Documentation | [docs.swarms.ai](https://docs.swarms.ai) |
| Technical support | [Book a Swarms Strategy Session](https://cal.com/swarms/swarms-strategy-session) |
| Discord support | [Join the Swarms Discord](https://discord.gg/EamjgSaEQf) |

---

License

Apache License