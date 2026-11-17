from copilot.state import AGENTS, MAX_STEPS


def test_agents_registered():
    assert set(AGENTS) == {"sql_analyst", "dq_agent", "runbook_rag", "incident_triage"}


def test_step_budget_is_bounded():
    assert 0 < MAX_STEPS <= 10
