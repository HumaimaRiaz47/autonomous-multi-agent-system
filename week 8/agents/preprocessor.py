
from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv(override=True)

DEFAULT_MODEL_NAME = os.getenv(
    "PRICER_PREPROCESSOR_MODEL",
    "huggingface/tgi"
)

HF_TOKEN = os.getenv("HF_TOKEN")
HF_ENDPOINT = os.getenv("HF_ENDPOINT")

SYSTEM_PROMPT = """Create a concise description of a product. Respond only in this format. Do not include part numbers.
Title: Rewritten short precise title
Category: eg Electronics
Brand: Brand name
Description: 1 sentence description
Details: 1 sentence on features"""


class Preprocessor:
    def __init__(
        self,
        model_name=DEFAULT_MODEL_NAME,
        reasoning_effort=None,
        base_url=None,
    ):
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_cost = 0

        self.model_name = model_name
        self.base_url = base_url or HF_ENDPOINT

    def messages_for(self, text: str) -> list[dict]:
        return [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text},
        ]

    def preprocess(self, text: str) -> str:
        if not HF_TOKEN or not self.base_url:
            raise ValueError(
                "Set HF_TOKEN and HF_ENDPOINT in your .env"
            )

        response = completion(
            model=self.model_name,
            messages=self.messages_for(text),
            api_base=self.base_url,
            api_key=HF_TOKEN,
            max_tokens=250,
        )

        usage = response.usage
        if usage:
            self.total_input_tokens += usage.prompt_tokens or 0
            self.total_output_tokens += usage.completion_tokens or 0

        cost = response._hidden_params.get("response_cost")
        if cost is not None:
            self.total_cost += cost

        return response.choices[0].message.content
