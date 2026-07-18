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
    ) -> Repository:

        for step in plan.steps:
            if step.tool_call is None:
                continue

            tool = self.registry.get(step.tool_call.tool)

            if step.tool_call.action == "metadata":
                repository = tool.enrich(repository)

        return repository
