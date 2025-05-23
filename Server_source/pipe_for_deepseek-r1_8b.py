from models.Pipe import Pipe

from services.MessagesGeneratorService import MessagesGeneratorService
from facades.RssFeedFacade import RssFeedFacade
from services.KaggleDataLoadingService import KaggleDataLoadingService

from services.VerifierService import VerifierService
from services.LabelerService import LabelerService
from services.DataDownloaderService import DataDownloaderService
from services.FloodCheckerService import FloodCheckerService

# loaders preparation
messagesGeneratorService = MessagesGeneratorService(total_messages=20)
kaggle_file = './Server_source/data/kaggle_tweets_dataset.csv'
kaggleDataLoadingService = KaggleDataLoadingService(path_to_kaggle_file=kaggle_file,no_rows_to_analysis=20)

loaders = [messagesGeneratorService,kaggleDataLoadingService]

# Pipeline elements
dataDownloaderService = DataDownloaderService(loaders)
floodCheckerService = FloodCheckerService('FloodReader_deepseek-r1_8b')
verifierService = VerifierService()

# Pipe
pipe_stages = [dataDownloaderService,floodCheckerService,verifierService]

data_input_path = './Server_source/data'
pipe = Pipe(pipe_stages,data_input_path)

# Running pipe
pipe.run_pipe()