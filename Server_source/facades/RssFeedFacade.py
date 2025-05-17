import feedparser
import pandas as pd
from bs4 import BeautifulSoup
import re

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
        self.max_per_feed = 2

    def fetch_rss_messages(self,path_to_input_folder:str) -> None:
        print('[Info][RssFeedFacade]: fetch_rss_messages() start')
        messages = []

        for url in self.feed_urls:
            try:
                feed = feedparser.parse(url)

                for entry in feed.entries[:self.max_per_feed]:
                    # pick summary → description → title
                    raw_html = getattr(entry, "summary", None) \
                        or getattr(entry, "description", None) \
                        or entry.title
                    
                    cleaned_message = self.clean_html(raw_html)
                    cleaned_message = re.sub(r"[^\x20-\x7E]+", "", cleaned_message)
                    messages.append({"message": cleaned_message})

            except Exception as e:
                print(f"An error occurred: {e}")

        df = pd.DataFrame(messages, columns=["message"])

        file_path = path_to_input_folder + '/rss_messages.csv'
        df.to_csv(file_path, index=False, encoding="utf-8",sep=';', quoting=1)
        print('[Info][RssFeedFacade]: fetch_rss_messages() end')

    def clean_html(self, html_content):
        soup = BeautifulSoup(html_content, "html.parser")

        # Remove all <a> tags (links)
        for a_tag in soup.find_all("a"):
            a_tag.decompose()

        # Remove all <img> tags (images)
        for img_tag in soup.find_all("img"):
            img_tag.decompose()

        # Extract and return the cleaned text
        return soup.get_text(separator=" ", strip=True)