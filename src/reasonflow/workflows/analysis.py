from reasonflow.agents.executor import Executor
from reasonflow.agents.planner import PlanningAgent
from reasonflow.models.goal import Goal
from reasonflow.models.memory import Memory
from reasonflow.models.repository import Repository
from reasonflow.services.github import GitHubClient
from reasonflow.services.llm.fake import FakeLLM
from reasonflow.tools.dependency import DependencyTool
from reasonflow.tools.github import GitHubTool
from reasonflow.tools.registry import ToolRegistry


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

        memory = Memory()

        planner = PlanningAgent(FakeLLM())
        plan = planner.create_plan(
            goal,
            memory,
        )

        print("\nPlanning...\n")

        for step in plan.steps:
            print(f"✓ {step.description}")

        registry = ToolRegistry()

        registry.register(
            "github",
            GitHubTool(GitHubClient()),
        )

        registry.register(
            "dependency",
            DependencyTool(),
        )

        executor = Executor(registry)

        repository = executor.execute(
            plan,
            repository,
            memory,
        )

        next_plan = planner.create_plan(
            goal,
            memory,
        )

        print("\nRepository Information")
        print("-" * 30)
        print(f"Owner           : {repository.owner}")
        print(f"Repository      : {repository.name}")
        print(f"Language        : {repository.language}")
        print(f"Default Branch  : {repository.default_branch}")
        print(f"License         : {repository.license}")
        print(f"Stars           : {repository.stars}")

        print("\nObservations")
        print("-" * 30)

        for observation in memory.observations:
            print(f"• {observation}")

        print("\nReflection")
        print("-" * 30)

        if not next_plan.steps:
            print("✓ Goal satisfied.")
        else:
            print("More work required.")

        return repository
