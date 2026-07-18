from reasonflow.agents.planner import PlanningAgent
from reasonflow.models.goal import Goal
from reasonflow.services.llm.fake_llm import FakeLLM


def test_planning_agent():
    goal = Goal(description="Analyze this repository")

    planner = PlanningAgent(FakeLLM())

    plan = planner.create_plan(goal)

    assert len(plan.steps) == 4
    assert plan.steps[0].description == "Analyze repository"
