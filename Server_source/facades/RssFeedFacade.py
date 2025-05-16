import feedparser
import pandas as pd

class RssFeedFacade():

    def __init__(self):
        self.feed_urls = [
            "https://media2.pl/rss/tag/agora.xml",
            "https://media2.pl/rss/tag/polskie-radio.xml",
            "https://next.gazeta.pl/pub/rss/rssnext.xml",
            "https://www.bankier.pl/rss/wiadomosci.xml",
            "https://www.money.pl/rss/rss.xml",
            "http://rss.gazeta.pl/pub/rss/gazetawyborcza_kraj.xml",
            "https://www.tvn24.pl/najnowsze.xml",
            "https://www.tvn24.pl/najwazniejsze.xml",
            "http://rss.gazeta.pl/pub/rss/gazetawyborcza_kraj.xml",
        ]
        self.max_per_feed = 10

    def fetch_rss_messages(self,file_path:str) -> None:

        messages = []

        for url in self.feed_urls:
            try:
                feed = feedparser.parse(url)

                for entry in feed.entries[:self.max_per_feed]:
                    # pick summary → description → title
                    msg = getattr(entry, "summary", None) \
                        or getattr(entry, "description", None) \
                        or entry.title
                    messages.append({"message": msg})

            except:
                print("An exception occurred")

        df = pd.DataFrame(messages, columns=["message"])
        df.to_csv(file_path, index=False, encoding="utf-8")