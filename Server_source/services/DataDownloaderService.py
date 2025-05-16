import datetime
import os

from facades.RssFeedFacade import RssFeedFacade
from facades.TweeterFacade import TweeterFacade
from services.MessagesGeneratorService import MessagesGeneratorService


class DataDownloaderService():

    def __init__(self):
        self.messagesGeneratorService = MessagesGeneratorService()
        self.rssFeedFacade = RssFeedFacade()
        self.tweeterFacade = TweeterFacade()

    def download_data(self,path_to_folder:str) -> str:
        
        x = datetime.datetime.now()
        folder_name = x.strftime("%Y-%m-%d_%H:%M:%S")

        path_to_input_folder = path_to_folder + '/' + folder_name

        try:
            os.mkdir(path_to_input_folder)
        except FileExistsError:
            print(f"Directory '{path_to_input_folder}' already exists.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{path_to_input_folder}'.")
        except Exception as e:
            print(f"An error occurred: {e}")

        self.messagesGeneratorService.generate_messeges(path_to_input_folder)
        self.rssFeedFacade.fetch_rss_messages(path_to_input_folder)
        self.tweeterFacade.download_tweets(10,path_to_input_folder)

        return path_to_input_folder
