from reasonflow.agents.planner import PlanningAgent
from reasonflow.models.goal import Goal
from reasonflow.models.memory import Memory
from reasonflow.services.llm.fake import FakeLLM


def test_planning_agent():
    goal = Goal(description="Analyze this repository")
    memory = Memory()

    planner = PlanningAgent(FakeLLM())

    plan = planner.create_plan(goal, memory)

    assert len(plan.steps) == 1

    step = plan.steps[0]

    assert step.description == "Fetch repository metadata"
    assert step.tool_call is not None
    assert step.tool_call.tool == "github"
    assert step.tool_call.action == "metadata"


def test_planning_agent_after_metadata():
    goal = Goal(description="Analyze this repository")

    memory = Memory()
    memory.add("Repository metadata collected for psf/requests")

    planner = PlanningAgent(FakeLLM())

    plan = planner.create_plan(goal, memory)

    assert len(plan.steps) == 0
