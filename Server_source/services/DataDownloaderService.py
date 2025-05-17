import datetime
import os

from facades.RssFeedFacade import RssFeedFacade
from facades.TweeterFacade import TweeterFacade
from models.PipeStage import PipeStage
from services.MessagesGeneratorService import MessagesGeneratorService


class DataDownloaderService(PipeStage):

    def __init__(self):
        self.messagesGeneratorService = MessagesGeneratorService()
        self.rssFeedFacade = RssFeedFacade()
        self.tweeterFacade = TweeterFacade()
    
    def flow(self,path_to_input_folder):
        print('[Info][DataDownloaderService]: start')
        self.download_data(path_to_input_folder)
        print('[Info][DataDownloaderService]: end')

    def download_data(self,path_to_folder:str) -> str:
        
        self.messagesGeneratorService.generate_messeges(path_to_folder)
        self.rssFeedFacade.fetch_rss_messages(path_to_folder)
        #self.tweeterFacade.download_tweets(10,path_to_folder) # Uncomment this.

