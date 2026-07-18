from reasonflow.models.memory import Memory
from reasonflow.models.plan import Plan
from reasonflow.models.repository import Repository
from reasonflow.tools.registry import ToolRegistry


class Executor:
    def __init__(self, registry: ToolRegistry):
        self.registry = registry

    def execute(
        self,
        plan: Plan,
        repository: Repository,
        memory: Memory,
    ) -> Repository:

        for step in plan.steps:
            if step.tool_call is None:
                continue

            tool_name = step.tool_call.tool.split(".")[0]
            tool = self.registry.get(tool_name)

            if step.tool_call.action == "metadata":
                repository = tool.enrich(repository)

                memory.add(
                    f"Repository metadata collected for {repository.owner}/{repository.name}"
                )

            elif step.tool_call.action == "discover":
                manifests = tool.find_manifests(repository)

                if not manifests:
                    memory.add("No dependency manifests found.")
                    continue

                for manifest in manifests:
                    memory.add(f"Found manifest: {manifest}")

                    dependencies = tool.read_dependencies(
                        repository,
                        manifest,
                    )

                    for dependency in dependencies:
                        memory.add(f"Dependency: {dependency}")

            elif step.tool_call.action == "scan":
                dependencies = []

                for observation in memory.observations:
                    if observation.startswith("Dependency: "):
                        dependencies.append(observation.replace("Dependency: ", ""))

                findings = tool.scan(dependencies)

                for finding in findings:
                    memory.add(finding)

        return repository
