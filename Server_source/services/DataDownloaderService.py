from facades.RssFeedFacade import RssFeedFacade
from facades.TweeterFacade import TweeterFacade
from models.PipeStage import PipeStage
from services.DataLoader import DataLoader
from services.KaggleDataLoadingService import KaggleDataLoadingService
from services.MessagesGeneratorService import MessagesGeneratorService


class DataDownloaderService(PipeStage):

    def __init__(self,services:list[DataLoader]):
        self.loadServices = services
    
    def flow(self,path_to_input_folder):
        print('[Info][DataDownloaderService]: start')
        self.download_data(path_to_input_folder)
        print('[Info][DataDownloaderService]: end')

    def download_data(self,path_to_folder:str) -> str:
        for service in self.loadServices:
            service.load(path_to_folder)

