from reasonflow.agents.planner import PlanningAgent
from reasonflow.models.goal import Goal
from reasonflow.models.repository import Repository
from reasonflow.services.github import GitHubClient
from reasonflow.services.llm.fake import FakeLLM
from reasonflow.tools.github import GitHubTool


class RepositoryAnalysisWorkflow:
    def run(self, repository_url: str) -> Repository:
        parts = repository_url.rstrip("/").split("/")

        repository = Repository(
            url=repository_url,
            owner=parts[-2],
            name=parts[-1],
        )

        goal = Goal(
            description="Analyze this repository",
        )

        planner = PlanningAgent(FakeLLM())
        plan = planner.create_plan(goal)

        # print(plan)
        print("\nPlanning...\n")

        for step in plan.steps:
            print(f"✓ {step.description}")

        github_tool = GitHubTool(GitHubClient())
        repository = github_tool.enrich(repository)

        # print(repository)
        print("\nRepository Information")
        print("-" * 30)
        print(f"Owner           : {repository.owner}")
        print(f"Repository      : {repository.name}")
        print(f"Language        : {repository.language}")
        print(f"Default Branch  : {repository.default_branch}")
        print(f"License         : {repository.license}")
        print(f"Stars           : {repository.stars}")

        return repository
