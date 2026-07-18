from reasonflow.agents.planner import PlanningAgent
from reasonflow.models.goal import Goal
from reasonflow.models.memory import Memory
from reasonflow.services.llm.fake import FakeLLM


def test_planning_agent():
    goal = Goal(description="Analyze this repository")
    memory = Memory()

    planner = PlanningAgent(FakeLLM())

    plan = planner.create_plan(goal, memory)

    assert len(plan.steps) == 3

    assert plan.steps[0].description == "Fetch repository metadata"
    assert plan.steps[0].tool_call.tool == "github"
    assert plan.steps[0].tool_call.action == "metadata"

    assert plan.steps[1].description == "Discover dependency manifests"
    assert plan.steps[1].tool_call.tool == "dependency"
    assert plan.steps[1].tool_call.action == "discover"

    assert plan.steps[2].description == "Scan dependencies for vulnerabilities"
    assert plan.steps[2].tool_call.tool == "vulnerability"
    assert plan.steps[2].tool_call.action == "scan"


def test_planning_agent_after_metadata():
    goal = Goal(description="Analyze this repository")

    memory = Memory()
    memory.add("Repository metadata collected for psf/requests")

    planner = PlanningAgent(FakeLLM())

    plan = planner.create_plan(goal, memory)

    assert len(plan.steps) == 0
