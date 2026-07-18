import os

from dotenv import load_dotenv
from openai import OpenAI

from reasonflow.services.llm.base import BaseLLM

load_dotenv()


class OpenAILLM(BaseLLM):
    def __init__(self):
        self.client = OpenAI(
            api_key=os.environ["OPENAI_API_KEY"],
        )

    def generate(self, prompt: str) -> str:
        response = self.client.responses.create(
            model="gpt-5-mini",
            input=prompt,
        )

        return response.output_text
