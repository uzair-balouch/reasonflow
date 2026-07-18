import json

from reasonflow.models.goal import Goal
from reasonflow.models.memory import Memory
from reasonflow.models.plan import Plan, PlanStep
from reasonflow.models.tool_call import ToolCall
from reasonflow.services.llm.base import BaseLLM


class PlanningAgent:
    def __init__(self, llm: BaseLLM):
        self.llm = llm

    def create_plan(
        self,
        goal: Goal,
        memory: Memory,
    ) -> Plan:

        observations = "\n".join(memory.observations)

        prompt = f"""
    You are an autonomous software engineering agent.

    Goal:
    {goal.description}

    Current observations:
    {observations}

    Available tools (USE THESE EXACT TOOL NAMES):

    Tool: github
    Allowed action:
    - metadata

    Tool: dependency
    Allowed action:
    - discover

    Tool: vulnerability
    Allowed action:
    - scan

    Rules:

    1. The "tool" field MUST be exactly one of:
    - github
    - dependency
    - vulnerability

    2. The "action" field MUST be exactly one of:
    - metadata
    - discover
    - scan

    3. Never combine tool and action.
    Correct:
        "tool": "dependency"
        "action": "discover"

    Incorrect:
        "tool": "dependency.discover"

    4. Return ONLY valid JSON.

    5. Do not use markdown.

    6. If the goal is complete, return:

    []

    Example:

    [
        {{
            "description": "Fetch repository metadata",
            "tool": "github",
            "action": "metadata"
        }}
    ]
    """

        response = self.llm.generate(prompt)

        print("\n========== LLM RESPONSE ==========\n")
        print(response)
        print("\n==================================\n")

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
