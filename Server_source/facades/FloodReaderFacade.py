from typing import Union
from ollama import chat, ChatResponse
from pydantic import ValidationError

from models.FloodYes import FloodYes
from models.FloodNo import FloodNo

FloodResult = Union[FloodYes, FloodNo]

class FloodReaderFacade():

    def ask_floodreader(self, tweet: str) -> FloodResult:
        """
        Sends a tweet to your FloodReader model (configured with a baked-in SYSTEM prompt),
        parses the JSON reply, and validates it against FloodYes/FloodNo.
        """

        response: ChatResponse = chat(
            model='FloodReader',
            messages=[
                {
                    'role':'user',
                    'content':tweet
                }
            ],
            stream=False
        )

        raw = response.message.content.strip()

        for Model in (FloodYes, FloodNo):
            try:
                return Model.model_validate_json(raw)
            except ValidationError:
                continue
        raise ValueError(f"Output did not match any schema:\n{raw}")




