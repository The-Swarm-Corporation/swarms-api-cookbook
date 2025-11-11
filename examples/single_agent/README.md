### Single-Agent Examples

Single-agent operations and batch runs using individual agents. Ensure `SWARMS_API_KEY` is set and dependencies are installed (see repo root `README.md`).

| File | Description | Run |
|---|---|---|
| `agent_overview.py` | Runs a single expert agent (“Bloodwork Diagnosis Expert”) on a diagnostic task and prints a formatted JSON response. | `python examples/single_agent/agent_overview.py` |
| `batch_example.py` | Submits multiple independent single-agent tasks in one batch using `client.agent.batch.run` (e.g., bloodwork interpretation and radiology summarization). | `python examples/single_agent/batch_example.py` |

Tip: Create a `.env` with `SWARMS_API_KEY=...` or export it in your shell.


