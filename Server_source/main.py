from models.Pipe import Pipe
from services.VerifierService import VerifierService
from services.LabelerService import LabelerService
from services.DataDownloaderService import DataDownloaderService
from services.FloodCheckerService import FloodCheckerService

data_input_path = './Server_source/data'

dataDownloaderService = DataDownloaderService()
labelerService = LabelerService()
floodCheckerService = FloodCheckerService()
verifierService = VerifierService()

pipe_stages = [dataDownloaderService,labelerService,floodCheckerService,verifierService]

pipe = Pipe(pipe_stages,data_input_path)

pipe.run_pipe()


