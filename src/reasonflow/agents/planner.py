import json

from reasonflow.models.goal import Goal
from reasonflow.models.plan import Plan, PlanStep
from reasonflow.models.tool_call import ToolCall
from reasonflow.services.llm.base import BaseLLM


class PlanningAgent:
    """Agent that creates a structured execution plan using an LLM."""

    def __init__(self, llm: BaseLLM):
        self.llm = llm

    def create_plan(self, goal: Goal) -> Plan:
        response = self.llm.generate(goal.description)

        data = json.loads(response)

        steps = []

        for index, step in enumerate(data, start=1):
            steps.append(
                PlanStep(
                    id=index,
                    description=step["description"],
                    tool_call=ToolCall(
                        tool=step["tool"],
                        action=step["action"],
                    ),
                )
            )

        return Plan(steps=steps)
