import sys

from services.DataDownloaderService import DataDownloaderService

data_input_path = './data_input'

dataDownloaderService = DataDownloaderService()

dataDownloaderService.download_data(data_input_path)