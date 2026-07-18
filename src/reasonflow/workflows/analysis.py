from reasonflow.agents.planner import PlanningAgent
from reasonflow.models.goal import Goal
from reasonflow.models.repository import Repository
from reasonflow.services.github import GitHubClient
from reasonflow.services.llm.fake import FakeLLM
from reasonflow.tools.github import GitHubTool


class RepositoryAnalysisWorkflow:
    def run(
        self,
        goal: Goal,
        repository: Repository,
    ) -> Repository:
        goal = Goal(
            description="Analyze this repository",
        )

        repository = Repository(
            url="https://github.com/psf/requests",
            owner="psf",
            name="requests",
        )

        planner = PlanningAgent(FakeLLM())

        plan = planner.create_plan(goal)

        print(plan)

        github_tool = GitHubTool(GitHubClient())

        repository = github_tool.enrich(repository)

        print(repository)
