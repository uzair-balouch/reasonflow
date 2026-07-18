from reasonflow.services.llm.base import BaseLLM


class FakeLLM(BaseLLM):
    def generate(self, prompt: str) -> str:
        return """
[
    {
        "description": "Fetch repository metadata",
        "tool": "github",
        "action": "metadata"
    }
]
"""
