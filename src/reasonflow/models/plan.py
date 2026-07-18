from dataclasses import dataclass, field

from reasonflow.models.tool_call import ToolCall


@dataclass(slots=True)
class PlanStep:
    id: int
    description: str
    tool_call: ToolCall | None = None


@dataclass(slots=True)
class Plan:
    steps: list[PlanStep] = field(default_factory=list)
