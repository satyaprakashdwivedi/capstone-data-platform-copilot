# Data Platform Copilot 🛠️🤖
*A multi-agent LangGraph system that helps data platform teams query data, check data quality, triage
pipeline incidents and find runbook answers — cost-aware, evaluated, observable, human-approved.*

> Status: 🔲 Weeks 13–16 of my [AI engineering program](https://github.com/satyaprakashdwivedi/ai-engineering-portfolio)

## Demo
- Live: _TBD_ · Video (3 min): _TBD_

## What it does
| Agent | Skill | Built on |
|---|---|---|
| `supervisor` | Routes requests, plans multi-step work, enforces budgets | LangGraph supervisor |
| `sql_analyst` | NL→SQL on DuckDB via MCP; fine-tuned local model first, Claude fallback | Module 04 + 07 |
| `dq_agent` | Freshness/volume/schema checks + ML anomaly detection | Module 01 |
| `runbook_rag` | Agentic RAG over pipeline runbooks with citations | Module 03 + 05 |
| `incident_triage` | Log analysis → root-cause hypothesis → draft RCA; **human approval** before actions | Module 05 + 06 |

See [ARCHITECTURE.md](ARCHITECTURE.md) and [docs/adr](docs/adr).

## Results
| Eval | Metric | Score |
|---|---|---|
| NL→SQL (100 Qs) | execution accuracy | – |
| Runbook QA (50 Qs) | faithfulness / relevance | – |
| Incident scenarios (20) | task success, avg $/run, p95 latency | – |
| Routing | % requests served by local model | – |

## Run
```bash
cp .env.example .env && uv sync --all-extras
ollama pull llama3.2:3b && ollama pull nomic-embed-text
uv run python -m copilot.seed   # synthetic warehouse + runbooks
docker compose up               # API + UI + Langfuse
```

## Built with AI agents
Specced, implemented, tested and reviewed by Claude Code subagents I orchestrate (`.claude/agents/`), with
Claude PR review in CI. Every decision and override is logged in [AI_LOG.md](AI_LOG.md).
