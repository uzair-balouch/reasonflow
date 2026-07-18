from reasonflow.services.llm.base import BaseLLM


class FakeLLM(BaseLLM):
    def generate(self, prompt: str) -> str:

        if "Repository metadata collected" in prompt:
            return """
[]
"""

        return """
[
    {
        "description": "Fetch repository metadata",
        "tool": "github",
        "action": "metadata"
    }
]
"""
