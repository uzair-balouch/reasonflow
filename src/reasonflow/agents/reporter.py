from reasonflow.models.goal import Goal
from reasonflow.models.memory import Memory
from reasonflow.models.repository import Repository
from reasonflow.services.llm.base import BaseLLM


class ReportingAgent:
    def __init__(self, llm: BaseLLM):
        self.llm = llm

    def generate_report(
        self,
        goal: Goal,
        repository: Repository,
        memory: Memory,
    ) -> str:

        observations = "\n".join(f"- {observation}" for observation in memory.observations)

        prompt = f"""
            You are a senior software architect.

            Create a professional repository analysis report in Markdown.

            Goal:
            {goal.description}

            Repository:

            Owner: {repository.owner}
            Name: {repository.name}
            Language: {repository.language}
            License: {repository.license}
            Stars: {repository.stars}

            Observations:

            {observations}

            Write the report using exactly these sections:

            # Repository Analysis Report

            ## Summary

            ## Repository

            ## Dependencies

            ## Security

            ## Enterprise Assessment

            ## Recommendations
            """

        return self.llm.generate(prompt)
