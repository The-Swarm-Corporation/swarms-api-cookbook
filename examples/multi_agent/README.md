### Multi-Agent Examples

Workflows where multiple agents collaborate, either concurrently, sequentially, or with hierarchical leadership. Make sure you’ve set your `SWARMS_API_KEY` and installed dependencies (see repo root `README.md`).

| File | Description | Run |
|---|---|---|
| `hospital_team.py` | Simulates a hierarchical hospital unit swarm: attending physician (leader), nurses, and a medical assistant collaborating on diagnosis and care planning from patient symptoms. Prints a structured JSON result. | `python examples/multi_agent/hospital_team.py` |
| `icd_ten_analysis.py` | Concurrent ICD code analysis with three agents (an analyzer and two explainers) producing detailed ICD insights from patient symptoms. | `python examples/multi_agent/icd_ten_analysis.py` |
| `python_client_batch_operations.py` | Pattern for processing a list of tasks in batch by looping and running `client.swarms.run` for each task. Good for bulk workloads. | `python examples/multi_agent/python_client_batch_operations.py` |
| `python_client_content_generation.py` | Sequential content generation workflow with a Research agent and a Writer agent to produce a blog post from current AI trends. | `python examples/multi_agent/python_client_content_generation.py` |
| `python_client_data_analysis_pipeline.py` | Sequential data analysis pipeline featuring Data Validator, Statistical Analyst, and Insight Generator agents. | `python examples/multi_agent/python_client_data_analysis_pipeline.py` |
| `python_client_first_swarm.py` | Minimal multi-agent medical analysis swarm (Symptom Analyzer and ICD Code Specialist) returning a response for given symptoms. | `python examples/multi_agent/python_client_first_swarm.py` |

Tip: Use a `.env` file or export `SWARMS_API_KEY` before running.


