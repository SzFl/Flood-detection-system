import os
import pandas as pd

from tweepy import Client
from dotenv import load_dotenv

class TweeterFacade():

    def __init__(self):
        load_dotenv(dotenv_path=".env")

        developer_bearer_token = os.getenv("TWEETER_BEARER_TOKEN")
        developer_bearer_token = str(developer_bearer_token) if developer_bearer_token else ""
        #print('TWEETER_BEARER_TOKEN' in os.environ)

        self.client = Client(bearer_token=developer_bearer_token)

    def download_tweets(self,no_tweets:int,path_to_input_folder:str) -> None:

        query = (
            "(\"powódź\" OR \"powodzie\" OR \"zalanie\" OR \"podtopienie\" OR \"podtopienia\" OR \"flood\" OR \"floods\")"
            "context:66.850073441055133696 "
            "place_country:PL "
            "-is:retweet"
        )

        try:
            tweets = self.client.search_recent_tweets(
                query=query,
                tweet_fields=["created_at", "lang", "context_annotations"],
                expansions=["author_id"],
                user_fields=["username", "location"],
                max_results=no_tweets
            )

            texts = [t.data["text"] for t in tweets.data]

            df = pd.DataFrame(texts, columns=["text"])

            path_to_save = path_to_input_folder + '/tweeter_messages.csv'
            df.to_csv(path_to_save, index=False, sep=';', quoting=1)

        except Exception as e:
            print(f"An error occurred: {e}")
