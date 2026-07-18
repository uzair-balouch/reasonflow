from dataclasses import dataclass, field


@dataclass(slots=True)
class PlanStep:
    id: int
    description: str


@dataclass(slots=True)
class Plan:
    steps: list[PlanStep] = field(default_factory=list)
