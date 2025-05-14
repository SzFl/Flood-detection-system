from typing import Literal, Optional
from pydantic import BaseModel, Field

class FloodYes(BaseModel):
    is_flood:   Literal[True]
    what:       Optional[str] = Field("", description="Short description of what happened")
    where:      Optional[str] = Field("", description="Location, if porvided")
    when:       Optional[str] = Field("", description="Time reference, if provided")
    impact:     Optional[str] = Field("", description="Short descipion of results e.g what was destroyed, if people were injured etc., if provided")
    tweet_text: str

    def print(self) -> None:
        print('### FloodYes')
        print(f'is_flood: {str(self.is_flood)}')
        print(f'what: {str(self.what)}')
        print(f'where: {str(self.where)}')
        print(f'when: {str(self.when)}')
        print(f'impact: {str(self.impact)}')
        print(f'tweet_text: {str(self.tweet_text)}')