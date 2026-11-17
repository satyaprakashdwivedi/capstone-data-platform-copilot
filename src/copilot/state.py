"""Shared graph state — the contract every agent reads/writes."""

from __future__ import annotations

import operator
from typing import Annotated, Literal, TypedDict

AgentName = Literal["sql_analyst", "dq_agent", "runbook_rag", "incident_triage", "FINISH"]
AGENTS: tuple[AgentName, ...] = ("sql_analyst", "dq_agent", "runbook_rag", "incident_triage")


class Finding(TypedDict):
    agent: str
    summary: str
    evidence: list[str]


class CopilotState(TypedDict, total=False):
    request: str
    next: AgentName
    findings: Annotated[list[Finding], operator.add]  # appended by each agent
    pending_action: str | None  # side effect awaiting human approval
    approved: bool
    cost_usd: Annotated[float, operator.add]
    steps: Annotated[int, operator.add]


MAX_STEPS = 8
