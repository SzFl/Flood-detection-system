from ollama import chat, ChatResponse
from pydantic import ValidationError

from models.Flood import Flood

class FloodReaderFacade():

    def ask_floodreader(self, tweet: str,chat_name) -> Flood:
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
    




