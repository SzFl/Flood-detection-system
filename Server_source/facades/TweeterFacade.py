import os
import pandas as pd

from tweepy import Client
from dotenv import load_dotenv

class TweeterFacade():

    def __init__(self):
        load_dotenv(dotenv_path="../.env")

        developer_bearer_token = os.getenv("TWEETER_BEARER_TOKEN")

        self.client = Client(bearer_token=developer_bearer_token)

    def download_tweets(self,no_tweets:int,file_path:str) -> None:

        query = (
            "flood OR zalanie OR \"broken dam\" OR powódź OR podtopienie OR powodzie OR podtopienia"
            "context:66.850073441055133696 "
            "place_country:PL "
            "-is:retweet"
        )

        tweets = self.client.search_recent_tweets(
            query=query,
            tweet_fields=["created_at", "lang", "context_annotations"],
            expansions=["author_id"],
            user_fields=["username", "location"],
            max_results=no_tweets
        )

        texts = [t.data["text"] for t in tweets.data]

        df = pd.DataFrame(texts, columns=["text"])
        df.to_csv(file_path, index=False)
