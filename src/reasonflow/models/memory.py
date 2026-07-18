from dataclasses import dataclass, field


@dataclass(slots=True)
class Memory:
    observations: list[str] = field(default_factory=list)

    def add(self, observation: str) -> None:
        self.observations.append(observation)
