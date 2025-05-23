import pandas as pd
import numpy as np

from services.DataLoader import DataLoader

class KaggleDataLoadingService(DataLoader):

    def load(self,path_to_folder:str):
        print('KaggleDataLoadingService')
        self.load_kaggle_data(path_to_folder)

    def __init__(self,path_to_kaggle_file:str,no_rows_to_analysis:int):
        self.path_to_kaggle_file = path_to_kaggle_file
        self.no_rows_to_analysis = no_rows_to_analysis

    def load_kaggle_data(self, path_to_folder:str):

        df = pd.read_csv(self.path_to_kaggle_file,sep=',')

        df['is_about_flood'] = np.where(df['label'] == 'Flood', 1, 0)

        df['message'] = (
            df['text']
            .str.replace(r'[^A-Za-z0-9# ]+', '', regex=True)
        )

        output = df[['is_about_flood','message']]

        output_subset = output.sample(n=self.no_rows_to_analysis, random_state=42)

        file_path = path_to_folder + '/kaggle_messages.csv'
        output_subset.to_csv(file_path,sep=';',quoting=1)