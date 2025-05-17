import time

from models.Pipe import Pipe
from services.LabelerService import LabelerService
from services.DataDownloaderService import DataDownloaderService
from services.FloodCheckerService import FloodCheckerService

data_input_path = './Server_source/data'

dataDownloaderService = DataDownloaderService()
labelerService = LabelerService()
floodCheckerService = FloodCheckerService()

pipe_stages = [dataDownloaderService,labelerService,floodCheckerService]

pipe = Pipe(pipe_stages,data_input_path)

pipe.run_pipe()


