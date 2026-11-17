# CLAUDE.md — Data Platform Copilot
Capstone multi-agent LangGraph app. Same conventions and subagent workflow as ai-engineering-portfolio.
- Code in `src/copilot/`; agents in `src/copilot/agents/<name>.py`, each exposing `build_node(router) -> Callable`.
- Graph assembled in `src/copilot/graph.py`; state schema in `src/copilot/state.py` (single source of truth).
- All tools go through the MCP server (`src/copilot/mcp_server.py`); DB credentials are read-only.
- Any side-effecting tool MUST be preceded by a LangGraph `interrupt()` for human approval.
- Tests: `uv run pytest -q` (fake LLMs, no paid calls). Evals: `uv run python -m evals.run_all`.
- Use `/build-module` with the capstone milestone name (e.g. `/build-module w14-agents`) — treat repo root as the module.
