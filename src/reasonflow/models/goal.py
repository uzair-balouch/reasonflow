from dataclasses import dataclass, field


@dataclass(slots=True)
class Goal:
    description: str
    constraints: list[str] = field(default_factory=list)
    success_criteria: list[str] = field(default_factory=list)
