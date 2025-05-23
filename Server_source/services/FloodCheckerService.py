from os import listdir
from os.path import isfile, join

import pandas as pd

from models.PipeStage import PipeStage
from models.FloodNo import FloodNo
from models.FloodYes import FloodYes
from facades.FloodReaderFacade import FloodReaderFacade

class FloodCheckerService(PipeStage):

    def __init__(self,chat_name:str):
         self.floodReaderFacade = FloodReaderFacade()
         self.chat_name = chat_name

    def flow(self,path_to_input_folder:str):
        print('[Info][FloodCheckerService]: start')
        self.indentify(path_to_input_folder)
        print('[Info][FloodCheckerService]: end')

    def indentify(self,path_to_input_folder:str):
        files = [f for f in listdir(path_to_input_folder) if isfile(join(path_to_input_folder, f))]

        for file in files:
            self.indentify_for_file(path_to_input_folder,file) 

    def indentify_for_file(self,path_to_input_folder:str,file_name:str):
        print(f'[Info][FloodCheckerService] indentify_for_file() Starts: {file_name}')
        path_to_input_file = path_to_input_folder+'/'+file_name

        message = 'default'

        try:
            df = pd.read_csv(path_to_input_file,sep=';')

            predictions = []
            responses = []
            
            for index, row in df.iterrows():
                print(f'[Info][FloodCheckerService] indentify_for_file() {index}')
                message = row['message']
                response = self.floodReaderFacade.ask_floodreader(message,self.chat_name)

                if response.is_flood:
                    predictions.append("1")
                else:
                    predictions.append("0")

                responses.append(response)
            
            df.insert(loc = 0, column = 'predictions', value = predictions)
            df.to_csv(path_to_input_file, index=False, encoding="utf-8",sep=';', quoting=1)

            resp_df = pd.DataFrame([response.to_dict() for response in responses])
            resp_path = path_to_input_folder+'/'+file_name[:-4] + '_response.csv'
            resp_df.to_csv(resp_path, index=False, encoding="utf-8",sep=';', quoting=1)

            print(f'[Info][FloodCheckerService] indentify_for_file() Ends: {file_name}')

        except Exception as e:
            print(f'[Erro][FloodCheckerService] indentify_for_file() {e}') 
            print(f'Message: \"{message}\"')
            print(f'[Info][FloodCheckerService] indentify_for_file() Ends: {file_name}')