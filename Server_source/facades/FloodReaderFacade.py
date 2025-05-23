from typing import Union
from ollama import chat, ChatResponse
from pydantic import ValidationError

from models.Flood import Flood
from models.FloodYes import FloodYes
from models.FloodNo import FloodNo

FloodResult = Union[FloodYes, FloodNo]

class FloodReaderFacade():

    def ask_floodreader(self, tweet: str,chat_name) -> FloodResult:
        """
        Sends a tweet to your FloodReader model (configured with a baked-in SYSTEM prompt),
        parses the JSON reply, and validates it against FloodYes/FloodNo.
        """

        response: ChatResponse = chat(
            model=chat_name,
            messages=[
                {
                    'role':'user',
                    'content':tweet
                }
            ],
            stream=False,
            format=Flood.model_json_schema()
        )

        raw = response.message.content.strip()

        return Flood.model_validate_json(raw)
    




