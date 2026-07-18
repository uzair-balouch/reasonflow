import os

from dotenv import load_dotenv
from google import genai

from reasonflow.services.llm.base import BaseLLM

load_dotenv()


class GeminiLLM(BaseLLM):
    def __init__(self):
        self.client = genai.Client(
            api_key=os.environ["GEMINI_API_KEY"],
        )

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        return response.text
