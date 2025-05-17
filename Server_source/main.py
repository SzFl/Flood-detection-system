import sys
import time

from services.LabelerService import LabelerService
from services.DataDownloaderService import DataDownloaderService
from services.FloodCheckerService import FloodCheckerService

verify = False
data_input_path = './Server_source/data_input'

start = time.time()

dataDownloaderService = DataDownloaderService()

path_to_input_folder = dataDownloaderService.download_data(data_input_path)

labelerService = LabelerService()
floodCheckerService = FloodCheckerService()

if verify:
    labelerService.label_tweets(path_to_input_folder)
    labelerService.label_rss(path_to_input_folder)
    floodCheckerService.indentify(path_to_input_folder)
else:
    floodCheckerService.indentify(path_to_input_folder)



end = time.time()
print(end - start)