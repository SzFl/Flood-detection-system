import datetime
import os
import time
from typing import List
from models.PipeStage import PipeStage


class Pipe():

    def __init__(self,list:List[PipeStage],path_to_data_folder:str):
        self.stages = list
        self.path_to_data_folder = path_to_data_folder

    def run_pipe(self) -> None:
        start = time.time()

        x = datetime.datetime.now()
        folder_name = x.strftime("%Y-%m-%d_%H:%M:%S")

        path_to_input_folder = self.path_to_data_folder + '/' + folder_name

        try:
            os.mkdir(path_to_input_folder)
        except FileExistsError:
            print(f"Directory '{path_to_input_folder}' already exists.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{path_to_input_folder}'.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        for stage in self.stages:
            stage.flow(path_to_input_folder)
        
        end = time.time()
        print('Time pipe was operating: '+ str(end - start))