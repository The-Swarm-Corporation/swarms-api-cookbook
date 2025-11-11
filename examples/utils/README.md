### Utilities

Utility scripts for quick checks, model discovery, basic client bootstrap, and rate limit diagnostics. Make sure `SWARMS_API_KEY` is configured and dependencies installed (see repo root `README.md`).

| File | Description | Run |
|---|---|---|
| `client_example.py` | Quick tour of client endpoints: lists available models, checks health, fetches swarm logs, prints rate limits, and checks available swarms. | `python examples/utils/client_example.py` |
| `python_client_health_status.py` | Checks API health and retrieves current rate limits; prints results. | `python examples/utils/python_client_health_status.py` |
| `python_client_model_info.py` | Lists available models from the API. | `python examples/utils/python_client_model_info.py` |
| `python_client_quickstart.py` | Minimal client bootstrap showing how to instantiate `SwarmsClient` with an API key (starting point for your own scripts). | `python examples/utils/python_client_quickstart.py` |
| `rate_limits.py` | Retrieves and prints current rate limits and health status for quick diagnostics. | `python examples/utils/rate_limits.py` |

Tip: Run any script with `python examples/utils/<script>.py`.


