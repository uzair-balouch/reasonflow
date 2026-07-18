from reasonflow.models.goal import Goal
from reasonflow.models.plan import Plan, PlanStep
from reasonflow.services.llm.base import BaseLLM


class PlanningAgent:
    """Agent that creates a plan to achieve a goal using an LLM."""

    def __init__(self, llm: BaseLLM):
        self.llm = llm

    def create_plan(self, goal: Goal) -> Plan:
        response = self.llm.generate(goal.description)

        steps = []

        for index, line in enumerate(response.strip().splitlines(), start=1):
            line = line.strip()

            if not line:
                continue

            # Remove "1. ", "2. ", etc.
            description = line.split(". ", 1)[1]

            steps.append(
                PlanStep(
                    id=index,
                    description=description,
                )
            )

        return Plan(steps=steps)
