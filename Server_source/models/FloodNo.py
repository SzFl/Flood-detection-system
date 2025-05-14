from typing import Literal, Optional
from pydantic import BaseModel, Field


class FloodNo(BaseModel):
    is_flood:   Literal[False]  # only accepts False exactly :contentReference[oaicite:1]{index=1}
    reason:     Optional[str] = Field("", description="Reason why this tweet does not talk about flooding.")
    tweet_text: str

    def print(self) -> None:
        print('### FloodNo')
        print(f'is_flood: {str(self.is_flood)}')
        print(f'reason: {str(self.reason)}')
        print(f'tweet_text: {str(self.reason)}')