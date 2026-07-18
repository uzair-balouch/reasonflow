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

    assert len(plan.steps) == 4
    assert plan.steps[0].description == "Analyze repository"


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
