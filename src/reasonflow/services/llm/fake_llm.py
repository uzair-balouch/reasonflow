from reasonflow.services.llm.base import BaseLLM


class FakeLLM(BaseLLM):
    def generate(self, prompt: str) -> str:
        return """
        1. Analyze repository
        2. Detect dependencies
        3. Scan vulnerabilities
        4. Produce report
        """
