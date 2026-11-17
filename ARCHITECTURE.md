# Architecture

```mermaid
flowchart LR
  U[User / Slack / UI] --> API[FastAPI + streaming]
  API --> SUP{{Supervisor<br/>LangGraph}}
  SUP --> SQL[sql_analyst]
  SUP --> DQ[dq_agent]
  SUP --> RAG[runbook_rag]
  SUP --> INC[incident_triage]
  INC -->|interrupt| HITL[[Human approval]]
  SQL --> MCP[(MCP server: DuckDB / logs / files)]
  DQ --> MCP
  INC --> MCP
  RAG --> VS[(Chroma + BM25)]
  SQL & DQ & RAG & INC --> R[LLM Router]
  R --> OL[Ollama: fine-tuned SQL model / llama3.2]
  R --> CL[Claude API]
  SUP --- CK[(SQLite checkpointer + store)]
  API -.traces.-> LF[Langfuse]
```

## Key decisions (ADRs to write in week 13)
1. Supervisor vs swarm topology · 2. MCP as the tool boundary (least privilege, read-only creds)
3. Local-first routing with confidence-based escalation to Claude · 4. HITL before any write/side effect
5. Eval suites as CI gates · 6. State schema & persistence

## Non-functional targets
p95 latency < 8s for single-agent requests · ≤ $0.02 average per request · ≥ 60% of calls served locally ·
zero write actions without approval · every run traced.
