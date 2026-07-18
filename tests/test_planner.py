from reasonflow.agents.planner import PlanningAgent
from reasonflow.models.goal import Goal
from reasonflow.models.repository import Repository
from reasonflow.services.github import GitHubClient
from reasonflow.services.llm.fake import FakeLLM
from reasonflow.tools.github import GitHubTool


def test_planning_agent():
    goal = Goal(description="Analyze this repository")

    planner = PlanningAgent(FakeLLM())

    plan = planner.create_plan(goal)

    assert len(plan.steps) == 1

    step = plan.steps[0]

    assert step.description == "Fetch repository metadata"
    assert step.tool_call is not None
    assert step.tool_call.tool == "github"
    assert step.tool_call.action == "metadata"


def test_fetch_repository():
    repository = Repository(
        url="https://github.com/psf/requests",
        owner="psf",
        name="requests",
    )

    tool = GitHubTool(GitHubClient())

    repository = tool.enrich(repository)

    assert repository.language == "Python"
    assert repository.default_branch
    assert repository.stars > 1000
