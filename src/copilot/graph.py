"""Supervisor graph — implemented in week 14 via /build-module w14-agents.

Plan: StateGraph(CopilotState) → supervisor node (structured output picks `next`) → agent nodes →
back to supervisor until FINISH or MAX_STEPS; incident_triage calls interrupt() before actions;
compiled with SqliteSaver checkpointer.
"""
