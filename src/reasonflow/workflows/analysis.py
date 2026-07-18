from reasonflow.agents.planner import PlannerAgent
from reasonflow.models.repository import Repository
from reasonflow.tools.github import GitHubTool


class RepositoryAnalysisWorkflow:
    """
    Orchestrates repository analysis.
    """

    def run(self, repository: Repository) -> None:
        planner = PlannerAgent()
        github = GitHubTool()

        plan = planner.create_plan(repository)

        print("Execution Plan:")

        for step in plan:
            print(f" - {step}")

        github.fetch_metadata(repository)
