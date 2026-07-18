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

            tool = self.registry.get(step.tool_call.tool)

            if step.tool_call.action == "metadata":
                repository = tool.enrich(repository)

                memory.add(
                    f"Repository metadata collected for {repository.owner}/{repository.name}"
                )

            elif step.tool_call.action == "discover":
                manifests = tool.find_manifests(repository)

                if manifests:
                    for manifest in manifests:
                        memory.add(f"Found manifest: {manifest}")

                else:
                    memory.add("No dependency manifests found.")

        return repository
